import json
import requests
from core.dotenv_util import DotEnvGetter


class Request:
    """
    A wrapper around the requests.Session object for performing HTTP requests.

    This class handles the creation of a requests session and the sending of HTTP requests.
    If the USE_PROXY environment variable is set to True, the session will use the specified proxy URL.
    Currently, only GET requests are supported.

    ...

    Attributes
    ----------
    __session : requests.Session
        The requests session to use for sending HTTP requests.

    Methods
    -------
    get(url: str, payload: dict = None, return_whole_response=False)
        Sends a GET request to the specified URL with an optional payload.

    __send(url, request_type, payload: dict, headers=None)
        Sends a HTTP request of the specified type to the specified URL with an optional payload and headers.
    """

    def __init__(self):
        """
        Initializes the Request object and creates a new requests session.
        If the USE_PROXY environment variable is set to True, the session will use the specified proxy URL.
        """
        self.__session = requests.session()
        if DotEnvGetter().use_proxy:
            proxy_url = DotEnvGetter().proxy_url
            self.__session.proxies = {
                'http': proxy_url,
                'https': proxy_url
            }

    def get(self, url: str, payload: dict = None, return_whole_response=False):
        """
        Sends a GET request to the specified URL with an optional payload.

        If return_whole_response is True, the whole response object will be returned;
        otherwise, only the JSON response content will be returned.

        Parameters
        ----------
        url : str
            The URL to send the GET request to.
        payload : dict, optional
            The payload to send with the GET request.
        return_whole_response : bool, optional
            Whether to return the whole response object.

        Returns
        -------
        response
            The response to the GET request. Depending on the value of return_whole_response,
            this may be the whole response object or just the JSON response content.
        """
        return self.__send(url, "GET", payload, return_whole_response)

    def __send(self, url, request_type, payload: dict, headers=None):
        """
        Sends a HTTP request of the specified type to the specified URL with an optional payload and headers.

        If the HTTP request is successful (i.e., the response status code is 200), the response is returned.
        Otherwise, an exception is raised.

        Parameters
        ----------
        url : str
            The URL to send the HTTP request to.
        request_type : str
            The type of HTTP request to send (e.g., "GET").
        payload : dict, optional
            The payload to send with the HTTP request.
        headers : dict, optional
            The headers to send with the HTTP request.

        Returns
        -------
        response
            The response to the HTTP request.

        Raises
        ------
        Exception
            If the HTTP request is unsuccessful (i.e., the response status code is not 200).
        """
        response = self.__session.request(request_type, url, headers=headers, data=payload)

        if response.status_code == 200:
            return response
        raise Exception(f"Got {response.status_code} while sending request")
