#!/usr/bin/env python3

import time

# Loop round and check services

# Stop wifi-repeater 10 minutes after startup
# Restart hass if updated and 2(?) minutes after startup
# Ping internet and restart box if not responding for ~30 mins

while True:

    # Get and print uptime
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    print("Current uptime = " + str(uptime_seconds) + " seconds")

    time.sleep(30)