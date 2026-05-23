import argparse
import json
from typing import Any, Dict

from cost_calculator import estimate_request_for_model, iter_jsonl, load_json
from router import route_request


def compare_request(request: Dict[str, Any], pricing: Dict[str, Any], rules: Dict[str, Any], baseline: str) -> Dict[str, Any]:
    routed_model = route_request(request["category"], rules)
    baseline_cost = estimate_request_for_model(request, pricing, baseline)
    routed_cost = estimate_request_for_model(request, pricing, routed_model)
    return {
        "request_id": request["id"],
        "category": request["category"],
        "baseline_model": baseline,
        "baseline_cost": baseline_cost,
        "routed_model": routed_model,
        "routed_cost": routed_cost,
        "estimated_savings": round(baseline_cost - routed_cost, 8),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare fixed-model cost with routing strategy cost.")
    parser.add_argument("--pricing", required=True, help="Path to pricing JSON file.")
    parser.add_argument("--rules", required=True, help="Path to routing rules JSON file.")
    parser.add_argument("--requests", required=True, help="Path to request JSONL file.")
    parser.add_argument("--baseline", default="claude-opus", help="Baseline model key for comparison.")
    args = parser.parse_args()

    pricing = load_json(args.pricing)
    rules = load_json(args.rules)

    baseline_total = 0.0
    routed_total = 0.0

    for request in iter_jsonl(args.requests):
        result = compare_request(request, pricing, rules, args.baseline)
        baseline_total += result["baseline_cost"]
        routed_total += result["routed_cost"]
        print(json.dumps(result, ensure_ascii=False))

    print(json.dumps({
        "summary": {
            "baseline_model": args.baseline,
            "baseline_total": round(baseline_total, 8),
            "routed_total": round(routed_total, 8),
            "estimated_savings": round(baseline_total - routed_total, 8),
            "estimated_savings_percent": round(((baseline_total - routed_total) / baseline_total) * 100, 2) if baseline_total else 0.0,
        }
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
