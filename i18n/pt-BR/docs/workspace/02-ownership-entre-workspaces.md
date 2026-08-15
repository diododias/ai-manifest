# 02 — Ownership entre workspaces

> Qual workspace é a fonte canônica de cada tipo de verdade, o que os demais recebem, e como um agente busca contexto de outro domínio sem duplicá-lo.

Três workspaces independentes só funcionam se a pergunta "qual é a versão correta?" tiver sempre uma resposta única. Esta página estabelece a regra que garante isso.

---

## Uma verdade, um dono

O princípio que governa a relação entre os três workspaces é simples e rígido: **uma informação autoritativa não deve ser mantida em dois lugares**. Cada tipo de verdade tem exatamente um workspace dono, e os demais recebem apenas o que precisam para operar — uma decisão aprovada, um handoff, um snapshot.

A razão é evitar o pior problema de documentação distribuída: duas versões da mesma verdade que divergem silenciosamente com o tempo, sem que ninguém saiba qual vale. Com um dono único por domínio, sempre há uma resposta objetiva para essa pergunta — o mesmo raciocínio que sustenta o compromisso "artefato só existe na fonte canônica", descrito em [Metodologia](../METODOLOGIA.md).

## O mapa de ownership

A tabela abaixo é a referência. Ela diz, para cada domínio de verdade, qual workspace é a fonte canônica e o que os outros dois recebem dele.

| Domínio | Fonte canônica | Os demais recebem |
|---|---|---|
| Valor, prioridade, outcome e requisitos | `pm/` | decisão aprovada e handoff de produto |
| Evidência de usuário, jornada e experiência | `ux/` | UX spec, critérios e handoff de experiência |
| Arquitetura, implementação e risco operacional | `tech-lead/` | viabilidade, contratos técnicos e evidence pack |

Repare que esta é a mesma [tabela de direitos de decisão](../metodologia/01-papeis.md#direitos-de-decisão) da metodologia, agora expressa em termos de arquivos e pastas. O PM é dono do valor tanto na decisão quanto no disco; o UX, da experiência; o Tech Lead, da técnica. A organização física do trabalho espelha a autoridade humana — não por coincidência, mas porque uma delas foi desenhada a partir da outra.

## Como um agente busca contexto de outro domínio

Na prática, um agente frequentemente precisa de contexto que pertence a outro workspace. Um Software Engineer Agent, operando no workspace do Tech Lead, precisa consultar o PRD, que vive no workspace do PM. Como fazer isso sem criar uma cópia que vai divergir?

A regra admite duas opções, ambas seguras.

| Opção | Quando usar | Cuidado |
|---|---|---|
| **Seguir o link até a fonte** | sempre que o artefato estiver acessível | ler onde ele realmente vive, no workspace dono — nunca reproduzir o conteúdo |
| **Usar um snapshot não autoritativo** | quando o link direto não for viável | identificar explicitamente como não autoritativo e confirmar validade antes de agir |

O que nunca se faz, em nenhuma das duas opções, é copiar a informação para o próprio workspace e passar a tratá-la como verdade local. No dia em que a original mudar, a cópia mente — e ninguém é avisado disso.

## Por que os exemplos são fictícios

Se você abrir os workspaces de exemplo em [`workspaces/`](../../workspaces/README.md), encontrará nomes, organizações, repositórios e estados fictícios. Isso é intencional: eles demonstram a estrutura, não o trabalho de produção de uma equipe real. Ao copiar a estrutura para o seu time, esses valores devem ser substituídos pelos seus — mas o princípio de ownership único não muda com a substituição.

---

*Anterior: [Estrutura do workspace](01-estrutura-do-workspace.md) · Próximo: [Harness do workspace](03-harness-do-workspace.md).*
