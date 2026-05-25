"""Utility helpers for Kubernetes manifest inspection."""

from collections import Counter
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from eks_manifest_auditor.models import Finding, Severity

WORKLOAD_KINDS = {"Deployment", "StatefulSet", "DaemonSet"}


def discover_yaml_files(root: Path) -> list[Path]:
    """Return YAML files under a file or directory path."""
    if root.is_file() and root.suffix.lower() in {".yaml", ".yml"}:
        return [root]
    if not root.exists():
        raise FileNotFoundError(f"Path does not exist: {root}")
    if not root.is_dir():
        raise ValueError(f"Path is not a YAML file or directory: {root}")
    return sorted(path for path in root.rglob("*") if _is_yaml_file(path))


def _is_yaml_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in {".yaml", ".yml"}


def get_nested(data: dict[str, Any], path: Iterable[str], default: Any = None) -> Any:
    """Read a nested dictionary value without raising KeyError."""
    current: Any = data
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def pod_spec_for(resource: dict[str, Any]) -> dict[str, Any]:
    """Return the pod spec section for workload or pod-like resources."""
    kind = resource.get("kind")
    if kind in WORKLOAD_KINDS:
        spec = get_nested(resource, ("spec", "template", "spec"), {})
    else:
        spec = resource.get("spec", {})
    return spec if isinstance(spec, dict) else {}


def containers_for(resource: dict[str, Any]) -> list[dict[str, Any]]:
    """Return normal and init containers for a manifest."""
    pod_spec = pod_spec_for(resource)
    containers: list[dict[str, Any]] = []
    for key in ("initContainers", "containers"):
        items = pod_spec.get(key, [])
        if isinstance(items, list):
            containers.extend(item for item in items if isinstance(item, dict))
    return containers


def metadata(resource: dict[str, Any]) -> dict[str, Any]:
    """Return Kubernetes metadata dictionary."""
    value = resource.get("metadata", {})
    return value if isinstance(value, dict) else {}


def annotations(resource: dict[str, Any]) -> dict[str, str]:
    """Return metadata annotations as strings."""
    value = metadata(resource).get("annotations", {})
    if not isinstance(value, dict):
        return {}
    return {str(key): str(val) for key, val in value.items()}


def severity_counts(findings: list[Finding]) -> dict[Severity, int]:
    """Count findings by severity with stable severity keys."""
    counts = Counter(Severity(item.severity) for item in findings)
    return {severity: counts.get(severity, 0) for severity in Severity}
