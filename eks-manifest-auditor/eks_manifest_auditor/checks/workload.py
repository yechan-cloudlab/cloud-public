"""Workload resource checks."""

from typing import Any

from eks_manifest_auditor.models import Finding, ManifestResource, Severity
from eks_manifest_auditor.utils import WORKLOAD_KINDS, containers_for


def check_resource_requests(resource: ManifestResource) -> list[Finding]:
    """Detect containers without resources.requests."""
    if resource.kind not in WORKLOAD_KINDS:
        return []
    findings: list[Finding] = []
    for container in containers_for(resource.raw):
        if not _has_resource_key(container, "requests"):
            findings.append(
                _finding(
                    resource,
                    Severity.MEDIUM,
                    "WORKLOAD_MISSING_RESOURCE_REQUESTS",
                    f"Container '{_container_name(container)}' is missing resources.requests.",
                    "Set CPU and memory requests for predictable scheduling.",
                )
            )
    return findings


def check_resource_limits(resource: ManifestResource) -> list[Finding]:
    """Detect containers without resources.limits."""
    if resource.kind not in WORKLOAD_KINDS:
        return []
    findings: list[Finding] = []
    for container in containers_for(resource.raw):
        if not _has_resource_key(container, "limits"):
            findings.append(
                _finding(
                    resource,
                    Severity.MEDIUM,
                    "WORKLOAD_MISSING_RESOURCE_LIMITS",
                    f"Container '{_container_name(container)}' is missing resources.limits.",
                    "Set CPU and memory limits or document why limits are intentionally omitted.",
                )
            )
    return findings


def check_image_latest_tag(resource: ManifestResource) -> list[Finding]:
    """Detect container images using the latest tag or no explicit tag."""
    if resource.kind not in WORKLOAD_KINDS:
        return []
    findings: list[Finding] = []
    for container in containers_for(resource.raw):
        image = str(container.get("image", ""))
        if _uses_latest_tag(image):
            findings.append(
                _finding(
                    resource,
                    Severity.HIGH,
                    "WORKLOAD_IMAGE_LATEST_TAG",
                    f"Container '{_container_name(container)}' uses a mutable image tag: {image}.",
                    "Pin images to immutable version tags or digests.",
                )
            )
    return findings


def check_replicas(resource: ManifestResource) -> list[Finding]:
    """Warn when Deployment or StatefulSet replicas are one or less."""
    if resource.kind not in {"Deployment", "StatefulSet"}:
        return []
    replicas = resource.raw.get("spec", {}).get("replicas", 1)
    if isinstance(replicas, int) and replicas <= 1:
        return [
            _finding(
                resource,
                Severity.LOW,
                "WORKLOAD_LOW_REPLICA_COUNT",
                f"{resource.kind} has replicas set to {replicas}.",
                "Use at least two replicas for production workloads when possible.",
            )
        ]
    return []


def _has_resource_key(container: dict[str, Any], key: str) -> bool:
    resources = container.get("resources", {})
    return (
        isinstance(resources, dict)
        and isinstance(resources.get(key), dict)
        and bool(resources[key])
    )


def _uses_latest_tag(image: str) -> bool:
    if not image:
        return False
    if "@" in image:
        return False
    last_segment = image.rsplit("/", maxsplit=1)[-1]
    if ":" not in last_segment:
        return True
    return last_segment.endswith(":latest")


def _container_name(container: dict[str, Any]) -> str:
    return str(container.get("name", "<unnamed>"))


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
