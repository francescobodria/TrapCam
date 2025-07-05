#!/bin/bash

# create hotspot 
sudo nmcli d wifi hotspot ifname wlan0 ssid TrapCam password <PASSWORD>
# activate hotspot mode
nmcli connection up Hotspot
# deactivate hotspot mode
nmcli connection down Hotspot