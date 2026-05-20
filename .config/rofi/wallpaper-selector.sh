#!/usr/bin/env bash

WALL_DIR="/home/leetuah/Pictures/Wallpapers"

rofi_list=""
for img in "$WALL_DIR"/*.{jpg,jpeg,png}; do
    [ -e "$img" ] || continue 
    
    filename=$(basename "$img")
    rofi_list+="${filename}\0icon\x1f${img}\n"
done

selected=$(echo -en "$rofi_list" | rofi -dmenu -i -p "󰸉 Wallpapers" -theme ~/.config/rofi/wallpaper-grid.rasi)

if [ -n "$selected" ]; then
    wall_path="$WALL_DIR/$selected"

    feh --bg-fill "$wall_path"
    wal -q -n -i "$wall_path"

    i3-msg reload > /dev/null
    polybar-msg cmd restart > /dev/null
    killall dunst 2>/dev/null
    notify-send "Wallpaper Updated" "Applied: $selected"
fi