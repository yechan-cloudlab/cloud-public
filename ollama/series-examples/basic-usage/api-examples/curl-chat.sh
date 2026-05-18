#!/usr/bin/env bash
set -euo pipefail

curl http://localhost:11434/api/chat \
  -d '{
    "model": "gemma3",
    "messages": [
      {"role": "user", "content": "What is local inference?"}
    ],
    "stream": false
  }'
