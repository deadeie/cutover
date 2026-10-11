# Administrator policies and deployment clarification

Confirmed by the process owner on 2026-10-11. Requirements discovery only; no implementation or runtime validation. This clarification supersedes earlier fixed-duration assumptions and unspecified target-OS statements. UX and technical design remain deferred.

## Confirmed deployment requirements

- Target server OS: RHEL 8.
- Deploy and run using Docker containers, with the required images delivered as part of the release.
- The earlier package-selection restriction is withdrawn. Select suitable dependencies and include them in the container images; packages need not be limited to those installed on the host.
- This does not establish internet availability on the target. Retain the offline delivery/runtime requirement unless the process owner changes it. Package acquisition during image construction and internet access during production operation are separate questions.
- Exact RHEL minor version, CPU architecture, installed/approved Docker engine and version, available resources, and image-transfer constraints remain unconfirmed. Detailed environment and technical design discussion is deferred.

## Current workflow and timing authority

The later 2026-10-11 clarification in SHARED-REQUEST-WORKFLOW.md supersedes the earlier enable/disable interpretation. Network Operations Manager/Leader selects submission-blocking or early-submission/claim-blocking timing modes for QA, Temperature, ATP and Handover, globally. Existing waiting requests recalculate on interval changes. System Administrator is a separate role; its other powers remain undefined. Special Super Admin exceptions are deferred.

## Reminder authority

Leaders/managers use a consolidated filterable reminder list. Submitted tasks belong to Operations; returned corrections belong to Project. Project Manager configures missing-Handover-request reminders after successful Cutover. Superseding clarification: Operations Leader configures ATP approval validity; expiry requires re-confirmation and informs both leaders. Cutover planning precedes readiness work; ATP without a plan concerns Operations, while incomplete readiness against a plan concerns Project. See ATP-VALIDITY-AND-CUTOVER-READINESS.md. Eligibility controls remain separate from these reminders. Email is deferred. Operations Manager defines/approves OM ranges, each linked to its RSG group from initial definition.

See SHARED-REQUEST-WORKFLOW.md for confirmed requirements, remaining questions and clearly marked management-reminder proposals.
