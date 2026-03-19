#!/usr/bin/env python3
"""
Main CLI entry point for the Dynatrace Documentation Pipeline.

Architecture (v2 — no auto-translation):
- scrape: download English docs from docs.dynatrace.com
- detect: find new/updated articles needing translation
- place: place a translated file and update navigation
- validate: run quality checks on all docs
- nav-stats: show navigation language statistics
- nav-upgrade: switch en/ → ru/ in nav where translations exist

Usage:
    python scripts/pipeline/run_pipeline.py scrape [--max-pages N]
    python scripts/pipeline/run_pipeline.py detect [--report path.json] [--markdown path.md]
    python scripts/pipeline/run_pipeline.py place --file docs/ru/path.md
    python scripts/pipeline/run_pipeline.py validate [--strict] [--report path.json]
    python scripts/pipeline/run_pipeline.py nav-stats
    python scripts/pipeline/run_pipeline.py nav-upgrade [--apply]
"""
import sys
import argparse
import json
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from pipeline.config import (
    DOCS_DIR, DOCS_EN, DOCS_RU, MKDOCS_CONFIG,
)
from pipeline.validator import DocumentValidator, NavValidator
from pipeline.nav_updater import NavUpdater
from pipeline.structured_logger import get_logger


def cmd_validate(args):
    """Run validation checks."""
    print("=" * 60)
    print("DOCUMENTATION VALIDATION")
    print("=" * 60)

    # Document validation
    validator = DocumentValidator(DOCS_DIR)
    issues = validator.validate_all(strict=args.strict)

    # Nav validation
    nav_validator = NavValidator(MKDOCS_CONFIG, DOCS_DIR)
    nav_issues = nav_validator.validate()
    issues.extend(nav_issues)

    # Print results
    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]

    print(f"\nResults: {len(errors)} errors, {len(warnings)} warnings")
    print("-" * 60)

    for issue in errors:
        print(f"  ERROR: {issue}")

    for issue in warnings[:20]:
        print(f"  WARN:  {issue}")

    if len(warnings) > 20:
        print(f"  ... and {len(warnings) - 20} more warnings")

    # Generate report
    if args.report:
        report = validator.generate_report(Path(args.report))
        report["nav_issues"] = [i.to_dict() for i in nav_issues]
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nReport saved to: {args.report}")

    if errors:
        if args.strict:
            print(f"\nFAILED: {len(errors)} errors found in strict mode.")
            return 1
        else:
            print(f"\nWARNING: {len(errors)} errors found but strict mode is off.")
            return 0
    return 0


def cmd_detect(args):
    """Detect new/updated articles needing translation."""
    # Import from scripts directory
    sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
    from detect_changes import detect_changes, generate_markdown_report

    source_dir = Path(args.source_dir) if args.source_dir else DOCS_EN
    target_dir = Path(args.target_dir) if args.target_dir else DOCS_RU

    result = detect_changes(source_dir, target_dir)

    print("=" * 60)
    print("CHANGE DETECTION REPORT")
    print("=" * 60)
    print(f"  Source files (en):     {result['total_source_files']}")
    print(f"  New articles:          {result['new_count']}")
    print(f"  Updated articles:      {result['updated_count']}")
    print(f"  Total needing work:    {result['total_changes']}")
    print("=" * 60)

    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nJSON report saved to: {args.report}")

    if args.markdown:
        md_report = generate_markdown_report(result)
        with open(args.markdown, "w", encoding="utf-8") as f:
            f.write(md_report)
        print(f"Markdown report saved to: {args.markdown}")

    return 0


def cmd_place(args):
    """Place a translated file and update navigation."""
    sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
    from place_translation import place_single_file, place_from_source, place_batch

    if args.batch_dir:
        stats = place_batch(Path(args.batch_dir), args.dry_run)
        return 0 if stats["failed"] == 0 else 1
    elif args.source and args.target:
        success = place_from_source(Path(args.source), args.target, args.dry_run)
        return 0 if success else 1
    elif args.file:
        success = place_single_file(Path(args.file), args.dry_run)
        return 0 if success else 1
    else:
        print("ERROR: Specify --file, --source+--target, or --batch-dir")
        return 1


