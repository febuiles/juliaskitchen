FROM python:3.11.9-bookworm AS builder

RUN mkdir -p /app/models

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    OLLAMA_HOST="0.0.0.0" \
    OLLAMA_MODELS="/app/models"


RUN curl -sSL https://ollama.com/install.sh | bash
RUN bash -c "ollama serve > /dev/null 2>&1 & until curl -s http://localhost:11434 > /dev/null; do echo 'Waiting for ollama...'; sleep 1; done && ollama pull llama3"

WORKDIR /app

COPY requirements.txt .
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

COPY . .


FROM python:3.11-slim
RUN mkdir -p /app/models

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    OLLAMA_HOST="0.0.0.0" \
    OLLAMA_MODELS="/app/models"

RUN apt-get update -y && apt-get install -y curl

WORKDIR /app

RUN curl -sSL https://ollama.com/install.sh | bash

COPY --from=builder /app/.venv .venv/
COPY --from=builder /app /app

RUN chmod a+x start.sh
CMD ["./start.sh"]
