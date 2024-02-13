FROM arm64v8/alpine:3

RUN apk add --update iptables ip6tables iptables-legacy curl

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

RUN mkdir -p /tmp/scripts
COPY scripts/* /tmp/scripts/

COPY start.sh /tmp/start.sh 

CMD ["/tmp/start.sh"]