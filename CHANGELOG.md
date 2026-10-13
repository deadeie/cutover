# Changelog

## Unreleased

- Stabilized local QA submission/correction and same-site identity; serialized mutation checks, validated site formats, required explicit first-router plane confirmation, and corrected request-form selection/eligibility. Seven workflow scenarios and browser checks cover this bounded increment. See `docs/LOCAL-STABILIZATION.md` for remaining gaps and historical duplicate data.

- Added a dependency-free, native Windows local workflow application under `application/`, backed by a local SQLite adapter so the user can evaluate persistent end-to-end process flow before the later RHEL/container packaging phase.
- Implemented router records, separate QA/TEMP/ATP/Handover requests, Operations claim/review/correction return and resubmission, weekly Cutover planning with optional planned executor, distinct actual executor and recorded success, and event history.
- Enforced the TEMP observation approval gate, Cutover prerequisite/ATP-validity gate with Operations ATP renewal task, and Handover elapsed time from successful Cutover. Added local timing settings and workflow tests.
- Documented local launch and architecture limits; role selection is simulated, production authentication/database/packaging remain unimplemented, and no live-network action is performed.
- Fixed duplicate QA submission on an already-QA'd router while allowing a separately confirmed second router at the same site; same-topology second-router QA requires explicit A/B identification.

- Added a formal, desktop-oriented standalone demo at `prototypes/demo/index.html` with overview, personal work, weekly Cutover planning, Operations queues, router/project records, reminders, management reports and settings. Uses local fictitious data; it is not a production application.
- Confirmed the planned Cutover executor is optional on each weekly-plan row. Other workflow stages keep their own assignments; Operations can record a different actual Cutover executor while preserving both identities and history.
- Superseded the explored HTML5UP Hyperspace visual direction with a restrained black/white administrative interface.
- Made Project request creation visible in the demo: add/select an in-scope router record, submit its next eligible stage request, and see the resulting task in the Operations queue. Added seeded examples for QA, TEMP, ATP renewal and Handover paths.

- Added the missing Persian weekly Cutover text wireframe with board/table layouts, approved pre-QA handling, current versus planned-time ATP readiness, editing proposals, role boundaries and review scenarios. No application implementation is implied.

- Confirmed primary weekly board and synchronized table layout; aligned the approved pre-QA plan flow for the 2026-10-12 publication checkpoint.

- Confirmed pre-QA planned items are active in the first release when they belong to the approved project scope; execution remains gated by QA/Temperature/ATP readiness.
- Started UX Phase 2 with an initial contract for personal workspace, weekly Cutover plan, Operations queues, Management dashboard and router detail.
- Added required personal workspace for each user: ongoing, completed, dependency-waiting, returned-for-correction and upcoming assigned work, with role-aware visibility.
- Approved weekly Cutover planning for initial implementation: one weekly plan with optional day/time placement per router row; no separate daily Project plans.
- Confirmed provincial project progress reporting and a leadership personnel workload/performance dashboard; documented proposed metrics and attribution rules separately.
- Proposed Cutover plan creation from stable project router records, with an optional pre-QA planned-item path pending confirmation; preserved readiness gating at execution.
- Confirmed Operations Leader global report/status visibility across all projects/provinces and Project Leader visibility/plan management limited to assigned projects; broader viewing does not grant additional editing or override powers.

### Reporting scope and leadership access

- Confirmed live network status/monitoring is out of scope; management reports and proposed logical graphs use recorded workflow and configuration data.
- Confirmed Operations Leader must have broader access than Project Leader; kept global versus assigned-project visibility and detailed permissions explicitly proposed pending confirmation.
- Preserved previously assigned action authority and the separate deferred automation-check capability.

### ATP boundaries and management reporting discussion

- Confirmed ATP validity at each Cutover start, uninterrupted active execution on later expiry, no new pre-Cutover renewal tasks after success, and validity recheck for failed/replanned attempts.
- Confirmed that increasing duration cannot revive expired ATP; its renewal task remains required.
- Recorded requested management reporting and a separately labeled proposal for report priorities, metrics, exports and later charts/logical RSG graphs.

### Confirmed ATP renewal and RSG membership checkpoint

- Confirmed blocking Cutover start with expired ATP, automatic Operations renewal tasks, equal validity duration for conditional ATP and recalculation of unexecuted approvals after duration changes.
- Approved configurable advance reminders for incomplete/invalid Temperature or ATP ahead of planned Cutover.
- Confirmed first/second RSG A/B membership in a shared range group as recorded relationships only.
- Consolidated the continuation checkpoint for publication at the user's request; application implementation remains out of scope.

- Corrected planning model: Cutover plans drive Project readiness; replaced Project-owned ATP-to-plan deadline with Operations-Leader-configured ATP validity and dual-leader expiry notifications. Documented renewal/execution-gate proposals separately.
- Confirmed Operations Manager approval of new-range requests and required group ownership at initial range definition.
- Confirmed normal site-code leading zeroes as well as X-pattern leading zeroes; X remains a distinct literal letter.

