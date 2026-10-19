# Temperature — confirmed requirements and open decisions

2026-10-13 superseding clarification: Operations explicitly chooses REOBSERVE or CORRECTION_ONLY on return, independently of the reason category. REOBSERVE begins a full new run at resubmission using the then-current duration. CORRECTION_ONLY permits approval after correction without a time gate. Running observation durations retain their original configured value. Older category-driven return rules below are superseded; see PROJECT-TARGETS-AND-REPLACEMENT.md. This update is not yet implemented.

This document supersedes the incomplete Temperature draft where they differ. Status: discovery, not implemented.

Time intervals are configurable; System Administrator is distinct from Operations Manager/Leader. Workflow timing authority is recorded in `SHARED-REQUEST-WORKFLOW.md`. The 48-hour observation references are the recorded baseline; effects of policy changes on existing/repeated observation runs remain open. See `ADMIN-POLICIES-AND-DEPLOYMENT.md`.

## Confirmed flow

Confirmed follow-up: there is no waiting interval between QA approval and Temperature submission or claim. Both are immediately permitted after QA approval. The configurable observation period starts at Temperature submission; Operations can work during it, but final approval is blocked until it completes. Existing correction/re-observation rules remain. This resolves the earlier two-clock question below; there is no additional QA-to-Temperature delay.

Latest 2026-10-11 clarification: extend the ATP/Handover queue, claim/review and acknowledged-continuation approach to Temperature. See `SHARED-REQUEST-WORKFLOW.md` for global submission/claim modes. There is no QA-to-Temperature interval; only the submission-based observation period applies before Temperature approval. Initial-release checks remain manual outside the system; see `MANUAL-CHECKS-AND-FUTURE-INTEGRATION.md`.

1. Project Commissioning Specialist submits for the same rollout record used in QA.
2. Full router name, OM IP, and hardware model are supplied at this stage. Preserve the QA alias and stable internal identity.
3. Network Operations observes temperature, CPU, and fans for 48 hours and checks the possibility of connecting to third-party monitoring systems.
4. Second-Line Operations Specialist approves progression or returns issues to the Project Team and original requester for correction.
5. Every action supports its own separately retrievable comment. Do not overwrite prior submission/review comments on resubmission.

## Province and model configuration

Latest range clarification: block submission if the OM IP is outside all allowed ranges of the selected province. Each RSG A/B pair shares one range with its subordinate ASG/CSG routers. Ranges are unique/non-overlapping and the user states only the last octet varies. See `OM-RANGES-AND-RSG-GROUPS.md` for confirmed facts and the approved separate range-registration flow for new RSGs. Operations Manager defines/approves the range, and group linkage is mandatory from the outset; A/B membership in that same group is confirmed.

Province administration stores both naming-standard codes and multiple OM address ranges per province. Ranges are generally /24; do not hard-code /24 as the only allowed prefix. Validate the router OM IP against any configured range belonging to its province. Router hardware is selected from the administrator-managed model catalog.

No expansion of OM, real address allocations, measurement thresholds, automatic router access, or monitoring integration implementation has been supplied or authorized by this requirement.

## Proposed implementation rules pending approval

- Store ranges as CIDR reference records linked to a stable province ID.
- Keep ranges and naming-code history for existing router records.
- Store submitted name/IP/model and their changes without creating another router record.
- Validate IP syntax, province membership, address conflicts, and reserved addresses; the uniqueness/network-segmentation policy still needs confirmation.
- Track monitoring runs separately from requests so corrections and repeated runs retain their evidence.
- Elapsed time makes a request eligible for review; it never automatically approves the stage.
- Apply the Operations Manager's configurable timing/override policy and retain its version.
- A readiness check does not by itself require this application to integrate with a monitoring system.

## Confirmed timing and correction rules

- The 48-hour interval begins at request submission.
- A connectivity-only issue does not require a fresh 48-hour interval. Preserve the existing observation start and completed monitoring credit, but resolve the connectivity issue before approval.
- An issue involving temperature, CPU, or fans requires a repeated full observation interval.
- Completing the 48-hour observation and establishing monitoring-system connectivity are both necessary for normal approval and progression to ATP. There is no extra 48-hour wait after Temperature approval.
- Second-Line Operations approval is still required; elapsed time alone is insufficient.
- Proposed: classify findings as CONNECTIVITY, TEMPERATURE, CPU, FAN, or UNCLASSIFIED; any thermal/CPU/fan finding in a mixed set requires repetition. Unclassified findings require reviewer classification.
- Confirmed: after temperature, CPU, or fan findings are corrected, the requesting Project user resubmits the same request and the new 48-hour interval starts at that resubmission time. Never discard earlier run history.

## Acceptance scenarios to implement later

- Authorized commissioning user submits name, OM IP, and model on the existing QA record.
- An IP in either of two configured province ranges is accepted; one outside both is rejected.
- Comments for first submission, return, resubmission, and approval remain independently retrievable.
- A return routes to the original requester and Project Team without losing monitoring history.
- Normal approval cannot occur before the configured observation interval; expiration alone does not approve.
- Only the configured reviewer can approve; actor and action time are recorded.

## Remaining details

- Measurements entered manually, attached as a report, or imported?
- Thresholds and monitoring-connectivity acceptance criteria?
- Detailed classification for mixed or ambiguous faults?
- Name/IP become current at submission or approval?
- Required comment policy beyond QA rejection; comment editing and visibility?
