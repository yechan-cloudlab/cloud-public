"""YAML parser for local Kubernetes manifest files."""

from pathlib import Path
from typing import Any

import yaml

from eks_manifest_auditor.models import ManifestResource, ParseError


def parse_manifest_file(file_path: Path) -> tuple[list[ManifestResource], list[ParseError]]:
    """Parse all Kubernetes resources from a YAML file.

    Invalid YAML is returned as a non-fatal ParseError so scans can continue.
    """
    try:
        content = file_path.read_text(encoding="utf-8")
        documents = list(yaml.safe_load_all(content))
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
        return [], [ParseError(file_path=str(file_path), message=str(exc))]

    resources: list[ManifestResource] = []
    for index, document in enumerate(documents):
        if not isinstance(document, dict) or not document:
            continue
        resource = _resource_from_document(document, file_path, index)
        if resource is not None:
            resources.append(resource)
    return resources, []


def _resource_from_document(
    document: dict[str, Any],
    file_path: Path,
    document_index: int,
) -> ManifestResource | None:
    """Convert a YAML document into a ManifestResource when it looks like Kubernetes."""
    kind = document.get("kind")
    metadata = document.get("metadata", {})
    if not isinstance(kind, str) or not isinstance(metadata, dict):
        return None
    name = metadata.get("name", "<unknown>")
    namespace = metadata.get("namespace") or "default"
    return ManifestResource(
        kind=kind,
        name=str(name),
        namespace=str(namespace),
        file_path=file_path,
        document_index=document_index,
        raw=document,
    )
