from pathlib import Path

from eks_manifest_auditor.scanner import Scanner


def test_irsa_annotation_missing_is_reported() -> None:
    findings, _ = Scanner().scan(Path("examples/bad-deployment.yaml"))
    check_ids = {finding.check_id for finding in findings}

    assert "IRSA_ROLE_ANNOTATION_MISSING" in check_ids


def test_irsa_annotation_present_is_reported_as_low() -> None:
    findings, errors = Scanner().scan(Path("examples/good-deployment.yaml"))
    irsa_findings = [
        finding for finding in findings if finding.check_id == "IRSA_ROLE_ANNOTATION_PRESENT"
    ]

    assert errors == []
    assert len(irsa_findings) == 1
    assert irsa_findings[0].severity == "LOW"
