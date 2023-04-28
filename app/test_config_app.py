"""Test main
"""

from dotenv import dotenv_values
from os import getenv, path

from app.config_app import load_env_vars


def test_load_env_vars():
    path_file = path.dirname(__file__) + "/"
    config = {
        **dotenv_values(),
        **dotenv_values(f"{path_file}.env.secret")
    }
    
    load_env_vars()

    all_env_vars_configured = True
    for env_var in config:
        if not getenv(env_var):
            all_env_vars_configured = False

    assert all_env_vars_configured