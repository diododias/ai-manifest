# Example workspaces

This area contains concrete implementations of the operational workspaces described in the Agent Team architecture.

Each role has an independent root so that its contracts, examples, and sources of truth can evolve without mixing responsibilities:

- [`tech-lead/`](tech-lead/README.md): feasibility, architecture, implementation and operational risk;
- [`ux/`](ux/README.md): research, experience, accessibility and validation with users;
- [`pm/`](pm/README.md): value, priority, requirements and product results.

The examples are not a team's production workspace. Names, organizations, repositories, and states are fictitious and must be replaced when copying the structure.

## Workflows within each workspace

Reusable contracts are in the [global workflow catalog](../workflows/README.md). Each user workspace must maintain `docs/workflows/` as a local binding layer: which workflows are enabled, which canonical version is used, permissions, integrations and handoff routing.

Artifacts from a run do not belong to `docs/workflows/`. They are located in `projects/<project>/`, in the workspace that owns the domain: the PM registers discovery, PRD, decisions and Work Items; UX records research, journeys, flows, specifications and validations; the Tech Lead records plans in `projects/<project>/plans/active/`, specs, ADRs, evidence, reviews and worktrees. `..coordination/` is temporary transit only.

Raw material that supports the analyzes and discussions of a workflow — transcripts, printscreens, emails, PDFs, Word documents and the like — is located in `projects/<project>/plans/assets/<workflow>/<YYYY-MM-DD>-<session-id>/`, in any of the three workspaces. Each run uses its own session folder; rerunning a workflow due to unsatisfactory results never overwrites or mixes material with the previous attempt. `plans/assets/` is not a canonical source — the conclusion goes to the artifact in the correct domain, and the asset remains as an auditable trace. See the skill [`workspace-projects`](../skills/workspace-projects/SKILL.md) for full details.

## Ownership between workspaces

| Domain | Canonical source | The remaining workspaces receive |
|---|---|---|
| Value, priority, outcome and requirements | `pm/` | approved decision and product handoff |
| User, journey and experience evidence | `ux/` | UX spec, criteria and experience handoff |
| Architecture, implementation and operational risk | `tech-lead/` | feasibility, technical contracts and evidence pack |

Authoritative information should not be maintained in two workspaces. When an AI needs context from another domain, it should follow the link to the source or use a snapshot identified as non-authoritative and confirm its validity before acting.
