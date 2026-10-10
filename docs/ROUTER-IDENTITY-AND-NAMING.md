# Router Identity and Naming Rules

## 1. Purpose

The rollout record must keep one continuous identity from Installation QA through Handover. The identifier begins as a temporary QA alias because the final router name is not known at Stage 1. At Stage 2, the final name is added to the same rollout record and becomes the current canonical name.

## 2. Identity lifecycle

```text
QA submission
  temporary_alias = GJNNN
  canonical_name = null
  ↓
Temperature submission
  temporary_alias = GJNNN  (preserved)
  canonical_name = BAGJXXX_GLNNNN (or an approved exception form)
  ↓
Later stages
  all forms reference the same internal rollout_item_id
  canonical_name is displayed as the primary router name
```

The application must not create a second rollout item when the final name is entered. It updates the same item and records an audit event containing the old value, new value, actor, timestamp, stage, and reason.

## 3. Stable internal identity

The database must use an internal immutable identifier such as `rollout_item_id` as the foreign-key anchor for every stage, evidence item, decision, timer, incident, and audit event. A temporary alias or canonical router name must never be used as the primary key.

Recommended fields:

| Field | Purpose | Mutability |
|---|---|---|
| `rollout_item_id` | Stable internal identity | Immutable |
| `qa_alias` | Alias submitted at Stage 1, e.g. `GJNNN` | Preserve original; corrections are versioned |
| `canonical_router_name` | Final name entered at Stage 2 | Editable only through controlled correction flow |
| `name_status` | `QA_ALIAS_ONLY`, `CANONICAL_SET`, `NAME_CORRECTION_PENDING`, `NAME_CORRECTED` | System-managed |
| `name_history` / name-change events | Old/new values and provenance | Append-only |
| `center_name` | Human-readable center name | Source and edit policy to confirm |
| `province` | Province entity | Reference data |
| `router_model` | Router model | Reference data |
| `site_code` | Numeric or structured center/site code | Source and uniqueness rule to confirm |
| `topology_position` | `RSG`, `ASG`, or `CSG` | Derived/validated |
| `plane` | Plane value where applicable, e.g. `A` or `B` | Conditional |

## 4. QA alias format

Stage 1 receives a short alias in the form:

```text
<province_or_area_code><site_number>
```

Example:

```text
GJNNN
```

At QA time, the installation specialist submits this alias together with:

- Center name.
- QA alias.
- Record creation date/time.
- Creating user.
- Project and project-router item reference.
- Any installation evidence required by the QA checklist.

The exact number of digits in `NNN` and whether leading zeroes are allowed must be confirmed. The alias must be unique within its defined scope, such as province, project, or center registry.

## 5. Canonical router-name pattern

The normal pattern is represented as:

```text
B<T><PP><CCC>_<SS><NNNN>
```

Where:

- `B` is always the fixed first character.
- `<T>` is the topology position: `R` = RSG, `A` = ASG, `C` = CSG.
- `<PP>` is the two-character province code in the prefix naming standard, for example `GJ` for Doshanbe.
- `<CCC>` is the three-character center abbreviation.
- `_` is the fixed separator.
- `<SS>` is the two-character suffix code for the province/administrative naming standard.
- `<NNNN>` is a four-digit number unique to the center within the province scope.

Example shape:

```text
BAGJXXX_GLNNNN
```

The prefix province code `<PP>` and the suffix code `<SS>` are separate reference values. They must not be assumed to be equal.

## 6. Known exceptions

### 6.1 Three-character suffix code

Some centers use a three-character suffix where the third character is always `X`. In this form, the numeric part has three digits:

```text
BAGJXXX_GLXNNN
```

This is a different structural pattern from the normal two-letter plus four-digit suffix and must be validated by a configured naming rule rather than by a hard-coded assumption.

### 6.2 RSG plane notation

RSG names have a shorter center section before `_` than the normal ASG/CSG form. Examples supplied by the process owner are:

```text
BRGJXA_GLNNN
BRGJXB_GLNNNN
```

The exact digit count and the relationship between plane and suffix length must be confirmed before implementing a strict validator. The earlier generic example `BRGJXX_GLNNNN` is retained as a family shape, not as a final validation rule.

### 6.3 TH province

For province `TH`, the province cannot reliably be inferred from the prefix characters after `BA`, `BR`, or `BC`. The suffix code after `_`, `TH`, is the authoritative province discriminator. For TH:

- ASG and CSG center characters after `BA` or `BC` are treated as the complete center abbreviation.
- RSG center characters after `BR` follow the TH-specific longer form.
- The parser and validator must use configured province reference data and suffix code, not a generic prefix-length assumption.

## 7. Configuration model for naming

Naming rules should be data-driven and administered by an authorized Operations Manager or another configured administrator. A province reference record should include display name, prefix code, suffix code, whether the suffix may include `X`, allowed topology positions, center-abbreviation length by topology position, site-number length by pattern, plane requirements, effective date/version, and active status.

Router model records are separate reference data and may be added or retired by the Operations Manager. Retiring a model must not invalidate historical rollout records.

## 8. Validation behavior

### At Stage 1 (QA)

- Validate the alias syntax and configured uniqueness scope.
- Do not require a canonical router name.
- Store the alias exactly as entered after normalization rules are applied.
- Record center, project, site, creator, and timestamp.

### At Stage 2 (Temperature)

- Require a canonical router name before the request can be submitted.
- Validate the name against the selected province, topology position, center, plane, and configured naming rule.
- Require a controlled link between the QA alias and the canonical name.
- Record a name-assignment event rather than silently replacing the QA value.

### At later stages

- Display the canonical name as the primary label.
- Keep the QA alias available in details, search, audit, and exports.
- If a correction is needed, use a correction workflow with reason and approval rather than an unrestricted edit.

## 9. Questions requiring confirmation

1. In `GJNNN`, is `GJ` always the suffix province code, and is `NNN` always three digits?
2. What is the uniqueness scope for the QA alias: province, project, center, or another registry?
3. In the normal pattern, is `NNNN` always four digits and zero-padded?
4. For the three-character suffix exception, is the numeric part always exactly three digits?
5. For RSG, should Plane A use three digits and Plane B use four digits, as in the examples, or was that difference a typo?
6. Is the center abbreviation for RSG always two characters outside TH and three characters for TH?
7. Are `GJ`, `GL`, and `TH` examples of separate maintained code lists rather than values that can be derived from each other?
8. Who may correct a canonical name after Stage 2, and does correction require Operations approval?
9. Is the full canonical name unique globally, per province, per project, or per center?
10. Which router-model fields must be selected at QA, and which are only known at Temperature?
