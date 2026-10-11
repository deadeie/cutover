# Project status

## Current phase

Phase 1: process discovery and confirmed requirements. No application, database migration or container has been implemented or runtime-tested. Read docs/RESUME-HERE.md first; detailed current requirements under docs/ supersede historical proposals and root-level duplicate foundation documents.

## Confirmed checkpoint

- Deployment: RHEL 8, Docker containers and delivered images. Suitable dependencies may be packaged in images; offline runtime remains the baseline. Detailed environment and technical design are deferred.
- Workflow: QA, Temperature, ATP and Handover use Operations task queues, claim/review, acknowledged colleague continuation and preserved correction/action history. Cutover keeps its separate planning/execution flow.
- QA: immediately submit/claim eligible after reported installation. Rejection means correction. Same-site routers have separate records with warning/confirmation and plane/topology identification.
- Temperature: immediately submit/claim eligible after QA approval, with no extra transition wait. Its configurable observation starts at submission; approval requires completed observation and Operations review. Preserve agreed correction/re-observation rules.
- Inter-stage policy: Operations Manager/Leader controls global submission-blocking versus early-submission/claim-blocking modes. Waiting requests recalculate on changes; already claimed requests retain their inter-stage eligibility rule. Time includes holidays.
- Cutover plan: Project plans first and pursues readiness. Only Operations records execution actions/results after start. Preserve failed attempts and actual participants. Successful completion and Operations confirmation share one event/time.
- ATP validity: Operations Leader sets duration. Expiry requires re-confirmation, blocks Cutover start and automatically creates an Operations review task. Notify Project and Operations Leaders. Conditional ATP uses the same duration. Changes recalculate approvals for routers not yet Cutover. Advance plan-readiness reminders have a configurable lead time.
- Handover: configurable interval after successful Cutover; conditional Handover completes transfer and releases Project while conditions remain tracked for Operations follow-up.
- Reminders: responsible-person alerts plus filterable consolidated leadership lists. Approved management reminders resolve when the expected action is performed, retaining history; reading an alert does not resolve it.
- Naming: site code is the QA name; multiple routers may share a site. Normal and X-pattern leading zeroes are allowed; X is a literal letter. TH province comes from the suffix. Preserve immutable router identity when assigning the full name at Temperature.
- OM ranges: one unique, non-overlapping range per RSG A/B pair. Operations Manager defines/approves new-range requests with group linkage required from the outset. Out-of-province OM IP blocks Temperature submission. First/second RSGs occupy their A/B positions in the same group; ASG/CSG membership follows range classification.
- Roles: System Administrator is separate from Operations Manager. Super Admin exceptions are deferred.
- Initial release records manual Operations checks. Photos/checklist forms, external automation and router-check connectivity are future extensions; no integration execution now.

## Decisions still open

- Initial timing/validity/reminder values, repetition and selected configuration permissions.
- Effect of increased ATP duration on an already expired approval/renewal task; expiry during/after Cutover and failed/replanned attempts.
- Observation-duration changes during a Temperature run; claim-warning and correction/resubmission timer behavior.
- Explicit all-province RSG grouping scope, full-name uniqueness and name-correction permissions.
- Precise RHEL/Docker architecture/versions, PostgreSQL deployment, authentication, email, UX and technical design.

## Validation and publication

This checkpoint contains requirements documents only. Validate document consistency and Git diffs; application tests are not applicable. The user authorized committing and pushing the checkpoint to origin/main. Use the actual Git result to establish publication status.
