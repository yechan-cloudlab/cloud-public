from pathlib import Path

from eks_manifest_auditor.scanner import Scanner


def test_ingress_annotation_list_is_reported() -> None:
    findings, errors = Scanner().scan(Path("examples/ingress-example.yaml"))
    check_ids = {finding.check_id for finding in findings}

    assert errors == []
    assert "INGRESS_ANNOTATION_LIST" in check_ids
    assert "INGRESS_CLASS_NOT_SET" not in check_ids
