---
title: Risco e autonomia progressiva
status: canonical
updated_at: 2026-08-09
---

# Risco e autonomia progressiva

> Como o modelo mede o peso de uma mudança (R0 a R4) e como decide quanto o sistema pode rodar sozinho (A0 a A4) — sem transformar autonomia em aposta.

## Duas escalas que trabalham juntas

O modelo separa duas perguntas que costumam ser confundidas. A primeira é "**quão arriscada é esta mudança?**", respondida pela classe de risco (R0 a R4). A segunda é "**quanto o sistema pode fazer sem intervenção humana?**", respondida pelo nível de autonomia (A0 a A4). Uma é sobre a mudança; a outra é sobre o sistema que a processa. Separá-las é o que permite dar autonomia alta para mudanças triviais e manter controle rígido sobre as perigosas — ao mesmo tempo, no mesmo time.

## Classes de risco: quanto verificar

A classe de risco define quanta verificação uma mudança exige antes de avançar. Quanto maior o risco, mais provas e mais aprovação humana. A classificação não é opinião: paths sensíveis elevam o risco automaticamente, e a dúvida não resolvida impede as classes mais baixas.

| Classe | Caracteriza | Exige |
|---|---|---|
| **R0 — mínimo** | documentação, texto e formatação; sem mudança de comportamento ou dados | merge automático após gates; review por amostragem |
| **R1 — baixo** | refatoração interna coberta por testes, sem migração nem integração crítica | aprovação curta; deploy automático com observação |
| **R2 — médio** | novo comportamento ou mudança de contrato interno; impacto reversível mas relevante | aprovação de produto ou Code Owner; canary e rollback |
| **R3 — alto** | dados persistidos, migrações, contratos públicos, autenticação, pagamentos | aprovação humana de produto e técnica antes de produção |
| **R4 — crítico** | impacto regulatório, financeiro, destrutivo ou de grande alcance | dupla aprovação, segregação de função e acompanhamento humano |

A regra de classificação tem uma proteção embutida contra otimismo: **um agente propõe o risco e outro tenta elevá-lo**, e o maior risco justificado prevalece. Reduzir a classe manualmente exige justificativa registrada, e qualquer mudança de escopo recalcula o risco do zero.

## Níveis de autonomia: quanto delegar

O nível de autonomia descreve quanto do fluxo acontece sem intervenção humana. Ele sobe devagar, e cada degrau troca uma aprovação manual por uma garantia estrutural.

| Nível | Significa |
|---|---|
| **A0 — assistido** | pessoas aprovam todas as transições |
| **A1 — execução autônoma** | agentes executam; pessoas aprovam decisões e merge |
| **A2 — merge por risco** | R0/R1 podem integrar por política |
| **A3 — entrega autônoma controlada** | baixo risco chega à produção com rollback comprovado |
| **A4 — orientado a exceções** | o fluxo saudável ocorre sem intervenção; pessoas tratam decisões e anomalias |

## A trava que impede a aposta

Este é o coração da página, e a regra que mais protege o modelo a longo prazo. **Elevar a autonomia exige seis condições ao mesmo tempo**: histórico suficiente, baixa taxa de falha, gates confiáveis, poucos falsos positivos, rollback testado e telemetria íntegra. Nenhuma delas, sozinha, autoriza a subida.

O motivo é que qualquer indicador isolado pode enganar. "Funcionou nas últimas dez vezes" pode ser sorte com amostra pequena. "A taxa de falha é baixa" pode significar que os gates não estão pegando os problemas. Só a combinação das seis condições transforma confiança em evidência. Por isso a revisão mensal do sistema tem uma regra própria: **nunca usar uma métrica isolada para elevar autonomia**.

## O elo com o repositório: a maturidade é o teto

Há um último princípio que conecta esta página ao [repo harness](../7-repo-harness/TLDR.md): a maturidade do harness é o **teto** da autonomia, nunca a consequência dela. Um repositório sem contexto, verificação, permissão e evidência adequados não pode operar com autonomia alta, por mais que o histórico pareça bom — porque falta a estrutura que tornaria esse histórico confiável. Se você encontrar um repositório operando acima do que seu harness sustenta, não é um repositório adiantado: é um gate faltando que ninguém percebeu ainda.

## Continue por aqui

Com risco e autonomia claros, o próximo passo é entender os **procedimentos** que padronizam o trabalho dos agentes em cada nível de risco — as [Skills](../3-skills/TLDR.md).
