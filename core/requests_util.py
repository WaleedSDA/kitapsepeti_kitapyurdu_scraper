import json
import requests
from core.dotenv_util import DotEnvGetter


class Request:

    def __init__(self):
        self.__session = requests.session()
        if DotEnvGetter().use_proxy:
            proxy_url = DotEnvGetter().proxy_url
            self.__session.proxies = {
                'http': proxy_url,
                'https': proxy_url
            }

    def get(self, url: str, payload: dict = None, return_whole_response=False):
        return self.__send(url, "GET", payload, return_whole_response)

    def __send(self, url, request_type, payload: dict, headers=None):
        response = self.__session.request(request_type, url, headers=headers, data=payload)

        if response.status_code == 200:
            return response
        raise f"Got {response.status_code} while sending request"
