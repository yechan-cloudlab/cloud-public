"""Security-oriented manifest checks."""

from typing import Any

from eks_manifest_auditor.models import Finding, ManifestResource, Severity
from eks_manifest_auditor.utils import containers_for, pod_spec_for

DANGEROUS_CAPABILITIES = {
    "SYS_ADMIN",
    "NET_ADMIN",
    "SYS_MODULE",
    "SYS_PTRACE",
    "DAC_READ_SEARCH",
    "DAC_OVERRIDE",
}

CLUSTER_SCOPED_KINDS = {
    "ClusterRole",
    "ClusterRoleBinding",
    "CustomResourceDefinition",
    "IngressClass",
    "MutatingWebhookConfiguration",
    "Namespace",
    "Node",
    "PersistentVolume",
    "StorageClass",
    "ValidatingWebhookConfiguration",
}


def check_privileged_containers(resource: ManifestResource) -> list[Finding]:
    """Detect privileged containers."""
    findings: list[Finding] = []
    for container in containers_for(resource.raw):
        security_context = _security_context(container)
        if security_context.get("privileged") is True:
            findings.append(
                _finding(
                    resource,
                    Severity.HIGH,
                    "SECURITY_PRIVILEGED_CONTAINER",
                    f"Container '{_container_name(container)}' sets privileged: true.",
                    "Avoid privileged containers unless there is a reviewed platform exception.",
                )
            )
    return findings


def check_host_path_volumes(resource: ManifestResource) -> list[Finding]:
    """Detect hostPath volumes."""
    pod_spec = pod_spec_for(resource.raw)
    volumes = pod_spec.get("volumes", [])
    if not isinstance(volumes, list):
        return []
    findings: list[Finding] = []
    for volume in volumes:
        if isinstance(volume, dict) and "hostPath" in volume:
            findings.append(
                _finding(
                    resource,
                    Severity.HIGH,
                    "SECURITY_HOST_PATH_VOLUME",
                    f"Volume '{volume.get('name', '<unnamed>')}' uses hostPath.",
                    "Replace hostPath with safer storage primitives such as PVCs when possible.",
                )
            )
    return findings


def check_default_namespace(resource: ManifestResource) -> list[Finding]:
    """Detect resources deployed to the default namespace."""
    if resource.kind in CLUSTER_SCOPED_KINDS:
        return []
    if resource.namespace != "default":
        return []
    return [
        _finding(
            resource,
            Severity.MEDIUM,
            "SECURITY_DEFAULT_NAMESPACE",
            "Resource is deployed to the default namespace.",
            "Use an application-specific namespace with clear ownership and policies.",
        )
    ]


def check_allow_privilege_escalation(resource: ManifestResource) -> list[Finding]:
    """Detect containers that explicitly allow privilege escalation."""
    findings: list[Finding] = []
    for container in containers_for(resource.raw):
        security_context = _security_context(container)
        if security_context.get("allowPrivilegeEscalation") is True:
            findings.append(
                _finding(
                    resource,
                    Severity.HIGH,
                    "SECURITY_ALLOW_PRIVILEGE_ESCALATION",
                    f"Container '{_container_name(container)}' allows privilege escalation.",
                    "Set allowPrivilegeEscalation: false for application containers.",
                )
            )
    return findings


def check_run_as_non_root(resource: ManifestResource) -> list[Finding]:
    """Detect pod specs without runAsNonRoot enabled at pod or container level."""
    containers = containers_for(resource.raw)
    if not containers:
        return []
    pod_security_context = pod_spec_for(resource.raw).get("securityContext", {})
    pod_non_root = (
        isinstance(pod_security_context, dict)
        and pod_security_context.get("runAsNonRoot") is True
    )
    findings: list[Finding] = []
    for container in containers:
        container_non_root = _security_context(container).get("runAsNonRoot") is True
        if not pod_non_root and not container_non_root:
            findings.append(
                _finding(
                    resource,
                    Severity.MEDIUM,
                    "SECURITY_RUN_AS_NON_ROOT_NOT_SET",
                    f"Container '{_container_name(container)}' does not set runAsNonRoot.",
                    "Set runAsNonRoot: true at the pod or container securityContext level.",
                )
            )
    return findings


