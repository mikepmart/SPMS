# Phase 5: Infrastructure

Project Author: Michael Mart

Prepared by Codex for owner review. Educational synthetic-data-only simulation. Status: PLANNED / NOT STARTED — explicit owner approval required.

## Task

Implement synthetic sensor, clocks, SQLite event/audit adapters, storage faults and stopped-on-restart behavior. Resolve bounded I/O, audit durability, retention/deletion, permissions and event ordering contracts before persistent schema work.

## Requirements

FR-001, FR-011, FR-012, FR-013, FR-014, FR-016; AR-002; SF-005, SF-006; SEC-005, SEC-006; PRIV-003, PRIV-005, PRIV-006; CL-001, CL-003, CL-004, CL-005, CL-006, CL-010

## Risk controls

RC-SAF-001, RC-SAF-002, RC-SAF-003, RC-SAF-005, RC-SAF-007, RC-SAF-008; RC-CYB-003, RC-CYB-004, RC-CYB-009, RC-CYB-012. All source controls remain proposed and unverified until actual evidence and review.

## Acceptance criteria

Fake-clock 10-second run emits 10 scheduled sets; freshness exact boundary works; event ordering is deterministic; monitoring/audit sink failures obey distinct policies; restart never restores old active state; history available only when readable and authorized. These phase criteria are planning proposals; exact SRS requirements and approved acceptance criteria remain authoritative. Review questions Q-01–12 and conflicts F-01–13 in the Phase 0 documentation.

## Planned tests / checks

Temporary SQLite integrations and fault injection (write denial/unavailable sink/failed read); wall-clock changes with monotonic elapsed time; actual forced process termination/restart; retention/deletion/backups; redaction and least-privilege review. RED–GREEN before adapter behavior.

## Definition of done

Owner approves progression and resolves questions affecting this work. Each coherent feature has an issue and branch, expected-failure RED test run/commit, GREEN implementation/regression evidence, meaningful refactor where appropriate, required quality/security checks, accurate source headers, updated RTM with source/test/control/result/commit/CI links, and a reviewable PR.

Record actual pass/fail counts and coverage or explicitly NOT RUN; do not mark untested requirements VERIFIED. Stop for owner review at this phase boundary. No automatic merge, release, force push or clinical/regulatory claim.
