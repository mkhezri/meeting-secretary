# Follow-up and service health

Maintain an authorized durable register, not chat recollection alone. The record must survive a session restart if ongoing follow-up is promised. Identify the actual store and mechanism, with last successful read/write or check and access scope. If no write permission/runtime exists, give the prepared register/schedule as a proposal; don't imply it has been saved or activated.

Each active action has: owner/acceptance, due date, last evidenced status, next permitted action, next review time, blockers, dependencies, risk, approval scope, escalation route and stop condition. Propose lead times based on consequence and dependencies; do not invent or activate a default daily/hourly reminder campaign. For date-only commitments seek an approved notification time and timezone separately.

Before each authorized check:
1. Reconcile current revision, latest owner instructions and existing provider events.
2. Read new responses or deliverables; retain original timestamps and source references.
3. Assess near-due blockers and dependency risks without declaring lateness when date/time is unresolved.
4. If a reminder is due under the approved plan, check deduplication and exact audience/data scope, then route once and record evidence.
5. Escalate only at the approved trigger to the approved recipient. Silence is not owner acceptance or completion.
6. Set next review; close only after criterion check plus authorized acceptance, or record cancellation/supersession separately.

Connection health: track adapter capability, last check, missing data interval, failure and resolver. Report a material outage or stale source once with impact and next step, then report only meaningful change or an authorized reminder. Do not equate an installed plugin with configured access, authenticated access with operational success, or a schedule file with a running scheduler. The register, scheduler and messaging service are separate components. No tool-independent skill can guarantee that nothing will ever be missed.

Store pending operations before submission in the authorized register. Stable operation key includes meeting/action/revision/operation/destination; provider support is needed for true idempotency. After uncertain send, read back before retry. If unresolved, hold; never switch channels or send again blindly. Deduplicate provider callbacks and reject mismatched revisions. Do not let delayed callbacks restore superseded approval.

Closure: inspect actual allowed evidence, check every acceptance condition, record evaluator and explicit authorized acceptance. An inaccessible file, completion claim, delivered assignment, or merely created plan cannot prove execution. Inaccessible evidence remains awaiting_evidence_acceptance with an access blocker. For rejected or defective evidence preserve required corrections and use needs_correction, not closed. Source changes can reopen an action without destroying prior history.

## Early warning from dependencies and lead time 
For each deadline identify prerequisite deliverables, evidenced expected duration, buffer if owner-approved, and the latest feasible prerequisite date. Missing durations produce an uncertainty flag, not a fabricated risk score. Separate hard contract deadlines from proposed targets. Detect blocked critical prerequisites and cycles; explain which outcome may be affected and the evidence, rather than asserting inevitable lateness.

Propose a review trigger before the latest safe start, with timezone, consequence, audience, cadence/maximum frequency, escalation and stop condition. Only activate that plan after approval and real scheduler verification. Recalculate after approved scope/date changes; invalidate affected old triggers and reconcile provider status to avoid double reminders. Discovered risk allows a private report within authorized context, not automatic outreach to new recipients.
