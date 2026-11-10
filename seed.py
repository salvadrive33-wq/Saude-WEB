"""Dados FICTÍCIOS de demonstração. Nenhum dado real de pacientes ou profissionais."""
from db import q, init_db
from app import insert  # noqa: E402  (reaproveita o helper de insert)


def run():
    units = [
        ("Hospital Municipal (DEMO)", "Hospital", "Centro, Ibiassucê - BA", "24 horas", "Urgência, Clínica geral, Exames", -14.2736, -42.2186, 1, 1, 0),
        ("UBS Centro (DEMO)", "UBS", "Rua Principal, Centro", "Seg a Sex, 7h às 17h", "Consultas, Vacinação, Pré-natal", -14.2712, -42.2201, 1, 1, 1),
        ("UBS Bairro Novo (DEMO)", "UBS", "Bairro Novo", "Seg a Sex, 8h às 16h", "Consultas, Odontologia", -14.2781, -42.2152, 1, 0, 0),
    ]
    uid = [insert("units", dict(name=n, type=t, address=a, hours=h, services=s, docs="Documento com foto e Cartão SUS",
                                lat=la, lng=ln, ramp=r, wc=w, libras=l, active=1)) for n, t, a, h, s, la, ln, r, w, l in units]
    sid = {n: insert("specialties", {"name": n}) for n in ("Clínico geral", "Pediatria", "Odontologia")}
    docs = [("Dra. Ana (DEMO)", "Clínico geral", uid[1], [0, 2, 4]), ("Dr. Paulo (DEMO)", "Pediatria", uid[0], [1, 3]),
            ("Dra. Carla (DEMO)", "Odontologia", uid[2], [0, 1, 3])]
    for name, spec, u, days in docs:
        did = insert("doctors", {"name": name, "specialty_id": sid[spec], "active": 1})
        q("INSERT INTO doctor_units(doctor_id,unit_id) VALUES(?,?)", (did, u), commit=True)
        for wd in days:
            insert("availabilities", dict(doctor_id=did, unit_id=u, weekday=wd, starts="08:00", ends="12:00", slot_minutes=30))
    insert("campaigns", dict(title="Campanha de demonstração", body="Texto fictício de uma campanha de saúde.", day=None, created_at="2026-10-01"))


if __name__ == "__main__":
    from app import app
    with app.app_context():
        init_db()
        run()
