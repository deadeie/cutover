# ATP — Acceptance Test Procedure

Status: confirmed process requirements plus explicitly marked design proposals. No code, router connection, or automation execution in this step.

## Confirmed workflow

1. Project Commissioning Specialist submits ATP for the existing router rollout record after Temperature acceptance.
2. The request appears in a queue available to Second-Line Network Operations.
3. One Second-Line specialist claims the request. Others can see who owns it and should respect claim precedence during normal operation.
4. The claimant performs configuration and non-configuration checks manually or optionally uses the existing automation.
5. The automation accepts router IP and credentials, checks the router, and returns findings. Its interface and behavior must be inspected before integration; do not assume an API or a particular protocol.
6. The specialist approves a problem-free request or returns findings to the commissioning specialist who submitted it.
7. The requester fixes issues and resubmits. Every cycle has separate findings, comments, results, actors, and chronological history, without a fixed retry count or overwriting older attempts. The record distinguishes the original claimant, any takeover worker, and the person who submits the correction.

## Claim rules — proposed implementation contract

- Allow exactly one primary claim per ATP request, enforced in the data transaction, not only by disabling a button.
- Simultaneous claims: exactly one succeeds; the other sees the current owner.
- Claiming accepts responsibility for review; it does not approve ATP.
- The primary claimant has precedence, but a different eligible Second-Line specialist may continue when the claimant is unavailable or has already returned initial findings and cannot continue.
- Before continuing, the second specialist must see a warning naming the current claimant and must explicitly acknowledge that they are taking over another specialist's request.
- The takeover is a separate action; it records the original claimant, continuing specialist, reason, time, and acknowledgement comment.
- After takeover, only the current active worker can start a check or record the decision in normal operation.
- Revalidate current ownership at execution and decision time, including after takeover and from stale browser sessions.
- Suggested states: QUEUED → CLAIMED/IN_REVIEW → APPROVED or RETURNED_FOR_CORRECTION → RESUBMITTED.
- Distinguish the Operations specialist who SENT findings/returned the request from the Project specialist who SUBMITTED fixes. Neither actor is inferred from the original claimant. Proposed resubmission routing: highlight the latest correction-request sender, while keeping acknowledged continuation available to other Second-Line staff. Notification routing remains to be confirmed.

## Claim response thresholds

Confirmed: duration is measured after claim; management configures a lower warning threshold and a higher serious-warning threshold. Notify the claimant at each threshold. If another specialist has taken over, notify the active worker as well.

Proposals:

- Require 0 < lower < higher; do not invent default durations.
- Persist claim time, threshold policy version, warning times, and acknowledgement separately from comments.
- Show remaining/overdue time and owner in the queue and request details.
- Escalate the higher warning to Operations Leader/Manager in addition to the claimant, subject to approval.
- Use deduplicated in-app notifications, including after application restart. External channels remain undecided.
- Warning expiry does not automatically approve, reject, release, or transfer the claim.
- Stop active Operations review timing when returned to Project for correction; track Project correction time separately (proposal).
- Retain total request age and each ownership interval through transfers. Confirm timer treatment on transfer/resubmission and whether policy changes affect existing claims.

## Manual and automation modes

- Manual review is fully supported without a successful automation run as a prerequisite.
- Automation results become evidence/findings attached to the current attempt; they do not themselves approve or reject the business request.
- Capture review method, reviewer, check time, findings, and evidence for either mode.
- Distinguish a failed tool/connection run from an actual router configuration finding. Permit manual completion with documented findings rather than classifying a tool failure as an ATP pass.
- Proposed integration boundary: internal container worker/adapter uses the existing automation in the air-gapped network; package its dependencies in the offline deliverable once its interface is known.
- Credentials must not appear in comments, findings, logs, images, or exported reports. Credential provisioning and retention are pending design decisions.
- Automatic configuration changes are not part of the described ATP checks.

## Proposed findings and history model

- ATP request references the immutable rollout ID.
- Review attempt has sequence, submitter, submission time, assigned reviewer history, method, decision, and decision time.
- Finding has an ID, category, description, source (manual/tool), evidence, and status.
- Each correction request records its actual Operations sender, findings, attempt, time and comments. Each Project correction response separately records its actual author and references those findings. The reviewer verifies resolution explicitly.
- Each claim/release/transfer, check run, return, correction, resubmission, and approval is a distinct action with its own comments.
- Store earlier finding snapshots so later edits cannot rewrite previous decisions.

## Continuation by another specialist

Confirmed extension: the same warning and explicit acknowledgement pattern applies to eligible Project specialists continuing another requester's work. Preserve original requester, actual correction responder and every continuation event. This does not grant Project users record actions once Cutover execution has begun.

Confirmed: another Second-Line specialist may continue after an explicit warning and acknowledgement, without manager intervention, including after the previous specialist sent findings. Single-active-worker enforcement, mandatory reason, and automation-run reconciliation below are implementation proposals rather than additional confirmed business requirements.

1. A second eligible specialist selects Continue despite another claimant being shown.
2. The system requires acknowledgement of the warning and a takeover reason/comment.
3. The active worker changes to the second specialist; the primary claimant remains in history.
4. A takeover does not erase prior findings, comments, warnings, or partial work.
5. Management involvement is not required for ordinary takeover; management escalation is available for disputes or repeated overdue work.
6. Before execution ownership changes, finish/cancel or reconcile an active automation run. A stale run cannot apply findings or a decision as the new reviewer. Retain its outcome as historical evidence and require current-owner review.
7. Do not reset overall age or erase already-issued warnings when transferring. Exact new-owner response allowance remains configurable and subject to confirmation.

## Acceptance scenarios for later implementation

- Competing claims produce one primary owner; another eligible specialist can continue only after warning acknowledgement and a recorded takeover action.
- Both manual and automation-assisted reviews can result in approval or correction return.
- Multiple correction cycles retain chronological findings and comments independently.
- Lower/higher thresholds notify once according to the selected policy without releasing ownership automatically.
- Transfer preserves partial work and rejects a late decision from the former owner.
- Active automation is reconciled before a successor starts another check.
- Router identity and QA/Temperature history remain linked throughout.

## Required follow-up

Second-Line Operations may conditionally approve ATP in exceptional cases. This grants Cutover eligibility while preserving a distinct conditional decision and referenceable conditions; see `CONDITIONAL-APPROVALS.md`.

- Lower/higher threshold values, time units, and calendar policy.
- Resubmission routing: previous reviewer or shared queue?
- Confirm notification routing and timer behavior after acknowledged continuation; manager approval is not required.
- Supply the automation code/interface and dependency description when integration design begins; do not place credentials in source or examples.
- ATP checklist, findings categories, required evidence, and pass criteria.
