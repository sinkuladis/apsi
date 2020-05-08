#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
mkdir apsi_backend/static
python manage.py generateschema --format openapi --title 'FakeOlx' --description 'Endpoints to use' > apsi_backend/static/schema.yml

exec "$@"