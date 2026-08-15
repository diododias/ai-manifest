---
name: analyse-bug
description: Analisa evidências de um bug, rastreia causa raiz e documenta impacto sem implementar correções. Use ao receber logs, prints, erros ou descrições de comportamento incorreto.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Analisar o problema reported, rastrear a causa raiz, identificar componentes afetados e gerar documentação estruturada.

## Contrato de artefatos

Antes de criar um relatório, siga [o contrato compartilhado](../references/workflow-contract.md).

## Inputs

- **Obrigatório:** evidência do bug (log, print, descrição, erro)
- **Opcional:** contexto adicional (quando aconteceu, frequency, impacto)

## Execution Steps

### 1. Coletar evidência

- Colete toda a informação disponível: logs, prints, stack traces,Descrição do comportamento esperado vs obtido.
- Se `$ARGUMENTS` for vazio, peça evidência ao usuário.

### 2. Classificar o bug

| Dimensão | Opção |
|----------|-------|
| Severidade | 🔴 Crash / 🟠 Funcional / 🟡 UI / 🔵 Cosmético |
| Impacto | Todos usuários / Alguns / Edge case |
| Recorrência | Sempre / Intermitente / Uma vez |
| Componente | Backend / Frontend / Infra / Database |

### 3. Rastrear causa raiz

Analise a evidência para identificar:

- **Sintoma:** o que o usuário/sistema apresenta.
- **Causa imediata:** o que no código/config causou o sintoma.
- **Causa raiz:** por que o código/config estava assim (falta de validação, race condition, etc.).

Use técnicas:
- Stack trace → arquivo → função → lógica.
- Log analysis → sequência de eventos.
- Reprodução → passos para recriar.

### 4. Identificar componentes afetados

| Componente | Arquivo | Função/Método | Impacto |
|-----------|---------|---------------|---------|
| ... | ... | ... | ... |

### 5. Documentar o bug

Gere `bugs/bug-<NOME-SLUG>.md`:

```markdown
# Bug: <Título>

**ID:** BUG-<NNN>
**Data:** <YYYY-MM-DD>
**Severidade:** 🔴/🟠/🟡/🔵
**Status:** 🟡 Analisado

---

## Sintoma

<o que acontece — comportamento observável>

## Comportamento Esperado

<o que deveria acontecer>

## Evidência

<logs, prints, stack traces — colar trechos relevantes>

## Causa Raiz

<análise técnica do porquê acontece>

## Componentes Afetados

| Componente | Arquivo | Função |
|-----------|---------|--------|
| ... | ... | ... |

## Passos para Reproduzir

1. <passo 1>
2. <passo 2>
3. <passo 3>

**Resultado:** <erro/bug>
**Esperado:** <comportamento correto>

## Impacto

- **Usuários:** <afeta todos/alguns/edge case>
- **Dados:** <perda/corrupção/dados OK>
- **Performance:** <sim/não/leve>

## Sugestão de Correção

<direção da correção — não implementar ainda>

## Referências

- <links, issues, PRs relacionados>
```

### 6. Reportar no chat

- Resumo: sintoma, causa raiz, severidade.
- Componentes afetados.
- Caminho para correção sugerido.
- Se precisa de mais informação para análise completa.

## Convenções

- Nunca implemente a correção — apenas analise.
- Documente com evidências, não suposições.
- Causa raiz é "por que" — não "o que" (sintoma).
- Português.

## Done When

- [ ] Evidência coletada e analisada
- [ ] Causa raiz identificada
- [ ] Componentes afetados mapeados
- [ ] `bug-<NOME>.md` gerado em `bugs/`
- [ ] Resumo reportado no chat
