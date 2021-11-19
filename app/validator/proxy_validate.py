import requests
import base64
from requests import Response
from requests.auth import HTTPBasicAuth


class ProxyValidator:

    @staticmethod
    def validate(proxy, validate_url, validate_keys, success_action: classmethod, failed_action: classmethod):
        pass

    @staticmethod
    def validate_proxy(validate_url, proxy, test_keys) -> bool:
        result: bool = False
        try:

            res = ProxyValidator.get_response(validate_url, proxy)
            result = ProxyValidator.is_succeed(res, test_keys)
        except Exception as e:
            print(str(e))

        return result

    @staticmethod
    def is_succeed(response: Response, test_keys: list) -> bool:
        if response.status_code != requests.codes.ok:
            return False
        res_data = response.text
        is_ok = not not res_data
        index = 0
        while is_ok and index < len(test_keys):
            is_ok = test_keys[index] in res_data
            index = index + 1
        return is_ok

    @staticmethod
    def get_response(request_url: str, proxy: str) -> Response:
        proxies = {
            'http': proxy,
            'https': proxy,
        }
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'

        }
        return requests.get(request_url, proxies=proxies, headers=headers, timeout=10)

    @staticmethod
    def read_urls(file_path) -> list:
        f = open(file_path, 'r')
        result = list()
        for line in f.readlines():  # 依次读取每行
            result.append(line.strip())  # 保存
        print('read {} url'.format(len(result)))
        f.close()
        return result
