# Repositórios locais

`repos/registry.yaml` registra os clones esperados. O código fica em `github/<organização>/<repositório>/`; missões concorrentes usam `worktrees/<organização>/<repositório>/<work-item>/`.

## Fluxo recomendado

1. Confirme organização, repositório e branch padrão no registro.
2. Clone em `repos/github/` e leia as instruções do próprio repositório.
3. Verifique o estado Git antes de criar uma missão.
4. Crie branch e worktree identificados pelo Work Item.
5. Registre os caminhos no Work Item antes de alterar código.
6. Remova o worktree somente após preservar commits e evidências.

Os checkouts são ignorados pelo `.gitignore` deste exemplo. Nunca documente SHA ou limpeza do checkout como se fossem estado permanente; consulte o Git diretamente.
