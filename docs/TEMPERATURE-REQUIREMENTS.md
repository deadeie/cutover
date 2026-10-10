# Temperature — confirmed requirements and open decisions

This document supersedes the incomplete Temperature draft where they differ. Status: discovery, not implemented.

## Confirmed flow

1. Project Commissioning Specialist submits for the same rollout record used in QA.
2. Full router name, OM IP, and hardware model are supplied at this stage. Preserve the QA alias and stable internal identity.
3. Network Operations observes temperature, CPU, and fans for 48 hours and checks the possibility of connecting to third-party monitoring systems.
4. Second-Line Operations Specialist approves progression or returns issues to the Project Team and original requester for correction.
5. Every action supports its own separately retrievable comment. Do not overwrite prior submission/review comments on resubmission.

## Province and model configuration

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
