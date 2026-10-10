# Phase 0 document review

Project Author: Michael Mart
Prepared by Codex for owner review, 10 October 2026.
Status: review complete; baseline approval PENDING; implementation NOT STARTED;
product verification NOT RUN; residual risk NOT ASSESSED.

## Repository and review evidence

The actual checkout is `C:\SPMS\SPMS`, inside workspace `C:\SPMS`. It initially
contained only `README.md`, with a clean working tree on `main` at
`6961ee2653f901781f74186f117fc9aae8ba9b28` (Initial commit).
`origin` is `https://github.com/mikepmart/SPMS.git`; GitHub read access and the
remote main SHA were verified. The source files were in sibling folders
`C:\SPMS\design\docs` and `C:\SPMS\design\regs`, rather than in the checkout.
They are now copied into this branch under the same `design` layout, without
changing their contents, versions, attribution, or notices. Repository visibility
is unchanged. No existing work was deleted.

All 13 sources were read in full. DOCX review extracted all paragraph and table
content in document order, plus headers, footers and ancillary text parts. The
nine DOCX files contain no tracked insertions/deletions and no embedded media.
XLSX review included every populated cell and comment on all three visible sheets:
Requirements RTM (79 × 12), Risk Control Register (23 × 7), and Read Me (8 × 2).
PDF review included every page: FDA 64, MDCG 46, GDPR 88; no page had empty text.
MDCG figure/table pages 5, 6, 10, 14, 15, 17 and 46 were also rendered and visually
inspected. This is a content review, not a layout audit or a regulatory approval.
The [manifest](source_manifest.json) records versions, sizes and SHA-256 hashes.
All 13 copied sources matched their originals.

The [inventory](requirements_inventory.md) preserves all 78 requirement texts and
RTM acceptance criteria. Automated comparison found identical SRS/RTM text for
78/78 requirements and identical separate acceptance criteria for 54/54 rows
where SRS supplies them. Twelve AR/DOC criteria are pending; twelve CL criteria
refer to planned test IDs rather than complete procedures. None is verified.

## Source-by-source assessment

| Source | Reviewed version | Role and principal result |
| --- | --- | --- |
| [SRS](../../design/docs/SPMS-SRS-001_v1.2.docx) | 1.2 | 66 original requirements plus CL-001–012. Controlled addendum defines precedence and CD-01–05, but formal approval remains pending. Exact boundaries, rejection classes, restart and sink failure rules drive implementation. |
| [AO](../../design/docs/SPMS-AO-001_v1.2.docx) | 1.2 | High-level Python/React, backend authority, ports/adapters, synthetic data and deployment boundary. Informal routes need alignment with detailed versioned contracts. |
| [SAD](../../design/docs/SPMS-SAD-001_v1.3.docx) | 1.3 controlling addendum; cover 1.2 | Component dependencies, runtime flows, persistence, trust boundaries, security/release architecture, ADR-001–005. Single process, no crash restoration, distinct stores and full snapshots are consistent across controlling addenda. |
| [SDD](../../design/docs/SPMS-SDD-001_v1.1.docx) | 1.1 controlling addendum; cover 1.0 | Domain invariants, validator, alarm transitions, services, schemas, REST/WS and failure handling. Earlier missing-tick ambiguity is resolved by CL-001; contract edge cases still require specification. |
| [STP](../../design/docs/SPMS-STP-001_v1.1.docx) | 1.1 controlling addendum; cover 1.0 | Unit, integration, security, browser, fault, coverage and release evidence. Clarification-case numbering diverges from RTM. Planned cases are not executed evidence. |
| [RTM](../../design/docs/SPMS-RTM-001_v1.1.xlsx) | 1.1 | All 78 requirements, 22 controls, original wording and NOT RUN statuses. Twelve pending criteria, 45 unlinked requirement rows, 22 placeholder control-test mappings and two blank primary risk links require review. |
| [SHA](../../design/docs/SPMS-SHA-001_v1.1.docx) | 1.1 controlling addendum; cover 1.0 | HAZ-01–10 and RC-SAF-001–010. Distinguishes misleading simulation from hypothetical clinical analogues; draft severity/likelihood matrix is not accepted risk. |
| [CRA](../../design/docs/SPMS-CRA-001_v1.1.docx) | 1.1 controlling addendum; cover 1.0 | CYB-01–12 and RC-CYB-001–012, STRIDE scenarios and lifecycle controls. Exploitability, owners, exact authentication and retention remain unspecified. |
| [SDP](../../design/docs/SPMS-SDP-001_v1.0.docx) | 1.0 | Sequential gates, TDD, controlled changes, verification and release responsibilities. Named reviewer/approver assignments remain pending. |
| [RMP](../../design/docs/SPMS-RMP-001_v1.0.docx) | 1.0 | Proposed S1–S3/L1–L3 educational risk evaluation and review/acceptance process. No risk has accepted residual disposition; cybersecurity exploitability needs separate rationale. |
| [FDA](../../design/regs/Premarket-Cybersecurity-Guidance-2026.pdf) | 3 February 2026; 64 PDF pages | Secure development lifecycle, security risk management, threat models, exact SBOM, architecture views, verification, transparency, updates and conditional statutory provisions. Engineering reference; no SPMS compliance conclusion. |
| [MDCG](../../design/regs/mdcg_2019_16_cybersecurity_en.pdf) | December 2019 original; 46 pages | Security/safety interaction, defense in depth, eight secure lifecycle practices, minimum IT environment, verification, documentation and lifecycle maintenance. Supplied file is not the July 2020 Rev.1. |
| [GDPR](../../design/regs/CELEX_32016R0679_EN_TXT.pdf) | Regulation (EU) 2016/679, OJ L119, 4 May 2016; 88 pages | Material/territorial scope, personal data, principles, rights, accountability, security and transfers. Applicability requires actual field/deployment/jurisdiction assessment, including operator metadata. |

