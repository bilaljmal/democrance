#!/bin/bash
/opt/venv/bin/python manage.py collectstatic  --noinput
/opt/venv/bin/python manage.py migrate  --noinput
APP_PORT=${PORT:-8000}
cd /neksio/

/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm main.wsgi:application --bind "0.0.0.0:${APP_PORT}"





