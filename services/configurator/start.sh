#!/bin/sh

sleep 180

# Setup IP tables rule to allow 2 way comms between docker network and wireless-repeater block
iptables-legacy -I nm-sh-fw-wlan0 -o wlan0 -s 172.18.4.0/24 -d 10.42.0.0/24 -j ACCEPT

# Keep this at the end
tail -f