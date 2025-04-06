#!/bin/sh

echo "🐍 Aplicando migraciones..."
python manage.py makemigrations
python manage.py migrate

echo "🚀 Levantando el servidor en 0.0.0.0:8000..."
python manage.py runserver 0.0.0.0:8000
