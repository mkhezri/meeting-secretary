# Meeting Secretary

Public edition **1.0.0**.

A portable meeting-lifecycle skill: preparation, private live Q&A, traceable minutes, approved assignments and evidence-based follow-through. The core instructions are English; a Persian overview and content template are included.

## What it provides

- Separate private preparation and participant agendas.
- Source-grounded answers and preserved transcription uncertainty.
- Decisions and actions with distinct review, routing and execution states.
- Company/domain/meeting/participant-scoped templates, approved visual variants and configurable branding.
- Bounded specialist routing, adapter contracts and approval proposals.
- Pure Python gate examples and offline regression tests.

## What must be configured by the user

Authorized sources, identities, organization profiles, templates, branding, storage, processing/retention rules, and action-specific approvals. Recording, calendar, messaging, persistence and monitoring require separately available, verified tools. This repository implements none of those services. It contains no credentials, real company assets or live configuration. Offline checks do not demonstrate production integration or permission authenticity.

## Quick start

1. Read [installation instructions](INSTALL.md).
2. Open [SKILL.md](skill/manage-meeting-secretary/SKILL.md).
3. Try the [synthetic meeting](examples/meeting.txt) and compare the [worked review](examples/worked-review.md).
4. Configure only adapters required for an authorized task; retain null/unconfigured values otherwise.
5. Review draft content, visual-template approval and distribution authority separately.

Example request: “Prepare an agenda and private briefing from these authorized notes. Draft minutes and proposed actions after the meeting; ask before sending anything.”

## Validation

Python 3, standard library only:

    PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skill/manage-meeting-secretary/tests -v
    PYTHONDONTWRITEBYTECODE=1 python3 tests/check_package.py

These checks exercise local workflow predicates; they do not run a recorder, scheduler or connector. See [validation notes](docs/VALIDATION.md) for coverage and limits.

## License and provenance

[MIT License](LICENSE), copyright (c) 2026 Mohammad Khezri. No third-party assets are bundled. See [PROVENANCE.md](PROVENANCE.md) for the scope and limits of the provenance review.

[معرفی فارسی](README.fa.md)
