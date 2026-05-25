"""Shared domain models for manifest scanning."""

from enum import StrEnum
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field


class Severity(StrEnum):
    """Finding severity levels."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Finding(BaseModel):
    """A single manifest audit result."""

    model_config = ConfigDict(use_enum_values=True)

    severity: Severity
    check_id: str
    resource_kind: str
    resource_name: str
    namespace: str
    message: str
    recommendation: str
    file_path: str


class ManifestResource(BaseModel):
    """Parsed Kubernetes manifest plus source metadata."""

    kind: str
    name: str
    namespace: str = "default"
    file_path: Path
    document_index: int = Field(default=0, ge=0)
    raw: dict


class ParseError(BaseModel):
    """Non-fatal YAML parse error."""

    file_path: str
    message: str
