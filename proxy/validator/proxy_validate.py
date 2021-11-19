import requests
from requests import Response


class ProxyValidator:

    @staticmethod
    def validate(proxy, validate_url, validate_keys, success_action: classmethod, failed_action: classmethod):
        pass

    @staticmethod
    def is_succeed(response: Response, test_keys: list):
        if response.status_code != requests.codes.ok:
            return False
        res_data = response.text
        is_ok = not not res_data
        index = 0
        while is_ok and index < len(test_keys):
            is_ok = test_keys[index] in res_data
            index = index + 1
        return is_ok
