"""Generate a Markdown investigation report from aggregated DNS query results."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REQUIRED_COLUMNS = {
    "instance_id",
    "query_name",
    "query_type",
    "rcode",
    "query_count",
}


@dataclass(frozen=True)
class Finding:
    score: int
    instance_id: str
    query_name: str
    query_type: str
    rcode: str
    query_count: int
    reasons: tuple[str, ...]


def normalize_domain(value: str) -> str:
    """Normalize a DNS name for rule matching."""
    return value.strip().lower().rstrip(".")


def load_rules(path: Path) -> set[str]:
    """Load exact-match domain rules from a newline-delimited text file."""
    return {
        normalize_domain(line)
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def validate_columns(fieldnames: Iterable[str] | None) -> None:
    """Raise a clear error when the input CSV schema is incomplete."""
    columns = set(fieldnames or [])
    missing = REQUIRED_COLUMNS - columns
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Input CSV is missing required columns: {missing_list}")


def parse_query_count(value: str) -> int:
    """Parse query_count and fail loudly on malformed rows."""
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Invalid query_count value: {value!r}") from exc


def score_row(row: dict[str, str], rules: set[str]) -> Finding | None:
    """Score one aggregated DNS result row."""
    domain = normalize_domain(row["query_name"])
    query_type = row["query_type"].strip().upper()
    rcode = row["rcode"].strip().upper()
    count = parse_query_count(row["query_count"])

    score = 0
    reasons: list[str] = []

    if domain in rules:
        score += 5
        reasons.append("known suspicious domain")
    if len(domain) >= 50:
        score += 2
        reasons.append("long domain")
    if query_type == "TXT" and count >= 10:
        score += 2
        reasons.append("high TXT volume")
    if rcode == "NXDOMAIN" and count >= 20:
        score += 2
        reasons.append("high NXDOMAIN volume")

    if score == 0:
        return None

    return Finding(
        score=score,
        instance_id=row["instance_id"].strip(),
        query_name=row["query_name"].strip(),
        query_type=query_type,
        rcode=rcode,
        query_count=count,
        reasons=tuple(reasons),
    )


def build_report(rows: list[dict[str, str]], rules: set[str]) -> str:
    """Build a Markdown report sorted by descending suspicion score."""
    findings = [finding for row in rows if (finding := score_row(row, rules))]
    findings.sort(key=lambda item: (-item.score, -item.query_count, item.query_name))

    lines = [
        "# Route 53 Resolver Query Log Suspicious Domain Report",
        "",
        "| Score | Instance ID | Query Name | Type | RCODE | Count | Reasons |",
        "|---:|---|---|---|---|---:|---|",
    ]

    for finding in findings:
        lines.append(
            f"| {finding.score} | {finding.instance_id} | {finding.query_name} | "
            f"{finding.query_type} | {finding.rcode} | {finding.query_count} | "
            f"{', '.join(finding.reasons)} |"
        )

    if not findings:
        lines.extend(["", "No suspicious findings matched the current rules."])

    lines.extend(
        [
            "",
            "## Notes",
            "- DNS query logs indicate lookups, not confirmed network connections.",
            "- Findings should be validated with additional telemetry such as VPC Flow Logs, proxy logs, or endpoint telemetry.",
        ]
    )

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown investigation report from aggregated DNS query CSV results."
    )
    parser.add_argument("--input", required=True, type=Path, help="Path to Athena CSV export")
    parser.add_argument("--rules", required=True, type=Path, help="Path to exact-match domain rules")
    parser.add_argument("--output", required=True, type=Path, help="Path to write Markdown report")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    with args.input.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        validate_columns(reader.fieldnames)
        rows = list(reader)

    report = build_report(rows, load_rules(args.rules))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()
