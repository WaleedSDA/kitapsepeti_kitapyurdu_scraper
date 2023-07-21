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

    def post(self, url: str, payload: dict = None, return_whole_response=False):

        return self.__send("POST", url, payload, return_whole_response)

    def get(self, url: str, payload: dict = None, return_whole_response=False):
        return self.__send("GET", url, payload, return_whole_response)

    def __send(self, url, request_type, payload: dict, return_whole_response, headers=None):
        response = self.__session.request(request_type, url, headers=headers, data=payload)

        if response.status_code == 200:
            if not return_whole_response:
                response_data = response.text
                return json.loads(response_data)
            return response
        raise f"Got {response.status_code} while sending request"
