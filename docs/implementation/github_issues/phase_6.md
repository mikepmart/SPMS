# Phase 6: API and cybersecurity

Project Author: Michael Mart

Prepared by Codex for owner review. Educational synthetic-data-only simulation. Status: PLANNED / NOT STARTED — explicit owner approval required.

## Task

Implement versioned FastAPI/WS contracts, authentication/roles/session scope, typed bounded input, redacted audit, secure mode configuration and TLS protections. Document threat model, vulnerability process and integrity/rollback design; no network mode until Q-08 controls are selected and verified.

## Requirements

SEC-001 through SEC-016; PRIV-001 through PRIV-008; AR-003; QA-003; FR-009, FR-010, FR-013, FR-015, FR-016; SF-006; CL-002, CL-003, CL-006, CL-007, CL-008, CL-010

## Risk controls

RC-SAF-004, RC-SAF-006, RC-SAF-007, RC-SAF-008, RC-SAF-009; RC-CYB-001 through RC-CYB-012. All source controls remain proposed and unverified until actual evidence and review.

## Acceptance criteria

Unauthorized/malformed/cross-session/expired/revoked requests cannot mutate alarms; observer is read-only; current episode binding enforced; REST/WS origins/session checked; local external bind denied; network HTTPS/WSS required; audit failures visible and fail closed; exact SBOM and scan dispositions recorded. These phase criteria are planning proposals; exact SRS requirements and approved acceptance criteria remain authoritative. Review questions Q-01–12 and conflicts F-01–13 in the Phase 0 documentation.

## Planned tests / checks

HTTPX negative/positive API tests; WebSocket auth/origin/expiry/revocation and resync; malformed/oversized/rate/queue-bound tests; stale/duplicate ack; TLS config, secret/redaction/dependency checks; audit fault injection. Coverage alone is not security acceptance.

## Definition of done

Owner approves progression and resolves questions affecting this work. Each coherent feature has an issue and branch, expected-failure RED test run/commit, GREEN implementation/regression evidence, meaningful refactor where appropriate, required quality/security checks, accurate source headers, updated RTM with source/test/control/result/commit/CI links, and a reviewable PR.

Record actual pass/fail counts and coverage or explicitly NOT RUN; do not mark untested requirements VERIFIED. Stop for owner review at this phase boundary. No automatic merge, release, force push or clinical/regulatory claim.
