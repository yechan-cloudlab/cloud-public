import argparse
import json
from pathlib import Path
from typing import Any

RULE_PATH = Path(__file__).with_name("routing_rules.json")


def load_rules(path: Path = RULE_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def classify_prompt(prompt: str, rules: dict[str, Any] | None = None) -> dict[str, Any]:
    rules = rules or load_rules()
    normalized = prompt.lower()
    prompt_len = len(prompt)

    for rule in rules["rules"]:
        min_chars = rule.get("min_chars", 0)
        max_chars = rule.get("max_chars")

        if prompt_len < min_chars:
            continue
        if max_chars is not None and prompt_len > max_chars:
            continue

        keywords = [keyword.lower() for keyword in rule.get("keywords", [])]
        has_keywords = bool(keywords)
        keyword_match = any(keyword in normalized for keyword in keywords)

        if keyword_match or (not has_keywords and (min_chars or max_chars)):
            return {
                "route_to": rule["route_to"],
                "matched_rule": rule["name"],
                "reason": rule["reason"],
                "prompt_chars": prompt_len,
            }

    fallback = rules["fallback"]
    return {
        "route_to": fallback["route_to"],
        "matched_rule": "fallback",
        "reason": fallback["reason"],
        "prompt_chars": prompt_len,
    }


def classify_json_file(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    results = []
    for item in payload["requests"]:
        result = classify_prompt(item["prompt"])
        results.append({"id": item["id"], **result})
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify an LLM request without calling any model.")
    parser.add_argument("input", help="Prompt text or a JSON file with requests")
    args = parser.parse_args()

    path = Path(args.input)
    if path.exists():
        result = classify_json_file(path)
    else:
        result = classify_prompt(args.input)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