## Conflicts and proposed dispositions

Finding labels below are review labels, not new requirement or control IDs. All
dispositions are proposals for Michael Mart's review; no supplied file was edited.

| Finding | Source evidence / problem | Proposed disposition and gate |
| --- | --- | --- |
| F-01 | SAD cover says 1.2, SDD/STP/SHA/CRA covers say 1.0; controlling addenda identify later versions. References still cite SRS 1.1, SAD 1.2, AO 1.1 and an old RTM filename. | Use named files and their explicit addendum versions for this review. Owner approves synchronized controlled revisions, version tables and references before baseline acceptance/release. Do not silently edit originals. |
| F-02 | FR-002 says each accepted reading within one second of receipt; CL-003 limits healthy transport and CL-009 specifies 95% within one second of backend acceptance. SAD asks for methodology. | Apply controlling clarification for planning, preserve FR wording, explicitly approve the 95% target and clock/measurement protocol before Phase 7–8 timing acceptance (Q-06). |
| F-03 | RTM links CL-n to TC-CL-n; STP cases 003 onward test different requirements. TC-CL-012 has no detailed STP procedure. SHA/CRA also retain legacy T-* and shorter TC-SEC-* IDs. | Approve the scenario-based crosswalk in the inventory, then revise STP/RTM/SHA/CRA together. Add missing procedures; do not equate identifiers by number (Q-03). |
| F-04 | Risk Control Register C13 (CYB-02) and C20 (CYB-09) are blank. Other CRA/SHA links are incomplete; all 22 control-test entries are placeholders; 45 requirement rows are unlinked. | Review supplemental mappings below, explicitly justify non-applicability where appropriate, and assign tests/owners. No omitted link is automatically accepted (Q-03/Q-10). |
| F-05 | AR-001–006 and DOC-001–006 lack separate SRS acceptance criteria; RTM says “Acceptance criteria to be approved.” | Approve measurable review/install/test/document criteria before claiming these requirements verified. Proposed phase gates are not substituted source criteria (Q-03). |
| F-06 | SDD §5 says scheduled gaps unresolved; CL-001 explicitly resets activation/recovery. Earlier audit-outage warning-only language differs from CL-006 fail-closed policy. Earlier SDD pseudocode increments revision for every command. | Controlled addenda govern: gaps reset pending counts; durable audit failure denies accountable network commands before mutation; rejected commands preserve revision/state. Preserve active alarms and running automatic evaluation. |
| F-07 | CL-012 asserts all earlier choices resolved, yet authentication lifecycle, retention durations, limits/backpressure, audit commit/outcome protocol, update tooling and approvers remain unspecified. | Treat CL-012 as change-authority policy; record genuinely unresolved details in open questions. Do not infer implementation permission or complete design closure. |
| F-08 | SDD state labels use ACTIVE_UNACK/ACTIVE_ACK in earlier table and longer names in the addendum; AO routes are unversioned while SAD/SDD use /api/v1 and /ws/v1. | Ratify one enum/schema and detailed versioned API before Phase 6; distinguish descriptive labels from wire values (Q-05). |
| F-09 | SHA describes RC-SAF-006 as “monotonic timestamp validation,” while SDD requires strictly increasing UTC measured_at per kind and monotonic elapsed freshness. | Keep separate semantics: ordering of measurement UTC timestamps versus monotonic elapsed clock. Clarify terminology in controlled revision; test both. |
| F-10 | CRA describes episode-bound idempotency/replay checks; STP expects duplicate acknowledgments rejected; detailed transition permits acknowledgment only from unacknowledged active state. HTTP response and audit behavior unspecified. | Preserve no second mutation/event for duplicates. Approve rejection versus explicit idempotent success, exact status/error and audit behavior before API implementation (Q-05). |
| F-11 | Actual source MDCG file is December 2019, while the official guidance listing has July 2020 Rev.1. Its NIS and transition-date context is historical. | Keep supplied baseline unchanged; ask whether to add Rev.1 as a separately versioned reference and assess impact (Q-11). Do not portray older legal context as a current binding rule. |
| F-12 | One process and volatile state are specified, but overload policy, missed-tick coalescing, blocking SQLite isolation, process-restart detection, and event ordering under UTC rollback need concrete contracts. | Define bounded limits and failure behavior before application/infrastructure work; no unbounded queues or SQLite calls blocking asynchronous ingress (Q-04/Q-07). |
| F-13 | Validator handles fields individually, but simultaneous invalid value and old timestamp, partial HR/SpO₂ sets, wrong-session input routing and rejection-event destination are not fully specified. | Specify rejection precedence and batch acceptance so CL-002 resets/preservation are deterministic. Preserve source rules; obtain clarification before affected Phase 2–4 tests (Q-04). |

