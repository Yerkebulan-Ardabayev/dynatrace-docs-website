#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ЗАВЕРШЕНИЕ УСТАНОВКИ (после скачивания)
Автоматически выполняет оставшиеся шаги:
- Организация файлов
- Перевод через Groq
- Сборка сайта
"""

import os
import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime

def print_step(step_num, total, title):
    """Красивый заголовок шага"""
    print()
    print("="*70)
    print(f"📍 ШАГ {step_num}/{total}: {title}")
    print("="*70)
    print()

def run_script(script_path, description, show_output=True):
    """Запуск Python скрипта"""
    print(f"▶️  {description}...")
    print()

    start_time = time.time()

    try:
        if show_output:
            # Показываем вывод в реальном времени
            process = subprocess.Popen(
                ['python', script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                bufsize=1
            )

            # Выводим построчно
            for line in process.stdout:
                print(line, end='')

            process.wait()
            returncode = process.returncode
        else:
            result = subprocess.run(
                ['python', script_path],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            returncode = result.returncode
            if returncode != 0:
                print(result.stderr)

        elapsed = time.time() - start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)

        if returncode == 0:
            print()
            print(f"✅ {description} завершено за {minutes}м {seconds}с")
            return True
        else:
            print()
            print(f"⚠️  {description} завершено с ошибками (код {returncode})")
            return False

    except Exception as e:
        print()
        print(f"❌ Ошибка: {e}")
        return False

def check_scraping_done():
    """Проверка, завершено ли скачивание"""
    docs_dir = Path('scripts/dynatrace-docs')
    if not docs_dir.exists():
        return False

    # Считаем markdown файлы
    md_files = list(docs_dir.rglob('*.md'))
    return len(md_files) > 100  # Предполагаем, что должно быть хотя бы 100 файлов

def main():
    """Главная функция"""

    os.chdir(Path(__file__).parent)

    print("="*70)
    print("🚀 АВТОМАТИЧЕСКОЕ ЗАВЕРШЕНИЕ УСТАНОВКИ")
    print("="*70)
    print()
    print("Этот скрипт выполнит:")
    print("  1. ✅ Организация файлов")
    print("  2. ⚡ Супер-быстрый перевод через Groq")
    print("  3. ✅ Сборка сайта")
    print()

    # Проверяем, завершено ли скачивание
    print("🔍 Проверка готовности документации...")

    if not check_scraping_done():
        print()
        print("⚠️  Скачивание ещё не завершено!")
        print()
        print("Варианты:")
        print("  1. Подождите окончания скачивания")
        print("  2. Запустите этот скрипт позже")
        print("  3. Или запустите полную установку: python run_complete.py")
        print()
        return

    print("✅ Документация скачана!")
    print()

    start_time = datetime.now()

    # ШАГ 1: Организация
    print_step(1, 3, "ОРГАНИЗАЦИЯ ФАЙЛОВ")
    success = run_script(
        'scripts/organize_docs.py',
        "Организация файлов документации",
        show_output=True
    )

    if not success:
        print("\n⚠️  Продолжаем несмотря на ошибки...")

    # ШАГ 2: Перевод через Groq
    print_step(2, 3, "СУПЕР-БЫСТРЫЙ ПЕРЕВОД ЧЕРЕЗ GROQ")
    print("⚡ Модель: Llama 3.1 70B")
    print("💰 Стоимость: БЕСПЛАТНО!")
    print("⏱️  Ожидаемое время: 10-15 минут")
    print()

    success = run_script(
        'scripts/translate_docs_groq.py',
        "Качественный перевод на русский",
        show_output=True
    )

    if not success:
        print("\n⚠️  Продолжаем несмотря на ошибки...")

    # ШАГ 3: Сборка сайта
    print_step(3, 3, "СБОРКА САЙТА")

    print("▶️  Сборка MkDocs сайта...")
    print()

    try:
        result = subprocess.run(
            ['mkdocs', 'build'],
            capture_output=False,
            text=True,
            encoding='utf-8'
        )

        if result.returncode == 0:
            print()
            print("✅ Сайт успешно собран!")
        else:
            print()
            print(f"⚠️  Сборка завершена с предупреждениями")

    except Exception as e:
        print()
        print(f"❌ Ошибка сборки: {e}")

    # Итоги
    total_time = datetime.now() - start_time
    minutes = int(total_time.total_seconds() // 60)
    seconds = int(total_time.total_seconds() % 60)

    print()
    print("="*70)
    print("🎉 УСТАНОВКА ЗАВЕРШЕНА!")
    print("="*70)
    print()
    print(f"⏱️  Общее время: {minutes}м {seconds}с")
    print()

    # Статистика
    docs_en = list(Path('docs/en').rglob('*.md')) if Path('docs/en').exists() else []
    docs_ru = list(Path('docs/ru').rglob('*.md')) if Path('docs/ru').exists() else []

    print("📊 Статистика:")
    print(f"   📄 Английских страниц: {len(docs_en)}")
    print(f"   📄 Русских страниц: {len(docs_ru)}")
    if docs_en and docs_ru:
        coverage = (len(docs_ru) / len(docs_en) * 100)
        print(f"   ✅ Покрытие перевода: {coverage:.1f}%")
    print()

    print("🚀 Готово к запуску!")
    print()
    print("Запустите локальный сервер:")
    print("   python local_server.py")
    print()
    print("Затем откройте: http://localhost:5000")
    print()
    print("💡 AI чат будет доступен по кнопке 'AI ⚡' в правом нижнем углу!")
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⛔ Прервано пользователем")
    except Exception as e:
        print(f"\n\n❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
