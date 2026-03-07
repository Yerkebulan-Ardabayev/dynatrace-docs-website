#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Локальный сервер для Dynatrace Documentation
✅ AI чат (Groq Llama 3.3 70B - серверный прокси)
✅ Rate limiting (10 req/min per IP)
✅ Conversation history
✅ Автообновление документации
✅ Работает локально (127.0.0.1 по умолчанию)
"""

import os
import sys
import json
import secrets
import subprocess
import time
import threading
from collections import defaultdict
import requests as http_requests
from pathlib import Path
from datetime import datetime
from functools import wraps
from flask import Flask, request, jsonify, send_from_directory, send_file, abort
from dotenv import load_dotenv

# Загрузка .env (API ключи)
load_dotenv()

# Настройка кодировки для Windows
if sys.platform == 'win32':
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__, static_folder='site', static_url_path='')

# Gzip compression for large static files (search index etc.)
try:
    from flask_compress import Compress
    Compress(app)
except ImportError:
    # Manual gzip for search_index.json via after_request
    import gzip as _gzip
    from io import BytesIO

    @app.after_request
    def compress_response(response):
        try:
            if (response.status_code == 200
                    and not response.direct_passthrough
                    and 'gzip' in request.headers.get('Accept-Encoding', '')
                    and response.content_type
                    and ('json' in response.content_type or 'javascript' in response.content_type)
                    and response.content_length
                    and response.content_length > 1024):
                data = response.get_data()
                buf = BytesIO()
                with _gzip.GzipFile(fileobj=buf, mode='wb', compresslevel=6) as gz:
                    gz.write(data)
                compressed = buf.getvalue()
                if len(compressed) < len(data):
                    response.set_data(compressed)
                    response.headers['Content-Encoding'] = 'gzip'
                    response.headers['Content-Length'] = len(compressed)
        except Exception:
            pass
        return response

# ============================================================================
# RATE LIMITING (in-memory, без внешних зависимостей)
# ============================================================================
class RateLimiter:
    """Простой rate limiter — 100% бесплатный, без Redis"""
    def __init__(self, max_requests=10, window_seconds=60):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = defaultdict(list)
        self.lock = threading.Lock()

    def is_allowed(self, key):
        now = time.time()
        with self.lock:
            self.requests[key] = [t for t in self.requests[key] if now - t < self.window]
            if len(self.requests[key]) >= self.max_requests:
                return False
            self.requests[key].append(now)
            return True

    def remaining(self, key):
        now = time.time()
        with self.lock:
            self.requests[key] = [t for t in self.requests[key] if now - t < self.window]
            return max(0, self.max_requests - len(self.requests[key]))

chat_limiter = RateLimiter(max_requests=10, window_seconds=60)

# ============================================================================
# КОНФИГУРАЦИЯ
# ============================================================================
DOCS_DIR = Path('docs')
SITE_DIR = Path('site')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

# Токен для защиты /api/update
UPDATE_TOKEN = os.environ.get('UPDATE_TOKEN', secrets.token_hex(16))

# Информация об AI
AI_ENABLED = bool(GROQ_API_KEY)
if AI_ENABLED:
    print("✅ AI чат (Groq Llama 3.3 70B) активирован!")
    print(f"🛡️  Rate limit: 10 req/min per IP")
else:
    print("⚠️  GROQ_API_KEY не задан - AI чат недоступен")

# ============================================================================
# АУТЕНТИФИКАЦИЯ ДЛЯ ОПАСНЫХ ЭНДПОИНТОВ
# ============================================================================

def require_update_token(f):
    """Декоратор: требует токен для доступа к endpoint"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('X-Update-Token', '')
        if not token or token != UPDATE_TOKEN:
            return jsonify({'error': 'Unauthorized. Set X-Update-Token header.'}), 401
        return f(*args, **kwargs)
    return decorated

# ============================================================================
# ГЛАВНАЯ СТРАНИЦА - ОТДАЧА СТАТИЧЕСКОГО САЙТА
# ============================================================================

