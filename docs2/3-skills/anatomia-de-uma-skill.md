---
title: Anatomia de uma skill
status: canonical
updated_at: 2026-08-09
---

# Anatomia de uma skill

> Como uma skill é estruturada em disco, o que a descrição precisa comunicar para ser acionada e por que uma skill se lê diferente de documentação para humanos.

## Uma skill é um diretório

No nível mais concreto, uma skill é um diretório com um arquivo `SKILL.md` na raiz. Esse arquivo carrega o procedimento; os demais existem para dar suporte a ele quando necessário.

```text
skills/<nome>/
├── SKILL.md        # o procedimento: entrada, passos, saída e critério de conclusão
├── README.md       # contexto adicional, quando o procedimento não se explica sozinho
├── templates/      # formatos de artefato que a skill produz
└── agents/         # configuração de agente específica, quando houver
```

O `SKILL.md` começa com um front matter que declara `name` e `description`. Desses dois, a **descrição é o campo mais importante** — e a razão surpreende quem está começando.

## A descrição é o que aciona a skill

A descrição não é um resumo cosmético. Ela é o texto que um agente lê para decidir se a skill se aplica à missão em curso. Uma descrição que só diz **o que** a skill faz, sem dizer **em que situação usá-la**, produz uma skill que existe mas nunca é acionada no momento certo.

Por isso a descrição precisa responder duas coisas ao mesmo tempo: o que a skill faz e quando ela deve ser usada. "Revisa um PRD" é fraco. "Revisa um PRD verificando rastreabilidade de objetivos, regras e critérios; use antes de aprovar qualquer PRD ou quando gaps de requisito são suspeitos" é o que faz a skill ser encontrada quando importa.

## O critério de parada separa skill de tutorial

Toda skill declara objetivo, inputs, outputs, tools permitidas, critérios de parada, exemplos e testes. De todos esses campos, o **critério de parada** é o que mais distingue uma skill de um tutorial genérico.

O motivo é comportamental: um agente que não sabe se terminou continua. Sem um critério explícito de conclusão — "a skill termina quando cada critério de aceite tem evidência vinculada" —, o agente ou para cedo demais, deixando trabalho pela metade, ou tarde demais, gerando ruído. O critério de parada é o que torna a conclusão verificável em vez de subjetiva.

## Convenções de artefato: a regra local prevalece

Skills que compartilham convenções de onde gravam artefatos apontam para um contrato de artefatos comum, que define onde PRD, SPEC, planos e requisitos vivem. Esse contrato carrega uma regra central que vale memorizar: **a convenção local do repositório prevalece**. Quando o repositório consumidor organiza os artefatos de um jeito diferente do padrão, a skill se adapta ao layout local e confirma o mapeamento antes de escrever — nunca impõe sua própria estrutura por cima.

## Por que uma skill se lê diferente desta wiki

Se você abrir um `SKILL.md`, vai notar que ele parece o oposto do que esta wiki prega: listas densas, imperativas, sem a prosa que suaviza a leitura humana. Isso é intencional, e a razão é o leitor. Esta wiki é lida por **pessoas** que estão aprendendo; um `SKILL.md` é lido por um **agente durante a execução**, que se beneficia de instruções compactas e diretas.

Em outras palavras: o padrão de documentação que favorece prosa e tabelas se aplica aos documentos de leitura humana. Instruções executadas por agentes — os `SKILL.md` e os pacotes de agente — seguem regras próprias de concisão, e listas densas ali são uma escolha correta, não um descuido.

## Continue por aqui

Você entende agora o que é uma skill, quando ela é acionada e como é escrita. O passo natural é conhecer **quem** executa essas skills — os [Agentes](../4-agentes/TLDR.md).
