# Cutover plan creation proposal

Status: user approved this approach for initial implementation and wants its practical issues discovered during use. Pre-QA planned items are active in the first release when they belong to the approved project scope. The Commissioning Leader creates weekly Cutover plans; daily planning is not a Project-leader activity. Keep the confirmed distinction between the rollout project defined by Design and the weekly Cutover plan managed by the Commissioning Leader.

## Existing confirmed context

- A Project has an intended router scope; Design defines rollout projects, with the detailed manager/specialist approval split still open.
- Commissioning Leader manages weekly Cutover plans for assigned projects. A weekly plan contains dated rows and optional daily/time-window placement; the leader does not create a separate daily plan. Planning may precede Temperature/ATP readiness; current prerequisites gate execution, not membership in a plan.
- QA may have only site code and center; the canonical name is assigned at Temperature. Multiple routers at one site have separate identities.
- A weekly plan may omit the planned executor. Actual Project executor and recording Operations specialist remain separately attributable.

## Recommended source of plan rows

Use a single project router list with stable internal identities, rather than free-text names copied into plans. Existing rollout records are selected directly. Pre-QA planned items are approved for the first release within project scope; authoring/import authority and the scope-addition approver remain to be defined.

Proposed initial planned-item fields: project, province, center, site code if known, topology and A/B where applicable/known, and planned model if known. Final name and OM IP are not required for pre-QA planning. Display missing fields explicitly; do not fabricate values or mark work complete.

## Proposed user flow

1. Leader selects an assigned project and creates a weekly plan with its week, timezone and optional daily/time-window placement for each row.
2. Choose Add from project router list. Filter by province, center, topology and progress; show QA/Temperature/ATP readiness and current/planned ATP validity next to each item.
3. Select rows, set their planned time/order and optionally assign the Project executor. Pending readiness is visible but does not prevent planning.
4. If a router is missing, use a governed Add planned item flow, or request its addition from the project-scope owner. Do not silently create a duplicate actual router from free-text plan entry. Role authority and optional bulk import remain open.
5. Save/publish the weekly plan under the future publication policy. Track readiness and reminders against each row's planned date/time. Publishing does not approve prerequisites or automatically submit QA/Temperature/ATP. Changing a row's day or time creates a revision/history entry; it does not create a new plan.
6. When QA begins, reference the selected planned item and create its QA request while retaining the same identity; later Temperature assigns its canonical name. This approved approach supersedes earlier assumptions that QA always creates a new item. Existing QA records are linked/selected, not recreated.
7. Each actual Cutover attempt rechecks current eligibility. Failed/replanned attempts preserve old records and use the same router identity in the new plan/attempt.

## Proposed consistency rules

- A site is not a router key. Preserve the confirmed warning and explicit second-router/plane/topology distinction even when planned items are introduced.
- Prevent accidental duplicate active plan rows for the same router/time window; show its existing plan and use explicit rescheduling with history.
- Completed/handed-over records are not ordinary candidates for a new initial Cutover. Any later maintenance/re-Cutover is outside the current onboarding flow unless separately specified.
- The plan row stores a reference, not an independently editable router identity. Name assignment updates the current display while historical events retain their context.
- Keep approved project scope totals and later additions/cancellations versioned for progress reporting. Adding a dated plan must not silently alter the project baseline.

## Decisions needed

- Pre-QA planning is confirmed; candidates need not already have QA records.
- Who may add/import pre-QA items, and who approves additions to the Design-defined project scope?
- Which initial fields are reliably known, and is an existing spreadsheet/list available as a future import source?
- Define weekly-plan publication, row changes after publication and cancellation roles in the UX/permission phase.
