#!/bin/bash
set -e

echo "Applying migrations"
python manage.py migrate

#echo "Collecting static"
#python manage.py collectstatic --noinput

echo "Starting app"
python manage.py runserver
