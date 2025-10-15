# HTTP Listener

_Simple HTTP listener that prints incoming requests._

## Requirements

- A **public IP address** reachable from the internet
- The selected **port must be open and exposed** (e.g., via port forwarding or firewall settings)
- Ensure no other service is already using the same port

## Executables (Linux/Windows)

- See [releases](https://github.com/alxweis/http-listener/releases) for prebuilt executables for Linux and Windows.

## Source

### Additional Requirements

- Python 3.8 or higher

### Setup

**Linux**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

**Windows**
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
````

### Usage

**Linux**
```bash
python3 main.py --port 5555 --endpoint my_endpoint
```

**Windows**
```powershell
python main.py --port 5555 --endpoint my_endpoint
```

Example output:

```
Listening on http://89.0.123.45:5555/my_endpoint
[2025-10-07 14:21:33] POST received
Headers: {...}
Body: {"test": "data"}
```

### Build

```bash
pyinstaller --onefile main.py --name http-listener
```

Executable in `dist/`.
