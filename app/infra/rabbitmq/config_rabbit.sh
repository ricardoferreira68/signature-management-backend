#!/bin/bash

export $(cat .env | xargs)
export $(cat .secrets | xargs)

# This script needs to be executed just once
if [ -f /$0.completed ] ; then
  echo "$0 `date` /$0.completed found, skipping run"
  exit 0
fi

# Wait for RabbitMQ startup
for (( ; ; )) ; do
  sleep 5
  rabbitmqctl -q node_health_check > /dev/null 2>&1
  if [ $? -eq 0 ] ; then
    echo "$0 `date` rabbitmq is now running"
    break
  else
    echo "$0 `date` waiting for rabbitmq startup"
  fi
done

# Execute RabbitMQ config commands here

# Create user
rabbitmqctl add_user $RABBITMQ_DEFAULT_USER $RABBITMQ_DEFAULT_PASSWORD
rabbitmqctl set_user_tags $RABBITMQ_DEFAULT_USER administrator
rabbitmqctl add_vhost /
rabbitmqctl set_permissions -p / $RABBITMQ_DEFAULT_USER ".*" ".*" ".*"
echo "$0 `date` user $RABBITMQ_DEFAULT_USER created"

# Create queue
rabbitmqadmin declare queue name=$RABBITMQ_READ_EMAIL_QUEUE durable=true
echo "$0 `date` queues created"

# Create mark so script is not ran again
touch /$0.completed
 