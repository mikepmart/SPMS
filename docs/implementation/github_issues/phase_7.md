# Phase 7: Frontend dashboard

Project Author: Michael Mart

Prepared by Codex for owner review. Educational synthetic-data-only simulation. Status: PLANNED / NOT STARTED — explicit owner approval required.

## Task

Implement React/TypeScript measurement/alarm dashboard, controls, event history, independent sensor/transport status, freshness and failure indicators. Render backend state only. Approve Q-05/06 contracts and timing methodology first.

## Requirements

FR-002, FR-003, FR-005, FR-009, FR-010, FR-011, FR-012, FR-014; SF-001 through SF-005; AR-003; QA-004; SEC-002, SEC-014, SEC-016; CL-003, CL-004, CL-005, CL-007, CL-008, CL-009

## Risk controls

RC-SAF-002, RC-SAF-003, RC-SAF-004, RC-SAF-005, RC-SAF-007, RC-SAF-010; RC-CYB-004, RC-CYB-005, RC-CYB-010. All source controls remain proposed and unverified until actual evidence and review.

## Acceptance criteria

Exact simulation-only warning visible on every monitoring screen; states readable without color alone; latest accepted values/units/timestamps match backend; ack does not clear; reconnect drops old revisions and fetches state; restart/storage/history status visible; approved CL-009 timing target measured. These phase criteria are planning proposals; exact SRS requirements and approved acceptance criteria remain authoritative. Review questions Q-01–12 and conflicts F-01–13 in the Phase 0 documentation.

## Planned tests / checks

Vitest/React Testing Library unit tests before components; Playwright start/stop/low/ack/recovery/disconnect/reconnect/restart/storage flows; observer and session access; accessibility labels, stale/no-data and transport separation; controlled browser timing and exception log.

## Definition of done

Owner approves progression and resolves questions affecting this work. Each coherent feature has an issue and branch, expected-failure RED test run/commit, GREEN implementation/regression evidence, meaningful refactor where appropriate, required quality/security checks, accurate source headers, updated RTM with source/test/control/result/commit/CI links, and a reviewable PR.

Record actual pass/fail counts and coverage or explicitly NOT RUN; do not mark untested requirements VERIFIED. Stop for owner review at this phase boundary. No automatic merge, release, force push or clinical/regulatory claim.
