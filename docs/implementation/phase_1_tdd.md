# Phase 1 TDD evidence

Project Author: Michael Mart. Prepared by Codex, 10 October 2026.

Scope: issues [#12](https://github.com/mikepmart/SPMS/issues/12) and
[#13](https://github.com/mikepmart/SPMS/issues/13), supporting QA-001/003/004/005/006/007,
SF-001 and PRIV-001. These smoke checks do not verify the complete product requirements.

## RED, before implementation

Executed 10 October 2026, 18:31 UTC, on Windows with CPython 3.14.8,
uv 0.13.0, Node 24.21.0 and npm 11.19.0. Locked backend and frontend installs
succeeded before this run. No health app, coverage-gate script or UI app existed.

| Command / working directory | Actual result | Expected missing behavior |
| --- | --- | --- |
| `uv run --locked pytest -q --tb=short --junitxml=../artifacts/phase1/red/backend.xml` / backend | Exit 1; 13 failed, 0 passed, collected successfully | Four bootstrap/health checks cannot import `spms.api.app`; nine coverage-gate cases cannot execute `tools/check_coverage.py`. |
| `npm.cmd test` / frontend | Exit 1; one failed suite, zero collected tests | Vite cannot resolve the not-yet-implemented `./App` component. This is a missing project module, not a missing tool/dependency. |

An earlier backend attempt failed collection because current Starlette requires
`httpx2` for its test client when deprecations are errors. That environment failure
was **not** accepted as RED evidence. The direct test dependency was corrected to
`httpx2==2.13.1`, locked and installed, then all 13 cases collected and failed for
the expected missing implementation. No warning suppression was added.

Full local command logs and backend JUnit are in ignored `artifacts/phase1/red/`.
The browser test was written before implementation but was not executed in RED:
there is no built UI or HTTP app to launch yet. Its actual GREEN result will be
recorded separately. This commit is an intentional TDD RED commit.

## GREEN and verification

Pending implementation and actual execution; no passing result is claimed here.
