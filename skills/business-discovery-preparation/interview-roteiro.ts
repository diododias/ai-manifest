/**
 * Workflow: Entrevista Roteiro para Business Discovery Preparation
 *
 * Entrevista interativa com PM pra preencher roteiro de agenda.
 * Permite skip em qualquer seção, flagra gaps, gera documento estruturado.
 */

export const meta = {
  name: 'interview-roteiro',
  description: 'Entrevista PM sobre roteiro de agenda. [PROGRESSIVE DISCLOSURE] Ativar quando a PM for preparar alinhamento/discovery ou estruturar uma demanda vaga antes de envolver engenharia.',
  phases: [
    { title: 'Setup', detail: 'Identificar feature e caminhos' },
    { title: 'Entrevista', detail: 'Questionar cada seção do roteiro' },
    { title: 'Processamento', detail: 'Estruturar respostas e detectar gaps' },
    { title: 'Geração', detail: 'Montar documento final' },
  ],
};

// Seções do roteiro em ordem
const ROTEIRO_SECTIONS = [
  {
    id: '0-contexto',
    title: 'Contexto em voz alta',
    description: 'O que é, qual épico, por que agora',
    mandatory: true,
    prompt: `Por favor, explique em voz alta: o que é esta demanda/feature, qual épico ela se encaixa, e por que agora é o momento certo?

Tente ser bem explícito — é o contexto que "todo mundo já sabe" mas que costuma desaparecer na transcrição depois.`,
  },
  {
    id: '1-recap',
    title: 'Recap do já decidido',
    description: 'Contexto implícito das agendas anteriores',
    mandatory: false,
    prompt: `Se você já teve agendas sobre isso antes, qual foi a última coisa que fechou? O que decidimos semana/mês passado?

Format: "Última vez fechamos X, Y. Hoje é sobre Z."

(Pule se for a primeira agenda sobre isto)`,
  },
  {
    id: '2-problema-negocio',
    title: 'Problema de negócio',
    description: 'Dor, quem sofre, métrica COM número',
    mandatory: true,
    prompt: `Que dor ou problema estamos resolvendo?

**Preencha os 3 pontos:**
1. **Qual é a dor?** (descrição)
2. **Pra quem?** (que perfil, role, ou segmento de usuário)
3. **Métrica de sucesso — COM NÚMERO** (ex: "reduzir tempo em 50%", "aumentar conversão de 10% pra 30%")

⚠️ Adjetivo vago ("mais rápido", "melhor") sem número volta como gap.`,
  },
  {
    id: '3-fluxo-principal',
    title: 'Fluxo principal (happy path)',
    description: 'Passo a passo, quem faz o quê, prioridades',
    mandatory: true,
    prompt: `Descreva o fluxo principal (happy path) passo a passo:
- Quem faz o quê
- Em que ordem
- **Qual é a prioridade de cada passo?** (P1 = MVP, sem isso não entrega valor; P2/P3 = incremento)

Format:
1. [Passo 1] — P1/P2/P3
2. [Passo 2] — P1/P2/P3
...`,
  },
  {
    id: '4-regras-negocio',
    title: 'Regras de negócio',
    description: 'Cada regra com exemplo concreto/numérico',
    mandatory: false,
    prompt: `Que regras de negócio o sistema deve seguir?

**Pra cada regra, forneça:**
1. O **gatilho ou estado** (quando, enquanto, se...)
2. O que **o sistema deve fazer** (ação/resposta)
3. Um **exemplo concreto/numérico** (é isso que a IA não consegue inferir)

Format:
**RN-1:** [gatilho] → [o sistema deve] [ação]
*Exemplo:* [caso real com números/valores]

(Se não tiver regra explícita, pule)`,
  },
  {
    id: '5-excecoes',
    title: 'Exceções / edge cases',
    description: 'Erros, limites, estados inválidos',
    mandatory: false,
    prompt: `Que exceções ou edge cases devemos considerar?

- Entrada inválida? (ex: e-mail errado, negativo, vazio)
- Limites? (ex: máximo de usuários, capacidade esgotada)
- Concorrência? (dois requests simultâneos)
- Estados inválidos ou contraditos?

(Pule se não tiver casos especiais)`,
  },
  {
    id: '6-fora-escopo',
    title: 'Fora de escopo',
    description: 'O que explicitamente NÃO vamos fazer',
    mandatory: false,
    prompt: `O que está **fora de escopo** desta demanda? O que você explicitamente NÃO quer fazer (pelo menos por agora)?

Format:
- [Item 1]
- [Item 2]

(Pule se tudo tá dentro de escopo)`,
  },
  {
    id: '7-cenarios',
    title: 'Cenários de aceite',
    description: 'Dado / Quando / Então em Gherkin',
    mandatory: false,
    prompt: `Por favor, descreva **cenários testáveis** pra cada história de usuário ou caso importante.

Use **Gherkin português:**
**Cenário X:**
- **Dado** [contexto inicial]
- **Quando** [ação do usuário]
- **Então** [resultado esperável observável]

⚠️ O "Então" é crucial — é o resultado que você observa, não uma ação. Exemplo certo: "vê mensagem de sucesso". Errado: "o sistema processa".

(Inclua cenários de exceção tb, se relevante)`,
  },
  {
    id: '8-duvidas',
    title: 'Dúvidas em aberto',
    description: 'O que ainda não tá respondido',
    mandatory: false,
    prompt: `Que dúvidas ou incertezas ainda ficaram? Coisas que você precisa confirmar com alguém?

Format:
- **DA-1** [pergunta] *(dono: quem, prazo: quando)*
- **DA-2** [pergunta] *(dono: quem, prazo: quando)*

(Pule se tá tudo claro)`,
  },
  {
    id: '9-materiais',
    title: 'Materiais de apoio',
    description: 'Links, mockups, documentações',
    mandatory: false,
    prompt: `Que materiais você traz pra esta reunião? Links, mockups, planilhas, documentos?

Format:
- [Descrição]: [link]
- [Descrição]: [link]

(Pule se não tiver materiais)`,
  },
];

