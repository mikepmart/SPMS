# Phase 0 requirements inventory

Project Author: Michael Mart
Prepared by Codex for Michael Mart's review. Review date: 10 October 2026.
Status: PROPOSED / NOT VERIFIED. No product requirement is marked implemented or verified.

## Source and scope

The [SRS v1.2](../../design/docs/SPMS-SRS-001_v1.2.docx) and all three worksheets of the [RTM v1.1](../../design/docs/SPMS-RTM-001_v1.1.xlsx) were read. Original files are preserved byte-for-byte; see [source manifest](source_manifest.json).

There are **78 unique requirement IDs**: FR 16, SF 6, AR 6, QA 8, DOC 6, SEC 16, PRIV 8, CL 12. All 78 IDs and requirement texts match between SRS and RTM. All 54 separately specified SRS acceptance criteria match RTM. Twelve AR/DOC rows lack separate SRS acceptance criteria; their RTM text is explicitly pending approval. Twelve CL paragraphs include normative verification expectations in their text; RTM uses generic test references, which are not adequate procedures.

The SRS controlled addendum takes precedence over conflicting earlier text **within the proposed document**. Formal baseline approval is still pending. Original wording below is preserved, including earlier wording clarified by CL requirements. No new requirement or risk-control IDs are created by this review.

Phases and reconciliation notes are planning proposals. Source risk links and test IDs below are copied unchanged, including incomplete mappings. They must be read with [document review](document_review.md), [open questions](open_questions.md), and the test-ID crosswalk at the end of this inventory. No test ID is evidence of execution.

## Exact requirement records

### FR-001

Source: SRS table 1, row 2; RTM `Requirements RTM!A2:L2`. Proposed phases: 5, 8.

**Requirement (verbatim):** The application shall generate synthetic heart rate and oxygen saturation readings once per second during an active simulation.

**RTM acceptance criteria (verbatim):** A controlled 10-second simulation produces 10 scheduled reading sets.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-FR-001. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-002

Source: SRS table 1, row 3; RTM `Requirements RTM!A3:L3`. Proposed phases: 7, 8.

**Requirement (verbatim):** The frontend shall display each accepted reading within one second of receipt.

**RTM acceptance criteria (verbatim):** An automated integration test verifies the displayed value and elapsed time.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-FR-002. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-003

Source: SRS table 1, row 4; RTM `Requirements RTM!A4:L4`. Proposed phases: 7, 8.

**Requirement (verbatim):** Each displayed measurement shall include its name, value, unit, and measurement timestamp.

**RTM acceptance criteria (verbatim):** Heart rate displays in bpm; oxygen saturation displays in percent; timestamps match accepted readings.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-FR-003. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-004

Source: SRS table 1, row 5; RTM `Requirements RTM!A5:L5`. Proposed phases: 2, 4, 6, 7, 8.

**Requirement (verbatim):** The application shall accept finite numeric heart rate values from 0–300 bpm and oxygen saturation values from 0–100%, inclusive. These ranges are simulation input limits.

**RTM acceptance criteria (verbatim):** Boundary values are accepted; out-of-range, missing, nonnumeric, and nonfinite values are rejected.

Source risks: HAZ-03. Source controls: RC-SAF-003. Source planned verification: TC-FR-004. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-005

Source: SRS table 1, row 6; RTM `Requirements RTM!A6:L6`. Proposed phases: 2, 4, 6, 7, 8.

**Requirement (verbatim):** Invalid readings shall not replace the last valid measurement. The frontend shall indicate invalid input, and the application shall record the rejection.

**RTM acceptance criteria (verbatim):** Injecting an invalid reading preserves the last valid value and creates a rejection event.

Source risks: HAZ-03. Source controls: RC-SAF-003. Source planned verification: TC-FR-005. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-006

Source: SRS table 1, row 7; RTM `Requirements RTM!A7:L7`. Proposed phases: 3, 4, 6, 7, 8.

**Requirement (verbatim):** The application shall activate a low-oxygen alarm after three consecutive valid readings below 92%. This threshold is a demonstration setting.

**RTM acceptance criteria (verbatim):** Two readings below 92% do not activate the alarm; the third activates it. A value of exactly 92% is not low.

Source risks: HAZ-01. Source controls: RC-SAF-001. Source planned verification: TC-FR-006. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-007

Source: SRS table 1, row 8; RTM `Requirements RTM!A8:L8`. Proposed phases: 3, 4, 6, 7, 8.

**Requirement (verbatim):** A valid oxygen reading at or above 92%, an invalid oxygen reading, or a sensor disconnect shall reset the pending low-oxygen count.

**RTM acceptance criteria (verbatim):** Each reset condition requires three new consecutive low readings before activation.

Source risks: HAZ-01. Source controls: RC-SAF-001. Source planned verification: TC-FR-007. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-008

Source: SRS table 1, row 9; RTM `Requirements RTM!A9:L9`. Proposed phases: 3, 4, 6, 7, 8.

**Requirement (verbatim):** An active low-oxygen alarm shall clear after three consecutive valid oxygen readings at or above 92%. Invalid readings shall reset the recovery count.

**RTM acceptance criteria (verbatim):** Two qualifying recovery readings leave the alarm active; the third clears it.

Source risks: HAZ-01. Source controls: RC-SAF-001. Source planned verification: TC-FR-008. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-009

