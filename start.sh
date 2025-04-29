#!/bin/bash

cd qyzmetapp
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn qyzmetapp.wsgi:application --timeout 100 --log-level=debug --bind 0.0.0.0:8000
