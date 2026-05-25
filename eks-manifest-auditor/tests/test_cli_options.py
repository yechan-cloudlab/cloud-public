from typer.testing import CliRunner

from eks_manifest_auditor.main import app

runner = CliRunner()


def test_fail_on_high_exits_non_zero_for_high_findings() -> None:
    result = runner.invoke(app, ["scan", "examples/bad-deployment.yaml", "--fail-on", "HIGH"])

    assert result.exit_code == 1
    assert "Failed:" in result.output


def test_fail_on_high_allows_good_deployment() -> None:
    result = runner.invoke(app, ["scan", "examples/good-deployment.yaml", "--fail-on", "HIGH"])

    assert result.exit_code == 0
