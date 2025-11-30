FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY callback_server.py .

EXPOSE 9000

CMD ["gunicorn", "--bind", "0.0.0.0:9000", "callback_server:app"]
