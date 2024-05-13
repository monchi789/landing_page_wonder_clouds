#!/bin/sh

# Espera a que la base de datos esté disponible
python3 manage.py wait_for_db

# Realiza las migraciones
python3 manage.py makemigrations
python3 manage.py migrate

# Imprimo un mensaje
echo "Servidor Levantado"