Source: SRS table 2, row 2; RTM `Requirements RTM!A10:L10`. Proposed phases: 3, 4, 6, 7, 8.

**Requirement (verbatim):** The user shall be able to acknowledge an active alarm. Acknowledgment shall change its status without clearing the underlying condition.

**RTM acceptance criteria (verbatim):** After acknowledgment, the alarm remains visible as active and acknowledged until its clearance criteria are met.

Source risks: HAZ-04. Source controls: RC-SAF-004. Source planned verification: TC-FR-009. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-010

Source: SRS table 2, row 3; RTM `Requirements RTM!A11:L11`. Proposed phases: 3, 4, 6, 7, 8.

**Requirement (verbatim):** A newly activated alarm following clearance shall require a new acknowledgment.

**RTM acceptance criteria (verbatim):** A previous acknowledgment does not carry over to a later alarm episode.

Source risks: HAZ-04. Source controls: RC-SAF-004. Source planned verification: TC-FR-010. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-011

Source: SRS table 2, row 4; RTM `Requirements RTM!A12:L12`. Proposed phases: 3, 4, 5, 7, 8.

**Requirement (verbatim):** A measurement shall be marked stale when more than five seconds have elapsed since receipt of its last valid reading.

**RTM acceptance criteria (verbatim):** At exactly five seconds it remains current; after five seconds it is stale. Before the first valid reading, it displays “No data.”

Source risks: HAZ-03. Source controls: RC-SAF-003. Source planned verification: TC-FR-011. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-012

Source: SRS table 2, row 5; RTM `Requirements RTM!A13:L13`. Proposed phases: 3, 4, 5, 7, 8.

**Requirement (verbatim):** The frontend shall identify a simulated sensor disconnect and shall preserve the last valid readings with stale indicators when applicable.

**RTM acceptance criteria (verbatim):** Disconnecting the sensor displays its disconnected state; measurements become stale according to FR-011.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-FR-012. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-013

Source: SRS table 2, row 6; RTM `Requirements RTM!A14:L14`. Proposed phases: 2, 4, 5, 6, 7, 8.

**Requirement (verbatim):** The application shall record session start/stop, alarm activation, acknowledgment, clearance, invalid input, and sensor disconnect/reconnect events.

**RTM acceptance criteria (verbatim):** Each event contains a session identifier, event type, UTC timestamp, and relevant details.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-FR-013. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-014

Source: SRS table 2, row 7; RTM `Requirements RTM!A15:L15`. Proposed phases: 2, 4, 5, 6, 7, 8.

**Requirement (verbatim):** The frontend shall display session events in chronological order.

**RTM acceptance criteria (verbatim):** A known event sequence appears in the expected order, including events with identical timestamps.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-FR-014. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-015

Source: SRS table 2, row 8; RTM `Requirements RTM!A16:L16`. Proposed phases: 2, 4, 6, 7, 8.

**Requirement (verbatim):** The application shall reject readings whose measurement timestamp is equal to or earlier than the last accepted timestamp for that measurement.

**RTM acceptance criteria (verbatim):** Duplicate and older readings do not update displayed values or alarm counters and produce rejection events.

Source risks: HAZ-06. Source controls: RC-SAF-006. Source planned verification: TC-FR-015. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### FR-016

Source: SRS table 2, row 9; RTM `Requirements RTM!A17:L17`. Proposed phases: 2, 4, 5, 6, 7, 8.

**Requirement (verbatim):** Starting a new session shall reset displayed readings, alarm states, and pending counters while retaining prior session records.

**RTM acceptance criteria (verbatim):** A new session begins with “No data” and no active alarms; previous events remain stored under their original session identifier.

Source risks: HAZ-08. Source controls: RC-SAF-008. Source planned verification: TC-FR-016. Source component: Domain / Application / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SF-001

Source: SRS table 3, row 2; RTM `Requirements RTM!A18:L18`. Proposed phases: 7, 8, 9.

**Requirement (verbatim):** Every monitoring screen shall display “Simulation only — not for clinical use.”

**RTM acceptance criteria (verbatim):** Automated browser tests verify the notice is visible.

Source risks: HAZ-10. Source controls: RC-SAF-010. Source planned verification: TC-SF-001. Source component: Domain / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SF-002

Source: SRS table 3, row 3; RTM `Requirements RTM!A19:L19`. Proposed phases: 7, 8, 9.

**Requirement (verbatim):** Alarm and sensor states shall be communicated through text as well as color.

**RTM acceptance criteria (verbatim):** Each state has a readable label; no state depends solely on color.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SF-002. Source component: Domain / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SF-003

Source: SRS table 3, row 4; RTM `Requirements RTM!A20:L20`. Proposed phases: 7, 8, 9.

**Requirement (verbatim):** Missing, invalid, or stale data shall not be presented as a normal current measurement.

**RTM acceptance criteria (verbatim):** Fault scenarios display the corresponding status alongside any retained value.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SF-003. Source component: Domain / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SF-004

Source: SRS table 3, row 5; RTM `Requirements RTM!A21:L21`. Proposed phases: 3, 4, 5, 7, 8.

**Requirement (verbatim):** Sensor disconnection shall not clear an existing physiological alarm.

**RTM acceptance criteria (verbatim):** An active low-oxygen alarm remains active during disconnection.

