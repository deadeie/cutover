# Resume checkpoint

User requested publication of the requirements and continuation later. Discovery only: no application or container has been built or tested.

## Current source of truth

Read the detailed stage requirements and latest clarifications before older proposal documents:

1. `ROLE-MATRIX.md` — three teams; separate Project installation/commissioning leaders.
2. `ROUTER-IDENTITY-AND-NAMING.md` — immutable rollout identity, QA alias, final name in Temperature; naming ambiguities remain.
3. `FORM-SPEC-STAGE-1-QA.md` — installer submits center/alias; timestamp and creator automatic; Second-Line approval or reasoned rejection.
4. `TEMPERATURE-REQUIREMENTS.md` — 48 hours from submission; connectivity-only correction does not restart; temperature/CPU/fan correction restarts at resubmission. Name, OM IP and hardware model; multiple province ranges.
5. `ATP-REQUIREMENTS.md` — claim, warnings, manual/optional automation checks, correction cycles and actual action authors.
6. `CUTOVER-REQUIREMENTS.md` — daily/weekly plans may omit executor; Operations alone records execution after start, including actual executor changes and success/failure. Failed attempt can be replanned without overwriting it.
7. `HANDOVER-REQUIREMENTS.md` — after successful Cutover plus 48 hours; ATP-style review.
8. `CONDITIONAL-APPROVALS.md` — conditional ATP permits Cutover; conditional Handover completes transfer and releases Project. Dedicated register and timed Operations reminders; external remediation team is out of scope.
9. `ACTION-COMMENTS.md` — independent comments per action/attempt and chronological history.

Eligible colleagues in either team may continue another person's work after a warning and acknowledgement, without required manager intervention. Preserve original and actual actors and actual Operations sender of each correction request. This does not override the Operations-only Cutover record rule.

## Next discussion

- Conditional reminder interval, time anchor, recipients, repetitions and condition-resolution recording.
- Naming examples resolving RSG digit counts, TH lengths, alias/suffix matching and multiple routers at one center.
- Detailed QA/ATP/Handover evidence and checks; monitoring thresholds.
- Claim warning thresholds and timer behavior after corrections/continuation.
- Target Linux distribution/architecture, container runtime, PostgreSQL location/version and authentication.
- Then UX and technical design; implementation follows explicit per-phase validation.

## Repository note

Local Git CLI and .git repository were not available at this checkpoint. Publication uses the authenticated GitHub browser interface. Browser commits are not evidence of a configured local origin or a CLI push. Earlier root-level copies of some documents exist on GitHub; `docs/` is the current requirements location.
