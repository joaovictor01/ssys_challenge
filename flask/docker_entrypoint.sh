#!/usr/bin/env bash
export FLASK_APP=main.py
# export FLASK_ENV=development
# flask db init
# flask db migrate
# flask db upgrade

# export FLASK_APP=main.py
export FLASK_ENV=production
uwsgi app.ini