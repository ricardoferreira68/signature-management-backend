from amqpstorm import management
from asyncio import run
from os import getenv
from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from time import sleep


if not getenv("RUN_CONTAINER"):
    from app.config_app import load_env_vars
    load_env_vars()

message = None

def minha_callback(ch, method, properties, body):
    message = body
    print(f'message: {message}')
    if not getenv("RUN_CONTAINER"):
        ch.stop_consuming()


async def connect():
    print(f'RABBITMQ_SERVER_URL: {getenv("RABBITMQ_SERVER_URL")}')
    print(f'RABBITMQ_SERVER_PORT: {getenv("RABBITMQ_SERVER_PORT")}')
    print(f'RABBITMQ_USER: {getenv("RABBITMQ_USER")}')
    print(f'RABBITMQ_PASSWORD: {getenv("RABBITMQ_PASSWORD")}')
    try:
        connection_parameters = ConnectionParameters(
            host=getenv("RABBITMQ_SERVER_URL"),
            port=getenv("RABBITMQ_SERVER_PORT"),
            credentials=PlainCredentials(
                username=getenv("RABBITMQ_USER"),
                password=getenv("RABBITMQ_PASSWORD")
            )
        )
        connection = BlockingConnection(connection_parameters)
        return connection
    except:
        raise Exception(f'Error connect RabbitMQ!')


async def rabbitmq_read_email():
    try:
        connection = await connect()
        channel = connection.channel()
    except:
        raise Exception(f'Error create channel')    

    try:
        channel.queue_declare(
            queue=getenv("RABBITMQ_READ_EMAIL_QUEUE"),
            durable=True
        )
    except:
        raise Exception(f'Error queue declare')    

    try:
        channel.basic_consume(
            queue=getenv("RABBITMQ_READ_EMAIL_QUEUE"),
            auto_ack=True,
            on_message_callback=minha_callback
        )
        print(f'Listen RabbitMQ on port {getenv("RABBITMQ_SERVER_PORT")}')
        channel.start_consuming()
        channel.close()
        connection.close()
        return message
    except:
        raise Exception(f'Error connect RabbitMQ!')    
    return {'message'}


run(rabbitmq_read_email())
