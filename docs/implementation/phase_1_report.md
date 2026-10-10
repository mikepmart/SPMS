# Phase 1 — Repository and development environment

Project Author: Michael Mart. Prepared by Codex, 10 October 2026.

**Status: COMPLETE for Phase 1 setup; owner review and Phase 2 approval pending.**
This is a scaffold verification report, not an educational release or product
acceptance report. No source requirement or risk control is declared fully VERIFIED.

## Requirements and implementation

Phase 1 supports AR-004/006, QA-001/003/004/005/006/007/008, DOC-002,
SEC-007/008/013, SF-001 and PRIV-001. The [working RTM](traceability.md) records
the exact scope limits for all 15 contributions and preserves all 78 requirement
and acceptance-criteria texts in [JSON](traceability.json).

Created separate backend domain/application/infrastructure/API namespaces,
a FastAPI factory with only a process-health endpoint, and a React/TypeScript
shell showing the exact nonclinical notice and stopped state. No domain model,
measurement generator, alarm, monitoring route, account or database is implemented.
These belong to later approved phases.

Added pinned runtimes, Python/npm lockfiles, pytest/cov/Ruff/mypy,
ESLint/Prettier/TypeScript/Vitest/Playwright, ignore/line-ending/editor settings,
the required PR template, and seven GitHub Actions jobs. All human-maintained
source files carry project/purpose/responsibility/requirement/control attribution;
JSON, generated locks and simple version files contain no invalid headers.

## Tests and actual results

[RED/GREEN evidence](phase_1_tdd.md) records the tests-first sequence. Intentional
RED `bfd31f8` produced 13 expected Python failures and one failed frontend suite
for the missing app component (zero tests collected in that suite). An earlier
dependency collection error was corrected and was not counted as valid RED.

| Verification | Actual result |
| --- | --- |
| Backend unit/tooling/integration/negative configuration tests | 13 passed, 0 failed, 0 skipped locally and independently on Windows and Ubuntu CI. |
| Frontend unit test | 1 passed, 0 failed, 0 skipped locally and on both CI operating systems. |
| Real Chromium / built UI / HTTP backend smoke | 1 passed, 0 failed, 0 skipped locally and on Ubuntu CI. |
| Python formatting / lint / strict types | PASS locally and on both CI operating systems; mypy checked 10 maintained source/test/tool files. |
| Frontend formatting / lint / strict types / production build | PASS locally and on both CI operating systems. No `skipLibCheck` or warning/error suppression added. |
| Clean-install rehearsal | PASS at committed revision `5cdc176`: fresh Python environment, `npm ci`, production build, 13 Python tests, 1 frontend test and 1 Chromium test. No environment activation or execution-policy change. |

There are 15 distinct bootstrap/tooling test cases, not 15 product acceptance
scenarios. CI executes the 13 Python and one frontend case on each operating
system plus one Linux Chromium case (29 executions). The test-marked security
case checks debug/documentation defaults; authentication and other Phase 6
security scenarios do not exist yet.

The first local browser attempt passed its assertion but hung during restricted
child-process cleanup. Its verified test process tree was stopped and its
nonzero exit was not counted as a completed run. A permitted rerun and an
independent clean-worktree browser run both exited 0. CI also exited successfully.

## Coverage

Python application statement coverage is **100% (7/7)** across every maintained
`spms` module, with no excluded statements. Application branch coverage is
**not applicable (0/0)**. The custom gate reports this honestly as `null` rather
than treating coverage.py's empty-branch convention as tested behavior.
The exact 90% statement gate is independent of branches and rejects 89.9%
without rounding. Nine tooling cases exercise boundary and invalid-report behavior.
The coverage utility is verification tooling rather than application source.

Frontend unit statement coverage is **20% (1/5)** and branch coverage **0% (0/2)**.
The component is covered; `main.tsx` is retained in coverage despite being
exercised only by the separate browser test. No frontend percentage gate was
invented and browser coverage is not blended into unit coverage.
The small bootstrap's Python percentage does not imply future monitoring coverage.

