from sys import argv
from pprint import pformat

from twisted.internet.task import react
from twisted.web.client import Agent, readBody
from twisted.web.http_headers import Headers


from twisted.python import log
from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent, ContentDecoderAgent, GzipDecoder

from pprint import pformat

from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from sys import argv
from pprint import pformat
from twisted.internet.task import react
from twisted.internet.ssl import optionsForClientTLS
from zope.interface import implementer
from twisted.web.iweb import IPolicyForHTTPS
from twisted.web.client import Agent, ResponseFailed, BrowserLikePolicyForHTTPS
from twisted.internet.task import react
from twisted.web.client import Agent, readBody
from twisted.web.http_headers import Headers


@implementer(IPolicyForHTTPS)
class OneHostnameWorkaroundPolicy(object):
    def __init__(self):
        self._normalPolicy = BrowserLikePolicyForHTTPS()
    def creatorForNetloc(self, hostname, port):
        if hostname == 'httpbin.org':
            hostname = 'httpbin.org'
        return self._normalPolicy.creatorForNetloc(hostname, port)


def cbRequest(response):
    print('Response version:', response.version)
    print('Response code:', response.code)
    print('Response phrase:', response.phrase)
    print('Response headers:')
    print(pformat(list(response.headers.getAllRawHeaders())))
    d = readBody(response)
    d.addCallback(cbBody)
    return d


def cbBody(body):
    print('Response body:')
    print(body)


@react
def main(reactor, url=b"http://httpbin.org/get"):
    #agent = Agent(reactor)
    agent = Agent(reactor, OneHostnameWorkaroundPolicy())
    d = agent.request(
        b'GET', url,
        Headers({'User-Agent': ['Twisted Web Client Example']}),
        None)
    d.addCallback(cbRequest)
    return d
