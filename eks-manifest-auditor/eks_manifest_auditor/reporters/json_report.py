"""JSON reporter."""

import json
from pathlib import Path

from eks_manifest_auditor.models import Finding
from eks_manifest_auditor.utils import severity_counts


def findings_to_json(findings: list[Finding]) -> str:
    """Serialize findings and summary to pretty JSON."""
    counts = severity_counts(findings)
    payload = {
        "summary": {severity.value: count for severity, count in counts.items()},
        "findings": [finding.model_dump() for finding in findings],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


def write_json_report(findings: list[Finding], file_path: Path) -> None:
    """Write findings JSON to disk."""
    file_path.write_text(findings_to_json(findings), encoding="utf-8")
