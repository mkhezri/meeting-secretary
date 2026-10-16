# Context-scoped template registry

Resolve company_id, business_domain, meeting_type and participant_organization_ids (complete sorted unique set). No wildcard, unknown partner or cross-domain fallback is valid. Organizational participant changes create a new context; changing individual attendees within the same organizations need not change the visual key, but recipients still require separate verification and permission.

Select an exact-context approved source and preserve its fixed wording and text structure. A historic example is only a candidate until current approval is established. For a new context, material layout/source-version change or changed branding, prepare the first visual variant privately and obtain the authorized owner's approval before official use. Do not repeatedly request visual approval for an unchanged approved exact-context variant.

## Configurable branding

No company logo, font, color or official format ships with this package. Configure each organization from authorized sources. The default logo-based variant needs an approved sourced mark for every participant organization; a two-company header includes both logos. For more organizations, confirm composition. Never invent, trace or generate a corporate logo. Unknown marks may appear only as clearly labeled placeholders in private review drafts, which cannot pass the official-format gate.

An organization may explicitly approve a text-only variant using branding_mode=text_only and branding_policy_ref identifying that choice. It must still pass exact-context visual approval and rendering review. This is an affirmative configuration choice, never a silent fallback for missing logos. Omitted branding_mode means logos_required.

## Record, approve, reuse

Use the empty registry template. Persist only with destination-specific write authority. Record variant_id/revision, exact scope, source/version, text_structure_source, artifact_digest, branding mode and policy reference, logo provenance where required, visual_approval (owner, authorization_ref, approved_at, exact revision/digest), visual_review and last_verified_at. A scope confirmation alone cannot create a source version, digest or asset approval.

Render the output and compare fonts, size, margins, direction, tables, headers, signatures and fixed text. Disclose unavailable fonts/substitutions and obtain approval before claiming conformity. Keep actual meeting-content approval keyed separately by meeting/revision/payload digest; keep recipient/data-sharing permission separate again. Branding and participant membership grant no access or sharing rights. Local checks cannot authenticate approvals or remote assets.
