#!/bin/bash
set -e
PROJECT_ROOT="$(dirname "$0")/.."

cd "$PROJECT_ROOT"
source ./scripts/export.sh
python3 -m pylint \
    --fail-under=9.0 \
    --fail-on=W,E \
    lib \
    widgets \
    $@
