# Open questions and approval gates

Project Author: Michael Mart
Prepared by Codex, 10 October 2026. Q-01 progression APPROVED; all other decisions PENDING.

Question labels are review references, not requirement IDs. No response, elapsed
time, issue creation or pull request creation counts as approval. Answers should
record Michael Mart's decision, scope, date, revision and any reviewer role.

## Required now

**Q-01 — Phase 1 progression.** Approve or reject starting Phase 1 repository and
development-environment setup after reviewing this Phase 0 pull request. The
master prompt explicitly requires a stop here. Proposed next scope: locked Python
and React/TypeScript environments, test/lint/type tooling, CI, smoke tests,
development instructions and PR template; no alarm or application features yet.
Gate: before any Phase 1 work. Status: APPROVED by Michael Mart's `yes` in this
conversation on 10 October 2026; see [scope record](approvals.md).

**Q-02 — Proposed baseline and change control.** Confirm that the explicit
controlled addenda govern conflicting earlier text for planning, while source
requirements remain unapproved until recorded approval. Approve a controlled
document-correction work item for F-01–13; preserve originals and create new
versions rather than overwrite history. Phase 1 tooling can proceed with Q-01;
behavior affected by unresolved questions must wait. Gate: before affected
implementation; complete approved baseline required by CL-011 before release.

## Before affected implementation

| Question | Decision required and proposal | Required before | Requirement/control references |
| --- | --- | --- | --- |
| Q-03 | Approve the STP scenario-based crosswalk, replacement/supplemental test procedures, missing risk mappings, and measurable AR/DOC acceptance criteria. Proposed AR checks: dependency boundaries/fake adapters, formatting/lint, maintainability review and clean locked install. Proposed DOC checks: controlled artifacts, complete trace/evidence, reviewed risk register, representative workflow validation report, revisioned release package and applicability report. These are proposals, not approved source criteria. | Relevant Phase 1 process checks and Phase 2–9 verification; no VERIFIED labels before criteria approval | AR-001–006; DOC-001–006; QA-008; SF-006; CL-011/012; all RC-SAF/RC-CYB controls |
| Q-04 | Define malformed-input precedence and partial reading-set acceptance: if a reading has both invalid value and old timestamp, which rejection class wins? Does invalid HR affect an otherwise valid SpO₂ sample? Define rejected-input monitoring event versus security audit destination, field redaction and stopped-session input behavior. Proposal: explicitly classify before transition; no silent coercion; independent accepted values only where approved. | Affected Phase 2 validator tests and Phase 3–4 transitions | FR-004/005/007/008/013/015/016; CL-001/002; SEC-004/011; RC-SAF-001/003/006/008; RC-CYB-002/005 |
| Q-05 | Ratify API/snapshot enum names and error/status contracts; duplicate acknowledgment reject versus idempotent success, exact audit behavior, and reconnect race/session-generation handling. Proposal: versioned SAD/SDD routes, full snapshots, episode/session checks, no second mutation/event, and accepted mutations alone increment revision. | Phase 4 state contract and Phase 6 API; frontend depends on this | FR-009/010; SEC-014/016; CL-008; RC-SAF-004/007/009; RC-CYB-010 |
| Q-06 | Approve CL-009's 95% timing target and protocol, clarifying FR-002's “each” language: sample size, browser/OS/hardware, warm-up, backend acceptance-to-render measurement/clock alignment, healthy-connection definition, percentile/count calculation and exception review. Define maximum transport-loss detection delay and stale-status refresh interval. | Phase 7 timing implementation and Phase 8 acceptance | FR-001/002/011; CL-003/009; SEC-016; RC-SAF-003/007 |
| Q-07 | Set concrete request/frame sizes, rate limits, queue capacity, database timeouts, subscriber backpressure and overload policy. Define missed/deferred-tick detection/coalescing, audit durable intent/outcome protocol, crash windows and monotonic ordering versus UTC rollback. Proposal: bounded per-session serialization, nonblocking adapters and explicit failed/rejected command outcome. No numeric limit is approved. | Phase 4 service contracts and Phase 5–6 adapters/ingress | FR-013/014; SF-005; SEC-004/005/011; CL-001/003/005/006/008; RC-SAF-001/005; RC-CYB-003/005/012 |
| Q-08 | Select network identity/authentication and credential lifecycle, session ownership/membership, REST and WebSocket origin/CSRF policy, expiry/revocation revalidation, TLS termination and operator provisioning. Proposal: local loopback-only default for development; network mode unavailable until all controls are implemented and tested. Do not invent credentials or treat a local operator as authenticated network identity. | Phase 6 network features; boundary assumptions before affected Phase 4–5 audit work | SEC-001/002/003/005/006/013/014; CL-006/007; RC-SAF-009; RC-CYB-001/003/004/006/008/009/010/012 |
| Q-09 | Approve field-level data inventory and concrete monitoring/audit retention durations, deletion/backup rules, audit exceptions, access/file permissions, and deployment jurisdiction/controller/processor assumptions. Proposal: minimal synthetic data, analytics off, no patient identifiers, no identifiable production/test records. GDPR conclusion awaits actual account/IP/log processing and jurisdiction. | Phase 5 persistent data schema; Phase 6 accounts/logs; external distribution | PRIV-001–008; CL-010; SEC-005/006; RC-CYB-004/009 |
| Q-10 | Assign engineering owner, reviewer/mentor, security/privacy reviewer, risk acceptor and release approver; approve educational S/L scoring and acceptance process separately from cyber exploitability rationale. Michael Mart is project owner/author; no additional person, credential or organization is assumed. Specify independence/role overlap honestly. | Before risk acceptance, workflow validation or release approval; named review process before feature closure | SF-006; DOC-003/004/005; SEC-009/010/012; CL-011; all source risks and controls |
| Q-11 | Keep supplied December 2019 MDCG as historical baseline only, or add July 2020 Rev.1 as a new controlled reference and commission complete impact comparison? Proposal: preserve supplied file unchanged and version any added reference. | Regulatory-context sign-off and release applicability review | DOC-006; SEC-009/010; PRIV-007; CL-011/012 |
| Q-12 | Select update/artifact integrity and rollback mechanism, trusted-key/distribution boundary, vulnerability intake/contact channel, support assumptions, triage deadlines and exception approval policy. No email address, support promise, project license or legal organization is invented. License/distribution terms need an explicit owner choice before external distribution. | Phase 6 security process; Phase 9 release exercise/distribution | SEC-007/008/012/015; DOC-005; CL-011; RC-CYB-007/011 |

## Decisions already present in the proposed addenda

CD-01–05 and CL-001–011 explicitly select a single backend process, volatile
runtime state with no automatic restart recovery, distinct sensor/transport state,
monitoring-write degradation with persistent incomplete-history status, and
loopback local mode versus secured network mode. They also define scheduled-gap
resets, rejection classes, monotonic elapsed time, durable network audit failure
policy and revisioned authoritative snapshots. These are no longer open choices
in this proposed design. Their formal approval is still pending, and the detailed
questions above must not be dismissed by CL-012's broad closure statement.

## Approval record

Phase 1 progression: APPROVED for setup only (see [record](approvals.md)). Baseline approval: PENDING. Document-correction
approval: PENDING. Risk acceptance: NOT ASSESSED. Merge approval: PENDING.
Release approval: NOT REQUESTED. No additional approval has been inferred by Codex.
