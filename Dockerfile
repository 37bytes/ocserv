FROM debian:latest

RUN apt-get update -qq && \ 
    DEBIAN_FRONTEND=noninteractive  apt-get -y install ocserv iptables procps rsync sipcalc ca-certificates certbot python3-certbot-dns-cloudflare cron rsyslog libpam-python mc pamtester

VOLUME /config
ADD ocserv /etc/default/ocserv
COPY docker-entrypoint.sh /entrypoint.sh
WORKDIR /config

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 443/tcp
EXPOSE 443/udp
CMD ["ocserv", "-c", "/config/ocserv.conf"]