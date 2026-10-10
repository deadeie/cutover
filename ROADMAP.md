# Cutover Project Roadmap

## Product intent

Build a modular system for managing and recording the router-onboarding process. The first release will model the workflow, roles, inputs, states, validation, audit history, and reporting. Direct router access or configuration changes remain out of scope until requirements and explicit authorization are approved.

## Delivery constraints

- Python 3.11 application baseline.
- PostgreSQL persistence.
- Modular monolith architecture with explicit module boundaries.
- Development on Windows; target execution on an offline Linux VM.
- No runtime dependency on public package registries, cloud services, CDNs, or internet access.
- Every capability must include requirements, acceptance criteria, tests, versioned documentation, and a change record.
- Secrets must never be committed to Git or included in the transfer bundle.

## Phases and approval gates

| Phase | Scope | Main outputs | Gate |
|---|---|---|---|
| 0. Foundation and governance | Repository, decisions, status tracking, container strategy, offline constraints | Project skeleton, roadmap, ADRs, status and change log | User validates roadmap and assumptions |
| 1. Process discovery | Model the five router-onboarding processes, actors, triggers, inputs, states, rules, exceptions, and outputs | Process maps, glossary, prioritized capability backlog | Process owners validate workflows |
| 2. Product and UX design | Roles, permissions, information architecture, forms, work queues, detail views, reports, error states | UX flows, wireframes, UI contract, accessibility notes | User validates UX direction |
| 3. Technical design | Domain model, PostgreSQL schema, API boundaries, audit model, migration policy, security decisions | Data model, API contract, ADRs, migration plan | Technical design review |
| 4. Runtime foundation | Python service, configuration, logging, health checks, PostgreSQL integration, migrations, test harness | Running local container stack, smoke tests | Local foundation validation |
| 5. Vertical slice | Implement one approved router-onboarding process end to end | First usable workflow with persistence, validation, audit, and UI/API | Acceptance test pass |
| 6. Capability increments | Implement remaining capabilities in small slices with tests and docs | Versioned releases and migration notes | Per-capability approval |
| 7. Offline packaging | Build Linux-compatible image and transfer bundle in an equivalent Linux build environment | Image archive, checksums, manifest, install/rollback guide | Offline installation test |
| 8. Release and operations | Clean-VM install, backup/restore, monitoring, incident and rollback procedures | Release candidate, runbook, handover package | Final release approval |

## Phase 0 work items

- [ ] Record source-document findings and assumptions.
- [ ] Establish repository documentation structure.
- [ ] Define the container and offline-transfer strategy.
- [ ] Define the local validation contract.
- [ ] Record unresolved decisions and owners.
- [ ] Obtain user approval before implementation begins.

## Proposed repository layout

```text
src/                 application code and modules
tests/               unit, integration, workflow, and packaging tests
migrations/          versioned database migrations
config/              documented configuration templates
scripts/             build, test, package, and offline-install tools
docs/                requirements, architecture, UX, ADRs, operations
docker/              Dockerfile and compose files
artifacts/           local build outputs; never commit secrets
```

## Definition of done for every capability

1. Requirement and workflow are documented.
2. Roles, inputs, states, rules, exceptions, and outputs are explicit.
3. Data changes have a reversible migration.
4. Unit and integration tests exist; workflow acceptance tests cover the criteria.
5. Audit events and error behavior are defined.
6. UX states include loading, empty, validation error, permission denied, and success.
7. The capability runs in the local container stack.
8. Change history and release notes are updated.

## Approval protocol

The implementation proceeds one phase at a time. At the end of each phase, `PROJECT_STATUS.md` records evidence, validation results, open risks, and the exact approval needed before the next phase starts.
