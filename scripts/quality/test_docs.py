#!/usr/bin/env python3
"""Validate documentation structure and content."""

import os
import sys
from pathlib import Path


def validate_docs():
    """Run basic documentation validation checks."""
    docs_dir = Path(__file__).resolve().parent.parent.parent / "docs"
    errors = []

    if not docs_dir.exists():
        print(f"ERROR: docs directory not found: {docs_dir}")
        sys.exit(1)

    # Check that docs/en exists and has markdown files
    en_dir = docs_dir / "en"
    if en_dir.exists():
        md_files = list(en_dir.rglob("*.md"))
        print(f"English docs: {len(md_files)} markdown files")
        if len(md_files) == 0:
            errors.append("No English markdown files found in docs/en/")
    else:
        print("WARNING: docs/en/ directory not found (may not have been scraped yet)")

    # Check that docs/ru exists
    ru_dir = docs_dir / "ru"
    if ru_dir.exists():
        md_files = list(ru_dir.rglob("*.md"))
        print(f"Russian docs: {len(md_files)} markdown files")
    else:
        print("WARNING: docs/ru/ directory not found")

    # Check for empty markdown files
    for lang_dir in [en_dir, ru_dir]:
        if not lang_dir.exists():
            continue
        for md_file in lang_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8", errors="replace").strip()
            if len(content) == 0:
                errors.append(f"Empty file: {md_file.relative_to(docs_dir)}")

    # Check mkdocs.yml exists
    mkdocs_yml = docs_dir.parent / "mkdocs.yml"
    if not mkdocs_yml.exists():
        errors.append("mkdocs.yml not found in project root")

    # Report results
    if errors:
        print(f"\n{len(errors)} validation error(s):")
        for err in errors[:20]:
            print(f"  - {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more")
        sys.exit(1)
    else:
        print("\nAll validation checks passed.")


if __name__ == "__main__":
    validate_docs()
