from pathlib import Path

from eks_manifest_auditor.scanner import Scanner


def test_missing_health_probes_are_reported() -> None:
    findings, errors = Scanner().scan(Path("examples/bad-deployment.yaml"))
    check_ids = {finding.check_id for finding in findings}

    assert errors == []
    assert "HEALTH_READINESS_PROBE_MISSING" in check_ids
    assert "HEALTH_LIVENESS_PROBE_MISSING" in check_ids
    assert "HEALTH_STARTUP_PROBE_MISSING" in check_ids


def test_good_deployment_sets_health_probes() -> None:
    findings, errors = Scanner().scan(Path("examples/good-deployment.yaml"))
    check_ids = {finding.check_id for finding in findings}

    assert errors == []
    assert "HEALTH_READINESS_PROBE_MISSING" not in check_ids
    assert "HEALTH_LIVENESS_PROBE_MISSING" not in check_ids
    assert "HEALTH_STARTUP_PROBE_MISSING" not in check_ids
