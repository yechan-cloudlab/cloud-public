"""Command-line interface for eks-manifest-auditor."""

from enum import StrEnum
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from eks_manifest_auditor.models import Finding, Severity
from eks_manifest_auditor.reporters.console import render_console
from eks_manifest_auditor.reporters.json_report import write_json_report
from eks_manifest_auditor.reporters.markdown import write_markdown_report
from eks_manifest_auditor.scanner import Scanner


class OutputFormat(StrEnum):
    """Supported report output formats."""

    console = "console"
    json = "json"
    markdown = "markdown"


app = typer.Typer(
    help="Local Kubernetes/EKS manifest static analysis CLI. No AWS or cluster connection is used."
)


@app.callback()
def main() -> None:
    """Run local manifest audit commands."""


@app.command()
def scan(
    path: Annotated[
        Path,
        typer.Argument(help="YAML file or directory containing Kubernetes manifests."),
    ],
    output: Annotated[OutputFormat, typer.Option("--output", "-o")] = OutputFormat.console,
    file: Annotated[
        Path | None,
        typer.Option("--file", "-f", help="Report output file for JSON/Markdown."),
    ] = None,
    fail_on: Annotated[
        Severity | None,
        typer.Option("--fail-on", help="Exit with code 1 when this severity or higher is found."),
    ] = None,
) -> None:
    """Scan local YAML manifests for operational and security findings."""
    console = Console()
    try:
        findings, parse_errors = Scanner().scan(path)
    except (FileNotFoundError, ValueError) as exc:
        console.print(f"[bold red]Error:[/] {exc}")
        raise typer.Exit(code=2) from exc

    if output == OutputFormat.console:
        render_console(findings, parse_errors)
        _exit_for_fail_on(findings, fail_on, console)

    if file is None:
        console.print("[bold red]Error:[/] --file is required when --output is json or markdown.")
        raise typer.Exit(code=2)

    if output == OutputFormat.json:
        write_json_report(findings, file)
    elif output == OutputFormat.markdown:
        write_markdown_report(findings, file)

    console.print(f"[green]Report written:[/] {file}")
    if parse_errors:
        console.print(f"[yellow]Warning:[/] {len(parse_errors)} YAML file(s) had parse errors.")
    _exit_for_fail_on(findings, fail_on, console)


def _exit_for_fail_on(
    findings: list[Finding],
    fail_on: Severity | None,
    console: Console,
) -> None:
    if fail_on is None:
        raise typer.Exit(code=0)
    threshold = _severity_rank(fail_on)
    matching = [
        finding
        for finding in findings
        if _severity_rank(Severity(finding.severity)) >= threshold
    ]
    if matching:
        console.print(
            f"[bold red]Failed:[/] {len(matching)} finding(s) at {fail_on.value} or higher."
        )
        raise typer.Exit(code=1)
    raise typer.Exit(code=0)


def _severity_rank(severity: Severity) -> int:
    return {
        Severity.LOW: 1,
        Severity.MEDIUM: 2,
        Severity.HIGH: 3,
    }[severity]


if __name__ == "__main__":
    app()
