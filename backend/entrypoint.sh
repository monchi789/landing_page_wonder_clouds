#!/bin/sh
set -e

# Espera a que la base de datos esté disponible en el puerto 5432
until ncat -z -w 2 db 5432; do
  echo "Esperando a que la base de datos esté disponible..."
  sleep 2
done

# Ejecuta las migraciones de Django
python manage.py migrate

# Inicia el servidor Django
exec "$@"
