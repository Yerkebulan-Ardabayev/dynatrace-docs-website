#!/usr/bin/env python3
"""
Upload documentation files to Google NotebookLM via Playwright.
Semi-automated: opens browser, you log in, then files upload automatically.

Usage:
    pip install playwright
    playwright install chromium
    python scripts/upload_to_notebooklm.py

Features:
    - Uploads files in batches of 50 (NotebookLM limit)
    - Auto-detects file input on page
    - Progress tracking with ETA
    - Fallback to manual upload if auto fails
"""

import asyncio
import sys
import io
import time
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("=" * 50)
    print("Playwright не установлен! Установите:")
    print("  pip install playwright")
    print("  playwright install chromium")
    print("=" * 50)
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
NOTEBOOKLM_DIR = PROJECT_ROOT / "docs" / "notebooklm"
NOTEBOOKLM_URL = "https://notebooklm.google.com"
BATCH_SIZE = 50
MAX_SOURCES = 300


async def try_auto_upload(page, files):
    """Попытка автоматически загрузить файлы через file input."""
    try:
        # Ищем кнопку "Add source"
        for selector in [
            'button:has-text("Add source")',
            'button:has-text("Добавить источник")',
            '[aria-label="Add source"]',
            '[aria-label="Добавить источник"]',
        ]:
            try:
                btn = page.locator(selector).first
                if await btn.is_visible(timeout=2000):
                    await btn.click()
                    await asyncio.sleep(2)
                    break
            except Exception:
                continue

        # Ищем опцию Upload
        for selector in [
            'text="Upload"', 'text="Загрузить"',
            'text="Upload file"', 'text="Загрузить файл"',
        ]:
            try:
                opt = page.locator(selector).first
                if await opt.is_visible(timeout=2000):
                    await opt.click()
                    await asyncio.sleep(2)
                    break
            except Exception:
                continue

        # Ищем file input
        file_input = page.locator('input[type="file"]')
        if await file_input.count() > 0:
            await file_input.set_input_files([str(f) for f in files])
            await asyncio.sleep(3)

            # Ищем кнопку подтверждения
            for selector in [
                'button:has-text("Insert")', 'button:has-text("Добавить")',
                'button:has-text("Upload")', 'button:has-text("Загрузить")',
            ]:
                try:
                    confirm = page.locator(selector).first
                    if await confirm.is_visible(timeout=3000):
                        await confirm.click()
                        await asyncio.sleep(5)
                        return True
                except Exception:
                    continue
            return True  # Files set but no confirm button found
        return False
    except Exception as e:
        print(f"    ❌ Авто-загрузка: {e}")
        return False


async def main():
    md_files = sorted(NOTEBOOKLM_DIR.glob("*.md"))
    if not md_files:
        print("❌ Нет файлов для загрузки!")
        print("   Сначала запустите: python scripts/generate_notebooklm.py")
        return

    if len(md_files) > MAX_SOURCES:
        print(f"⚠️ {len(md_files)} файлов > лимит {MAX_SOURCES}. Загружаю первые {MAX_SOURCES}.")
        md_files = md_files[:MAX_SOURCES]

    print("=" * 60)
    print(f"  📚 NotebookLM Upload — {len(md_files)} файлов")
    print(f"  📂 {NOTEBOOKLM_DIR}")
    print("=" * 60)
    print()
    input("  Нажмите ENTER для открытия браузера...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--start-maximized"])
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()

        print("\n[1] 🌐 Открываю NotebookLM...")
        await page.goto(NOTEBOOKLM_URL, timeout=30000)
        await asyncio.sleep(3)

        print()
        print("=" * 60)
        print("  📋 ДЕЙСТВИЕ:")
        print("  1. Войдите в Google аккаунт")
        print("  2. Создайте/откройте ноутбук 'Dynatrace Documentation'")
        print("  3. Вернитесь сюда")
        print("=" * 60)
        input("\n  Нажмите ENTER когда внутри ноутбука...")

        # Upload in batches
        batches = [md_files[i:i + BATCH_SIZE] for i in range(0, len(md_files), BATCH_SIZE)]
        uploaded = 0
        start = time.time()

        for bn, batch in enumerate(batches, 1):
            print(f"\n  📦 Батч {bn}/{len(batches)} ({len(batch)} файлов)")

            # Try auto
            success = await try_auto_upload(page, batch)

            if success:
                uploaded += len(batch)
                print(f"    ✅ Загружено автоматически!")
            else:
                # Manual fallback
                print(f"    ⚠️ Авто не сработало — ручной режим:")
                print(f"    Нажмите 'Add source' → 'Upload' в NotebookLM")
                print(f"    Выберите файлы из: {NOTEBOOKLM_DIR}")
                for f in batch[:5]:
                    print(f"      • {f.name}")
                if len(batch) > 5:
                    print(f"      ... и ещё {len(batch) - 5}")
                input(f"    Нажмите ENTER когда загрузите...")
                uploaded += len(batch)

            elapsed = time.time() - start
            pct = uploaded * 100 // len(md_files)
            print(f"    📊 {uploaded}/{len(md_files)} ({pct}%)")

            if bn < len(batches):
                await asyncio.sleep(3)

        total_time = time.time() - start
        print()
        print("=" * 60)
        print(f"  ✅ ГОТОВО! {uploaded}/{len(md_files)} файлов загружено")
        print(f"  ⏱️ {int(total_time // 60)}м {int(total_time % 60)}с")
        print(f"  🧠 NotebookLM RAG готов!")
        print("=" * 60)

        input("\n  ENTER для закрытия браузера...")
        await browser.close()


if __name__ == "__main__":
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    asyncio.run(main())
