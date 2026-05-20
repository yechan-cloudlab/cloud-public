"""Run the LLM cost router.

This sample intentionally keeps provider calls small and explicit:
- dry-run mode shows the routing decision without calling any model
- Ollama calls use the local Ollama HTTP API
- Bedrock calls use boto3 and require AWS credentials
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from classify_request import classify_request

ROOT_DIR = Path(__file__).resolve().parents[1]


def load_rules(path: str | Path | None = None) -> dict[str, Any]:
    rules_path = Path(path) if path else ROOT_DIR / "router" / "routing_rules.json"
    with rules_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def route_request(prompt: str, rules: dict[str, Any]) -> dict[str, Any]:
    decision = classify_request(prompt, rules)
    return {
        "provider": decision.provider,
        "model": decision.model,
        "rule": decision.rule,
        "reason": decision.reason,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="LLM cost router sample")
    parser.add_argument("prompt", help="User prompt to route")
    parser.add_argument("--rules", help="Path to routing rules JSON")
    parser.add_argument("--dry-run", action="store_true", help="Only print routing decision")
    args = parser.parse_args()

    rules = load_rules(args.rules)
    decision = route_request(args.prompt, rules)

    if args.dry_run:
        print(json.dumps({"prompt": args.prompt, "decision": decision}, ensure_ascii=False, indent=2))
        return

    if decision["provider"] == "ollama":
        from ollama.ollama_client import generate_with_ollama

        response = generate_with_ollama(args.prompt, model=decision["model"])
    elif decision["provider"] == "bedrock_claude":
        from bedrock.claude_client import generate_with_claude

        response = generate_with_claude(args.prompt, model_id=decision["model"])
    else:
        raise ValueError(f"Unsupported provider: {decision['provider']}")

    print(json.dumps({"decision": decision, "response": response}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
