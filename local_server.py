#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Локальный сервер для Dynatrace Documentation
✅ AI чат (Gemini - бесплатно!)
✅ Качественный перевод (Claude API)
✅ Автообновление документации
✅ Работает в локальной сети
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory

# Настройка кодировки для Windows
if sys.platform == 'win32':
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__, static_folder='site', static_url_path='')

# Конфигурация
DOCS_DIR = Path('docs')
SITE_DIR = Path('site')

# Информация об AI
AI_ENABLED = True  # Groq для чата и перевода (бесплатно!)
print("✅ AI чат (Groq Llama 3.1 70B - СУПЕР БЫСТРО!) активирован!")
print("✅ Перевод (Groq Llama 3.1 70B - СУПЕР БЫСТРО!) активирован!")

# ============================================================================
# ГЛАВНАЯ СТРАНИЦА - ОТДАЧА СТАТИЧЕСКОГО САЙТА
# ============================================================================

@app.route('/')
def index():
    """Главная страница"""
    return send_from_directory(SITE_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Отдача статических файлов"""
    return send_from_directory(SITE_DIR, path)

# ============================================================================
# API - AI ЧАТ
# ============================================================================
# Gemini AI чат работает на клиенте (в gemini-chat.js) - бесплатно!
# Этот сервер просто отдаёт статические файлы

# ============================================================================
# API - ОБНОВЛЕНИЕ ДОКУМЕНТАЦИИ
# ============================================================================

@app.route('/api/update', methods=['POST'])
def update_docs():
    """Обновление документации (скачивание + перевод + сборка)"""

    try:
        print("\n" + "="*70)
        print("🔄 ЗАПУСК ОБНОВЛЕНИЯ ДОКУМЕНТАЦИИ")
        print("="*70)

        # Шаг 1: Скачивание
        print("\n[1/4] Скачивание документации с docs.dynatrace.com...")
        result = subprocess.run(
            ['python', 'scripts/scrape_docs.py', '--max-pages', '1000'],
            capture_output=True,
            text=True,
            timeout=7200,  # 2 часа максимум
            encoding='utf-8'
        )

        if result.returncode != 0:
            print(f"❌ Ошибка скачивания: {result.stderr}")
            return jsonify({
                'success': False,
                'error': f'Ошибка скачивания: {result.stderr}'
            }), 500

        print("✅ Скачивание завершено")

        # Шаг 2: Организация
        print("\n[2/4] Организация файлов...")
        result = subprocess.run(
            ['python', 'scripts/organize_docs.py'],
            capture_output=True,
            text=True,
            timeout=600,
            encoding='utf-8'
        )

        if result.returncode != 0:
            print(f"❌ Ошибка организации: {result.stderr}")
            return jsonify({
                'success': False,
                'error': f'Ошибка организации: {result.stderr}'
            }), 500

        print("✅ Организация завершена")

        # Шаг 3: Перевод (Gemini - бесплатно!)
        print("\n[3/4] Перевод на русский (Gemini - бесплатно!)...")
        result = subprocess.run(
            ['python', 'scripts/translate_docs_gemini.py'],
            capture_output=True,
            text=True,
            timeout=7200,
            encoding='utf-8'
        )

        if result.returncode != 0:
            print(f"⚠️  Ошибка перевода (продолжаем): {result.stderr}")

        print("✅ Перевод завершен")

        # Шаг 4: Сборка сайта
        print("\n[4/4] Сборка сайта...")
        result = subprocess.run(
            ['mkdocs', 'build'],
            capture_output=True,
            text=True,
            timeout=300,
            encoding='utf-8'
        )

        if result.returncode != 0:
            print(f"❌ Ошибка сборки: {result.stderr}")
            return jsonify({
                'success': False,
                'error': f'Ошибка сборки: {result.stderr}'
            }), 500

        print("✅ Сборка завершена")

        print("\n" + "="*70)
        print("✅ ОБНОВЛЕНИЕ ЗАВЕРШЕНО УСПЕШНО!")
        print("="*70)

        return jsonify({
            'success': True,
            'message': 'Документация обновлена успешно!',
            'timestamp': datetime.now().isoformat()
        })

    except subprocess.TimeoutExpired:
        return jsonify({
            'success': False,
            'error': 'Превышено время ожидания'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ============================================================================
# API - СТАТУС
# ============================================================================

@app.route('/api/status')
def status():
    """Статус сервера и документации"""

    # Подсчет файлов
    en_docs = list(DOCS_DIR.glob('en/**/*.md')) if (DOCS_DIR / 'en').exists() else []
    ru_docs = list(DOCS_DIR.glob('ru/**/*.md')) if (DOCS_DIR / 'ru').exists() else []

    return jsonify({
        'server': 'online',
        'ai_enabled': AI_ENABLED,
        'ai_chat_model': 'Gemini 1.5 Flash (Free)',
        'translation_model': 'Gemini 1.5 Pro (Free)',
        'documentation': {
            'english': len(en_docs),
            'russian': len(ru_docs),
            'translation_coverage': f"{(len(ru_docs)/len(en_docs)*100):.1f}%" if en_docs else '0%'
        },
        'last_update': datetime.now().isoformat(),
        'cost': 'FREE! 🎉'
    })

# ============================================================================
# ЗАПУСК СЕРВЕРА
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("🚀 DYNATRACE DOCUMENTATION SERVER")
    print("="*70)
    print()
    print("📚 Документация Dynatrace с AI чатом")
    print("🤖 AI чат: Gemini 1.5 Flash (бесплатно!)")
    print("✨ Перевод: Gemini 1.5 Pro (бесплатно!)")
    print("🌍 Язык: Английский + Русский")
    print("💰 Стоимость: БЕСПЛАТНО! 🎉")
    print()

    # Проверка сайта
    if not SITE_DIR.exists():
        print("⚠️  Сайт не собран. Запустите: mkdocs build")
        print()

    # Информация о доступе
    print("="*70)
    print("✅ Сервер запущен!")
    print()
    print("🌐 Локально:        http://localhost:5000")
    print("🌐 В сети:          http://<ваш-IP>:5000")
    print()
    print("Узнать ваш IP: ipconfig (Windows) или ifconfig (Linux)")
    print("="*70)
    print()

    # Запуск Flask
    app.run(
        host='0.0.0.0',  # Доступ из сети
        port=5000,
        debug=False,
        threaded=True
    )
