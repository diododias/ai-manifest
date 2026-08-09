---
title: O harness do workspace
status: canonical
updated_at: 2026-08-09
---

# O harness do workspace

> O que torna um workspace operável por agentes de forma repetível: as convenções, as skills de base e as garantias de coordenação quando vários agentes trabalham ao mesmo tempo.

## O que "harness do workspace" significa

Você já encontrou a palavra *harness* algumas vezes. Vale defini-la com precisão aqui, porque ela tem dois sentidos que não podem se confundir. Um harness, de forma geral, é o conjunto de arquivos, convenções e verificações que torna um espaço **compreensível e seguro** para um agente operar sem precisar que alguém recite o contexto toda vez.

O **harness do workspace** é esse conjunto aplicado ao espaço de trabalho do trio — o que organiza o trabalho do agente *fora* do código. Ele é diferente do repo harness, que vive dentro do repositório de código e é o assunto da [seção 7](../7-repo-harness/TLDR.md). A regra de decisão que separa os dois: se a informação continua verdadeira quando outro time clona o repositório de código, ela é repo harness; se ela descreve como o trabalho está organizado — quais projetos existem, quem faz o quê esta semana, em qual Work Item —, ela é workspace.

## As convenções que o workspace impõe

O harness do workspace se materializa nas convenções que você já viu nas páginas anteriores desta seção, agora reunidas sob um nome. São elas que permitem a um agente chegar a um workspace desconhecido e operar corretamente.

A primeira convenção é a **cadeia de resolução**: `workspace do owner → projects/<project> → Work Item → fontes canônicas`. Um agente sempre resolve onde trabalhar por esse caminho, nunca por adivinhação. A segunda é a **separação entre persistente e trânsito**: fontes canônicas em `projects/`, auxiliares em `.coordination/` e `memory.md`. A terceira é o **isolamento de sessão**: cada execução usa sua própria pasta em `plans/assets/`, de modo que reexecuções não se sobrescrevem.

## As skills de base são o harness em ação

Aqui as peças se encaixam. As três skills de base — [`workspace-memory`, `workspace-projects` e `workspace-board`](../3-skills/skills-de-base.md) — são, na prática, o harness do workspace executável. Elas não produzem o entregável de nenhuma fase; elas garantem que o agente respeite as convenções do workspace antes de produzir qualquer coisa.

| Skill de base | Convenção que aplica |
|---|---|
| `workspace-memory` | retomar contexto e nunca tratar `memory.md` como fonte canônica |
| `workspace-projects` | localizar a fonte canônica correta e isolar assets por sessão |
| `workspace-board` | assumir e reconciliar Work Items com evidência |

Por isso elas são obrigatórias em toda missão: sem elas, o harness do workspace seria apenas uma convenção documentada, não uma convenção seguida.

## Quando vários agentes operam ao mesmo tempo

O harness do workspace ganha importância extra quando **vários agentes** trabalham em paralelo. As falhas que aparecem aí não são de qualidade — são de coordenação, e cada uma tem uma contramedida.

| Falha de coordenação | O que acontece | Contramedida |
|---|---|---|
| Sobrescrita silenciosa | dois agentes editam o mesmo arquivo; o último vence | um arquivo por unidade de trabalho; worktree por Work Item |
| Contenção em arquivo comum | vários atualizam o mesmo board ou log | consolidação por um coordenador |
| Perda de rastro | não se sabe qual agente produziu o quê | autoria e versão registradas em cada artefato |
| Handoff perdido | trabalho fica preso em trânsito | handoff só conclui na fonte canônica |

Note o paralelo com o repo harness: lá, o mesmo tipo de problema (vários agentes sobre o mesmo código) é resolvido por worktrees e identidades distintas. A ideia é a mesma dos dois lados da fronteira — **isolar a execução para que a colaboração não vire colisão**.

## Continue por aqui

Você fechou o lado de *fora* do código: como o trabalho do agente é organizado no workspace. A próxima seção atravessa a fronteira para o lado de *dentro* — o que um repositório de código carrega para ser operado por agentes com segurança. Siga para [Repositório da aplicação (harness)](../7-repo-harness/TLDR.md).
