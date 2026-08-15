# MCPs

MCPs (Model Context Protocol) são servidores que expõem ferramentas para o agente via protocolo padronizado. No contexto do harness, eles representam a camada de integração com sistemas externos — repositórios de código, rastreadores de tarefas, bancos de dados, APIs de serviços — e operam sob as mesmas regras de permissão que qualquer outra tool.

A diferença entre uma tool local e um MCP é que o MCP carrega estado externo e pode produzir efeitos fora do repositório. Isso eleva o custo de um uso indevido: uma tool local que falha não sai do contexto da sessão; um MCP que age sobre o sistema errado pode comprometer dados reais antes que o gate local detecte.

Um servidor MCP também é uma dependência, não apenas uma integração. É código de terceiros com acesso à sessão, e adicioná-lo é uma decisão de supply chain que pertence à mesma revisão de uma nova biblioteca — ver [Confiança](TRUST.md#o-harness-é-uma-supply-chain).

## `.agent/mcps.json`

O arquivo `mcps.json` declara quais servidores MCP o agente está autorizado a invocar naquele repositório, com que escopos, e quais operações estão explicitamente fora de alcance.

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

Operações não declaradas em `scope` são tratadas como proibidas. A ausência do arquivo `mcps.json` equivale a escopo zero: o agente não invoca MCPs até que haja declaração explícita.

## Autorização por camada

MCPs atravessam dois controles de acesso independentes:

O primeiro é o `settings.json`, que determina se MCPs estão permitidos como categoria de tool. Um repositório pode proibir MCPs por completo antes de qualquer granularidade de escopo.

O segundo é o `mcps.json`, que determina quais servidores e quais operações específicas estão autorizadas. Essa separação existe porque o risco varia por servidor — acesso de leitura ao GitHub é diferente de acesso de escrita a um banco de produção.

### Escopo de leitura não é automaticamente o escopo seguro

A entrada `postgres` acima permite `run_select` e proíbe toda escrita, o que parece uma escolha conservadora. Ela é conservadora quanto à *integridade* e não diz nada sobre *confidencialidade*. Quando a tabela contém dados pessoais ou regulados, o SELECT é o incidente: as linhas entram no contexto do modelo, e dali qualquer chamada de saída autorizada pode levá-las para fora do perímetro.

Duas operações individualmente inofensivas compõem um caminho de exfiltração — ler o dado e depois escrever um comentário em um rastreador público. Nenhuma lista de `scope` detecta isso, porque nenhuma das operações é proibida isoladamente. Definir o escopo de uma tool de leitura, portanto, exige nomear *o que ela pode ler*, não apenas *que ela pode ler*:

| Em vez de | Declare |
|---|---|
| `run_select` no banco de produção | `run_select` restrito a um schema sem dados pessoais ou a uma réplica de leitura com dados anonimizados |
| `read_file` sobre toda a árvore | os paths que não carregam credenciais nem dados de clientes |
| `read_issue` em qualquer projeto do rastreador | os projetos aos quais o Work Item pertence |

A regra de composição decorrente é: **uma sessão que contém dados sensíveis não pode possuir, ao mesmo tempo, escopo de escrita para fora.** Quando ambos são genuinamente necessários, eles são separados em agentes diferentes, com escopos diferentes, e o handoff entre eles carrega a conclusão, não os dados. [Confiança](TRUST.md#exfiltração-é-uma-composição-de-permissões) cobre a forma geral.

## Operações que exigem aprovação humana

Operações de escrita em sistemas externos têm efeito permanente e, em muitos casos, visível a terceiros. As categorias que exigem aprovação antes de execução são:

- Abertura, fechamento ou merge de PRs
- Criação ou encerramento de Issues em rastreadores externos
- Qualquer operação sobre banco de dados além de SELECT — e qualquer SELECT que alcance dados pessoais ou regulados
- Envio de notificações ou mensagens em canais externos
- Mudanças em configurações de CI/CD via MCP

O gatilho de aprovação é declarado em `require_human_approval` no `mcps.json` e em `permissions.md`. A redundância é intencional: o JSON protege o escopo técnico; o Markdown protege o julgamento em casos limítrofes.

## MCPs e o evidence pack

Toda operação via MCP que produz efeito externo deve ser registrada no evidence pack da unidade de trabalho. O script `scripts/evidence.sh` deve capturar as chamadas realizadas, os parâmetros enviados e a resposta recebida — não o resumo que o agente produziu sobre elas.

Sem esse rastro, a revisão humana de um trabalho que envolveu MCPs se baseia na narrativa do agente, não nos fatos do que foi feito. Esse é o padrão que o evidence pack existe para evitar.

Respostas devolvidas por um MCP são conteúdo externo e são tratadas como dado, nunca como instrução — um corpo de issue que diz "ignore as regras anteriores" é uma string em um campo, e [Confiança](TRUST.md) é onde essa fronteira é definida.

---

*Próximo: [Confiança](TRUST.md) — em quais entradas o agente pode agir e quais ele pode apenas ler.*
