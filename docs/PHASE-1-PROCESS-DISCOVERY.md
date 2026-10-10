# Phase 1 — Process Discovery Pack

## Purpose

Turn the project brief into explicit, testable workflows before implementation. The process names below are working hypotheses inferred from the brief and must be confirmed by the process owner.

## Discovery rules

- Do not infer permission to change router configuration from a request to register or track a router.
- Every process must identify its owner, trigger, inputs, states, rules, exceptions, outputs, audit events, and acceptance criteria.
- Ambiguous decisions are recorded as open questions instead of being hidden in code.
- A workflow is implementation-ready only after its owner validates the process map and acceptance criteria.

## Proposed five-process map

### P1 — Router onboarding request intake

**Trigger:** An authorized user needs a router added to the managed network inventory.

**Actors:** Requester, intake operator, process owner.

**Inputs:** Requester identity, project, center name, temporary router alias such as `GJNNN`, record date/time, installer identity, installation evidence, and attachments.

**States:** Draft → Submitted → Returned for correction → Accepted → Rejected → Cancelled.

**Rules to confirm:** Required fields, duplicate detection, allowed requester roles, attachment policy, and service-level target.

**Output:** A uniquely identified rollout item with a complete audit trail. The item initially has a QA alias and may not yet have a canonical router name.

### P2 — Request validation and completeness review

**Trigger:** A submitted request enters the validation queue.

**Actors:** Validator, process owner.

**Inputs:** P1 request, organizational records, validation checklist, and (when available) the canonical router name.

**States:** Queued → In review → Needs information → Validated → Invalid.

**Rules to confirm:** Validation checklist, evidence requirements, reassignment, due dates, and invalidation reasons.

**Output:** A validation decision and recorded reasons/evidence. The canonical name is assigned/validated in this stage and linked to the existing rollout item; a new item is not created.

### P3 — Technical and security approval

**Trigger:** A request passes completeness validation.

**Actors:** Technical reviewer, security reviewer, approver.

**Inputs:** Validated request, network placement, ownership, risk classification, implementation plan.

**States:** Pending review → Technical approved → Security approved → Approved → Rejected → Changes requested.

**Rules to confirm:** Separation of duties, approval thresholds, expiry of approvals, conflict handling, and escalation.

**Output:** A versioned approval decision. Approval alone does not authorize automated router mutation.

### P4 — Provisioning preparation and execution record

**Trigger:** An approved request is scheduled for implementation.

**Actors:** Implementation operator, technical owner.

**Inputs:** Approved request, implementation checklist, maintenance window, rollback plan.

**States:** Planned → Ready → In progress → Blocked → Completed → Rolled back → Failed.

**Rules to confirm:** Whether execution is manual or integrated, evidence required, start/finish timestamps, rollback criteria, and change-window controls.

**Output:** An execution record with evidence and a clear result. Direct router integration remains a separately approved capability.

### P5 — Closure, reporting, and audit review

**Trigger:** Execution reaches a terminal state or a review period expires.

**Actors:** Process owner, auditor, reporting user.

**Inputs:** Request history, validation and approval decisions, execution evidence, incidents.

**States:** Pending closure → Closed → Reopened for review → Archived.

**Rules to confirm:** Closure checklist, reopen authority, retention period, report filters, and export format.

**Output:** Closed record, audit history, operational metrics, and reportable data.

## Cross-process requirements

## Router identity continuity requirement

The same internal rollout item must be carried through all five processes. Stage 1 stores the temporary QA alias (for example `GJNNN`). Stage 2 adds the canonical router name (for example `BAGJXXX_GLNNNN`) and updates the current display name on that same item. The original alias and the name-change event remain available for audit, search, and reporting.

- Immutable audit events for state changes, decisions, assignments, and sensitive actions.
- Role-based access with least privilege and explicit denial behavior.
- Idempotent transitions and duplicate-submission protection.
- Server-side validation independent of the user interface.
- Time zone and timestamp policy suitable for the operating organization.
- Search, filtering, pagination, and export rules to be confirmed during UX design.

## Discovery workshop checklist

For each process, obtain answers to:

1. Who starts it and what event starts it?
2. What is the minimum valid input?
3. Which roles can view, edit, approve, execute, reopen, or export?
4. What are every allowed state transition and rejection reason?
5. What evidence is mandatory at each transition?
6. What happens on timeout, duplicate, failure, or partial completion?
7. What must be searchable, reportable, retained, or redacted?
8. What is explicitly outside the process boundary?

## Phase 1 exit criteria

- [ ] Process owner confirms the names and boundaries of P1–P5.
- [ ] Each process has an approved state model and transition table.
- [ ] Required fields and validation rules are listed.
- [ ] Roles and approval separation are confirmed.
- [ ] Exceptions and terminal outcomes are documented.
- [ ] The first vertical slice is selected from the backlog.