## Risk review and proposed supplemental traceability

All HAZ-01–10 and CYB-01–12 remain OPEN / NOT VERIFIED, residual risk NOT ASSESSED,
approval PENDING. Existing High/Medium labels are engineering triage, not
probabilistic clinical risk measurements. The RMP's severity/likelihood matrix is
proposed, and owner/reviewer roles and acceptance criteria require approval.
Security assessments should document attacker preconditions and exploitability
separately, and cross-reference safety effects and risks introduced by controls.

| Existing control | Risk / control focus | Supplemental source links proposed for RTM review | Planned effectiveness evidence |
| --- | --- | --- | --- |
| RC-SAF-001 | HAZ-01 missed or incorrect low-oxygen alarm | SF-006; retain FR-006/007/008, CL-001/002 | Every activation/recovery boundary, gaps and rejection class with deterministic state transition tests |
| RC-SAF-002 | HAZ-02 disconnect clears active alarm | FR-012 alongside SF-004 | Disconnect/reconnect with acknowledged and unacknowledged active episodes |
| RC-SAF-003 | HAZ-03 invalid/stale display | FR-015; SF-003 alongside existing links | Invalid preservation, exact 5-second boundary, UTC adjustments, visible status and timing |
| RC-SAF-004 | HAZ-04 acknowledgment clears/carries over | Retain FR-009/010, SEC-014 | Current episode only; no clear; new episode needs fresh acknowledgment |
| RC-SAF-005 | HAZ-05 storage failure interrupts monitoring | Retain SF-005, CL-005 | Faulted writes while activation/recovery continue; incomplete history remains after recovery |
| RC-SAF-006 | HAZ-06 replay changes counters | Retain FR-015, CL-002 | Duplicate/older UTC timestamps preserve accepted values and both counters |
| RC-SAF-007 | HAZ-07 obsolete browser state | Retain SEC-016, CL-003/004/008 | Transport loss, restart and older snapshot rejection plus authoritative resync |
| RC-SAF-008 | HAZ-08 session leakage | Retain FR-016 | New session resets runtime state; history queries remain scoped |
| RC-SAF-009 | HAZ-09 unauthorized mutation | SEC-001; SEC-014 alongside SEC-002 | Role/session/episode denial preserves state; accepted network commands have durable audit |
| RC-SAF-010 | HAZ-10 clinical misuse | Retain SF-001 | Persistent exact warning on every monitoring screen, user guide and release review |
| RC-CYB-001 | CYB-01 spoofed identity | Retain SEC-001/002, CL-007 | Unauthenticated, role, expiry/revocation and cross-session REST/WS tests |
| RC-CYB-002 | CYB-02 tampered inputs | SEC-004; SEC-011 (CRA explicit; RTM blank) | Typed/bounded malformed inputs and unauthorized injection cannot change alarm |
| RC-CYB-003 | CYB-03 repudiation | SEC-014; CL-006 alongside SEC-005 | Durable audit acceptance and defined failed-command outcomes |
| RC-CYB-004 | CYB-04 unauthorized history | SEC-002; SEC-006; PRIV-004/005/006 alongside CL-010 | Session authorization, minimal fields, access/retention/deletion review |
| RC-CYB-005 | CYB-05 denial of service | SEC-004; SEC-011 alongside SEC-016 | Bounded requests/queues; overload and transport uncertainty are visible; domain behavior preserved |
| RC-CYB-006 | CYB-06 elevated privileges | SEC-013 alongside SEC-002, CL-007 | Observer denial, secure default bind/config and per-session operator checks |
| RC-CYB-007 | CYB-07 vulnerable supply chain | SEC-012 alongside SEC-007/008, CL-011 | Locked dependency scan, exact SBOM, triaged findings and documented remediation |
| RC-CYB-008 | CYB-08 plaintext exposure | Retain SEC-003 | HTTPS/WSS enforcement in network mode; local exception is explicit and loopback only |
| RC-CYB-009 | CYB-09 exposed secrets | SEC-005; SEC-006; PRIV-005 (CRA explicit/related; RTM blank) | Secret scans and audit/log redaction, file permissions and no committed credentials |
| RC-CYB-010 | CYB-10 replayed/stale acknowledgment | Retain SEC-014 | Wrong episode/session and duplicate request cannot mutate state again |
| RC-CYB-011 | CYB-11 malicious update | Retain SEC-015, CL-011 | Integrity verification rejects altered artifact; rollback exercise records exact revisions |
| RC-CYB-012 | CYB-12 audit unavailable | CL-006 alongside SEC-005 | Fail closed before accountable network command mutation; ongoing ticks and alarms continue |

