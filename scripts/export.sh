#!/bin/bash
set -e
if [ -n "${BASH_SOURCE[0]}" ] && [ "${BASH_SOURCE[0]}" = "${0}" ] ; then
    echo "This script should be sourced, not executed:"
    echo ". ${BASH_SOURCE[0]}"
    exit 1
fi

SCRIPT_NAME=$(realpath "$BASH_SOURCE")
DIR_NAME=$(dirname "$SCRIPT_NAME")
ROOT_DIR=$(realpath "$DIR_NAME/..")

export PYTHONPATH="$ROOT_DIR/"
echo "PYTHONPATH is now $PYTHONPATH"
set +e
