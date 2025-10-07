import argparse
from datetime import datetime

import requests
from flask import Flask, request

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
parser.add_argument("--endpoint", type=str, required=True)
args = parser.parse_args()

app = Flask(__name__)


@app.route(f"/{args.endpoint}", methods=["POST", "GET"])
def listener():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{ts}] {request.method} received:")
    print(f"Headers: {dict(request.headers)}")
    print(f"Body: {request.data.decode() if request.data else '(no body)'}")
    print()
    return "", 200


if __name__ == "__main__":
    try:
        ip = requests.get("https://api.ipify.org").text.strip()
    except:
        ip = "UNKNOWN"

    print(f"Listening on http://{ip}:{args.port}/{args.endpoint}")
    app.run(host="0.0.0.0", port=args.port, debug=False, use_reloader=False)
