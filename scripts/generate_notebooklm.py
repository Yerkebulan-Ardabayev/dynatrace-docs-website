#!/usr/bin/env python3
"""
Generate combined documentation files optimized for Google NotebookLM.

NotebookLM limits:
- Max 300 sources per notebook
- Max 500,000 words per source
- Supported: .txt, .md, .pdf, Google Docs, etc.

Strategy:
- Group markdown files by subcategory (2nd-level directory)
- If a group exceeds 400K words, split into parts
- Output as .md files in docs/notebooklm/
"""

import os
import sys
from pathlib import Path
from datetime import datetime

MAX_WORDS_PER_FILE = 400_000  # leave headroom under 500K limit
OUTPUT_DIR = Path("docs/notebooklm")


def get_subcategory(rel_path: Path) -> str:
    """Get grouping key from relative path."""
    parts = rel_path.parts
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return parts[0] if parts else "root"


def collect_groups(en_dir: Path) -> dict:
    """Group all markdown files by subcategory."""
    groups = {}
    for md_file in sorted(en_dir.rglob("*.md")):
        rel = md_file.relative_to(en_dir)
        key = get_subcategory(rel)
        if key not in groups:
            groups[key] = []
        groups[key].append(md_file)
    return groups


def read_file_safe(path: Path) -> str:
    """Read file with error handling."""
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def combine_files(files: list, category_name: str) -> str:
    """Combine multiple markdown files into one with clear separators."""
    parts = []
    parts.append(f"# Dynatrace Documentation: {category_name}\n")
    parts.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}\n")
    parts.append(f"Files combined: {len(files)}\n")
    parts.append("---\n")

    for f in files:
        content = read_file_safe(f).strip()
        if not content:
            continue
        # Add file path as context for RAG
        parts.append(f"\n## Source: {f.name}\n\n")
        parts.append(content)
        parts.append("\n\n---\n")

    return "\n".join(parts)


def word_count(text: str) -> int:
    return len(text.split())


def generate(en_dir: str = "docs/en", output_dir: str = "docs/notebooklm"):
    """Main generation function."""
    en_path = Path(en_dir)
    out_path = Path(output_dir)

    if not en_path.exists():
        print(f"Source directory not found: {en_path}")
        sys.exit(1)

    # Clean output directory
    if out_path.exists():
        for f in out_path.glob("*.md"):
            f.unlink()
    out_path.mkdir(parents=True, exist_ok=True)

    groups = collect_groups(en_path)
    print(f"Found {len(groups)} subcategories from {sum(len(v) for v in groups.values())} files\n")

    total_files_written = 0
    total_words = 0

    for key in sorted(groups.keys()):
        files = groups[key]
        combined = combine_files(files, key)
        words = word_count(combined)

        # Safe filename
        safe_name = key.replace("/", "__").replace("\\", "__")

        if words <= MAX_WORDS_PER_FILE:
            # Single file
            out_file = out_path / f"{safe_name}.md"
            out_file.write_text(combined, encoding="utf-8")
            total_files_written += 1
            total_words += words
            print(f"  {safe_name}.md  ({len(files)} docs, {words:,} words)")
        else:
            # Split into parts
            part_num = 1
            current_parts = []
            current_words = 0

            for f in files:
                content = read_file_safe(f).strip()
                if not content:
                    continue
                file_words = len(content.split())

                if current_words + file_words > MAX_WORDS_PER_FILE and current_parts:
                    # Write current part
                    part_content = combine_files(current_parts, f"{key} (Part {part_num})")
                    out_file = out_path / f"{safe_name}__part{part_num}.md"
                    out_file.write_text(part_content, encoding="utf-8")
                    print(f"  {out_file.name}  ({len(current_parts)} docs, {current_words:,} words)")
                    total_files_written += 1
                    total_words += current_words
                    part_num += 1
                    current_parts = []
                    current_words = 0

                current_parts.append(f)
                current_words += file_words

            # Write remaining
            if current_parts:
                part_content = combine_files(current_parts, f"{key} (Part {part_num})")
                out_file = out_path / f"{safe_name}__part{part_num}.md"
                out_file.write_text(part_content, encoding="utf-8")
                print(f"  {out_file.name}  ({len(current_parts)} docs, {current_words:,} words)")
                total_files_written += 1
                total_words += current_words

    # Also include Russian docs if available
    ru_path = Path("docs/ru")
    if ru_path.exists():
        ru_files = list(ru_path.rglob("*.md"))
        if ru_files:
            combined_ru = combine_files(ru_files, "Russian Translation (RU)")
            words_ru = word_count(combined_ru)
            if words_ru <= MAX_WORDS_PER_FILE:
                out_file = out_path / "russian_translation_all.md"
                out_file.write_text(combined_ru, encoding="utf-8")
                total_files_written += 1
                total_words += words_ru
                print(f"\n  russian_translation_all.md  ({len(ru_files)} docs, {words_ru:,} words)")

    print(f"\n{'='*60}")
    print(f"NotebookLM export complete!")
    print(f"  Files generated: {total_files_written}")
    print(f"  Total words:     {total_words:,}")
    print(f"  Output:          {out_path.absolute()}")
    print(f"  NotebookLM limit: 300 sources (used {total_files_written})")
    print(f"{'='*60}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate NotebookLM-ready docs")
    parser.add_argument("--en-dir", default="docs/en", help="English docs directory")
    parser.add_argument("--output", default="docs/notebooklm", help="Output directory")
    args = parser.parse_args()
    generate(args.en_dir, args.output)
