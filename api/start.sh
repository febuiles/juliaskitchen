#!/usr/bin/env bash

ollama serve & until curl -s http://localhost:11434 > /dev/null; do echo 'Waiting for ollama...'; sleep 1; done && ollama run llama3 ""

/app/.venv/bin/uvicorn api:app --host 0.0.0.0 --port 8000
