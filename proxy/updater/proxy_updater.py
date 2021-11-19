import json
import threading
import time

import requests

from config.settings import *
from util.redis_util import RedisUtil
from util.updater_util import UpdateUtil


class ProxyUpdater:

    def __init__(self) -> None:
        self.api_url = UPDATE_API_URL
        self.update_interval = UPDATE_INTERVAL
        self.redis_client = RedisUtil.get_redis_client(REDIS_HOST, REDIS_PORT, REDIS_DB)

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
            redis_pipeline = self.redis_client.pipeline()
            now_ms = int(time.time() * 1000)
            record_key = UpdateUtil.generate_record_key()
            record_proxies = record_key + ':proxies'
            record_count = record_key + ':count'
            proxy_expire_prefix = UpdateUtil.generate_expire_prefix()
            proxy_track_key = UpdateUtil.generate_track_key()
            for proxy_info in proxy_data:
                try:
                    if ProxyUpdater.filter_proxy(proxy_info):
                        proxy = ProxyUpdater.parse_proxy(proxy_info)
                        for key in UPDATE_QUEUE_KEY:
                            redis_pipeline.zadd(REST_QUEUE_PREFIX + key, {proxy: 3})

                        proxy_expire_key = proxy_expire_prefix + proxy
                        redis_pipeline.set(proxy_expire_key, json.dumps(proxy_info))
                        redis_pipeline.expire(proxy_expire_key, UPDATE_EXPIRE_TIME_DEFAULT)
                        redis_pipeline.hset(proxy_track_key, proxy, str(now_ms))
                        # record
                        redis_pipeline.hset(record_proxies, proxy, time.time_ns())
                        redis_pipeline.incrby(record_count)
                        count = count + 1
                    else:
                        print('error proxy: ' + str(proxy_info))
                except Exception as e:
                    print('update proxy_info[{}] error: {}'.format(str(proxy_info), str(e)))
            redis_pipeline.expire(record_proxies, UPDATE_PROXY_RECORD_EXPIRE)
            redis_pipeline.expire(record_count, UPDATE_PROXY_RECORD_EXPIRE)
            redis_pipeline.execute()
            print('TestProxyUpdater get {} proxy from TEST API'.format(count))
            return count
        except Exception as e:
            print('update TEST proxy_data[{}] error: {}'.format(str(data), str(e)))
            return count

    @staticmethod
    def parse_proxy(proxy_info):
        return eval(UPDATE_PROXY_PARSE_METHOD)

    @staticmethod
    def filter_proxy(proxy_info):
        return eval(UPDATE_PROXY_FILTER_METHOD)
