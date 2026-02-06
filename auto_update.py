#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Автоматическое обновление документации Dynatrace каждый день
Запускается как фоновая служба Windows
"""

import schedule
import time
import subprocess
import logging
from datetime import datetime
from pathlib import Path

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('auto_update.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def update_documentation():
    """Обновление документации"""
    logger.info("="*70)
    logger.info("🔄 НАЧАЛО АВТООБНОВЛЕНИЯ ДОКУМЕНТАЦИИ")
    logger.info("="*70)

    try:
        # 1. Скачивание
        logger.info("[1/4] Скачивание документации...")
        result = subprocess.run(
            ['python', 'scripts/scrape_docs.py', '--max-pages', '1000'],
            capture_output=True,
            text=True,
            timeout=7200,
            encoding='utf-8'
        )

        if result.returncode != 0:
            logger.error(f"Ошибка скачивания: {result.stderr}")
            return False

        logger.info("✅ Скачивание завершено")

        # 2. Организация
        logger.info("[2/4] Организация файлов...")
        result = subprocess.run(
            ['python', 'scripts/organize_docs.py'],
            capture_output=True,
            text=True,
            timeout=600,
            encoding='utf-8'
        )

        if result.returncode != 0:
            logger.error(f"Ошибка организации: {result.stderr}")
            return False

        logger.info("✅ Организация завершена")

        # 3. СУПЕР-БЫСТРЫЙ перевод (Groq - бесплатно!)
        logger.info("[3/4] СУПЕР-БЫСТРЫЙ перевод на русский (Groq Llama 3.1 70B)...")
        result = subprocess.run(
            ['python', 'scripts/translate_docs_groq.py'],
            capture_output=True,
            text=True,
            timeout=7200,
            encoding='utf-8'
        )

        if result.returncode != 0:
            logger.warning(f"Ошибка перевода (продолжаем): {result.stderr}")

        logger.info("✅ Перевод завершен")

        # 4. Сборка сайта
        logger.info("[4/4] Сборка сайта...")
        result = subprocess.run(
            ['mkdocs', 'build'],
            capture_output=True,
            text=True,
            timeout=300,
            encoding='utf-8'
        )

        if result.returncode != 0:
            logger.error(f"Ошибка сборки: {result.stderr}")
            return False

        logger.info("✅ Сборка завершена")

        logger.info("="*70)
        logger.info(f"✅ ОБНОВЛЕНИЕ ЗАВЕРШЕНО: {datetime.now()}")
        logger.info("="*70)

        return True

    except subprocess.TimeoutExpired:
        logger.error("❌ Превышено время ожидания")
        return False
    except Exception as e:
        logger.error(f"❌ Ошибка обновления: {str(e)}")
        return False

def main():
    """Главная функция"""
    print("="*70)
    print("🤖 АВТООБНОВЛЕНИЕ DYNATRACE ДОКУМЕНТАЦИИ")
    print("="*70)
    print()
    print("📅 Расписание:")
    print("   • Каждый день в 03:00 - полное обновление")
    print("   • Каждые 12 часов - быстрая проверка")
    print()
    print("📝 Логи: auto_update.log")
    print("="*70)
    print()

    # Расписание
    schedule.every().day.at("03:00").do(update_documentation)
    schedule.every(12).hours.do(update_documentation)

    # Первое обновление сразу (опционально)
    # print("🚀 Запуск первичного обновления...")
    # update_documentation()

    # Основной цикл
    print("⏰ Ожидание расписания...")
    print("   (Ctrl+C для остановки)")
    print()

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⛔ Остановлено пользователем")
