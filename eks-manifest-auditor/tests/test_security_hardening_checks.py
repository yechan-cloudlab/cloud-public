from pathlib import Path

from eks_manifest_auditor.scanner import Scanner


def test_bad_deployment_security_hardening_findings() -> None:
    findings, errors = Scanner().scan(Path("examples/bad-deployment.yaml"))
    check_ids = {finding.check_id for finding in findings}

    assert errors == []
    assert "SECURITY_READ_ONLY_ROOT_FILESYSTEM_NOT_SET" in check_ids
    assert "SECURITY_DANGEROUS_CAPABILITY" in check_ids
    assert "SECURITY_CAPABILITIES_DROP_ALL_NOT_SET" in check_ids
    assert "SECURITY_SECCOMP_PROFILE_NOT_SET" in check_ids
    assert "SECURITY_RUN_AS_ROOT_USER" in check_ids


def test_good_deployment_security_hardening_passes() -> None:
    findings, errors = Scanner().scan(Path("examples/good-deployment.yaml"))
    check_ids = {finding.check_id for finding in findings}

    assert errors == []
    assert "SECURITY_READ_ONLY_ROOT_FILESYSTEM_NOT_SET" not in check_ids
    assert "SECURITY_DANGEROUS_CAPABILITY" not in check_ids
    assert "SECURITY_CAPABILITIES_DROP_ALL_NOT_SET" not in check_ids
    assert "SECURITY_SECCOMP_PROFILE_NOT_SET" not in check_ids
    assert "SECURITY_RUN_AS_ROOT_USER" not in check_ids
