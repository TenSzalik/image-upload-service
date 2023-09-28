#!/bin/sh
ENV="$1"
shift
PRODUCTION="production"
DEVELOPMENT="development"

if [ "$ENV" = "$PRODUCTION" ]; then
    python3 manage.py migrate
    python3 manage.py collectstatic --noinput
    python3 manage.py create_system_user
    python3 manage.py trycreatesuperuser
fi

if [ "$ENV" = "$DEVELOPMENT" ]; then
    python3 manage.py migrate
    python3 manage.py loaddata initial_data.json
fi

exec "$@"
