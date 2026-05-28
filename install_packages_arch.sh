#!/usr/bin/env bash

set -e

echo "Updating system."
sudo pacman -Syu --noconfirm

OFFICIAL_PACKAGES=(
    "xorg-server"
    "xorg-xinit"
    "xorg-xprop"
    "i3-wm"
    "i3blocks"
    "perl-anyevent-i3"
    "xorg-xrandr"
    "sddm"

    "picom"
    "feh"
    "rofi"
    "polybar"
    "dunst"
    "libnotify"
    "python-pywal"
    "polkit-gnome"

    "pipewire"
    "pipewire-pulse"
    "pavucontrol"
    "network-manager-applet"

    "alacritty"
    "zsh"
    "starship"
    "zsh-autosuggestions"
    "zsh-syntax-highlighting"
    "fastfetch"

    "python"
    "thunar"
    "unzip"
    "zip"
    "noto-fonts"
    "noto-fonts-emoji"
    "playerctl"
    "wget"
    "ttf-jetbrains-mono-nerd"

    "amd-ucode"
    "mesa"
    "vulkan-radeon"
    "xf86-video-amdgpu"
    "base-devel"
    "cmake"
    "gdb"
    "glfw-x11"
    "glm"
    "ncdu"
    "xournalpp"
    "rnote"
)

echo "Installing official packages."
sudo pacman -S --needed --noconfirm "${OFFICIAL_PACKAGES[@]}"

if ! command -v yay &> /dev/null; then
    echo "Installing yay."
    sudo pacman -S --needed --noconfirm base-devel git
    git clone https://aur.archlinux.org/yay.git /tmp/yay
    cd /tmp/yay
    makepkg -si --noconfirm
    cd ~
    rm -rf /tmp/yay
else
    echo "yay is already installed."
fi

AUR_PACKAGES=(
    "vesktop"
    "visual-studio-code-bin"
    "microsoft-edge-stable-bin"
    # "picom-ftlabs-git" # for animations
)

echo "Installing AUR packages."
yay -S --needed --noconfirm "${AUR_PACKAGES[@]}"

echo "Enabled sddm."
sudo systemctl enable sddm

echo "Changing shell to zsh."
if [ "$SHELL" != "/usr/bin/zsh" ]; then
    chsh -s /usr/bin/zsh
    echo "Shell changed successfully."
fi
