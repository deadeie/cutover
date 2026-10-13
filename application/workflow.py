"""Business workflow rules, independent from HTTP and persistence details."""
from datetime import datetime, timedelta, timezone
import re
from . import store

STAGES=("QA","TEMP","ATP","HANDOVER")
LABELS={"QA":"کنترل کیفیت","TEMP":"دما","ATP":"تأیید آمادگی","HANDOVER":"تحویل"}


def act(data):
    if not isinstance(data, dict):
        raise ValueError("ساختار درخواست معتبر نیست.")
    kind=data.get("action","")
    actor=(data.get("actor") or "کاربر نمایشی").strip()[:80]
    with store.connect() as db:
        # Serialize validation and mutation across tabs/HTTP workers.
        db.execute("BEGIN IMMEDIATE")
        if kind=="router.create":
            data = dict(data)
            for key in ("province", "site", "topology", "name"):
                data[key] = str(data.get(key, "")).strip().upper()
            if not re.fullmatch(r"[A-Z]{2}(?:[0-9]{4}|X[0-9]{3})", data["site"]):
                raise ValueError("کد سایت باید مانند GL0012 یا GLX012 باشد.")
            if data["province"] != data["site"][:2]:
                raise ValueError("کد استان با کد سایت مطابقت ندارد.")
            if data["topology"] not in ("RSG", "ASG", "CSG"):
                raise ValueError("توپولوژی معتبر نیست.")
            required=["project","province","site","center","topology"]
            if any(not str(data.get(k,"")).strip() for k in required): raise ValueError("فیلدهای پروژه، استان، کد سایت، مرکز و توپولوژی الزامی‌اند.")
            siblings=db.execute("SELECT id FROM routers WHERE UPPER(province)=UPPER(?) AND UPPER(site)=UPPER(?)",(data["province"].strip(),data["site"].strip())).fetchall()
            if siblings and data.get("duplicate_site_confirmed") not in (True, "true"):
                raise ValueError("برای این کد سایت قبلاً روتر ثبت شده؛ اگر روتر دوم همین مرکز است، ثبت جداگانه را تأیید کنید.")
            if data["name"] and db.execute("SELECT 1 FROM routers WHERE UPPER(TRIM(name))=? AND UPPER(TRIM(site))=?", (data["name"], data["site"])).fetchone():
                raise ValueError("این روتر با همین نام در این سایت قبلاً ثبت شده است.")
            cur=db.execute("INSERT INTO routers(project,province,site,center,topology,name,om_ip,installed_at,created_at) VALUES(?,?,?,?,?,?,?,?,?)",(data["project"].strip(),data["province"].upper(),data["site"].upper(),data["center"].strip(),data["topology"],data.get("name","").upper(),data.get("om_ip","").strip(),store.now(),store.now()))
            store.event(db,cur.lastrowid,None,actor,"ثبت روتر",data["site"])
        elif kind=="request.create":
            rid=int(data["router_id"]); stage=data["stage"]
            if stage not in STAGES: raise ValueError("مرحله نامعتبر است.")
            r=db.execute("SELECT * FROM routers WHERE id=?",(rid,)).fetchone()
            if not r: raise ValueError("روتر پیدا نشد.")
            if stage=="QA":
                prior=db.execute("SELECT 1 FROM requests WHERE router_id=? AND stage='QA'",(rid,)).fetchone()
                if prior:
                    raise ValueError("برای این رکورد روتر قبلاً QA ثبت شده است. اگر QA برگشت خورده، همان درخواست را پس از اصلاح دوباره ارسال کنید؛ برای روتر دوم، رکورد جدا بسازید.")
                peer=db.execute("SELECT 1 FROM routers WHERE province=? AND site=? AND topology=? AND id<>?",(r["province"],r["site"],r["topology"],rid)).fetchone()
                if peer and data.get("plane") not in ("A","B"):
                    raise ValueError("برای روتر دوم هم‌توپولوژی در همین سایت، هنگام QA مشخص کنید روتر A است یا B.")
                peers=db.execute("SELECT q.* FROM requests q JOIN routers r2 ON r2.id=q.router_id WHERE r2.site=? AND r2.topology=? AND r2.id<>? AND q.stage='QA'", (r["site"],r["topology"],rid)).fetchall()
                for previous in peers:
                    if previous["plane"] == data.get("plane"):
                        raise ValueError("این پلین قبلاً برای روتر دیگری در همین سایت و توپولوژی ثبت شده است.")
                    if not previous["plane"]:
                        other=data.get("peer_plane")
                        if other not in ("A","B") or other==data.get("plane"):
                            raise ValueError("پلین روتر اول را هم صریحاً تأیید کنید؛ دو روتر نباید پلین یکسان داشته باشند.")
                        db.execute("UPDATE requests SET plane=? WHERE id=?", (other,previous["id"]))
                        store.event(db,previous["router_id"],previous["id"],actor,"تأیید پلین روتر اول",other)
            plane=data.get("plane","") if stage=="QA" else ""
            approved={x[0] for x in db.execute("SELECT stage FROM requests WHERE router_id=? AND state IN ('Approved','Conditional')",(rid,))}
            if stage in approved:
                raise ValueError("این مرحله قبلاً تأیید شده؛ درخواست جدید مجاز نیست. تمدید ATP از صف عملیات پیگیری می‌شود.")
            prereq={"QA":set(),"TEMP":{"QA"},"ATP":{"QA","TEMP"},"HANDOVER":{"QA","TEMP","ATP"}}[stage]
            if not prereq.issubset(approved): raise ValueError("پیش‌نیازهای این مرحله هنوز تأیید نشده‌اند.")
            if stage=="QA" and not r["installed_at"]: raise ValueError("ابتدا نصب روتر را ثبت کنید.")
            if stage=="HANDOVER":
                plan=db.execute("SELECT created_at FROM plans WHERE router_id=? AND state='Completed' ORDER BY id DESC LIMIT 1",(rid,)).fetchone()
                if not plan: raise ValueError("برای این نمونه ابتدا Cutover را با موفقیت ثبت کنید.")
                hours=int(db.execute("SELECT value FROM settings WHERE key='handover_wait_hours'").fetchone()[0])
                completed=db.execute("SELECT execution_at FROM plans WHERE router_id=? AND state='Completed' ORDER BY id DESC LIMIT 1",(rid,)).fetchone()
                if not completed[0] or datetime.fromisoformat(completed[0]) + timedelta(hours=hours)>datetime.now(timezone.utc): raise ValueError(f"مهلت انتظار Handover هنوز تمام نشده است ({hours} ساعت).")
            if db.execute("SELECT 1 FROM requests WHERE router_id=? AND stage=? AND state IN ('Queued','Claimed','Correction')",(rid,stage)).fetchone(): raise ValueError("برای این مرحله درخواست فعال وجود دارد.")
            cur=db.execute("INSERT INTO requests(router_id,stage,state,created_at,submitted_by,note,plane) VALUES(?,?,?,?,?,?,?)",(rid,stage,"Queued",store.now(),actor,data.get("note","")[:500],plane))
            store.event(db,rid,cur.lastrowid,actor,"ثبت درخواست",f"{LABELS[stage]}{f' · روتر {plane}' if plane else ''}")
        elif kind in ("request.claim","request.approve","request.return"):
            qid=int(data["request_id"]); q=db.execute("SELECT * FROM requests WHERE id=?",(qid,)).fetchone()
            if not q: raise ValueError("درخواست پیدا نشد.")
            if kind=="request.claim":
                if q["state"]!="Queued": raise ValueError("این درخواست در صف قابل Claim نیست.")
                db.execute("UPDATE requests SET state='Claimed',claimed_by=?,claimed_at=? WHERE id=?",(actor,store.now(),qid)); event="Claim درخواست"
            else:
                if q["state"]!="Claimed": raise ValueError("فقط درخواست Claim‌شده قابل بررسی است.")
                if kind=="request.return" and not str(data.get("note", "")).strip():
                    raise ValueError("علت برگشت برای اصلاح الزامی است.")
                if kind=="request.approve" and q["stage"]=="TEMP":
                    hours=int(db.execute("SELECT value FROM settings WHERE key='temp_observation_hours'").fetchone()[0])
                    ready=datetime.fromisoformat(q["created_at"])+timedelta(hours=hours)
                    if ready>datetime.now(timezone.utc): raise ValueError(f"دورهٔ مشاهدهٔ دما تمام نشده؛ تأیید بعد از {fmt_remaining(ready)} ممکن می‌شود.")
                new="Approved" if kind=="request.approve" else "Correction"
                db.execute("UPDATE requests SET state=?,note=? WHERE id=?",(new,data.get("note","")[:500],qid)); event="تأیید مرحله" if new=="Approved" else "بازگشت برای اصلاح"
            store.event(db,q["router_id"],qid,actor,event,data.get("note",LABELS[q["stage"]]))
        elif kind=="plan.create":
            rid=int(data["router_id"]); week=data["week"]
            if not db.execute("SELECT 1 FROM routers WHERE id=?",(rid,)).fetchone(): raise ValueError("روتر پیدا نشد.")
            cur=db.execute("INSERT INTO plans(week,router_id,planned_executor,created_at) VALUES(?,?,?,?)",(week,rid,data.get("planned_executor","").strip(),store.now()))
            store.event(db,rid,None,actor,"افزودن به برنامهٔ هفتگی",f"هفته {week}; مجری برنامه: {data.get('planned_executor') or 'تعیین نشده'}")
        elif kind=="plan.execute":
            pid=int(data["plan_id"]); plan=db.execute("SELECT * FROM plans WHERE id=?",(pid,)).fetchone()
            if not plan: raise ValueError("ردیف برنامه پیدا نشد.")
            approved={x[0] for x in db.execute("SELECT stage FROM requests WHERE router_id=? AND state IN ('Approved','Conditional')",(plan["router_id"],))}
            if not {"QA","TEMP","ATP"}.issubset(approved): raise ValueError("اجرای Cutover مسدود است: QA، دما و ATP باید تأیید شده باشند.")
            atp=db.execute("SELECT created_at FROM requests WHERE router_id=? AND stage='ATP' AND state IN ('Approved','Conditional') ORDER BY id DESC LIMIT 1",(plan["router_id"],)).fetchone()
            validity=int(db.execute("SELECT value FROM settings WHERE key='atp_validity_days'").fetchone()[0])
            if not atp or datetime.fromisoformat(atp[0])+timedelta(days=validity)<=datetime.now(timezone.utc):
                if not db.execute("SELECT 1 FROM requests WHERE router_id=? AND stage='ATP' AND state IN ('Queued','Claimed','Correction')",(plan["router_id"],)).fetchone():
                    cur=db.execute("INSERT INTO requests(router_id,stage,state,created_at,submitted_by,note) VALUES(?,?,?,?,?,?)",(plan["router_id"],"ATP","Queued",store.now(),"سامانه","تمدید خودکار ATP منقضی‌شده"))
                    store.event(db,plan["router_id"],cur.lastrowid,"سامانه","ایجاد تمدید ATP","اعتبار ATP برای Cutover منقضی یا ناموجود است")
                db.commit()
                raise ValueError("اجرای Cutover مسدود است: ATP معتبر نیست؛ درخواست تمدید در صف عملیات ثبت شد.")
            db.execute("UPDATE plans SET state='Completed',actual_executor=?,note=?,execution_at=? WHERE id=?",(data.get("actual_executor","").strip(),data.get("note","")[:500],store.now(),pid))
            store.event(db,plan["router_id"],None,actor,"ثبت موفق Cutover",f"مجری واقعی: {data.get('actual_executor') or 'ثبت نشده'}")
        elif kind=="settings.save":
            for key in ("temp_observation_hours","handover_wait_hours","atp_validity_days"):
                val=int(data[key])
                if not 0<=val<=8760: raise ValueError("مقادیر تنظیمات باید بین صفر تا ۸۷۶۰ باشند.")
                db.execute("INSERT INTO settings(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",(key,str(val)))
            store.event(db,None,None,actor,"تغییر تنظیمات زمان", "تنظیمات محلی فرایند")
        elif kind=="request.resubmit":
            qid=int(data["request_id"]); q=db.execute("SELECT * FROM requests WHERE id=?",(qid,)).fetchone()
            if not q or q["state"]!="Correction": raise ValueError("فقط درخواست برگشتی قابل ارسال مجدد است.")
            if not str(data.get("note", "")).strip():
                raise ValueError("شرح اصلاح انجام‌شده الزامی است.")
            if q["stage"]=="TEMP":
                db.execute("UPDATE requests SET created_at=? WHERE id=?",(store.now(),qid))
            db.execute("UPDATE requests SET state='Queued',claimed_by='',claimed_at='',note=? WHERE id=?",(data["note"].strip()[:500],qid))
            store.event(db,q["router_id"],qid,actor,"ارسال مجدد پس از اصلاح",data.get("note","")[:500])
        else: raise ValueError("عملیات ناشناخته است.")
    return store.state()


def fmt_remaining(ready):
    seconds=max(0,int((ready-datetime.now(timezone.utc)).total_seconds()))
    return f"{seconds//3600} ساعت و {(seconds%3600)//60} دقیقهٔ دیگر"
