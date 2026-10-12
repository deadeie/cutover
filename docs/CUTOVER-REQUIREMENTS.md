# Cutover — requirements and proposed operating model

Status: requirements updated with Operations-only execution recording. Proposed views and advance planning accepted by the user; detailed checklist criteria remain open.

## Entry condition

Latest clarification: the Cutover plan is Project's primary plan and may precede Temperature/ATP. Track missing readiness against that plan. ATP approval has an Operations-Leader-configured validity interval; expiry requires re-confirmation and notification to both Project and Operations Leaders. ATP approved without a plan is an Operations concern. See `ATP-VALIDITY-AND-CUTOVER-READINESS.md`; blocking Cutover start with expired ATP, automatic Operations renewal tasks and configurable advance readiness warnings are confirmed.

2026-10-11 clarification: successful Cutover completion and Operations confirmation of success are one event/time, used as the Handover timing anchor. Cutover is excluded from the shared QA/Temperature/ATP/Handover timing modes. Plan-readiness, ATP-validity and missing-Handover-request reminders are recorded in `SHARED-REQUEST-WORKFLOW.md`. Initial checks remain manual; future integration is described in `MANUAL-CHECKS-AND-FUTURE-INTEGRATION.md`.

Actual Cutover requires full or conditional ATP approval by Second-Line Operations. The schedule displays QA, Temperature and ATP states, with conditional approval visibly distinct. Advance planning of pending routers with execution blocked is accepted. Scheduling does not grant execution permission.

Confirmed execution boundary: ATP must be valid at each attempt's start; expiry during an already validly started attempt does not interrupt it. Successful Cutover stops further pre-Cutover ATP renewal tasks. Failed/replanned attempts recheck validity at their new start. See `ATP-VALIDITY-AND-CUTOVER-READINESS.md`.

## Scheduling model

The Commissioning Leader creates and manages **weekly** Cutover plans. The leader does not create a separate daily plan. A weekly plan contains router rows, each optionally assigned to a specific day and time window within that week.

The user requested clarification of where candidate routers come from. `CUTOVER-PLAN-CREATION-PROPOSAL.md` recommends selecting stable records from the assigned project's router list and, if approved, supporting planned items before QA. Pre-QA item creation, import and related permissions are proposals; do not treat them as implemented or confirmed. Existing routers must not be duplicated merely to add them to a plan.

Recommended plan fields:

- Plan ID and name.
- Week start/end, time zone, and optional maintenance window.
- Optional row-level day and start/end time window within the week.
- Project and province filters.
- Plan status: Draft, Published, In progress, Completed, Cancelled, Archived.
- Created/published by and timestamps.
- Version or revision when rows are changed after publication.

Recommended router-row fields:

- Existing rollout item and current canonical router name.
- Project, province, center, hardware model, and OM IP.
- QA, Temperature, and ATP status snapshots plus links to the current approvals.
- Planned sequence/order and target time window.
- Planned Project person: optional, particularly in weekly plans; the Commissioning Leader can assign on the execution day. Keep the actual executor separately identifiable.
- Network Operations participant: selected when the work is accepted/started by First-Line or Second-Line Operations; this person may vary by row.
- Row status: Planned, Ready, Accepted by Operations, In progress, Completed, Failed, Rolled back, Blocked, Rescheduled, Cancelled.
- Pre-check result, execution result, post-check result, comments, and evidence.

## Proposed scheduling controls

1. Publishing validates readiness again. Operations must recheck current ATP approval when authorizing execution; a schedule snapshot cannot replace current approval. ATP expiry and Operations Leader configuration are confirmed; the confirmed start gate, equal validity of conditional ATP, recalculation of unexecuted approvals and remaining expiry edge cases are described in `ATP-VALIDITY-AND-CUTOVER-READINESS.md`.
2. The schedule shows readiness badges for QA, Temperature, and ATP and provides the blocking reason.
3. Weekly planning may leave the Project executor unassigned. Operations can record or change the actual executor, including last-minute changes, with full attribution and history. Proposal: require actual executor identity before execution is recorded as started.
4. Operations participant remains variable and is recorded when the row is accepted or started.
5. Moving a row to another day/time creates a new plan-row revision and preserves the previous date/time, reason, and actor. It does not create a separate daily plan.
6. The same router cannot be active in two Cutover rows at overlapping times without an authorized exception.
7. A published plan is a coordination record; it does not approve prerequisites or automatically start a Cutover.

## Cutover execution flow

```text
Commissioning Leader publishes plan
        ↓
Operations First-Line/Second-Line specialist opens row
        ↓
Pre-check: ATP approval, identity, schedule, and dependencies
        ↓
Operations specialist confirms readiness and records pre-check comment
        ↓
Assigned Project person performs Cutover with Operations support
        ↓
Operations records execution completion based on coordination with the Project executor
        ↓
Operations performs initial post-checks manually or through a future automation
        ↓
Completed / Failed / Rolled back / Blocked
```

## Responsibility boundary

- The Commissioning Leader assigns the Project execution person.
- The First-Line or Second-Line Operations specialist is the variable Operations participant and confirms readiness.
- The Project person performs the physical/operational work with Operations, but has no Cutover record action after execution begins. Coordination outside the record is not a required Project submission.
- First-Line or Second-Line Operations records execution progress, completion and success/failure and performs initial post-checks.
- Operations may change the Project executor at the last minute. Store old/new person, actor, timestamp, explanation, action comment and the relevant attempt. Keep planned assignment history.
- Post-checks include alarms, traffic, links, router logs and overall condition. Exact pass/fail thresholds and evidence remain open.
- Operations records an unsuccessful outcome with explanations. After the router problem is resolved, the Commissioning Leader may add it to a new daily/weekly plan. This creates a new attempt on the same router; never overwrite the failed attempt.
- Distinguish actual executor, recording Operations specialist and final approving Operations specialist; they need not be the same person.
- Every pre-check, start, completion notification, post-check, failure, rollback, and approval has its own action comment and evidence.

## Future Cutover-check automation

Design an adapter boundary now, but keep manual checks as the valid first mode:

```text
CutoverCheck interface
  ├── ManualCutoverCheck
  └── AutomationCutoverCheck (future adapter)
```

Automation output must be stored as evidence for a check attempt and must distinguish:

- Tool failure or unreachable automation.
- Router/network check failure.
- Successful check with findings.
- Successful check without findings.

Automation must not automatically approve Cutover unless an explicitly approved policy later allows that behavior. Credentials and secrets must not be stored in comments, logs, image layers, or exported schedules.

## Suggested schedule views

- Calendar/day view for the selected date.
- Week board grouped by project, province, or Operations participant.
- Table view with readiness badges and blocking reasons.
- Detail drawer showing approvals, assigned Project person, current Operations participant, action comments, and evidence.
- Conflict view for overlapping rows, missing ATP, expired approvals, and overdue work.

## Open decisions

1. Exact publication and revision controls for plans? Advance planning with execution blocked is confirmed.
2. What are the Cutover window fields and timezone rules?
3. Which exact pre-checks must Operations complete before Project execution starts?
4. What are the exact pass criteria/evidence for alarms, traffic, links, logs and overall condition?
5. Is Operations participation selected by the specialist who opens the row, by the Leader, or by a queue acceptance action?
6. Should actual executor be mandatory at start or before final result? Operations can change that person with history.
7. Can one Operations specialist support multiple rows in the same window?
8. Which failures require rollback, and who authorizes it?
9. Resolved: successful Cutover completion and Operations confirmation share one event/time, which starts the configurable Handover interval.
10. What information will the future Cutover automation consume and return?
