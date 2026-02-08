#!/bin/bash

set -e

echo "==> Installing official packages..."
sudo pacman -S --needed - < pkg/pacman.txt

if command -v yay >/dev/null 2>&1; then
    echo "==> Installing AUR packages..."
    yay -S --needed - < pkg/aur.txt
else
    echo "==> yay not found. Skipping AUR packages."
fi

echo "==> Copying dotfiles..."
cp -r dotfiles/. ~/

echo "==> Installing SDDM config..."
sudo cp system/sddm/Xsetup /usr/share/sddm/scripts/
sudo chmod +x /usr/share/sddm/scripts/Xsetup

echo "==> Setup complete."
