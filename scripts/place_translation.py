#!/usr/bin/env python3
"""
Place a translated article into the correct location and update navigation.

This script:
1. Validates the translated markdown file
2. Places it in docs/ru/ mirroring the docs/en/ structure
3. Updates mkdocs.yml navigation: switches en/ → ru/ for the translated file
4. Optionally removes the article from the pending translations list

Usage:
    # Place a single translated file
    python scripts/place_translation.py --file docs/ru/observe/dashboards.md

    # Place a translated file from an arbitrary path (copies to correct location)
    python scripts/place_translation.py --source my_translation.md --target observe/dashboards.md

    # Batch: place all translated files in a directory
    python scripts/place_translation.py --batch-dir translations/

    # Dry run (show what would happen)
    python scripts/place_translation.py --file docs/ru/observe/dashboards.md --dry-run
"""
import argparse
import re
import shutil
import sys
import yaml
from pathlib import Path
from typing import Optional

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
DOCS_EN = DOCS_DIR / "en"
DOCS_RU = DOCS_DIR / "ru"
MKDOCS_CONFIG = PROJECT_ROOT / "mkdocs.yml"


class _SafeLoaderIgnoreUnknown(yaml.SafeLoader):
    """YAML loader that ignores unknown Python tags."""
    pass

_SafeLoaderIgnoreUnknown.add_multi_constructor(
    "tag:yaml.org,2002:python/",
    lambda loader, suffix, node: None,
)


def validate_translation(file_path: Path) -> list:
    """
    Validate a translated markdown file.
    Returns list of issues (empty = valid).
    """
    issues = []

    if not file_path.exists():
        issues.append(f"File not found: {file_path}")
        return issues

    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        issues.append(f"File is not valid UTF-8: {file_path}")
        return issues

    # Must have some content beyond frontmatter
    body = re.sub(r"^---\n.*?\n---\n?", "", content, flags=re.DOTALL).strip()
    if len(body) < 50:
        issues.append(f"File too short (only {len(body)} chars after frontmatter)")

    # Check for CJK characters (likely broken translation)
    cjk = re.findall(r"[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff]", content)
    if cjk:
        issues.append(f"Contains {len(cjk)} CJK characters (possibly broken translation)")

    # Check for CSS artifacts from scraper
    css_artifacts = re.findall(r"\.css-[a-z0-9]+-[a-z]+", content)
    if css_artifacts:
        issues.append(f"Contains {len(css_artifacts)} CSS artifacts from scraping")

    return issues


def find_nav_entry(config_path: Path, en_path: str) -> Optional[str]:
    """
    Find the nav entry title for a given en/ path.
    Returns the title string if found.
    """
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=_SafeLoaderIgnoreUnknown)

    nav = config.get("nav", [])
    result = {"title": None}
    _search_nav(nav, en_path, result)
    return result["title"]


def _search_nav(items, target_path: str, result: dict):
    """Recursively search nav for a path."""
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                for title, value in item.items():
                    if isinstance(value, str) and value == target_path:
                        result["title"] = title
                        return
                    elif isinstance(value, list):
                        _search_nav(value, target_path, result)
                        if result["title"]:
                            return


