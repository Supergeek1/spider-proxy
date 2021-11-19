import time

from config.settings import UPDATE_EXPIRED_LISTEN_PREFIX, UPDATER_NAME, UPDATE_PROXY_RECORD_KEY,UPDATE_TRACK_TIME_KEY


class UpdateUtil:

    @staticmethod
    def generate_expire_prefix(queue_key=UPDATER_NAME):
        return '{}:{}:'.format(UPDATE_EXPIRED_LISTEN_PREFIX, queue_key)

    @staticmethod
    def generate_record_key():
        return '{}:{}:{}'.format(UPDATE_PROXY_RECORD_KEY, UPDATER_NAME, time.strftime('"%Y%m%d'))

    @staticmethod
    def generate_track_key():
        return '{}:{}'.format(UPDATE_TRACK_TIME_KEY, UPDATER_NAME)
