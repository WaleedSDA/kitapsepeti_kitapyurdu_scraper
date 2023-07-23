import os

from core.singleton_metaclass import Singleton
from dotenv import load_dotenv


class DotEnvGetter(metaclass=Singleton):
    """
    A singleton class used to load and get environment variables.

    This class utilizes the singleton design pattern to ensure that the .env file is only loaded once,
    regardless of the number of instances of this class that are created.

    ...

    Properties
    ----------
    db_uri : str
        The URI of the database, obtained from the DB_URI environment variable.
    db_name : str
        The name of the database, obtained from the DB_NAME environment variable.
    proxy_url : str
        The URL of the proxy, obtained from the PROXY_URL environment variable.
    use_proxy : bool
        A boolean value indicating whether to use the proxy or not, obtained from the USE_PROXY environment variable.

    """

    def __init__(self):
        """
        Initializes the DotEnvGetter and loads the .env file.
        """
        load_dotenv()

    @property
    def db_uri(self):
        """
        The URI of the database, obtained from the DB_URI environment variable.

        Returns
        -------
        str
            The URI of the database.
        """
        return os.getenv("DB_URI")

    @property
    def db_name(self):
        """
        The name of the database, obtained from the DB_NAME environment variable.

        Returns
        -------
        str
            The name of the database.
        """
        return os.getenv("DB_NAME")

    @property
    def proxy_url(self):
        """
        The URL of the proxy, obtained from the PROXY_URL environment variable.

        Returns
        -------
        str
            The URL of the proxy.
        """
        return os.getenv("PROXY_URL")

    @property
    def use_proxy(self):
        """
        A boolean value indicating whether to use the proxy or not, obtained from the USE_PROXY environment variable.

        Returns
        -------
        bool
            Whether to use the proxy or not.
        """
        result = os.getenv("USE_PROXY")
        return True if result == "True" else False
