"""Ingress resource checks."""

from eks_manifest_auditor.models import Finding, ManifestResource, Severity
from eks_manifest_auditor.utils import annotations


def check_ingress_annotations(resource: ManifestResource) -> list[Finding]:
    """Report Ingress annotations and missing class annotation."""
    if resource.kind != "Ingress":
        return []
    anns = annotations(resource.raw)
    annotation_names = ", ".join(sorted(anns)) if anns else "none"
    findings = [
        _finding(
            resource,
            Severity.LOW,
            "INGRESS_ANNOTATION_LIST",
            f"Ingress annotations: {annotation_names}.",
            "Review annotations for controller-specific behavior and ownership.",
        )
    ]
    has_class_annotation = "kubernetes.io/ingress.class" in anns
    has_class_name = bool(resource.raw.get("spec", {}).get("ingressClassName"))
    if not has_class_annotation and not has_class_name:
        findings.append(
            _finding(
                resource,
                Severity.MEDIUM,
                "INGRESS_CLASS_NOT_SET",
                "Ingress class is not set by annotation or spec.ingressClassName.",
                "Set spec.ingressClassName or kubernetes.io/ingress.class explicitly.",
            )
        )
    return findings


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
