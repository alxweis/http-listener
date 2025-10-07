import argparse
import socket
import sys
from datetime import datetime

import requests
from flask import Flask, request

parser = argparse.ArgumentParser(description="Simple HTTP Listener")
parser.add_argument("--port", type=int, required=True)
parser.add_argument("--endpoint", type=str, required=True)
args = parser.parse_args()

app = Flask(__name__)


def is_port_open(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.bind(("0.0.0.0", port))
        s.close()
        return True
    except OSError:
        return False


def has_public_ip():
    try:
        ip = requests.get("https://api.ipify.org", timeout=5).text.strip()
        private_prefixes = ("10.", "172.", "192.168.", "127.")
        if any(ip.startswith(p) for p in private_prefixes):
            return None
        return ip
    except Exception:
        return None


@app.route(f"/{args.endpoint}", methods=["POST", "GET"])
def listener():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{ts}] {request.method} received")
    print(f"Headers: {dict(request.headers)}")
    print(f"Body: {request.data.decode() if request.data else '(no body)'}")
    return "", 200


if __name__ == "__main__":
    public_ip = has_public_ip()
    if not public_ip:
        print("Error: No public IP detected or network not reachable.")
        sys.exit(1)

    if not is_port_open(args.port):
        print(f"Error: Port {args.port} is not available or already in use.")
        sys.exit(1)

    print(f"Listening on http://{public_ip}:{args.port}/{args.endpoint}")
    app.run(host="0.0.0.0", port=args.port, debug=False, use_reloader=False)
