# Phase 3: Alarm state machine

Project Author: Michael Mart

Prepared by Codex for owner review. Educational synthetic-data-only simulation. Status: PLANNED / NOT STARTED — explicit owner approval required.

## Task

Implement deterministic activation/recovery, acknowledgment, new episode identity, pending counters and invalid/missing/disconnect transitions. No ambiguous transition implemented without clarification.

## Requirements

FR-006, FR-007, FR-008, FR-009, FR-010, FR-012, FR-015; SF-004, SF-006; SEC-014 (domain episode semantics); CL-001, CL-002

## Risk controls

RC-SAF-001, RC-SAF-002, RC-SAF-004, RC-SAF-006; RC-CYB-010. All source controls remain proposed and unverified until actual evidence and review.

## Acceptance criteria

Three consecutive valid SpO2 <92 activate; >=92 is non-low; three >=92 clear active alarm. Ack never clears; new episode needs new ack. Scheduled gaps/invalid classes reset pending counts as specified; replay/wrong-session/unauthorized input preserves counters; disconnect preserves active alarm. These phase criteria are planning proposals; exact SRS requirements and approved acceptance criteria remain authoritative. Review questions Q-01–12 and conflicts F-01–13 in the Phase 0 documentation.

## Planned tests / checks

RED–GREEN tests for every documented state/input transition and 91/92/93 boundaries, both active ack states, low-low-gap-low, recovery-recovery-gap-recovery, rejected timestamps and episode reuse. Reconcile STP/RTM IDs rather than assuming same-number meaning.

## Definition of done

Owner approves progression and resolves questions affecting this work. Each coherent feature has an issue and branch, expected-failure RED test run/commit, GREEN implementation/regression evidence, meaningful refactor where appropriate, required quality/security checks, accurate source headers, updated RTM with source/test/control/result/commit/CI links, and a reviewable PR.

Record actual pass/fail counts and coverage or explicitly NOT RUN; do not mark untested requirements VERIFIED. Stop for owner review at this phase boundary. No automatic merge, release, force push or clinical/regulatory claim.
