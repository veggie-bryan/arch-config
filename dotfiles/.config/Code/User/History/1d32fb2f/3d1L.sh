#!/bin/bash

sleep 1

WALLPAPER="$HOME/Pictures/wallpapers/street.jpg"

swww img "$WALLPAPER" \
  --transition-type fade \
  --transition-duration 0.7
