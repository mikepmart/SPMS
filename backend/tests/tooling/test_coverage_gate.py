# Project: Simulated Patient Monitoring System (SPMS)
# Project Author: Michael Mart | Prepared by Codex
# File: tests/tooling/test_coverage_gate.py
# Purpose: Specify the statement-coverage gate independently of branch coverage.
# Responsibilities: Exact boundary, non-rounded failure and invalid-report rejection.
# Requirements: QA-001, QA-005, QA-006, QA-007.
import json
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.unit
@pytest.mark.parametrize(
    ("covered", "statements", "covered_branches", "branches", "expected"),
    [
        (90, 100, 0, 10, 0),
        (89, 100, 10, 10, 1),
        (899, 1000, 10, 10, 1),
        (9, 10, 0, 0, 0),
        (100, 100, 10, 10, 0),
    ],
)
def test_statement_gate_is_independent_of_branches(
    tmp_path: Path,
    covered: int,
    statements: int,
    covered_branches: int,
    branches: int,
    expected: int,
) -> None:
    """Branch coverage cannot conceal a statement failure or add an unapproved gate."""
    report = tmp_path / "coverage.json"
    report.write_text(
        json.dumps(
            {
                "totals": {
                    "covered_lines": covered,
                    "num_statements": statements,
                    "covered_branches": covered_branches,
                    "num_branches": branches,
                }
            }
        ),
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, "tools/check_coverage.py", str(report)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == expected, result.stderr
    summary = json.loads(result.stdout)
    assert summary["statement_percent"] == covered / statements * 100
    assert summary["branch_percent"] == (
        covered_branches / branches * 100 if branches else None
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "content",
    [
        "not-json",
        "{}",
        '{"totals":{"covered_lines":0,"num_statements":0}}',
        '{"totals":{"covered_lines":101,"num_statements":100,"covered_branches":0,"num_branches":0}}',
    ],
)
def test_invalid_report_cannot_pass_the_gate(tmp_path: Path, content: str) -> None:
    """Missing, empty and inconsistent evidence is a failed check, never 100%."""
    report = tmp_path / "coverage.json"
    report.write_text(content, encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "tools/check_coverage.py", str(report)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
    assert "Invalid coverage report" in result.stderr