def update_nav_entry(config_path: Path, en_path: str, ru_path: str,
                     dry_run: bool = False) -> bool:
    """
    Update mkdocs.yml: replace en_path with ru_path in navigation.
    Creates a backup before modifying.
    Returns True if changed.
    """
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if en/ entry exists in nav
    if en_path not in content:
        # Maybe it's already pointing to ru/
        if ru_path in content:
            print(f"  Nav already points to: {ru_path}")
            return False
        # Not in nav at all — need to add it
        return add_nav_entry(config_path, ru_path, dry_run)

    if dry_run:
        print(f"  [DRY RUN] Would replace nav: {en_path} → {ru_path}")
        return True

    # Backup
    backup = config_path.with_suffix(".yml.bak")
    with open(backup, "w", encoding="utf-8") as f:
        f.write(content)

    # Replace only in YAML value context
    for prefix in [": ", "- "]:
        content = content.replace(f"{prefix}{en_path}", f"{prefix}{ru_path}")

    with open(config_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  Nav updated: {en_path} → {ru_path}")
    return True


def add_nav_entry(config_path: Path, ru_path: str, dry_run: bool = False) -> bool:
    """
    Add a new nav entry for a translated file.
    Places it in the correct section based on directory structure.
    """
    # Determine section from path
    parts = ru_path.split("/")
    if len(parts) < 2:
        print(f"  Cannot determine section for: {ru_path}")
        return False

    # The corresponding en/ file should exist to get the title
    en_path = "en/" + "/".join(parts[1:])
    en_file = DOCS_DIR / en_path
    if en_file.exists():
        title = extract_title_from_file(en_file)
    else:
        title = parts[-1].replace(".md", "").replace("-", " ").title()

    if dry_run:
        print(f"  [DRY RUN] Would add nav entry: {title}: {ru_path}")
        return True

    # For now, just log — manual nav insertion is complex
    # The nav_updater can handle this on next deploy
    print(f"  New article not in nav. Add manually or run nav-upgrade:")
    print(f"    Title: {title}")
    print(f"    Path: {ru_path}")
    return False


def extract_title_from_file(md_file: Path) -> str:
    """Extract title from markdown file."""
    try:
        content = md_file.read_text(encoding="utf-8")
        if content.startswith("---"):
            end = content.find("---", 3)
            if end > 0:
                for line in content[3:end].split("\n"):
                    if line.strip().startswith("title:"):
                        return line.split(":", 1)[1].strip().strip("'\"")
        for line in content.split("\n"):
            if line.startswith("# "):
                return line[2:].strip()
    except Exception:
        pass
    return md_file.stem.replace("-", " ").title()


def place_single_file(file_path: Path, dry_run: bool = False) -> bool:
    """
    Place a translated file and update navigation.
    file_path should be docs/ru/<relative_path>.
    """
    # Resolve to absolute if relative
    if not file_path.is_absolute():
        file_path = (PROJECT_ROOT / file_path).resolve()

    # Determine relative path
    try:
        rel = file_path.relative_to(DOCS_RU)
    except ValueError:
        print(f"ERROR: File must be under {DOCS_RU} (got: {file_path})")
        return False

    rel_str = str(rel)
    en_nav_path = f"en/{rel_str}"
    ru_nav_path = f"ru/{rel_str}"

    print(f"\nPlacing translation: {ru_nav_path}")

    # Validate
    issues = validate_translation(file_path)
    if issues:
        print(f"  VALIDATION ISSUES:")
        for issue in issues:
            print(f"    ⚠ {issue}")
        if any("not found" in i or "not valid UTF-8" in i for i in issues):
            return False
        print("  Continuing with warnings...")

    # Check that en/ source exists
    en_file = DOCS_EN / rel
    if not en_file.exists():
        print(f"  WARNING: No English source at {en_nav_path}")
        print(f"  This may be a new article without English version.")

    # Update navigation
    nav_changed = update_nav_entry(MKDOCS_CONFIG, en_nav_path, ru_nav_path, dry_run)

    if not dry_run:
        print(f"  ✅ Translation placed: {ru_nav_path}")
    else:
        print(f"  [DRY RUN] Would place: {ru_nav_path}")

    return True


def place_from_source(source: Path, target_rel: str, dry_run: bool = False) -> bool:
    """
    Copy a translation file from an arbitrary location to docs/ru/<target_rel>
    and update navigation.
    """
    target = DOCS_RU / target_rel

    if not source.exists():
        print(f"ERROR: Source file not found: {source}")
        return False

    # Validate source
    issues = validate_translation(source)
    if issues:
        print("VALIDATION ISSUES:")
        for issue in issues:
            print(f"  ⚠ {issue}")

    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        print(f"Copied: {source} → {target}")
    else:
        print(f"[DRY RUN] Would copy: {source} → {target}")

    return place_single_file(target, dry_run)


def place_batch(batch_dir: Path, dry_run: bool = False) -> dict:
    """
    Place all .md files from a batch directory.
    Files should be organized in subdirectories matching docs/en/ structure.
    E.g., batch_dir/observe/dashboards.md → docs/ru/observe/dashboards.md
    """
    stats = {"placed": 0, "failed": 0, "skipped": 0}

    if not batch_dir.exists():
        print(f"ERROR: Batch directory not found: {batch_dir}")
        return stats

    md_files = sorted(batch_dir.rglob("*.md"))
    print(f"Found {len(md_files)} translation files in {batch_dir}")

    for md_file in md_files:
        rel = md_file.relative_to(batch_dir)
        target = DOCS_RU / rel

        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(md_file, target)

        success = place_single_file(target, dry_run)
        if success:
            stats["placed"] += 1
        else:
            stats["failed"] += 1

    print(f"\nBatch results: {stats['placed']} placed, {stats['failed']} failed")
    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Place translated articles and update navigation"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=Path,
                       help="Path to translated file already in docs/ru/")
    group.add_argument("--source", type=Path,
                       help="Source file to copy (use with --target)")
    group.add_argument("--batch-dir", type=Path,
                       help="Directory with batch translations")

    parser.add_argument("--target", type=str,
                        help="Target relative path under docs/ru/ (with --source)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would happen without making changes")
    args = parser.parse_args()

    if args.file:
        success = place_single_file(args.file, args.dry_run)
        return 0 if success else 1

    elif args.source:
        if not args.target:
            print("ERROR: --target is required with --source")
            return 1
        success = place_from_source(args.source, args.target, args.dry_run)
        return 0 if success else 1

    elif args.batch_dir:
        stats = place_batch(args.batch_dir, args.dry_run)
        return 0 if stats["failed"] == 0 else 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
