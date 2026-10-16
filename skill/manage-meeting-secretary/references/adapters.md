# Optional adapter contract

The skill is portable guidance, not an implementation of any service. No provider is required for offline drafts. Inventory available tools against these roles: source_reader, capture, transcription, calendar, messaging, register, evidence_reader, scheduler and artifact_renderer. One provider may cover several roles; installed does not mean connected or authorized.

For each role record provider, capability, connection state, last verified operation/time, source coverage, read/write scope, permitted audience, retention, known limits and error evidence. Start with templates/adapters.example.json. Keep real credentials outside configuration and logs. Do not bootstrap accounts, grant OAuth access, or install software merely to fill a role.

Before a live operation verify actual tool availability, identity, destination, action-specific authorization, current approved revision, permitted payload and result semantics. Tool success may establish submission but not delivery or completion. Log provider IDs only in authorized private runtime storage, never in a public example.

A register adapter needs durable read/write evidence. A scheduler needs a verified job identifier and bounded plan with timezone, trigger, audience, content scope, escalation and stopping condition. A schedule JSON file alone is not a running job. If a required role is unavailable, preserve a portable draft plus precise blocker; never simulate a live result. Denied access stops that operation. Alternative tools must not circumvent restrictions.

The supplied Python helpers are demonstrations of local evidence predicates. They trust supplied fields and cannot verify identity, authorization authenticity, source freshness, consent or remote state. Treat them as testable workflow aids, not security enforcement, schema validators, or production-ready connectors.
