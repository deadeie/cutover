# Capability Backlog — Initial Prioritization

Priority uses **P0** for the first vertical slice, **P1** for the first release, and **P2** for later increments.

| ID | Capability | Priority | Depends on | Acceptance signal |
|---|---|---:|---|---|
| C-001 | Create and submit onboarding request | P0 | P1 process confirmation, roles | Valid request receives an ID and audit event |
| C-002 | Request completeness validation queue | P0 | C-001 | Validator can accept, return, or invalidate with reason |
| C-003 | State transition and audit framework | P0 | Domain model | Invalid transitions are rejected and every valid transition is traceable |
| C-004 | Role and permission enforcement | P0 | Role decisions | Unauthorized reads and writes are denied and audited |
| C-005 | PostgreSQL migrations and repository layer | P0 | Technical design | Clean database can be created and migrated deterministically |
| C-006 | Request search, filtering, and detail view | P1 | C-001, UX design | Authorized users can find and inspect records |
| C-007 | Technical/security approval workflow | P1 | P3 confirmation, C-003, C-004 | Approval decisions are separated, versioned, and auditable |
| C-008 | Execution record and rollback evidence | P1 | P4 confirmation | Manual or integrated execution is recorded without hidden side effects |
| C-009 | Closure and reopen workflow | P1 | P5 confirmation | Closed records follow retention and reopen rules |
| C-010 | Operational reports and export | P1 | C-006, P5 confirmation | Authorized users can generate reproducible reports |
| C-011 | Offline container packaging | P1 | Runtime foundation | Bundle installs and runs without internet |
| C-012 | Router read-only integration | P2 | Explicit scope and authorization | Approved read-only operations are isolated and audited |
| C-013 | Router configuration mutation | P2 | Separate security/design approval | No implementation until explicit authorization and rollback are approved |

## Recommended first vertical slice

Implement C-001 through C-005 as one thin slice. It validates the domain model, authentication boundary, database migrations, state transitions, audit events, and local container runtime without requiring router access.

## Prioritization risks

- P1–P5 names and boundaries are provisional.
- Authentication and identity integration are not specified.
- Target Linux distribution, CPU architecture, and container engine are not specified.
- Approval roles and separation-of-duties rules require process-owner input.
