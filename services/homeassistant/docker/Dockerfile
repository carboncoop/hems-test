FROM homeassistant/home-assistant:stable

COPY docker/start.sh /tmp/start.sh

RUN chmod +x /tmp/start.sh

COPY custom_components /config/custom_components

CMD ["bash","/tmp/start.sh"]
