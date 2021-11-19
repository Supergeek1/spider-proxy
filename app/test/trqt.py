from treq import get


def done(response):
    print(response.code)
    reactor.stop()

def eb(e):
    print(e)
    reactor.stop()


get("https://httpbin.org/get").addCallback(done).addErrback(eb)

from twisted.internet import reactor

reactor.run()
