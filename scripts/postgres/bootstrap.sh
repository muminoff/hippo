#!/bin/bash

set -e

dropdb hippo
dropuser hippo
createuser -s hippo
createdb -O hippo hippo

python hippo/manage.py migrate
python hippo/manage.py loaddata hippo/fixtures/services.json
python hippo/manage.py loaddata hippo/fixtures/users.json
