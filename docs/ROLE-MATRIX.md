# Roles and confirmed responsibilities

Status: requirements discovery; no permission implementation yet.

## Confirmed leadership access direction

- Operations Leader must have broader access in this system than Project Leader.
- Confirmed scope: Operations Leader can view reports and workflow status across all projects and provinces. Project Leader can view only assigned projects and manage plans within that responsibility, preserving the existing Installation/Commissioning role split.
- Preserve existing task ownership and action permissions: Operations Manager defines/approves OM ranges; Operations Leader configures ATP validity; Project leadership manages Cutover plans under its assigned responsibility. System Administrator remains a separate role and Super Admin exceptions remain deferred.

## Leadership access: confirmed scope and remaining details

| Capability | Operations Leader | Project Leader |
|---|---|---|
| Reports and workflow visibility | All projects/provinces and relevant queues of both teams | Assigned projects and the status of their Operations reviews |
| Cutover plans | View all plans and readiness/blockers | Create/manage plans within assigned Project responsibility; preserve separate Installation/Commissioning roles |
| Operational policies | Existing confirmed inter-stage timing and ATP validity authority; other warning settings to be finalized | Project follow-up settings only where separately authorized; do not transfer Project Manager settings automatically |
| Follow-up | Operations backlog and Project-side blockers affecting readiness | Project work and returned corrections within assigned scope |
| Exports and drill-down (proposed implementation detail) | Same authorized row scope as reports | Same authorized row scope as reports |

Global Operations Leader visibility and assigned-project Project Leader visibility/plan management are confirmed. Broader visibility does not automatically permit editing Project plans, performing specialist approvals, overriding prerequisites or approving new ranges. Export availability, the assignment/delegation mechanism and other unspecified permissions remain open.

## Previously confirmed responsibilities

Latest authority corrections: Operations Manager defines/approves new OM ranges with mandatory RSG-group linkage at creation. Operations Leader configures ATP validity duration. ATP expiry informs both Project and Operations Leaders. This supersedes the earlier Project-Leader-configured ATP-to-plan reminder interpretation below. Cutover-plan readiness is Project's concern; approved ATP without a plan is Operations' concern.

Latest 2026-10-11 clarification supersedes conflicting assignments below: System Administrator is a separate role from Operations Manager. Operations Manager AND Operations Leader may configure system-wide inter-stage waits and submission/claim modes for QA, Temperature, ATP and Handover. Project Manager configures reminders for Cutover without a Handover request; Operations Leader configures ATP validity; expiry creates Operations renewal work and informs both leaders. The earlier Project-owned ATP-to-plan deadline is superseded. QA and Temperature inherit the Operations claim/review approach. Submitted tasks concern Operations; returned corrections concern Project. Leadership reminders are a filterable consolidated list. Super Admin exception powers are deferred, not granted. See `SHARED-REQUEST-WORKFLOW.md`.

| Group | Roles |
|---|---|
| Design | Manager; Specialist |
| Project | Project Manager; Installation Leader; Commissioning Leader; Installation Specialist; Commissioning Specialist |
| Network Operations | Manager; Leader; First-Line Specialist; Second-Line Specialist |

| Activity | Confirmed responsibility | Still to define |
|---|---|---|
| Define policy and rollout projects | Design Team | Manager/specialist approval split |
| Submit QA | Installation Specialist | Assignment and delegation |
| Approve/reject QA | Second-Line Operations Specialist; rejection requires reason | Reassignment |
| Submit Temperature | Commissioning Specialist | Assignment and delegation |
| Monitor temperature, CPU, fan for 48 hours and check monitoring connectivity | Network Operations | Monitoring method and thresholds |
| Approve/return Temperature | Second-Line Operations Specialist | Resubmission timer policy |
| Correct Temperature problems | Project Team and the original requesting specialist | Escalation |
| ATP submission | Project Commissioning Specialist | Checklist |
| ATP claim, review and decision | One Second-Line Operations Specialist | Reassignment and resubmission rules |
| Cutover planning | Commissioning Leader assigns the Project execution person and publishes daily/weekly plans | Window and publication rules |
| Cutover pre-check | First-Line or Second-Line Operations confirms ATP readiness | Exact checklist |
| Cutover execution | Project person performs with Operations; only First-/Second-Line Operations records actions/results after start and can change actual Project executor with history | Detailed checks |
| Cutover post-check | First-Line or Second-Line Operations checks result | Manual/automation criteria |
| Handover requests | Commissioning Specialist after successful Cutover plus 48 hours | Checklist |
| Handover claim/review | Second-Line Operations, ATP-style correction and continuation | Conditional decision effect |
| Conditional ATP/Handover approval | Second-Line Operations | Progression and ownership implications |
| Joint Cutover | Project and Operations; First-Line Operations generally participates | Exact responsibilities |
| Workflow configuration and router hardware catalog | Operations Manager | Delegation |
| Province naming codes and OM networks | Administrator configuration requested | Delegation |

Installation and commissioning leaders are distinct roles. Leadership does not automatically grant review, approval, or override permissions. The earlier speculative RACI matrix is superseded by these confirmed assignments; other permissions remain undecided.
