# Local stabilization checkpoint

The current application remains a limited local evaluation slice. Seven automated workflow tests and browser inspection do not establish complete acceptance of all requirements.

## Completed in this pass

- Serialized read/check/write operations to prevent simultaneous duplicate requests and conflicting claims.
- Normalize new site/province/topology inputs; accept GL0012 and GLX012 as distinct valid codes, reject invalid formats and province mismatches.
- Explicit confirmation for another router at an existing site; reject reuse of the same full name at that site.
- QA pairing requires explicit confirmation of the first unknown plane and rejects matching planes. Existing history remains preserved.
- Require correction reasons and resubmission descriptions; QA correction retains its original creation time and request identity.
- Block manual new submissions after stage approval; ATP renewals remain on the Operations path.
- Preserve router selection across UI renders, expose immutable router IDs, disable unavailable stages, and prevent duplicate in-flight browser submissions.

## Evidence

`py -3 -m unittest discover -s tests -v`: seven scenarios, including four simultaneous QA submissions resulting in exactly one stored request, complete correction cycle, site normalization, explicit paired-router identity, and existing stage-gate tests.

Browser inspection checks request-stage eligibility and router selection preservation. The existing local database contains duplicate historical QA/TEMP records produced by earlier builds. These have not been silently deleted or merged. Historical totals and rows can still reflect them; a reviewed reconciliation is needed separately.

## Next work

Still incomplete: real authorization, complete identity/range administration, TEMP correction categories and observation anchors, ATP approval timestamps/no-revival semantics, Cutover attempts, policy modes, reminders and reports. Do not describe this checkpoint as a finished system.
