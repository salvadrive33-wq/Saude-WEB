"""Saúde Ibiassucê: backend Flask (API pública, API administrativa e entrega das páginas)."""
import logging, os, re, secrets, time
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import Flask, jsonify, make_response, request, session
from werkzeug.exceptions import HTTPException
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import check_password_hash, generate_password_hash
import db
from db import INTEGRITY, q
from web_assets import FILES

STATUSES = ("agendada", "confirmada", "concluida", "cancelada")
FAILS = {}  # tentativas de login por IP (memória; suficiente para 1 servidor)


class ApiError(Exception):
    def __init__(self, msg, code=400):
        self.msg, self.code = msg, code


def now_local():
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("America/Bahia"))
    except Exception:
        return datetime.now(timezone(timedelta(hours=-3)))


def clean(data, spec, partial=False):
    """Valida e converte campos conforme spec {campo: (tipo, obrigatorio, tamanho_max)}."""
    out = {}
    for k, (t, req, *mx) in spec.items():
        if partial and k not in data:
            continue
        v = data.get(k)
        if v is None or v == "":
            if req:
                raise ApiError(f"Campo obrigatório: {k}")
            out[k] = (1 if k == "active" else 0) if t == "bool" else None  # novos registros nascem ativos
            continue
        try:
            if t == "str":
                v = str(v).strip()
                if len(v) > (mx[0] if mx else 200):
                    raise ValueError
            elif t == "int":
                v = int(v)
            elif t == "bool":
                v = 1 if v in (True, 1, "1", "true") else 0
            elif t == "lat":
                v = float(v); assert -90 <= v <= 90
            elif t == "lng":
                v = float(v); assert -180 <= v <= 180
            elif t == "date":
                datetime.strptime(str(v), "%Y-%m-%d"); v = str(v)
            elif t == "time":
                datetime.strptime(str(v), "%H:%M"); v = str(v)
        except (ValueError, TypeError, AssertionError):
            raise ApiError(f"Valor inválido em: {k}")
        out[k] = v
    return out


def insert(table, d):
    return q(f"INSERT INTO {table}({','.join(d)}) VALUES({','.join('?' * len(d))}) RETURNING id",
             list(d.values()), commit=True)[0]["id"]


def update(table, rid, d):
    if d:
        q(f"UPDATE {table} SET {','.join(k + '=?' for k in d)} WHERE id=?", [*d.values(), rid], commit=True)


def minutes(hhmm):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def free_slots(doctor_id, unit_id, day):
    """Horários livres: faixas cadastradas menos reservas ativas e horários que já passaram."""
    d = datetime.strptime(day, "%Y-%m-%d").date()
    now = now_local()
    if d < now.date():
        return []
    ok = q("""SELECT 1 FROM doctors d JOIN doctor_units du ON du.doctor_id=d.id JOIN units u ON u.id=du.unit_id
              WHERE d.id=? AND u.id=? AND d.active=1 AND u.active=1""", (doctor_id, unit_id))
    if not ok:
        return []
    taken = {r["slot"] for r in q("SELECT slot FROM appointments WHERE doctor_id=? AND day=? AND status<>'cancelada'",
                                  (doctor_id, day))}
    limit = now.hour * 60 + now.minute if d == now.date() else -1
    out = []
    for a in q("SELECT starts,ends,slot_minutes FROM availabilities WHERE doctor_id=? AND unit_id=? AND weekday=? ORDER BY starts",
               (doctor_id, unit_id, d.weekday())):
        t = minutes(a["starts"])
        while t + a["slot_minutes"] <= minutes(a["ends"]):
            hhmm = f"{t // 60:02d}:{t % 60:02d}"
            if hhmm not in taken and t > limit:
                out.append(hhmm)
            t += a["slot_minutes"]
    return out


