import sys

from twisted.internet.task import react
from twisted.web.client import Agent, ResponseFailed, BrowserLikePolicyForHTTPS
from twisted.web.iweb import IPolicyForHTTPS
from zope.interface import implementer


@implementer(IPolicyForHTTPS)
class OneHostnameWorkaroundPolicy(object):
    def __init__(self):
        self._normalPolicy = BrowserLikePolicyForHTTPS()

    def creatorForNetloc(self, hostname, port):
        if hostname == b"www.cnblogs.com":
            hostname = b"www.cnblogs.com"
        return self._normalPolicy.creatorForNetloc(hostname, port)


@react
def main(reactor):
    agent = Agent(reactor, OneHostnameWorkaroundPolicy())
    requested = agent.request(b"GET", b"http://www.cnblogs.com/PatrickLiu/p/8656675.html")

    def gotResponse(response):
        print(response.code)

    def noResponse(failure):
        failure.trap(ResponseFailed)
        print(failure.value.reasons[0].getTraceback())

    return requested.addCallbacks(gotResponse, noResponse)
