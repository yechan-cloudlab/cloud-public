from pathlib import Path

from eks_manifest_auditor.scanner import Scanner


def test_bad_deployment_has_at_least_five_findings() -> None:
    findings, errors = Scanner().scan(Path("examples/bad-deployment.yaml"))

    assert errors == []
    assert len(findings) >= 5


def test_good_deployment_has_no_high_findings() -> None:
    findings, errors = Scanner().scan(Path("examples/good-deployment.yaml"))

    assert errors == []
    assert all(finding.severity != "HIGH" for finding in findings)
