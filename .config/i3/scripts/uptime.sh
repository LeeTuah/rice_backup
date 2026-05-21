#!/bin/sh

read -r up rest < /proc/uptime

seconds=$(awk 'BEGIN {print int('$up')}')
days=$((seconds / 86400))
hours=$(((seconds % 86400) / 3600))
minutes=$(((seconds % 3600) / 60))
secs=$((seconds % 60))

if [ "$days" -gt 0 ]; then
    printf "%dd %02dh %02dm %02ds\n" "$days" "$hours" "$minutes" "$secs"
else
    printf "%02dh %02dm %02ds\n" "$hours" "$minutes" "$secs"
fi
