from flask import (Flask, jsonify as flask_jsonify)

from rest.proxy_service import ProxyManager
from rest.proxy_service import ProxyService

rest = Flask(__name__)
proxy_service: ProxyService = ProxyService(ProxyManager())


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
    proxy_info = proxy_service.get_proxy(queue_key)
    if not proxy_info:
        return jsonify({
            'proxy': None,
            'score': None,
            'return_code': 10000,  # 没有可用代理
            'status_code': 200
        })

    return jsonify({
        'proxy': proxy_info[0].decode(),
        'score': proxy_info[1].decode(),
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
