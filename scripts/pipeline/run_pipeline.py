#!/usr/bin/env python3
"""
Main CLI entry point for the Dynatrace Documentation Pipeline.

Usage:
    python scripts/pipeline/run_pipeline.py scrape [--max-pages N]
    python scripts/pipeline/run_pipeline.py translate [--target-lang ru] [--dir docs/en]
    python scripts/pipeline/run_pipeline.py validate [--strict] [--report path.json]
    python scripts/pipeline/run_pipeline.py nav-stats
    python scripts/pipeline/run_pipeline.py nav-upgrade [--apply]
    python scripts/pipeline/run_pipeline.py cache-stats
    python scripts/pipeline/run_pipeline.py cache-clean
"""
import sys
import argparse
import json
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from pipeline.config import (
    DOCS_DIR, DOCS_EN, DOCS_RU, CACHE_DIR,
    TERMINOLOGY_FILE, MKDOCS_CONFIG,
)
from pipeline.validator import DocumentValidator, NavValidator
from pipeline.cache_manager import CacheManager
from pipeline.nav_updater import NavUpdater


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

    for issue in warnings[:20]:  # Limit warnings output
        print(f"  WARN:  {issue}")

    if len(warnings) > 20:
        print(f"  ... and {len(warnings) - 20} more warnings")

    # Generate report
    if args.report:
        report = validator.generate_report(Path(args.report))
        # Add nav issues
        report["nav_issues"] = [i.to_dict() for i in nav_issues]
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nReport saved to: {args.report}")

    # Exit code
    if errors and args.strict:
        print("\nFAILED: Errors found in strict mode")
        return 1
    return 0


def cmd_translate(args):
    """Run translation pipeline."""
    from pipeline.translator import TranslationPipeline

    print("=" * 60)
    print(f"TRANSLATION PIPELINE ({args.target_lang})")
    print("=" * 60)

    source_dir = Path(args.dir) if args.dir else DOCS_EN
    target_dir = DOCS_DIR / args.target_lang

    pipeline = TranslationPipeline(
        cache_dir=CACHE_DIR,
        terminology_file=TERMINOLOGY_FILE,
    )

    if not pipeline.providers:
        print("ERROR: No translation providers available.")
        print("Set GEMINI_API_KEY, GROQ_API_KEY, or OPENROUTER_API_KEY in .env")
        return 1

    print(f"Source: {source_dir}")
    print(f"Target: {target_dir}")
    print(f"Providers: {[p.name for p in pipeline.providers]}")
    print()

    stats = pipeline.translate_directory(source_dir, target_dir, args.target_lang)

    print("\n" + "=" * 60)
    print("TRANSLATION RESULTS")
    print(f"  Total files:  {stats['total']}")
    print(f"  Translated:   {stats['translated']}")
    print(f"  Skipped:      {stats['skipped']}")
    print(f"  Failed:       {stats['failed']}")
    print("=" * 60)

    return 0 if stats["failed"] == 0 else 1


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


def cmd_cache_stats(args):
    """Show cache statistics."""
    cache = CacheManager(CACHE_DIR)
    stats = cache.get_stats()

    print("=" * 60)
    print("TRANSLATION CACHE STATISTICS")
    print("=" * 60)
    print(f"  Total cached:  {stats['total_cached']}")
    print(f"  Cache hits:    {stats['hits']}")
    print(f"  Cache misses:  {stats['misses']}")
    print(f"  Expired:       {stats['expired']}")

    return 0


def cmd_cache_clean(args):
    """Clean expired cache entries."""
    cache = CacheManager(CACHE_DIR)
    removed = cache.clear_expired()
    print(f"Removed {removed} expired cache entries.")
    return 0


def cmd_scrape(args):
    """Run documentation scraper (delegates to existing script)."""
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
        description="Dynatrace Documentation Pipeline CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Pipeline command")

    # scrape
    p_scrape = subparsers.add_parser("scrape", help="Scrape Dynatrace docs")
    p_scrape.add_argument("--max-pages", type=int, default=1000)

    # translate
    p_translate = subparsers.add_parser("translate", help="Translate documentation")
    p_translate.add_argument("--target-lang", default="ru")
    p_translate.add_argument("--dir", help="Source directory (default: docs/en)")
    p_translate.add_argument("--terminology", default=str(TERMINOLOGY_FILE))

    # validate
    p_validate = subparsers.add_parser("validate", help="Validate documentation")
    p_validate.add_argument("--strict", action="store_true")
    p_validate.add_argument("--report", help="Output report file path")

    # nav-stats
    subparsers.add_parser("nav-stats", help="Show navigation statistics")

    # nav-upgrade
    p_nav = subparsers.add_parser("nav-upgrade", help="Upgrade nav to Russian")
    p_nav.add_argument("--apply", action="store_true")

    # cache-stats
    subparsers.add_parser("cache-stats", help="Show cache statistics")

    # cache-clean
    subparsers.add_parser("cache-clean", help="Clean expired cache")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    commands = {
        "scrape": cmd_scrape,
        "translate": cmd_translate,
        "validate": cmd_validate,
        "nav-stats": cmd_nav_stats,
        "nav-upgrade": cmd_nav_upgrade,
        "cache-stats": cmd_cache_stats,
        "cache-clean": cmd_cache_clean,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
