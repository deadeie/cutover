# UX Phase 2 foundation

Status: UX contract plus a clickable desktop demo at `../prototypes/demo/index.html`. The demo uses fictitious local data and is not a connected application. It covers the main system destinations; unresolved business decisions remain visibly marked.

## Product navigation

The first release uses a role-aware navigation shell with these destinations:

1. **My workspace** — every user starts with their personal work.
2. **Project plans** — weekly Cutover plans available within the user's project scope.
3. **Operations queues** — QA, Temperature, ATP, Handover and ATP renewal tasks for eligible Operations users.
4. **Management** — reports, provincial progress and personnel workload for authorized leaders/managers.
5. **Routers and projects** — searchable records and detail views within role scope.
6. **Administration** — only the configured administration roles see policy, catalog, province and OM-range settings.

The navigation must show the user's current role and active project scope. A wider Operations Leader view must not silently grant specialist approval or Project-plan editing actions.

## Page 1 — My workspace

This is the default landing page for every authenticated user.

### Sections

- **Ongoing:** active tasks assigned or claimed by the user.
- **Needs my action:** returned corrections, requested submissions or overdue actions.
- **Waiting on others:** the user's item is pending another team/person, with the dependency and last action shown.
- **Upcoming:** assigned future work and weekly Cutover rows.
- **Completed:** the user's completed actions and decisions, filterable by period, stage and outcome.

### Required behavior

- Separate mandatory eligibility/observation time from overdue personal work.
- Show stage, router/site, project, current owner, due/eligible time, severity and next action.
- Open the exact task or router detail from every row.
- Reading or acknowledging an item does not resolve it. Completing the expected action removes it from the active section and preserves its history.
- A person who continued someone else's work sees their own action in history; the original actor remains unchanged.

## Page 2 — Weekly Cutover plan

The Commissioning Leader creates one weekly plan for an assigned project. Individual rows may have a day and time window within that week; a separate daily Project plan is not created.

See `UX-WEEKLY-CUTOVER-WIREFRAME.md` for the Persian text wireframe, shared board/table behavior, pre-QA identity, readiness and acceptance scenarios. Approved layout choices and proposed interactions are labeled separately.

### Plan header

- Project, week, timezone, plan status and revision.
- Created/published by and timestamps.
- Counts for planned, ready, blocked, in progress, completed and failed rows.
- Warning banner when any row has incomplete Temperature, expired/expiring ATP or another execution blocker.

### Row table/board

Each row displays project router identity, province/site, optional topology/A-B, planned day/time, planned Cutover executor, Operations participant, QA/Temperature/ATP badges, ATP valid-until and readiness blocker. The Commissioning Leader assigns a planned executor to every router before publishing; this assignment is only for Cutover. QA, Temperature, ATP and Handover responsibility follows its independent task assignment/claim flow. Operations records the actual Cutover executor and may record a different person while retaining the planned assignment.

The leader selects existing project router records. A pre-QA planned item may be selected only if the approved project-scope workflow supports it; adding a new router outside project scope requires separate approval. Do not create duplicate router records when QA or the canonical name is later recorded.

### Actions

- Add from project router list.
- Add an approved in-scope planned item before QA; this is enabled in release one.
- Set/revise row day, time, order and required planned Cutover executor.
- Publish, revise, cancel or archive according to the future permission policy.
- Open router details and readiness blockers.

Publishing never approves QA/Temperature/ATP or starts Cutover. Before execution, Operations rechecks current prerequisites and ATP validity.

## Page 3 — Operations queues

Operations users see separate tabs or saved filters for QA, Temperature, ATP, Handover and ATP renewal. Each request is a complete task card/row, not a hidden substep of a Project screen.

### Queue row

- Stage, router/site, project/province and current canonical/QA identity.
- Eligibility state: waiting, claimable, claimed, returned or completed.
- Waiting-until/eligible-at time, observation completion where relevant and claim age.
- Current claimant, previous claimant(s), latest correction sender and next action.
- Full/conditional decision, ATP validity and blocking reason.

### Interaction rules

- Claim is server-validated; a waiting item cannot be claimed even if a stale screen shows it as available.
- A colleague continuing another person's work sees a warning and must acknowledge it with a reason.
- QA/Temperature use the same claim/review/correction pattern as ATP/Handover.
- A return sends the actionable item to Project; resubmission returns it to Operations while preserving attempts and comments.
- Expired ATP automatically creates a renewal task. Renewal is claimed and reviewed in this queue; it does not restart QA/Temperature automatically.

## Page 4 — Management dashboard

### Top-level cards

- Project progress by province.
- Weekly Cutover readiness and execution outcomes.
- ATP valid, near expiry, expired and renewal-in-progress.
- Queue age and correction backlog by stage/team.
- Personnel workload: ongoing, completed, waiting, overdue and correction work.

### Filters

Date/as-of time, project, province, site, RSG group, topology, stage, status, team, person, conditional state, ATP validity and reminder severity.

Operations Leader sees all projects/provinces. Project Leader sees assigned projects and manages plans within that scope. Exact manager scopes, exports and delegation remain to be finalized.

### Performance safeguards

- Show volume, delay and dependency together; do not create an unexplained overall score.
- Count unique routers, sites, attempts and actions separately.
- Separate required waiting/observation from actionable delay.
- Attribute each action to its actual actor; a takeover does not transfer earlier credit.
- Every aggregate opens its underlying records and their event history.

## Page 5 — Router detail

The router detail page is the shared drill-down target from all four primary pages.

- Identity: immutable rollout ID, site code, canonical name, topology, A/B, province, center, model, OM IP and RSG group/range.
- Stage timeline: QA, Temperature, ATP, Cutover and Handover states.
- Plan history: current and prior weekly plan rows, revisions and outcomes.
- Validity/readiness: Temperature observation, ATP decision/conditions/valid-until, blockers and renewal tasks.
- Responsibility: current owner, actual actors, continuation/takeover history and next action.
- Audit timeline: comments, decisions, corrections, reminders, policy references and timestamps.

## Shared states and accessibility

Every list/detail page needs explicit loading, empty, waiting, blocked, permission-denied, validation-error, conflict/stale-data and success states. Color is supplementary: waiting and conditional states must include text, icon/label and reason. Keyboard navigation, readable contrast and non-color status indicators are required design constraints.

## Confirmed UX decisions

- Weekly board is the primary planning view; a synchronized table provides filtering, sorting and detail editing. Both operate on the same plan and router rows.

- Pre-QA planned items are active in the first release. They must come from the approved project scope; adding a router outside that scope remains a separate approval flow.

## Open UX decisions

- Who approves additions to the approved project scope.
- Exact status names and colors for waiting/claimable/conditional/expired.
- Which report exports are available initially.
- Assignment/delegation flows and manager scopes.
- RHEL deployment, authentication and technical design are later phases, not UX blockers.
