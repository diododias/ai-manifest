# MCPs

MCPs (Model Context Protocol) are servers that expose tools to the agent via a standardized protocol. In the context of harness, they represent the integration layer with external systems — code repositories, task trackers, databases, service APIs — and operate under the same permission rules as any other tool.

The difference between a local tool and an MCP is that the MCP carries external state and can produce effects outside the repository. This increases the cost of misuse: a local tool that fails does not leave the session context; an MCP that acts on the wrong system can compromise real data before the local gate detects it.

An MCP server is also a dependency, not just an integration. It is third-party code with access to the session, and adding one is a supply chain decision that belongs in the same review as adding a library — see [Trust](TRUST.md#the-harness-is-a-supply-chain).

## `.agent/mcps.json`

The `mcps.json` file declares which MCP servers the agent is authorized to invoke in that repository, with what scopes, and which operations are explicitly off limits.

```json
{
  "servers": [
    {
      "name": "github",
      "scope": ["read_pr", "list_issues", "create_comment"],
      "forbidden": ["delete_branch", "force_push", "merge_pr"]
    },
    {
      "name": "linear",
      "scope": ["read_issue", "update_status"],
      "forbidden": ["delete_issue", "modify_project"]
    },
    {
      "name": "postgres",
      "scope": ["read_schema", "run_select"],
      "forbidden": ["insert", "update", "delete", "drop"]
    }
  ],
  "require_human_approval": ["create_pr", "close_issue", "run_migration"]
}
```

Operations not declared in `scope` are treated as prohibited. The absence of the `mcps.json` file is equivalent to zero scope: the agent does not invoke MCPs until there is explicit declaration.

## Authorization by layer

MCPs traverse two independent access controls:

The first is `settings.json`, which determines whether MCPs are allowed as a tool category. A repository may disallow MCPs altogether before any scoping granularity.

The second is `mcps.json`, which determines which servers and which specific operations are authorized. This separation exists because risk varies by server — read access to GitHub is different from write access to a production database.

### Read scope is not automatically the safe scope

The `postgres` entry above allows `run_select` and forbids every write, which reads as the conservative choice. It is conservative about *integrity* and says nothing about *confidentiality*. Where the table holds personal or regulated data, the SELECT is the incident: the rows enter the model's context, and from there any authorized outbound call can carry them out of the perimeter.

Two operations that are each individually harmless compose into an exfiltration path — read the data, then write a comment on a public tracker. Neither `scope` list catches this, because neither operation is prohibited on its own. Scoping a read tool therefore requires naming *what it may read*, not only *that it may read*:

| Instead of | Declare |
|---|---|
| `run_select` on the production database | `run_select` restricted to a schema with no personal data, or a read replica of anonymized data |
| `read_file` across the whole tree | the paths that carry no credentials or customer data |
| `read_issue` on any tracker project | the projects the work item belongs to |

The composition rule that follows from this: **a session holding sensitive data must not simultaneously hold an outbound write scope.** Where both are genuinely needed, they are separated into different agents with different scopes, and the handoff between them carries the conclusion rather than the data. [Trust](TRUST.md#exfiltration-is-a-composition-of-permissions) covers the general form.

## Operations that require human approval

Writing operations on external systems have a permanent effect and, in many cases, visible to third parties. The categories that require approval before execution are:

- Opening, closing or merging PRs
- Creation or closure of Issues in external trackers
- Any operation on the database other than SELECT — and any SELECT reaching personal or regulated data
- Sending notifications or messages on external channels
- Changes to CI/CD configurations via MCP

The approval trigger is declared in `require_human_approval`, `mcps.json`, and `permissions.md`. The redundancy is intentional: JSON protects the technical scope; Markdown protects judgment in borderline cases.

## MCPs and the evidence pack

Every operation via MCP that produces an external effect must be recorded in the work unit's evidence pack. The `scripts/evidence.sh` script should capture the calls made, the parameters sent, and the response received — not the summary the agent produced about them.

Without this trail, human review of work involving MCPs is based on the agent's narrative, not the facts of what was done. This is the pattern that the evidence pack exists to avoid.

Responses returned by an MCP are external content and are treated as data, never as instructions — an issue body that says "ignore the previous rules" is a string in a field, and [Trust](TRUST.md) is where that boundary is defined.

---

*Next: [Trust](TRUST.md) — which inputs the agent may act on, and which it may only read.*
