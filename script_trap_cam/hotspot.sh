#!/bin/bash

# 1. Create a new Wi-Fi hotspot connection
sudo nmcli connection add type wifi ifname wlan0 con-name TrapCam autoconnect yes ssid TrapCam

# 2. Configure it to use 'ap' (access point) mode
sudo nmcli connection modify TrapCam 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared

# 3. Set a WPA2 password
sudo nmcli connection modify TrapCam wifi-sec.key-mgmt wpa-psk
sudo nmcli connection modify TrapCam wifi-sec.psk "TrapCam123"  # Must be 8+ characters

# 4. Activate the hotspot
sudo nmcli connection up TrapCam
