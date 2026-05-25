"""Service resource checks."""

from eks_manifest_auditor.models import Finding, ManifestResource, Severity


def check_load_balancer_service(resource: ManifestResource) -> list[Finding]:
    """Detect Service type LoadBalancer."""
    if resource.kind != "Service":
        return []
    service_type = resource.raw.get("spec", {}).get("type", "ClusterIP")
    if service_type == "LoadBalancer":
        return [
            _finding(
                resource,
                Severity.MEDIUM,
                "SERVICE_LOAD_BALANCER",
                "Service exposes a cloud LoadBalancer.",
                "Confirm external exposure is required and has ownership controls.",
            )
        ]
    return []


def check_node_port_service(resource: ManifestResource) -> list[Finding]:
    """Detect NodePort Services or explicit nodePort fields."""
    if resource.kind != "Service":
        return []
    spec = resource.raw.get("spec", {})
    service_type = spec.get("type", "ClusterIP")
    ports = spec.get("ports", [])
    has_node_port = isinstance(ports, list) and any(
        isinstance(port, dict) and "nodePort" in port for port in ports
    )
    if service_type == "NodePort" or has_node_port:
        return [
            _finding(
                resource,
                Severity.MEDIUM,
                "SERVICE_NODE_PORT",
                "Service uses NodePort exposure.",
                "Prefer ClusterIP plus Ingress or a controlled LoadBalancer.",
            )
        ]
    return []


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
