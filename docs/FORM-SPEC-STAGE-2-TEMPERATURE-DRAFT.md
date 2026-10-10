# Form Specification — Stage 2: Temperature (Draft)

SUPERSEDED: See `TEMPERATURE-REQUIREMENTS.md` for updated process-owner requirements. The original draft below is retained for history, not as the current specification.

This is intentionally a partial specification. The process owner has confirmed only that the Project Team submits a Temperature request and that the final canonical router name is determined at this stage.

## Confirmed behavior

- Stage 2 is available only after Stage 1 QA approval and any configured waiting rule.
- The Commissioning Specialist is the expected Project Team submitter.
- The form must capture the canonical router name.
- The canonical name is written to the existing `rollout_item`; a new router record is not created.
- The original QA alias remains searchable and auditable.
- Network Operations reviews and approves or returns the request for correction.

## Known fields

| Field | Required | Rule |
|---|---:|---|
| Existing rollout item | Yes | Must reference the approved Stage 1 item |
| QA alias | Read-only | Displayed for continuity |
| Canonical router name | Yes | Validated against configured naming rules and selected context |
| Name assignment reason | Yes | Explains the assignment from QA alias to canonical name |
| Submitted by | System | Must be a permitted Commissioning Specialist or configured role |
| Submitted date/time | System | Server timestamp |
| Supporting evidence | Configurable | Pending Temperature checklist |
| Temperature-specific fields | Pending | To be supplied by process owner |

## Canonical-name assignment

On successful submission or approval, the system creates a name-assignment event:

```text
rollout_item_id
old_name = QA alias
new_name = canonical router name
changed_by
changed_at
stage = TEMPERATURE
reason
```

The current display label becomes the canonical name only after the configured assignment point. The exact point—submission or Operations approval—must be confirmed.

## Pending questions

1. What does Temperature mean in the operational process?
2. What are the form fields, evidence, and pass/fail criteria?
3. Does the canonical name become active at submission or after Operations approval?
4. What is the minimum/maximum wait after Stage 1 approval?
5. What rejection reasons and correction fields are required?
6. Can the canonical name be corrected after approval, and who approves the correction?
