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


def build_rule_map(rules_config: Dict[str, Any]) -> Dict[str, str]:
    return {rule["category"]: rule["model"] for rule in rules_config.get("rules", [])}


def route_request(category: str, rules_config: Dict[str, Any]) -> str:
    rule_map = build_rule_map(rules_config)
    return rule_map.get(category, rules_config["default_model"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Route Bedrock requests to a Claude model category.")
    parser.add_argument("--rules", required=True, help="Path to routing rules JSON file.")
    parser.add_argument("--requests", required=True, help="Path to request JSONL file.")
    args = parser.parse_args()

    rules_config = load_json(args.rules)

    for request in iter_jsonl(args.requests):
        model = route_request(request["category"], rules_config)
        print(json.dumps({"request_id": request["id"], "category": request["category"], "selected_model": model}, ensure_ascii=False))


if __name__ == "__main__":
    main()
