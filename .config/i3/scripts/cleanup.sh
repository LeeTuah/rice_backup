#!/bin/bash

echo "Starting system cleanup..."
echo "--------------------------"

echo "Cleaning package caches..."
if command -v paccache &> /dev/null; then
    sudo paccache -r
    yay -Sc --aur --noconfirm
else
    yay -Sc --noconfirm
fi

echo "Checking for orphaned packages..."
ORPHANS=$(pacman -Qtdq)
if [ -n "$ORPHANS" ]; then
    echo "Removing orphans: $ORPHANS"
    sudo pacman -Rns $ORPHANS --noconfirm
else
    echo "No orphaned packages to remove."
fi

echo "Vacuuming systemd journal (keeping last 2 weeks)..."
sudo journalctl --vacuum-time=2weeks

echo "Removing unused Flatpak leftovers..."
flatpak uninstall --unused --noninteractive

echo "Clearing standard application caches..."
rm -rf ~/.cache/vscode-cpptools
rm -rf ~/.cache/microsoft-edge

echo "Clearing Discord and Vesktop caches..."

rm -rf ~/.config/discord/Cache
rm -rf ~/.config/discord/GPUCache
rm -rf ~/.config/discord/Code\ Cache

rm -rf ~/.config/vesktop/sessionData/Cache
rm -rf ~/.config/vesktop/sessionData/GPUCache
rm -rf ~/.config/vesktop/sessionData/Code\ Cache

echo "--------------------------"
echo "Cleanup complete!"