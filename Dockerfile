FROM simdd/node-ubuntu-supervisor:latest

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY . /app

WORKDIR /app

RUN export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && pipenv install  &&  npm install

EXPOSE 1234 4321
CMD ["/usr/bin/supervisord"]