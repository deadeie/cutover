# Management reporting proposal

Status: management reports are requested; specific reports, metrics and visualizations below are proposals for review. No reports, graphs, application code or export files have been implemented. Existing filterable leadership reminder lists remain confirmed separately.

## Confirmed scope and access direction

- Project progress by province is required for the first release.
- Leaders require a management dashboard showing each person's workload and performance, including completed work and work in progress. The detailed metrics below are proposed for agreement, not an approved scoring formula.
- Each person must have a personal workspace showing their own ongoing and completed tasks. Include items awaiting another team/person separately so personal responsibility is not confused with dependency waiting.
- Live network status and continuous network monitoring are outside this system's scope. Reports use recorded workflow events, decisions, plans, configuration and logical router relationships.
- Confirmed: Operations Leader views reports/status across all projects and provinces; Project Leader views assigned projects only and manages plans within that responsibility. Viewing all projects does not grant Operations Leader permission to edit Project plans or bypass process rules. See `ROLE-MATRIX.md`; unspecified export/assignment permissions remain open.
- Future automation-assisted ATP checks remain a distinct deferred capability; this reporting scope does not introduce or implement live monitoring.

## Proposed first-release reports

| Report | Decision supported | Main contents |
|---|---|---|
| Cutover plan readiness | Which planned routers need attention before their execution window? | Plan/date, province, router, QA/Temperature status, ATP decision and current expiry, expected validity at planned start, blocker, responsible team/person and time remaining |
| Plan delivery and outcomes | What was planned, executed, delayed or unsuccessful? | Planned routers, started/completed/failed attempts, overdue/no-result rows, reschedules and recorded reasons; preserve original plan and revisions |
| Project progress by province (required) | Where does rollout stand and where is it delayed? | Router counts by current stage/state, full versus conditional Handover, waiting age and outstanding next action; percentage only with a defined scope denominator |
| Personnel workload and performance (required dashboard; metric details proposed) | Who is handling work, what have they completed and where is the load concentrated? | Current assigned/claimed load, completed actions/reviews in the selected period, corrections, waiting dependencies, overdue work and stage-specific elapsed times; drill-down to the actual records |
| Work queues and delays | Which team needs to act and why is work waiting? | Eligible-unclaimed, claimed, returned-for-correction, pending Project action; waiting duration, actual actors and handovers, required observation separated from actionable delay |
| ATP validity and renewal | Which approvals threaten upcoming Cutover? | Valid, near-expiry, expired and renewal-in-progress records, conditional decisions, approvals without a plan, plan-date conflicts and renewal history |
| Conditional decisions and unresolved conditions | Which conditions still need follow-up after acceptance/delivery? | ATP/Handover decision, condition, responsible follow-up, age, reminder status and action history; conditional Handover is completed delivery with open conditions, not unfinished Project work |
| Router/site and RSG inventory | What equipment belongs to each province/site/RSG pair? | Site, immutable router identity, full name or QA code, topology, A/B role, OM IP, group/range, model and workflow state; distinguish installed site count from router count |

An individual router's event timeline is a detail view for these reports: submissions, claims, corrections, decisions, ATP renewals, Cutover attempts, Handover and configuration references.

## Personnel dashboard — proposed measures

| Measure | Proposed meaning |
|---|---|
| In progress now | Active tasks currently attributable to that person, by team/stage and current responsibility |
| Completed in period | Work/review attempts completed by that actual actor during the chosen period; approvals, conditional decisions and returns for correction shown separately |
| Waiting on another party | Tasks the person previously handled but which now require another team or person; do not mislabel them as their active backlog |
| Overdue actionable work | Tasks exceeding the agreed response/correction deadline while that person is responsible; exclude mandatory observation/eligibility waits |
| Review/correction elapsed time | Time under the relevant responsibility interval; show required waits and returned-to-other-team time separately. This is not measured hands-on labor time |
| Correction cycles | Number and reasons of return/resubmission cycles; distinguish who sent findings from who corrected them, without assuming who caused the underlying issue |
| Throughput trend | Weekly/monthly completed work by stage and role, with counts of unique routers separate from attempts/actions |

- First/previous claimant, actual reviewer, Project correction author, actual Cutover executor and Operations recorder are distinct actors; a takeover must not give the final person credit for every prior action.
- A return for correction is completed review work but not completion/approval of the stage. Present those counts separately.
- Include tasks active before the reporting period in the current workload snapshot; completed-in-period and as-of-now counters use different explicit time definitions.
- Compare like stages/roles and display volume, delays and dependencies together. An overall performance score/ranking is not yet specified; no invented weights or inference from login duration.
- Operations Leader's confirmed global scope applies; Project Leader sees activity within assigned projects only, including only those activities when a person works across projects.
- Any future assignment suggestion based on workload is separate from the report; it must not automatically assign/reassign tasks.

