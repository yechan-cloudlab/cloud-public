"""Markdown reporter."""

from pathlib import Path

from eks_manifest_auditor.models import Finding, Severity
from eks_manifest_auditor.utils import severity_counts


def findings_to_markdown(findings: list[Finding]) -> str:
    """Render findings as a Markdown report."""
    counts = severity_counts(findings)
    lines = [
        "# EKS Manifest Auditor Report",
        "",
        "## Summary",
        "",
        f"- Total findings: {len(findings)}",
        f"- HIGH: {counts[Severity.HIGH]}",
        f"- MEDIUM: {counts[Severity.MEDIUM]}",
        f"- LOW: {counts[Severity.LOW]}",
        "",
        "## Findings Table",
        "",
        "| Severity | Check ID | Resource | Namespace | Message | File |",
        "|---|---|---|---|---|---|",
    ]
    if findings:
        for finding in findings:
            lines.append(
                "| "
                f"{finding.severity} | "
                f"{_escape(finding.check_id)} | "
                f"{_escape(finding.resource_kind + '/' + finding.resource_name)} | "
                f"{_escape(finding.namespace)} | "
                f"{_escape(finding.message)} | "
                f"{_escape(finding.file_path)} |"
            )
    else:
        lines.append("| - | - | - | - | No findings. | - |")

    lines.extend(
        [
            "",
            "## Severity Summary",
            "",
            "| Severity | Count |",
            "|---|---:|",
            f"| HIGH | {counts[Severity.HIGH]} |",
            f"| MEDIUM | {counts[Severity.MEDIUM]} |",
            f"| LOW | {counts[Severity.LOW]} |",
            "",
            "## Recommendations",
            "",
        ]
    )
    if findings:
        for index, finding in enumerate(findings, start=1):
            lines.append(
                f"{index}. **{finding.check_id}** "
                f"({finding.resource_kind}/{finding.resource_name}): {finding.recommendation}"
            )
    else:
        lines.append("- No remediation is required for the scanned manifests.")
    lines.append("")
    return "\n".join(lines)


def write_markdown_report(findings: list[Finding], file_path: Path) -> None:
    """Write Markdown report to disk."""
    file_path.write_text(findings_to_markdown(findings), encoding="utf-8")


def _escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")
