#!/bin/sh
ENV="$1"
shift
PRODUCTION="production"
DEVELOPMENT="development"

wait_for_db() {
    wait-for-it.sh -h db -p 5432 -t 30
    echo "Database is ready!"
}

if [ "$ENV" = "$PRODUCTION" ]; then
    wait_for_db

    python3 manage.py migrate
    python3 manage.py collectstatic --noinput
fi

if [ "$ENV" = "$DEVELOPMENT" ]; then
    wait_for_db

    python3 manage.py migrate
    python3 manage.py loaddata initial_data.json
    python3 manage.py loaddata initial_user.json
fi

exec "$@"
