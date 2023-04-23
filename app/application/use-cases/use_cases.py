from app.infra.event_bus.read_queues import read_email


async def read_message_email(email_server, email_account, email_password):
    message = await read_email(email_server, email_account, email_password)
    return {'message'}