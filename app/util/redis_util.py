from redis import Redis


class RedisUtil:

    @staticmethod
    def get_redis_client(host: str, port: int, database: int, **kwargs) -> Redis:
        return Redis(host, port, database, password=kwargs.get('password', None),
                     decode_responses= True)
