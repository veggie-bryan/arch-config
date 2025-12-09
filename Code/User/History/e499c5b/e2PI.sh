#!/usr/bin/env bash

# Show the active output name
wpctl status | awk '
/\*.*Sink/ {
    # Next line is the name
    getline
    name=$0
    sub(/^[[:space:]]+/, "", name)
    print name
}'