Source risks: HAZ-02. Source controls: RC-SAF-002. Source planned verification: TC-SF-004. Source component: Domain / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SF-005

Source: SRS table 3, row 6; RTM `Requirements RTM!A22:L22`. Proposed phases: 4, 5, 7, 8.

**Requirement (verbatim):** If event storage fails, the application shall display an event-recording failure indicator and continue evaluating incoming readings.

**RTM acceptance criteria (verbatim):** An injected storage failure produces a visible indicator while alarm evaluation continues. The indicator remains until a successful subsequent write.

Source risks: HAZ-05. Source controls: RC-SAF-005. Source planned verification: TC-SF-005. Source component: Domain / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SF-006

Source: SRS table 3, row 7; RTM `Requirements RTM!A23:L23`. Proposed phases: 2–9 (each relevant control).

**Requirement (verbatim):** Automated tests shall verify each identified software risk control.

**RTM acceptance criteria (verbatim):** Every risk-control entry links to at least one passing test.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SF-006. Source component: Domain / UI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### AR-001

Source: SRS table 4, row 2; RTM `Requirements RTM!A24:L24`. Proposed phases: 1–9 (architecture/process gates).

**Requirement (verbatim):** The monitoring rules and alarm state transitions shall be implemented in Python independently of the frontend, network interface, and storage implementation.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-AR-001. Source component: Architecture / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### AR-002

Source: SRS table 4, row 3; RTM `Requirements RTM!A25:L25`. Proposed phases: 1–9 (architecture/process gates).

**Requirement (verbatim):** Sensor input, time, and event storage shall be replaceable with controlled test implementations.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-AR-002. Source component: Architecture / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### AR-003

Source: SRS table 4, row 4; RTM `Requirements RTM!A26:L26`. Proposed phases: 1–9 (architecture/process gates).

**Requirement (verbatim):** The frontend shall display application state; authoritative alarm decisions shall reside in the Python application.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-AR-003. Source component: Architecture / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### AR-004

Source: SRS table 4, row 5; RTM `Requirements RTM!A27:L27`. Proposed phases: 1–9 (architecture/process gates).

**Requirement (verbatim):** The codebase shall pass its configured lint and formatting checks before a change is accepted.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-AR-004. Source component: Architecture / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### AR-005

Source: SRS table 4, row 6; RTM `Requirements RTM!A28:L28`. Proposed phases: 1–9 (architecture/process gates).

**Requirement (verbatim):** Code review shall assess duplicated logic, excessive complexity, hidden mutable state, unclear naming, and overly broad exception handling.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-AR-005. Source component: Architecture / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### AR-006

Source: SRS table 4, row 7; RTM `Requirements RTM!A29:L29`. Proposed phases: 1–9 (architecture/process gates).

**Requirement (verbatim):** Dependencies and their resolved versions shall be recorded to support reproducible installation and testing.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-AR-006. Source component: Architecture / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### QA-001

Source: SRS table 5, row 2; RTM `Requirements RTM!A30:L30`. Proposed phases: 1–9 (verification process).

**Requirement (verbatim):** Functional changes shall follow a test-driven development workflow.

**RTM acceptance criteria (verbatim):** Development history demonstrates a failing test, implementation, and passing test for representative features.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-QA-001. Source component: CI / Tests.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### QA-002

Source: SRS table 5, row 3; RTM `Requirements RTM!A31:L31`. Proposed phases: 1–9 (verification process).

**Requirement (verbatim):** Automated unit tests shall cover validation, alarm activation and recovery boundaries, acknowledgment, timestamp ordering, and stale-data detection.

**RTM acceptance criteria (verbatim):** Required scenarios pass using controlled input and time.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-QA-002. Source component: CI / Tests.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### QA-003

Source: SRS table 5, row 4; RTM `Requirements RTM!A32:L32`. Proposed phases: 1–9 (verification process).

**Requirement (verbatim):** Automated integration tests shall verify sensor input, application state, and event-storage interactions.

**RTM acceptance criteria (verbatim):** Tests verify normal operation and injected failures.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-QA-003. Source component: CI / Tests.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### QA-004

Source: SRS table 5, row 5; RTM `Requirements RTM!A33:L33`. Proposed phases: 1–9 (verification process).

**Requirement (verbatim):** Automated browser tests shall verify monitoring, alarm acknowledgment, sensor failure, recovery, and event-history workflows.

**RTM acceptance criteria (verbatim):** All required workflows pass.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-QA-004. Source component: CI / Tests.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### QA-005

Source: SRS table 5, row 6; RTM `Requirements RTM!A34:L34`. Proposed phases: 1–9 (verification process).

**Requirement (verbatim):** Automated tests shall achieve at least 90% statement coverage across maintained Python application code.

**RTM acceptance criteria (verbatim):** The coverage report meets the threshold. Test code and generated files are excluded; other exclusions require documented justification.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-QA-005. Source component: CI / Tests.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### QA-006

Source: SRS table 5, row 7; RTM `Requirements RTM!A35:L35`. Proposed phases: 1–9 (verification process).

**Requirement (verbatim):** Branch coverage shall be measured and reported separately.

**RTM acceptance criteria (verbatim):** Each automated verification run produces a branch-coverage report.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-QA-006. Source component: CI / Tests.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### QA-007

