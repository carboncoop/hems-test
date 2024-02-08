FROM arm64v8/alpine:3

RUN apk add --update iptables ip6tables iptables-legacy

COPY start.sh /tmp/start.sh 
RUN chmod +x /tmp/start.sh 

CMD ["/tmp/start.sh"]