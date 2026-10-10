# Sequential implementation plan

Project Author: Michael Mart
Prepared by Codex, 10 October 2026. Plan status: PROPOSED; Phase 1 progression
APPROVED in conversation (see [approval record](approvals.md)).

## Scope and authority

Build an educational synthetic-data-only simulator, using pure Python monitoring
rules, FastAPI/SQLite adapters and a React/TypeScript dashboard. No patient data,
clinical purpose, regulatory conformity or final release is authorized by this
plan. The [inventory](requirements_inventory.md) carries the exact 78 requirements
and original acceptance criteria. The [review](document_review.md) and
[open questions](open_questions.md) qualify the baseline and its unresolved details.

Phase 0 is reviewed and [Phase 1 setup is complete](phase_1_report.md), pending
owner review. Each subsequent major phase needs Michael Mart's
explicit progression approval after its report and reviewable PR. Opening an issue
does not start a phase, approve a baseline correction, accept risk or authorize merge.

## GitHub roadmap and phase gates

Each linked issue contains requirements, existing control IDs, proposed phase
acceptance criteria, planned tests and definition of done. All ten issues were
created and then read back from GitHub to verify their titles and open state.
The [work-item record](github_work_items.json) and [issue drafts](github_issues/phase_0.md)
preserve the requested scope. Feature-sized child issues and branches will be
created when their phase is approved; do not implement an entire phase as one
unreviewable change.

