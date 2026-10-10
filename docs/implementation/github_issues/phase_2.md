# Phase 2: Domain models and validation

Project Author: Michael Mart

Prepared by Codex for owner review. Educational synthetic-data-only simulation. Status: PLANNED / NOT STARTED — explicit owner approval required.

## Task

Implement pure Python measurements, sessions, domain events and validation; UTC timestamp ordering and explicit rejection classes. Obtain Q-04 clarification before ambiguous mixed-invalid/partial-set behavior.

## Requirements

FR-003, FR-004, FR-005, FR-013, FR-014, FR-015, FR-016; AR-001, AR-002; QA-001, QA-002; SF-006; CL-002, CL-003

## Risk controls

RC-SAF-003, RC-SAF-006, RC-SAF-008; RC-CYB-002 (domain validation contribution). All source controls remain proposed and unverified until actual evidence and review.

## Acceptance criteria

Inclusive HR 0–300 and SpO2 0–100 accepted; wrong types, missing/nonfinite/out-of-range values rejected; last accepted values preserved; duplicate/older timestamps rejected without counter mutation; model invariants documented and traceable. These phase criteria are planning proposals; exact SRS requirements and approved acceptance criteria remain authoritative. Review questions Q-01–12 and conflicts F-01–13 in the Phase 0 documentation.

## Planned tests / checks

RED–GREEN boundary and type tests including NaN/Infinity, missing values, equal/older timestamps, kind-specific ordering and timezone handling. Confirm domain imports no frontend/network/storage implementation. Relevant regressions, quality and coverage gates.

## Definition of done

Owner approves progression and resolves questions affecting this work. Each coherent feature has an issue and branch, expected-failure RED test run/commit, GREEN implementation/regression evidence, meaningful refactor where appropriate, required quality/security checks, accurate source headers, updated RTM with source/test/control/result/commit/CI links, and a reviewable PR.

Record actual pass/fail counts and coverage or explicitly NOT RUN; do not mark untested requirements VERIFIED. Stop for owner review at this phase boundary. No automatic merge, release, force push or clinical/regulatory claim.
