# Project: Simulated Patient Monitoring System (SPMS)
# Project Author: Michael Mart | Prepared by Codex
# File: tools/check_coverage.py
# Purpose: Gate actual Python statement coverage at 90% and report branches apart.
# Responsibilities: Validate coverage.py JSON and reject absent/invalid evidence.
# Requirements: QA-005, QA-006, QA-007; master prompt statement-coverage policy.
# Controls: No product risk control implemented by this verification utility.
"""Use exact line counts; combined line/branch percentages are not the gate."""

import json
import sys
from pathlib import Path
from typing import cast


def count(totals: dict[str, object], key: str) -> int:
    """Require nonnegative integer evidence, excluding booleans."""
    value = totals[key]
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("Invalid count")
    return value


def main() -> int:
    """Return 0 for sufficient statements, 1 for shortfall, 2 for invalid evidence."""
    try:
        if len(sys.argv) != 2:
            raise ValueError("Expected one JSON report")
        raw: object = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        if not isinstance(raw, dict) or not isinstance(raw.get("totals"), dict):
            raise ValueError("Missing totals")
        totals = cast(dict[str, object], raw["totals"])
        covered = count(totals, "covered_lines")
        statements = count(totals, "num_statements")
        covered_branches = count(totals, "covered_branches")
        branches = count(totals, "num_branches")
        if statements == 0 or covered > statements or covered_branches > branches:
            raise ValueError("Inconsistent totals")
    except OSError, ValueError, KeyError, TypeError:
        print("Invalid coverage report", file=sys.stderr)
        return 2

    print(
        json.dumps(
            {
                "covered_statements": covered,
                "statements": statements,
                "statement_percent": covered / statements * 100,
                "covered_branches": covered_branches,
                "branches": branches,
                "branch_percent": covered_branches / branches * 100
                if branches
                else None,
                "minimum_statement_percent": 90,
            }
        )
    )
    return 0 if covered * 100 >= 90 * statements else 1


if __name__ == "__main__":
    raise SystemExit(main())
