# Phase 8: System verification

Project Author: Michael Mart

Prepared by Codex for owner review. Educational synthetic-data-only simulation. Status: PLANNED / NOT STARTED — explicit owner approval required.

## Task

Execute backend/frontend/system/security/fault suites, lint/type checks, statement and branch coverage, traceability review and representative educational-user workflow validation. Investigate and retain failures; approve source criteria and test crosswalk first.

## Requirements

All 78 SRS v1.2/RTM v1.1 requirements; especially QA-001 through QA-008, SF-006, DOC-002, DOC-003, DOC-004, SEC-010, CL-009, CL-011

## Risk controls

RC-SAF-001 through RC-SAF-010; RC-CYB-001 through RC-CYB-012. All source controls remain proposed and unverified until actual evidence and review.

## Acceptance criteria

Required suites and quality checks pass; Python statement coverage >=90% across maintained app code with branch coverage separately reported; each risk control has passing effectiveness evidence tied to exact revision; RTM has source/test/commit/CI links; anomalies and residual reviews are explicit. These phase criteria are planning proposals; exact SRS requirements and approved acceptance criteria remain authoritative. Review questions Q-01–12 and conflicts F-01–13 in the Phase 0 documentation.

## Planned tests / checks

Full backend unit/integration, API/WS security, store/audit/network/restart/concurrency faults, Vitest and Playwright suites; timing protocol; install reproduction; risk-control scenario review. Workflow validation report records actual users/reviewers and outcomes, never invented clinical validation.

## Definition of done

Owner approves progression and resolves questions affecting this work. Each coherent feature has an issue and branch, expected-failure RED test run/commit, GREEN implementation/regression evidence, meaningful refactor where appropriate, required quality/security checks, accurate source headers, updated RTM with source/test/control/result/commit/CI links, and a reviewable PR.

Record actual pass/fail counts and coverage or explicitly NOT RUN; do not mark untested requirements VERIFIED. Stop for owner review at this phase boundary. No automatic merge, release, force push or clinical/regulatory claim.
