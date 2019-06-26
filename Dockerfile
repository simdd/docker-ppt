FROM ubuntu:13.04

RUN apt-get update
RUN apt-get upgrade -yb

RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 1234 4321
CMD ["/usr/bin/supervisord"]