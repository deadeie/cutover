# Handover

Status: requirements discovery; no implementation yet.

The 48-hour references below describe the baseline, not a fixed constant. Operations Manager/Leader controls the confirmed waiting/claim modes; System Administrator is a separate role. See `SHARED-REQUEST-WORKFLOW.md`.

## Confirmed

Latest 2026-10-11 clarification: Operations Manager/Leader controls the global wait and submission-blocking versus early-submission/claim-blocking mode, as described in `SHARED-REQUEST-WORKFLOW.md`. Recalculate waiting requests on policy changes. Cutover success and Operations confirmation are one event/time; hours are continuous, including holidays. The System Administrator is a separate role. This supersedes the earlier open timestamp and enable/disable interpretation. Manual checks and future integration are covered in `MANUAL-CHECKS-AND-FUTURE-INTEGRATION.md`.

- After successful Cutover, the Project Commissioning Specialist can request Handover once 48 hours have passed.
- Use the same router/rollout record and preserve every previous stage.
- The division of work follows ATP: Second-Line Operations claims, reviews, approves or returns findings for correction.
- An eligible colleague in either team may continue after warning and explicit acknowledgement, with original and actual actors retained.
- Repeated correction cycles retain separate findings, action comments, evidence, submitters and reviewers in chronological order.
- Full Operations approval marks the router handed over.
- Conditional Handover also completes handover and releases the Project Team. Remaining work belongs to an external team outside this system. Keep the router in the conditional register with timed reminders to Operations.

## Proposed state flow

WAITING_FOR_ELIGIBILITY → DRAFT → SUBMITTED → CLAIMED / IN_REVIEW
→ APPROVED / CONDITIONALLY_APPROVED / RETURNED_FOR_CORRECTION
→ corrected resubmission and a new review attempt where applicable.

## Proposed timing implementation

- Use the authoritative Operations-recorded successful Cutover event plus 48 hours; confirm whether its recorded completion time or approval time is the anchor.
- Failed attempts do not qualify; retain every failed and successful attempt separately.
- Recheck eligibility at submission, not only in the displayed countdown.
- Inherit the versioned configurable timing policy; no new exceptions assumed.
- Apply ATP-style configurable lower/higher claim warnings; numerical thresholds still need definition.

## Acceptance scenarios to implement later

- A failed Cutover cannot qualify for normal Handover submission.
- Before the eligibility boundary submission is blocked; at the boundary it becomes eligible.
- Project and Operations continuation records actual actors without rewriting original authors.
- Correction cycles and conditional decisions remain independently retrievable.
- Both full and conditional approval mark handover complete; conditional approval additionally preserves the conditions register and reminders.

## Open details

- Handover checklist, evidence and pass criteria.
- Exact authoritative Cutover-success time and incident handling during the wait.
- Conditional-register reminder interval, recipients, repetition and resolution-recording rules.
- Claim warning thresholds, notification routing and condition follow-up responsibilities.
