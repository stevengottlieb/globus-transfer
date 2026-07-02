"""Tests for the gtransfer command line."""

from typer.testing import CliRunner

from globus_transfer.cli import app

runner = CliRunner()


def test_doctor_succeeds() -> None:
    result = runner.invoke(app, ["doctor"])

    assert result.exit_code == 0
    assert "gtransfer is installed and ready" in result.output


def test_placeholder_command_succeeds() -> None:
    result = runner.invoke(app, ["login"])

    assert result.exit_code == 0
    assert "login is not implemented yet" in result.output


def test_help_lists_placeholder_commands() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    for command in [
        "login",
        "logout",
        "endpoint",
        "copy",
        "sync",
        "status",
        "history",
        "resume",
        "doctor",
    ]:
        assert command in result.output
