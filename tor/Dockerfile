# TOR Proxy Dockerfile
FROM alpine:latest
RUN apk add --no-cache tor
EXPOSE 9050
USER nobody
CMD ["tor", "-f", "/etc/tor/torrc"]