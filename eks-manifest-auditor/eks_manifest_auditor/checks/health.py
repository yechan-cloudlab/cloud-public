"""Container health probe checks."""

from eks_manifest_auditor.models import Finding, ManifestResource, Severity
from eks_manifest_auditor.utils import WORKLOAD_KINDS, containers_for


def check_readiness_probe(resource: ManifestResource) -> list[Finding]:
    """Detect workload containers without readinessProbe."""
    return _missing_probe_findings(
        resource,
        probe_name="readinessProbe",
        severity=Severity.MEDIUM,
        check_id="HEALTH_READINESS_PROBE_MISSING",
        message_suffix="does not set readinessProbe.",
        recommendation="Set readinessProbe so traffic is sent only after the container is ready.",
    )


def check_liveness_probe(resource: ManifestResource) -> list[Finding]:
    """Detect workload containers without livenessProbe."""
    return _missing_probe_findings(
        resource,
        probe_name="livenessProbe",
        severity=Severity.LOW,
        check_id="HEALTH_LIVENESS_PROBE_MISSING",
        message_suffix="does not set livenessProbe.",
        recommendation="Set livenessProbe when the process can hang without exiting.",
    )


def check_startup_probe(resource: ManifestResource) -> list[Finding]:
    """Recommend startupProbe for workload containers."""
    return _missing_probe_findings(
        resource,
        probe_name="startupProbe",
        severity=Severity.LOW,
        check_id="HEALTH_STARTUP_PROBE_MISSING",
        message_suffix="does not set startupProbe.",
        recommendation=(
            "Set startupProbe for slow-starting applications to avoid premature restarts."
        ),
    )


def _missing_probe_findings(
    resource: ManifestResource,
    probe_name: str,
    severity: Severity,
    check_id: str,
    message_suffix: str,
    recommendation: str,
) -> list[Finding]:
    if resource.kind not in WORKLOAD_KINDS:
        return []
    findings: list[Finding] = []
    for container in containers_for(resource.raw):
        if probe_name not in container:
            findings.append(
                _finding(
                    resource,
                    severity,
                    check_id,
                    f"Container '{_container_name(container)}' {message_suffix}",
                    recommendation,
                )
            )
    return findings


def _container_name(container: dict) -> str:
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
