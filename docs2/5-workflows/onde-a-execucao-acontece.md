---
title: Onde a execução acontece
status: canonical
updated_at: 2026-08-09
---

# Onde a execução acontece

> A diferença entre o catálogo canônico e a execução no workspace, onde cada artefato é gravado por workflow e por que um handoff só termina na fonte canônica.

## Catálogo versus execução: a distinção que evita bagunça

Esta é a distinção mais importante para não misturar documentação com trabalho real. O **catálogo de workflows** é canônico e versionado — ele descreve como cada etapa deveria acontecer, e não recebe artefatos de nenhuma execução concreta. A **execução** acontece dentro do workspace de cada owner, em `projects/<project>/`.

Em outras palavras: o catálogo é a receita; a execução é o prato. Você nunca escreve no verso da receita o que aconteceu no jantar de ontem. Um agente nunca grava no catálogo global um `PB`, `PRD`, plano, evidência ou handoff de uma execução.

## Como o agente resolve onde trabalhar

Antes de iniciar qualquer missão, o agente segue uma cadeia de resolução fixa para descobrir onde ler e onde escrever:

```text
workspace do owner → projects/<project> → Work Item → fontes canônicas
```

Cada usuário ou papel executa o workflow dentro do seu próprio workspace. A instalação desse workspace mantém uma pasta `docs/workflows/` que **referencia** o workflow canônico — registrando qual versão está habilitada, permissões, integrações e adaptações locais. Essa camada local aponta para o catálogo; nunca o copia nem vira uma fonte de verdade concorrente.

## Onde cada workflow grava seus artefatos

Cada etapa grava seus artefatos persistentes na fonte canônica do domínio dono daquele conteúdo. A tabela abaixo mostra o mapa — repare que produto vai para o workspace do PM, experiência para o do UX, e engenharia para o do Tech Lead.

| Workflow | Artefatos persistentes | Trânsito temporário |
|---|---|---|
| Intake | `<pm>/projects/<project>/work-items/` | `.coordination/inbox/` e `handoffs/` |
| Discovery | PM: `discovery/`; UX: `research/` e `journeys/`; TL: `engineering/architecture/` | `.coordination/handoffs/` |
| Produto e UX | PM: `requirements/prd/`, `strategy/`, `decisions/`; UX: `flows/`, `specifications/`, `prototypes/`, `validation/` | `handoffs/` de cada workspace |
| Especificação | TL: `plans/active/`, `engineering/specs/`, `engineering/adr/`, `work-items/` | `execution/handoffs/` |
| Implementação | TL: `work-items/`, `execution/evidence/`, `repos/worktrees/<org>/<repo>/<work-item>/` | `.coordination/active/` |
| Validação e PR | TL: `execution/reviews/` e `execution/evidence/` | `.coordination/blockers/` |
| Homologação | PM, UX e TL: cada um em seu `validation/` ou `evidence/` | handoff para release |
| Produção | TL: `execution/evidence/`, `LEARNINGS.md`, registro de release | incidente e rollback em `.coordination/` |
| Conhecimento | fonte canônica do domínio; TL: `LEARNINGS.md`; PM: novo `work-item/` | propostas em `.coordination/` |

## Persistente versus trânsito: quando um handoff termina

A coluna da direita da tabela merece atenção, porque expõe uma regra sutil. As pastas `.coordination/` e o `memory.md` são **auxiliares** — trânsito temporário, não fonte de verdade. Um handoff só se torna **concluído** quando seu artefato final chegou à fonte canônica do projeto.

Isso significa que um trabalho parado em `.coordination/` não está pronto, por mais completo que pareça. Ele ainda está a caminho. A conclusão é definida pela chegada ao destino canônico, não pela existência de um rascunho em trânsito.

## Bindings locais podem restringir, nunca ampliar

Há uma última assimetria, intencional, que conecta esta página ao modelo de autonomia. O binding local em `<workspace>/docs/workflows/` declara a versão do workflow canônico e pode **restringir** ferramentas, permissões e integrações. O que ele **não pode** fazer é ampliar autonomia ou alterar gates sem a decisão prevista no modelo operacional.

A lógica é a mesma que protege todo o sistema: afrouxar uma proteção exige decisão explícita e owner; apertá-la, não. O caminho de menor resistência nunca pode ser reduzir a segurança.

## Continue por aqui

Você viu que a execução vive no workspace de cada owner. A próxima seção abre esse workspace por dentro: sua estrutura, seu ownership e o harness que o torna operável. Siga para [Workspace](../6-workspace/TLDR.md).
