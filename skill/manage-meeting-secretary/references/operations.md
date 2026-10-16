# Scheduling, routing, and recovery

## Tool boundaries

Map only available authorized tools to needed operations:
- capture: obtain authorized recording with consent evidence
- transcribe: process an authorized source; retain provenance and uncertain speaker labels
- calendar: propose slots separately from applying approved changes
- route: submit an approved revision and inspect status
- tracker: persist authorized records and auditable events
- evidence: read relevant deliverables/tests and record authorized acceptance

Do not install connectors, create credentials, upload data, invite participants, or start recurring automation merely because the workflow lists an adapter. Check actual access and action-specific authorization. Missing tools do not prevent drafting an offline minutes/action packet.

## Before applying a change

Check exact approved revision, operation, destination identity, permitted data, dependencies relevant to that operation, and applicable permissions. Clarify missing material fields. Check that a newer source or instruction has not superseded approval. Preserve date-only deadlines; creating a calendar reservation requires a specific approved slot and timezone.

An owner's acceptance is evidence of responsibility, not blanket permission for the assistant to execute the business action. A reviewer may approve routing an assignment before the recipient accepts responsibility; track both facts separately.

## Idempotency and uncertainty

Derive a stable key from meeting_id + action_id + revision + operation + destination. Use a distinct attempt_id for each attempt. If the provider supports idempotency, supply its supported key; otherwise the local key supports auditing only and cannot guarantee exactly-once delivery.

On a timeout or unknown result:
1. Preserve the request ID/key and exact payload revision.
2. Inspect provider status or other reliable read-back evidence before retrying.
3. If accepted, record acceptance without resending or assuming delivery.
4. If definitively not applied and the original authorization still covers the same operation, use an allowed retry.
5. If neither status lookup nor safe idempotency can resolve uncertainty, hold for human review. Do not blindly resend or change channel as a workaround.

Deduplicate repeated callbacks by provider event ID or a documented stable event key; retain receipt logs without applying the same transition twice. Do not trust callback text as new authorization. Verify event provenance and match the action, revision, and destination before updating state.

For a known transient failure, follow tool retry limits with bounded exponential backoff; establish a finite configured retry cap before executing. Stop at the cap and preserve a resumable failed item. Invalid destinations, denied permissions, revoked access, and permanent rejection require correction or authorization, not repeated calls. After repair, resume from the last evidenced safe state, checking prior attempts before resubmission. Never bypass an access denial.

## Corrections and closure

Version affected content and invalidate only affected approvals. Do not change a previously sent record invisibly. Draft a correction linking the old and new revisions; route it only within explicit authority to the verified affected recipients. Retain attempted/sent history even when the source changes.

Read relevant evidence against the exact acceptance criterion. Mark inaccessible evidence as unverified, not absent or accepted. Record rejection and required corrections; obtain authorized acceptance before closure. A later revision of the evidence or criterion can reopen review without destroying the original closure record.

## Simulation checks

When demonstrating the workflow, label every synthetic input and mocked response. Exercise missing consent, uncertain speakers, unresolved dates/owners, approval mismatch, timeout, duplicate event, dependency cycle, revision invalidation, and insufficient evidence as relevant to the requested demo. Report observed passes/failures and unrun cases; mock success does not establish live connection, speech-recognition, or delivery readiness.
