# Installation and configuration

This package contains skill instructions and local helpers. Choose a host that supports skill instructions and explicitly authorize any installation or external integration.

## Manual use without installation

Read `skill/manage-meeting-secretary/SKILL.md` in an assistant that can access local files, together with the references relevant to the task. Provide authorized notes explicitly. The assistant can draft content without any external integration.

## Skill-capable host

After approving this package for use, follow that host's supported skill-import flow with the complete `skill/manage-meeting-secretary` folder. The directory must retain `SKILL.md`, `references`, `templates`, `scripts` and `tests`. A host must support skill instructions; copying a folder alone does not prove discovery, activation or execution.

For a local host that explicitly documents a user-managed skill directory, copy this folder there under `manage-meeting-secretary`, preserving relative paths. For managed personal-skill services, use their supported import/save mechanism rather than assuming a local copy will synchronize. This package provides no product-specific installation script and changes no host settings.

After installation, verify the host discovers the name `manage-meeting-secretary` and run an offline request against the synthetic example. Avoid enabling overlapping meeting skills without selecting which should govern the task. Uninstall through the host's supported mechanism; removing this instruction package does not cancel external reminders already created by an authorized runtime.

## Configure only the needed capabilities

Use the adapter example as a starting inventory, not a deployment file. Establish source/read permissions separately from writes, recording consent, processing destinations, retention, recipient identity and communication approval. Store runtime configuration and credentials outside the distributable repository. Do not put secrets in an adapter JSON file.

Create company profiles from current authorized evidence. Register exact-context visual variants only after source/rendering review and approval. Choose logo-based branding with sourced marks or explicitly approved text-only branding. Configure no defaults based on synthetic examples.

## Verify actual runtime before promising follow-up

Check persistent register access, actual scheduler/job state, authorized trigger/cadence, timezone, audience, permitted content, escalation and stopping condition. If these are unavailable, provide a proposed schedule and clear limitation. No installation of this skill creates a continuous agent, consent to record, or permission to message anyone.