Source: SRS table 5, row 8; RTM `Requirements RTM!A36:L36`. Proposed phases: 1–9 (verification process).

**Requirement (verbatim):** Each proposed code change shall trigger automated tests, lint checks, formatting checks, and coverage measurement.

**RTM acceptance criteria (verbatim):** Any failed required check prevents the change from being accepted.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-QA-007. Source component: CI / Tests.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### QA-008

Source: SRS table 5, row 9; RTM `Requirements RTM!A37:L37`. Proposed phases: 1–9 (verification process).

**Requirement (verbatim):** Automated verification shall retain test results and coverage reports.

**RTM acceptance criteria (verbatim):** Reports identify the tested source revision and run outcome.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-QA-008. Source component: CI / Tests.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### DOC-001

Source: SRS table 6, row 2; RTM `Requirements RTM!A38:L38`. Proposed phases: 0–9 (controlled documentation).

**Requirement (verbatim):** The project shall maintain version-controlled requirements, an architecture description, a hazard analysis, and a test plan.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-DOC-001. Source component: Engineering process.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### DOC-002

Source: SRS table 6, row 3; RTM `Requirements RTM!A39:L39`. Proposed phases: 0–9 (controlled documentation).

**Requirement (verbatim):** A traceability matrix shall connect each functional and safety requirement to its implementation and verification tests.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-DOC-002. Source component: Engineering process.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### DOC-003

Source: SRS table 6, row 4; RTM `Requirements RTM!A40:L40`. Proposed phases: 0–9 (controlled documentation).

**Requirement (verbatim):** The hazard analysis shall identify hazards, foreseeable causes, software controls, and control-verification tests.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-DOC-003. Source component: Engineering process.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### DOC-004

Source: SRS table 6, row 5; RTM `Requirements RTM!A41:L41`. Proposed phases: 0–9 (controlled documentation).

**Requirement (verbatim):** A validation report shall document whether representative users can complete the intended simulated workflows.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-DOC-004. Source component: Engineering process.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### DOC-005

Source: SRS table 6, row 6; RTM `Requirements RTM!A42:L42`. Proposed phases: 0–9 (controlled documentation).

**Requirement (verbatim):** Each release shall identify its source revision, verification results, known defects, and limitations.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-DOC-005. Source component: Engineering process.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### DOC-006

Source: SRS table 6, row 7; RTM `Requirements RTM!A43:L43`. Proposed phases: 0–9 (controlled documentation).

**Requirement (verbatim):** A regulatory-context document shall explain how the project’s artifacts relate to relevant FDA software guidance and distinguish educational evidence from a regulatory submission.

**RTM acceptance criteria (verbatim):** Acceptance criteria to be approved

Separate SRS acceptance criteria: **not specified**. Approval and measurable criteria are required before verification; see Q-03.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-DOC-006. Source component: Engineering process.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-001

Source: SRS table 7, row 2; RTM `Requirements RTM!A44:L44`. Proposed phases: 6, 8, 9.

**Requirement (verbatim):** Protected operations shall require authenticated operator identity in network-accessible mode.

**RTM acceptance criteria (verbatim):** Unauthenticated start/stop, acknowledge, disconnect and event-history requests are rejected; tests confirm no state change.

Source risks: CYB-01. Source controls: RC-CYB-001. Source planned verification: TC-SEC-001. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-002

Source: SRS table 7, row 3; RTM `Requirements RTM!A45:L45`. Proposed phases: 6, 8, 9.

**Requirement (verbatim):** Backend shall authorize each state-changing operation and session subscription.

**RTM acceptance criteria (verbatim):** Observer requests to modify session or alarm state return 403; operator requests succeed; cross-session access denied.

Source risks: CYB-01; CYB-06; HAZ-09. Source controls: RC-CYB-001; RC-CYB-006; RC-SAF-009. Source planned verification: TC-SEC-002. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-003

Source: SRS table 7, row 4; RTM `Requirements RTM!A46:L46`. Proposed phases: 6, 8, 9.

**Requirement (verbatim):** Network deployments shall use HTTPS and WSS; local-only mode shall bind to loopback.

**RTM acceptance criteria (verbatim):** Configuration tests reject insecure network binding and plaintext remote transport.

Source risks: CYB-08. Source controls: RC-CYB-008. Source planned verification: TC-SEC-003. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-004

Source: SRS table 7, row 5; RTM `Requirements RTM!A47:L47`. Proposed phases: 6, 8, 9.

**Requirement (verbatim):** All API and WebSocket inputs shall be schema-validated with bounded sizes and typed fields.

**RTM acceptance criteria (verbatim):** Malformed, oversized, nonfinite, duplicate and out-of-order inputs are rejected without altering accepted state.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SEC-004. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-005

Source: SRS table 7, row 6; RTM `Requirements RTM!A48:L48`. Proposed phases: 4, 5, 6, 8, 9.

**Requirement (verbatim):** Security-relevant events shall be recorded separately from clinical-simulation events without secrets.

**RTM acceptance criteria (verbatim):** Authentication failures, denied commands and security configuration changes produce redacted audit records.

Source risks: CYB-03; CYB-12. Source controls: RC-CYB-003; RC-CYB-012. Source planned verification: TC-SEC-005. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-006

