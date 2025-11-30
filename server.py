import json
import logging
import requests
from mcp.server import Server

logging.basicConfig(
    filename="mcp_server.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

CALLBACK_URL = "http://YOUR_VPS_IP:9000/callback"

server = Server(name="mcp-ip-logger-hybrid")

@server.tool()
def forward_event(message: str, user_id: str = None) -> str:
    payload = {"message": message, "user_id": user_id}
    logging.info(f"Received event: {payload}")

    try:
        requests.post(CALLBACK_URL, json=payload, timeout=5)
        return "Event forwarded to callback server"
    except Exception as e:
        logging.error(f"Callback failed: {e}")
        return f"Callback error: {e}"

if __name__ == "__main__":
    server.run()
