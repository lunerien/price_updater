#!/bin/bash
set -e
PROJECT_ROOT="$(dirname "$0")/.."

python3 -m libcst.tool codemod autotyping.AutotypeCommand \
    --none-return \
    --scalar-return \
    --bool-param \
    --int-param \
    --float-param \
    --str-param \
    lib/ widgets/ ./
