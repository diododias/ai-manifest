# Flow artifacts contract

Use this contract in product and engineering skills.

1. Before reading or writing artifacts, look up the convention of the consuming repository. If there is configuration or a local rule, it prevails.
2. Without local convention, use the default layout: `business-discovery/<feature>/requisitos.md`, `teamwork/plan/feature-plan-<feature>/`, `.agents/prd/<feature>/PRD.md` and `.agents/spec/<feature>/SPEC.md`.
3. Only create an output artifact directory when the task authorizes producing that artifact. Never create all directories preemptively.
4. If the existing layout differs from the standard, present the mapping and ask for confirmation before writing. Preserve existing artifacts and history.
5. Treat approved PRD and SPEC as baseline: record deviations in a report; only change requirements, acceptance criteria or status after an explicit decision has been recorded.

Use paths relative to the root of the consumer repository and inform the paths actually used in the result.
