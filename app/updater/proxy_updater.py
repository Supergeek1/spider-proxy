import threading
import time

import requests
from config.settings import *


class ProxyUpdater:

    def __init__(self) -> None:
        self.api_url = UPDATE_API_URL
        self.update_interval = UPDATE_INTERVAL

    def start_update_thread(self):
        t = threading.Thread(target=self.update_proxy)
        t.start()

    def update_proxy(self):
        while True:
            self._update_proxy()
            time.sleep(self.update_interval)

    def _update_proxy(self) -> int:
        count = 0
        data = None
        try:
            res = requests.get(self.api_url)
            if UPDATE_PROXY_API_DATA_FORMAT == 'json':
                data = res.json()
            else:
                data = res.text
            proxy_data = eval(UPDATE_PROXY_DATA_KEY)

            for proxy_info in proxy_data:
                try:
                    if proxy_info:
                        proxy = ProxyUpdater.parse_proxy(proxy_info)
                        for key in UPDATE_QUEUE_KEY:
                            print(key)
                        count = count + 1
                except Exception as e:
                    print('update proxy_info[{}] error: {}'.format(str(proxy_info), str(e)))
            print('TestProxyUpdater get {} app from TEST API'.format(count))
            return count
        except Exception as e:
            print('update TEST proxy_data[{}] error: {}'.format(str(data), str(e)))
            return count

    @staticmethod
    def parse_proxy(proxy_info):
        UPDATE_PROXY_PARSE_METHOD = 'http://{}:{}'.format(proxy_info['ip'], proxy_info['port'])
        return eval(UPDATE_PROXY_PARSE_METHOD)