## Personal workspace — required first-release view

- **Ongoing:** tasks currently assigned or actively claimed by the user, grouped by stage and urgency.
- **Completed:** the user's completed actions and decisions, with date, stage, outcome and router link.
- **Waiting:** tasks the user submitted or owns where the next action belongs to another team/person; show the dependency and last action.
- **Returned for correction:** items requiring the user/team to respond, with findings, due/reminder state and resubmission action.
- **Upcoming/assigned:** planned Cutover rows or other future work assigned to the user, separated from active work.
- **History:** searchable actions performed by the user, without rewriting the original actor when another person continues the work.

The workspace should open the exact task or router detail, show why an item is waiting or blocked, and distinguish required eligibility/observation time from overdue personal work. A user sees only records permitted by their role and project scope; Operations Leader's global visibility and Project Leader's assigned-project scope remain in force.

## Proposed common behavior

- Filters: date window, project, province, site, RSG group, topology, stage/status, team/person, conditional state, ATP validity and reminder severity where applicable.
- Date semantics must be explicit: planned execution date, approval date, completion date and snapshot time are not interchangeable.
- Show report generation/as-of time. Support historical reports from recorded events rather than rewriting past status when current settings change.
- Allow summary counts to open the exact underlying router/task/attempt rows, then the relevant detail record.
- Provide saved filters and tabular exports, with Excel/CSV as first candidates. PDF/print layouts can be considered later. No export formats are confirmed yet.
- Scope report rows and exports by authorized role/team/project/province; exact access matrix needs approval. Leadership alone does not imply universal access.
- Show the actual responsible team/person and evidence for delay; do not infer individual performance solely from closure counts or total request age.

## Metric definitions to agree before implementation

- Project completion: use delivered routers divided by defined in-scope routers; define cancelled/out-of-scope handling. Full and conditional Handover both count as delivered under the confirmed lifecycle, shown separately.
- Count router records, unique sites, task attempts and Cutover attempts separately. Two routers at a site and repeated ATP reviews must not inflate unique-router progress.
- Time to claim starts when a request becomes claim-eligible. Required waits/Temperature observation are separate from overdue operational work.
- Time in Operations and time returned to Project should be distinguishable from end-to-end elapsed time; timer stop/pause policies remain open.
- Plan adherence must specify original schedule versus latest revised schedule. Rescheduling should not silently erase missed commitments.
- Cutover success rate must state whether the denominator is attempts or unique routers; retries are separate attempts.
- ATP validity reports reflect current confirmed policy and preserve historical approval/expiry events. Increasing duration cannot revive an already expired approval; its renewal task remains required.

## Proposed later visualizations

1. Stage/state distribution by project and province, with selectable breakdowns.
2. Planned versus completed Cutover trend by day/week, with failures and reschedules separately visible.
3. Distribution of eligible-unclaimed age, review time and correction time by stage/team; aggregate summaries link to source rows.
4. Timeline of upcoming Cutover windows alongside ATP expiry, highlighting readiness conflicts.
5. Logical province -> RSG pair -> ASG/CSG graph with workflow/validity badges and router drill-down.

The logical graph reflects configured range/group relationships and recorded workflow status only. Live link status, traffic/health monitoring and discovered physical topology are outside the system's scope and are not proposed reporting features. Graph scope across provinces follows the final RSG-grouping decision.

## Data/history needed to support later reports

Propose retaining stable router/site/group identity, plan revisions, actual stage/action timestamps, active responsibility intervals, decision/condition/renewal history and policy changes from the first release. Use real records; do not manufacture missing historical baselines. Detailed schema and storage choices remain deferred to technical design.

## Review questions

- Which proposed reports are required for release one, and which should follow later?
- Provincial project progress and the personnel workload/performance dashboard are required. Confirm detailed personnel measures, whether any score is desired, and remaining report priorities.
- Define manager scopes, project assignment/delegation and export details separately. Operations Leader global visibility and Project Leader assigned-project visibility/plan management are already confirmed.
- Is project scope (planned total routers) already maintained, so a reliable completion percentage can be defined?
- Are Excel/CSV exports needed initially, and are saved filters sufficient before scheduled/email reporting is considered?
