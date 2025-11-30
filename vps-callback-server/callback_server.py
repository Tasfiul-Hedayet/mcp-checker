from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="callback.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@app.post("/callback")
def callback():
    data = request.json
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    logging.info(f"Received payload: {data}")
    logging.info(f"Client IP: {ip}")

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
