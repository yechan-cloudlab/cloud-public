import json
import os
import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any

import boto3

bedrock_runtime = boto3.client("bedrock-runtime")
dynamodb = boto3.resource("dynamodb")


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Count input tokens, call Amazon Bedrock, and return the answer with usage metadata."""
    request_id = getattr(context, "aws_request_id", None) or str(uuid.uuid4())
    try:
        request = _parse_event(event)
    except ValueError as exc:
        return _response(400, {"request_id": request_id, "message": str(exc)})

    user_id = str(request.get("user_id", "anonymous"))
    prompt = str(request.get("prompt", "")).strip()
    model_id = str(request.get("model_id") or os.environ.get("DEFAULT_MODEL_ID", ""))
    max_input_tokens = int(os.environ.get("MAX_INPUT_TOKENS", "2000"))

    if not prompt:
        return _response(400, {"message": "prompt is required"})
    if not model_id:
        return _response(400, {"message": "model_id is required or DEFAULT_MODEL_ID must be set"})

    messages = [{"role": "user", "content": [{"text": prompt}]}]
    estimated_input_tokens = _count_input_tokens(model_id, messages)

    if estimated_input_tokens > max_input_tokens:
        usage = {
            "estimated_input_tokens": estimated_input_tokens,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": estimated_input_tokens,
        }
        _log_usage(request_id, user_id, model_id, usage, blocked=True)
        return _response(
            413,
            {
                "request_id": request_id,
                "user_id": user_id,
                "model_id": model_id,
                "message": "estimated input tokens exceed MAX_INPUT_TOKENS",
                "usage": usage,
            },
        )

    bedrock_response = bedrock_runtime.converse(
        modelId=model_id,
        messages=messages,
        inferenceConfig={
            "maxTokens": int(request.get("max_tokens", os.environ.get("DEFAULT_MAX_OUTPUT_TOKENS", "512"))),
            "temperature": float(request.get("temperature", os.environ.get("DEFAULT_TEMPERATURE", "0.2"))),
            "topP": float(request.get("top_p", os.environ.get("DEFAULT_TOP_P", "0.9"))),
        },
    )

    answer = _extract_answer(bedrock_response)
    actual_usage = bedrock_response.get("usage", {})
    input_tokens = int(actual_usage.get("inputTokens", estimated_input_tokens))
    output_tokens = int(actual_usage.get("outputTokens", 0))
    total_tokens = int(actual_usage.get("totalTokens", input_tokens + output_tokens))
    usage = {
        "estimated_input_tokens": estimated_input_tokens,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
    }

    record = {
        "request_id": request_id,
        "user_id": user_id,
        "model_id": model_id,
        "estimated_input_tokens": estimated_input_tokens,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _save_usage(record)
    _log_usage(request_id, user_id, model_id, usage, blocked=False)

    return _response(
        200,
        {
            "request_id": request_id,
            "user_id": user_id,
            "model_id": model_id,
            "answer": answer,
            "usage": usage,
        },
    )


def _parse_event(event: dict[str, Any]) -> dict[str, Any]:
    if "body" not in event:
        return event
    body = event.get("body")
    if body is None:
        return {}
    if isinstance(body, dict):
        return body
    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        raise ValueError("event body must be valid JSON") from exc


def _count_input_tokens(model_id: str, messages: list[dict[str, Any]]) -> int:
    response = bedrock_runtime.count_tokens(
        modelId=model_id,
        input={"converse": {"messages": messages}},
    )
    return int(response["inputTokens"])


def _extract_answer(response: dict[str, Any]) -> str:
    content = response.get("output", {}).get("message", {}).get("content", [])
    text_blocks = [block.get("text", "") for block in content if "text" in block]
    return "\n".join(text_blocks).strip()


def _save_usage(record: dict[str, Any]) -> None:
    table_name = os.environ.get("TOKEN_USAGE_TABLE", "").strip()
    if not table_name:
        return

    table = dynamodb.Table(table_name)
    item = {key: _to_decimal(value) for key, value in record.items()}
    table.put_item(Item=item)


def _log_usage(
    request_id: str,
    user_id: str,
    model_id: str,
    usage: dict[str, int],
    *,
    blocked: bool,
) -> None:
    print(
        json.dumps(
            {
                "event": "bedrock_token_usage",
                "request_id": request_id,
                "user_id": user_id,
                "model_id": model_id,
                "blocked": blocked,
                "usage": usage,
            },
            ensure_ascii=False,
        )
    )


def _response(status_code: int, body: dict[str, Any]) -> dict[str, Any]:
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, ensure_ascii=False),
    }


def _to_decimal(value: Any) -> Any:
    if isinstance(value, float):
        return Decimal(str(value))
    if isinstance(value, dict):
        return {key: _to_decimal(inner_value) for key, inner_value in value.items()}
    if isinstance(value, list):
        return [_to_decimal(item) for item in value]
    return value


