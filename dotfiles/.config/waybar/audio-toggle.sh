#!/usr/bin/env bash

# Available sinks (add more if you want)
SINKS=(63 98)

# Get current default
CURRENT=$(wpctl status | awk '/\*.*Sink/ {print $2}')

# Strip trailing dot if present
CURRENT=${CURRENT%.}

# Find index of current sink
for i in "${!SINKS[@]}"; do
    if [[ "${SINKS[$i]}" == "$CURRENT" ]]; then
        NEXT_INDEX=$(( (i + 1) % ${#SINKS[@]} ))
        NEXT_SINK=${SINKS[$NEXT_INDEX]}
        wpctl set-default "$NEXT_SINK"
        exit 0
    fi
done

# Fallback: set to first sink
wpctl set-default "${SINKS[0]}"