- Confirmed normal RSG examples, leading zeroes for X site codes, explicit first/second QA plane confirmation and ASG/CSG topology distinction.
- Confirmed one shared range per RSG pair, non-overlapping province ranges and rejection of out-of-province OM IP; documented a proposed separate new-range registration flow.
- Approved additional management reminders and removal from the active list only when the expected action is performed, retaining history.

- Confirmed immediate QA submission/claim after installation and immediate Temperature submission/claim after QA approval; retained configurable observation before Temperature approval.
- Captured warning/confirmation for a second router at an existing site and separate simultaneous QA requests with A/B identification on the second request; final names remain assigned at Temperature.

- Confirmed across QA, Temperature, ATP and Handover: inter-stage interval changes recalculate unclaimed waiting requests; already claimed reviews continue under the eligibility rule at claim time without being paused by the new interval.

### 2026-10-11 — Shared requests, ownership and naming

- Extended claim/review requirements to QA and Temperature, with per-stage Operations queues and correction responsibility returning to Project.
- Confirmed system-wide Operations Manager/Leader timing modes, recalculation of waiting requests, continuous hours and unified Cutover success time; separated System Administrator role.
- Confirmed consolidated leadership reminder lists and Project-configured missing-plan/missing-Handover reminders; marked further reminders as proposals.
- Clarified QA site-code identity, shared-site router examples, TH suffix/topology interpretation and TH-only OM-range mapping; retained contradictory RSG examples as unresolved.
- Confirmed QA rejection means correction and initial release records external manual checks; future evidence/checklist/automation extensions remain requirements only.

### 2026-10-11 — Deployment and administrator policy clarification

- Confirmed RHEL 8, Docker containers and image delivery; withdrew earlier package-selection restrictions while retaining offline runtime requirements.
- Confirmed administrator-controlled intervals and Handover submission enablement; recorded open questions about scope, wait waivers and existing requests.
- Confirmed personal reminder routing with awareness for relevant section leaders/managers.
- Updated the continuation checkpoint and local Git status; naming/checklist discovery continues before UX and technical design.

### Conditional decisions and continuation checkpoint

- Confirmed conditional ATP permits Cutover and conditional Handover completes delivery, releasing Project responsibility.
- Added conditional-router register and configurable timed Operations reminders; external remediation team remains outside system scope.
- Added `docs/RESUME-HERE.md` to distinguish confirmed requirements, proposals and next-session decisions.

### Cutover control and Handover clarification

- Extended acknowledged continuation to Project users; preserved Cutover Operations-only record actions after start.
- Accepted weekly plans without assigned executor, advance readiness views and future check adapter.
- Captured Operations-attributed executor changes and unsuccessful attempts followed by new plans.
- Added Handover after successful Cutover plus 48 hours and distinct conditional ATP/Handover decisions; effects on progression remain open.

### Latest process-owner clarification

- Replaced manager-dependent ATP handoff with warning/acknowledgement continuation by another Second-Line specialist; retain actual correction-request sender separately.
- Confirmed Temperature repeat interval begins when the corrected same request is resubmitted.
- Captured daily/weekly Cutover planning, named Project executor, variable Operations participant, execution authorization, completion report and Operations post-check approval.

### ATP and Temperature clarification

- Temperature starts at submission; monitoring faults repeat the interval, connectivity-only faults do not; no additional pre-ATP waiting interval.
- ATP means Acceptance Test Procedure; recorded exclusive Second-Line claims, management-configurable warning levels, manual/optional automation review and separately retained correction cycles.
- Proposed release, accepted handoff, and management reassignment with preserved work and ownership/run safeguards; awaiting user validation.
- Proposed Cutover schedule, named Project executor, variable Operations participant, pre-check/post-check flow, and future automation adapter boundary.

### Requirements clarification

- Confirmed Second-Line Operations QA review and mandatory rejection reason.
- Captured 48-hour Temperature monitoring, CPU/fan checks, monitoring-system readiness, OM IP and hardware model.
- Captured multiple generally /24 OM ranges per province and action-specific comments.
- Replaced speculative role matrix with confirmed responsibilities and separate installation/commissioning leaders.
- Timer start, restart, and possible extra inter-stage wait remain unresolved.

### Added

- Initial project roadmap and phase gates.
- Initial project status, assumptions, risks, and approval gate.
- Documentation-first implementation tracking.
- Phase 1 process-discovery pack, glossary, and prioritized capability backlog.
- Revised process model with Design, Project, and Network Operations groups; five gated stages; configurable timers; and workflow administration rules.
- Initial role and responsibility matrix for the three groups.
- Router identity lifecycle, QA alias, canonical naming patterns, and naming exceptions.
- Stage 1 QA form specification and partial Stage 2 Temperature form specification.

### Notes

- No application code or production container has been implemented yet.
- Phase 1 is waiting for process-owner validation.