| Phase / issue | Scope | Required completion evidence / next gate |
| --- | --- | --- |
| 0 — [Document/project review #1](https://github.com/mikepmart/SPMS/issues/1) | Read 13 sources; inventory 78 requirements/22 controls; find conflicts; propose architecture/roadmap; publish issues and review documentation. | Five requested review artifacts, hashes/wording checks, committed branch, PR and honest phase report. **STOP for Michael Mart's Phase 1 approval.** |
| 1 — [Repository/environment #2](https://github.com/mikepmart/SPMS/issues/2) | Backend/frontend structures and locked environments; pytest/cov, Ruff, mypy, lint/TypeScript, Vitest, Playwright; CI, .gitignore, README, smoke tests and PR template. | Clean backend/frontend installs, initial tests/lint/types pass, CI actually executes with artifacts, reproducible instructions and exact tool/dependency versions recorded. No alarm features. STOP for review/Phase 2 approval. |
| 2 — [Models/validation #3](https://github.com/mikepmart/SPMS/issues/3) | Measurements, sessions, domain events, finite/range/type/UTC-order validation and rejection classifications. Resolve affected Q-03/Q-04 first. | RED–GREEN evidence for inclusive bounds, NaN/Infinity, missing/wrong types, duplicate/older/per-kind timestamps and preservation. Pure domain dependency boundary holds. STOP for Phase 3 approval. |
| 3 — [Alarm state machine #4](https://github.com/mikepmart/SPMS/issues/4) | Activation, recovery, acknowledgment, episode identity, counter resets and invalid/missing/disconnect behavior. | Every source transition/boundary tested deterministically, including both active acknowledgment states, low-low-gap-low and recovery-recovery-gap-recovery. No ambiguous transition implemented. STOP for Phase 4 approval. |
| 4 — [Application services #5](https://github.com/mikepmart/SPMS/issues/5) | Orchestrator/services, bounded serialization, revisions/full snapshots, session isolation, domain events and sink failures through ports. Resolve Q-04/Q-05/Q-07. | Interleaved tick/ack/stop/fault tests; accepted/rejected mutation semantics; monitoring-write continuation versus accountable-audit denial; completeness persists. STOP for Phase 5 approval. |
| 5 — [Infrastructure #6](https://github.com/mikepmart/SPMS/issues/6) | Synthetic sensor, monotonic/UTC clocks, SQLite event/audit adapters, restart and persistence faults. Resolve retention/audit/I/O contracts. | Real temporary DB integrations, 10 fake-clock ticks, stale boundary/clock change, injected store faults, actual process kill/restart, scoped readable history and privacy review. STOP for Phase 6 approval. |
| 6 — [API/cybersecurity #7](https://github.com/mikepmart/SPMS/issues/7) | Versioned REST/WS, auth/roles/session/origin/lifecycle, bounded schemas/requests, audit/redaction, secure config/TLS and security process. Resolve Q-05/Q-07/Q-08/Q-09/Q-12 as affected. | Positive and negative REST/WS security tests, malformed/replay/cross-session/observer/expiry/revocation/overload cases, default loopback and secured network configuration, fault/redaction checks, threat/control review and scan dispositions. STOP for Phase 7 approval. |
| 7 — [Dashboard #8](https://github.com/mikepmart/SPMS/issues/8) | Values/units/timestamps, alarm/ack, controls, event history, independent sensor/transport/freshness/storage/restart indicators. Resolve Q-05/Q-06. | Vitest/RTL before components and Playwright workflows; persistent exact warning; text plus color; no frontend alarm logic; old-revision discard/resync; controlled timing measurements/exceptions. STOP for Phase 8 approval. |
| 8 — [System verification #9](https://github.com/mikepmart/SPMS/issues/9) | Complete unit/integration/security/fault/frontend/browser suites, lint/types, coverage, traceability and representative educational workflow validation. | Actual results tied to commit/CI; ≥90% Python statement coverage across maintained app source and branch coverage separately; explicit passing evidence for every control; reviewed anomalies and workflow report. STOP for Phase 9 approval. |
| 9 — [Release preparation #10](https://github.com/mikepmart/SPMS/issues/10) | Notes, exact SBOM, scans, verification/coverage/risk reports, known limits/anomalies, install/user guide, reproducible setup and integrity/rollback exercise. | CL-011 approved baseline/control mappings, actual tests, vulnerability/anomaly dispositions, role sign-offs, privacy/retention and integrity/rollback evidence. **STOP; final release requires separate approval.** |

Dependencies are sequential 0→1→2→3→4→5→6→7→8→9, with owner review at every arrow.
An implementation question blocks affected behavior, not unrelated approved setup.
No scope may be silently omitted to declare a phase complete.

## Feature workflow after approval

1. Read exact requirement/criteria, controls and relevant resolved questions.
   Create a coherent feature issue and branch from the approved base.
2. RED: write behavior tests first, run them, confirm the expected missing-behavior
   failure, retain the result and commit with a clear `test(...)` message. A broken
   environment is not valid RED evidence.
3. GREEN: implement the smallest sound change, run new and relevant regression
   tests and commit with `feat(...)` or `fix(...)`.
4. REFACTOR: improve names/types/dependencies/duplication when useful, rerun tests
   and commit meaningful changes. Do not manufacture commits for their count.
5. VERIFY: run applicable pytest/pytest-cov, Ruff, mypy, frontend lint/TypeScript,
   Vitest, Playwright and security checks; report real outcomes and limitations.
6. TRACE: add implementation/test references, existing controls, actual result,
   commit SHA and CI artifacts to RTM. Unexecuted planned cases remain NOT RUN.
7. PR: explain requirements, behavior, tests/results, statement/branch coverage,
   risk/security changes, docs and limitations. Never merge a branch with failing
   required checks. Stop for review; never merge automatically.

Branch examples in the master prompt are conventions, not existing branches.
Use Conventional Commits; retain intentional RED commits on feature history and
make the PR's final revision pass required checks. Never force push, rewrite
published history, commit secrets, change visibility, invent a license or edit
third-party attribution. Human-maintained source/test/config files must have
accurate language-appropriate purpose/responsibility/project-author/requirement/
control headers where applicable. Do not add comments to JSON, generated code,
lockfiles or vendor files. Mark Codex preparation honestly.

## Verification strategy and evidence

Unit tests cover all state/validation/timestamp/freshness boundaries with fake time.
Integration tests cover scheduler, event/audit storage faults, command concurrency,
session isolation and actual restart. API/WS tests cover auth/roles/session/origin,
credential lifecycle, bounded input and failed audit. Browser tests cover user
flows, independent connection states, failure indicators and measured timing.
Coverage supports these scenarios; it does not replace control-effectiveness tests.

Python statement coverage must be ≥90% across maintained application source;
report branch coverage separately on each automated verification run. Do not hide
uncovered code with arbitrary exclusions. Require formatting/lint/types and all
applicable test/security gates. Initial Phase 1 CI must establish jobs for Python
format/lint/types/unit/integration/coverage, frontend lint/types/unit/browser,
security, vulnerability and secret scans, and exact machine-readable SBOM.
Jobs for future features must transparently report scope instead of fabricating
passing suites. Archive results and reports with the tested source revision.

For each risk record retain cause/sequence, educational effect, initial rationale,
control implementation/effectiveness evidence, new risks, residual disposition,
approver and date. No control is verified merely by being listed in a header or
having a similarly numbered planned test. Reconcile the source test-ID conflicts
before executable test links are treated as traceability. Record representative
user validation separately from verification and never call it clinical validation.

## Release gate

No release is currently approved. Before any educational release, reconcile and
approve the baseline; implement applicable requirements; run required tests;
verify every control; satisfy statement coverage and report branches; triage scan
findings; generate an exact locked-dependency SBOM; sign off open anomalies and
residual risks; demonstrate reproducible install and integrity/rollback; document
privacy applicability/retention, support assumptions and nonclinical limitations;
record authorized approvals. Phase 9 preparation alone does not publish a release.
