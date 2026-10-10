# Phase 9: Release preparation

Project Author: Michael Mart

Prepared by Codex for owner review. Educational synthetic-data-only simulation. Status: PLANNED / NOT STARTED — explicit owner approval required.

## Task

Prepare revisioned release notes, SBOM, scan/verification/coverage/risk reports, known limits, unresolved anomalies, install instructions and user guide. Exercise integrity/rollback and clean setup; record risk/privacy/support decisions. Do not publish a final release without approval.

## Requirements

DOC-001 through DOC-006; AR-006; QA-005, QA-006, QA-008; SF-001, SF-006; SEC-007, SEC-008, SEC-010, SEC-012, SEC-015; PRIV-001 through PRIV-008; CL-010, CL-011, CL-012

## Risk controls

RC-SAF-001 through RC-SAF-010; RC-CYB-001 through RC-CYB-012 (evidence/disposition review). All source controls remain proposed and unverified until actual evidence and review.

## Acceptance criteria

Approved baseline and control mappings; actual passing evidence and coverage; exact locked dependency SBOM; vulnerability/anomaly dispositions signed off; reproducible install; update integrity/rollback demonstrated; synthetic-only/nonclinical labels; all required role approvals recorded. These phase criteria are planning proposals; exact SRS requirements and approved acceptance criteria remain authoritative. Review questions Q-01–12 and conflicts F-01–13 in the Phase 0 documentation.

## Planned tests / checks

Clean locked install and browser smoke, artifact tampering rejection and rollback exercise, exact SBOM/lock matching, scan triage, release checklist/RTM/risk/privacy review. Repeat broader tests only for changed artifacts or unresolved concerns; record exact source/artifact revisions.

## Definition of done

Owner approves progression and resolves questions affecting this work. Each coherent feature has an issue and branch, expected-failure RED test run/commit, GREEN implementation/regression evidence, meaningful refactor where appropriate, required quality/security checks, accurate source headers, updated RTM with source/test/control/result/commit/CI links, and a reviewable PR.

Record actual pass/fail counts and coverage or explicitly NOT RUN; do not mark untested requirements VERIFIED. Stop for owner review at this phase boundary. No automatic merge, release, force push or clinical/regulatory claim.
