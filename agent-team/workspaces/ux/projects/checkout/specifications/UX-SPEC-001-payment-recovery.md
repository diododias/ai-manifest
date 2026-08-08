---
id: UX-SPEC-001
project: checkout
status: draft
owner: ux-specification-agent
reviewer: ux
source: RESEARCH-001
updated_at: 2026-08-08
---

# Recuperação do pagamento

## Estados

- **Processando:** bloqueia reenvio acidental e anuncia progresso.
- **Sucesso:** confirma resultado e próximo passo.
- **Falha recuperável:** explica a ação segura disponível.
- **Resultado indeterminado:** não afirma falha; oferece consulta e orientação.
- **Conflito:** informa que a tentativa não corresponde à operação original e orienta retorno seguro.

## Conteúdo

Usar termos compreensíveis e validados; não expor chave técnica, stack trace ou estado interno do provedor.

## Acessibilidade

- mudança de estado anunciada sem mover foco inesperadamente;
- operação completa por teclado;
- progresso e resultado não dependem apenas de cor;
- mensagens associadas semanticamente ao pagamento e à ação.

## Critérios de UX

- [ ] Usuário distingue processamento, sucesso e estado indeterminado.
- [ ] Retry seguro preserva contexto e evita operação duplicada.
- [ ] Falhas oferecem próxima ação compreensível.
- [ ] Fluxo atende aos requisitos de teclado, foco e anúncio.