def cmd_nav_stats(args):
    """Show navigation statistics."""
    updater = NavUpdater(MKDOCS_CONFIG, DOCS_DIR)
    stats = updater.list_nav_stats()

    print("=" * 60)
    print("NAVIGATION STATISTICS")
    print("=" * 60)
    print(f"  Total entries: {stats['total']}")
    print(f"  Russian (ru/): {stats['ru']}")
    print(f"  English (en/): {stats['en']}")
    print(f"  Managed:       {stats['managed']}")
    print(f"  Other:         {stats['other']}")

    if stats['total'] > 0:
        ru_pct = stats['ru'] / stats['total'] * 100
        print(f"\n  Russian coverage: {ru_pct:.1f}%")

    return 0


def cmd_nav_upgrade(args):
    """Upgrade nav entries from en/ to ru/ where translations exist."""
    updater = NavUpdater(MKDOCS_CONFIG, DOCS_DIR)
    upgradeable = updater.upgrade_to_russian(dry_run=not args.apply)

    if not upgradeable:
        print("No nav entries to upgrade (no new ru/ translations found).")
        return 0

    print(f"Found {len(upgradeable)} entries that can be upgraded to Russian:")
    for entry in upgradeable:
        print(f"  {entry['title']}: {entry['en_path']} -> {entry['ru_path']}")

    if args.apply:
        print(f"\nApplied {len(upgradeable)} upgrades to {MKDOCS_CONFIG}")
    else:
        print("\nDry run — use --apply to make changes.")

    return 0


def cmd_scrape(args):
    """Run documentation scraper."""
    import subprocess

    print("=" * 60)
    print("SCRAPING DYNATRACE DOCUMENTATION")
    print("=" * 60)

    scraper_path = PROJECT_ROOT / "scripts" / "scrape_docs.py"
    if not scraper_path.exists():
        print(f"ERROR: Scraper not found at {scraper_path}")
        return 1

    cmd = [sys.executable, str(scraper_path)]
    if args.max_pages:
        cmd.extend(["--max-pages", str(args.max_pages)])

    result = subprocess.run(cmd, cwd=str(PROJECT_ROOT))
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Dynatrace Documentation Pipeline CLI (v2)"
    )
    subparsers = parser.add_subparsers(dest="command", help="Pipeline command")

    # scrape
    p_scrape = subparsers.add_parser("scrape", help="Scrape Dynatrace docs")
    p_scrape.add_argument("--max-pages", type=int, default=1000)

    # detect
    p_detect = subparsers.add_parser("detect", help="Detect new/updated articles")
    p_detect.add_argument("--source-dir", help="Source dir (default: docs/en)")
    p_detect.add_argument("--target-dir", help="Target dir (default: docs/ru)")
    p_detect.add_argument("--report", help="Output JSON report path")
    p_detect.add_argument("--markdown", help="Output Markdown report path")

    # place
    p_place = subparsers.add_parser("place", help="Place translated file")
    p_place.add_argument("--file", help="Path to file already in docs/ru/")
    p_place.add_argument("--source", help="Source file to copy")
    p_place.add_argument("--target", help="Target relative path under docs/ru/")
    p_place.add_argument("--batch-dir", help="Directory with batch translations")
    p_place.add_argument("--dry-run", action="store_true")

    # validate
    p_validate = subparsers.add_parser("validate", help="Validate documentation")
    p_validate.add_argument("--strict", action="store_true")
    p_validate.add_argument("--report", help="Output report file path")

    # nav-stats
    subparsers.add_parser("nav-stats", help="Show navigation statistics")

    # nav-upgrade
    p_nav = subparsers.add_parser("nav-upgrade", help="Upgrade nav to Russian")
    p_nav.add_argument("--apply", action="store_true")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    commands = {
        "scrape": cmd_scrape,
        "detect": cmd_detect,
        "place": cmd_place,
        "validate": cmd_validate,
        "nav-stats": cmd_nav_stats,
        "nav-upgrade": cmd_nav_upgrade,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
