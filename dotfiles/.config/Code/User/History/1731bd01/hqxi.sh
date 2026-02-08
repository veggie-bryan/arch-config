#!/usr/bin/env bash

# Kill existing dashboard windows
hyprctl dispatch killactive      # if you're focused on one
hyprctl dispatch movetoworkspace 1
hyprctl clients -j | jq -r '.[] | select(.class == "dash-term" or .class == "dash-btop" or .class == "Spotify") | .address' | while read -r addr; do
    hyprctl dispatch closewindow "$addr"
done

sleep 0.3

# Relaunch windows
kitty --class dash-term &
sleep 0.2
kitty --class dash-btop -e btop &
sleep 0.2
flatpak run com.spotify.Client &

sleep 0.3

# Move to workspace 1
hyprctl dispatch workspace 1
