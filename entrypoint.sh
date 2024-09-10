#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn 'my_site.wsgi:application' --bind :$PORT