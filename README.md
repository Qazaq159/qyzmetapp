

Required environmental variabels

- DJANGO_SETTINGS_MODULE
variables possible values:
    qyzmetapp.settings.test - Postgres DB, debug True
    qyzmetapp.settings.local - Sqlite DB, debug True
    qyzmetapp.settings.relase - Postgres DB, debug False


- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT

default envvars for local

export DJANGO_SETTINGS_MODULE=qyzmetapp.settings.test
export DB_NAME=qyzmetdb
export DB_USER=qyzmetuser
export DB_PASSWORD=qYzmetaPP2025
export DB_HOST=localhost
export DB_PORT=5432
