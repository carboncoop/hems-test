# Refactoring our HEMS to better match upstream projects

The current HEMS system developed as part of OpenADR and later REScoop VPP was first scoped over 3 years ago, in which time there have been significant changes in the upstream projects, most notably in Home Assistant. Many of the additional services we developed are now included in core or in core and custom integrations. This is an attempt to realign the HEMS with the various upstream components and strip out some of the complexity.

# Home Assistant, Configurator and MQTT

We're using the excellent [Balena-homeassistant](https://github.com/balena-io-experimental/balena-homeassistant) project as a basis for these components. 

* [**Home Assistant**](https://www.home-assistant.io/) tracks the latest release, the /config directory is configured as a persistent volume.
* **Configurator** - mirrors the existing setup on our current HEMS (though without the now redundant link to the glue config) - need to add security - via [Environment variables]([environment variable](https://www.balena.io/docs/learn/manage/variables/)) see: https://github.com/danielperna84/hass-configurator/wiki/Configuration
* **MQTT** - As current HEMS

# Missing elements from existing HEMS

* **InfluxDB** - we'd like to move from our current 1.8 setup to 2.0+. Very interested in the edge replication functionality to influxcloud, which brings the advantage of automated gathering of device load information, feed loss tracking and local caching (for later replication). There are again some interesting examples of this on balena hub which we might use a basis - for example [balenaAir](https://github.com/balenair/balenair), which benefits from webinars and walkthroughs from influx & balena. This would remove the need for us to run Telegraf.
* **COFYbox config** - there are a variety of tasks fulfilled by this application, the primary is the creation of an access point for device connection - this can now be acheived via [balena Wifi-Repeater](https://github.com/balena-labs-projects/wifi-repeater), as yet it's unclear if all the additional functions can be dealt with via edge replication.
* **Glue** - retired in favour of packaging system.
* **cofycloud-api-pull** - Likely that COFYcloud won't be available after project end - retired in favour of more granular OpenADR signals.
* **Telegraf** - Potentially retired in favour of edge replication for aggregation.


## Hardware required

* Raspberry Pi 3B (current fleet) or Raspberry Pi 4B - 2GB (replacement for new boxes)
* 64GB Micro-SD Card (with wear levelling)
* Power supply and cable
* Optional: For connecting Zigbee devices - [SONOFF 3.0 dongle plus](https://sonoff.tech/product/gateway-and-sensors/sonoff-zigbee-3-0-usb-dongle-plus-e/) or HA Skyconnect (for future MATTER compatibility).


