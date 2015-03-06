#!/usr/bin/env bash

source venv/bin/activate

if [[ "$OSTYPE" == "darwin"*  ]]; then # Mac
  echo "Mac install"
  export CFLAGS=-Qunused-arguments
  export CPPFLAGS=-Qunused-arguments
fi

pip $*
pip freeze > requirements.txt
