#!/bin/bash

# Script to configure the network interface

# Check if the script is being run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run script as root."
  exit 1
fi

# Configuration parameters
myNEW_INTERFACE="eth0"

# Path to the netplan configuration file
myNETPLAN_FILE=$(ls /etc/netplan/*.yaml 2>/dev/null)

# Check if we found the netplan configuration file
if [ -z "$myNETPLAN_FILE" ]; then
    echo "The netplan configuration file not found!"
    exit 1
fi

# Check if cloud-init generated network configuration
if grep -q "# This file is generated from information provided by the datasource" "$myNETPLAN_FILE"; then
    echo "Cloud-init network configuration detected. Disabling it."
    echo "network: {config: disabled}" > /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg
    echo "Cloud-init network configuration disabled."
fi

# Find the current network interface
myINTERFACE=$(awk '/ethernets:/ {getline; sub(/:$/, ""); print $1}' "$myNETPLAN_FILE")

# Check if we found the interface
if [ -z "$myINTERFACE" ]; then
    echo "Network interface not found in the configuration file!"
    exit 1
fi

# Create a backup of the current netplan configuration
cp "$myNETPLAN_FILE" "${myNETPLAN_FILE}.bak"

# Replace the interface
sed -i "s/$myINTERFACE/$myNEW_INTERFACE/" "$myNETPLAN_FILE"

# Apply new netplan configuration
netplan apply

echo "The network interface $myINTERFACE has been configured to $myNEW_INTERFACE."
