from fake_useragent import UserAgent
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.python.log import err
from twisted.web._newclient import Response
from twisted.web.client import ProxyAgent, Headers
from twisted.internet.protocol import Protocol
import json
from twisted.test.proto_helpers import (
    AccumulatingProtocol,
    EventLoggingObserver,
    StringTransport,
    StringTransportWithDisconnection,
    )

ua = UserAgent()


def display(response: Response):
    print('Received response')
    protocol = AccumulatingProtocol()
    print(response.deliverBody(protocol))


def main():
    headers = Headers({'User-Agent': [ua.random]})
    endpoint = TCP4ClientEndpoint(reactor, '58.218.200.223', 4324)
    agent = ProxyAgent(endpoint)
    d = agent.request('GET'.encode(), 'http://httpbin.org/ip'.encode(), headers)
    d.addCallbacks(display, err)
    d.addCallback(lambda ignored: reactor.stop())
    reactor.run()
    print('ss')


if __name__ == '__main__':
    main()
