from os import getenv
from pika import BlockingConnection, ConnectionParameters, PlainCredentials

from app.main import load_env_vars


load_env_vars()

def minha_callback(ch, method, properties, body):
    print(body)

async def connetion():
    try:
        connect_parameters = ConnectionParameters(
            host=getenv("RABBITMQ_SERVER_URL"),
            port=getenv("RABBITMQ_SERVER_PORT"),
            credentials=PlainCredentials(
                username=getenv("RABBITMQ_DEFAULT_USER"),
                password=getenv("RABBITMQ_DEFAULT_PASSWORD")
            )
        )
        connect = BlockingConnection(connect_parameters)
        return connect
    except:
        raise Exception(f'Error connect RabbitMQ!')


async def read_email(email_server, email_account, email_password):
    try:
        channel = await connetion().channel()
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
    except:
        raise Exception(f'Error connect RabbitMQ!')    
    return {'message'}