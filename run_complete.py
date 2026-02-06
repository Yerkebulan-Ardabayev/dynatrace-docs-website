#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ПОЛНАЯ АВТОМАТИЧЕСКАЯ УСТАНОВКА
Скачивание → Организация → Перевод → Сборка → Запуск сервера
ВСЁ АВТОМАТИЧЕСКИ!
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def print_banner(text):
    """Красивый баннер"""
    print()
    print("="*70)
    print(f"🚀 {text}")
    print("="*70)
    print()

def run_command(cmd, description, timeout=7200):
    """Запуск команды с красивым выводом"""
    print(f"\n{'='*70}")
    print(f"▶️  {description}")
    print(f"{'='*70}\n")

    try:
        result = subprocess.run(
            cmd,
            capture_output=False,  # Показываем вывод в реальном времени
            text=True,
            timeout=timeout,
            shell=True if isinstance(cmd, str) else False
        )

        if result.returncode == 0:
            print(f"\n✅ {description} - УСПЕШНО!\n")
            return True
        else:
            print(f"\n⚠️  {description} - ОШИБКА (код {result.returncode})\n")
            return False

    except subprocess.TimeoutExpired:
        print(f"\n⏱️  {description} - ПРЕВЫШЕН ТАЙМАУТ\n")
        return False
    except Exception as e:
        print(f"\n❌ {description} - ОШИБКА: {e}\n")
        return False

def main():
    """Главная функция"""

    print_banner("ПОЛНАЯ АВТОМАТИЧЕСКАЯ УСТАНОВКА DYNATRACE DOCS")

    print("📋 План работы:")
    print("   1. ⬇️  Скачивание документации (1000 страниц)")
    print("   2. 📁 Организация файлов")
    print("   3. ⚡ СУПЕР-БЫСТРЫЙ перевод через Groq")
    print("   4. 🏗️  Сборка сайта")
    print("   5. 🚀 Запуск локального сервера")
    print()

    input("Нажмите Enter для старта... ")

    # Переходим в директорию проекта
    os.chdir(Path(__file__).parent)

    # ШАГ 1: Скачивание
    print_banner("ШАГ 1/5: СКАЧИВАНИЕ ДОКУМЕНТАЦИИ")
    print("⏱️  Примерное время: 20-25 минут")
    print("📊 Скачиваем 1000 страниц с docs.dynatrace.com...")
    print()

    success = run_command(
        ['python', 'scripts/scrape_docs.py', '--max-pages', '1000'],
        "Скачивание документации",
        timeout=7200
    )

    if not success:
        print("❌ Ошибка скачивания. Прерываю.")
        return

    # ШАГ 2: Организация
    print_banner("ШАГ 2/5: ОРГАНИЗАЦИЯ ФАЙЛОВ")
    print("⏱️  Примерное время: 30 секунд")
    print()

    success = run_command(
        ['python', 'scripts/organize_docs.py'],
        "Организация файлов",
        timeout=600
    )

    if not success:
        print("⚠️  Ошибка организации, но продолжаем...")

    # ШАГ 3: Перевод (GROQ - СУПЕР БЫСТРО!)
    print_banner("ШАГ 3/5: СУПЕР-БЫСТРЫЙ ПЕРЕВОД ЧЕРЕЗ GROQ")
    print("⚡ Модель: Llama 3.1 70B")
    print("⏱️  Примерное время: 10-15 минут (в 10 раз быстрее обычного!)")
    print("💰 Стоимость: БЕСПЛАТНО!")
    print()

    success = run_command(
        ['python', 'scripts/translate_docs_groq.py'],
        "Качественный перевод на русский",
        timeout=7200
    )

    if not success:
        print("⚠️  Ошибка перевода, но продолжаем...")

    # ШАГ 4: Сборка сайта
    print_banner("ШАГ 4/5: СБОРКА САЙТА")
    print("⏱️  Примерное время: 30 секунд")
    print()

    success = run_command(
        ['mkdocs', 'build'],
        "Сборка сайта MkDocs",
        timeout=300
    )

    if not success:
        print("❌ Ошибка сборки сайта. Проверьте mkdocs.")
        return

    # ШАГ 5: Готово!
    print_banner("УСТАНОВКА ЗАВЕРШЕНА! 🎉")

    print("✅ Всё готово к работе!")
    print()
    print("📊 Статистика:")

    # Подсчет файлов
    docs_en = list(Path('docs/en').rglob('*.md')) if Path('docs/en').exists() else []
    docs_ru = list(Path('docs/ru').rglob('*.md')) if Path('docs/ru').exists() else []

    print(f"   📄 Английских страниц: {len(docs_en)}")
    print(f"   📄 Русских страниц: {len(docs_ru)}")
    if docs_en:
        coverage = (len(docs_ru) / len(docs_en) * 100)
        print(f"   📊 Покрытие перевода: {coverage:.1f}%")
    print()

    print("🚀 Запустить локальный сервер?")
    print()
    print("   Команда: python local_server.py")
    print("   URL: http://localhost:5000")
    print()

    choice = input("Запустить сейчас? (y/n): ").lower()

    if choice == 'y':
        print_banner("ЗАПУСК ЛОКАЛЬНОГО СЕРВЕРА")
        print("🌐 Сервер запускается на http://localhost:5000")
        print("🤖 AI чат: Groq Llama 3.1 70B (супер быстро!)")
        print()
        print("Нажмите Ctrl+C для остановки")
        print()

        try:
            subprocess.run(['python', 'local_server.py'])
        except KeyboardInterrupt:
            print("\n\n✅ Сервер остановлен")
    else:
        print()
        print("💡 Запустите вручную когда будете готовы:")
        print("   python local_server.py")
        print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⛔ Прервано пользователем")
    except Exception as e:
        print(f"\n\n❌ Критическая ошибка: {e}")
