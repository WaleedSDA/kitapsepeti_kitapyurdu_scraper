import os

from core.singleton_metaclass import Singleton
from dotenv import load_dotenv


class DotEnvGetter(metaclass=Singleton):

    def __init__(self):
        load_dotenv()

    @property
    def db_uri(self):
        return os.getenv("DB_URI")

    @property
    def db_name(self):
        return os.getenv("DB_NAME")

    @property
    def proxy_url(self):
        return os.getenv("PROXY_URL")

    @property
    def use_proxy(self):
        result = os.getenv("USE_PROXY")
        return True if result == "True" else False
