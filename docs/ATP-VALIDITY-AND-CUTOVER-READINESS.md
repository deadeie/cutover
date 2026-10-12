# ATP validity and Cutover readiness

Latest process-owner clarification. Requirements discovery only. This supersedes the earlier Project-owned ATP-to-plan deadline interpretation.

## Confirmed business requirements

- The Cutover plan is Project's primary planning record. The leader can plan first; commissioning staff then pursue Temperature/ATP readiness for that plan.
- Planned Cutover with unknown/incomplete Temperature or ATP is a Project concern. Do not require ATP completion before a router can be planned.
- ATP approved without a Cutover plan is an Operations concern, not a Project-owned deadline to add a plan.
- ATP approval has a limited validity period because router condition can change after approval.
- The Operations Leader defines and may change that validity duration. No default duration has been approved.
- Once the validity period has elapsed, the ATP is no longer acceptable for the pending Cutover and requires ATP confirmation again.
- Inform both the Project Leader and Operations Leader when renewed ATP confirmation is required. Preserve the consolidated filterable leadership reminder lists.
- Adding a Cutover plan does not renew ATP. The validity requirement matters even when the router already has a future Cutover date.
- This is an approval-validity rule, separate from inter-stage waiting, Temperature observation, claim response warnings and conditional follow-up. Already claimed requests retain their inter-stage eligibility rule; ATP approval validity is a separate rule. Confirmed: changes to ATP validity duration recalculate existing approvals for routers not yet Cutover.

## Confirmed renewal and readiness controls

- Block Cutover start when ATP is expired; retain the plan and historical records.
- Expiry automatically creates an Operations re-confirmation task on the same router, with claim/review and correction-return behavior; Project does not need to initiate a new request.
- Conditional ATP uses the same validity duration; preserve its conditions.
- Recalculate still-valid ATP approvals for routers not yet Cutover when Operations Leader changes the duration. Confirmed exception: a duration increase never revives an already expired approval; its existing renewal task must be completed.
- Warn about approaching planned Cutover when Temperature or ATP is incomplete/invalid; the advance warning interval is configurable.
- New confirmation creates a new review decision and interval while preserving earlier reviews.

## Confirmed execution and policy-change boundaries

- Check ATP validity at the start of every Cutover attempt. If it expires during an attempt that began validly, do not interrupt that execution.
- After successful Cutover, do not create further ATP renewal tasks for pre-Cutover eligibility; the router follows Handover. Existing conditions/history are not erased.
- A failed and replanned Cutover must pass ATP validity again at its new start; expired ATP requires renewed confirmation.
- Increasing the validity duration does not restore an already expired approval. Its automatic Operations renewal task remains required; recalculate approvals that are still valid.

## Lifecycle details and remaining proposals

1. Record each ATP approval time, approver, validity policy and valid-until time. Expiration is derived from the approval time plus the configured duration; recalculate still-valid approvals for routers not yet Cutover when the duration changes, preserving the confirmed no-revival rule for expired decisions.
2. Show the current acceptance state (full/conditional) separately from validity (valid, expiring, expired, renewed by a later review). Never overwrite the original approval or findings.
3. In a Cutover plan, show whether Temperature is approved, whether ATP exists/currently remains valid, and whether that ATP is expected to remain valid at the planned execution time.
4. Confirmed: warn before a plan date if Temperature/ATP prerequisites are incomplete or invalid, using a configurable warning lead time. Forecasting expiry at the planned time remains part of the proposed display. Numerical defaults, precise routing and repetition remain open.
5. Immediately before recording Cutover start, revalidate current ATP validity as well as the existing prerequisites. Confirmed behavior: block start with expired ATP while retaining the plan and its history.
6. On expiry before Cutover, create an Operations re-confirmation task linked to the same router and earlier ATP, using the shared claim/review/correction workflow. Automatic task creation is confirmed; no new Project initiation is required.
7. A successful new review creates a new ATP decision and validity interval; old decisions, expiry events, corrections and conditional findings remain available. Creating/claiming a review or reading its reminder does not itself restore validity.
8. Proposed default: renewal repeats the necessary ATP checks only; do not restart QA/Temperature automatically. A separate finding may require additional action; that policy remains open.

## Questions to settle

- Define the exact renewal check scope and how findings may require additional stage work; automatic restart of QA/Temperature is not confirmed.
- Which initial validity duration and pre-expiry/pre-plan reminder lead times should be configured?

## Verification scenarios for later implementation

- A pending router can be planned before Temperature/ATP approval; its incomplete readiness is visible.
- An ATP approved today for a later Cutover shows both current validity and forecast validity at the planned time.
- Reaching expiry alerts both leaders even if a Cutover plan already exists.
- An expired ATP blocks execution from both a fresh and previously opened plan screen.
- Expiry automatically creates the Operations task; a conditional approval follows the same validity duration without losing conditions.
- Changing duration recalculates still-valid unexecuted approvals; increasing duration does not revive expired approvals or cancel their required renewal tasks.
- An ATP expiring mid-execution does not interrupt an attempt started validly. A failed/replanned attempt rechecks validity at its next start.
- Successful Cutover stops creation of pre-Cutover ATP renewal tasks; Handover and condition follow-up remain independent.
- A re-confirmation preserves router identity/history and creates a new decision; it does not erase unresolved conditions.
- Merely moving a plan date, opening a notification or claiming a renewal task cannot renew ATP.