Source: SRS table 7, row 7; RTM `Requirements RTM!A49:L49`. Proposed phases: 4, 5, 6, 8, 9.

**Requirement (verbatim):** Stored event data and application secrets shall have least-privilege access protections.

**RTM acceptance criteria (verbatim):** Tests/configuration review verify restricted file permissions and no embedded credentials.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SEC-006. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-007

Source: SRS table 7, row 8; RTM `Requirements RTM!A50:L50`. Proposed phases: 1, 6, 8, 9.

**Requirement (verbatim):** CI shall scan Python and frontend dependencies for known vulnerabilities.

**RTM acceptance criteria (verbatim):** Scan artifacts retained; unresolved findings are reviewed and dispositioned before release.

Source risks: CYB-07. Source controls: RC-CYB-007. Source planned verification: TC-SEC-007. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-008

Source: SRS table 7, row 9; RTM `Requirements RTM!A51:L51`. Proposed phases: 1, 6, 8, 9.

**Requirement (verbatim):** Each release shall produce an SBOM covering backend and frontend resolved dependencies.

**RTM acceptance criteria (verbatim):** Machine-readable CycloneDX or SPDX SBOM generated and linked to revision.

Source risks: CYB-07. Source controls: RC-CYB-007. Source planned verification: TC-SEC-008. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-009

Source: SRS table 7, row 10; RTM `Requirements RTM!A52:L52`. Proposed phases: 0, 6, 8, 9.

**Requirement (verbatim):** A version-controlled threat model shall describe assets, data flows, entry points and trust boundaries.

**RTM acceptance criteria (verbatim):** Review records show identified threats, controls and owners.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SEC-009. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-010

Source: SRS table 7, row 11; RTM `Requirements RTM!A53:L53`. Proposed phases: 0, 6, 8, 9.

**Requirement (verbatim):** Cybersecurity risks shall trace to mitigations and verification evidence.

**RTM acceptance criteria (verbatim):** Every identified security risk has a documented disposition and at least one linked verification activity.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SEC-010. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-011

Source: SRS table 7, row 12; RTM `Requirements RTM!A54:L54`. Proposed phases: 6, 8, 9.

**Requirement (verbatim):** Malformed and unauthorized requests shall not corrupt monitoring or alarm state.

**RTM acceptance criteria (verbatim):** Fault-injection tests preserve state and show explicit error responses.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SEC-011. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-012

Source: SRS table 7, row 13; RTM `Requirements RTM!A55:L55`. Proposed phases: 1, 6, 8, 9.

**Requirement (verbatim):** The project shall document vulnerability intake, triage, remediation and release decisions.

**RTM acceptance criteria (verbatim):** A sample vulnerability record demonstrates the process and evidence retention.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SEC-012. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-013

Source: SRS table 7, row 14; RTM `Requirements RTM!A56:L56`. Proposed phases: 6, 8, 9.

**Requirement (verbatim):** The system shall use least-privilege and secure configuration defaults.

**RTM acceptance criteria (verbatim):** Default configuration disallows external network exposure and debug endpoints.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-SEC-013. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-014

Source: SRS table 7, row 15; RTM `Requirements RTM!A57:L57`. Proposed phases: 3, 4, 6, 7, 8.

**Requirement (verbatim):** Alarm acknowledgment shall be authorized and bound to the current alarm episode.

**RTM acceptance criteria (verbatim):** Unauthorized, stale-episode and duplicate acknowledgment scenarios have passing tests.

Source risks: CYB-10; HAZ-04. Source controls: RC-CYB-010; RC-SAF-004. Source planned verification: TC-SEC-014. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-015

Source: SRS table 7, row 16; RTM `Requirements RTM!A58:L58`. Proposed phases: 1, 6, 8, 9.

**Requirement (verbatim):** Release documentation shall define secure update, rollback and integrity verification procedures.

**RTM acceptance criteria (verbatim):** A controlled update/rollback exercise is recorded.

Source risks: CYB-11. Source controls: RC-CYB-011. Source planned verification: TC-SEC-015. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### SEC-016

Source: SRS table 7, row 17; RTM `Requirements RTM!A59:L59`. Proposed phases: 4, 6, 7, 8.

**Requirement (verbatim):** Transport interruption shall be differentiated from sensor disconnection and shown explicitly.

**RTM acceptance criteria (verbatim):** WebSocket interruption produces connection warning and snapshot resynchronization after reconnect.

Source risks: HAZ-07; CYB-05. Source controls: RC-SAF-007; RC-CYB-005. Source planned verification: TC-SEC-016. Source component: Security / API / CI.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### PRIV-001

Source: SRS table 8, row 2; RTM `Requirements RTM!A60:L60`. Proposed phases: 1–9 (scope/data gates).

**Requirement (verbatim):** The simulator shall use synthetic physiological measurements only.

**RTM acceptance criteria (verbatim):** Test data and UI include no actual patient records; release review confirms synthetic-only datasets.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-PRIV-001. Source component: Privacy / data inventory.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### PRIV-002

Source: SRS table 8, row 3; RTM `Requirements RTM!A61:L61`. Proposed phases: 1–9 (scope/data gates).

**Requirement (verbatim):** The system shall not require patient names, dates of birth, or medical record identifiers.

**RTM acceptance criteria (verbatim):** Data schema review confirms absence of patient-identifying fields.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-PRIV-002. Source component: Privacy / data inventory.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### PRIV-003

