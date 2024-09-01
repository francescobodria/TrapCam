#!/bin/bash

# create hotspot 
sudo nmcli d wifi hotspot ifname wlan0 ssid <SSID> password <PASSWORD>
# activate hotspot mode
nmcli connection up my-hotspot
# deactivate hotspot mode
nmcli connection down my-hotspot