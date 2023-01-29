FROM debian:latest

VOLUME /config

COPY docker-entrypoint.sh /entrypoint.sh

RUN apt-get update && apt-get -y install ocserv libnss-ldap nslcd iptables procps rsync sipcalc ca-certificates certbot python3-certbot-dns-cloudflare cron

ADD ocserv /etc/default/ocserv
ADD pam_ldap /etc/default/pam_ldap

RUN rm -f /etc/pam_ldap.conf && touch /config/pam_ldap.conf &&  \
    ln -fs /config/pam_ldap.conf /etc/pam_ldap.conf &&  \
    ln -fs /config/pam_ldap.conf /etc/libnss-ldap.conf && \
    ln -fs /etc/default/pam_ldap/nsswitch.conf /etc/nsswitch.conf


WORKDIR /config

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 443/tcp
EXPOSE 443/udp
CMD ["ocserv", "-c", "/config/ocserv.conf", "-f"]