#!/usr/bin/env python3
"""
Cleanup scraped documentation artifacts:
1. Remove duplicate h1 headings (when title: in front matter matches # Title)
2. Remove scraped metadata bullet lists (version, category, read time, publish date)
3. Fix BOM characters (ï»¿ → empty)
4. Remove excessive blank lines after cleanup
"""

import re
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"

# Patterns for scraped metadata lines to remove
METADATA_PATTERNS = [
    r'^\*\s*(Последняя версия|Текущая версия|Latest version).*$',
    r'^\*\s*(Обзор|Overview|Приложение|Application|App|Classic)$',
    r'^\*\s*(Время чтения|Чтение|Read time|Reading time).*$',
    r'^\*\s*(Опубликовано|Обновлено|Published|Updated).*$',
    r'^\*\s*(Dynatrace Managed|Dynatrace SaaS)$',
    r'^\*\s*(Руководство|Guide|Практическое руководство|How-to)$',
    r'^\*\s*(Ссылка|Reference|Справочник)$',
    r'^\*\s*(Концепция|Concept)$',
]

METADATA_RE = re.compile('|'.join(METADATA_PATTERNS), re.MULTILINE | re.IGNORECASE)

# BOM artifacts
BOM_PATTERN = re.compile(r'ï»¿')


def extract_front_matter(content: str):
    """Extract title from YAML front matter."""
    if not content.startswith('---'):
        return None, content

    end = content.find('---', 3)
    if end == -1:
        return None, content

    fm = content[3:end].strip()
    body = content[end + 3:].lstrip('\n')

    title = None
    for line in fm.split('\n'):
        if line.startswith('title:'):
            title = line[6:].strip().strip('"').strip("'")
            break

    return title, body


def rebuild_with_front_matter(content: str, body: str):
    """Rebuild file with original front matter + cleaned body."""
    if not content.startswith('---'):
        return body

    end = content.find('---', 3)
    fm_block = content[:end + 3]
    return fm_block + '\n\n' + body.lstrip('\n')


def clean_file(filepath: Path, dry_run=False) -> dict:
    """Clean a single markdown file. Returns dict of changes made."""
    changes = {'h1_removed': False, 'metadata_removed': 0, 'bom_fixed': 0}

    content = filepath.read_text(encoding='utf-8')
    original = content

    title, body = extract_front_matter(content)

    if title is None:
        # No front matter, skip h1 dedup
        body = content
        has_fm = False
    else:
        has_fm = True

    lines = body.split('\n')
    cleaned_lines = []
    h1_removed = False
    metadata_removed = 0
    i = 0

    while i < len(lines):
        line = lines[i]

        # Remove duplicate h1 if it matches front matter title
        if not h1_removed and title and line.startswith('# '):
            h1_text = line[2:].strip()
            # Fuzzy match - titles might differ slightly
            if (h1_text == title or
                h1_text.lower() == title.lower() or
                h1_text.replace('—', '-').strip() == title.replace('—', '-').strip()):
                h1_removed = True
                changes['h1_removed'] = True
                i += 1
                # Skip blank lines after removed h1
                while i < len(lines) and lines[i].strip() == '':
                    i += 1
                continue

        # Remove metadata bullet lines
        if METADATA_RE.match(line.strip()):
            metadata_removed += 1
            changes['metadata_removed'] += 1
            i += 1
            continue

        cleaned_lines.append(line)
        i += 1

    body = '\n'.join(cleaned_lines)

    # Fix BOM characters
    bom_count = len(BOM_PATTERN.findall(body))
    if bom_count:
        body = BOM_PATTERN.sub('', body)
        changes['bom_fixed'] = bom_count

    # Remove excessive blank lines (3+ → 2)
    body = re.sub(r'\n{4,}', '\n\n\n', body)

    # Rebuild with front matter
    if has_fm:
        result = rebuild_with_front_matter(content, body)
    else:
        result = body

    if result != original:
        if not dry_run:
            filepath.write_text(result, encoding='utf-8')
        return changes

    return {}


def main():
    dry_run = '--dry-run' in sys.argv

    dirs_to_clean = [DOCS_DIR / 'ru', DOCS_DIR / 'managed']
    total_changes = {'files': 0, 'h1_removed': 0, 'metadata_removed': 0, 'bom_fixed': 0}

    for docs_dir in dirs_to_clean:
        if not docs_dir.exists():
            continue

        for md_file in sorted(docs_dir.rglob('*.md')):
            changes = clean_file(md_file, dry_run=dry_run)
            if changes:
                total_changes['files'] += 1
                if changes.get('h1_removed'):
                    total_changes['h1_removed'] += 1
                total_changes['metadata_removed'] += changes.get('metadata_removed', 0)
                total_changes['bom_fixed'] += changes.get('bom_fixed', 0)

                if dry_run or '-v' in sys.argv:
                    detail = []
                    if changes.get('h1_removed'): detail.append('h1')
                    if changes.get('metadata_removed'): detail.append(f"{changes['metadata_removed']} meta")
                    if changes.get('bom_fixed'): detail.append(f"{changes['bom_fixed']} bom")
                    print(f"  {'[DRY] ' if dry_run else ''}Fixed {md_file.relative_to(DOCS_DIR)}: {', '.join(detail)}")

    prefix = '[DRY RUN] ' if dry_run else ''
    print(f"\n{prefix}Cleanup complete:")
    print(f"  Files modified: {total_changes['files']}")
    print(f"  Duplicate h1 removed: {total_changes['h1_removed']}")
    print(f"  Metadata lines removed: {total_changes['metadata_removed']}")
    print(f"  BOM characters fixed: {total_changes['bom_fixed']}")


if __name__ == '__main__':
    main()
