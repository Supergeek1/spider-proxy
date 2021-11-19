import logging

from config.settings import REST_QUEUE_CONF, REST_QUEUE_COMMON, PROXY_USAGE_TYPE_ROUND, PROXY_USAGE_INTERVAL
from rest.proxy_manager import ProxyManager
from rest.redis_listen import RedisListen


class ProxyService:
    def __init__(self, manage: ProxyManager):
        self.manager = manage
        self.redis_listen = RedisListen()
        self.redis_listen.listen_expired()

    def get_proxy(self, queue_key) -> list:
        if not queue_key or queue_key not in REST_QUEUE_CONF:
            queue_key = REST_QUEUE_COMMON
        result: list = None
        usage = REST_QUEUE_CONF.get(queue_key)
        if PROXY_USAGE_TYPE_ROUND == usage:
            result = self.manager.get_proxy_round(queue_key)
        elif PROXY_USAGE_INTERVAL in usage:
            result = self.manager.get_proxy_interval(queue_key, int(usage[usage.index('_') + 1:]))
        else:
            logging.error('error queue_key: ' + queue_key)
        return result

    def get_proxies(self, queue_key) -> list:
        result: list = []
        if not queue_key or queue_key not in REST_QUEUE_CONF:
            logging.error('error queue_key: ' + queue_key)
            result.append('key Not found')
        else:
            proxies = self.manager.get_proxies(queue_key)
            for proxy in proxies:
                result.append(proxy.decode())
        return result
