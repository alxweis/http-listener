import argparse
from datetime import datetime

import requests
from flask import Flask, request

# Parse CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=5000, help="Port number")
parser.add_argument("--endpoint", type=str, default="webhook", help="Endpoint path")
args = parser.parse_args()

app = Flask(__name__)


@app.route(f"/{args.endpoint}", methods=["POST", "GET"])
def webhook():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] Received request on /{args.endpoint}:")
    print(request.data.decode("utf-8") if request.data else "(no body)")
    return "OK", 200


if __name__ == "__main__":
    try:
        public_ip = requests.get("https://api.ipify.org").text.strip()
    except Exception:
        public_ip = "UNKNOWN"

    print(f"Server running on http://{public_ip}:{args.port}/{args.endpoint} (Ctrl+C to stop)")
    app.run(host="0.0.0.0", port=args.port)
