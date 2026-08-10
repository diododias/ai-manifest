#MCPs

MCPs (Model Context Protocol) are servers that expose tools to the agent via a standardized protocol. In the context of harness, they represent the integration layer with external systems — code repositories, task trackers, databases, service APIs — and operate under the same permission rules as any other tool.

The difference between a local tool and an MCP is that the MCP carries external state and can produce effects outside the repository. This increases the cost of misuse: a local tool that fails does not leave the session context; an MCP that acts on the wrong system can compromise real data before the local gate detects it.

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

## Operations that require human approval

Writing operations on external systems have a permanent effect and, in many cases, visible to third parties. The categories that require approval before execution are:

- Opening, closing or merging PRs
- Creation or closure of Issues in external trackers
- Any operation on the database other than SELECT
- Sending notifications or messages on external channels
- Changes to CI/CD configurations via MCP

The approval trigger is declared in `require_human_approval`, `mcps.json`, and `permissions.md`. The redundancy is intentional: JSON protects the technical scope; Markdown protects judgment in borderline cases.

## MCPs and the evidence pack

Every operation via MCP that produces an external effect must be recorded in the work unit's evidence pack. The `scripts/evidence.sh` script should capture the calls made, the parameters sent, and the response received — not the summary the agent produced about them.

Without this trail, human review of work involving MCPs is based on the agent's narrative, not the facts of what was done. This is the pattern that the evidence pack exists to avoid.
