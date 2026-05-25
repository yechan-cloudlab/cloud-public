import json
from pathlib import Path

from eks_manifest_auditor.reporters.json_report import write_json_report
from eks_manifest_auditor.reporters.markdown import write_markdown_report
from eks_manifest_auditor.scanner import Scanner


def test_json_report_generation(tmp_path: Path) -> None:
    findings, _ = Scanner().scan(Path("examples/bad-deployment.yaml"))
    report_file = tmp_path / "report.json"

    write_json_report(findings, report_file)
    payload = json.loads(report_file.read_text(encoding="utf-8"))

    assert "summary" in payload
    assert len(payload["findings"]) >= 5


def test_markdown_report_generation(tmp_path: Path) -> None:
    findings, _ = Scanner().scan(Path("examples/bad-deployment.yaml"))
    report_file = tmp_path / "report.md"

    write_markdown_report(findings, report_file)
    content = report_file.read_text(encoding="utf-8")

    assert "## Summary" in content
    assert "## Findings Table" in content
    assert "## Severity Summary" in content
    assert "## Recommendations" in content
