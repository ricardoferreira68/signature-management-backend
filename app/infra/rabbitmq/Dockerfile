FROM rabbitmq:3-management

ADD init.sh /
ADD config_rabbit.sh /

RUN chmod +x /init.sh /config_rabbit.sh

CMD ["/init.sh"]
 