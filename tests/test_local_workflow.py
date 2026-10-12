import tempfile
import unittest
from pathlib import Path
from application import store, workflow


class LocalWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old_path = store.DB_PATH
        store.DB_PATH = Path(self.tmp.name) / "test.sqlite3"
        store.init()

    def tearDown(self):
        store.DB_PATH = self.old_path
        self.tmp.cleanup()

    def act(self, action, **kwargs):
        return workflow.act({"action": action, "actor": "آزمون", **kwargs})

    def approve(self, request_id):
        self.act("request.claim", request_id=request_id)
        self.act("request.approve", request_id=request_id)

    def newest_request(self, stage):
        return max((q for q in store.state()["requests"] if q["stage"] == stage), key=lambda q:q["id"])["id"]

    def fresh_router_id(self):
        return max(r["id"] for r in store.state()["routers"])

    def test_stage_gates_temp_observation_and_cutover_executor(self):
        state = store.state()
        rid = self.fresh_router_id()
        with self.assertRaisesRegex(ValueError, "پیش‌نیاز"):
            self.act("request.create", router_id=rid, stage="ATP")
        self.act("request.create", router_id=rid, stage="QA")
        qa = self.newest_request("QA")
        self.approve(qa)
        self.act("request.create", router_id=rid, stage="TEMP")
        temp = self.newest_request("TEMP")
        self.act("request.claim", request_id=temp)  # Work can proceed during observation.
        with self.assertRaisesRegex(ValueError, "دورهٔ مشاهده"):
            self.act("request.approve", request_id=temp)
        self.act("settings.save", temp_observation_hours=0, handover_wait_hours=0, atp_validity_days=30)
        self.act("request.approve", request_id=temp)
        self.act("request.create", router_id=rid, stage="ATP")
        atp = self.newest_request("ATP")
        self.approve(atp)
        plan = self.act("plan.create", router_id=rid, week="2026-10-12", planned_executor="مجری برنامه")
        pid = plan["plans"][-1]["id"]
        self.act("plan.execute", plan_id=pid, actual_executor="مجری واقعی")
        done = next(p for p in store.state()["plans"] if p["id"] == pid)
        self.assertEqual(done["planned_executor"], "مجری برنامه")
        self.assertEqual(done["actual_executor"], "مجری واقعی")
        handover = self.act("request.create", router_id=rid, stage="HANDOVER")
        self.assertTrue(any(q["stage"] == "HANDOVER" for q in handover["requests"]))

    def test_cutover_blocks_until_prerequisites_and_adds_atp_renewal(self):
        rid = self.fresh_router_id()
        pid = self.act("plan.create", router_id=rid, week="2026-10-12")["plans"][-1]["id"]
        with self.assertRaisesRegex(ValueError, "QA.*ATP"):
            self.act("plan.execute", plan_id=pid)

    def test_expired_atp_materializes_operations_renewal_task(self):
        rid = self.fresh_router_id()
        self.act("settings.save", temp_observation_hours=0, handover_wait_hours=48, atp_validity_days=0)
        # Mark all three gates approved to reach ATP expiry behavior.
        self.act("request.create", router_id=rid, stage="QA")
        self.approve(self.newest_request("QA"))
        self.act("request.create", router_id=rid, stage="TEMP")
        self.approve(self.newest_request("TEMP"))
        self.act("request.create", router_id=rid, stage="ATP")
        self.approve(self.newest_request("ATP"))
        renewals=[q for q in store.state()["requests"] if q["stage"]=="ATP" and q["state"]=="Queued"]
        self.assertEqual(len(renewals),1)
        self.assertIn("تمدید", renewals[0]["note"])

    def test_qa_is_once_per_router_but_second_same_site_router_is_allowed(self):
        first = self.fresh_router_id()
        self.act("request.create", router_id=first, stage="QA")
        self.approve(self.newest_request("QA"))
        with self.assertRaisesRegex(ValueError, "قبلاً QA ثبت شده"):
            self.act("request.create", router_id=first, stage="QA")
        source=next(r for r in store.state()["routers"] if r["id"]==first)
        details={"project":source["project"],"province":source["province"],"site":source["site"],"center":"روتر دوم همان مرکز","topology":source["topology"]}
        with self.assertRaisesRegex(ValueError, "روتر دوم"):
            self.act("router.create", **details)
        details["duplicate_site_confirmed"]=True
        self.act("router.create", **details)
        second=self.fresh_router_id()
        with self.assertRaisesRegex(ValueError, "مشخص کنید روتر A است یا B"):
            self.act("request.create", router_id=second, stage="QA")
        result=self.act("request.create", router_id=second, stage="QA", plane="B")
        self.assertTrue(any(q["router_id"]==second and q["plane"]=="B" for q in result["requests"]))


if __name__ == "__main__":
    unittest.main()
