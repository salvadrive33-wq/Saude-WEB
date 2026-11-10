import os, sys, tempfile, unittest
from datetime import timedelta
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.update(ADMIN_EMAIL="admin@teste.com", ADMIN_PASSWORD="senha-segura-123", SEED_DEMO="1")
from app import create_app, now_local  # noqa: E402

H = {"X-Requested-With": "fetch"}


def next_weekday(wd):
    d = now_local().date() + timedelta(days=1)
    while d.weekday() != wd:
        d += timedelta(days=1)
    return d.strftime("%Y-%m-%d")


class Api(unittest.TestCase):
    def setUp(self):
        self.f = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.app = create_app({"TESTING": True, "SQLITE_PATH": self.f.name, "SESSION_COOKIE_SECURE": False, "DATABASE_URL": None})
        self.c = self.app.test_client()
        self.c.get("/api/health")  # inicializa banco, admin e dados de demonstração

    def tearDown(self):
        os.unlink(self.f.name)

    def login(self, pw="senha-segura-123"):
        return self.c.post("/api/admin/login", json={"email": "admin@teste.com", "password": pw}, headers=H)

    def pick(self):
        d = self.c.get("/api/doctors").json[0]  # Dra. Ana: UBS Centro, Seg/Qua/Sex
        return d["id"], d["units"][0]["unit_id"], next_weekday(d["units"][0]["availabilities"][0]["weekday"])

    def book(self, did, uid, day, slot, name="Visitante Teste"):
        return self.c.post("/api/appointments", json=dict(doctor_id=did, unit_id=uid, day=day, slot=slot, patient_name=name))

    def test_public_data_comes_from_db(self):
        self.assertEqual(len(self.c.get("/api/units").json), 3)
        self.assertEqual(len(self.c.get("/api/units?q=odonto").json), 1)

    def test_booking_and_conflict(self):
        did, uid, day = self.pick()
        slots = self.c.get(f"/api/slots?doctor_id={did}&unit_id={uid}&day={day}").json
        self.assertEqual(slots[:2], ["08:00", "08:30"])
        r = self.book(did, uid, day, "08:00"); self.assertEqual(r.status_code, 201); self.assertTrue(r.json["demo"])
        self.assertEqual(self.book(did, uid, day, "08:00").status_code, 409)
        self.assertNotIn("08:00", self.c.get(f"/api/slots?doctor_id={did}&unit_id={uid}&day={day}").json)

    def test_invalid_booking(self):
        did, uid, day = self.pick()
        self.assertEqual(self.book(did, uid, day, "23:00").status_code, 409)  # fora da faixa
        self.assertEqual(self.book(did, uid, "2020-01-01", "08:00").status_code, 409)  # data passada
        self.assertEqual(self.book(did, uid, day, "08:00", "A").status_code, 400)  # nome curto

    def test_admin_requires_auth(self):
        for path in ("/api/admin/stats", "/api/admin/units", "/api/admin/appointments"):
            self.assertEqual(self.c.get(path).status_code, 401)
        self.assertEqual(self.c.post("/api/admin/units", json={"name": "x"}, headers=H).status_code, 401)
        self.assertEqual(self.login("errada").status_code, 401)

    def test_csrf_header_required(self):
        self.login()
        self.assertEqual(self.c.post("/api/admin/units", json={"name": "x"}).status_code, 400)

    def test_admin_changes_reach_public_and_cancel_frees_slot(self):
        self.assertEqual(self.login().status_code, 200)
        r = self.c.post("/api/admin/units", json=dict(name="Nova UBS (DEMO)", type="UBS", address="Rua X", lat=-14.27, lng=-42.22), headers=H)
        self.assertEqual(r.status_code, 201)
        self.assertEqual(len(self.c.get("/api/units").json), 4)
        self.c.put(f"/api/admin/units/{r.json['id']}", json={"active": False}, headers=H)
        self.assertEqual(len(self.c.get("/api/units").json), 3)
        did, uid, day = self.pick()
        ap = self.book(did, uid, day, "09:00")
        self.assertEqual(self.c.get("/api/admin/stats").json["appointments"], 1)
        aid = self.c.get("/api/admin/appointments").json[0]["id"]
        self.c.put(f"/api/admin/appointments/{aid}", json={"status": "cancelada"}, headers=H)
        self.assertEqual(self.book(did, uid, day, "09:00").status_code, 201)
        self.assertEqual(self.c.put(f"/api/admin/appointments/{aid}", json={"status": "agendada"}, headers=H).status_code, 409)

    def test_availability_conflict_and_unit_with_appointments(self):
        self.login()
        did, uid, day = self.pick()
        wd = [a for a in self.c.get("/api/admin/availabilities").json if a["doctor_id"] == did][0]["weekday"]
        body = dict(doctor_id=did, unit_id=uid, weekday=wd, starts="11:00", ends="13:00")
        self.assertEqual(self.c.post("/api/admin/availabilities", json=body, headers=H).status_code, 409)
        body.update(starts="14:00", ends="16:00")
        self.assertEqual(self.c.post("/api/admin/availabilities", json=body, headers=H).status_code, 201)
        self.book(did, uid, day, "08:00")
        self.assertEqual(self.c.delete(f"/api/admin/units/{uid}", headers=H).status_code, 409)

    def test_presence_toggle(self):
        self.login(); did, uid, _ = self.pick(); day = now_local().strftime("%Y-%m-%d")
        self.c.post("/api/admin/presence", json=dict(doctor_id=did, unit_id=uid, day=day), headers=H)
        self.assertTrue(self.c.get("/api/doctors").json[0]["units"][0]["presence_today"])
        self.c.post("/api/admin/presence", json=dict(doctor_id=did, unit_id=uid, day=day, confirmed=False), headers=H)
        self.assertFalse(self.c.get("/api/doctors").json[0]["units"][0]["presence_today"])

    def test_only_listed_files_are_public(self):
        self.assertEqual(self.c.get("/static/theme.css").status_code, 200)
        for name in ("app.py", "db.py", ".env", "test_api.py", "local.db"):
            self.assertEqual(self.c.get("/static/" + name).status_code, 404)
        self.assertEqual(self.c.get("/").status_code, 200)
        self.assertEqual(self.c.get("/admin").status_code, 200)

    def test_persistence_after_restart(self):
        did, uid, day = self.pick(); self.book(did, uid, day, "10:00")
        app2 = create_app({"TESTING": True, "SQLITE_PATH": self.f.name, "SESSION_COOKIE_SECURE": False})
        c2 = app2.test_client(); c2.get("/api/health")
        self.assertNotIn("10:00", c2.get(f"/api/slots?doctor_id={did}&unit_id={uid}&day={day}").json)


if __name__ == "__main__":
    unittest.main()
