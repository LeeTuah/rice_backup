#!/usr/bin/env bash

# Get MAC addresses of all connected bluetooth devices
connected_devices=$(bluetoothctl devices Connected | awk '{print $2}')

for device in $connected_devices; do
    # Extract battery percentage using bluetoothctl info
    battery=$(bluetoothctl info "$device" | grep "Battery Percentage" | awk -F'[()]' '{print $2}')
    
    if [ -n "$battery" ]; then
        # Print the headphone icon and percentage
        echo "󰋋 $battery%"
        exit 0
    fi
done

# Output nothing if no wireless device with a battery is connected
echo ""
