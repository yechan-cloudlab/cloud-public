"""ServiceAccount and IRSA checks."""

from eks_manifest_auditor.models import Finding, ManifestResource, Severity
from eks_manifest_auditor.utils import annotations

IRSA_ANNOTATION = "eks.amazonaws.com/role-arn"


def check_irsa_annotation(resource: ManifestResource) -> list[Finding]:
    """Check whether ServiceAccount has the EKS IRSA annotation."""
    if resource.kind != "ServiceAccount":
        return []
    anns = annotations(resource.raw)
    if IRSA_ANNOTATION in anns:
        return [
            _finding(
                resource,
                Severity.LOW,
                "IRSA_ROLE_ANNOTATION_PRESENT",
                "ServiceAccount has an IRSA role annotation.",
                "Review the IAM role policy scope and trust policy before production use.",
            )
        ]
    return [
        _finding(
            resource,
            Severity.MEDIUM,
            "IRSA_ROLE_ANNOTATION_MISSING",
            "ServiceAccount does not have an eks.amazonaws.com/role-arn annotation.",
            "Add IRSA annotation when AWS permissions are required.",
        )
    ]


def _finding(
    resource: ManifestResource,
    severity: Severity,
    check_id: str,
    message: str,
    recommendation: str,
) -> Finding:
    return Finding(
        severity=severity,
        check_id=check_id,
        resource_kind=resource.kind,
        resource_name=resource.name,
        namespace=resource.namespace,
        message=message,
        recommendation=recommendation,
        file_path=str(resource.file_path),
    )
