# Scoped corrections and measurable quality

## Correction lifecycle
Capture an owner's correction with its exact source reference, affected company/project/meeting or field, prior value/behavior, corrected value/behavior, reason if provided, and effective scope. Apply a clear correction to the requested deliverable; do not assume it authorizes changes to unrelated meetings, installed skills or existing source files.

A reusable rule proposal has rule_id/version, scope, authority reference, example/counterexample, applicability conditions, status (proposed/approved/retired), previous version and rollback reference. Reusable adoption requires explicit authority for that scope. Add a regression case for the failure and a negative case proving an unrelated company/project is unaffected. Test before proposing a package upgrade. Do not self-modify global instructions, access controls or credentials. Broader generalization remains a proposal even if the original correction was valid.

## Metrics
Use an explicitly defined review window, sample IDs, source coverage, reviewer, rubric and deduplication method. Report numerator, denominator and count separately; unknown and excluded records must be reported, not silently counted as correct. No reviewed sample means “not measured,” not zero errors. A zero denominator means N/A.

- Missed-action rate: independently source-reviewed actionable commitments absent from extracted register / all actionable commitments independently identified in the same reviewed source sample. State the agreed definition of actionable commitment. This measures extraction, not unseen source coverage.
- Wrong-owner rate: extracted actions with an owner contradicted by verified source/owner clarification / reviewed extracted actions with independently resolvable owners. Report unresolved owners separately.
- Unsupported-deadline rate: reviewed extracted actions carrying a deadline without source or explicit approval / all reviewed extracted actions carrying a deadline. Keep proposed dates separate from claimed commitments.
- Duplicate-action rate: redundant action records after the first legitimate record in each verified duplicate group / all reviewed extracted action records. Legitimate repeated tasks and version history are not duplicates.
- Late-follow-up rate: authorized follow-up occurrences performed after their approved trigger plus explicit tolerance, or still outstanding past that time / all authorized follow-up occurrences due in the window. Exclude documented cancellation before due; report blocked, unknown telemetry and missing runtime separately. Do not call an unapproved suggestion a missed reminder. Overdue and verifiably unperformed occurrences count as late, including a verified absent runtime. Unobservable outcomes remain unknown. With unknown outcomes, report a verified lower bound/range (known late / all due through (known late + unknown) / all due), or a clearly labeled observed-case rate with coverage, never an exact overall rate.

Attach examples and error causes, distinguish simulated versus operational samples, and preserve the measurement version so comparisons use the same definitions. Smaller samples and limited source coverage constrain conclusions. Report improvements only from comparable observed before/after samples; do not promise zero errors or invent scores.
