# Fully managed Home Energy Management System (HEMS)

This system was designed and built by Carbon Co-op to provide energy communities with a secure and private in-home device for data gathering and high-load device control. The project is primarily aimed at the following usecases: 

* **Building performance/retrofit evaluation**
While smart meter data is useful, the addition of local sensor data allows for the separation of the impact of fabric, HVAC and control measures and can account for changes in user behaviour, solar generation and electric vehicles charging. A fully managed HEMS allows us to provide monitoring to meet householder or project requirements, even with non-techical users via fleet deployment and remote support.


* **Demand Side Flexiblity**
The HEMS forms the endpoint for community 'demand side response' schemes, such as our [PowerShaper Flex service](https://flex.powershaper.io/), turning high load domestic devices up and down in order to respond to needs of a renewable rich power grid.

# HEMS System, Services and functionality
![Diagram showing each service running on the Balena OS and a description of its functionality.](https://cc-site-media.s3.amazonaws.com/uploads/2024/05/HEMS-services-diagram.png)


## Software setup

Running this project is as simple as deploying it to a balenaCloud application, then downloading the OS image from the dashboard and flashing your SD card.

[![](https://balena.io/deploy.png)](https://dashboard.balena-cloud.com/deploy)

We recommend this button as the de-facto method for deploying new apps on balenaCloud, especially if you are just getting started or want to test out the project. However, if you want to modify the docker-compose or tinker with the code, you'll need to clone this repo and use the [balenaCLI](https://github.com/balena-io/balena-cli) to push to your devices. This can be done later if you initially deploy using the button above. [Read more](https://www.balena.io/docs/learn/deploy/deployment/).

### First login
To access your new Home Assistant instance, browse to the IP address of your device (which you can find on your balenaCloud dashboard). Go through the Home Assistant setup process and establish a username and password. To obtain a secure public URL for your Home Assistant instance, simply click the "Public Device URL" switch on your balenaCloud dashboard. You'll then see a link to access your unique device URL.

## File Locations

The project's docker-compose file creates a persistent volume on your disk/SD card for storing Home Assistant configuration files. These are located in the `/config` folder.

## Configuring Home Assistant
Generally we recommend UI configuration from the Home Assistant standard UI, but if you have particular requirements that mean you need to edit yaml files a text editor called Hass-Configurator is available locally on port 3218. (To access this go to http://%your-ip-address%:3218 - Using this editor, you can make changes to the Home Assistant configuration file `configuration.yaml` which is the in the default folder `hass-config` for Hass-Configurator. (`hass-config` is mapped to `/config`)

# Home Assistant and supporting containers.

* [**Home Assistant**](https://www.home-assistant.io/) tracks the final version of the previous months release for stablity.
* **MQTT** - Mosquitto broker.
* [**InfluxDB**](https://www.influxdata.com/) is a comprehensive time-series database. We are using the 2.x branch in order to utilise the edge replication functionality to influxcloud, which brings the advantage of automated gathering of device load information, feed loss tracking and local caching (for later replication). 
* [**WiFi repeater**](https://github.com/balena-labs-projects/wifi-repeater) a balena labs project to add a wifi access point to balena installations.
* [**NGINX reverse proxy**](https://www.nginx.com/) 


# Managing Community Custom Components

* **Community components** - The Home Assistant Community Store provides much simpler installation and most importantly management of updates for custom components. Moving away from fleet wide deployment of custom components will free us up in terms of what devices we can support. We have already installed HACS on the ABS test fleet boxes and it's working very well.


# Configuration considerations

## Hardware required

* Raspberry Pi 4B - 2GB or more
* 64GB Micro-SD Card (with wear levelling)
* Power supply and cable
* Optional: For connecting Zigbee devices - [SONOFF 3.0 dongle plus](https://sonoff.tech/product/gateway-and-sensors/sonoff-zigbee-3-0-usb-dongle-plus-e/) or [HA Skyconnect](https://www.home-assistant.io/skyconnect/) - for future MATTER compatibility (note: multi-protocol support is only available currently in HA OS version).