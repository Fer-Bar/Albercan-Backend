#!/bin/bash

python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', 'password_secret')" | python manage.py shell

python manage.py collectstatic --no-input

python manage.py runserver 0.0.0.0:8000
