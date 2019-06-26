FROM simdd/node-ubuntu-supervisor:latest

COPY . /app
WORKDIR /app

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 1234 4321
CMD ["/usr/bin/supervisord"]