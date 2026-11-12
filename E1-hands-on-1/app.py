"""E1 - hands-on 1: a minimal Flask app deployed on the local network.

Run:  python app.py            (defaults to port 2027)
      PORT=8080 python app.py  (or set the PORT variable in run.bat)
"""

import os
import socket

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

PORT = int(os.environ.get("PORT", "2027"))
PAGE_NAME = "hands-on 1"
STUDENT_ID = "124020402"
MESSAGE = "Hello, this is a web app deployed at a local server!"


def lan_ip() -> str:
    """Best-effort lookup of the interface IP other devices can reach."""
    for probe in ("8.8.8.8", "1.1.1.1"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.connect((probe, 80))  # UDP connect sends no packet
            ip = sock.getsockname()[0]
            if not ip.startswith("127."):
                return ip
        except OSError:
            pass
        finally:
            sock.close()
    try:
        return socket.gethostbyname(socket.gethostname())
    except OSError:
        return "127.0.0.1"


@app.route("/")
@app.route("/hands-on-1")
def hands_on_1():
    return render_template(
        "hands_on_1.html",
        page_name=PAGE_NAME,
        message=MESSAGE,
        port=PORT,
        server_ip=lan_ip(),
        client_ip=request.remote_addr,
        student_id=STUDENT_ID,
    )


@app.route("/api/info")
def api_info():
    return jsonify(
        page=PAGE_NAME,
        message=MESSAGE,
        student_id=STUDENT_ID,
        server_ip=lan_ip(),
        port=PORT,
        client_ip=request.remote_addr,
        url=f"http://{lan_ip()}:{PORT}",
    )


if __name__ == "__main__":
    ip = lan_ip()
    print(f" * Local:   http://127.0.0.1:{PORT}")
    print(f" * Network: http://{ip}:{PORT}")
    app.run(host="0.0.0.0", port=PORT, debug=False)