These are mapping proposals, not new controls, verified mitigations, or acceptance
of residual risk. Exact source mappings are preserved separately in the inventory.

## Regulatory reference interpretation

The supplied FDA guidance's §§IV–VII and appendices motivate a secure product
development lifecycle, threat modeling, separate security/safety reasoning,
architecture and trust-boundary documentation, exact machine-readable SBOM,
boundary/negative security testing, vulnerability handling and update integrity.
Premarket submission and section 524B obligations require an actual applicability
determination; this educational project does not claim one. The current
[FDA guidance page](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket)
confirms a February 2026 guidance superseding June 2025. This metadata check does
not establish SPMS conformity.

The supplied MDCG §§2–6 and annexes connect safety and security risk management,
defense in depth, intended environment, secure lifecycle practices, verification,
user documentation, vulnerability maintenance and residual-risk review. They are
guidance, not a substitute for a legal applicability assessment. The official
[MDCG listing](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)
and [Rev.1 PDF](https://health.ec.europa.eu/document/download/b23b362f-8a56-434c-922a-5b3ca4d0a7a1_en?filename=md_cybersecurity_en.pdf)
identify July 2020 Rev.1. Only its identity/version was checked; a full Rev.1
content/impact comparison is outside this supplied-baseline review.

The supplied GDPR Articles 2–4 set scope and definitions; Articles 5–6, 12–22,
24–32 and 44–49 inform principles, lawful processing, transparency/rights,
accountability, safeguards and transfers when applicable. Article 35 assessment
and incident obligations need evaluation against actual processing. The
field inventory must include account references, IP addresses and logs as well
as synthetic measurements; synthetic physiology alone cannot decide applicability.
PRIV-003/006/007 and CL-010 require purposes, access, retention/deletion, backups,
jurisdiction and a documented conclusion. No GDPR non-applicability or compliance
claim is made. The [official EUR-Lex entry](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)
was challenged by anti-bot verification during the supplementary web check; the
complete supplied OJ PDF was read and remains the review source. It is not asserted
to be a current consolidated text.

Any real patient data, clinical purpose, external deployment or changed data scope
requires change control and a fresh applicability/risk/privacy review. IEC 62304,
ISO 14971 and hypothetical FDA Class II context are engineering references in
the drafts, not SPMS classifications, certifications or evidence of conformity.

## Disposition

Phase 0's content-review, inventory, conflict identification and planning criteria
are satisfied. [Open questions](open_questions.md) identify the decisions needed
at each later gate. Approving progression to repository setup does not by itself
approve every baseline correction, accept risk, authorize a merge, or permit release.
