#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Локальная проверка обновлений + перевод + отправка в Telegram.

Запуск:
    python scripts/check_and_notify.py              # полный цикл
    python scripts/check_and_notify.py --notify-only # только тест Telegram
    python scripts/check_and_notify.py --skip-scrape # без скрейпинга
    python scripts/check_and_notify.py --translate   # + автоперевод через API

Переменные окружения (или .env файл):
    TG_BOT_TOKEN  — токен Telegram-бота
    TG_CHAT_ID    — ID чата для уведомлений
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
SCRIPTS_DIR = Path(__file__).parent

# Load .env
def _load_dotenv():
    for env_path in [BASE_DIR / ".env", SCRIPTS_DIR / ".env", Path(".env")]:
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

_load_dotenv()


def send_telegram(msg: str, parse_mode: str = "Markdown") -> bool:
    """Send message via Telegram Bot API."""
    import requests

    token = os.environ.get("TG_BOT_TOKEN", "")
    chat_id = os.environ.get("TG_CHAT_ID", "")

    if not token or not chat_id:
        print("ERROR: TG_BOT_TOKEN or TG_CHAT_ID not set")
        print("Set them in .env file or environment variables")
        return False

    try:
        resp = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={
                "chat_id": chat_id,
                "text": msg,
                "parse_mode": parse_mode,
                "disable_web_page_preview": "true",
            },
            timeout=15,
        )
        if resp.status_code == 200 and resp.json().get("ok"):
            print("Telegram: OK")
            return True
        else:
            print(f"Telegram ERROR: {resp.status_code} — {resp.text[:200]}")
            return False
    except Exception as e:
        print(f"Telegram EXCEPTION: {e}")
        return False


def run_scrape(max_pages: int = 1000) -> bool:
    """Run scraper."""
    import subprocess
    print("=" * 60)
    print("STAGE 1: Scraping docs.dynatrace.com")
    print("=" * 60)
    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "scrape_docs.py"),
         "--max-pages", str(max_pages)],
        cwd=str(SCRIPTS_DIR),
    )
    return result.returncode == 0


def run_detect() -> dict:
    """Run change detection. Returns report dict."""
    import subprocess
    print()
    print("=" * 60)
    print("STAGE 2: Detecting changes")
    print("=" * 60)

    report_json = BASE_DIR / "changes_report.json"
    report_md = BASE_DIR / "changes_report.md"

    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "detect_changes.py"),
         "--source-dir", str(BASE_DIR / "docs" / "en"),
         "--target-dir", str(BASE_DIR / "docs" / "ru"),
         "--repo", "Yerkebulan-Ardabayev/dynatrace-docs-website",
         "--report", str(report_json),
         "--markdown", str(report_md)],
        cwd=str(BASE_DIR),
    )

    if report_json.exists():
        return json.load(open(report_json, "r", encoding="utf-8"))
    return {"new_count": 0, "updated_count": 0, "total_changes": 0}


def run_translate(report: dict, max_articles: int = 50) -> dict:
    """Run auto-translation on changed articles."""
    import subprocess
    print()
    print("=" * 60)
    print(f"STAGE 3: Auto-translating (max {max_articles} articles)")
    print("=" * 60)

    report_path = BASE_DIR / "changes_report.json"
    result_path = BASE_DIR / "translation_result.json"

    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "translate_changed.py"),
         "--report", str(report_path),
         "--max-articles", str(max_articles)],
        cwd=str(BASE_DIR),
    )

    if result_path.exists():
        return json.load(open(result_path, "r", encoding="utf-8"))
    return {"translated_count": 0}


