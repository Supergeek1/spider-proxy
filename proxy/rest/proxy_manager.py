from config.settings import REDIS_PORT, REDIS_HOST, REDIS_DB, REST_INTERVAL_PREFIX
from util.redis_util import RedisUtil
from util.rest_util import RestUtil


class ProxyManager:

    def __init__(self):
        self.redis_client = RedisUtil.get_redis_client(REDIS_HOST, REDIS_PORT, REDIS_DB)

    def get_proxies(self, queue_key: str):
        redis_key = RestUtil.generate_rest_queue(queue_key)
        return self.redis_client.zrange(redis_key, 0, 1)

    def get_proxy_round(self, queue_key: str) -> list:
        redis_key = RestUtil.generate_rest_queue(queue_key)
        queue_b = RestUtil.generate_rest_queue_b(queue_key)
        lua_script = """
                    local proxy_info_list = redis.call('ZRANGE',KEYS[1], 0, 0,'WITHSCORES')
                    if(#proxy_info_list == 0)then
                        local proxy_info_list_b = redis.call('ZRANGE',KEYS[2], 0, -1,'WITHSCORES')
                        if(#proxy_info_list_b == 0)then
                            return nil
                        end
                        if(#proxy_info_list_b > 2)then
                            for i=3,#proxy_info_list_b,2 do  
                                redis.call('ZADD', KEYS[1], proxy_info_list_b[i+1], proxy_info_list_b[i])
                            end 
                        end
                        redis.call('DEL', KEYS[2])
                        proxy_info_list={proxy_info_list_b[1], proxy_info_list_b[2]}
                    else
                        redis.call('ZREM',KEYS[1], proxy_info_list[1])    
                    end
                    redis.call('ZADD', KEYS[2], proxy_info_list[2], proxy_info_list[1])
                    return proxy_info_list  
                    """
        return self.redis_client.eval(lua_script, 2, redis_key, queue_b)

    def get_proxy_interval(self, queue_key: str, interval_seconds: int) -> list:
        redis_key = RestUtil.generate_rest_queue(queue_key)
        interval_prefix = REST_INTERVAL_PREFIX + queue_key + ':'
        lua_script = """
                    local proxy_info_list = redis.call('ZRANGE',KEYS[1], 0, 0,'WITHSCORES')
                    if(#proxy_info_list == 0)then
                        return nil
                    end 
                    local proxy = proxy_info_list[1]
                    redis.call('ZREM',KEYS[1], proxy)
                    local redis_interval_key = \'""" + interval_prefix + """\' .. proxy_info_list[2] ..':'.. proxy
                    redis.call('SET', redis_interval_key, proxy)
                    redis.call('EXPIRE', redis_interval_key, KEYS[2])
                    return proxy_info_list  
                    """
        return self.redis_client.eval(lua_script, 2, redis_key, interval_seconds)
