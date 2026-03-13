#!/usr/bin/env python3
"""
Unified documentation pipeline orchestrator.

Runs the full pipeline: scrape -> diff -> translate -> nav-update -> validate -> deploy.
Designed for both local use and CI/CD.

Usage:
    python scripts/sync_and_deploy.py                  # full pipeline
    python scripts/sync_and_deploy.py --skip-scrape    # translate & deploy only
    python scripts/sync_and_deploy.py --dry-run        # no git commit/push
    python scripts/sync_and_deploy.py --force           # re-translate everything
"""
import sys
import subprocess
import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from pipeline.config import (
    DOCS_DIR, DOCS_EN, DOCS_RU, CACHE_DIR,
    TERMINOLOGY_FILE, MKDOCS_CONFIG,
)


class PipelineOrchestrator:
    """Coordinates all pipeline stages with diff-based incremental updates."""

    def __init__(self, args):
        self.args = args
        self.stats = {
            "started": datetime.now().isoformat(),
            "scrape": {"status": "skipped"},
            "diff": {"changed": 0, "files": []},
            "translate": {"status": "skipped"},
            "nav": {"upgraded": 0},
            "validate": {"errors": 0, "warnings": 0},
            "deploy": {"status": "skipped"},
        }

    def run(self):
        """Execute the full pipeline."""
        print("=" * 70)
        print("  DYNATRACE DOCUMENTATION PIPELINE")
        print(f"  Started: {self.stats['started']}")
        print("=" * 70)

        # Stage 1: Scrape
        if not self.args.skip_scrape:
            self._stage_scrape()
        else:
            print("\n[1/5] Scrape: SKIPPED (--skip-scrape)")

        # Stage 2: Diff — find changed files
        changed_files = self._stage_diff()

        if not changed_files and not self.args.force:
            print("\nNo changes detected. Pipeline complete.")
            self._print_summary()
            return 0

        # Stage 3: Translate only changed files
        self._stage_translate(changed_files)

        # Stage 4: Update navigation
        self._stage_nav_update()

        # Stage 5: Validate
        exit_code = self._stage_validate()

        # Stage 6: Deploy (commit + push)
        if not self.args.dry_run:
            self._stage_deploy()
        else:
            print("\n[Deploy] SKIPPED (--dry-run)")

        self._print_summary()
        return exit_code

    def _stage_scrape(self):
        """Stage 1: Scrape documentation source."""
        print("\n[1/5] Scraping Dynatrace documentation...")
        scraper = PROJECT_ROOT / "scripts" / "scrape_docs.py"

        cmd = [sys.executable, str(scraper)]
        if self.args.max_pages:
            cmd.extend(["--max-pages", str(self.args.max_pages)])

        result = subprocess.run(cmd, cwd=str(PROJECT_ROOT))
        self.stats["scrape"]["status"] = "success" if result.returncode == 0 else "failed"

        # Run organize if it exists
        organize = PROJECT_ROOT / "scripts" / "organize_docs.py"
        if organize.exists():
            subprocess.run([sys.executable, str(organize)], cwd=str(PROJECT_ROOT))

    def _stage_diff(self) -> list:
        """Stage 2: Find files that need translation (content-hash diff)."""
        print("\n[2/5] Detecting changes...")

        changed = []
        en_files = list(DOCS_EN.rglob("*.md"))

        for en_file in en_files:
            relative = en_file.relative_to(DOCS_EN)
            ru_file = DOCS_RU / relative

            # New file — no Russian version yet
            if not ru_file.exists():
                changed.append(en_file)
                continue

            # Existing file — compare content hashes
            en_hash = self._file_hash(en_file)
            # Check if the source changed since last translation
            cache_marker = CACHE_DIR / "hashes" / f"{relative}.hash"
            if cache_marker.exists():
                stored_hash = cache_marker.read_text().strip()
                if stored_hash == en_hash:
                    continue  # No change
            changed.append(en_file)

        if self.args.force:
            changed = en_files
            print(f"  Force mode: re-translating all {len(changed)} files")
        else:
            print(f"  Changed/new files: {len(changed)} out of {len(en_files)}")

        self.stats["diff"]["changed"] = len(changed)
        self.stats["diff"]["files"] = [str(f.relative_to(PROJECT_ROOT)) for f in changed[:20]]
        return changed

    def _stage_translate(self, changed_files: list):
        """Stage 3: Translate only changed files. Stops gracefully on quota exhaustion."""
        if not changed_files:
            print("\n[3/5] Translate: nothing to translate")
            return

        print(f"\n[3/5] Translating {len(changed_files)} files...")

        from pipeline.translator import TranslationPipeline, QuotaExhaustedError
        pipeline = TranslationPipeline(CACHE_DIR, TERMINOLOGY_FILE)

        if not pipeline.providers:
            print("  WARNING: No translation providers configured. Set API keys.")
            self.stats["translate"]["status"] = "no_providers"
            return

        translated = 0
        failed = 0
        quota_stopped = False
        remaining = 0

        for i, source_file in enumerate(changed_files):
            relative = source_file.relative_to(DOCS_EN)
            target_file = DOCS_RU / relative

            print(f"  -> {relative}")
            try:
                if pipeline.translate_file(source_file, target_file, "ru"):
                    translated += 1
                    self._store_hash(source_file, relative)
                else:
                    failed += 1
            except QuotaExhaustedError:
                quota_stopped = True
                remaining = len(changed_files) - i - 1
                print(f"\n  [QUOTA] All providers exhausted after {translated} translations.")
                print(f"  [QUOTA] {remaining} files postponed to next pipeline run.")
                break

        status = "quota_partial" if quota_stopped else "success"
        self.stats["translate"] = {
            "status": status,
            "translated": translated,
            "failed": failed,
            "total": len(changed_files),
            "remaining": remaining,
        }
        print(f"  Done: {translated} translated, {failed} failed" +
              (f", {remaining} postponed (quota)" if quota_stopped else ""))

    def _stage_nav_update(self):
        """Stage 4: Update mkdocs.yml navigation en/ -> ru/."""
        print("\n[4/5] Updating navigation...")

        from pipeline.nav_updater import NavUpdater
        updater = NavUpdater(MKDOCS_CONFIG, DOCS_DIR)
        upgradeable = updater.upgrade_to_russian(dry_run=False)
        self.stats["nav"]["upgraded"] = len(upgradeable)

        if upgradeable:
            print(f"  Upgraded {len(upgradeable)} nav entries to Russian")
            for entry in upgradeable[:5]:
                print(f"    {entry['title']}: en/ -> ru/")
            if len(upgradeable) > 5:
                print(f"    ... and {len(upgradeable) - 5} more")
        else:
            print("  No nav entries to upgrade")

    def _stage_validate(self) -> int:
        """Stage 5: Validate documentation quality."""
        print("\n[5/5] Validating...")

        from pipeline.validator import DocumentValidator, NavValidator
        dv = DocumentValidator(DOCS_DIR)
        issues = dv.validate_all()

        nv = NavValidator(MKDOCS_CONFIG, DOCS_DIR)
        nav_issues = nv.validate()
        issues.extend(nav_issues)

        errors = [i for i in issues if i.severity == "error"]
        warnings = [i for i in issues if i.severity == "warning"]

        self.stats["validate"]["errors"] = len(errors)
        self.stats["validate"]["warnings"] = len(warnings)

        print(f"  Errors: {len(errors)}, Warnings: {len(warnings)}")
        for e in errors[:5]:
            print(f"    ERROR: {e}")

        return 1 if len(errors) > 10 else 0  # Allow minor errors

    def _stage_deploy(self):
        """Stage 6: Git commit and push."""
        print("\n[Deploy] Committing and pushing...")

        cmds = [
            ["git", "add", "docs/", "scripts/.translation_cache/", "mkdocs.yml"],
        ]

        for cmd in cmds:
            subprocess.run(cmd, cwd=str(PROJECT_ROOT))

        # Check if there are staged changes
        result = subprocess.run(
            ["git", "diff", "--staged", "--quiet"],
            cwd=str(PROJECT_ROOT),
        )

        if result.returncode == 0:
            print("  No changes to commit")
            self.stats["deploy"]["status"] = "no_changes"
            return

        date_str = datetime.now().strftime("%Y-%m-%d")
        msg = f"docs: auto-update {date_str}\n\nTranslated: {self.stats['translate'].get('translated', 0)}, Nav upgraded: {self.stats['nav']['upgraded']}"

        subprocess.run(
            ["git", "commit", "-m", msg],
            cwd=str(PROJECT_ROOT),
        )

        push_result = subprocess.run(
            ["git", "push"],
            cwd=str(PROJECT_ROOT),
        )
        self.stats["deploy"]["status"] = "success" if push_result.returncode == 0 else "push_failed"

    def _print_summary(self):
        """Print pipeline summary."""
        print("\n" + "=" * 70)
        print("  PIPELINE SUMMARY")
        print("=" * 70)
        print(f"  Scrape:     {self.stats['scrape']['status']}")
        print(f"  Changed:    {self.stats['diff']['changed']} files")
        print(f"  Translate:  {self.stats['translate']}")
        print(f"  Nav update: {self.stats['nav']['upgraded']} entries upgraded")
        print(f"  Validate:   {self.stats['validate']['errors']} errors, {self.stats['validate']['warnings']} warnings")
        print(f"  Deploy:     {self.stats['deploy']['status']}")
        print("=" * 70)

        # Save stats
        stats_file = PROJECT_ROOT / "scripts" / ".pipeline_stats.json"
        self.stats["finished"] = datetime.now().isoformat()
        with open(stats_file, "w", encoding="utf-8") as f:
            json.dump(self.stats, f, indent=2, ensure_ascii=False)

    @staticmethod
    def _file_hash(path: Path) -> str:
        """SHA256 of file content (first 16 hex chars)."""
        return hashlib.sha256(path.read_bytes()).hexdigest()[:16]

    def _store_hash(self, source_file: Path, relative: Path):
        """Store content hash to track changes."""
        hash_dir = CACHE_DIR / "hashes"
        hash_dir.mkdir(parents=True, exist_ok=True)
        marker = hash_dir / f"{relative}.hash"
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text(self._file_hash(source_file))


def main():
    parser = argparse.ArgumentParser(description="Dynatrace docs pipeline orchestrator")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping stage")
    parser.add_argument("--dry-run", action="store_true", help="No git commit/push")
    parser.add_argument("--force", action="store_true", help="Re-translate all files")
    parser.add_argument("--max-pages", type=int, default=1000, help="Max pages to scrape")
    args = parser.parse_args()

    orchestrator = PipelineOrchestrator(args)
    return orchestrator.run()


if __name__ == "__main__":
    sys.exit(main())
