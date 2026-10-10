# Project Status

## Current phase

**Phase 0 — Foundation and governance**

## Status

**Awaiting user validation**

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
- Direct router connection/configuration is a future capability requiring separate analysis and approval.

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

After validation, the next implementation step will be Phase 1: create the process-discovery pack and a first prioritized capability backlog.
