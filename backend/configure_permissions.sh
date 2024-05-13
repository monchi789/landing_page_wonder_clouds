#!/bin/bash

mkdir -p /var/lib/pgadmin/sessions
chown -R pgadmin:pgadmin /var/lib/pgadmin/sessions
chmod -R 755 /var/lib/pgadmin/sessions
chmod +x configure_permissions.sh
