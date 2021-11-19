import argparse

from config.settings import REST_PORT
from rest import rest

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=REST_PORT)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()
    rest.run(port=args.port, host=args.host)
