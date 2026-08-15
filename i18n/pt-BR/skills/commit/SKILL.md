---
name: "commit"
description: "Prepara e cria um commit com escopo explícito e convenções do repositório. Use quando o usuário pedir para registrar mudanças em Git; só envie ao remoto se ele pedir push."
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Criar commits claros seguindo convenções do repositório, com referência à issue quando houver.

## Inputs

- **Obrigatório:** código modificado (git status)
- **Opcional:** mensagem personalizada via `$ARGUMENTS`
- **Opcional:** número da issue

## Execution Steps

### 1. Verificar estado

```bash
git status
git diff --stat
```

- Identifique todos os arquivos modificados/criados/deletados.
- Verifique se há arquivos que não devem ser commitados (secrets, temp).

### 2. Selecionar arquivos

- Adicione apenas arquivos relevantes para a feature.
- Nunca commite secrets, configs sensíveis ou artefatos temporários.
- Use `git add <arquivo>` para seleção explícita (evite `git add .`).

### 3. Montar mensagem de commit

Siga a convenção do repositório:

```
<tipo>(<escopo>): <descrição curta>

<corpo opcional>

Refs #<issue>
Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

**Tipos:** `feat`, `fix`, `chore`, `test`, `refactor`, `docs`, `style`, `perf`

**Regras:**
- Primera linha: max 72 caracteres, imperativo, sem ponto final.
- Corpo: explica o "porquê" (não o "o que").
- Referência à issue: `Refs #N` (parcial) ou `Closes #N` (completo).
- Co-Authored-By: quando aplicável (trabalho com IA).

### 4. Executar commit

- Mostre os arquivos selecionados e a mensagem proposta antes do commit se o
  usuário não tiver autorizado explicitamente o commit.

```bash
git commit -m "feat(feature-slug): descrição curta

Corpo do commit explicando a mudança.

Refs #N"
```

### 5. Push

- Faça push apenas quando o usuário o solicitar explicitamente ou quando ele
  tiver autorizado publicação como parte da tarefa.
- Antes de enviar, confirme branch remota e que não há arquivos não
  relacionados no índice.

```bash
git push origin <branch-name>
```

- Não presuma que CI abre PR nem que a base é `develop`.
- Se houver PR manual, proponha o próximo passo; não o abra implicitamente.

### 6. Reportar no chat

- Hash do commit curto.
- Arquivos incluídos.
- Branch e status do push.

## Convenções

- Um commit lógico = uma unidade de mudança.
- Não commite "WIP" ou "temp" — limpe antes.
- Mensagens em português (ou inglês se for padrão do repo).
- Sempre referencie a issue quando existir.

## Done When

- [ ] Arquivos selecionados corretamente
- [ ] Mensagem segue convenção do repositório
- [ ] Commit realizado com sucesso
- [ ] Push concluído, quando solicitado
- [ ] Hash do commit reportado
