import logging
import random

from flask import (Flask, jsonify as flask_jsonify)

from rest.proxy_service import ProxyManager
from rest.proxy_service import ProxyService

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

proxy_manager = ProxyManager()
proxy_service: ProxyService = ProxyService(proxy_manager)
rest = Flask(__name__)


def jsonify(*args, **kwargs):
    response = flask_jsonify(*args, **kwargs)
    if not response.data.endswith(b"\n"):
        response.data += b"\n"
    return response


@rest.errorhandler(404)
def not_found(e):
    return jsonify({
        'reason': 'resource not found',
        'status_code': 404
    })


@rest.errorhandler(500)
def not_found(e):
    return jsonify({
        'reason': 'internal server error',
        'status_code': 500
    })


@rest.route("/proxy/<queue_key>")
def get_proxy(queue_key):
    proxy_queue: list = proxy_service.get_proxy(queue_key)
    proxy = proxy_queue.pop(0)
    # luminati 代理: http://lum-customer-wisers-zone-icp_us_hk-session-{}:ymg4kj2r5dh5@zproxy.luminati.io:22225
    if proxy and ('lum' in queue_key or 'lum' in proxy):
        proxy = proxy.format(random.random())

    proxy_queue.append(proxy)

    if not proxy:
        return jsonify({
            'proxy': None,
            'score': None,
            'return_code': 10000,  # 没有可用代理
            'status_code': 200
        })

    logging.info('/proxy/' + queue_key + '   proxy[%s]' % proxy)
    return jsonify({
        'proxy': proxy,
        'score': 999,
        'return_code': 50000,
        'status_code': 200
    })


@rest.route("/test/<test_key>")
def test(test_key):
    result = proxy_service.test(test_key)

    return jsonify({
        'test_result': result,
        'return_code': 50000,
        'status_code': 200
    })


@rest.route("/pool/<queue_key>")
def get_proxies(queue_key):
    proxies = proxy_service.get_proxies(queue_key)
    if not proxies:
        return jsonify({
            'proxies': [],
            'return_code': 10000,  # 没有可用代理
            'status_code': 200
        })
    return jsonify({
        'proxies': proxies,
        'status_code': 200
    })


@rest.route("/pool/detail/<queue_key>")
def get_proxies_detail(queue_key):
    proxies = proxy_service.get_proxies_detail(queue_key)
    if not proxies:
        return jsonify({
            'proxies': [],
            'return_code': 10000,  # 没有可用代理
            'status_code': 200
        })
    return jsonify({
        'proxies': proxies,
        'status_code': 200
    })
