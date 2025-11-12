FROM python:3.11-slim

WORKDIR /app

# 1️⃣ Install system deps + pip dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential && \
    pip install --upgrade pip && \
    pip install --no-cache-dir litellm uvicorn fastapi python-dotenv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY config/config.yaml /app/config.yaml

EXPOSE 8000

CMD ["litellm", "--config", "/app/config.yaml", "--port", "8000"]