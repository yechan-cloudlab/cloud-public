"""Manifest scanner orchestration."""

from pathlib import Path

from eks_manifest_auditor.checks import CHECKS, Check
from eks_manifest_auditor.models import Finding, ParseError
from eks_manifest_auditor.parser import parse_manifest_file
from eks_manifest_auditor.utils import discover_yaml_files


class Scanner:
    """Run registered checks against local Kubernetes manifest files."""

    def __init__(self, checks: list[Check] | None = None) -> None:
        self.checks = checks or CHECKS

    def scan(self, target: Path) -> tuple[list[Finding], list[ParseError]]:
        """Scan a file or directory and return findings plus parse errors."""
        findings: list[Finding] = []
        parse_errors: list[ParseError] = []
        for yaml_file in discover_yaml_files(target):
            resources, errors = parse_manifest_file(yaml_file)
            parse_errors.extend(errors)
            for resource in resources:
                for check in self.checks:
                    findings.extend(check(resource))
        return findings, parse_errors
