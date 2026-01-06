#!/bin/sh


echo "migrate...."
python manage.py migrate --noipoint

echo "collect statics...."
python manage.py collectstatic --noipoint

echo "starting gunicorn"
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000