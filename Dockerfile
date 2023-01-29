FROM debian:latest

VOLUME /config

COPY docker-entrypoint.sh /entrypoint.sh

RUN set -x \
  && apt-get update && apt-get install --no-install-recommends -y ocserv \
    certbot python3-certbot-dns-cloudflare cron iptables libnss-ldap iptables procps rsync sipcalc ca-certificates \
  && apt-get -y autoremove && apt-get -y clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm /etc/ocserv/ocserv.conf \
  && chmod +x /entrypoint.sh

RUN rm -f /etc/pam_ldap.conf && touch /config/pam_ldap.conf && ln -s /config/pam_ldap.conf /etc/pam_ldap.conf

ADD ocserv /etc/default/ocserv
ADD pam_ldap /etc/default/pam_ldap

WORKDIR /config

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 443/tcp
EXPOSE 443/udp
CMD ["ocserv", "-c", "/config/ocserv.conf", "-f"]