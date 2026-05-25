from pathlib import Path

from eks_manifest_auditor.scanner import Scanner


def test_service_exposure_findings() -> None:
    findings, _ = Scanner().scan(Path("examples/bad-deployment.yaml"))
    check_ids = {finding.check_id for finding in findings}

    assert "SERVICE_LOAD_BALANCER" in check_ids
    assert "SERVICE_NODE_PORT" in check_ids
