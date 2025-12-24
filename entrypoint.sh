#!/bin/sh


echo "migrate...."
pyhon manage.py migrate --noipoint

echo "collect statics...."
pyhon manage.py collectstatic --noipoint

echo "starting gunicorn"
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000