from time import sleep

from app.infra.event_bus.listen_queue import rabbitmq_read_email


async def read_message_email(channel):
    message = None
    if channel == 'RabbitMQ':
        print('\n\nWaint to RabbitMQ Serve starting ...')
        message = await rabbitmq_read_email()
        print(f'message: {message}')

    return message
 