#!/bin/sh
ENV="$1"
shift
PRODUCTION="production"
DEVELOPMENT="development"

if [ "$ENV" = "$PRODUCTION" ]; then
    python3 manage.py migrate
    python3 manage.py collectstatic --noinput
fi

if [ "$ENV" = "$DEVELOPMENT" ]; then
    python3 manage.py migrate
    python3 manage.py loaddata initial_data.json
    python3 manage.py loaddata initial_user.json
fi

exec "$@"
