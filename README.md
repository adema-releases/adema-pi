# ADEMA Pi Django Bootstrap

Minimal Django application ready for deployment on ADEMA Pi (Raspberry Pi OS / Debian 12).

## Quick start

```bash
# 1. Clone
git clone <repo-url> ademapi && cd ademapi

# 2. Virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux / macOS / Raspberry Pi OS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Environment
cp .env.example .env
# edit .env to set SECRET_KEY, DEBUG, ALLOWED_HOSTS, database values

# 5. Django setup
python manage.py migrate
python manage.py collectstatic --no-input

# 6. Development server
python manage.py runserver 0.0.0.0:8000
```

## Environment variables

| Variable | Description | Default |
| --- | --- | --- |
| `SECRET_KEY` | Django secret key | `django-insecure-change-me` |
| `DEBUG` | Enables debug mode when `True` | `False` |
| `ALLOWED_HOSTS` | Comma-separated hostnames | `127.0.0.1,localhost` |
| `ADEMA_DB_ENGINE` | `sqlite` or `postgres` | `sqlite` |
| `ADEMA_DB_NAME` | Postgres database name | `ademapi` |
| `ADEMA_DB_USER` | Postgres user | `ademapi` |
| `ADEMA_DB_PASSWORD` | Postgres password | `ademapi` |
| `ADEMA_DB_HOST` | Postgres host | `localhost` |
| `ADEMA_DB_PORT` | Postgres port | `5432` |

## Deployment notes

1. Apply migrations and collect static files before starting gunicorn.
2. Example gunicorn command:
   ```bash
   gunicorn ademapi.wsgi:application --bind 0.0.0.0:8000 --workers 3
   ```
3. Configure nginx to proxy traffic to gunicorn and serve `staticfiles/`.
