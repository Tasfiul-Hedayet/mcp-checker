# VPS Callback Server

Receives events from Smithery MCP and logs data + client IP.

## Run locally
pip install -r requirements.txt
python callback_server.py

## Docker
docker build -t callback-server .
docker run -p 9000:9000 callback-server
