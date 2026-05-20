#!/usr/bin/env bash

options="Shutdown\nReboot\nLogout\nLock\nSuspend"

selected=$(echo -e "$options" | rofi -dmenu -i -p "Power Menu")

case $selected in
  Shutdown) systemctl poweroff ;;
  Reboot) systemctl reboot ;;
  Logout) i3-msg exit ;;
  Lock) i3lock ;;
  Suspend) systemctl suspend ;;
esac
