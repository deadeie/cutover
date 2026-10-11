# OM ranges and RSG groups

Requirements discovery. The process owner approved the range-request/approval flow, Operations Manager authority and mandatory group linkage at initial range definition. The process owner also confirmed that the first RSG occupies its A/B position in the pair and the second completes the same group; this records relationships only and does not modify the network. No networking or database implementation is included.

## Confirmed requirements

- An RSG A/B pair shares one range with its subordinate ASG/CSG routers. Each pair has exactly one range; a province may have several pairs and several allowed ranges.
- Operations Manager defines and approves allowed province ranges. Each range must reference its RSG group from the outset; unassigned active province ranges are not allowed in the confirmed target workflow.
- If a router's OM IP does not belong to an allowed range of its selected province, block submission where OM IP is collected (currently Temperature). QA does not yet require an OM IP.
- User states ranges are unique and do not overlap; only the last octet varies between router addresses in a range. Do not treat matching two groups as an expected business case.
- TH naming is exceptional: province is determined from the suffix, not center letters in the prefix. Topology is determined by the second character.
- User approved range registration with Operations Manager approval and required group ownership from the start. Parent-group classification supports reporting and future uses. Explicit all-province scope remains to be confirmed; TH naming remains exceptional.

## Approved range registration flow and classification clarification

1. Maintain a province's allowed ranges as the authoritative list. Each range must reference an RSG group representing an A/B pair, independently of whether both router records exist yet.
2. Operations Manager creates the RSG group and its one range, linked to the province. Pair membership can be populated as the A and B routers enter the system; do not require both first.
3. If Project is entering Temperature for a new RSG whose range is absent, preserve the form as a draft and offer a separate request to register the range/group. The router request is not submitted and does not enter the Operations claim queue until its IP passes the province rule.
4. The range-registration request identifies province, proposed range, site/group identity and planned plane. It is a reference-data request, not approval of the router's QA/Temperature/ATP.
5. Operations Manager reviews it, checks uniqueness/non-overlap and group ownership, then activates the province range/group or returns it for correction with a reason. System Administrator is not assigned this approval merely by holding that separate role.
6. When activated, notify Project; revalidate and allow explicit Temperature submission. Do not submit the saved router request automatically. The administrator may also predefine the group/range before router entry.
7. Confirmed representation: the group represents the two separate RSG routers sharing one range. For example, BRJHFA_TH1234 is the A router and BRJHFB_TH1234 is the B router in that pair. Recording membership labels their existing relationship; it does not change topology, select a network route or make one RSG subordinate to the other. The first router occupies its identified A/B position and the second completes the same group.
8. A matching ASG/CSG is associated with the group for that range. Group ownership is required when defining the allowed range, so there is no unassigned-range fallback in the target flow.

## Proposed integrity and history rules

- Reject duplicate/overlapping range definitions so the confirmed uniqueness assumption remains true in stored configuration.
- Propose this grouping model for every province, with TH-specific name parsing kept separate; user confirmation of all-province scope is pending.
- Keep approval and change history for reference data. Changes to ranges/group assignments must not silently rewrite historical workflow decisions.
- Preserve the router's immutable identity and separate site code from RSG group membership.

## Questions to settle

- Confirm the model applies to every province, not just TH. Confirm the formal range notation/size during data design; no technical subnet restrictions are implemented now.