Source: SRS table 8, row 4; RTM `Requirements RTM!A62:L62`. Proposed phases: 5, 6, 8, 9.

**Requirement (verbatim):** The project shall maintain a data inventory covering events, logs, accounts and metadata.

**RTM acceptance criteria (verbatim):** Inventory lists data category, purpose, storage location, retention and access.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-PRIV-003. Source component: Privacy / data inventory.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### PRIV-004

Source: SRS table 8, row 5; RTM `Requirements RTM!A63:L63`. Proposed phases: 1–9 (scope/data gates).

**Requirement (verbatim):** The system shall minimize personal data collection and disable third-party analytics by default.

**RTM acceptance criteria (verbatim):** Configuration and network inspection verify no analytics endpoints.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-PRIV-004. Source component: Privacy / data inventory.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### PRIV-005

Source: SRS table 8, row 6; RTM `Requirements RTM!A64:L64`. Proposed phases: 5, 6, 8, 9.

**Requirement (verbatim):** Application logs shall exclude credentials, tokens and unnecessary identifiers.

**RTM acceptance criteria (verbatim):** Automated log-redaction tests cover authentication and errors.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-PRIV-005. Source component: Privacy / data inventory.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### PRIV-006

Source: SRS table 8, row 7; RTM `Requirements RTM!A65:L65`. Proposed phases: 5, 6, 8, 9.

**Requirement (verbatim):** The system shall document retention, deletion and backup handling.

**RTM acceptance criteria (verbatim):** Test verifies documented deletion procedure for synthetic sessions; audit-retention exception documented.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-PRIV-006. Source component: Privacy / data inventory.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### PRIV-007

Source: SRS table 8, row 8; RTM `Requirements RTM!A66:L66`. Proposed phases: 0, 6, 9.

**Requirement (verbatim):** A GDPR applicability assessment shall be maintained and reviewed on scope changes.

**RTM acceptance criteria (verbatim):** Document explains whether identifiable natural-person data is processed and which obligations may apply.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-PRIV-007. Source component: Privacy / data inventory.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### PRIV-008

Source: SRS table 8, row 9; RTM `Requirements RTM!A67:L67`. Proposed phases: 1–9 (scope/data gates).

**Requirement (verbatim):** Adding real or identifiable personal data shall require design and privacy review before release.

**RTM acceptance criteria (verbatim):** Change checklist blocks unreviewed scope expansion.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-PRIV-008. Source component: Privacy / data inventory.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-001

Source: SRS controlled revision addendum, CL-001 — Scheduled gaps; RTM `Requirements RTM!A68:L68`. Proposed phases: 3, 4, 5, 8.

**Requirement (verbatim):** A missing scheduled SpO₂ reading interrupts consecutiveness and resets a pending activation or recovery counter; it does not clear an active alarm. A missed tick is detected using the deterministic simulation scheduler; the event is logged if storage is available. Verify low-low-gap-low does not activate, and recovery-recovery-gap-recovery does not clear.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-001

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: HAZ-01. Source controls: RC-SAF-001. Source planned verification: TC-CL-001. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-002

Source: SRS controlled revision addendum, CL-002 — Rejection classes; RTM `Requirements RTM!A69:L69`. Proposed phases: 2, 3, 4, 6, 8.

**Requirement (verbatim):** Invalid physiological value, missing SpO₂ value, or malformed/missing measurement timestamp resets the applicable pending count; a duplicate/out-of-order timestamp, wrong session, or unauthorized input is rejected without changing alarm counters. None overwrite last accepted data. Each rejection is classified and tested.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-002

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: HAZ-01; HAZ-06. Source controls: RC-SAF-001; RC-SAF-006. Source planned verification: TC-CL-002. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-003

Source: SRS controlled revision addendum, CL-003 — Time and transport; RTM `Requirements RTM!A70:L70`. Proposed phases: 4, 5, 6, 7, 8.

**Requirement (verbatim):** The backend uses a monotonic clock for 5-second staleness and simulation deadlines, and UTC timestamps for records. At 5.000 s a reading is CURRENT; at >5.000 s it is STALE. UI delivery ≤1 second applies only while the authenticated browser connection is healthy under the specified controlled test environment; transport loss produces an immediate connection-uncertain indicator on detection.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-003

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: HAZ-03; HAZ-07. Source controls: RC-SAF-003; RC-SAF-007. Source planned verification: TC-CL-003. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-004

Source: SRS controlled revision addendum, CL-004 — Restart; RTM `Requirements RTM!A71:L71`. Proposed phases: 4, 5, 7, 8.

**Requirement (verbatim):** Unexpected restart never resumes an old monitoring session or alarm episode automatically. UI shows monitoring stopped/restart detected; preserved event history is accessible only if storage is healthy; new session must be explicitly started. Verify with forced process termination and restart.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-004

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: HAZ-07. Source controls: RC-SAF-007. Source planned verification: TC-CL-004. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-005

Source: SRS controlled revision addendum, CL-005 — Persistence failure; RTM `Requirements RTM!A72:L72`. Proposed phases: 4, 5, 7, 8.

