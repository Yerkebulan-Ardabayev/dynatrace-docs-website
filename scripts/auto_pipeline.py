#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full auto-pipeline: detect → translate via Claude Code → PDF → Obsidian → Telegram.

This script is designed to run unattended via Windows Task Scheduler.
It calls Claude Code CLI to translate documents (no API keys needed).

Usage:
    python scripts/auto_pipeline.py
    python scripts/auto_pipeline.py --max-translate 10
    python scripts/auto_pipeline.py --skip-translate
"""
import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
SCRIPTS_DIR = Path(__file__).parent
REPORT_JSON = BASE_DIR / "changes_report.json"
TRANSLATION_RESULT = BASE_DIR / "translation_result.json"

# Load .env
for env_path in [BASE_DIR / ".env", SCRIPTS_DIR / ".env"]:
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, val = line.partition("=")
                    key = key.strip()
                    val = val.strip().strip("'\"")
                    if key and key not in os.environ:
                        os.environ[key] = val
        break


def log(msg: str):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def run_cmd(cmd: list, cwd: str = None, timeout: int = 300) -> tuple[int, str]:
    """Run command and return (exit_code, output)."""
    try:
        result = subprocess.run(
            cmd, cwd=cwd or str(BASE_DIR),
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=timeout,
        )
        return result.returncode, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return 1, "TIMEOUT"
    except Exception as e:
        return 1, str(e)


def stage_detect() -> dict:
    """Stage 1: Detect changes."""
    log("STAGE 1: Detecting changes...")

    code, output = run_cmd([
        sys.executable, str(SCRIPTS_DIR / "detect_changes.py"),
        "--source-dir", str(BASE_DIR / "docs" / "en"),
        "--target-dir", str(BASE_DIR / "docs" / "ru"),
        "--repo", "Yerkebulan-Ardabayev/dynatrace-docs-website",
        "--report", str(REPORT_JSON),
        "--markdown", str(BASE_DIR / "changes_report.md"),
    ])

    print(output[-500:] if len(output) > 500 else output)

    if REPORT_JSON.exists():
        report = json.load(open(REPORT_JSON, "r", encoding="utf-8"))
        log(f"  New: {report['new_count']}, Updated: {report['updated_count']}, "
            f"Total: {report['total_changes']}")
        return report

    log("  WARNING: No report generated")
    return {"new_count": 0, "updated_count": 0, "total_changes": 0}


def stage_translate_claude(report: dict, max_articles: int = 20) -> int:
    """Stage 2: Translate using Claude Code CLI."""
    articles = report.get("new_articles", []) + report.get("updated_articles", [])
    if not articles:
        log("  No articles to translate")
        return 0

    articles = articles[:max_articles]
    log(f"STAGE 2: Translating {len(articles)} articles via Claude Code...")

    translated_files = []
    failed = 0

    for i, article in enumerate(articles, 1):
        rel_path = article["path"]
        en_file = BASE_DIR / "docs" / "en" / rel_path
        ru_file = BASE_DIR / "docs" / "ru" / rel_path

        if not en_file.exists():
            log(f"  [{i}/{len(articles)}] SKIP (not found): {rel_path}")
            continue

        log(f"  [{i}/{len(articles)}] {rel_path}")

        # Build Claude prompt
        prompt = (
            f"Read the file docs/en/{rel_path} and translate it from English to Russian. "
            f"Save the translation to docs/ru/{rel_path}. "
            f"Rules: keep Dynatrace terms in English (OneAgent, ActiveGate, Smartscape, "
            f"PurePath, Davis AI, Dynatrace, Grail, DQL, etc). "
            f"Keep all Markdown formatting, code blocks, links, YAML frontmatter. "
            f"Keep file paths and URLs. Professional quality. "
            f"Just translate and save, no commentary."
        )

        # Call Claude Code in non-interactive mode
        code, output = run_cmd(
            ["claude", "-p", prompt, "--allowedTools", "Read,Write,Edit,Bash"],
            cwd=str(BASE_DIR),
            timeout=180,
        )

        if code == 0 and ru_file.exists():
            translated_files.append(rel_path)
            log(f"    OK")
        else:
            failed += 1
            log(f"    FAILED (exit={code})")
            if output:
                # Print last few lines for debugging
                lines = output.strip().split("\n")
                for line in lines[-3:]:
                    log(f"    > {line[:120]}")

    # Save result
    result = {
        "translated_count": len(translated_files),
        "failed_count": failed,
        "translated_files": translated_files,
    }
    with open(TRANSLATION_RESULT, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    log(f"  Translated: {len(translated_files)}, Failed: {failed}")
    return len(translated_files)


def stage_pdf(translated_count: int):
    """Stage 3: Generate PDFs."""
    if translated_count == 0:
        return

    log("STAGE 3: Generating PDFs...")
    code, output = run_cmd([
        sys.executable, str(SCRIPTS_DIR / "generate_pdfs.py"),
        "--report", str(TRANSLATION_RESULT),
        "--output-dir", str(BASE_DIR / "pdf-docs"),
    ], timeout=300)
    print(output[-300:] if len(output) > 300 else output)


def stage_obsidian():
    """Stage 4: Sync to Obsidian."""
    log("STAGE 4: Syncing to Obsidian...")
    code, output = run_cmd([
        sys.executable, str(SCRIPTS_DIR / "sync_to_obsidian.py"),
        "--no-pull",
    ], timeout=120)
    print(output[-300:] if len(output) > 300 else output)


def stage_git_push(translated_count: int):
    """Stage 5: Commit and push changes."""
    if translated_count == 0:
        return

    log("STAGE 5: Committing and pushing...")

    run_cmd(["git", "config", "user.name", "Yerkebulan Ardabayev"])
    run_cmd(["git", "config", "user.email", "yerkebulan.ardabayev@gmail.com"])
    run_cmd(["git", "add", "docs/ru/", "pdf-docs/", "scripts/.change_tracking/"])

    # Check if there are staged changes
    code, _ = run_cmd(["git", "diff", "--staged", "--quiet"])
    if code != 0:  # There are changes
        date = datetime.now().strftime("%Y-%m-%d")
        msg = f"docs(ru): auto-translate {translated_count} articles {date}"
        run_cmd(["git", "commit", "-m", msg])
        code, output = run_cmd(["git", "push"], timeout=60)
        log(f"  Push: {'OK' if code == 0 else 'FAILED'}")
    else:
        log("  No changes to commit")


def stage_telegram(report: dict, translated_count: int):
    """Stage 6: Send Telegram notification."""
    log("STAGE 6: Sending Telegram notification...")
    import requests

    token = os.environ.get("TG_BOT_TOKEN", "")
    chat_id = os.environ.get("TG_CHAT_ID", "")

    if not token or not chat_id:
        log("  WARNING: TG_BOT_TOKEN or TG_CHAT_ID not set")
        return

    total = report.get("total_changes", 0)
    new = report.get("new_count", 0)
    updated = report.get("updated_count", 0)
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    site = "https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/"

    if total > 0:
        msg = f"📝 *Dynatrace Docs — Обновления*\n"
        msg += f"\n📊 Обнаружено *{total}* изменений:\n"
        msg += f"  • Новых: *{new}*\n"
        msg += f"  • Обновлённых: *{updated}*\n"
        if translated_count > 0:
            msg += f"\n✅ Переведено: *{translated_count}* (Claude Code)\n"
        msg += f"\n🕐 {date}\n🌐 [Сайт]({site})"
    else:
        msg = f"✅ *Dynatrace Docs*\n\n"
        msg += f"Проверка {date} — изменений нет.\n🌐 [Сайт]({site})"

    try:
        resp = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={
                "chat_id": chat_id,
                "text": msg,
                "parse_mode": "Markdown",
                "disable_web_page_preview": "true",
            },
            timeout=15,
        )
        log(f"  Telegram: {'OK' if resp.json().get('ok') else 'FAILED'}")
    except Exception as e:
        log(f"  Telegram ERROR: {e}")


def main():
    parser = argparse.ArgumentParser(description="Full auto-pipeline")
    parser.add_argument("--max-translate", type=int, default=20)
    parser.add_argument("--skip-translate", action="store_true")
    parser.add_argument("--skip-obsidian", action="store_true")
    parser.add_argument("--skip-push", action="store_true")
    args = parser.parse_args()

    start = time.time()
    log("=" * 60)
    log("DYNATRACE DOCS AUTO-PIPELINE")
    log(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    log("=" * 60)

    # 1. Detect
    report = stage_detect()
    total = report.get("total_changes", 0)

    # 2. Translate
    translated = 0
    if total > 0 and not args.skip_translate:
        translated = stage_translate_claude(report, args.max_translate)

    # 3. PDF
    if translated > 0:
        stage_pdf(translated)

    # 4. Obsidian
    if translated > 0 and not args.skip_obsidian:
        stage_obsidian()

    # 5. Git push
    if not args.skip_push:
        stage_git_push(translated)

    # 6. Telegram
    stage_telegram(report, translated)

    elapsed = time.time() - start
    log("")
    log(f"DONE in {int(elapsed//60)}m {int(elapsed%60)}s")
    log(f"Changes: {total}, Translated: {translated}")


if __name__ == "__main__":
    main()
