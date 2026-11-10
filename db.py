"""Acesso ao banco. PostgreSQL (Neon) em produção; SQLite local para desenvolvimento e testes."""
import sqlite3
from flask import current_app, g

try:
    import psycopg2, psycopg2.extras
    INTEGRITY = (sqlite3.IntegrityError, psycopg2.IntegrityError)
except ImportError:  # psycopg2 só é necessário quando DATABASE_URL está definida
    psycopg2 = None
    INTEGRITY = (sqlite3.IntegrityError,)

SCHEMA = [
 """CREATE TABLE IF NOT EXISTS units(id {pk}, name TEXT NOT NULL, type TEXT NOT NULL, address TEXT NOT NULL,
    phone TEXT, hours TEXT, services TEXT, docs TEXT, lat REAL, lng REAL,
    ramp INTEGER NOT NULL DEFAULT 0, wc INTEGER NOT NULL DEFAULT 0, libras INTEGER NOT NULL DEFAULT 0,
    active INTEGER NOT NULL DEFAULT 1)""",
 "CREATE TABLE IF NOT EXISTS specialties(id {pk}, name TEXT NOT NULL UNIQUE)",
 """CREATE TABLE IF NOT EXISTS doctors(id {pk}, name TEXT NOT NULL,
    specialty_id INTEGER NOT NULL REFERENCES specialties(id), active INTEGER NOT NULL DEFAULT 1,
    UNIQUE(name, specialty_id))""",
 """CREATE TABLE IF NOT EXISTS doctor_units(doctor_id INTEGER NOT NULL REFERENCES doctors(id) ON DELETE CASCADE,
    unit_id INTEGER NOT NULL REFERENCES units(id) ON DELETE CASCADE, PRIMARY KEY(doctor_id, unit_id))""",
 """CREATE TABLE IF NOT EXISTS availabilities(id {pk}, doctor_id INTEGER NOT NULL, unit_id INTEGER NOT NULL,
    weekday INTEGER NOT NULL CHECK(weekday BETWEEN 0 AND 6), starts TEXT NOT NULL, ends TEXT NOT NULL,
    slot_minutes INTEGER NOT NULL DEFAULT 30 CHECK(slot_minutes BETWEEN 10 AND 120),
    UNIQUE(doctor_id, unit_id, weekday, starts),
    FOREIGN KEY(doctor_id, unit_id) REFERENCES doctor_units(doctor_id, unit_id) ON DELETE CASCADE)""",
 """CREATE TABLE IF NOT EXISTS presence(doctor_id INTEGER NOT NULL REFERENCES doctors(id) ON DELETE CASCADE,
    unit_id INTEGER NOT NULL REFERENCES units(id) ON DELETE CASCADE, day TEXT NOT NULL, confirmed_at TEXT NOT NULL,
    PRIMARY KEY(doctor_id, unit_id, day))""",
 """CREATE TABLE IF NOT EXISTS appointments(id {pk}, code TEXT NOT NULL UNIQUE,
    doctor_id INTEGER NOT NULL REFERENCES doctors(id), unit_id INTEGER NOT NULL REFERENCES units(id),
    day TEXT NOT NULL, slot TEXT NOT NULL, patient_name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'agendada', created_at TEXT NOT NULL)""",
 # impede duas reservas ativas para o mesmo médico, dia e horário (mesmo com cliques simultâneos)
 """CREATE UNIQUE INDEX IF NOT EXISTS uq_appt_active ON appointments(doctor_id, day, slot)
    WHERE status <> 'cancelada'""",
 "CREATE TABLE IF NOT EXISTS campaigns(id {pk}, title TEXT NOT NULL, body TEXT NOT NULL, day TEXT, created_at TEXT NOT NULL)",
 "CREATE TABLE IF NOT EXISTS admins(id {pk}, email TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL)",
]

def is_pg():
    return bool(current_app.config.get("DATABASE_URL"))

def get_db():
    if "db" not in g:
        if is_pg():
            g.db = psycopg2.connect(current_app.config["DATABASE_URL"], connect_timeout=20,
                                    cursor_factory=psycopg2.extras.RealDictCursor)
        else:
            g.db = sqlite3.connect(current_app.config["SQLITE_PATH"])
            g.db.row_factory = sqlite3.Row
            g.db.execute("PRAGMA foreign_keys=ON")
    return g.db

def close_db(_=None):
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()

def q(sql, params=(), commit=False):
    """Executa SQL com placeholders '?' (convertidos para %s no PostgreSQL). Retorna lista de dicts."""
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute(sql.replace("?", "%s") if is_pg() else sql, tuple(params))
        rows = [dict(r) for r in cur.fetchall()] if cur.description else []
        if commit:
            conn.commit()
        return rows
    except Exception:
        conn.rollback()
        raise

def init_db():
    pk = "SERIAL PRIMARY KEY" if is_pg() else "INTEGER PRIMARY KEY AUTOINCREMENT"
    for stmt in SCHEMA:
        q(stmt.format(pk=pk), commit=True)
