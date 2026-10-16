# Record contract

Use these fields as a provider-neutral logical schema, adapting storage to the task. Null means unknown, not false or waived. Do not fabricate records to fill the schema. Store system timestamps as ISO 8601 with an offset; preserve source-local dates, calendar system, and timezone separately when conversion is unresolved.

## Meeting and provenance

- meeting_id; revision; title; meeting_date; timezone; calendar_system
- source_id; source_version; source_kind (notes, transcript, audio, synthetic); source_locator
- participants with identity/role verification status
- consent evidence and scope when capture/processing requires it
- confidentiality; permitted audience; permitted processing; retention policy if real capture or persistence is planned
- segment_id; source_id/version; text; source lines or actual audio start/end; speaker_label; attribution status (verified, uncertain, unknown)

## Decision and action

Decision: decision_id, revision, description, classification (decision or proposal), source_refs, approval if applicable.

Action:
- action_id (stable across revisions); revision; output_description
- owner; owner_acceptance evidence/status; department; recipient identity and verification status
- due_at (null unless a complete instant is established); due_date for a date-only commitment; timezone; original_due_expression; conflicting_due_values
- dependencies: action_id or condition plus evidence required to satisfy it
- acceptance_criterion; acceptance_owner
- source_refs with source version and line/segment/range
- unresolved_fields/questions; proposed_changes kept separate from source facts
- review_status; routing_status; execution_status
- approval records; attempts/events; evidence; closure_acceptance

Approval: actor and authority basis, timestamp, exact object IDs/revisions, operation, destination, data scope, approved schedule/follow-up scope, source of authorization. Distinguish a draft approval proposal from an actual authorization.

Follow-up: authorized_by, authorization_ref, action scope, destination, allowed information, cadence/trigger, escalation recipient/condition, stopping condition, verified mechanism or null.

Event: event_id, object ID/revision, timestamp, type, actor/provider, source/result reference, previous/new state when applicable, reason. Append history; do not silently rewrite it. Redact unnecessary personal data and never store secrets in the log.

Attempt: attempt_id, idempotency_key, exact revision/destination/operation, attempted_at, provider_request_id if returned, outcome, status_lookup evidence, next permitted action.

## Separate states and evidence gates

Review: draft → needs_clarification or awaiting_approval → approved. An edited affected revision returns to review; old approvals remain historical only.

Routing: not_queued → queued → service_accepted → delivered → acknowledged. Use only states the available evidence supports; an acknowledgment may establish receipt even if the provider lacks a delivery event. Record uncertain and failed outcomes explicitly. Do not infer human receipt from service_accepted.

Execution: unknown/unreported until evidence establishes a state. Do not infer not_started from silence or a missing progress report; use it only with explicit evidence or newly initialized workflow state labeled as system-origin, not a source claim. Supported progression: not_started → blocked or ready → in_progress → completion_claimed → awaiting_evidence_acceptance → closed_with_evidence. Permit direct moves only when their evidence gates are independently met; this is not a requirement to invent intermediate events. Record owner acceptance independently. A routing event cannot move execution state.

Closed_with_evidence requires the relevant deliverable/test, criterion check, authorized acceptance with timestamp, and exact evidence_id and evidence_version of accepted evidence. Evidence versions must identify immutable content; if the provider permits in-place changes under one version, also bind a content digest and verify it in the adapter before acceptance. A completion claim or delivered message is insufficient. Rejected evidence returns to in_progress or needs_correction. Record cancelled, superseded, and reopened with reason and provenance; never count them as accepted completions.

For each blocked/uncertain item, record category, reason, required next step, last change time, and resolver only if assigned. Useful categories: consent/access, source quality, ownership/deadline, dependencies, approval, uncertain send, permanent failure, insufficient evidence.

## Additional records
Live answer: question_id, meeting_id/revision, asked_at, question, attribution_status, intended_audience, answer, classification, source_refs/version/pinpoint, data_as_of, retrieved_at, specialist, calculation_inputs/formula/units, uncertainty, disputed_points, persistence_authorization_ref, retention, linked_correction.

Profile: company_id/project_id, profile_version, source_refs, effective_at, verified_at, verification_status, missing_fields, template_source/version/status and visual_conformance_result.

Rule change: rule_id/version, scope, correction_source, proposed_change, authority_ref, approval_status, regression_case_ids, test_result, previous_version, rollback_ref. Metrics: metric_id/definition_version, review_window, sample_ids, coverage, reviewer, numerator, denominator, excluded/unknown counts, synthetic_or_operational, examples.
