#!/bin/sh
python manage.py migrate
python manage.py shell < populate_db.py
gunicorn -b 0.0.0.0:8000 localee.wsgi
