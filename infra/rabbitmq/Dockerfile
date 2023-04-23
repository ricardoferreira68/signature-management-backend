FROM rabbitmq:3-management

ADD .env /
ADD .secrets /
ADD init.sh /
ADD config_rabbit.sh /

RUN chmod +x /init.sh /config_rabbit.sh

ENTRYPOINT ["/init.sh"]
