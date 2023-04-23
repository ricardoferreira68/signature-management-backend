clear

if [ -f app/.env ]
then
  export $(cat app/.env | xargs)
fi

if [ -f app/.env.secret ]
then
  export $(cat app/.env.secret | xargs)
fi

docker-compose up --build
