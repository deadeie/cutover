"""SQLite local persistence adapter. Domain rules live in workflow.py."""
import json
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("CUTOVER_DB", ROOT / "data" / "cutover.sqlite3"))


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@contextmanager
def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def init():
    with connect() as db:
        db.executescript("""
        CREATE TABLE IF NOT EXISTS routers(
          id INTEGER PRIMARY KEY, project TEXT NOT NULL, province TEXT NOT NULL,
          site TEXT NOT NULL, center TEXT NOT NULL, topology TEXT NOT NULL,
          name TEXT DEFAULT '', om_ip TEXT DEFAULT '', installed_at TEXT NOT NULL,
          created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS requests(
          id INTEGER PRIMARY KEY, router_id INTEGER NOT NULL REFERENCES routers(id),
          stage TEXT NOT NULL, state TEXT NOT NULL, created_at TEXT NOT NULL,
          claimed_by TEXT DEFAULT '', claimed_at TEXT DEFAULT '', submitted_by TEXT NOT NULL,
          note TEXT DEFAULT ''
        );
        CREATE TABLE IF NOT EXISTS events(
          id INTEGER PRIMARY KEY, router_id INTEGER, request_id INTEGER,
          at TEXT NOT NULL, actor TEXT NOT NULL, action TEXT NOT NULL, detail TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS plans(
          id INTEGER PRIMARY KEY, week TEXT NOT NULL, router_id INTEGER NOT NULL REFERENCES routers(id),
          planned_executor TEXT DEFAULT '', actual_executor TEXT DEFAULT '',
          state TEXT NOT NULL DEFAULT 'Planned', note TEXT DEFAULT '', created_at TEXT NOT NULL,
          execution_at TEXT DEFAULT ''
        );
        CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY, value TEXT NOT NULL);
        """)
        for key, value in {"temp_observation_hours":"48", "handover_wait_hours":"48", "atp_validity_days":"30"}.items():
            db.execute("INSERT OR IGNORE INTO settings(key,value) VALUES(?,?)", (key,value))
        if db.execute("SELECT COUNT(*) FROM routers").fetchone()[0] == 0:
            seed(db)


def seed(db):
    # Synthetic records make the first local launch useful for a flow walkthrough.
    items = [
        ("پروژه شمال", "TH", "TH1234", "مرکز نمونه یک", "RSG", "BRJHFA_TH1234", "10.10.1.2"),
        ("پروژه شمال", "TH", "TH2345", "مرکز نمونه دو", "ASG", "BAIMKG_TH2345", "10.10.1.3"),
        ("پروژه غرب", "HJ", "HJ1111", "مرکز نمونه سه", "RSG", "BARSTGU_HJ1111", "10.20.1.2"),
    ]
    for project, province, site, center, topology, name, ip in items:
        cur = db.execute("INSERT INTO routers(project,province,site,center,topology,name,om_ip,installed_at,created_at) VALUES(?,?,?,?,?,?,?,?,?)", (project,province,site,center,topology,name,ip,now(),now()))
        rid=cur.lastrowid
        if rid == 1:
            db.execute("INSERT INTO requests(router_id,stage,state,created_at,submitted_by,note) VALUES(?,?,?,?,?,?)",(rid,"QA","Queued",now(),"راه‌اندازی پروژه","نمونهٔ نمایشی"))
        event(db,rid,None,"سامانه","ایجاد رکورد",f"رکورد نمونه {name}")


def event(db, router_id, request_id, actor, action, detail):
    db.execute("INSERT INTO events(router_id,request_id,at,actor,action,detail) VALUES(?,?,?,?,?,?)", (router_id,request_id,now(),actor,action,detail))


def state():
    with connect() as db:
        # Materialize the confirmed ATP renewal task when an uncut router's
        # latest approval has expired. Refreshing the local app reevaluates it.
        validity=int(db.execute("SELECT value FROM settings WHERE key='atp_validity_days'").fetchone()[0])
        for row in db.execute("SELECT r.id, a.created_at FROM routers r JOIN requests a ON a.router_id=r.id AND a.stage='ATP' AND a.state IN ('Approved','Conditional') WHERE NOT EXISTS (SELECT 1 FROM plans p WHERE p.router_id=r.id AND p.state='Completed') AND a.id=(SELECT MAX(a2.id) FROM requests a2 WHERE a2.router_id=r.id AND a2.stage='ATP' AND a2.state IN ('Approved','Conditional'))"):
            if datetime.fromisoformat(row[1])+timedelta(days=validity)<=datetime.now(timezone.utc) and not db.execute("SELECT 1 FROM requests WHERE router_id=? AND stage='ATP' AND state IN ('Queued','Claimed','Correction')",(row[0],)).fetchone():
                cur=db.execute("INSERT INTO requests(router_id,stage,state,created_at,submitted_by,note) VALUES(?,?,?,?,?,?)",(row[0],"ATP","Queued",now(),"سامانه","تمدید خودکار ATP منقضی‌شده"))
                event(db,row[0],cur.lastrowid,"سامانه","ایجاد تمدید ATP","اعتبار ATP منقضی شد؛ Cutover نیازمند تأیید مجدد است")
        routers=[dict(x) for x in db.execute("SELECT * FROM routers ORDER BY id DESC")]
        requests=[dict(x) for x in db.execute("SELECT q.*,r.name,r.site,r.center,r.project,r.province,r.topology FROM requests q JOIN routers r ON r.id=q.router_id ORDER BY q.id DESC")]
        plans=[dict(x) for x in db.execute("SELECT p.*,r.name,r.site,r.center,r.project,r.province FROM plans p JOIN routers r ON r.id=p.router_id ORDER BY p.week,p.id")]
        events=[dict(x) for x in db.execute("SELECT e.*,r.name,r.site FROM events e LEFT JOIN routers r ON r.id=e.router_id ORDER BY e.id DESC LIMIT 80")]
        settings={r[0]:r[1] for r in db.execute("SELECT key,value FROM settings").fetchall()}
        return {"routers":routers,"requests":requests,"plans":plans,"events":events,"settings":settings}
