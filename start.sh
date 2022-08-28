#!/bin/bash

python manage.py runserver
/Applications/Chromium.app/Contents/MacOS/Chromium --incognito --start-maximized --kiosk --app='http://localhost:8000/'

