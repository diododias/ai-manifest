import sys
import re
import argparse
from pathlib import Path

def clean_vtt(input_path: str, output_path: str = None) -> None:
    """
    Lê um arquivo VTT de transcrição, remove os metadados e blocos de tempo,
    e junta as falas em um formato de texto limpo para reduzir o consumo de tokens.
    """
    path = Path(input_path)
    if not path.exists():
        print(f"Erro: Arquivo '{input_path}' não encontrado.")
        sys.exit(1)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remover o cabeçalho WEBVTT e metadados iniciais
    content = re.sub(r'^WEBVTT.*?\n\n', '', content, flags=re.MULTILINE | re.DOTALL)

    # Remover índices numéricos de blocos (se existirem, geralmente isolados em uma linha)
    content = re.sub(r'^\d+\n', '', content, flags=re.MULTILINE)

    # Remover linhas de timestamp (ex: 00:00:05.000 --> 00:00:10.000)
    # Suporta formatos com ou sem horas, milissegundos, etc.
    content = re.sub(r'^\d{2}:\d{2}.*?-->.*?\n', '', content, flags=re.MULTILINE)

    # Limpar tags de formatação VTT dentro do texto (ex: <v Speaker Name>, <b>, <i>, <c>)
    # Se for uma tag de voz <v Speaker Name>, transformamos em "Speaker Name:"
    content = re.sub(r'<v\s+([^>]+)>', r'\1: ', content)
    
    # Remover outras tags (ex: <i>, </i>, <c.color>, etc)
    content = re.sub(r'<[^>]+>', '', content)

    # Quebrar em linhas e remover espaços extras/linhas em branco excessivas
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            cleaned_lines.append(line)

    # Opcional: agrupar falas consecutivas do mesmo speaker (simplificado)
    # Isso ajuda ainda mais na legibilidade se a ferramenta de reunião gerar VTT linha a linha
    merged_lines = []
    current_speaker = None
    current_text = []

    for line in cleaned_lines:
        match = re.match(r'^([^:]+):\s*(.*)', line)
        if match:
            speaker = match.group(1).strip()
            text = match.group(2).strip()
            if speaker == current_speaker:
                current_text.append(text)
            else:
                if current_speaker is not None:
                    merged_lines.append(f"{current_speaker}: {' '.join(current_text)}")
                current_speaker = speaker
                current_text = [text]
        else:
            # Falas continuadas sem speaker explícito ou texto comum
            if current_speaker is not None:
                current_text.append(line)
            else:
                merged_lines.append(line)

    if current_speaker is not None:
        merged_lines.append(f"{current_speaker}: {' '.join(current_text)}")

    final_text = '\n\n'.join(merged_lines)

    if not output_path:
        # Se não fornecido output, salva como .txt no mesmo diretório
        output_path = path.with_suffix('.txt')
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_text)
        
    print(f"Limpeza concluída! Arquivo salvo em: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Limpa um arquivo de transcrição VTT, removendo timestamps e metadados para otimização de tokens (LLM).")
    parser.add_argument("input_vtt", help="Caminho para o arquivo VTT de entrada")
    parser.add_argument("-o", "--output", help="Caminho para o arquivo de texto de saída (opcional)", default=None)
    
    args = parser.parse_args()
    clean_vtt(args.input_vtt, args.output)

if __name__ == "__main__":
    main()
