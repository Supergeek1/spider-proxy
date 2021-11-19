import threading

from config.settings import REDIS_PORT, REDIS_HOST, REDIS_DB, REST_INTERVAL_PREFIX
from util.redis_util import RedisUtil
from util.rest_util import RestUtil


class RedisListen:

    def __init__(self, redis_key_prefix=REST_INTERVAL_PREFIX) -> None:
        self.redis_client = RedisUtil.get_redis_client(REDIS_HOST, REDIS_PORT, REDIS_DB)
        self.redis_key_prefix = redis_key_prefix

    def listen_expired(self):
        t = threading.Thread(target=self._sub_expired)
        t.setDaemon(True)
        t.start()

    def _sub_expired(self):
        pub = self.redis_client.pubsub()  # Return a Publish/Subscribe object.
        pub.subscribe('__keyevent@' + str(REDIS_DB) + '__:expired')
        for msg in pub.listen():
            try:
                redis_key_data = msg['data']
                if isinstance(redis_key_data, bytes):
                    data_key = redis_key_data.decode()
                    if data_key.startswith(self.redis_key_prefix):
                        proxy_info = data_key.replace(self.redis_key_prefix, '')
                        idx = proxy_info.index(':')
                        queue_key = proxy_info[:idx]
                        proxy_info = proxy_info[idx + 1:]
                        idx = proxy_info.index(':')
                        speed = int(proxy_info[:idx])
                        proxy = proxy_info[idx + 1:]
                        self.redis_client.zadd(RestUtil.generate_rest_queue(queue_key), {proxy: speed})
                        print('ReidsListen -> add proxy to rest queue[' + queue_key + ']: ' + proxy)
            except Exception as e:
                print(e)
