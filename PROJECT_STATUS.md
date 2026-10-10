# Project Status

## Current phase

AUTHORITATIVE CHECKPOINT: user requested saving requirements to GitHub and continuing later. Read `docs/RESUME-HERE.md`. Conditional ATP permits Cutover. Conditional Handover completes transfer and releases Project; outstanding work belongs to an external team outside this system. A conditional-router register retains conditions and timed Operations reminders. Interval/recipients remain open. No application/container implementation or runtime test is complete. Earlier pending statements below are historical and superseded by this checkpoint.

Latest clarification: Project-team continuation mirrors Operations warning/acknowledgement. Weekly plans may omit executor; after Cutover starts only Operations records actions/results and actual executor changes. Failed attempts remain historical and may be replanned. Handover begins after successful Cutover plus 48 hours. Conditional ATP/Handover decisions are confirmed; downstream eligibility/ownership semantics await clarification.

Current update: Temperature re-observation starts on corrected-request resubmission. Second-Line continuation after warning/acknowledgement needs no manager approval. ATP correction-request sender and Project correction author are tracked separately from the claimant. Cutover planning and execution flow captured, with UI proposals pending validation. Discovery continues; no implementation/runtime tests performed.

**Phase 1 — Process discovery and form definition**

## Status

**Phase 1 detailed — QA form ready; awaiting next process details**

## Evidence reviewed

- `documentation/سند جامع پروژه.docx`
- `documentation/سند جامع پروژه.pdf`
- Existing GitHub repository: `deadeie/cutover`

## Confirmed baseline

- Domain: management and recording of the router-onboarding process.
- Runtime baseline: Python 3.11.
- Database baseline: PostgreSQL.
- Architecture: modular monolith with clear module ownership.
- Target: offline Linux VM, with a portable transfer bundle.
- Current repository state: documentation-first; no application implementation was present during review.
- Optional ATP router-check automation is now requested for design. Its integration/interface must be reviewed before implementation; automatic configuration changes remain outside scope.

## Initial risks and open decisions

| ID | Item | Impact | Owner | Status |
|---|---|---|---|---|
| R-001 | The five operational processes are not yet detailed enough to implement safely. | High | Process owner | Open |
| R-002 | Target Linux distribution and CPU architecture are not specified. | High | Infrastructure owner | Open |
| R-003 | Runtime container engine and offline transfer method are not specified. | High | Infrastructure owner | Open |
| R-004 | User roles, identity provider, and authentication method are not specified. | High | Product owner | Open |
| R-005 | UI delivery surface (web UI, API-only, or both) is not specified. | Medium | Product owner | Open |
| R-006 | PostgreSQL version and backup destination are not specified. | Medium | Infrastructure owner | Open |

## Validation required from user

Please validate:

1. The roadmap and phase gates.
2. The modular-monolith direction using Python 3.11 and PostgreSQL.
3. The offline Linux VM delivery constraint and Linux-compatible image build.
4. The decision to start with process discovery and UX before production code.

After validation, the next implementation step will be Phase 2: UX flows and technical design for the approved first vertical slice.

## Phase 1 evidence

- `docs/HANDOVER-REQUIREMENTS.md` — handover timing and ATP-style review.
- `docs/CONDITIONAL-APPROVALS.md` — confirmed capability versus proposed follow-up fields and open semantics.

- `docs/ATP-REQUIREMENTS.md` — ATP requirements and proposed claim recovery policy.
- `docs/CUTOVER-REQUIREMENTS.md` — daily/weekly schedule and execution model.

- `docs/TEMPERATURE-REQUIREMENTS.md` — current Temperature requirements; supersedes its earlier draft.
- `docs/ACTION-COMMENTS.md` — comments separated by stage/action/attempt.
- `docs/ROLE-MATRIX.md` — corrected Project roles and confirmed responsibilities.

- `docs/PHASE-1-PROCESS-DISCOVERY.md`
- `docs/CAPABILITY_BACKLOG.md`
- `docs/GLOSSARY.md`
- `docs/PROCESS-MODEL-V2.md`
- `docs/ROLE-MATRIX.md`
- `docs/ROUTER-IDENTITY-AND-NAMING.md`
- `docs/FORM-SPEC-STAGE-1-QA.md`
- `docs/FORM-SPEC-STAGE-2-TEMPERATURE-DRAFT.md`

## Phase 1 validation required

Please validate the revised organization model, five-stage workflow, role assignments, gating rules, timer behavior, and the recommended first vertical slice (C-001 through C-005). Please answer the open questions in `docs/PROCESS-MODEL-V2.md` in batches, starting with questions 1–10. Any corrections will be applied before Phase 2 UX and technical design.

## New process-owner input captured

- Stage 1 QA starts with a temporary alias such as `GJNNN`.
- Stage 2 Temperature assigns and validates the canonical router name on the same rollout item.
- Canonical naming has normal forms and province/topology/plane exceptions; these are documented in `docs/ROUTER-IDENTITY-AND-NAMING.md`.
- The naming rule still needs confirmation for RSG digit counts, QA alias uniqueness scope, and TH-specific lengths.
- Stage 1 QA form fields and acceptance criteria are documented.
- Stage 2 currently has a confirmed name-assignment portion and an explicit placeholder for the remaining Temperature fields.
