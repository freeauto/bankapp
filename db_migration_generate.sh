#!/usr/bin/env bash

source _include.sh || exit 1

if [ -z "$1" ]; then
  echo "Please enter some description of the revision."
  exit 1
fi

rm alembic/versions/*.pyc
alembic revision --autogenerate -m "$*"
