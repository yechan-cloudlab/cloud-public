from pathlib import Path

from eks_manifest_auditor.checks.security import check_default_namespace
from eks_manifest_auditor.models import ManifestResource
from eks_manifest_auditor.scanner import Scanner


def test_bad_deployment_security_findings() -> None:
    findings, _ = Scanner().scan(Path("examples/bad-deployment.yaml"))
    check_ids = {finding.check_id for finding in findings}

    assert "SECURITY_PRIVILEGED_CONTAINER" in check_ids
    assert "SECURITY_HOST_PATH_VOLUME" in check_ids
    assert "SECURITY_ALLOW_PRIVILEGE_ESCALATION" in check_ids
    assert "SECURITY_DEFAULT_NAMESPACE" in check_ids
    assert "SECURITY_RUN_AS_NON_ROOT_NOT_SET" in check_ids


def test_cluster_scoped_resources_do_not_trigger_default_namespace() -> None:
    for kind in ("IngressClass", "ValidatingWebhookConfiguration", "MutatingWebhookConfiguration"):
        resource = ManifestResource(
            kind=kind,
            name="cluster-resource",
            namespace="default",
            file_path=Path("cluster.yaml"),
            raw={"apiVersion": "v1", "kind": kind, "metadata": {"name": "cluster-resource"}},
        )

        assert check_default_namespace(resource) == []
