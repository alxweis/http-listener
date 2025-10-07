# HTTP Listener

Minimal Python script to log incoming HTTP requests.

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python http_listener.py --port 1234 --endpoint my_endpoint
```

Example output:

```
Listening on http://89.0.123.45:1234/my_endpoint
[2025-10-07 14:21:33] POST received
Headers: {...}
Body: {"test": "data"}
```

## Build

```bash
pyinstaller --onefile http_listener.py --name http_listener
```

Executable in `dist/`.
