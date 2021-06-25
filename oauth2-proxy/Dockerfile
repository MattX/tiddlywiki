FROM quay.io/oauth2-proxy/oauth2-proxy:latest-armv6

COPY emails.txt /etc/emails.txt
COPY oauth2-proxy.cfg /etc/oauth2-proxy.cfg

CMD ["--config=/etc/oauth2-proxy.cfg"]
