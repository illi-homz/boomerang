#!/bin/bash

source /home/www/boomerang/env/bin/activate
exec gunicorn  -c "/home/www/boomerang/gunicorn_config.py" project.wsgi
