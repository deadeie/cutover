# Form Specification — Stage 1: Installation QA

## Purpose

Allow the Project Team's Installation Specialist to report that a router has been installed and request Network Operations review.

## Actors

- **Submitter:** Project Team — Installation Specialist.
- **Reviewer:** Network Operations — Second-Line Specialist.
- **Administrator:** Operations Manager, for field, role, timer, and rule configuration.

## Record identity

The form creates one `rollout_item` and one Stage 1 request. It does not create a separate record for later stages.

| Field | Required | Source | Rule |
|---|---:|---|---|
| Request ID | System | System | Immutable, human-readable identifier |
| Project | Yes | Project catalog | Must reference an approved project, e.g. `Phase 5` |
| Project router item | Yes | Project scope | Must belong to the selected project |
| Center name | Yes | Submitter / site catalog | Must be linked to the project site where possible |
| QA alias | Yes | Submitter | Initial short form such as `GJNNN`; no canonical router name required |
| Record date/time | Yes | System | Server timestamp; display user time zone according to policy |
| Created by | Yes | System | Authenticated user identity |
| Installation Specialist | Yes | User/team directory | Must be a Project Team installation role |
| Installation evidence | Configurable | Submitter | Required items are defined by the QA checklist |
| Comment | Configurable | Submitter | Free text subject to length and sensitive-data rules |

The project, project-router item, center, and any planned router model should be prefilled when the project has already defined them. The final router name is intentionally absent at this stage.

## QA alias validation

- Normalize only the configured safe transformations, such as trimming surrounding whitespace and applying uppercase.
- Validate against the active alias rule for the selected province/area.
- Do not infer a canonical router name from the alias.
- Enforce the configured uniqueness scope and show a clear duplicate warning.
- Preserve the original submitted value in audit history if normalization changes the display value.

## Stage 1 state machine

```text
Draft
  → Submitted
  → In review
  → Approved → Stage 2 becomes eligible
  → Changes requested → Draft/Resubmitted
  → Rejected → terminal unless reopened by policy
  → Cancelled → terminal
```

## Review actions

Confirmed: Second-Line Operations approves or rejects; rejection requires a reason. Every action supports a separately stored comment linked to that action. Other actions below are design proposals pending confirmation.

The Network Operations reviewer can:

- Approve the QA request.
- Request changes with one or more reasons.
- Reject with a mandatory reason.
- Add review evidence or comments.
- Reassign the review if permitted by policy.

The reviewer cannot change the submitter's data silently. Any correction uses a recorded revision or returns the request for correction.

## Acceptance criteria

1. A permitted Installation Specialist can create a draft for a project router item.
2. The form requires center name and QA alias before submission.
3. The system records request ID, creator, and server timestamp automatically.
4. A submitted request enters the configured Network Operations review queue.
5. Approval makes Stage 2 eligible only after any configured dependency/time rule is satisfied.
6. Rejection or change request requires a reason and keeps the same rollout item identity.
7. The system preserves the QA alias when the canonical name is added later.
8. All state changes, comments, evidence, and decisions are auditable.

## Pending decisions

- Exact QA checklist and mandatory evidence.
- QA alias digit count, leading-zero policy, and uniqueness scope.
- Reassignment rules; the normal reviewer is confirmed as Second-Line Operations.
- Whether rejection is terminal or can be reopened.
- Minimum delay from Stage 1 approval to Stage 2 submission.
