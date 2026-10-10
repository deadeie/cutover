# Conditional ATP and Handover approvals

## Confirmed requirements

Second-Line Operations may approve ATP or Handover conditionally in exceptional situations. These decisions must be visibly distinct, attributable and independently referenceable.

## Proposed representation

- Decision ID, router ID, stage, review attempt, approving user/role, timestamp and decision type CONDITIONAL_APPROVAL.
- Condition descriptions and references to unresolved findings, with a separate action comment.
- Display a dedicated conditional badge in router details, schedules, queues and reports; do not render a normal green full-approval badge.
- Suggested follow-up fields: responsible person, due date if applicable, evidence, follow-up status and resolving reviewer. These are proposals, not confirmed mandatory fields.
- Resolving a condition creates a new event; preserve the original conditional decision and its conditions.

## Confirmed progression and ownership

- Conditional ATP permits Cutover while retaining its conditions and distinct status.
- Conditional Handover completes handover and removes responsibility from the Project Team. A different team handles remaining conditions outside this system; do not create roles or a task workflow for that external team.
- Maintain a dedicated conditional-router register, linked to the router, stage decision, unresolved conditions and history. Handover completion must not remove the router from this register.
- Provide a configurable follow-up interval. When it elapses, notify Network Operations about that router and its conditions. A reminder does not reopen Project work or revoke handover automatically.

## Proposed register and reminder design

- Columns: router, province, project, ATP/Handover conditional decision, conditions, approval time/person, next reminder, overdue status and latest Operations follow-up.
- Keep handover lifecycle status separate from condition-follow-up status.
- Proposed timer anchor: conditional decision time plus configured interval; exact interval, anchor, recipients and repetition policy remain to be chosen.
- Record reminder events and acknowledgements per router/condition. Persist due times and deduplicate delivery after restart; operate without external internet services.
- Operations may record follow-up notes and external reference numbers. Who may mark conditions resolved, and required evidence, remain open.
- The register includes conditional ATP and Handover records; preserve both when a router has both decisions.
