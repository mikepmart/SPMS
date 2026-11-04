# Phase 1: Repository and development environment

Project Author: Michael Mart

Prepared by Codex for owner review. Educational synthetic-data-only simulation. Status: PLANNED / NOT STARTED — explicit owner approval required.

## Task

Establish backend and React/TypeScript structures, locked dependencies, pytest/pytest-cov, Ruff, mypy, frontend lint/type checks, Vitest, Playwright, GitHub Actions, .gitignore, README and PR template. Select supported exact tool versions during this phase; no domain features.

## Requirements

AR-001, AR-002, AR-003, AR-004, AR-005, AR-006; QA-001 through QA-008; DOC-001, DOC-002; SEC-007, SEC-008, SEC-013; PRIV-001, PRIV-002, PRIV-004; CL-007, CL-012

## Risk controls

RC-CYB-006, RC-CYB-007, RC-CYB-009 (tooling/defaults; effectiveness remains unverified). All source controls remain proposed and unverified until actual evidence and review.

## Acceptance criteria

Clean backend/frontend installs succeed; smoke tests, lint and type checks pass; CI runs and archives actual evidence; setup instructions reproduce; no secrets or generated dependencies committed. These phase criteria are planning proposals; exact SRS requirements and approved acceptance criteria remain authoritative. Review questions Q-01–12 and conflicts F-01–13 in the Phase 0 documentation.

## Planned tests / checks

Write smoke tests before minimal stubs; confirm RED for missing behavior, then GREEN. Clean locked install, package/import and browser smoke, quality gates, dependency/secret scan and initial exact SBOM. Report actual statement and branch coverage with scope; never invent a value.

## Definition of done

Owner approves progression and resolves questions affecting this work. Each coherent feature has an issue and branch, expected-failure RED test run/commit, GREEN implementation/regression evidence, meaningful refactor where appropriate, required quality/security checks, accurate source headers, updated RTM with source/test/control/result/commit/CI links, and a reviewable PR.

Record actual pass/fail counts and coverage or explicitly NOT RUN; do not mark untested requirements VERIFIED. Stop for owner review at this phase boundary. No automatic merge, release, force push or clinical/regulatory claim.
