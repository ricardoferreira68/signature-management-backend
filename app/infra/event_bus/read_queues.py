from os import getenv
from pika import BlockingConnection, ConnectionParameters, PlainCredentials


async def connetion():
    try:
        connect = await ConnectionParameters(
            host=getenv("RABBITMQ_SERVER_URL"),
            port=getenv("RABBITMQ_SERVER_PORT"),
            credentials=PlainCredentials(
                username=getenv("RABBITMQ_DEFAULT_USER"),
                password=getenv("RABBITMQ_DEFAULT_PASSWORD")
            )
        )
    except:
        raise Exception(f'Error connect RabbitMQ!')

async def read_email(email_server, email_account, email_password):
    try:
        channel = BlockingConnection(await connetion())
        
    )