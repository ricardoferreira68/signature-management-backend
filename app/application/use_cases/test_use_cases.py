import pytest
from os import getenv

from app.application.use_cases.use_cases import read_message_email


# @staticmethod
@pytest.mark.asyncio
async def test_read_message_email():
    email_server = getenv('IMAP_EMAIL_SERVER')
    email_account = getenv('EMAIL_ACCOUNT')
    email_password = getenv('EMAIL_PASSWOD')
    
    message = await read_message_email(email_server, email_account, email_password)

    assert message