def check_read_only_root_filesystem(resource: ManifestResource) -> list[Finding]:
    """Detect containers without readOnlyRootFilesystem enabled."""
    findings: list[Finding] = []
    for container in containers_for(resource.raw):
        security_context = _security_context(container)
        if security_context.get("readOnlyRootFilesystem") is not True:
            findings.append(
                _finding(
                    resource,
                    Severity.MEDIUM,
                    "SECURITY_READ_ONLY_ROOT_FILESYSTEM_NOT_SET",
                    (
                        f"Container '{_container_name(container)}' does not set "
                        "readOnlyRootFilesystem."
                    ),
                    (
                        "Set readOnlyRootFilesystem: true when the application does not need "
                        "writes to the root filesystem."
                    ),
                )
            )
    return findings


def check_dangerous_capabilities(resource: ManifestResource) -> list[Finding]:
    """Detect Linux capabilities that are usually too broad for application pods."""
    findings: list[Finding] = []
    for container in containers_for(resource.raw):
        added = set(_capability_values(container, "add"))
        dangerous = sorted(added & DANGEROUS_CAPABILITIES)
        for capability in dangerous:
            findings.append(
                _finding(
                    resource,
                    Severity.HIGH,
                    "SECURITY_DANGEROUS_CAPABILITY",
                    f"Container '{_container_name(container)}' adds Linux capability {capability}.",
                    (
                        "Remove broad Linux capabilities unless there is a reviewed platform "
                        "exception."
                    ),
                )
            )
    return findings


def check_capabilities_drop_all(resource: ManifestResource) -> list[Finding]:
    """Recommend dropping all Linux capabilities by default."""
    findings: list[Finding] = []
    for container in containers_for(resource.raw):
        dropped = {capability.upper() for capability in _capability_values(container, "drop")}
        if "ALL" not in dropped:
            findings.append(
                _finding(
                    resource,
                    Severity.LOW,
                    "SECURITY_CAPABILITIES_DROP_ALL_NOT_SET",
                    (
                        f"Container '{_container_name(container)}' does not drop all Linux "
                        "capabilities."
                    ),
                    (
                        "Set securityContext.capabilities.drop: ['ALL'] and add back only "
                        "required capabilities."
                    ),
                )
            )
    return findings


def check_seccomp_profile(resource: ManifestResource) -> list[Finding]:
    """Detect pod specs without seccompProfile at pod or container level."""
    containers = containers_for(resource.raw)
    if not containers:
        return []
    pod_security_context = pod_spec_for(resource.raw).get("securityContext", {})
    pod_seccomp = (
        isinstance(pod_security_context, dict)
        and isinstance(pod_security_context.get("seccompProfile"), dict)
    )
    findings: list[Finding] = []
    for container in containers:
        container_seccomp = isinstance(
            _security_context(container).get("seccompProfile"),
            dict,
        )
        if not pod_seccomp and not container_seccomp:
            findings.append(
                _finding(
                    resource,
                    Severity.MEDIUM,
                    "SECURITY_SECCOMP_PROFILE_NOT_SET",
                    f"Container '{_container_name(container)}' does not set seccompProfile.",
                    (
                        "Set seccompProfile, for example RuntimeDefault, at the pod or "
                        "container level."
                    ),
                )
            )
    return findings


def check_run_as_root_user(resource: ManifestResource) -> list[Finding]:
    """Detect containers that explicitly run as UID 0."""
    containers = containers_for(resource.raw)
    if not containers:
        return []
    pod_security_context = pod_spec_for(resource.raw).get("securityContext", {})
    pod_run_as_root = (
        isinstance(pod_security_context, dict)
        and pod_security_context.get("runAsUser") == 0
    )
    findings: list[Finding] = []
    for container in containers:
        security_context = _security_context(container)
        container_run_as_root = security_context.get("runAsUser") == 0
        if pod_run_as_root or container_run_as_root:
            findings.append(
                _finding(
                    resource,
                    Severity.HIGH,
                    "SECURITY_RUN_AS_ROOT_USER",
                    f"Container '{_container_name(container)}' explicitly runs as UID 0.",
                    "Run application containers as a non-root UID and set runAsNonRoot: true.",
                )
            )
    return findings


def _security_context(container: dict[str, Any]) -> dict[str, Any]:
    value = container.get("securityContext", {})
    return value if isinstance(value, dict) else {}


def _capability_values(container: dict[str, Any], key: str) -> list[str]:
    capabilities = _security_context(container).get("capabilities", {})
    if not isinstance(capabilities, dict):
        return []
    values = capabilities.get(key, [])
    if not isinstance(values, list):
        return []
    return [str(value).upper() for value in values]


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
