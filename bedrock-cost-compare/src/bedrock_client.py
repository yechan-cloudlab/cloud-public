"""Minimal Bedrock Runtime client wrapper.

This file is intentionally small. It is provided as a reference point for where
model routing output would be connected to a real Bedrock Runtime invocation.
Do not run this against production prompts without logging, masking, and budget controls.
"""

from __future__ import annotations

import json
from typing import Any, Dict

import boto3


class BedrockClaudeClient:
    def __init__(self, region_name: str = "us-east-1") -> None:
        self.client = boto3.client("bedrock-runtime", region_name=region_name)

    def invoke_messages_api(self, model_id: str, prompt: str, max_tokens: int = 1024) -> Dict[str, Any]:
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }

        response = self.client.invoke_model(
            modelId=model_id,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json",
        )
        return json.loads(response["body"].read())
