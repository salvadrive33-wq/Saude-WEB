# Saúde Ibiassucê: sistema web (feira de ciências)

App público para tablet (`/`) e painel administrativo para computador (`/admin`), com o mesmo backend Flask e o mesmo banco PostgreSQL.
Todos os agendamentos são **de demonstração**. Não cadastre dados reais de pacientes.

## Arquivos
Só 7 arquivos na raiz do repositório, sem pastas: `app.py` (backend), `db.py`, `seed.py`, `test_api.py`, `web_assets.py` (páginas e estilos do sistema, gerado automaticamente), `requirements.txt` e `README.md`.

## Arquitetura
- Um único serviço **Flask** (Render, plano gratuito) entrega as páginas e a API.
- Banco **PostgreSQL no Neon** (plano gratuito). Localmente, sem `DATABASE_URL`, usa SQLite.
- Mapa: Leaflet + OpenStreetMap (sem chave de API; precisa de internet).

## Rodar localmente (opcional)
```
pip install -r requirements.txt
export SEED_DEMO=1 COOKIE_SECURE=0 ADMIN_EMAIL=admin@feira.com ADMIN_PASSWORD=uma-senha-longa
python -c "from app import app; app.run()"
```
Abra http://127.0.0.1:5000 e http://127.0.0.1:5000/admin. Testes: `python -m unittest test_api`.

## Publicar (tudo gratuito)
1. **GitHub:** crie um repositório e envie o conteúdo desta pasta. Nunca envie um arquivo `.env`.
2. **Neon** (neon.com): crie um projeto (região mais próxima disponível) e copie a *connection string* (`postgresql://...`). Ela contém a senha: trate como segredo.
3. **Render** (render.com, entre com o GitHub): New > Web Service > escolha o repositório.
   - Language: Python 3 · Instance Type: **Free**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --timeout 120`
4. **Environment Variables** no Render:

| Variável | Valor |
|---|---|
| `DATABASE_URL` | connection string do Neon |
| `SECRET_KEY` | texto aleatório longo (40+ caracteres), só seu |
| `ADMIN_EMAIL` | e-mail do administrador |
| `ADMIN_PASSWORD` | senha com 10+ caracteres (não reutilize outra senha) |
| `SEED_DEMO` | `1` (carrega dados fictícios se o banco estiver vazio) |
| `COOKIE_SECURE` | `1` |
| `PYTHON_VERSION` | `3.12.3` |

5. **Conferir:** abra `https://SEU-SERVICO.onrender.com/api/health`. Deve aparecer `{"ok":true}`. Depois abra `/` e `/admin`.
   O primeiro acesso após inatividade pode levar cerca de 1 minuto.
6. **Atualizar:** envie as mudanças ao GitHub; o Render publica de novo sozinho.
- A conta de administrador só é criada se ainda não existir nenhuma. Mudar `ADMIN_EMAIL`/`ADMIN_PASSWORD` depois não altera a conta existente.

## Roteiro de demonstração (todos os dados fictícios, com "(DEMO)" no nome)
1. Chromebook: abrir `/admin` e entrar.
2. Unidades: cadastrar "UBS Feira (DEMO)" com endereço e coordenadas.
3. Médicos: cadastrar "Dr. Feira (DEMO)", escolher especialidade e marcar a unidade.
4. Horários: criar um horário para o dia da apresentação e confirmar a presença.
5. Tablet: abrir `/`, consultar a unidade e o médico (Serviços > Unidades / Médicos).
6. Tablet: Agendar consulta e conferir o código de confirmação.
7. Chromebook: Agendamentos, achar o código e confirmar a consulta.

## Antes da apresentação
- 10 minutos antes: abra os dois endereços para "acordar" o servidor e o banco.
- No tablet: Serviços > Ajustes > **Testar conexão**.
- Teste na rede da escola: o site, o mapa (precisa carregar os mapas do OpenStreetMap) e as fontes do Google.
- Guarde a senha do administrador. Sem internet, o sistema não funciona.

## Limitações
- Plano gratuito: servidor dorme após 15 min sem uso; banco pode demorar alguns segundos para acordar.
- Uma única conta de administrador, criada pelas variáveis de ambiente.
- Não há backup automático: se precisar, exporte pelo painel do Neon.
