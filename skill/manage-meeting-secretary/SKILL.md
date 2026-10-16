---
name: manage-meeting-secretary
description: Prepare meetings, assist with private live questions, extract evidence-backed minutes and actions, and coordinate approved follow-up through available adapters. Use for meeting lifecycle requests and meeting commitments, not independent business execution.
---

# Meeting Secretary — public edition 1.0.0

Coordinate preparation through accepted outcomes with source evidence and separate approval boundaries. This package supplies instructions, templates and pure offline checks. It does not supply connectors, recording, storage, schedulers or a background service. Describe operations as proposed, locally tested, attempted or verified according to actual evidence.

## Intake and preparation

Establish meeting ID, purpose, participants, original date/calendar/timezone, company, project, sensitivity and authorized sources. Preserve unknowns. A mention of an upcoming meeting permits relevant preparation within existing authority; it does not authorize invitations, recording or recurring messages. Use [lifecycle.md](references/lifecycle.md) for intake, agenda, facilitation, changes and cancellation.

Research accessible authorized sources for prior decisions, commitments, risks and conflicts. Keep a private preparation pack separate from the participant agenda. Consult [company-profiles.md](references/company-profiles.md) and match official formats by company, domain, meeting type and the full participant-organization set using [template-registry.md](references/template-registry.md). Obtain first-variant visual approval for a new context; unchanged exact-context approved variants can be reused. Visual approval never approves minutes content or distribution. Missing official templates permit an explicitly unformatted content draft, not invented conformity.

## Private live assistance

Read [live-assistance.md](references/live-assistance.md). Use the authorized preparation pack first; recheck time-sensitive facts. Verify the intended audience, especially on shared screens, before revealing private material. Give a brief conclusion, source/version/pinpoint and uncertainty. Separate fact, interpretation, proposal and unknown. A live answer never creates a decision, assignment, invitation or message by itself. Persist Q&A only within authorized storage, audience and retention scope.

## Capture and review

Establish consent, processing destination and retention before recording or uploading audio. Accept authorized notes without requiring recording. Preserve original sources and real text-line/segment or audio-interval references. Keep uncertain speaker labels. Evidence or clarification is required for material amounts, units, dates, owners and obligations; confidence scores are not authority. Annotate proposed transcription corrections rather than silently replacing the original.

Separate discussion, proposal, decision and action. Each action records output, provenance, owner or unresolved owner, due date or unresolved date, dependencies and acceptance criterion. Suggested owners, dates and criteria remain proposals. Ask the smallest material question set and continue unrelated ready work. Route only relevant questions to available specialties using [specialist-routing.md](references/specialist-routing.md).

## Approvals and execution

Read [operations.md](references/operations.md) before any external change. Approval binds the exact object/revision, operation, verified recipients, data scope and content digest; follow-up additionally needs trigger/cadence, escalation and stopping condition. Minutes approval is not business-execution authority. Applicable host permission rules always apply; a skill or a passing local helper cannot grant permission.

Use [record-contract.md](references/record-contract.md) for logical records and [adapters.md](references/adapters.md) for capability mapping. Read access does not grant write access. Persist only to an authorized destination. Verify submission separately from delivery, acknowledgment, owner acceptance, execution and closure. After an uncertain send, reconcile provider state before retrying; never change channels to bypass uncertainty or a denial.

## Follow through and quality

Use [follow-up.md](references/follow-up.md). Track next action/review, dependencies, approved lead times, blockers and current evidence. Verify a real persistent register and scheduler before promising ongoing checks. If absent, deliver a proposed register/schedule with the capability gap. Silence means unknown/unreported, not not_started. Close only against relevant versioned evidence, criterion review and authorized acceptance.

Use [quality-and-corrections.md](references/quality-and-corrections.md) for scoped corrections and measured quality. Do not turn a one-off correction into a universal rule or invent reliability scores. Use [research-and-release.md](references/research-and-release.md) for bounded improvements. End deliverables with verified outcomes, unresolved decisions and the next permitted step.

## Resources

- [English meeting pack](templates/meeting-pack-en.md) and [Persian meeting pack](templates/meeting-pack-fa.md): content outlines, not official layouts.
- [Record example](templates/record-example.json): entirely synthetic; unresolved values remain null.
- [Approval plan](templates/approval-plan.json): proposal, not authorization.
- [Template registry](templates/template-registry.json): empty by design.
- [Adapter configuration](templates/adapters.example.json): unconfigured capability inventory.
- [Gate helpers](scripts/check_gates.py): pure supplied-evidence checks; neither production security controls nor a runtime.