@app.route('/')
def index():
    """Главная страница"""
    return send_from_directory(SITE_DIR, 'index.html')

# ============================================================================
# API - AI ЧАТ (СЕРВЕРНЫЙ ПРОКСИ + RATE LIMITING)
# ============================================================================

@app.route('/api/chat', methods=['POST'])
def chat_proxy():
    """Прокси для Groq API — ключ остаётся на сервере, rate-limited"""
    if not GROQ_API_KEY:
        return jsonify({'error': 'API key not configured on server'}), 503

    # Rate limiting по IP
    client_ip = request.remote_addr or 'unknown'
    if not chat_limiter.is_allowed(client_ip):
        remaining = chat_limiter.remaining(client_ip)
        return jsonify({
            'error': 'Превышен лимит запросов (10/мин). Подождите.',
            'retry_after': 60
        }), 429

    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Missing "message" field'}), 400

    message = data['message']
    context = data.get('context', '')

    try:
        response = http_requests.post(
            GROQ_API_URL,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {GROQ_API_KEY}'
            },
            json={
                'model': 'llama-3.3-70b-versatile',
                'messages': [
                    {'role': 'system', 'content': context},
                    {'role': 'user', 'content': message}
                ],
                'temperature': 0.7,
                'max_tokens': 1024,
                'top_p': 1,
                'stream': False
            },
            timeout=30
        )

        if response.status_code == 429:
            return jsonify({'error': 'Groq rate limit. Подождите 30с.'}), 429

        if response.status_code != 200:
            return jsonify({'error': f'Groq API error: {response.status_code}'}), 502

        result = response.json()
        answer = result['choices'][0]['message']['content']

        resp = jsonify({
            'choices': [{'message': {'content': answer}}]
        })
        resp.headers['X-RateLimit-Remaining'] = str(chat_limiter.remaining(client_ip))
        return resp

    except http_requests.Timeout:
        return jsonify({'error': 'Request timeout (30s)'}), 504
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

# ============================================================================
# API - ОБНОВЛЕНИЕ ДОКУМЕНТАЦИИ (ЗАЩИЩЕНО ТОКЕНОМ)
# ============================================================================

