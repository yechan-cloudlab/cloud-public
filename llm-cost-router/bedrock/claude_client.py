import json
import os

import boto3
from dotenv import load_dotenv

load_dotenv()


class BedrockClaudeClient:
    def __init__(self, model_id: str | None = None, region_name: str | None = None) -> None:
        self.model_id = model_id or os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-5-sonnet-20240620-v1:0")
        self.region_name = region_name or os.getenv("AWS_REGION", "us-east-1")
        self.client = boto3.client("bedrock-runtime", region_name=self.region_name)

    def chat(self, prompt: str) -> str:
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1024,
            "messages": [
                {
                    "role": "user",
                    "content": [{"type": "text", "text": prompt}],
                }
            ],
        }

        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json",
        )
        payload = json.loads(response["body"].read())
        return payload["content"][0]["text"]