def build_telegram_message(report: dict, translated: int = 0) -> str:
    """Build Telegram notification message."""
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    new = report.get("new_count", 0)
    updated = report.get("updated_count", 0)
    total = report.get("total_changes", 0)
    repo_url = "https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website"
    site_url = "https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/"

    if total > 0:
        msg = f"📝 *Dynatrace Docs — Обновления*\n"
        msg += f"\n📊 Обнаружено *{total}* изменений:\n"
        msg += f"  • Новых статей: *{new}*\n"
        msg += f"  • Обновлённых: *{updated}*\n"

        if translated > 0:
            msg += f"\n✅ Автоперевод: *{translated}* статей переведены\n"

        # Add section breakdown
        sections = {}
        for a in report.get("new_articles", []) + report.get("updated_articles", []):
            sec = a.get("section", "Другое")
            sections.setdefault(sec, []).append(a)

        if sections:
            msg += "\n📋 *Что изменилось:*\n"
            for sec, arts in sorted(sections.items())[:10]:
                titles = [a.get("title", a["path"]) for a in arts[:3]]
                msg += f"*{sec}* ({len(arts)} шт.)\n"
                for t in titles:
                    msg += f"  — {t}\n"
                if len(arts) > 3:
                    msg += f"  — ...и ещё {len(arts)-3}\n"

        # Release details
        releases = [a for a in report.get("new_articles", []) + report.get("updated_articles", [])
                     if a.get("is_release") and a.get("summary")]
        if releases:
            msg += "\n🚀 *Новые релизы:*\n"
            for rel in releases[:3]:
                title = rel.get("title", rel["path"])
                summary = rel["summary"][:300]
                msg += f"\n📦 {title}\n{summary}\n"

        msg += f"\n🕐 Проверка: {date}\n"
        msg += f"🔗 [Issues]({repo_url}/issues?q=label%3Atranslation+is%3Aopen)\n"
        msg += f"🌐 [Сайт]({site_url})"
    else:
        msg = f"✅ *Dynatrace Docs — Синхронизация*\n\n"
        msg += f"Проверка выполнена {date}.\n"
        msg += f"Изменений не обнаружено — все переводы актуальны.\n\n"
        msg += f"🌐 [Сайт]({site_url})"

    return msg


def main():
    parser = argparse.ArgumentParser(
        description="Check Dynatrace docs updates + Telegram notification"
    )
    parser.add_argument("--notify-only", action="store_true",
                        help="Only send test Telegram message (no scrape/detect)")
    parser.add_argument("--skip-scrape", action="store_true",
                        help="Skip scraping, only detect + notify")
    parser.add_argument("--translate", action="store_true",
                        help="Auto-translate changed articles via API")
    parser.add_argument("--max-translate", type=int, default=50,
                        help="Max articles to translate")
    parser.add_argument("--max-pages", type=int, default=1000,
                        help="Max pages to scrape")
    parser.add_argument("--no-notify", action="store_true",
                        help="Skip Telegram notification")
    args = parser.parse_args()

    # Test mode — just send a test message
    if args.notify_only:
        print("Sending test Telegram message...")
        msg = (
            "🧪 *Тест уведомлений Dynatrace Docs*\n\n"
            f"Проверка связи: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            "✅ Бот работает!"
        )
        ok = send_telegram(msg)
        sys.exit(0 if ok else 1)

    # Full pipeline
    print("=" * 60)
    print("DYNATRACE DOCS — LOCAL PIPELINE")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    print()

    # Stage 1: Scrape
    if not args.skip_scrape:
        run_scrape(args.max_pages)

    # Stage 2: Detect
    report = run_detect()
    total = report.get("total_changes", 0)

    # Stage 3: Translate (optional)
    translated = 0
    if args.translate and total > 0:
        t_result = run_translate(report, args.max_translate)
        translated = t_result.get("translated_count", 0)

    # Stage 4: Notify
    print()
    print("=" * 60)
    print("NOTIFICATION")
    print("=" * 60)

    msg = build_telegram_message(report, translated)
    print(f"\nMessage preview:\n{msg}\n")

    if not args.no_notify:
        send_telegram(msg)
    else:
        print("(--no-notify: Telegram skipped)")

    print()
    print(f"Total changes: {total}")
    if translated:
        print(f"Translated: {translated}")
    print("Done.")


if __name__ == "__main__":
    main()
