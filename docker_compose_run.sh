clear

docker rm -f $(docker ps -aq)

if [ -f app/.env ]
then
  export $(cat app/.env | xargs)
fi

if [ -f app/.env.secret ]
then
  export $(cat app/.env.secret | xargs)
fi

sed -i 's/RABBITMQ_USER/'$RABBITMQ_USER'/g' ./app/infra/rabbitmq/definitions.json
sed -i 's/RABBITMQ_PASSWORD/'$RABBITMQ_PASSWORD'/g' ./app/infra/rabbitmq/definitions.json

docker-compose up --build

# docker run --name read_email_message -d -i -t read_email_message python3 /app/infra/event_bus/listen_queues.py
# docker exec -d read_email_message python3 /app/infra/event_bus/listen_queues.py
# echo "Waiting rabbitmq container up ..."
# sleep 60
# docker restart read_email_message
