from pathlib import Path

from eks_manifest_auditor.parser import parse_manifest_file


def test_parser_handles_multi_document_yaml() -> None:
    resources, errors = parse_manifest_file(Path("examples/bad-deployment.yaml"))

    assert errors == []
    assert [resource.kind for resource in resources] == ["Deployment", "Service", "ServiceAccount"]


def test_parser_gracefully_handles_invalid_yaml(tmp_path: Path) -> None:
    bad_file = tmp_path / "broken.yaml"
    bad_file.write_text("apiVersion: v1\nkind: Pod\nmetadata: [", encoding="utf-8")

    resources, errors = parse_manifest_file(bad_file)

    assert resources == []
    assert len(errors) == 1
