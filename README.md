# Simulated Patient Monitoring System (SPMS)

Project Author: Michael Mart. Scaffold and documentation prepared by Codex.

**Simulation only — not for clinical use.**

SPMS is a proposed educational software engineering demonstration using synthetic
heart rate and oxygen saturation data. It is not intended for patient monitoring,
diagnosis, treatment, or clinical decisions. No FDA clearance, CE marking,
regulatory conformity, or clinical validation is claimed.

Phase 1 provides locked development environments, a stopped React shell, a
FastAPI health endpoint, smoke tests and automated verification. Monitoring,
alarms, accounts and persistence are not implemented yet. Each later phase
requires Michael Mart's approval. No project license has been selected.

## Repository

- `backend/src/spms/`: API adapter and separate domain/application/infrastructure
  namespaces. Only the API bootstrap currently has behavior.
- `backend/tests/`: unit, integration, negative configuration and tooling tests.
- `frontend/src/`: React shell and unit test; `frontend/e2e/`: real HTTP browser smoke.
- `design/docs/` and `design/regs/`: unchanged copies of all 13 supplied sources.
- `.github/workflows/verify.yml`: quality, tests, security scans and SBOM artifacts.

## Prerequisites

Use CPython **3.14.8**, uv **0.13.0**, Node **24.21.0**, npm **11.19.0** and Git.
Versions are pinned in `.python-version`, `.uv-version`, `.node-version` and
`frontend/package.json`. The selected Node distribution includes the required
npm. Install Node from the [official downloads](https://nodejs.org/en/download)
and uv using its [official instructions](https://docs.astral.sh/uv/getting-started/installation/).
`uv python install 3.14.8` can supply Python when it is not installed.

Run commands from the repository root unless a `cd` is shown. On Windows
PowerShell use `npm.cmd` and `npx.cmd` so no activation script or execution-policy
change is necessary. On Linux/macOS use `npm` and `npx`.
Verify `uv --version`, `node --version` and `npm.cmd --version` before installing.
The first install, browser download and advisory scans need network access.

## Locked installation

```powershell
uv sync --locked --project backend
cd frontend
npm.cmd ci
npm.cmd exec -- playwright install chromium
cd ..
```

`uv.lock` and `package-lock.json` record exact dependencies. `npm ci` checks the
lock against the manifest; `.npmrc` enforces engine versions and disables
dependency lifecycle scripts. The browser is installed explicitly. On Linux CI
use `npx --no-install playwright install --with-deps chromium` for system libraries.
Do not use `npm audit fix` or an unlocked install as a verification step.

## Run locally

Start the health bootstrap in one terminal:

```powershell
uv run --locked --project backend uvicorn spms.api.app:create_app --factory --host 127.0.0.1 --port 8000
```

Start the UI in a second terminal:

```powershell
cd frontend
npm.cmd run dev
```

Open <http://127.0.0.1:5173>. The page visibly identifies a stopped synthetic
simulation. <http://127.0.0.1:8000/health> returns
`{"status":"ok","simulation_only":true}`. It indicates process availability only.
Both development servers bind to loopback by default. Use one backend process;
network deployment and monitoring APIs belong to later approved phases.

## Verify

From the repository root:

```powershell
cd backend
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked mypy
uv run --locked pytest -q --cov=spms --cov-branch --cov-report=term-missing --cov-report=json:../artifacts/backend/coverage.json --cov-report=xml:../artifacts/backend/coverage.xml --junitxml=../artifacts/backend/junit.xml
uv run --locked python tools/check_coverage.py ../artifacts/backend/coverage.json
cd ../frontend
npm.cmd run format:check
npm.cmd run lint
npm.cmd run typecheck
npm.cmd run test:coverage
npm.cmd run build
npm.cmd run test:e2e
cd ..
```

The Python gate uses exact statement counts across all `spms` application source
and requires at least 90%. Branch coverage is reported separately; an application
with no branches reports it as not applicable. The coverage utility is tested
separately and is not application code. Frontend coverage includes `main.tsx`;
browser results are not combined with jsdom coverage. Ports 8000 and 4173 must be
free for Playwright, which launches and stops its own backend and built UI.

## Security and supply-chain evidence

The [workflow](.github/workflows/verify.yml) contains executable commands for
hashed Python dependency export/audit, npm audit, Bandit static analysis, full Git
history secret scanning and CycloneDX SBOM generation. Direct dependencies and
CI actions are pinned. Gitleaks is pinned in `.gitleaks-version`; its official
archive checksum is verified before execution. No scan suppressions are configured.

Reports are written under ignored `artifacts/` and retained by CI for 30 days,
named with the tested commit SHA. Preserve relevant artifacts for a release
record before retention expires. Scans query current advisories; a clean result
is scoped to that run and does not establish product security or regulatory
conformity. SBOMs include development tooling as well as runtime packages.

## Review and phase gates

Use an issue and coherent branch for substantial work. Write tests, record an
expected missing-behavior RED result and commit tests before implementation.
Implement, run relevant checks, update traceability and open a PR using the
template. Never merge failing checks or merge without owner approval.

- [Phase 1 completion/evidence report](docs/implementation/phase_1_report.md)
- [Phase 1 RED/GREEN evidence](docs/implementation/phase_1_tdd.md)
- [Working traceability](docs/implementation/traceability.md)
- [Approval record](docs/implementation/approvals.md)

- [Phase 0 completion report](docs/implementation/phase_0_report.md)
- [Requirements inventory](docs/implementation/requirements_inventory.md)
- [Document review and conflicts](docs/implementation/document_review.md)
- [Implementation plan](docs/implementation/implementation_plan.md)
- [Open questions and approval gates](docs/implementation/open_questions.md)
- [Architecture decisions](docs/implementation/architecture_decisions.md)
- [Original source documents and hashes](docs/implementation/source_manifest.json)

The original source documents are unchanged copies of the supplied files. Their
engineering requirements and risk controls remain proposed. Project attribution
does not imply personal authorship of generated work. Phase progression,
baseline approval, risk acceptance, PR merge and release are separate decisions.
