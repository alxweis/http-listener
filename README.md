# HTTP Listener

Minimal Python script to log incoming HTTP requests.

> See [releases](https://github.com/alxweis/http-listener/releases) for prebuilt executables for Linux and Windows.

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python http_listener.py --port 5555 --endpoint my_endpoint
```

Example output:

```
Listening on http://89.0.123.45:5555/my_endpoint
[2025-10-07 14:21:33] POST received
Headers: {...}
Body: {"test": "data"}
```

## Build

```bash
pyinstaller --onefile http_listener.py --name http-listener
```

Executable in `dist/`.