**Requirement (verbatim):** A monitoring-event write failure does not block alarm evaluation. The backend exposes event_storage_status=FAILED and history_completeness=INCOMPLETE; a subsequent successful write may restore write-health but must not claim that missing events were recovered. Verify failure and recovery behavior.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-005

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: HAZ-05. Source controls: RC-SAF-005. Source planned verification: TC-CL-005. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-006

Source: SRS controlled revision addendum, CL-006 — Security audit failure; RTM `Requirements RTM!A73:L73`. Proposed phases: 4, 5, 6, 8.

**Requirement (verbatim):** Network-mode operator commands that require accountable audit records (start/stop, acknowledge, sensor manipulation, security configuration) fail closed if the audit sink cannot accept a durable record, except an already-running sensor tick and automatic alarm evaluation must continue. The command response indicates failure without falsely reporting success; test audit-sink fault injection.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-006

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: CYB-12. Source controls: RC-CYB-012. Source planned verification: TC-CL-006. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-007

Source: SRS controlled revision addendum, CL-007 — Local/network roles; RTM `Requirements RTM!A74:L74`. Proposed phases: 1, 6, 7, 8.

**Requirement (verbatim):** Local mode: bind 127.0.0.1 only; one explicit local-operator context, no remote access, visible mode banner; tests confirm external bind disabled. Network mode: secure authentication, Observer read-only, Operator authorized to start/stop/acknowledge and simulate sensor faults, session-level authorization for REST and WebSocket, origin and session checks, credential expiry/revocation handling.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-007

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: CYB-01; CYB-06. Source controls: RC-CYB-001; RC-CYB-006. Source planned verification: TC-CL-007. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-008

Source: SRS controlled revision addendum, CL-008 — State synchronization; RTM `Requirements RTM!A75:L75`. Proposed phases: 4, 6, 7, 8.

**Requirement (verbatim):** Every authoritative state snapshot includes session_id, revision, server timestamp, sensor status, connection-independent data freshness, alarm episode/state, storage health and history completeness. Revision increases for each accepted mutation; clients discard older revisions and GET a fresh snapshot after reconnection.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-008

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: HAZ-07. Source controls: RC-SAF-007. Source planned verification: TC-CL-008. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-009

Source: SRS controlled revision addendum, CL-009 — Measurable timing; RTM `Requirements RTM!A76:L76`. Proposed phases: 5, 7, 8.

**Requirement (verbatim):** In deterministic scheduler tests, a 10-second active simulation emits 10 scheduled sets, with exact fake-clock ticks. In controlled local browser integration tests, 95% of accepted readings must render within 1.0 second of backend acceptance with no injected delay; all timing exceptions are logged and reviewed. This is a project target, not clinical performance validation.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-009

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: HAZ-03. Source controls: RC-SAF-003. Source planned verification: TC-CL-009. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-010

Source: SRS controlled revision addendum, CL-010 — Privacy inventory; RTM `Requirements RTM!A77:L77`. Proposed phases: 0, 5, 6, 9.

**Requirement (verbatim):** Record each processed field (including account ID, IP address, timestamps, audit metadata), purpose, access, retention, deletion and applicable jurisdiction. Synthetic physiological data alone does not establish GDPR non-applicability. No real patient identifiers or patient data may enter test fixtures or production simulation.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-010

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: CYB-04. Source controls: RC-CYB-004. Source planned verification: TC-CL-010. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-011

Source: SRS controlled revision addendum, CL-011 — Controlled release; RTM `Requirements RTM!A78:L78`. Proposed phases: 8, 9.

**Requirement (verbatim):** A release requires approved requirement baseline, mapped hazard and cybersecurity controls, documented test outcomes, vulnerability dispositions, SBOM for exact locked dependencies, signed-off open anomalies and evidence tied to a source revision. This requirement defines a release gate; no release is yet approved.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-011

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: CYB-07; CYB-11. Source controls: RC-CYB-007; RC-CYB-011. Source planned verification: TC-CL-011. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

### CL-012

Source: SRS controlled revision addendum, CL-012 — Design authority; RTM `Requirements RTM!A79:L79`. Proposed phases: 0–9 (change control).

**Requirement (verbatim):** All unresolved choices in prior design drafts are resolved by CL-001–CL-011 for the educational baseline. Changes to these decisions require change-control review and impact analysis across risk, tests, and design.

**RTM acceptance criteria (verbatim):** Verify specified behavior in TC-CL-012

The SRS requirement paragraph above contains the actual normative behavior and verification expectations. The RTM test reference requires reconciliation with STP; see F-03 and the crosswalk below.

Source risks: NOT LINKED — review applicability. Source controls: (blank). Source planned verification: TC-CL-012. Source component: As specified in clarification.

Source implementation: TBD; evidence: NOT RUN; status: NOT RUN; owner: TBD. Source review note: Design-stage mapping; verify risk relevance.

## Risk-control register (source mappings, not approvals)

All 22 source controls are OPEN / NOT VERIFIED; every residual risk is NOT ASSESSED and approval PENDING. Every planned-test cell in this source worksheet is `TBD — verify mapped case`. Forty-five requirement rows say `NOT LINKED — review applicability`; lack of a link is not an approved non-applicability decision.

