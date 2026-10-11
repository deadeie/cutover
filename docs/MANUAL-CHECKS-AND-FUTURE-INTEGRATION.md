# Manual checks and future integration

Confirmed 2026-10-11. Requirements and extensibility intent only; detailed architecture remains a later phase.

## Initial release

- The system records workflow events and Operations decisions. Checks and checklist evaluation are performed by Operations outside the system.
- For QA, Project reports installation completion, site code and center name. Operations sends a checklist to its designated provincial contact outside the application. The Second-Line specialist records approval or return for correction on that basis.
- Provincial contacts do not need accounts or in-system tasks for the current release.
- No QA photo-upload or structured-checklist feature is requested now. Mandatory uploads and checklist completion inside the application are not initial-release gates.
- Temperature, ATP, Cutover and Handover checks remain manual external work recorded by Operations. Detailed measurement thresholds/checklist engines are not prerequisites for this event-recording release.
- Earlier suggestions of evidence fields are extensibility proposals, not mandatory implemented upload functionality.

## Future capabilities to accommodate

- Add photos, checklist templates/completed checklists and evidence linked to the existing router, stage and review attempt without replacing request identity or history.
- Integrate the process owner's existing external automation, likely as an early enhancement after initial release.
- Allow future router connectivity for checks through a separable integration boundary. No router connection, automation execution or configuration mutation is authorized/implemented now.
- Proposed future integration contract: manual and automated check results can be attached to the same attempt; distinguish tool/connectivity errors from actual failed checks. Detailed interfaces, credentials and dependencies will be reviewed during technical design.
- Business decisions remain attributable to Operations; adding automated results does not itself authorize automatic approval.