@app.route('/api/update', methods=['POST'])
@require_update_token
def update_docs():
    """Обновление документации (скачивание + перевод + сборка)"""

    try:
        print("\n" + "="*70)
        print("🔄 ЗАПУСК ОБНОВЛЕНИЯ ДОКУМЕНТАЦИИ")
        print("="*70)

        # Шаг 1: Скачивание
        print("\n[1/5] Скачивание документации с docs.dynatrace.com...")
        result = subprocess.run(
            ['python', 'scripts/scrape_docs.py', '--max-pages', '1000'],
            capture_output=True, text=True, timeout=7200, encoding='utf-8'
        )
        if result.returncode != 0:
            return jsonify({'success': False, 'error': f'Scrape failed: {result.stderr[:200]}'}), 500
        print("✅ Скачивание завершено")

        # Шаг 2: Организация
        print("\n[2/5] Организация файлов...")
        result = subprocess.run(
            ['python', 'scripts/organize_docs.py'],
            capture_output=True, text=True, timeout=600, encoding='utf-8'
        )
        if result.returncode != 0:
            return jsonify({'success': False, 'error': f'Organize failed: {result.stderr[:200]}'}), 500
        print("✅ Организация завершена")

        # Шаг 3: Перевод
        print("\n[3/5] Перевод на русский (Gemini + Groq fallback)...")
        result = subprocess.run(
            ['python', 'scripts/translate_docs_groq.py'],
            capture_output=True, text=True, timeout=7200, encoding='utf-8'
        )
        if result.returncode != 0:
            print(f"⚠️  Перевод с ошибками (продолжаем): {result.stderr[:200]}")
        print("✅ Перевод завершен")

        # Шаг 4: Валидация переводов (NEW!)
        print("\n[4/5] Валидация переводов...")
        result = subprocess.run(
            ['python', 'scripts/validate_translations.py'],
            capture_output=True, text=True, timeout=300, encoding='utf-8',
            cwd='scripts'
        )
        if result.returncode != 0:
            print(f"⚠️  Валидация: найдены проблемы (продолжаем)")
        else:
            print("✅ Валидация пройдена")

        # Шаг 5: Сборка сайта
        print("\n[5/5] Сборка сайта...")
        result = subprocess.run(
            ['mkdocs', 'build'],
            capture_output=True, text=True, timeout=300, encoding='utf-8'
        )
        if result.returncode != 0:
            return jsonify({'success': False, 'error': f'Build failed: {result.stderr[:200]}'}), 500
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
        return jsonify({'success': False, 'error': 'Превышено время ожидания'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': 'Internal error'}), 500

# ============================================================================
# API - СТАТУС
# ============================================================================

@app.route('/api/status')
def status():
    """Статус сервера и документации"""
    en_docs = list(DOCS_DIR.glob('en/**/*.md')) if (DOCS_DIR / 'en').exists() else []
    ru_docs = list(DOCS_DIR.glob('ru/**/*.md')) if (DOCS_DIR / 'ru').exists() else []

    return jsonify({
        'server': 'online',
        'ai_enabled': AI_ENABLED,
        'ai_chat_model': 'Groq Llama 3.3 70B',
        'translation_model': 'Gemini Flash + Groq Fallback',
        'rate_limit': '10 req/min per IP',
        'documentation': {
            'english': len(en_docs),
            'russian': len(ru_docs),
            'translation_coverage': f"{(len(ru_docs)/len(en_docs)*100):.1f}%" if en_docs else '0%'
        },
        'last_update': datetime.now().isoformat()
    })

# ============================================================================
# ОТДАЧА СТАТИЧЕСКИХ ФАЙЛОВ (после API маршрутов)
# ============================================================================

@app.route('/<path:path>')
def serve_static(path):
    """Отдача статических файлов"""
    return send_from_directory(SITE_DIR, path)

@app.errorhandler(404)
def handle_404(e):
    """Обработка 404: поддержка directory URLs (MkDocs)"""
    path = request.path.strip('/')
    if path:
        index_file = SITE_DIR / path / 'index.html'
        if index_file.exists():
            return send_file(str(index_file.resolve()))
    return send_from_directory(SITE_DIR, '404.html'), 404

# ============================================================================
# ЗАПУСК СЕРВЕРА
# ============================================================================

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Dynatrace Documentation Server')
    parser.add_argument('--host', default='127.0.0.1', help='Bind address (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=5000, help='Port (default: 5000)')
    parser.add_argument('--public', action='store_true', help='Listen on 0.0.0.0 (LAN access)')
    args = parser.parse_args()

    bind_host = '0.0.0.0' if args.public else args.host

    print("="*70)
    print("🚀 DYNATRACE DOCUMENTATION SERVER")
    print("="*70)
    print()
    print("📚 Документация Dynatrace с AI чатом")
    print(f"🤖 AI чат: {'Groq Llama 3.3 70B' if AI_ENABLED else 'НЕ НАСТРОЕН (set GROQ_API_KEY)'}")
    print(f"🛡️  Rate limit: 10 req/min per IP")
    print(f"✨ Перевод: Gemini Flash + Groq Fallback")
    print("🌍 Язык: Английский + Русский")
    print()

    if not SITE_DIR.exists():
        print("⚠️  Сайт не собран. Запустите: mkdocs build")
        print()

    print("="*70)
    print("✅ Сервер запущен!")
    print()
    print(f"🌐 Адрес: http://{bind_host}:{args.port}")
    print(f"🔑 Update token: {UPDATE_TOKEN}")
    print("   Пример: curl -X POST -H 'X-Update-Token: <token>' http://localhost:5000/api/update")
    print("="*70)
    print()

    app.run(
        host=bind_host,
        port=args.port,
        debug=False,
        threaded=True
    )
