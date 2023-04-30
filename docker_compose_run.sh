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

cp ./app/infra/rabbitmq/definitions.json ./app/infra/rabbitmq/definitions.copy
cp ./app/configuration.py ./app/infra/event_bus

sed -i 's/RABBITMQ_USER/'$RABBITMQ_USER'/g' ./app/infra/rabbitmq/definitions.copy
sed -i 's/RABBITMQ_PASSWORD/'$RABBITMQ_PASSWORD'/g' ./app/infra/rabbitmq/definitions.copy

docker-compose up --build

rm ./app/infra/rabbitmq/definitions.copy