| Risk ID | Control ID | Primary linked requirements (RTM verbatim) | Source row |
| --- | --- | --- | --- |
| HAZ-01 | RC-SAF-001 | FR-006; FR-007; FR-008; CL-001; CL-002 | Risk Control Register!2 |
| HAZ-02 | RC-SAF-002 | SF-004 | Risk Control Register!3 |
| HAZ-03 | RC-SAF-003 | FR-004; FR-005; FR-011; CL-003; CL-009 | Risk Control Register!4 |
| HAZ-04 | RC-SAF-004 | FR-009; FR-010; SEC-014 | Risk Control Register!5 |
| HAZ-05 | RC-SAF-005 | SF-005; CL-005 | Risk Control Register!6 |
| HAZ-06 | RC-SAF-006 | FR-015; CL-002 | Risk Control Register!7 |
| HAZ-07 | RC-SAF-007 | SEC-016; CL-003; CL-004; CL-008 | Risk Control Register!8 |
| HAZ-08 | RC-SAF-008 | FR-016 | Risk Control Register!9 |
| HAZ-09 | RC-SAF-009 | SEC-002 | Risk Control Register!10 |
| HAZ-10 | RC-SAF-010 | SF-001 | Risk Control Register!11 |
| CYB-01 | RC-CYB-001 | SEC-001; SEC-002; CL-007 | Risk Control Register!12 |
| CYB-02 | RC-CYB-002 | (blank in source) | Risk Control Register!13 |
| CYB-03 | RC-CYB-003 | SEC-005 | Risk Control Register!14 |
| CYB-04 | RC-CYB-004 | CL-010 | Risk Control Register!15 |
| CYB-05 | RC-CYB-005 | SEC-016 | Risk Control Register!16 |
| CYB-06 | RC-CYB-006 | SEC-002; CL-007 | Risk Control Register!17 |
| CYB-07 | RC-CYB-007 | SEC-007; SEC-008; CL-011 | Risk Control Register!18 |
| CYB-08 | RC-CYB-008 | SEC-003 | Risk Control Register!19 |
| CYB-09 | RC-CYB-009 | (blank in source) | Risk Control Register!20 |
| CYB-10 | RC-CYB-010 | SEC-014 | Risk Control Register!21 |
| CYB-11 | RC-CYB-011 | SEC-015; CL-011 | Risk Control Register!22 |
| CYB-12 | RC-CYB-012 | SEC-005; CL-006 | Risk Control Register!23 |

Supplemental mappings proposed from SHA/CRA are recorded in document review F-04. Blank RTM links for CYB-02 and CYB-09 are defects to resolve, not exclusions.

## STP clarification-case reconciliation proposal

STP v1.1 and RTM v1.1 use the same `TC-CL-*` labels with different meanings. This table preserves **STP's existing case IDs** and proposes links based on each case's actual scenario. It does not rename tests or amend the approved baseline. Multiple scenarios are needed to verify most requirements.

| Existing STP case | Actual STP scenario | Requirements to link (proposal) | Remaining verification |
| --- | --- | --- | --- |
| TC-CL-001 | Low, low, missed tick, low does not activate | CL-001; FR-006; FR-007 | Add recovery-gap scenario (TC-CL-004) and sensor-gap logging |
| TC-CL-002 | Duplicate timestamp preserves pending count | CL-002; FR-015 | Also out-of-order, wrong session, unauthorized classes |
| TC-CL-003 | Invalid SpO₂ resets activation count | CL-002; FR-004; FR-005; FR-007 | Missing/malformed timestamp, missing SpO₂, recovery counter |
| TC-CL-004 | Recovery, recovery, missed tick, recovery does not clear | CL-001; FR-008 | Active alarm preservation and gap event |
| TC-CL-005 | Forced process termination and restart | CL-004 | UI stopped/restart indicator and readable/unreadable history |
| TC-CL-006 | Event-store failure and recovery | CL-005; SF-005 | Failed write does not block alarm; incomplete history persists |
| TC-CL-007 | Audit-sink failure blocks operator command | CL-006; SEC-005 | All accountable commands; running ticks/evaluation continue |
| TC-CL-008 | Observer, cross-session and expiry denial | CL-007; SEC-001; SEC-002 | REST and WebSocket, origin, revocation, operator success |
| TC-CL-009 | Older revision discard and reconnect resync | CL-008; SEC-016 | Session changes, duplicate revisions, complete snapshot, restart |
| TC-CL-010 | Local mode rejects external bind | CL-007; SEC-013 | Local operator context and visible mode banner |
| TC-CL-011 | Locked SBOM and vulnerability exceptions | CL-011; SEC-007; SEC-008 | Approved baseline, all controls/tests, anomalies and revision evidence |

No detailed STP case is supplied for TC-CL-012. No existing TC-CL case fully specifies CL-003 time/transport, CL-009 timing measurement, CL-010 field inventory, or CL-012 authority/change control. Add explicit procedures with owner-approved IDs. Keep TC-FR-011 for the 5-second boundary and add wall-clock-change and transport-loss coverage. Legacy SHA/CRA `T-*`, `TC-SEC-02/04/05/06/08` and `TC-REL-01` references also require mapping to actual executable tests; do not infer equivalence from a similar name.

## Evidence policy

Implementation/test paths, commit SHAs, CI run links, actual outcomes and reviewer sign-off will be added incrementally after approved RED–GREEN–REFACTOR work. All source verification statuses remain NOT RUN. The [Phase 0 report](phase_0_report.md) concerns document review only. Product statement/branch coverage is not available.
