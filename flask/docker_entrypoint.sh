#!/usr/bin/env bash
export FLASK_APP=main.py
export FLASK_ENV=production
uwsgi app.ini