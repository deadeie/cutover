# Project status

## Current phase

Phase 1: process discovery and confirmed requirements. No application, database migration or container has been implemented or runtime-tested. Read docs/RESUME-HERE.md first; detailed current requirements under docs/ supersede historical proposals and root-level duplicate foundation documents.

UX Phase 2 has an initial contract, a Persian weekly-plan wireframe and a standalone desktop demo at `prototypes/demo/index.html`. The demo uses fictitious local data and is not the application implementation. No database migration, backend or container has been implemented or runtime-tested.

## Confirmed checkpoint

- Deployment: RHEL 8, Docker containers and delivered images. Suitable dependencies may be packaged in images; offline runtime remains the baseline. Detailed environment and technical design are deferred.
- Workflow: QA, Temperature, ATP and Handover use Operations task queues, claim/review, acknowledged colleague continuation and preserved correction/action history. Cutover keeps its separate planning/execution flow.
- QA: immediately submit/claim eligible after reported installation. Rejection means correction. Same-site routers have separate records with warning/confirmation and plane/topology identification.
- Temperature: immediately submit/claim eligible after QA approval, with no extra transition wait. Its configurable observation starts at submission; approval requires completed observation and Operations review. Preserve agreed correction/re-observation rules.
- Inter-stage policy: Operations Manager/Leader controls global submission-blocking versus early-submission/claim-blocking modes. Waiting requests recalculate on changes; already claimed requests retain their inter-stage eligibility rule. Time includes holidays.
- Cutover plan: Project plans first and pursues readiness. Only Operations records execution actions/results after start. Preserve failed attempts and actual participants. Successful completion and Operations confirmation share one event/time.
- Cutover planning decision: Commissioning Leader creates a weekly plan; rows may have individual day/time placement inside that week. Separate daily Project plans are not used in the initial implementation.
- The Commissioning Leader must assign a planned Cutover executor to each router before publishing the weekly plan. This assignment applies only to Cutover; QA, Temperature, ATP and Handover have separate task assignments. Operations records the actual Cutover executor and may record another person while preserving both identities and history.
- ATP validity: Operations Leader sets duration. Expiry requires re-confirmation, blocks Cutover start and automatically creates an Operations review task. Notify Project and Operations Leaders. Conditional ATP uses the same duration. Changes recalculate approvals for routers not yet Cutover. Advance plan-readiness reminders have a configurable lead time. Validity is checked at each attempt start; expiry mid-execution does not interrupt it. Successful Cutover stops pre-Cutover renewals; failed/replanned attempts recheck. Increasing duration never revives expired ATP.
- Handover: configurable interval after successful Cutover; conditional Handover completes transfer and releases Project while conditions remain tracked for Operations follow-up.
- Reminders: responsible-person alerts plus filterable consolidated leadership lists. Approved management reminders resolve when the expected action is performed, retaining history; reading an alert does not resolve it.
- Naming: site code is the QA name; multiple routers may share a site. Normal and X-pattern leading zeroes are allowed; X is a literal letter. TH province comes from the suffix. Preserve immutable router identity when assigning the full name at Temperature.
- OM ranges: one unique, non-overlapping range per RSG A/B pair. Operations Manager defines/approves new-range requests with group linkage required from the outset. Out-of-province OM IP blocks Temperature submission. First/second RSGs occupy their A/B positions in the same group; ASG/CSG membership follows range classification.
- Roles: System Administrator is separate from Operations Manager. Operations Leader has global report/status visibility across projects/provinces; Project Leader is limited to assigned projects and their plan management. Unspecified action/export/assignment details remain open in `docs/ROLE-MATRIX.md`. Super Admin exceptions are deferred.
- Reporting scope: live network status and continuous monitoring are excluded. Management reports and possible later graphs concern recorded workflows and configured logical relationships.
- Required reporting: project progress by province and a leadership dashboard of personnel workload/performance (including completed and in-progress work). Detailed metrics remain proposed in `docs/MANAGEMENT-REPORTING-PROPOSAL.md`.
- Required user experience: each person has a personal workspace for ongoing, completed, waiting, returned-for-correction and upcoming assigned work, scoped by role/project permissions.
- Initial release records manual Operations checks. Photos/checklist forms, external automation and router-check connectivity are future extensions; no integration execution now.

## Confirmed UX direction

- Pre-QA planned items are active in the first release when they belong to the approved project scope. They can enter the weekly Cutover plan before QA, while execution remains blocked until prerequisites pass.
- Initial desktop demo: `prototypes/demo/index.html`, with overview, personal work, weekly plan, Operations queues, router/project list, reminders, management reports and configuration views. It is for local presentation and process review only; it has no backend connection. The former Hyperspace template is not the current design direction.

## Decisions still open

- Approval and import authority for additions to the approved project scope; see `docs/CUTOVER-PLAN-CREATION-PROPOSAL.md`.
- Initial timing/validity/reminder values, repetition and selected configuration permissions.
- Management report priorities, metrics, exports, manager scopes, project assignment and later graphs; see `docs/MANAGEMENT-REPORTING-PROPOSAL.md`. ATP execution/expiry edge cases are confirmed; exact renewal-check scope remains open.
- Observation-duration changes during a Temperature run; claim-warning and correction/resubmission timer behavior.
- Explicit all-province RSG grouping scope, full-name uniqueness and name-correction permissions.
- Precise RHEL/Docker architecture/versions, PostgreSQL deployment, authentication, email, UX and technical design.

## Validation and publication

This checkpoint contains requirements documents and a local interactive UX demo only; no production application, database or container exists. Check Git status and origin/main to establish publication state.
