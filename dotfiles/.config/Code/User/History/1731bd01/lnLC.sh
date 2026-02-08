#!/usr/bin/env bash

# Rebuild Hyprland dashboard on workspace 1

# 1. Close existing dashboard windows (terminal, btm, Spotify) on workspace 1
hyprctl clients -j | jq -r '
  .[] 
  | select(
      .workspace.id == 1 and 
      (.class == "dash-term" or .class == "dash-btm" or .class == "Spotify")
    ) 
  | .address
' | while read -r addr; do
  hyprctl dispatch closewindow address:"$addr"
done

# 2. Make sure workspace 1 is on HDMI-A-2 (your main monitor)
hyprctl dispatch moveworkspacetomonitor 1 HDMI-A-2

# 3. Respawn dashboard apps

# Spotify FIRST → fills left half
spotify &

# Terminal (top-right)
sleep 0.5
kitty --class dash-term &

# btm (bottom-right)
sleep 0.1
kitty --class dash-btm -e btm &


# 4. Focus workspace 1
sleep 0.1
hyprctl dispatch workspace 1
