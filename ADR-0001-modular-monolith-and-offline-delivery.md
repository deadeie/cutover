# ADR-0001: Modular monolith and offline delivery

## Status

Proposed — production architecture awaits validation. A native Windows/SQLite local flow slice is implemented only for process evaluation; it does not change the target RHEL 8/offline delivery requirements or choose the production database.

## Context

The source document selects Python 3.11, PostgreSQL, and a modular architecture. The target environment is an offline Linux VM. The project must be transferable without depending on public package registries, cloud services, or CDNs during installation or runtime.

## Decision

Use a modular monolith for the first release. Package the application and its runtime dependencies into a versioned container image built in a Linux-compatible build environment. Deliver an offline bundle containing the image archive, checksums, dependency/package manifest, configuration template, migration commands, smoke-test commands, and rollback instructions.

## Consequences

- One deployable unit keeps the first release operationally simple.
- Module boundaries remain explicit so a later service split is possible.
- Native dependencies must be built and tested against the target Linux architecture.
- The repository must separate source, migrations, configuration templates, tests, build scripts, and operations documentation.
- Secrets and environment-specific credentials stay outside Git and outside the transfer bundle.
- The local evaluation app uses a standard-library HTTP host and SQLite adapter behind a separate workflow module. Preserve this separation while the process is refined; validate the database adapter/migrations, authentication, and RHEL packaging in their own later design/release steps.

## Rejected for now

- Microservices: adds deployment and offline-operability cost before process boundaries are understood.
- Runtime internet installation: conflicts with the air-gapped target.
- Direct router mutation: requires a separate approved capability and authorization model.
