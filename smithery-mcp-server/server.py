import json
import logging
import requests
from mcp.server import Server

# Configure logging on Smithery side
logging.basicConfig(
    filename="mcp_server.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Your VPS callback endpoint
CALLBACK_URL = "http://YOUR_VPS_IP:9000/callback"

server = Server(name="mcp-ip-logger-hybrid")

@server.tool()
def forward_event(message: str, user_id: str = None) -> str:
    """
    Client triggers this tool.
    Smithery runs it.
    This server forwards the data to your VPS endpoint.
    """

    payload = {
        "message": message,
        "user_id": user_id
    }

    logging.info(f"Received event: {payload}")

    try:
        # send to VPS
        requests.post(CALLBACK_URL, json=payload, timeout=5)
        return "Event forwarded to callback server"
    except Exception as e:
        logging.error(f"Callback failed: {e}")
        return f"Callback error: {e}"

if __name__ == "__main__":
    server.run()
