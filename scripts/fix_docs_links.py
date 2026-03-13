#!/usr/bin/env python3
"""
Fix broken /docs/ absolute links in MkDocs markdown files.

All internal links use '/docs/X' absolute paths from the original Dynatrace docs,
but this MkDocs site serves at '/dynatrace-docs-website/'. This script converts
them to relative .md links that MkDocs can resolve correctly.

Strategy:
- For a file in docs/{lang}/a/b/c.md linking to /docs/x/y/z
- Find the target .md file: first check same {lang}/, then common/, then other langs
- Compute relative path from source file's directory to target file
- Replace the link
"""

import os
import re
import sys
from pathlib import Path

DOCS_ROOT = Path(__file__).parent.parent / "docs"

# Search order for finding target files, by source directory
SEARCH_ORDERS = {
    "ru": ["ru", "common", "en"],
    "en": ["en", "common", "ru"],
    "common": ["common", "ru", "en"],
    "managed": ["managed", "ru", "common", "en"],
    "notebooklm": ["notebooklm", "ru", "common", "en"],
    "ai": ["ai", "ru", "common", "en"],
}

# Link pattern: [text](/docs/path) or [text](/docs/path "title") or [text](/docs/path#anchor)
LINK_PATTERN = re.compile(
    r'(\[(?:[^\[\]]*(?:\[[^\[\]]*\])?[^\[\]]*)\])'  # [text] part (handles nested brackets)
    r'\(/docs/([^)"\s#]+)'                             # (/docs/path
    r'(#[^)"\s]*)?'                                    # optional #anchor
    r'(\s+"[^"]*")?'                                   # optional "title"
    r'\)'                                              # closing )
)

# Also match bare URL references like (/docs/path)
BARE_LINK_PATTERN = re.compile(
    r'\((/docs/[^)"\s#]+)'
    r'(#[^)"\s]*)?'
    r'(\s+"[^"]*")?'
    r'\)'
)

def find_target_file(target_path: str, source_lang: str) -> Path | None:
    """Find the actual .md file for a /docs/X target path."""
    search_order = SEARCH_ORDERS.get(source_lang, ["ru", "common", "en"])

    for lang_dir in search_order:
        # Try exact .md file
        candidate = DOCS_ROOT / lang_dir / f"{target_path}.md"
        if candidate.exists():
            return candidate

        # Try as directory with index.md
        candidate = DOCS_ROOT / lang_dir / target_path / "index.md"
        if candidate.exists():
            return candidate

        # Try without trailing segment as directory
        # e.g., /docs/a/b might be docs/ru/a/b.md or docs/ru/a/b/index.md

    return None


def compute_relative_path(source_file: Path, target_file: Path) -> str:
    """Compute relative path from source file's directory to target file."""
    source_dir = source_file.parent
    try:
        rel = os.path.relpath(target_file, source_dir)
        # Convert Windows backslashes to forward slashes
        rel = rel.replace("\\", "/")
        return rel
    except ValueError:
        # Different drives on Windows
        return None


def get_source_lang(source_file: Path) -> str:
    """Determine which language directory a source file is in."""
    rel = source_file.relative_to(DOCS_ROOT)
    parts = rel.parts
    if parts:
        return parts[0]  # 'ru', 'en', 'common', etc.
    return "ru"


def fix_links_in_file(filepath: Path, dry_run: bool = False) -> tuple[int, list[str]]:
    """Fix /docs/ links in a single file. Returns (count_fixed, list_of_unfixed)."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return 0, []

    source_lang = get_source_lang(filepath)
    fixed_count = 0
    unfixed = []

    def replace_link(match):
        nonlocal fixed_count, unfixed
        full_match = match.group(0)

        # Extract parts
        text_part = match.group(1)  # [text]
        target_path = match.group(2)  # path after /docs/
        anchor = match.group(3) or ""  # #anchor or empty
        title = match.group(4) or ""  # "title" or empty

        # Find the actual target file
        target_file = find_target_file(target_path, source_lang)

        if target_file is None:
            # Target file not found — still convert to relative link
            # pointing to the most likely location (same lang dir)
            # This avoids absolute /docs/ 404s; MkDocs will warn about
            # broken relative links which is better than silent 404s
            best_guess = DOCS_ROOT / source_lang / f"{target_path}.md"
            best_guess_dir = DOCS_ROOT / source_lang / target_path / "index.md"

            # Use the guessed path even though it doesn't exist
            if source_lang in ("common", "ru", "en", "managed"):
                guess_target = best_guess
            else:
                guess_target = best_guess

            rel_path = compute_relative_path(filepath, guess_target)
            if rel_path:
                unfixed.append(f"  GUESS: /docs/{target_path} -> {rel_path}")
                fixed_count += 1
                return f"{text_part}({rel_path}{anchor}{title})"

            unfixed.append(f"  {filepath}: /docs/{target_path} -> NOT FOUND")
            return full_match  # Leave unchanged as last resort

        # Compute relative path
        rel_path = compute_relative_path(filepath, target_file)
        if rel_path is None:
            unfixed.append(f"  {filepath}: /docs/{target_path} -> PATH ERROR")
            return full_match

        fixed_count += 1
        return f"{text_part}({rel_path}{anchor}{title})"

    new_content = LINK_PATTERN.sub(replace_link, content)

    if fixed_count > 0 and not dry_run:
        filepath.write_text(new_content, encoding="utf-8")

    return fixed_count, unfixed


def main():
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    total_fixed = 0
    total_unfixed = 0
    all_unfixed = []
    files_processed = 0

    # Find all .md files with /docs/ links
    for md_file in DOCS_ROOT.rglob("*.md"):
        # Skip assets
        if "assets" in md_file.parts or "overrides" in md_file.parts:
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        if "/docs/" not in content:
            continue

        fixed, unfixed = fix_links_in_file(md_file, dry_run=dry_run)

        if fixed > 0 or unfixed:
            files_processed += 1
            total_fixed += fixed
            all_unfixed.extend(unfixed)
            total_unfixed += len(unfixed)

            if verbose and fixed > 0:
                print(f"  Fixed {fixed} links in {md_file.relative_to(DOCS_ROOT)}")

    print(f"\n{'=' * 60}")
    print(f"RESULTS:")
    print(f"  Files processed: {files_processed}")
    print(f"  Links fixed:     {total_fixed}")
    print(f"  Links unfixed:   {total_unfixed}")
    print(f"{'=' * 60}")

    if all_unfixed and verbose:
        print(f"\nUnfixed links (target not found):")
        for msg in all_unfixed[:50]:
            print(msg)
        if len(all_unfixed) > 50:
            print(f"  ... and {len(all_unfixed) - 50} more")

    return 0 if total_unfixed == 0 else 1


if __name__ == "__main__":
    main()
