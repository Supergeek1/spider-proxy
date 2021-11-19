import threading
import sys

from config.settings import REDIS_PORT, REDIS_HOST, REDIS_DB, UPDATE_QUEUE_KEY, REST_QUEUE_PREFIX, UPDATER_NAME
from util.redis_util import RedisUtil
from util.updater_util import UpdateUtil


class UpdateRedisLister:

    def __init__(self) -> None:
        self.redis_client = RedisUtil.get_redis_client(REDIS_HOST, REDIS_PORT, REDIS_DB)
        self.redis_key_prefix = UpdateUtil.generate_expire_prefix()

    def start_expired_listen_thread(self):
        t = threading.Thread(target=self._sub_expired)
        t.start()

    def _sub_expired(self):
        pub = self.redis_client.pubsub()  # Return a Publish/Subscribe object.
        pub.subscribe('__keyevent@' + str(REDIS_DB) + '__:expired')
        for msg in pub.listen():
            try:
                redis_key_data: str = msg['data']
                if type(redis_key_data) == str and redis_key_data.startswith(self.redis_key_prefix):
                    proxy = redis_key_data.replace(self.redis_key_prefix, '')
                    pipeline = self.redis_client.pipeline()
                    for key in UPDATE_QUEUE_KEY:
                        pipeline.zrem(REST_QUEUE_PREFIX + key, proxy)
                    pipeline.hdel(UpdateUtil.generate_track_key(), proxy)
                    pipeline.execute()
                    print('RedisListen -> remove expired app[' + UPDATER_NAME + ']: ' + proxy)
            except Exception as e:
                print(e)
                sys.exit()

