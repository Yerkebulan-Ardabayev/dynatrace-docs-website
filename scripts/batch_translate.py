#!/usr/bin/env python3
"""
Batch translation script with progress tracking.
Translates EN docs to RU using the pipeline with rate-limit awareness.

Usage:
    python scripts/batch_translate.py [--batch-size N] [--priority SECTION]
"""
import sys
import time
import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from pipeline.translator import TranslationPipeline
from pipeline.config import DOCS_DIR, DOCS_EN, DOCS_RU, CACHE_DIR, TERMINOLOGY_FILE


# Priority order for translation (most important first)
PRIORITY_SECTIONS = [
    "getting-started.md",
    "dynatrace-api.md",
    "index.md",
    "ingest-from.md",
    "dynatrace-intelligence.md",
    "license.md",
    "semantic-dictionary.md",
    "whats-new.md",
    # Then directories by importance
    "platform",
    "observe",
    "manage",
    "managed",
    "dynatrace-intelligence",
    "analyze-explore-automate",
    "deliver",
    "discover-dynatrace",
    "dynatrace-api",
    "ingest-from",
    "secure",
    "whats-new",
    "license",
    "semantic-dictionary",
]


def get_files_to_translate():
    """Get list of files needing translation, sorted by priority."""
    en_files = list(DOCS_EN.rglob("*.md"))

    need_translation = []
    for f in en_files:
        rel = f.relative_to(DOCS_EN)
        ru_target = DOCS_RU / rel
        if not ru_target.exists():
            need_translation.append(f)

    # Sort by priority
    def priority_key(path):
        rel = str(path.relative_to(DOCS_EN))
        for i, section in enumerate(PRIORITY_SECTIONS):
            if rel == section or rel.startswith(section + "/"):
                return (i, rel)
        return (len(PRIORITY_SECTIONS), rel)

    need_translation.sort(key=priority_key)
    return need_translation


def translate_batch(files, pipeline, batch_size=50):
    """Translate a batch of files with progress tracking."""
    total = len(files)
    translated = 0
    failed = 0
    skipped = 0

    start_time = time.time()

    for i, source_file in enumerate(files[:batch_size]):
        rel = source_file.relative_to(DOCS_EN)
        target_file = DOCS_RU / rel

        # Size check - skip very large files for now (> 50KB)
        file_size = source_file.stat().st_size
        if file_size > 50000:
            print(f"  [{i+1}/{min(batch_size, total)}] SKIP (too large {file_size//1024}KB): {rel}")
            skipped += 1
            continue

        print(f"  [{i+1}/{min(batch_size, total)}] Translating: {rel} ({file_size//1024}KB)")

        try:
            result = pipeline.translate_file(source_file, target_file, "ru")
            if result:
                translated += 1
            else:
                failed += 1
                print(f"    FAILED: {rel}")
        except Exception as e:
            failed += 1
            print(f"    ERROR: {rel}: {e}")

        # Progress update every 10 files
        if (i + 1) % 10 == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed * 60 if elapsed > 0 else 0
            print(f"\n  --- Progress: {i+1}/{min(batch_size, total)} | "
                  f"OK: {translated} | Failed: {failed} | "
                  f"Rate: {rate:.1f} files/min ---\n")

    elapsed = time.time() - start_time
    return {
        "translated": translated,
        "failed": failed,
        "skipped": skipped,
        "elapsed_seconds": elapsed,
    }


def main():
    parser = argparse.ArgumentParser(description="Batch translate documentation")
    parser.add_argument("--batch-size", type=int, default=100,
                       help="Number of files to translate in this batch")
    parser.add_argument("--priority", type=str, default=None,
                       help="Only translate files in this section")
    parser.add_argument("--skip-large", type=int, default=50000,
                       help="Skip files larger than N bytes (default: 50000)")
    args = parser.parse_args()

    print("=" * 60)
    print("BATCH TRANSLATION")
    print("=" * 60)

    # Init pipeline
    pipeline = TranslationPipeline(CACHE_DIR, TERMINOLOGY_FILE)
    if not pipeline.providers:
        print("ERROR: No translation providers available!")
        return 1

    print(f"Providers: {[p.name for p in pipeline.providers]}")

    # Get files
    files = get_files_to_translate()

    if args.priority:
        files = [f for f in files
                 if str(f.relative_to(DOCS_EN)).startswith(args.priority)]

    print(f"Files needing translation: {len(files)}")
    print(f"Batch size: {args.batch_size}")
    print()

    if not files:
        print("Nothing to translate!")
        return 0

    # Show what we'll translate
    print("First files in queue:")
    for f in files[:10]:
        rel = f.relative_to(DOCS_EN)
        size = f.stat().st_size
        print(f"  {rel} ({size//1024}KB)")
    if len(files) > 10:
        print(f"  ... and {len(files) - 10} more")
    print()

    # Translate
    stats = translate_batch(files, pipeline, args.batch_size)

    # Summary
    print()
    print("=" * 60)
    print("BATCH RESULTS")
    print(f"  Translated: {stats['translated']}")
    print(f"  Failed:     {stats['failed']}")
    print(f"  Skipped:    {stats['skipped']}")
    print(f"  Time:       {stats['elapsed_seconds']:.0f}s ({stats['elapsed_seconds']/60:.1f}min)")
    print("=" * 60)

    # Remaining
    remaining = get_files_to_translate()
    print(f"\nRemaining files to translate: {len(remaining)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
