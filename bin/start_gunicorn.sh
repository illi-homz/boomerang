#!/bin/bash

source /home/il/github/boomerang/env/bin/activate
exec gunicorn  -c "/home/il/github/boomerang/gunicorn_config.py" wsgi
