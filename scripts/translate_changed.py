#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate only changed articles detected by detect_changes.py.

Reads changes_report.json and translates new/updated articles.
Uses the same translation engine as translate_docs_groq.py.

Usage:
    python scripts/translate_changed.py \
        --report changes_report.json \
        --max-articles 50
"""
import argparse
import json
import sys
import time
from pathlib import Path

# Import translation functions from existing script
sys.path.insert(0, str(Path(__file__).parent))
from translate_docs_groq import (
    translate_text, split_into_chunks, post_fix_known_errors,
    cache, CACHE_FILE, MAX_CHUNK_CHARS,
    GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY,
)

BASE_DIR = Path(__file__).parent.parent
EN_DIR = BASE_DIR / "docs" / "en"
RU_DIR = BASE_DIR / "docs" / "ru"


def translate_single_file(en_file: Path, ru_file: Path) -> bool:
    """Translate a single file. Returns True on success."""
    try:
        content = en_file.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  ERROR reading {en_file}: {e}")
        return False

    if len(content) > MAX_CHUNK_CHARS:
        chunks = split_into_chunks(content)
        parts = []
        for i, chunk in enumerate(chunks, 1):
            print(f"  chunk {i}/{len(chunks)}...")
            result = translate_text(chunk, f"{en_file.name}#chunk{i}")
            if result is None:
                print(f"  FAILED chunk {i}")
                return False
            parts.append(result)
        translated = "\n\n".join(parts)
    else:
        translated = translate_text(content, str(en_file.name))
        if translated is None:
            return False

    ru_file.parent.mkdir(parents=True, exist_ok=True)
    ru_file.write_text(translated, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(description="Translate changed articles")
    parser.add_argument("--report", required=True, help="Path to changes_report.json")
    parser.add_argument("--max-articles", type=int, default=50,
                        help="Max articles to translate (0 = unlimited)")
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        print(f"Report not found: {report_path}")
        sys.exit(1)

    report = json.load(open(report_path, "r", encoding="utf-8"))

    # Check API keys
    has_api = GEMINI_API_KEY or GROQ_API_KEY or OPENROUTER_API_KEY
    if not has_api:
        print("WARNING: No API keys set (GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY)")
        print("Translation skipped.")
        json.dump({"translated_count": 0, "skipped": "no_api_keys"},
                  open("translation_result.json", "w"))
        return

    # Collect articles to translate (new first, then updated)
    articles = report.get("new_articles", []) + report.get("updated_articles", [])
    if not articles:
        print("No articles to translate.")
        json.dump({"translated_count": 0}, open("translation_result.json", "w"))
        return

    max_articles = args.max_articles if args.max_articles > 0 else len(articles)
    articles = articles[:max_articles]

    print(f"Translating {len(articles)} articles...")
    print(f"API: Gemini={'ON' if GEMINI_API_KEY else 'OFF'}"
          f" | Groq={'ON' if GROQ_API_KEY else 'OFF'}"
          f" | OpenRouter={'ON' if OPENROUTER_API_KEY else 'OFF'}")
    print()

    translated_count = 0
    failed_count = 0
    translated_files = []
    start = time.time()

    for i, article in enumerate(articles, 1):
        rel_path = article["path"]
        en_file = EN_DIR / rel_path
        ru_file = RU_DIR / rel_path

        if not en_file.exists():
            print(f"[{i}/{len(articles)}] SKIP (not found): {rel_path}")
            continue

        print(f"[{i}/{len(articles)}] {rel_path}")

        ok = translate_single_file(en_file, ru_file)
        if ok:
            translated_count += 1
            translated_files.append(rel_path)
            print(f"  OK")
        else:
            failed_count += 1
            print(f"  FAILED")

        # Save cache periodically
        if i % 5 == 0:
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)

    # Final cache save
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    elapsed = time.time() - start
    print()
    print(f"Done: {translated_count} translated, {failed_count} failed, "
          f"{int(elapsed // 60)}m {int(elapsed % 60)}s")

    # Save result for downstream steps
    result = {
        "translated_count": translated_count,
        "failed_count": failed_count,
        "translated_files": translated_files,
        "elapsed_seconds": int(elapsed),
    }
    with open("translation_result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
