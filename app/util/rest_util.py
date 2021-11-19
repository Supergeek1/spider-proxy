from config.settings import REST_QUEUE_PREFIX, REST_QUEUE_ROUND_SUFFIX


class RestUtil:

    @staticmethod
    def generate_rest_queue(queue_key: str):
        return REST_QUEUE_PREFIX + queue_key

    @staticmethod
    def generate_rest_queue_b(queue_key: str):
        return REST_QUEUE_PREFIX + queue_key + REST_QUEUE_ROUND_SUFFIX
