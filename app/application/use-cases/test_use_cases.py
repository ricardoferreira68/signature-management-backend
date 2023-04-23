import pytest
from os import getenv

from use_cases import read_message_email


def test_env_vars():
    imap_email_server = getenv('IMAP_EMAIL_SERVER')
    email_account = getenv('EMAIL_ACCOUNT')
    email_password = getenv('EMAIL_PASSWORD')

    assert imap_email_server is not None
    assert email_account is not None
    assert email_password is not None

# @staticmethod
@pytest.mark.asyncio
async def test_read_message_email():
    email_server = getenv('IMAP_EMAIL_SERVER')
    email_account = getenv('EMAIL_ACCOUNT')
    email_password = getenv('EMAIL_PASSWOD')
    
    message = await read_message_email(email_server, email_account, email_password)

    assert message
