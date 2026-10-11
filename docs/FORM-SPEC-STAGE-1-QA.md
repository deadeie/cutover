# Form Specification — Stage 1: Installation QA

## Purpose

Confirmed follow-up: QA is immediately submit/claim eligible once installation completion is reported; no prior-stage delay is required. If the site code already has a recorded router, warn the submitter and allow explicit confirmation that this is a second router at the same center. If both are being installed together, create two separate QA requests and ask the second submitter whether that router is A or B. Project knows whether two routers are planned. Full names are assigned separately at Temperature. Confirmed follow-up: explicitly confirm the first simultaneous request's plane when assigning A/B to the second; do not infer it silently. Same-site ASG/CSG may be distinguished by topology selected at QA. Existing correction cycles remain on the original request rather than creating an additional router.

Latest clarification (2026-10-11): QA uses the shared Operations queue, claim/review and acknowledged-continuation workflow in `SHARED-REQUEST-WORKFLOW.md`. QA alias is the site code, potentially shared by multiple routers at the same site; the confirmed per-router plane/topology distinction is described above. Operations coordinates a checklist with an external provincial contact and Second-Line records the outcome. Photo/checklist features are deferred; no mandatory in-app evidence upload is required. See `MANUAL-CHECKS-AND-FUTURE-INTEGRATION.md` and the latest naming clarification.

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
  → Rejected / returned for correction → corrected resubmission on the same item
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

- Structured checklists/photos are future features; no mandatory in-app evidence upload for the initial release.
- QA site-code format, leading zeroes and shared-site identity are confirmed in `ROUTER-IDENTITY-AND-NAMING.md`.
- Reassignment rules; the normal reviewer is confirmed as Second-Line Operations.
- Rejection returns the request for correction (confirmed); no terminal rejection inferred.
- Resolved: no delay from QA approval to Temperature submission/claim; observation remains a separate Temperature requirement.
