import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable


def load_json(path: str) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def iter_jsonl(path: str) -> Iterable[Dict[str, Any]]:
    with Path(path).open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at line {line_number}: {exc}") from exc


def estimate_cost(input_tokens: int, output_tokens: int, input_per_1m: float, output_per_1m: float) -> float:
    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("Token counts must be non-negative.")
    input_cost = (input_tokens / 1_000_000) * input_per_1m
    output_cost = (output_tokens / 1_000_000) * output_per_1m
    return round(input_cost + output_cost, 8)


def estimate_request_for_model(request: Dict[str, Any], pricing: Dict[str, Any], model_name: str) -> float:
    model_price = pricing["models"][model_name]
    return estimate_cost(
        input_tokens=int(request["input_tokens"]),
        output_tokens=int(request["output_tokens"]),
        input_per_1m=float(model_price["input_per_1m"]),
        output_per_1m=float(model_price["output_per_1m"]),
    )


def estimate_request_for_all_models(request: Dict[str, Any], pricing: Dict[str, Any]) -> Dict[str, float]:
    return {
        model_name: estimate_request_for_model(request, pricing, model_name)
        for model_name in pricing["models"]
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Estimate Bedrock Claude cost by model.")
    parser.add_argument("--pricing", required=True, help="Path to pricing JSON file.")
    parser.add_argument("--requests", required=True, help="Path to request JSONL file.")
    args = parser.parse_args()

    pricing = load_json(args.pricing)
    totals = {model: 0.0 for model in pricing["models"]}

    for request in iter_jsonl(args.requests):
        estimates = estimate_request_for_all_models(request, pricing)
        print(json.dumps({"request_id": request["id"], "category": request["category"], "estimates": estimates}, ensure_ascii=False))
        for model, cost in estimates.items():
            totals[model] += cost

    print(json.dumps({"totals": {k: round(v, 8) for k, v in totals.items()}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
