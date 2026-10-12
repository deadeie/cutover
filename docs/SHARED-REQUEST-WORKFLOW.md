# Shared request workflow — QA, Temperature, ATP and Handover

Process-owner clarification, 2026-10-11. Confirmed requirements are separated from proposals and open questions. This document supersedes conflicting earlier workflow and timing proposals. A local demo illustrates the workflow; no production application code has been built.

## Creating stage requests from a Project router record

- First create or select one router/work item inside the approved Project scope. That record is the shared identity used across QA, Temperature, ATP, Cutover and Handover; stage requests do not create duplicate router records.
- Once installation is reported complete, a Project user submits a QA request against that record with the site/center/topology details. Operations receives a separate QA task in its queue.
- After QA approval, the Project user submits the Temperature request on the same record. The canonical router name and OM IP are completed as required for that stage; Operations receives a separate Temperature task.
- After Temperature approval, the Project user submits ATP on the same record; it becomes a separate Operations task. An expired ATP is re-confirmed through the Operations renewal/review flow.
- After successful Cutover and the configured wait, Project submits Handover on the same record. The request is routed to the Handover Operations queue.
- The request form shows only the next stage whose prerequisites are met. An already submitted/pending request is followed in its existing queue item; duplicate active requests are not created.
- The planned Cutover executor in a weekly plan is independent from these stage requests and is optional. Assignment of QA, Temperature, ATP and Handover work follows their own Operations assignment/claim process.

## Confirmed task lifecycle

- Extend the ATP/Handover claim-and-review approach to QA and Temperature: Operations selects a request, claims responsibility, reviews it, and records approval or returns it for correction.
- Retain the existing acknowledged-continuation approach for eligible colleagues, actual actors, separate correction cycles and action comments. Existing ATP implementation proposals are not automatically confirmed by this extension.
- Project submissions appear individually and comprehensively in Operations work queues, separated by stage, so Operations can select and perform them.
- A submitted, unclaimed task is an Operations team concern. Returning a task for correction makes it a Project team concern; resubmission returns it to Operations.
- Personal tasks requiring attention notify the relevant person. Leaders/managers see a consolidated, filterable reminder list for their section. Email and other channels are deferred.
- QA rejection means return for correction, not terminal rejection.
- Cutover retains its separate planning/execution workflow and Operations-only execution recording.

## Confirmed global timing policy

Network Operations Manager or Leader can change intervals and select either mode for the request stages (excluding Cutover):

1. Block submission until the configured interval after completion of the previous process has elapsed.
2. Accept early submission but block Operations claim until that interval has elapsed. Waiting requests must have a distinct color/format; their presentation changes when eligible. Visual distinction alone is insufficient: claim must actually be prevented.

- Policy scope is system-wide, not a per-router/project exception. Whether one mode applies to all stages or each stage has its own system-wide mode remains open.
- Recalculate existing waiting requests using updated intervals, including the supplied 48-to-24-hour example.
- Confirmed follow-up: in all four stages, an already claimed request continues under the inter-stage eligibility rule in force when it was claimed. A later interval change does not pause its review or prevent recording its result. Recalculate unclaimed waiting requests under the new interval. This confirmation concerns inter-stage eligibility, not an inferred change to monitoring durations or claim-warning timers.
- Time is continuous elapsed time, including holidays.
- Successful Cutover completion and Operations confirmation of success are one business event/time. That event anchors the Handover interval.
- System Administrator is separate from Operations Manager. Timing controls above explicitly belong to Operations Manager/Leader; other System Administrator privileges remain undefined.
- Exceptional Super Admin access is a future discussion; do not implement an unrestricted bypass or grant it to existing roles now.
- A blanket shutdown of all submissions, a zero-delay bypass mode and automatic approval are not confirmed by these two modes.

## Timing questions still open

- Resolved: QA can be submitted and claimed immediately after installation is reported complete, without a preceding-stage delay. Operations response time is tracked separately.
- Resolved: Temperature can be submitted and claimed immediately after QA approval. There is no QA-to-Temperature waiting interval. Its configurable observation period starts at Temperature submission; Operations may work during it but cannot approve before it ends. Previously confirmed correction/re-observation rules remain in force.
- How do changes to the observation duration affect a running Temperature observation? Do not infer this from the separate inter-stage claim-time policy.
- How does switching submission/claim modes affect submitted waiting requests? Changes to intervals do not interrupt already claimed reviews (confirmed above).
- Does each stage have a separate system-wide interval and mode? What are the initial values for each transition?
- Does time gating apply again on correction resubmission? Preserve the confirmed Temperature correction rules until clarified.
- What happens to claim-warning timers during transfer, correction and resubmission? Which lower/higher thresholds apply to QA/Temperature?

## Confirmed management reminders

| Trigger | Responsible team | Interval configured by |
|---|---|---|
| Successful Cutover without a Handover request after the configured interval | Project | Project Manager |
| ATP validity expires before Cutover, requiring re-confirmation whether planned or not | Operations; inform both Project and Operations Leaders | Operations Leader |
| Cutover is planned but Temperature/ATP readiness is incomplete or unknown | Project; relevant Operations visibility | Advance warning interval is configurable; numerical value and role authority remain open |

Cutover planning comes first in Project work. ATP approved without a plan is an Operations concern; the earlier Project-owned ATP-to-plan deadline is superseded. ATP now has Operations-Leader-configured validity and requires re-confirmation on expiry. See `ATP-VALIDITY-AND-CUTOVER-READINESS.md` for confirmed start blocking, automatic Operations renewal tasks, equal conditional ATP validity and recalculation of unexecuted approvals. Advance plan-readiness warning is approved with configurable lead time. Exact defaults and remaining expiry edge cases are open.

## Approved additional reminders

- Eligible request left unclaimed: Operations team and its leadership.
- Claimed review delayed: responsible Operations specialist and leadership, using lower/higher warnings.
- Correction not resubmitted: responsible Project specialist and relevant Installation/Commissioning Leader.
- QA/Temperature approved but the next request not submitted: Project, after an agreed interval.
- Planned Cutover date passed without an execution outcome: Commissioning Leader before execution starts; responsible Operations specialist after it starts.
- Conditional approval awaiting follow-up: Operations, preserving release of Project responsibility after conditional Handover.

Confirmed lifecycle: completing the expected action removes the reminder from the active list while preserving its history. Merely reading/acknowledging the reminder does not resolve it. All approved reminders are visible in the relevant leadership consolidated filterable list. Exact threshold values and repetition remain open. The earlier ATP-to-plan deadline is superseded by plan-readiness tracking and ATP validity; adding a plan does not renew an approval.

Suggested list fields: router/site, stage, reason, responsible team/person, age, threshold, due time, severity and current status. Suggested filters: team, stage, project, province, person, reminder type and overdue status.

## Proposed enforcement and history requirements

- Revalidate current timing and policy when accepting submissions and claims, including after a policy change or from a stale screen.
- Preserve decisions/history; eligibility does not automatically claim or approve a request.
- Show textual waiting/eligible status and eligible-at time in addition to color.
- Keep eligibility waits, monitoring intervals, review warnings and missing-next-action reminders as distinct concepts.
- Suppress actionable unclaimed-work warnings while a request cannot yet be claimed; whether management also needs a waiting informational list remains open.
- Record configuration changes and reminder lifecycle events. Deduplication, repeat cadence and edge cases remain open; action-based resolution with history retention is confirmed above.
