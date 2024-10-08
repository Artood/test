#!/bin/bash

# Script to configure the network interface

# Check if the script is being run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run script as root."
  exit 1
fi

# Configuration parameters
INTERFACE="eth0"

# Path to the netplan configuration file
NETPLAN_FILE=$(ls /etc/netplan/*.yaml 2>/dev/null)

# Create a backup of the current netplan configuration
cp $NETPLAN_FILE "${NETPLAN_FILE}.bak"

# Write the new netplan configuration
cat <<EOL > $NETPLAN_FILE
network:
  ethernets:
    $INTERFACE:
     dhcp4: true
  version: 2
EOL

# Apply the new netplan configuration
netplan apply
echo "The network interface has been configured to $INTERFACE."