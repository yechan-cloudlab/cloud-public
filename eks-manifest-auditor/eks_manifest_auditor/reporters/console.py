"""Rich console reporter."""

from rich.console import Console
from rich.table import Table

from eks_manifest_auditor.models import Finding, ParseError, Severity
from eks_manifest_auditor.utils import severity_counts

SEVERITY_STYLE = {
    Severity.HIGH: "bold red",
    Severity.MEDIUM: "yellow",
    Severity.LOW: "cyan",
}


def render_console(findings: list[Finding], parse_errors: list[ParseError] | None = None) -> None:
    """Render findings as a Rich table with a severity summary."""
    console = Console()
    table = Table(title="EKS Manifest Auditor Findings", show_lines=False)
    table.add_column("Severity", style="bold")
    table.add_column("Check ID")
    table.add_column("Resource")
    table.add_column("Namespace")
    table.add_column("Message")
    table.add_column("File")

    for finding in findings:
        severity = Severity(finding.severity)
        table.add_row(
            f"[{SEVERITY_STYLE[severity]}]{severity.value}[/]",
            finding.check_id,
            f"{finding.resource_kind}/{finding.resource_name}",
            finding.namespace,
            finding.message,
            finding.file_path,
        )

    console.print(table)

    if parse_errors:
        error_table = Table(title="Parse Errors")
        error_table.add_column("File")
        error_table.add_column("Message")
        for error in parse_errors:
            error_table.add_row(error.file_path, error.message)
        console.print(error_table)

    counts = severity_counts(findings)
    console.print("\n[bold]Summary[/]")
    for severity in (Severity.HIGH, Severity.MEDIUM, Severity.LOW):
        console.print(f"[{SEVERITY_STYLE[severity]}]{severity.value} {counts[severity]}[/]")
