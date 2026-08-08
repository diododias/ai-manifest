#!/usr/bin/env bash
set -euo pipefail

# Consolida cada workspace OpenClaw em um prompt independente.
# Uso:
#   ./build-full.sh         # gera <agente>/FULL.md para todos os agentes
#   ./build-full.sh --check # falha se algum FULL.md estiver desatualizado

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
mode="write"

usage() {
  cat <<'EOF'
Uso: build-full.sh [--check]

Opções:
  --check    verifica se cada <agente>/FULL.md corresponde às fontes
  -h, --help mostra esta ajuda
EOF
}

while (($# > 0)); do
  case "$1" in
    --check)
      mode="check"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Erro: opção desconhecida: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

write_file() {
  local agent_workspace="$1"
  local file_name="$2"
  local source_file="$agent_workspace/$file_name"
  local agent_id="${agent_workspace%/}"
  agent_id="${agent_id##*/}"

  printf '<!-- %s/%s -->\n' "$agent_id" "$file_name"
  cat "$source_file"
  printf '\n'
}

# Globbing ordenado torna o resultado estável e evita depender de registry.yaml.
for agent_workspace in "$script_dir"/*/; do
  [[ -d "$agent_workspace" ]] || continue

  agent_id="${agent_workspace%/}"
  agent_id="${agent_id##*/}"
  output_file="${agent_workspace%/}/FULL.md"
  tmp_file="$(mktemp "${TMPDIR:-/tmp}/agent-team-full.XXXXXXXX")"

  cleanup_agent() {
    rm -f "$tmp_file"
  }
  trap cleanup_agent EXIT

  for file_name in AGENTS.md SOUL.md IDENTITY.md USER.md; do
    if [[ ! -f "$agent_workspace/$file_name" ]]; then
      echo "Erro: ausente $agent_workspace/$file_name" >&2
      exit 1
    fi
  done

  {
    printf '# %s — Full Prompt\n\n' "$agent_id"
    cat <<'EOF'
Este arquivo reúne as instruções deste agente para ferramentas que aceitam um único prompt. O conteúdo é gerado por `build-full.sh`; edite os arquivos-fonte e regenere-o.

EOF
    write_file "$agent_workspace" AGENTS.md
    write_file "$agent_workspace" SOUL.md
    write_file "$agent_workspace" IDENTITY.md
    write_file "$agent_workspace" USER.md
  } >"$tmp_file"

  if [[ "$mode" == "check" ]]; then
    if [[ ! -f "$output_file" ]] || ! cmp -s "$tmp_file" "$output_file"; then
      echo "Desatualizado: $output_file (execute ./build-full.sh)" >&2
      exit 1
    fi
    echo "Atualizado: $output_file"
  else
    mv "$tmp_file" "$output_file"
    chmod 0644 "$output_file"
    echo "Gerado: $output_file"
  fi

  trap - EXIT
  rm -f "$tmp_file"
done