## Security and dependency evidence

The [successful CI run](https://github.com/mikepmart/SPMS/actions/runs/38076892742)
scanned 79 applicable exact Python runtime/development dependencies with no
known vulnerabilities and no skipped dependencies. npm audit reported zero
known vulnerabilities at every severity (444 lock dependency entries, including
platform/optional entries). Bandit scanned application and verification-tool
source with zero findings/errors, zero `nosec` suppressions. Gitleaks scanned
complete fetched Git history and reported zero secrets; the local history scan
also passed before push. Checks are scoped to the recorded revision/advisory date.

CycloneDX 1.6 JSON SBOMs were generated and retained: CI Linux backend 79
dependency components and frontend 375 installed dependency components, with
the root component recorded separately. These target-environment SBOMs include
development tools; the lockfiles also record conditional packages for other
platforms. This is tooling setup for SEC-008, not a release SBOM approval.

Pinned Gitleaks archives are checked against official SHA-256 manifests before
execution. Official CI actions are pinned to verified commit SHAs. Workflows
use a read-only contents token and no `pull_request_target` or automatic merge.
Development servers bind loopback; network-mode product security is future work.

Two npm deprecation warnings remain: `glob@10.5.0` and
`prebuild-install@7.1.3`, both optional development descendants of the SBOM
tool's `libxmljs2` dependency. `npm explain` confirmed these paths. Lifecycle
scripts are disabled, JSON SBOM generation works, and current advisory scans
report no matching vulnerabilities. They remain recorded maintenance items
under issue #14; no suppression, forced transitive override or residual-risk
acceptance has been inferred. Reassess before release preparation.

## GitHub and evidence

Branch: `chore/phase-1-environment`, stacked on `docs/phase-0-review` at
`731c7f9877626a34e61f73582bc654812ec85f81`. Phase 0 PR
[#11](https://github.com/mikepmart/SPMS/pull/11) remains open and unmerged.
The Phase 1 PR targets that branch so its diff contains only Phase 1 work;
retarget to `main` after the owner reviews and merges Phase 0.

- RED: `bfd31f8e9c5b398c4d0efa109e05e3f2bd10a1d3`.
- GREEN: `0a5a8f8c22fa5ed2d2b77a62e5965bcf468b924d`.
- Verified source/toolchain/CI: `5cdc17663f1586309071b64157cb881342a3fe8b`.
- Parent issue [#2](https://github.com/mikepmart/SPMS/issues/2); work items
  [#12](https://github.com/mikepmart/SPMS/issues/12),
  [#13](https://github.com/mikepmart/SPMS/issues/13),
  [#14](https://github.com/mikepmart/SPMS/issues/14).

All seven jobs concluded success. All seven archived result bundles were
downloaded; their official artifact digests were checked and JUnit/coverage/
security/SBOM contents inspected. [Committed verification metadata](phase_1_verification.json)
records job/artifact URLs, digests, actual counts and local command exits.
Full reports are retained in GitHub for 30 days; local copies are under ignored
`artifacts/` and workspace task temporary storage. Documentation-only follow-up
commits preserve the tested implementation; final PR checks must also pass.
No branch-protection settings or independent human review are claimed.

## Documentation and remaining gates

Updated README installation/run/verification instructions, approval record,
implementation-plan and open-question status, working RTM, TDD record and this
report. All 13 original source hashes remain unchanged; no source XLSX or
acceptance criterion was overwritten. Phase 0 inventory and risk register remain
unchanged, including proposed baseline and NOT VERIFIED / NOT ASSESSED statuses.

The [approval record](approvals.md) authorizes Phase 1 setup only. Q-02–12,
baseline/criteria approval, full risk-control verification and residual-risk
acceptance remain pending. No PR is merged and no release is approved.

**Next proposed work: Phase 2 — domain models and validation, only after Michael
Mart approves progression and affected Q-03/Q-04 decisions are resolved. STOP.**
