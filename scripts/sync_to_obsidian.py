#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync translated documentation and PDFs to Obsidian vault.

This LOCAL script:
1. Pulls latest changes from GitHub
2. Generates PDFs for new/updated translated docs (if not already done by CI)
3. Copies PDFs + Markdown to Obsidian raw/ folder
4. Creates index notes for Obsidian organization

Usage:
    python scripts/sync_to_obsidian.py
    python scripts/sync_to_obsidian.py --no-pull --no-pdf
    python scripts/sync_to_obsidian.py --vault "D:/MyVault"
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RU_DIR = BASE_DIR / "docs" / "ru"
PDF_DIR = BASE_DIR / "pdf-docs"
SYNC_STATE_FILE = BASE_DIR / "scripts" / ".change_tracking" / "obsidian_sync_state.json"

# Default Obsidian vault path
DEFAULT_VAULT = Path.home() / "Documents" / "ObsidianVault"
RAW_SUBDIR = "raw"
DYNATRACE_SUBDIR = "Dynatrace Docs"


def load_sync_state() -> dict:
    if SYNC_STATE_FILE.exists():
        return json.load(open(SYNC_STATE_FILE, "r", encoding="utf-8"))
    return {"last_sync": None, "synced_files": {}}


def save_sync_state(state: dict):
    SYNC_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SYNC_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def git_pull():
    """Pull latest changes from remote."""
    print("Pulling latest changes...")
    result = subprocess.run(
        ["git", "pull", "--ff-only"],
        cwd=str(BASE_DIR),
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  WARNING: git pull failed: {result.stderr.strip()}")
        return False
    print(f"  {result.stdout.strip()}")
    return True


def find_new_or_updated_files(state: dict) -> list[Path]:
    """Find ru/ files that are new or modified since last sync."""
    synced = state.get("synced_files", {})
    files = []

    for md_file in RU_DIR.rglob("*.md"):
        rel = str(md_file.relative_to(RU_DIR))
        mtime = md_file.stat().st_mtime
        prev_mtime = synced.get(rel)

        if prev_mtime is None or mtime > prev_mtime:
            files.append(md_file)

    return files


def generate_pdf_if_needed(md_file: Path) -> Path | None:
    """Generate PDF for a markdown file if it doesn't exist or is outdated."""
    rel = md_file.relative_to(RU_DIR)
    pdf_file = PDF_DIR / rel.with_suffix(".pdf")

    # Skip if PDF exists and is newer than source
    if pdf_file.exists():
        if pdf_file.stat().st_mtime >= md_file.stat().st_mtime:
            return pdf_file

    # Import PDF generator
    sys.path.insert(0, str(Path(__file__).parent))
    from generate_pdfs import md_to_pdf

    if md_to_pdf(md_file, pdf_file):
        return pdf_file
    return None


def copy_to_obsidian(files: list[Path], vault_path: Path, generate_pdf: bool) -> int:
    """Copy files to Obsidian vault. Returns count of copied files."""
    raw_dir = vault_path / RAW_SUBDIR / DYNATRACE_SUBDIR
    raw_dir.mkdir(parents=True, exist_ok=True)

    copied = 0

    for md_file in files:
        rel = md_file.relative_to(RU_DIR)

        # Copy Markdown
        md_dest = raw_dir / rel
        md_dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md_file, md_dest)

        # Generate and copy PDF
        if generate_pdf:
            pdf_file = generate_pdf_if_needed(md_file)
            if pdf_file and pdf_file.exists():
                pdf_dest = raw_dir / rel.with_suffix(".pdf")
                pdf_dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(pdf_file, pdf_dest)

        copied += 1

    return copied


def create_obsidian_index(vault_path: Path, files: list[Path]):
    """Create/update an index note in Obsidian for the synced docs."""
    index_dir = vault_path / RAW_SUBDIR / DYNATRACE_SUBDIR
    index_file = index_dir / "_index.md"

    # Build section index
    sections = {}
    for md_file in files:
        rel = md_file.relative_to(RU_DIR)
        parts = rel.parts
        section = parts[0] if len(parts) > 1 else "root"
        sections.setdefault(section, []).append(str(rel))

    lines = [
        "---",
        "title: Dynatrace Documentation Index",
        f"updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "tags: [dynatrace, documentation, auto-sync]",
        "---",
        "",
        "# Dynatrace Documentation (RU)",
        "",
        f"Last sync: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"Total files: {len(files)}",
        "",
    ]

    for section in sorted(sections.keys()):
        section_files = sorted(sections[section])
        lines.append(f"## {section.replace('-', ' ').title()} ({len(section_files)})")
        lines.append("")
        for f in section_files[:20]:
            name = Path(f).stem.replace("-", " ").title()
            lines.append(f"- [[{f}|{name}]]")
        if len(section_files) > 20:
            lines.append(f"- ... and {len(section_files) - 20} more")
        lines.append("")

    index_file.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Sync docs to Obsidian vault")
    parser.add_argument("--vault", type=str, default=str(DEFAULT_VAULT),
                        help=f"Obsidian vault path (default: {DEFAULT_VAULT})")
    parser.add_argument("--no-pull", action="store_true",
                        help="Skip git pull")
    parser.add_argument("--no-pdf", action="store_true",
                        help="Skip PDF generation")
    parser.add_argument("--force", action="store_true",
                        help="Force sync all files (ignore sync state)")
    args = parser.parse_args()

    vault_path = Path(args.vault)
    if not vault_path.exists():
        print(f"ERROR: Obsidian vault not found: {vault_path}")
        print(f"Use --vault to specify the correct path")
        sys.exit(1)

    print("=" * 60)
    print("DYNATRACE DOCS → OBSIDIAN SYNC")
    print("=" * 60)
    print(f"Vault: {vault_path}")
    print(f"Target: {vault_path / RAW_SUBDIR / DYNATRACE_SUBDIR}")
    print()

    # Step 1: Pull latest
    if not args.no_pull:
        git_pull()
        print()

    # Step 2: Find files to sync
    state = load_sync_state()
    if args.force:
        files = list(RU_DIR.rglob("*.md"))
        print(f"Force mode: syncing ALL {len(files)} files")
    else:
        files = find_new_or_updated_files(state)
        print(f"Found {len(files)} new/updated files since last sync")

    if not files:
        print("Nothing to sync. All files are up to date.")
        return

    # Step 3: Copy to Obsidian
    print()
    print("Copying to Obsidian vault...")
    copied = copy_to_obsidian(files, vault_path, generate_pdf=not args.no_pdf)
    print(f"  Copied {copied} files")

    # Step 4: Create index
    all_ru_files = list(RU_DIR.rglob("*.md"))
    create_obsidian_index(vault_path, all_ru_files)
    print("  Index updated")

    # Step 5: Update sync state
    for md_file in files:
        rel = str(md_file.relative_to(RU_DIR))
        state["synced_files"][rel] = md_file.stat().st_mtime
    state["last_sync"] = datetime.now().isoformat()
    save_sync_state(state)

    print()
    print("=" * 60)
    print(f"DONE: {copied} files synced to Obsidian")
    print(f"Location: {vault_path / RAW_SUBDIR / DYNATRACE_SUBDIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
