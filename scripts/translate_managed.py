#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate Managed docs: docs/managed/<path>.md -> docs/managed-ru/<path>.md via Claude Code CLI.

Reads changes_report.json (produced by detect_changes.py) and translates new + updated articles.
No external API keys — uses local 'claude -p' CLI.
"""

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EN_DIR = BASE_DIR / "docs" / "managed"
RU_DIR = BASE_DIR / "docs" / "managed-ru"
RESULT_JSON = BASE_DIR / "translation_result_managed.json"


def log(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def run_claude(prompt: str, timeout: int = 240) -> tuple[int, str]:
    try:
        result = subprocess.run(
            [
                "claude",
                "-p",
                prompt,
                "--model",
                "claude-sonnet-4-6",
                "--allowedTools",
                "Read,Write,Edit,Bash",
            ],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        return result.returncode, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return 1, "TIMEOUT"
    except Exception as e:
        return 1, str(e)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Translate Managed docs via Claude CLI"
    )
    parser.add_argument("--report", required=True, help="changes_report.json path")
    parser.add_argument("--max-articles", type=int, default=250)
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="If RU file already exists, skip (don't re-translate)",
    )
    args = parser.parse_args()

    report = json.load(open(args.report, "r", encoding="utf-8"))
    articles = report.get("new_articles", []) + report.get("updated_articles", [])
    if not articles:
        log("No articles to translate (report shows 0 new + 0 updated)")
        json.dump(
            {"translated_count": 0, "failed_count": 0, "translated_files": []},
            open(RESULT_JSON, "w", encoding="utf-8"),
            indent=2,
            ensure_ascii=False,
        )
        return

    articles = articles[: args.max_articles]
    log(f"Translating {len(articles)} Managed articles via Claude CLI")
    log(f"  EN_DIR: {EN_DIR}")
    log(f"  RU_DIR: {RU_DIR}")
    log("")

    translated: list[str] = []
    failed = 0
    skipped = 0
    start = time.time()

    for i, article in enumerate(articles, 1):
        rel = article["path"]
        en = EN_DIR / rel
        ru = RU_DIR / rel

        if not en.exists():
            log(f"  [{i}/{len(articles)}] SKIP — EN file missing: {rel}")
            skipped += 1
            continue

        if args.skip_existing and ru.exists():
            log(f"  [{i}/{len(articles)}] SKIP — RU exists (--skip-existing): {rel}")
            skipped += 1
            continue

        log(f"  [{i}/{len(articles)}] {rel}")

        prompt = (
            f"Read docs/managed/{rel} and translate it from English to Russian, "
            f"saving to docs/managed-ru/{rel} (create parent directories if needed). "
            f"First read TRANSLATION_STYLE_GUIDE.md and follow it exactly. Key rules: "
            f"(1) Translate ONLY the frontmatter `title:` value; copy the `source:` and `scraped:` "
            f"lines byte-for-byte unchanged. "
            f"(2) Keep Dynatrace product terms in English (OneAgent, ActiveGate, Smartscape, PurePath, "
            f"Davis AI, Grail, Dynatrace, USQL, DQL, ServiceNow, Kubernetes). "
            f"(3) Keep every bold UI label in English exactly as written (for example **Settings**, "
            f"**Dashboards**, **Save**, **Technologies & Processes**) because they match the real interface. "
            f"(4) Preserve all Markdown structure: the same heading count and levels, the same table "
            f"columns and rows, code blocks, links, image URLs, anchors (#...), file paths and ENV "
            f"variables unchanged. Keep the SAME NUMBER OF LINES as the source. "
            f"(5) This is Dynatrace MANAGED (on-premises) documentation; do not add SaaS-specific notes. "
            f"(6) NEVER use the long dash (em-dash) character in the Russian text; use a comma, a colon, "
            f"or parentheses instead. "
            f"(7) If a line contains a broken or garbled character (mojibake), leave those exact bytes unchanged. "
            f"(8) In metric tables, keep metric Names and dimension identifiers in English; translate the "
            f"Description, Unit and Recommended values. "
            f"(9) Also translate the quoted title/tooltip text inside links and images (the text in quotes "
            f"after the URL), but never change the URL itself or any #anchor. "
            f"(10) Use these fixed renderings for the metadata bullets: Overview->Обзор, "
            f"How-to guide->Практическое руководство, Reference->Справочник, Explanation->Пояснение, "
            f"'N-min read'->'Чтение: N мин', 'Published <Mon DD, YYYY>'->'Опубликовано <DD месяца YYYY> г.', "
            f"'Updated on <Mon DD, YYYY>'->'Обновлено <DD месяца YYYY> г.'. "
            f"(11) Translate EVERY heading and bullet, leaving none in English: "
            f"'## Prerequisites'->'## Предварительные условия', '## Related topics'->'## Связанные темы', "
            f"'## Limitations'->'## Известные ограничения', '## Enable monitoring'->'## Включение мониторинга', "
            f"and version bullets like 'Dynatrace version 1.x+'->'Dynatrace версии 1.x+'. In two-column "
            f"message or parameter tables translate the left label cells too (for example Explanation, "
            f"System action, User response). But keep version identifiers and message codes unchanged "
            f"(for example v1beta6, ZDZ079D). "
            f"Use professional, natural, technical Russian with the formal 'вы'. Just translate and save "
            f"the file, output no commentary."
        )

        code, output = run_claude(prompt, timeout=240)

        if code == 0 and ru.exists():
            translated.append(rel)
            log("    OK")
        else:
            failed += 1
            log(f"    FAILED (exit={code})")
            if output:
                for line in output.strip().split("\n")[-3:]:
                    log(f"    > {line[:140]}")

        # Save progress incrementally so we don't lose state on crash
        json.dump(
            {
                "translated_count": len(translated),
                "failed_count": failed,
                "skipped_count": skipped,
                "translated_files": translated,
            },
            open(RESULT_JSON, "w", encoding="utf-8"),
            indent=2,
            ensure_ascii=False,
        )

    elapsed = time.time() - start
    log("")
    log(f"DONE in {int(elapsed // 60)}m {int(elapsed % 60)}s")
    log(f"Translated: {len(translated)} / Failed: {failed} / Skipped: {skipped}")


if __name__ == "__main__":
    main()
