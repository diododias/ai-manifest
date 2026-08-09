---
title: Workflow — validação adversarial
status: proposed
updated_at: 2026-08-08
---

# Workflow — validação adversarial

Valida a mudança por perspectivas independentes e converte achados em um evidence pack único. Os reviewers não assumem que o resultado dos testes do autor é suficiente.

| Aspecto | Contrato |
|---|---|
| Entrada | diff, PRD, UX spec, SPEC, `CHECKLIST.md`, resultados locais e risco |
| Consolida | QA / Validation Agent |
| Colaboram | Security Review; Architecture Review; Adversarial Code Reviewer |
| Saída | checklist comprovado, findings classificados, evidências reproduzíveis e recomendação de gate |
| Owner humano | Tech Lead; PM e UX para seus critérios |
| Gate | todos os checks obrigatórios aprovados e nenhum bloqueador aberto |

```mermaid
flowchart LR
    A[Mudança pronta] --> B[QA\ncritérios e cenários]
    A --> C[Security\nsegurança e privacidade]
    A --> D[Architecture\nfronteiras e contratos]
    A --> E[Code Reviewer\ncorretude e manutenção]
    B --> F[QA\nconsolida evidence pack]
    C --> F
    D --> F
    E --> F
    F --> G{CI fast e deep lanes}
    G -- falha corrigível --> H[Implementação]
    G -- aprovado --> I[PR e merge]
    G -- exceção --> J[Tech Lead]
```

## Sequência

1. O QA Agent deriva cobertura da `CHECKLIST.md` e executa cenários nominal, erro, recuperação, regressão e casos-limite.
2. Security, Architecture e Code Reviewer investigam em paralelo seus domínios e apresentam findings com evidência, severidade, impacto e ação sugerida.
3. O QA Agent consolida sem silenciar divergências, mapeando cada critério para evidência ou gap.
4. CI decide os checks requeridos pela classe de risco e pelos paths alterados. Findings corrigíveis voltam à implementação; toda correção material recebe nova validação proporcional.

## Encerramento

Antes de fechar a rodada, registre:

| Artefato | Destino | Obrigatório |
|---|---|---|
| Review do Code Reviewer | `execution/reviews/code-<WI-id>.md` | sim |
| Review do Security Agent | `execution/reviews/security-<WI-id>.md` | quando aplicável |
| Review do Architecture Agent | `execution/reviews/architecture-<WI-id>.md` | quando aplicável |
| Evidence pack consolidado (QA Agent) | `execution/evidence/<WI-id>.md` | sim |
| Work Item atualizado | `work-items/<WI-id>.md` — status e link para evidence | sim |
| STATUS.md | fase `review`, próximo gate: `PR / loop back` | sim |

Achados abertos em qualquer review bloqueiam o gate. Cada resolução exige evidência referenciada no arquivo de review correspondente, não apenas texto.

## Escalonamento

Escalar falso positivo, exceção, requisito ausente ou divergência sem regra de desempate. O QA Agent não pode fechar sozinho um achado de outro reviewer sem evidência de revalidação.
