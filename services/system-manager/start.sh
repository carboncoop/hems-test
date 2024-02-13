#!/bin/sh

# configuration scripts. Run in background
/tmp/scripts/iptables.sh &

# Run the watchdog script. Shouldn't exit
/tmp/scripts/watchdog.py