import argparse
import sys
sys.path.append('/app/app')

from config.settings import REST_PORT
from rest import rest as app

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=REST_PORT)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()
    app.run(port=args.port, host=args.host)