def admin_required(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        if not session.get("admin_id"):
            raise ApiError("Faça login para continuar.", 401)
        return fn(*a, **kw)
    return wrapper


UNIT = {"name": ("str", True, 120), "type": ("str", True, 30), "address": ("str", True, 200),
        "phone": ("str", False, 30), "hours": ("str", False, 120), "services": ("str", False, 300),
        "docs": ("str", False, 300), "lat": ("lat", False), "lng": ("lng", False), "ramp": ("bool", False),
        "wc": ("bool", False), "libras": ("bool", False), "active": ("bool", False)}
DOCTOR = {"name": ("str", True, 120), "specialty_id": ("int", True), "active": ("bool", False)}
AVAIL = {"doctor_id": ("int", True), "unit_id": ("int", True), "weekday": ("int", True), "starts": ("time", True),
         "ends": ("time", True), "slot_minutes": ("int", False)}
CAMP = {"title": ("str", True, 120), "body": ("str", True, 600), "day": ("date", False)}


def create_app(test_config=None):
    app = Flask(__name__, static_folder=None)  # arquivos servidos por rota própria (lista permitida)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)
    app.config.update(
        DATABASE_URL=os.getenv("DATABASE_URL"), SQLITE_PATH=os.getenv("SQLITE_PATH", "local.db"),
        SECRET_KEY=os.getenv("SECRET_KEY"), SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=os.getenv("COOKIE_SECURE", "1") == "1", PERMANENT_SESSION_LIFETIME=timedelta(hours=8),
        _ready=False)
    if test_config:
        app.config.update(test_config)
    if not app.config["SECRET_KEY"]:
        app.config["SECRET_KEY"] = secrets.token_hex(32)
        logging.warning("SECRET_KEY não definida: sessões serão perdidas a cada reinicialização.")
    app.teardown_appcontext(db.close_db)

    @app.before_request
    def prepare():
        if not app.config["_ready"] and request.path.startswith("/api/"):
            db.init_db()
            bootstrap()
            app.config["_ready"] = True
        if request.path.startswith("/api/admin") and request.method != "GET" \
                and request.headers.get("X-Requested-With") != "fetch":
            raise ApiError("Requisição inválida.", 400)

    def bootstrap():
        email, pw = os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD")
        if email and pw and not q("SELECT 1 FROM admins"):
            if len(pw) < 10:
                logging.error("ADMIN_PASSWORD precisa ter 10+ caracteres; conta não criada.")
            else:
                insert("admins", {"email": email.strip().lower(), "password_hash": generate_password_hash(pw)})
        if os.getenv("SEED_DEMO") == "1" and not q("SELECT 1 FROM units"):
            import seed
            seed.run()

    @app.errorhandler(ApiError)
    def api_error(e):
        return jsonify(error=e.msg), e.code

    @app.errorhandler(404)
    def not_found(_):
        return (jsonify(error="Não encontrado."), 404) if request.path.startswith("/api/") else ("Página não encontrada.", 404)

    @app.errorhandler(Exception)
    def crash(e):
        if isinstance(e, HTTPException):
            return jsonify(error=e.description), e.code
        logging.exception(e)
        return jsonify(error="Erro interno. Tente novamente em instantes."), 500

    # ---------- páginas ----------
    MIME = {"html": "text/html", "css": "text/css", "js": "text/javascript"}

    def serve(name):
        resp = make_response(FILES[name])
        resp.headers["Content-Type"] = MIME[name.rsplit(".", 1)[1]] + "; charset=utf-8"
        resp.headers["Cache-Control"] = "no-cache"
        return resp

    @app.get("/")
    def page_public():
        return serve("public.html")

    @app.get("/admin")
    def page_admin():
        return serve("admin.html")

    @app.get("/static/<name>")
    def asset(name):
        if name not in FILES or name.endswith(".html"):  # só estilos e scripts; nunca código Python
            raise ApiError("Não encontrado.", 404)
        return serve(name)

    # ---------- API pública ----------
    @app.get("/api/health")
    def health():
        q("SELECT 1")
        return jsonify(ok=True)

    @app.get("/api/units")
    def units():
        term = f"%{request.args.get('q', '').strip().lower()}%"
        return jsonify(q("""SELECT * FROM units WHERE active=1 AND
                 (lower(name) LIKE ? OR lower(address) LIKE ? OR lower(coalesce(services,'')) LIKE ?) ORDER BY name""",
                         (term, term, term)))

    @app.get("/api/specialties")
    def specialties():
        return jsonify(q("SELECT * FROM specialties ORDER BY name"))

    @app.get("/api/doctors")
    def doctors():
        sql, args = """SELECT d.id,d.name,d.active,d.specialty_id,s.name AS specialty FROM doctors d
                       JOIN specialties s ON s.id=d.specialty_id WHERE 1=1""", []
        if request.args.get("public", "1") == "1":
            sql += " AND d.active=1"
        if request.args.get("unit_id"):
            sql += " AND d.id IN (SELECT doctor_id FROM doctor_units WHERE unit_id=?)"; args.append(request.args["unit_id"])
        if request.args.get("specialty_id"):
            sql += " AND d.specialty_id=?"; args.append(request.args["specialty_id"])
        docs = q(sql + " ORDER BY d.name", args)
        today = now_local().strftime("%Y-%m-%d")
        for d in docs:
            d["units"] = q("""SELECT u.id AS unit_id,u.name AS unit_name,
                (SELECT 1 FROM presence p WHERE p.doctor_id=du.doctor_id AND p.unit_id=du.unit_id AND p.day=?) AS presence_today
                FROM doctor_units du JOIN units u ON u.id=du.unit_id WHERE du.doctor_id=?""" + (" AND u.active=1" if request.args.get("public", "1") == "1" else ""), (today, d["id"]))
            for u in d["units"]:
                u["presence_today"] = bool(u["presence_today"])
                u["availabilities"] = q("""SELECT weekday,starts,ends,slot_minutes FROM availabilities
                    WHERE doctor_id=? AND unit_id=? ORDER BY weekday,starts""", (d["id"], u["unit_id"]))
        return jsonify(docs)

    @app.get("/api/slots")
    def slots():
        c = clean(request.args, {"doctor_id": ("int", True), "unit_id": ("int", True), "day": ("date", True)})
        return jsonify(free_slots(c["doctor_id"], c["unit_id"], c["day"]))

    @app.get("/api/campaigns")
    def campaigns():
        return jsonify(q("SELECT * FROM campaigns ORDER BY id DESC"))

    @app.post("/api/appointments")
    def book():
        c = clean(request.get_json(silent=True) or {}, {"doctor_id": ("int", True), "unit_id": ("int", True),
                  "day": ("date", True), "slot": ("time", True), "patient_name": ("str", True, 80)})
        if len(c["patient_name"]) < 2:
            raise ApiError("Informe um nome com pelo menos 2 letras.")
        if c["slot"] not in free_slots(c["doctor_id"], c["unit_id"], c["day"]):
            raise ApiError("Horário indisponível. Escolha outro horário.", 409)
        code = secrets.token_hex(3).upper()
        try:
            insert("appointments", {**c, "code": code, "status": "agendada", "created_at": now_local().isoformat(timespec="seconds")})
        except INTEGRITY:
            raise ApiError("Este horário acabou de ser reservado. Escolha outro.", 409)
        info = q("""SELECT d.name AS doctor,s.name AS specialty,u.name AS unit FROM doctors d
                    JOIN specialties s ON s.id=d.specialty_id JOIN units u ON u.id=? WHERE d.id=?""",
                 (c["unit_id"], c["doctor_id"]))[0]
        return jsonify(code=code, day=c["day"], slot=c["slot"], demo=True, **info), 201

    # ---------- autenticação ----------
    @app.post("/api/admin/login")
    def login():
        ip, now = request.remote_addr, time.time()
        FAILS[ip] = [t for t in FAILS.get(ip, []) if now - t < 300]
        if len(FAILS[ip]) >= 5:
            raise ApiError("Muitas tentativas. Aguarde 5 minutos.", 429)
        d = request.get_json(silent=True) or {}
        row = q("SELECT * FROM admins WHERE email=?", (str(d.get("email", "")).strip().lower(),))
        if not row or not check_password_hash(row[0]["password_hash"], str(d.get("password", ""))):
            FAILS[ip].append(now)
            raise ApiError("E-mail ou senha incorretos.", 401)
        session.clear(); session.permanent = True; session["admin_id"] = row[0]["id"]
        return jsonify(ok=True, email=row[0]["email"])

    @app.post("/api/admin/logout")
    def logout():
        session.clear()
        return jsonify(ok=True)

    @app.get("/api/admin/me")
    @admin_required
    def me():
        return jsonify(q("SELECT id,email FROM admins WHERE id=?", (session["admin_id"],))[0])

    # ---------- API administrativa ----------
    @app.get("/api/admin/stats")
    @admin_required
    def stats():
        n = lambda sql, a=(): q(sql, a)[0]["n"]
        today = now_local().strftime("%Y-%m-%d")
        return jsonify(
            units=n("SELECT count(*) AS n FROM units WHERE active=1"), doctors=n("SELECT count(*) AS n FROM doctors WHERE active=1"),
            appointments=n("SELECT count(*) AS n FROM appointments"),
            today=n("SELECT count(*) AS n FROM appointments WHERE day=? AND status<>'cancelada'", (today,)),
            by_status={r["status"]: r["n"] for r in q("SELECT status,count(*) AS n FROM appointments GROUP BY status")},
            recent=q("""SELECT a.id,a.code,a.day,a.slot,a.status,a.patient_name,d.name AS doctor,u.name AS unit FROM appointments a
                        JOIN doctors d ON d.id=a.doctor_id JOIN units u ON u.id=a.unit_id ORDER BY a.id DESC LIMIT 8"""))

    def crud(path, table, spec, extra=None):
        """Registra GET/POST/PUT/DELETE administrativos para uma tabela simples."""
        def lst():
            return jsonify(q(f"SELECT * FROM {table} ORDER BY id DESC"))

        def add():
            d = clean(request.get_json(silent=True) or {}, spec)
            try:
                rid = insert(table, d)
            except INTEGRITY:
                raise ApiError("Registro duplicado ou relacionamento inválido.", 409)
            return jsonify(id=rid), 201

        def edit(rid):
            d = clean(request.get_json(silent=True) or {}, spec, partial=True)
            try:
                update(table, rid, d)
            except INTEGRITY:
                raise ApiError("Registro duplicado ou relacionamento inválido.", 409)
            return jsonify(ok=True)

        def remove(rid):
            if table in ("units", "doctors") and q(f"SELECT 1 FROM appointments WHERE {table[:-1]}_id=? LIMIT 1", (rid,)):
                raise ApiError("Há agendamentos vinculados. Desative o registro em vez de remover.", 409)
            q(f"DELETE FROM {table} WHERE id=?", (rid,), commit=True)
            return jsonify(ok=True)
        for name, fn, meth, url in (("lst", lst, "GET", ""), ("add", add, "POST", ""), ("edit", edit, "PUT", "/<int:rid>"),
                                    ("remove", remove, "DELETE", "/<int:rid>")):
            app.add_url_rule(f"/api/admin/{path}{url}", f"{path}_{name}", admin_required(fn), methods=[meth])

    crud("units", "units", UNIT)
    crud("doctors", "doctors", DOCTOR)
    crud("campaigns", "campaigns", CAMP)
    crud("specialties", "specialties", {"name": ("str", True, 80)})

    @app.put("/api/admin/doctors/<int:rid>/units")
    @admin_required
    def doctor_units(rid):
        ids = {int(x) for x in (request.get_json(silent=True) or {}).get("unit_ids", [])}
        q("DELETE FROM doctor_units WHERE doctor_id=? AND unit_id NOT IN (%s)" % ",".join("?" * len(ids) or "0"),
          [rid, *ids] if ids else [rid], commit=True)
        for u in ids:
            if not q("SELECT 1 FROM doctor_units WHERE doctor_id=? AND unit_id=?", (rid, u)):
                try:
                    q("INSERT INTO doctor_units(doctor_id,unit_id) VALUES(?,?)", (rid, u), commit=True)
                except INTEGRITY:
                    raise ApiError("Médico ou unidade inexistente.", 409)
        return jsonify(ok=True)

    @app.get("/api/admin/availabilities")
    @admin_required
    def av_list():
        return jsonify(q("""SELECT a.*,d.name AS doctor,u.name AS unit FROM availabilities a JOIN doctors d ON d.id=a.doctor_id
                            JOIN units u ON u.id=a.unit_id ORDER BY d.name,a.weekday,a.starts"""))

    def check_av(d, own_id=0):
        if not 0 <= d["weekday"] <= 6 or minutes(d["ends"]) <= minutes(d["starts"]):
            raise ApiError("Horário final deve ser depois do inicial e o dia deve estar entre 0 e 6.")
        for o in q("SELECT id,starts,ends FROM availabilities WHERE doctor_id=? AND weekday=? AND id<>?",
                   (d["doctor_id"], d["weekday"], own_id)):
            if minutes(d["starts"]) < minutes(o["ends"]) and minutes(o["starts"]) < minutes(d["ends"]):
                raise ApiError("Conflito: o médico já tem horário cadastrado nesse período.", 409)

    @app.post("/api/admin/availabilities")
    @admin_required
    def av_add():
        d = clean(request.get_json(silent=True) or {}, AVAIL)
        d["slot_minutes"] = d["slot_minutes"] or 30
        check_av(d)
        try:
            return jsonify(id=insert("availabilities", d)), 201
        except INTEGRITY:
            raise ApiError("Associe o médico à unidade antes de cadastrar horários.", 409)

    @app.put("/api/admin/availabilities/<int:rid>")
    @admin_required
    def av_edit(rid):
        cur = q("SELECT * FROM availabilities WHERE id=?", (rid,))
        if not cur:
            raise ApiError("Não encontrado.", 404)
        d = {**cur[0], **clean(request.get_json(silent=True) or {}, AVAIL, partial=True)}
        check_av(d, rid)
        update("availabilities", rid, {k: d[k] for k in ("weekday", "starts", "ends", "slot_minutes")})
        return jsonify(ok=True)

    @app.delete("/api/admin/availabilities/<int:rid>")
    @admin_required
    def av_del(rid):
        q("DELETE FROM availabilities WHERE id=?", (rid,), commit=True)
        return jsonify(ok=True)

    @app.post("/api/admin/presence")
    @admin_required
    def presence_set():
        c = clean(request.get_json(silent=True) or {}, {"doctor_id": ("int", True), "unit_id": ("int", True), "day": ("date", True)})
        q("DELETE FROM presence WHERE doctor_id=? AND unit_id=? AND day=?", (c["doctor_id"], c["unit_id"], c["day"]), commit=True)
        if (request.get_json(silent=True) or {}).get("confirmed") is False:
            return jsonify(ok=True)
        try:
            q("INSERT INTO presence VALUES(?,?,?,?)", (c["doctor_id"], c["unit_id"], c["day"], now_local().isoformat(timespec="seconds")), commit=True)
        except INTEGRITY:
            raise ApiError("Médico ou unidade inexistente.", 409)
        return jsonify(ok=True)

    @app.get("/api/admin/appointments")
    @admin_required
    def appts():
        sql, args = """SELECT a.id,a.code,a.day,a.slot,a.status,a.patient_name,a.created_at,a.doctor_id,a.unit_id,
            d.name AS doctor,s.name AS specialty,u.name AS unit FROM appointments a JOIN doctors d ON d.id=a.doctor_id
            JOIN specialties s ON s.id=d.specialty_id JOIN units u ON u.id=a.unit_id WHERE 1=1""", []
        for key, col in (("unit_id", "a.unit_id"), ("doctor_id", "a.doctor_id"), ("day", "a.day"), ("status", "a.status")):
            if request.args.get(key):
                sql += f" AND {col}=?"; args.append(request.args[key])
        return jsonify(q(sql + " ORDER BY a.day DESC,a.slot DESC LIMIT 500", args))

    @app.put("/api/admin/appointments/<int:rid>")
    @admin_required
    def appt_status(rid):
        st = (request.get_json(silent=True) or {}).get("status")
        if st not in STATUSES:
            raise ApiError("Situação inválida.")
        try:
            q("UPDATE appointments SET status=? WHERE id=?", (st, rid), commit=True)
        except INTEGRITY:
            raise ApiError("Conflito: o horário já foi reservado por outro agendamento ativo.", 409)
        return jsonify(ok=True)

    return app


app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
