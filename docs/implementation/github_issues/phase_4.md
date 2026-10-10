# Phase 4: Application services

Project Author: Michael Mart

Prepared by Codex for owner review. Educational synthetic-data-only simulation. Status: PLANNED / NOT STARTED — explicit owner approval required.

## Task

Implement orchestrator, session/alarm services, bounded command serialization, accepted-mutation revisions, complete snapshots, event generation and failure handling through ports. Resolve Q-04/05/07 and audit contracts before affected implementation.

## Requirements

FR-005 through FR-016; AR-001, AR-002, AR-003; SF-004, SF-005, SF-006; SEC-005, SEC-011, SEC-014, SEC-016; CL-001 through CL-008

## Risk controls

RC-SAF-001 through RC-SAF-009; RC-CYB-003, RC-CYB-005, RC-CYB-010, RC-CYB-012. All source controls remain proposed and unverified until actual evidence and review.

## Acceptance criteria

Concurrent commands serialize deterministically; rejected commands preserve state/revision; sessions remain isolated; failed event persistence cannot stop alarms; durable network audit failure denies accountable commands before mutation; history incompleteness persists. These phase criteria are planning proposals; exact SRS requirements and approved acceptance criteria remain authoritative. Review questions Q-01–12 and conflicts F-01–13 in the Phase 0 documentation.

## Planned tests / checks

Fake clock/sensor and failing repository/publisher tests; interleaved tick/ack/stop/fault commands; authorization and audit failures; revision/snapshot completeness; new-session reset. RED–GREEN proof and relevant regression/quality/coverage evidence.

## Definition of done

Owner approves progression and resolves questions affecting this work. Each coherent feature has an issue and branch, expected-failure RED test run/commit, GREEN implementation/regression evidence, meaningful refactor where appropriate, required quality/security checks, accurate source headers, updated RTM with source/test/control/result/commit/CI links, and a reviewable PR.

Record actual pass/fail counts and coverage or explicitly NOT RUN; do not mark untested requirements VERIFIED. Stop for owner review at this phase boundary. No automatic merge, release, force push or clinical/regulatory claim.
