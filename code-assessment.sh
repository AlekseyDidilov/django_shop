#!/usr/bin/env bash

declare -a FAILURES

add_fail() {
    FAILURES+=("$1")
}

black --check . || add_fail black
flake8 . || add_fail flake8
if [[ ${#FAILURES[@]} -ne 0 ]]; then
    cat <<RESULT
===================================================
= Code assessment is failed! Please fix errors!!! =
===================================================
Failed tool(s):
RESULT
    for var in "${FAILURES[@]}"; do
        echo "- ${var}"
    done
    exit 11
fi