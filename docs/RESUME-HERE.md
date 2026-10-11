# Resume checkpoint

Requirements discovery only. No application or container has been built or tested. Latest user clarifications take precedence over historical proposals in older documents.

## Current source of truth

1. SHARED-REQUEST-WORKFLOW.md: QA, Temperature, ATP and Handover have separate Operations task queues with claim/review, acknowledged continuation and correction cycles. Submitted work concerns Operations; returned corrections concern Project.
2. QA submission/claim is immediate after reported installation completion. Temperature submission/claim is immediate after QA approval. There is no QA-to-Temperature waiting interval. Temperature approval still requires its configurable observation period starting at submission and Operations review. Thermal/CPU/fan correction resubmission restarts observation; connectivity-only correction does not.
3. Operations Manager/Leader controls system-wide inter-stage timing modes: block early submission, or accept it but block claim until eligible. Waiting unclaimed requests recalculate on interval changes. Already claimed requests retain their claim-time inter-stage eligibility rule; review/results are not interrupted. Hours include holidays. Cutover success and Operations confirmation share one event/time.
4. ROUTER-IDENTITY-AND-NAMING.md: QA name is the site code, shared by multiple routers at one site. Warn and require confirmation for a second router. Simultaneous installation uses separate QA requests, asks A/B for the second and explicitly confirms the first plane. Same-site ASG/CSG can be distinguished by topology at QA. Full names are supplied at Temperature. TH province comes from the suffix; topology comes from the second character; each RSG A/B pair shares one unique non-overlapping range with its children. Province IP validation is mandatory. OM-RANGES-AND-RSG-GROUPS.md records the approved range-request flow: Operations Manager defines/approves ranges and group ownership is mandatory initially. A/B membership is confirmed: each RSG occupies its plane position in the shared pair; the second completes that group. Explicit all-province scope remains to be clarified. Normal RSG examples are confirmed; leading zeroes are allowed in both normal and X site codes. X is a literal letter, never equivalent to zero.
5. MANUAL-CHECKS-AND-FUTURE-INTEGRATION.md: first release records externally performed Operations checks and decisions. QA rejection returns for correction. External provincial QA contacts are not system users. Photo/checklist features and external automation/router-check integration are future capabilities; preserve extensibility without implementing them now.
6. ROLE-MATRIX.md: System Administrator is distinct from Operations Manager. Installation and Commissioning Leaders are distinct. Timing authority above belongs to Operations Manager/Leader; Super Admin exceptions are deferred.
7. CUTOVER-REQUIREMENTS.md: daily/weekly planning may omit the planned executor. Only Operations records execution after start, including actual executor changes and success/failure. Failed attempts are preserved and may be replanned.
8. HANDOVER-REQUIREMENTS.md and CONDITIONAL-APPROVALS.md: conditional ATP permits Cutover; conditional Handover completes transfer and releases Project. Conditions remain in a dedicated register with Operations reminders; external remediation is out of scope.
9. ACTION-COMMENTS.md: preserve actual actors, separate action comments and chronological attempts. Eligible Project/Operations colleagues may continue with warning and acknowledgement without mandatory manager intervention.
10. ADMIN-POLICIES-AND-DEPLOYMENT.md: RHEL 8 with Docker and delivered images. Package-selection restrictions are withdrawn; offline runtime remains the baseline. Detailed environment, email, UX and technical design are deferred.

## Reminders

Personal reminders target the responsible person. Relevant leaders/managers have a consolidated filterable list. Project Manager configures the missing-Handover-request reminder after successful Cutover. The former Project-owned ATP-to-plan deadline is superseded: Cutover planning comes first, missing Temperature/ATP readiness concerns Project, and approved ATP without a plan concerns Operations. Operations Leader configures ATP validity; expiry requires re-confirmation and informs both leaders. Confirmed in ATP-VALIDITY-AND-CUTOVER-READINESS.md: expired ATP blocks Cutover start and automatically creates an Operations renewal task. Conditional ATP has the same validity duration. Duration changes recalculate approvals of routers not yet Cutover. An approaching Cutover plan with incomplete/invalid Temperature or ATP generates a reminder with configurable advance warning time. The additional reminders in SHARED-REQUEST-WORKFLOW.md are approved. Performing the expected action resolves the active reminder while preserving history; reading it does not. Initial validity/advance-warning values, recurrence, restoration after extending an expired approval and expiry during/after Cutover remain open.

## Next discussion

- Confirm explicit all-province grouping scope. RSG pair membership, range requests, Operations Manager authority and mandatory initial group ownership are approved.
- Full-name uniqueness and name-correction permissions; leading-zero rules are resolved.
- Set ATP validity and readiness-reminder defaults. Resolve restoration after a duration increase, expiry during/after Cutover, failed/replanned attempts and exact renewal-check scope; the start gate, automatic task, conditional validity and recalculation are confirmed.
- Remaining timing details: stage-specific mode configuration, mode changes for waiting requests, correction/continuation warning timers and observation-duration changes during a Temperature run.
- Detailed checklists and automated checks are not blockers for initial-release event recording.

## Repository note

A local clone exists at dalaran/cutover with origin pointing to deadeie/cutover. The user authorized committing and publishing this requirements checkpoint to origin/main. Verify the actual publication result with Git; this document is not proof of a completed push. Earlier root-level duplicate documents are historical; docs/ contains current requirements.
