#!/usr/bin/env bash

connected_devices=$(bluetoothctl devices Connected | awk '{print $2}')

for device in $connected_devices; do
    battery=$(bluetoothctl info "$device" | grep "Battery Percentage" | awk -F'[()]' '{print $2}')
    
    if [ -n "$battery" ]; then
        echo "󰋋 $battery%"
        exit 0
    fi
done

echo ""
