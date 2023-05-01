from time import sleep

from app.infra.event_bus.listen_queue import rabbitmq_read_email


async def read_message_email(channel: str) -> set:
    """Read message from brocker queue.

    Args:
        channel (str): defines which brocker provides the queue, for example: RabbitMQ.

    Returns:
        set: serialized message

    # >>> read_message_email('BrockerTest')
    # {'test'}
    """
    message = None
    if channel == 'BrockerTest':
        return {'test'}
    elif channel == 'RabbitMQ':
        print('\n\nWaint to RabbitMQ Serve starting ...')
        message = await rabbitmq_read_email()
        print(f'message: {message}')
        return message
    return None
