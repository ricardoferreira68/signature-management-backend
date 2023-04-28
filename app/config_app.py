"""Application configuration file
"""

from dotenv import load_dotenv
from os import path


def load_env_vars():
    path_file = path.dirname(__file__) + "/"
    # print(f'path: {path_file}')
    load_dotenv()
    load_dotenv(f"{path_file}.env.secret")
