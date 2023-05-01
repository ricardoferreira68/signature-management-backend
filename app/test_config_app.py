"""Test main
"""

from os import getenv, path

from dotenv import dotenv_values

from app.configuration import start_setting_env_vars_and_log_file


def test_load_env_vars():
    path_file = path.dirname(__file__) + '/'
    config = {**dotenv_values(), **dotenv_values(f'{path_file}.env.secret')}

    start_setting_env_vars_and_log_file()

    all_env_vars_configured = True
    for env_var in config:
        if not getenv(env_var):
            print(f'env var: {env_var}')
            all_env_vars_configured = False

    assert all_env_vars_configured
