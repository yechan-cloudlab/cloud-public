from pathlib import Path

from eks_manifest_auditor.scanner import Scanner


def test_bad_deployment_security_findings() -> None:
    findings, _ = Scanner().scan(Path("examples/bad-deployment.yaml"))
    check_ids = {finding.check_id for finding in findings}

    assert "SECURITY_PRIVILEGED_CONTAINER" in check_ids
    assert "SECURITY_HOST_PATH_VOLUME" in check_ids
    assert "SECURITY_ALLOW_PRIVILEGE_ESCALATION" in check_ids
    assert "SECURITY_DEFAULT_NAMESPACE" in check_ids
