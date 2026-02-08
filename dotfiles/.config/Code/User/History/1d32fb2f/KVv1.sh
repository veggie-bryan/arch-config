#!/bin/bash

sleep 1

WALLPAPER="$HOME/Pictures/wallpapers/neonNight.png"

swww img "$WALLPAPER" \
  --transition-type fade \
  --transition-duration 0.7
