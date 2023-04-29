import pytest

from app.application.use_cases.use_cases import read_message_email


# @staticmethod
@pytest.mark.asyncio
async def test_read_message_email():
    channel = 'RabbitMQ'
    
    message = await read_message_email(channel)

    assert message