// ============================================================================
// Main workflow
// ============================================================================

phase('Setup');

// 1. Solicitar feature slug
log('Iniciando Business Discovery Preparation...');

const featureInfo = await agent(
  `PM vai preencher roteiro de agenda. Pergunte:
  1. Como se chama a feature/épico? (nome/slug)
  2. Qual é a demanda em 1 linha?
  3. Tem material já preparado (links, docs, mockups)?
  4. Primeiro vez falando sobre isso ou já teve agendas antes?

  Responda com JSON: { featureSlug, demandaOneLiner, hasMaterial, isFirstTime }`,
  {
    label: 'setup-feature-info',
    phase: 'Setup',
    schema: {
      type: 'object',
      properties: {
        featureSlug: { type: 'string' },
        demandaOneLiner: { type: 'string' },
        hasMaterial: { type: 'boolean' },
        isFirstTime: { type: 'boolean' },
      },
      required: ['featureSlug', 'demandaOneLiner'],
    },
  }
);

log(`Feature: ${featureInfo.featureSlug} — ${featureInfo.demandaOneLiner}`);

// 2. Se tiver material, ler e oferece dois caminhos
let materialsContext = '';
if (featureInfo.hasMaterial) {
  materialsContext = await agent(
    `PM vai descrever material que trouxe (links, docs).
    Peça para descrever brevemente cada um (nome + o que é).
    Compile em texto corrido pra usar como contexto.`,
    {
      label: 'setup-materials',
      phase: 'Setup',
    }
  );
  log('Materiais carregados para contexto...');
}

// 3. Escolher caminho: zero vs com material
const pathChoice = await agent(
  `PM quer preencher roteiro. Oferça 2 caminhos:

  **Zero:** entrevista completa sobre cada seção do roteiro.
  **Com material:** lê o que já existe, depois aprofunda em gaps.

  ${featureInfo.hasMaterial ? 'Tem material (${materialsContext}), então oferça ambas.' : 'Sem material, sugira Zero.'}

  Responda com JSON: { path: "zero" | "com-material" }`,
  {
    label: 'setup-path-choice',
    phase: 'Setup',
    schema: {
      type: 'object',
      properties: {
        path: { type: 'string', enum: ['zero', 'com-material'] },
      },
      required: ['path'],
    },
  }
);

log(
  `Caminho escolhido: ${pathChoice.path}${
    featureInfo.hasMaterial ? ' (com material)' : ' (do zero)'
  }`
);

phase('Entrevista');

// ============================================================================
// Interview loop
// ============================================================================

const responses = new Map<string, string>();
const skipped = new Set<string>();

// Função auxiliar: perguntar e capturar
async function askSection(
  section: (typeof ROTEIRO_SECTIONS)[0]
): Promise<void> {
  const sectionLabel = section.id;

  log(`Seção: ${section.title}`);

  // Perguntar principal
  const answer = await agent(
    `${section.description}

${section.prompt}`,
    {
      label: `roteiro-${sectionLabel}`,
      phase: 'Entrevista',
    }
  );

  if (!answer || answer.toLowerCase().includes('skip')) {
    skipped.add(sectionLabel);
    log(`⏩ Seção ${section.title} pulada.`);
  } else {
    responses.set(sectionLabel, answer);

    // Confirmar o que entendeu
    const confirm = await agent(
      `Você respondeu sobre "${section.title}":

---
${answer}
---

Você quer:
a) Editar/revisar esta resposta?
b) Prosseguir pra próxima seção?
c) Pular esta seção e continuar?

Responda com JSON: { action: "edit" | "next" | "skip" }`,
      {
        label: `roteiro-${sectionLabel}-confirm`,
        phase: 'Entrevista',
        schema: {
          type: 'object',
          properties: {
            action: { type: 'string', enum: ['edit', 'next', 'skip'] },
          },
          required: ['action'],
        },
      }
    );

    if (confirm.action === 'edit') {
      log('Reentrando seção pra edição...');
      await askSection(section);
    } else if (confirm.action === 'skip') {
      responses.delete(sectionLabel);
      skipped.add(sectionLabel);
      log(`⏩ Seção ${section.title} pulada após resposta.`);
    }
  }
}

