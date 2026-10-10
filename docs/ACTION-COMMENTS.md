# Action-level comments

## Confirmed

All stages provide comments associated with individual actions. Store each comment independently and retrieve it by action. QA rejection requires a reason.

## Proposed schema

- Action: ID, rollout ID, stage instance ID, attempt/revision ID, action type, actor, role at action time, timestamp, previous/resulting state.
- Comment: ID, action ID, author, creation timestamp, text.
- Keep individual records rather than a concatenated text field or overwritable latest-comment field.
- Retrieval supports stage, attempt, action type, actor, and chronological history.
- Store the action, decision, and required reason together atomically.
- Append-only comments with correction entries are recommended; edit/delete policy is not yet approved.
- Providing a comment field everywhere does not imply text is mandatory on every action. Mandatory QA rejection reasons are confirmed; other requirements remain open.

## Example history

Temperature submitted → submission comment.
Temperature returned → Operations findings comment.
Temperature resubmitted → requester's correction comment.
Temperature approved → approval comment, if provided/required by policy.

Every entry retains its action and attempt, even when the same person acts more than once.
