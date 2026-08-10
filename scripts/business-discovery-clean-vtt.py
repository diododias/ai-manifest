import sys
import re
import argparse
from pathlib import Path

def clean_vtt(input_path: str, output_path: str = None) -> None:
    """
    Reads a VTT transcript file, removes metadata and timestamp blocks,
    and joins utterances into a clean text format to reduce token usage.
    """
    path = Path(input_path)
    if not path.exists():
        print(f"Error: File '{input_path}' was not found.")
        sys.exit(1)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the WEBVTT header and initial metadata.
    content = re.sub(r'^WEBVTT.*?\n\n', '', content, flags=re.MULTILINE | re.DOTALL)

    # Remove numeric block indexes (when present, usually on a separate line).
    content = re.sub(r'^\d+\n', '', content, flags=re.MULTILINE)

    # Remove timestamp lines (for example, 00:00:05.000 --> 00:00:10.000).
    # Supports formats with or without hours, milliseconds, and so on.
    content = re.sub(r'^\d{2}:\d{2}.*?-->.*?\n', '', content, flags=re.MULTILINE)

    # Remove VTT formatting tags from the text (for example, <v Speaker Name>, <b>, <i>, <c>).
    # A voice tag such as <v Speaker Name> becomes "Speaker Name:".
    content = re.sub(r'<v\s+([^>]+)>', r'\1: ', content)
    
    # Remove other tags (for example, <i>, </i>, <c.color>, and so on).
    content = re.sub(r'<[^>]+>', '', content)

    # Split into lines and remove extra whitespace and excessive blank lines.
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            cleaned_lines.append(line)

    # Optionally group consecutive utterances from the same speaker (simplified).
    # This further improves readability when the meeting tool generates VTT line by line.
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
            # Continued utterances without an explicit speaker, or ordinary text.
            if current_speaker is not None:
                current_text.append(line)
            else:
                merged_lines.append(line)

    if current_speaker is not None:
        merged_lines.append(f"{current_speaker}: {' '.join(current_text)}")

    final_text = '\n\n'.join(merged_lines)

    if not output_path:
        # If no output path is provided, save as .txt in the same directory.
        output_path = path.with_suffix('.txt')
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_text)
        
    print(f"Cleanup complete. File saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Cleans a VTT transcript file by removing timestamps and metadata for token optimization (LLM).")
    parser.add_argument("input_vtt", help="Path to the input VTT file")
    parser.add_argument("-o", "--output", help="Path to the output text file (optional)", default=None)
    
    args = parser.parse_args()
    clean_vtt(args.input_vtt, args.output)

if __name__ == "__main__":
    main()
