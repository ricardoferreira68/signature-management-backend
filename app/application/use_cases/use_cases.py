from app.infra.event_bus.listen_queues import rabbitmq_read_email


async def read_message_email(channel):
    message = None
    if channel == 'RabbitMQ':
        message = await rabbitmq_read_email()

    return message
