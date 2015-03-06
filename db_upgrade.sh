#!/usr/bin/env bash

source _include.sh || exit 1

if [ "$1" == "prod" ]; then
  echo "=== PRODUCTION: migrating up"
  # alembic -c alembic_prod.ini upgrade +1 # upgrades by one migration
  alembic -c alembic_prod.ini upgrade head # upgrades to latest
else
  echo "=== LOCALDEV: migrating up"
  # alembic upgrade +1 # upgrades by one migration
  alembic upgrade head # upgrades to latest
fi
