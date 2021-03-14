#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py loaddata initial_data.json
exec "$@"