// Rodar entrevista em seções — permitir skip em não-obrigatórias
for (const section of ROTEIRO_SECTIONS) {
  if (section.mandatory) {
    await askSection(section);
  } else {
    // Perguntar se quer responder
    const wantToRespond = await agent(
      `**${section.title}**

${section.description}

Quer responder sobre isto?
- Sim, responder agora
- Não, pular e confirmar na agenda

(Type "sim" ou "não" / "skip")`,
      {
        label: `roteiro-${section.id}-want`,
        phase: 'Entrevista',
      }
    );

    if (
      !wantToRespond.toLowerCase().includes('não') &&
      !wantToRespond.toLowerCase().includes('skip')
    ) {
      await askSection(section);
    } else {
      skipped.add(section.id);
      log(`⏭️ ${section.title} será confirmada na agenda.`);
    }
  }
}

phase('Processamento');

// ============================================================================
// Process responses: detectar gaps
// ============================================================================

log('Analisando gaps e incoerências...');

const gapReport = await agent(
  `Analise as respostas pra detectar gaps comuns:

**Respostas capturadas:**
${Array.from(responses.entries())
  .map(([id, resp]) => `**${id}:**\n${resp}`)
  .join('\n\n')}

**Procure por:**
1. Métrica vaga (ex: "rápido" sem número) em Problema de Negócio
2. Regras sem exemplo concreto/numérico
3. Cenários sem "Então" claro (resultado observável)
4. Referências não definidas ("aquele fluxo", "do jeito que...")
5. Prioridades não definidas em passos do fluxo

**Responda com JSON:**
\`\`\`json
{
  "gaps": [
    { "sectionId": "...", "type": "metrica-vaga" | "sem-exemplo" | "sem-entao" | "referencia-vaga" | "prioridade-vaga", "detail": "descrição" }
  ],
  "summary": "X gaps encontrados"
}
\`\`\``,
  {
    label: 'gap-detection',
    phase: 'Processamento',
    schema: {
      type: 'object',
      properties: {
        gaps: {
          type: 'array',
          items: {
            type: 'object',
            properties: {
              sectionId: { type: 'string' },
              type: { type: 'string' },
              detail: { type: 'string' },
            },
          },
        },
        summary: { type: 'string' },
      },
      required: ['gaps', 'summary'],
    },
  }
);

log(`⚠️  ${gapReport.summary}`);
if (gapReport.gaps.length > 0) {
  for (const gap of gapReport.gaps) {
    log(`  • ${gap.sectionId}: ${gap.detail}`);
  }
}

phase('Geração');

// ============================================================================
// Generate document
// ============================================================================

log('Gerando documento final...');

const document = await agent(
  `Monte um arquivo Markdown pronto pra usar como roteiro de agenda.

**Inputs:**
- Feature: ${featureInfo.featureSlug}
- Demanda: ${featureInfo.demandaOneLiner}
- Respostas capturadas: ${Array.from(responses.keys()).join(', ')}
- Seções puladas: ${Array.from(skipped).join(', ') || 'nenhuma'}
- Gaps detectados: ${gapReport.gaps.map((g) => g.sectionId).join(', ') || 'nenhum'}

**Estrutura base:**
# Roteiro de Agenda — [feature]
- **Data:** TBD
- **Participantes:** [usuário], [PM], [outros]
- **Demanda:** [1 linha]
- **Gravação:** TBD
- **Material de referência:** [links/docs]

## [0 a 9]. [Nome da Seção]
[Conteúdo ou PENDENTE se pulado]

---
## ⚠️ Gaps detectados neste roteiro
[Lista de gaps]

**Regras:**
1. Preencha as seções com as respostas capturadas.
2. Seções puladas ficam como [PENDENTE — confirmar na agenda].
3. Liste os gaps detectados no fim.

Retorne o markdown puro (sem \`\`\`).`,
  {
    label: 'generate-document',
    phase: 'Geração',
  }
);

log('Documento gerado.');

// ============================================================================
// Output
// ============================================================================

// Salvar documento em disco (fora do workflow, vai ser tratado pela skill)
// Aqui retornamos o documento e metadados

return {
  featureSlug: featureInfo.featureSlug,
  demandaOneLiner: featureInfo.demandaOneLiner,
  document: document,
  responses: Object.fromEntries(responses),
  skipped: Array.from(skipped),
  gaps: gapReport.gaps,
  gapSummary: gapReport.summary,
  materialsContext: materialsContext || null,
  path: `business-discovery-preparation/${featureInfo.featureSlug}/roteiro-preenchido.md`,
};
