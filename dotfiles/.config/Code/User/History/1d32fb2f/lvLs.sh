#!/bin/bash

sleep 1

WALLPAPER="$HOME/Pictures/wallpapers/earthMoon.jpg"

swww img "$WALLPAPER" \
  --transition-type fade \
  --transition-duration 0.7
