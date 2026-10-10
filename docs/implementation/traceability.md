# Working requirements traceability

Project Author: Michael Mart. Prepared by Codex, 10 October 2026.

This additive working RTM supplements the unchanged proposed source XLSX.
[Machine-readable rows](traceability.json) preserve all 78 requirement and
acceptance-criteria texts exactly, including unresolved source inconsistencies.
The [inventory](requirements_inventory.md) preserves original planned test IDs.
Bootstrap test identifiers below are not substitutes for product acceptance
procedures. No requirement or control is marked VERIFIED; baseline/criteria
approval, full behavior verification and risk acceptance remain pending.

Measured source revision: `5cdc17663f1586309071b64157cb881342a3fe8b`. [Successful CI artifacts](https://github.com/mikepmart/SPMS/actions/runs/38076892742) are
summarized with checksums in [verification evidence](phase_1_verification.json).
Implementation references include GREEN `0a5a8f8` and CI `5cdc176`; RED
`bfd31f8` precedes implementation. The original risk register retains its
OPEN/NOT VERIFIED and residual NOT ASSESSED statuses.

## Phase 1 contributions

| Requirement | Implementation / check references | Supporting controls | Actual result and scope limit |
| --- | --- | --- | --- |
| SF-001 | `frontend/src/App.tsx`; `frontend/src/App.test.tsx`; `frontend/e2e/bootstrap.spec.ts` | RC-SAF-010 | PASS supporting check only. Exact notice visible on the sole scaffold screen; future monitoring screens not implemented. |
| AR-004 | `backend/pyproject.toml`; `frontend/eslint.config.js`; `frontend/package.json`; `ruff format --check .`; `ruff check .`; `npm run format:check`; `npm run lint` | None claimed | PASS supporting check only. Configured formatting and lint pass; source acceptance criteria approval remains pending. |
| AR-006 | `backend/uv.lock`; `frontend/package-lock.json`; `.python-version`; `.node-version`; `.uv-version`; `uv sync --locked --project backend`; `npm ci`; `clean install rehearsal` | None claimed | PASS supporting check only. Exact dependencies/runtimes recorded and fresh installs tested. |
| QA-001 | `docs/implementation/phase_1_tdd.md`; `backend/tests/`; `frontend/src/App.test.tsx` | None claimed | PASS supporting check only. Intentional RED bfd31f8 precedes GREEN 0a5a8f8; applies to bootstrap only. |
| QA-003 | `backend/src/spms/api/app.py`; `tests/integration/test_health.py::test_health_identifies_the_synthetic_only_scaffold`; `tests/integration/test_health.py::test_monitoring_routes_are_not_exposed_by_bootstrap` | None claimed | PASS supporting check only. HTTP integration smoke infrastructure only; sensor/state/event-store acceptance scenarios remain NOT RUN. |
| QA-004 | `frontend/playwright.config.ts`; `frontend/e2e/bootstrap.spec.ts`; `loads the stopped simulation shell and the nonclinical backend` | None claimed | PASS supporting check only. Real Chromium bootstrap test only; monitoring/ack/failure/recovery/history scenarios remain NOT RUN. |
| QA-005 | `backend/pyproject.toml`; `backend/tools/check_coverage.py`; `tests/tooling/test_coverage_gate.py`; `pytest --cov=spms --cov-branch` | None claimed | PASS supporting check only. Application statements 7/7 (100%); exact 90% gate tested against 89%, 89.9%, 90%, 100% and invalid evidence. |
| QA-006 | `backend/tools/check_coverage.py`; `tests/tooling/test_coverage_gate.py::test_statement_gate_is_independent_of_branches` | None claimed | PASS supporting check only. Branches reported apart; application currently 0/0, not applicable. |
| QA-007 | `.github/workflows/verify.yml`; `seven CI jobs and their executable steps` | None claimed | PASS supporting check only. Push and PR workflow executes tests, lint, formatting, types and coverage on Windows/Linux. |
| QA-008 | `.github/workflows/verify.yml`; `docs/implementation/phase_1_verification.json`; `seven downloaded CI artifacts with verified SHA-256 digests` | None claimed | PASS supporting check only. JUnit, coverage, security and SBOM artifacts retained 30 days; preserve release evidence separately before expiry. |
| DOC-002 | `docs/implementation/traceability.json`; `docs/implementation/traceability.md`; `78 exact requirement/criteria rows compared to inventory; 13 source hashes unchanged` | None claimed | PASS supporting check only. Additive working RTM records implementation/test/control/result/commit/CI references; original XLSX preserved. |
| SEC-007 | `.github/workflows/verify.yml`; `backend/uv.lock`; `frontend/package-lock.json`; `pip-audit --require-hashes --disable-pip --strict`; `npm audit --json` | RC-CYB-007 | PASS supporting check only. CI scans exact Python and npm runtime/development dependencies; zero known findings in recorded run, no skips/suppressions. |
| SEC-008 | `.github/workflows/verify.yml`; `frontend/package.json`; `cyclonedx-py environment`; `npm run sbom` | RC-CYB-007 | PASS supporting check only. Phase 1 target-environment CycloneDX SBOMs generated; no release exists and release requirement remains pending. |
| SEC-013 | `backend/src/spms/api/app.py`; `frontend/vite.config.ts`; `frontend/playwright.config.ts`; `.github/workflows/verify.yml`; `tests/unit/test_bootstrap.py::test_bootstrap_disables_debug_and_interactive_api_docs`; `frontend/e2e/bootstrap.spec.ts` | RC-CYB-006 | PASS supporting check only. Loopback development defaults, no debug/docs and read-only CI token; full secure product/network-mode control not implemented. |
| PRIV-001 | `frontend/src/App.tsx`; `backend/src/spms/api/app.py`; `frontend/src/App.test.tsx`; `tests/integration/test_health.py::test_health_identifies_the_synthetic_only_scaffold` | None claimed | PASS supporting check only. Synthetic-only identity and stopped state; no measurement generation, storage or personal data introduced. Full data-flow verification pending. |

## Complete requirement status index

Exact text/acceptance/source-control fields are in the JSON above; no row is omitted.

| ID | Working status | Original source verification |
| --- | --- | --- |
| FR-001 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-002 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-003 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-004 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-005 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-006 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-007 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-008 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-009 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-010 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-011 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-012 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-013 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-014 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-015 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| FR-016 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SF-001 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| SF-002 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SF-003 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SF-004 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SF-005 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SF-006 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| AR-001 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| AR-002 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| AR-003 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| AR-004 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| AR-005 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| AR-006 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| QA-001 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| QA-002 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| QA-003 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| QA-004 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| QA-005 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| QA-006 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| QA-007 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| QA-008 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| DOC-001 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| DOC-002 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| DOC-003 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| DOC-004 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| DOC-005 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| DOC-006 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-001 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-002 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-003 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-004 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-005 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-006 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-007 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| SEC-008 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| SEC-009 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-010 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-011 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-012 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-013 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| SEC-014 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-015 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| SEC-016 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| PRIV-001 | PARTIAL / SUPPORTING EVIDENCE ONLY — NOT VERIFIED | NOT RUN |
| PRIV-002 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| PRIV-003 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| PRIV-004 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| PRIV-005 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| PRIV-006 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| PRIV-007 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| PRIV-008 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-001 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-002 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-003 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-004 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-005 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-006 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-007 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-008 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-009 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-010 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-011 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
| CL-012 | NOT IMPLEMENTED / NOT RUN | NOT RUN |
