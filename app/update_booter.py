from updater.proxy_updater import ProxyUpdater
from updater.update_redis_lister import UpdateRedisLister

if __name__ == "__main__":
    ProxyUpdater().start_update_thread()
    UpdateRedisLister().start_expired_listen_thread()
