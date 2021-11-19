import ast
import os

REDIS_HOST = os.getenv('REDIS_HOST', 'redis-proxy')
REDIS_PORT = int(os.getenv('REDIS_PORT', ))
REDIS_DB = int(os.getenv('REDIS_DB', 1))

REST_PORT = int(os.getenv('REST_PORT', 5055))

PROXY_USAGE_TYPE_ROUND = 'round'
PROXY_USAGE_INTERVAL = 'interval'

REST_QUEUE_COMMON = 'https'
REST_QUEUE_PREFIX = 'rest:queue:'
REST_QUEUE_ROUND_SUFFIX = '_b'
REST_INTERVAL_PREFIX = 'rest:interval:'

REST_QUEUE_CONF = {
    'all': 'round',
    'http': 'round',
    'https': 'round',
    'region.cn': 'round',
    'region.other': 'round',
}

REST_QUEUE_CUSTOM = ast.literal_eval(os.getenv('REST_QUEUE_CUSTOM', '{ \
    "weibo": "interval_10", \
    "sina": "interval_10", \
    "zhima": "round", \
    "five": "round" \
    }'))

REST_QUEUE_CONF.update(REST_QUEUE_CUSTOM)

REST_VALIDATE_URL = {
    'http': 'http://httpbin.org/ip',
    'https': 'https://httpbin.org/ip'
}
REST_VALIDATE_URL_CUSTOM = {

}
REST_VALIDATE_URL.update(REST_VALIDATE_URL_CUSTOM)
REST_VALIDATE_KEYS = {
    'http': 'origin',
    'https': 'origin'
}
REST_VALIDATE_KEYS_CUSTOM = {

}
REST_VALIDATE_KEYS.update(REST_VALIDATE_KEYS_CUSTOM)

UPDATER_NAME = os.getenv("UPDATER_NAME", "zhima")
UPDATE_API_URL = os.getenv('UPDATE_API_URL', '')
UPDATE_INTERVAL = int(os.getenv('UPDATE_INTERVAL', '20'))
UPDATE_TRACK_TIME_KEY = os.getenv('UPDATE_TRACK_TIME_KEY', 'updater:track')
UPDATE_EXPIRE_TIME_DEFAULT = int(os.getenv('UPDATE_EXPIRE_TIME_DEFAULT', '30'))
UPDATE_PROXY_DATA_KEY = os.getenv('UPDATE_PROXY_DATA_KEY', "data['data']")
UPDATE_PROXY_API_DATA_FORMAT = os.getenv('UPDATE_PROXY_API_DATA_FORMAT', 'json')
UPDATE_PROXY_PARSE_METHOD = os.getenv('UPDATE_PROXY_PARSE_METHOD',
                                      "'http://{}:{}'.format(proxy_info['ip'], proxy_info['port'])")
UPDATE_PROXY_FILTER_METHOD = os.getenv('UPDATE_PROXY_FILTER_METHOD', "proxy_info")
UPDATE_QUEUE_KEY = [x.strip() for x in os.getenv('UPDATE_QUEUE_KEY', 'all, zhima').split(',')]

UPDATE_PROXY_RECORD_EXPIRE = os.getenv('UPDATE_PROXY_RECORD_EXPIRE', '259200')  # 3days
UPDATE_PROXY_RECORD_KEY = os.getenv('UPDATE_PROXY_RECORD_KEY', 'updater:record')

UPDATE_EXPIRED_LISTEN_PREFIX = os.getenv("UPDATE_EXPIRED_LISTEN_PREFIX", "updater:expire")
