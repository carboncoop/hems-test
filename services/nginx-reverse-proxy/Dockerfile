ARG ARCH=arm32v7

FROM ${ARCH}/nginx:latest

# Remove default sites
RUN rm -rf /usr/share/nginx/html/*

# Add configuration file
COPY nginx.conf /etc/nginx/nginx.conf
COPY http.conf /etc/nginx/conf.d/default.conf

COPY wait-for-it.sh .

# Start the container
EXPOSE 80
CMD ["./wait-for-it.sh", "cofybox-config:8000", "-t", "0", "--", "nginx", "-g", "daemon off;"]
