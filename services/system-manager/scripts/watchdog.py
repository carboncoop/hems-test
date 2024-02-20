#!/usr/bin/env python3

import time
from datetime import datetime

import logging

import watchdog_utils

logging.basicConfig(
        format='%(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')

# Loop round and check services

# Stop wifi-repeater 10 minutes after startup
# Restart hass if updated
# Ping internet and restart box if not responding for ~30 mins

last_seen = datetime.now()
wifi_started_at = None

logging.info("Watchdog script started")

while True:

    wifi_started_at = watchdog_utils.check_wifi_repeater_n_stop(wifi_started_at)

    watchdog_utils.restart_hass()

    last_seen = watchdog_utils.check_internet(last_seen)

    time.sleep(30)
