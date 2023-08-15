# Refactoring our HEMS to better match upstream projects

The current HEMS system developed as part of OpenADR and later REScoop VPP was first scoped over 3 years ago, in which time there have been significant changes in the upstream projects, most notably in Home Assistant, Influx and Balena itself. Many of the additional services we developed are now included in core or in core and custom integrations. This is an attempt to realign the HEMS with the various upstream components and strip out some of the complexity.

# Home Assistant, Configurator and MQTT

The repo is currently a clone of the excellent [Balena-homeassistant](https://github.com/balena-io-experimental/balena-homeassistant) project which is what we are using for the Area Based Scheme test system, it is working well but lacking some key functionality we have in the current COFYbox. Below are the included services.

* [**Home Assistant**](https://www.home-assistant.io/) tracks the latest release, the /config directory is configured as a persistent volume.
* **Configurator** - mirrors the existing setup on our current HEMS (though without the now redundant link to the glue config) - need to add security (lacking in current COFYbox) - via [Environment variables]([environment variable](https://www.balena.io/docs/learn/manage/variables/)) see: https://github.com/danielperna84/hass-configurator/wiki/Configuration
* **MQTT** - As current HEMS

# Missing services from existing HEMS

* **InfluxDB** - we'd like to move from our current 1.8 setup to 2.0+. Very interested in the edge replication functionality to influxcloud, which brings the advantage of automated gathering of device load information, feed loss tracking and local caching (for later replication). There are again some interesting examples of this on balena hub which we might use a basis - for example [balenaAir](https://github.com/balenair/balenair), which benefits from webinars and walkthroughs from influx & balena. This would remove the need for us to run Telegraf.
* **COFYbox config** - there are a variety of tasks fulfilled by this application, the primary is the creation of an access point for device connection - this can now be acheived via [balena Wifi-Repeater](https://github.com/balena-labs-projects/wifi-repeater), as yet it's unclear if all the additional functions can be dealt with via edge replication.
* **Glue** - retired in favour of packaging system and custom integration.
* **cofycloud-api-pull** - Likely that COFYcloud won't be available after project end - retired in favour of more granular OpenADR signals.
* **Telegraf** - Potentially retired in favour of edge replication for aggregation.
* **NGINX reverse proxy** - ?

# Additional services for discussion

* **Grafana** - very standard companion graphing application for influx - on present COFYbox while all data is stored locally on the box, there is no way for the end user to access that data never mind visualise it. It maybe that grafana is too much for casual users and we should look at how we can enable HA to access and visualise historic data? 
* **ESPHome** - simple interface to setup, configure & control ESP8266/ESP32 based devices. Very well integrated into Home Assistant, could be worthy of exploration? [see example docker compose](https://github.com/klutchell/balena-homeassistant/blob/main/docker-compose.yml).

# Managing Community Custom Components

* **Community components** - The Home Assistant Community Store provides much simpler installation and most importantly management of updates for custom components. Moving away from fleet wide deployment of custom components will free us up in terms of what devices we can support. We have already installed HACS on the ABS test fleet boxes and it's working very well.

# PowerShaper Custom Components

* **[PowerShaper](https://gitlab.com/rescoopvpp/cofybox-balena/-/tree/main/services/homeassistant/custom_components/powershaper?ref_type=heads)** - Our most crucial element as it's the basis of our PowerShaper service. 1st priority.
* **[PowerShaper Monitor](https://gitlab.com/carboncoop/powershaper-monitor-hass/-/tree/9618d0c4c4fadd57487b63c343d3166208b1f93d)** - 3rd priority
* **[Cofybox Packages](https://gitlab.com/rescoopvpp/cofybox-balena/-/tree/main/services/homeassistant/custom_components/cofybox_packages?ref_type=heads)** - 2nd priority

We should discuss our aspirations for these components post VPP. Should we begin the process of getting them on HACS and eventually into core HA?

# Configuration considerations

* **Revisit HA configuration** - our current configuration.yaml is long and complex with a large number of work-arounds (mainly for non-persistant config issues which this rebasing would resolve), propose we start with minimal default and add in additions only where required. For example, removing 'name' and 'unit' settings from yaml, would open up UI based configuration of general settings (which is currently disabled). Other settings limit autodiscovery and adding of new devices to default dashboard. If required we can still set elements like 'name' fleet wide using app env variables.
* **PowerShaper prep** - setting up the env variables to allow integration with PowerShaper - maybe worth revisiting [original hems config](https://gitlab.com/carboncoop/hems/-/blob/master/balena/balena-production.yml) to seperate out any COFYcloud complication. 
* **User seperation** - at present most users login with the same account as admin - resulting in logins which are hard to remember and making tracking of changes difficult. Instead we should have default admin accounts and also create specific user accounts. Suggest these new accounts be 'non-admin' and that sidebar access to HACS and ESPhome should be admin only.



## Hardware required

* Raspberry Pi 3B (current fleet) or Raspberry Pi 4B - 2GB (replacement for new boxes)
* 64GB Micro-SD Card (with wear levelling)
* Power supply and cable
* Optional: For connecting Zigbee devices - [SONOFF 3.0 dongle plus](https://sonoff.tech/product/gateway-and-sensors/sonoff-zigbee-3-0-usb-dongle-plus-e/) or [HA Skyconnect](https://www.home-assistant.io/skyconnect/) - for future MATTER compatibility (note: multi-protocol support is only available currently in HA OS version).