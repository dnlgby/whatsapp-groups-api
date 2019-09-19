#!/usr/bin/env bash

set -e

PROJECT_MANAGE_PATH='/usr/local/apps/whatsapp_groups_api/app'

git pull
$PROJECT_MANAGE_PATH/env/bin/python manage.py migrate
$PROJECT_MANAGE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart app

echo "DONE! :)"
