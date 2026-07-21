#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Перевод документации Dynatrace

Порядок провайдеров:
  1. claude -p  (подписка Claude Code, основной)
  2. Google Gemini Flash (1500 req/day бесплатно)
  3. Groq Llama 3.3 70B (100K tokens/day бесплатно)
  4. OpenRouter (бесплатные модели)

Каждый следующий включается, только если предыдущий недоступен, поэтому при
живой подписке переводит она, а бесплатные ключи это запасной вариант.

Авторизация и ключи берутся ТОЛЬКО из окружения / .env (никогда не в коде):
  CLAUDE_CODE_OAUTH_TOKEN — токен из `claude setup-token` (headless-режим)
  GEMINI_API_KEY  — https://aistudio.google.com/apikey
  GROQ_API_KEY    — https://console.groq.com
"""

import os
import sys
import io
import json
import time
import shutil
import hashlib
import subprocess
from pathlib import Path

# requests нужен ТОЛЬКО запасным HTTP-провайдерам (Gemini/Groq/OpenRouter).
# Основной путь идёт через claude -p, поэтому отсутствие библиотеки не должно
# ронять перевод целиком: провайдеры, которым она нужна, просто отключатся.
try:
    import requests
except ImportError:
    requests = None

# Fix Windows encoding (cp1251 can't handle emoji)
if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
        elif hasattr(sys.stdout, 'buffer'):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

# Загрузка .env файла (если есть)
def _load_dotenv():
    env_paths = [
        Path(__file__).parent.parent / '.env',  # корень проекта
        Path(__file__).parent / '.env',
        Path('.env'),
    ]
    for env_path in env_paths:
        if env_path.exists():
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, _, val = line.partition('=')
                        key = key.strip()
                        val = val.strip().strip('"').strip("'")
                        if key and key not in os.environ:
                            os.environ[key] = val
            break
_load_dotenv()

# API ключи из окружения (или .env)
GEMINI_API_KEYS = [val for key, val in os.environ.items() if key.startswith('GEMINI_API_KEY') and val]
GEMINI_API_KEY = GEMINI_API_KEYS[0] if GEMINI_API_KEYS else ''
GROQ_API_KEY   = os.environ.get('GROQ_API_KEY', '')
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')

# --- claude -p (подписка Claude Code) ---
# Авторизация headless-вызова идёт через CLAUDE_CODE_OAUTH_TOKEN (`claude setup-token`).
# Без токена CLI отвечает "Not logged in", провайдер отдаёт None и включается fallback.
CLAUDE_ENABLED = os.environ.get('CLAUDE_TRANSLATE', '1') != '0'
CLAUDE_BIN     = os.environ.get('CLAUDE_BIN', 'claude')
CLAUDE_MODEL   = os.environ.get('CLAUDE_TRANSLATE_MODEL', 'sonnet')
CLAUDE_TIMEOUT = int(os.environ.get('CLAUDE_TRANSLATE_TIMEOUT', '600'))
# Пауза при упоре в лимит подписки, потом одна повторная попытка.
CLAUDE_LIMIT_WAIT = int(os.environ.get('CLAUDE_TRANSLATE_LIMIT_WAIT', '300'))

GROQ_API_URL   = 'https://api.groq.com/openai/v1/chat/completions'
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'
# Бесплатные модели OpenRouter — пробуем по очереди при rate limit
OPENROUTER_MODELS = [
    'google/gemma-3-27b-it:free',           # Google Gemma 3 27B (работает!)
    'meta-llama/llama-3.3-70b-instruct:free', # Llama 3.3 70B
    'microsoft/phi-4-reasoning-plus:free',   # Microsoft Phi-4
    'qwen/qwen3-8b:free',                   # Qwen 3 8B
]

# Директории
DOCS_DIR = Path('../docs')
EN_DIR   = DOCS_DIR / 'en'
RU_DIR   = DOCS_DIR / 'ru'

# Кеш переводов
CACHE_FILE = Path('.translation_cache_groq.json')
cache = {}
if CACHE_FILE.exists():
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        cache = json.load(f)

MAX_CHUNK_CHARS = 10000

import re

# ============================================================================
# ЗАЩИТА BRAND-ТЕРМИНОВ (placeholder-подход — 100% надёжность)
# ============================================================================
# LLM иногда игнорирует инструкцию "не переводи".
# Решение: заменяем термины на плейсхолдеры ПЕРЕД отправкой,
# восстанавливаем ПОСЛЕ получения перевода. Модель физически
# не может перевести то, чего нет в тексте.

PROTECTED_TERMS = [
    # Dynatrace products (порядок важен! Длинные первыми)
    'Cluster Management Console', 'Real User Monitoring',
    'Synthetic Monitoring', 'Session Replay', 'Service Flow',
    'Management Zone', 'Mission Control', 'Host Group', 'Host Unit',
    'OneAgent', 'ActiveGate', 'Smartscape', 'PurePath', 'Davis AI',
    'AppEngine', 'Dynatrace', 'Extensions', 'Environment',
    'Grail', 'DQL', 'CMC', 'Hub',
    # Cloud / DevOps
    'Kubernetes', 'OpenShift', 'Docker', 'Ansible', 'Helm',
    'REST API', 'gRPC', 'AWS', 'Azure', 'GCP',
    'API', 'SDK', 'JSON', 'YAML', 'XML',
]

def protect_terms(text: str) -> tuple[str, dict]:
    """Заменяет protected terms на плейсхолдеры. Возвращает (text, mapping)."""
    mapping = {}
    counter = 0
    for term in PROTECTED_TERMS:
        # Case-sensitive поиск
        pattern = re.compile(re.escape(term))
        if pattern.search(text):
            placeholder = f'__KEEP{counter:03d}__'
            mapping[placeholder] = term
            text = pattern.sub(placeholder, text)
            counter += 1
    return text, mapping

def restore_terms(text: str, mapping: dict) -> str:
    """Восстанавливает оригинальные термины из плейсхолдеров."""
    for placeholder, term in mapping.items():
        text = text.replace(placeholder, term)
    return text

def post_fix_known_errors(text: str) -> str:
    """Исправляет известные ошибочные переводы (на случай старого кеша)."""
    fixes = {
        'Один Агент': 'OneAgent', 'ОдинАгент': 'OneAgent',
        'Один агент': 'OneAgent', 'одинагент': 'OneAgent',
        'Активный шлюз': 'ActiveGate', 'Активгейт': 'ActiveGate',
        'Активный Шлюз': 'ActiveGate',
        'Чистый путь': 'PurePath', 'Чистый Путь': 'PurePath',
        'Умная карта': 'Smartscape', 'Умный ландшафт': 'Smartscape',
        'Консоль управления кластером': 'Cluster Management Console',
        'Центр управления': 'Mission Control',
        'Единица хоста': 'Host Unit', 'Группа хостов': 'Host Group',
    }
    for wrong, correct in fixes.items():
        text = text.replace(wrong, correct)
    return text

TRANSLATION_PROMPT = """Переведи следующую техническую документацию Dynatrace с английского на русский.

ВАЖНО:
- Сохрани всё форматирование Markdown (заголовки, списки, код, ссылки, YAML frontmatter)
- Все слова вида __KEEP000__, __KEEP001__ и т.д. — это плейсхолдеры. НЕ ПЕРЕВОДИ их, оставь как есть!
- Переведи качественно и профессионально
- НЕ добавляй никаких комментариев, только перевод
- Не добавляй вводные фразы типа "Вот перевод:" — сразу начинай с перевода

Текст для перевода:

{text}"""


def split_into_chunks(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list:
    """Разбивает текст на чанки по Markdown-заголовкам"""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    # Границы секций ищем ТОЛЬКО вне блоков кода: строка вида `# установка пакета`
    # внутри ``` это комментарий шелла, а не заголовок, и раньше по ней резали
    # блок кода пополам (11 крупных статей корпуса, включая agctl и quarkus).
    sections = _split_outside_code(text, lambda ln: re.match(r'^#{1,3} ', ln))
    current_chunk = ""
    for section in sections:
        if len(current_chunk) + len(section) > max_chars and current_chunk:
            chunks.append(current_chunk)
            current_chunk = section
        else:
            current_chunk += ('\n' if current_chunk else '') + section
    if current_chunk:
        chunks.append(current_chunk)

    final_chunks = []
    for chunk in chunks:
        if len(chunk) <= max_chars:
            final_chunks.append(chunk)
        else:
            # Дробим по абзацам, но НИКОГДА не режем внутри блока кода. Блоки кода
            # содержат пустые строки, поэтому наивное деление по '\n\n' разрывало
            # ``` пополам: чанк получал незакрытый фенс, модель закрывала его
            # по-своему, и статья вечно падала на сверке («было 22, стало 21»).
            # Так намертво зациклились две большие статьи session-data-export.
            sub_chunk = ""
            for para in _paragraphs_keeping_code(chunk):
                if len(sub_chunk) + len(para) + 2 > max_chars and sub_chunk:
                    final_chunks.append(sub_chunk)
                    sub_chunk = para
                else:
                    sub_chunk += ('\n\n' if sub_chunk else '') + para
            if sub_chunk:
                final_chunks.append(sub_chunk)

    return final_chunks


def _split_outside_code(text: str, is_boundary) -> list:
    """Режет текст по строкам-границам, никогда не заходя внутрь ```-блока.

    Блок кода остаётся целым куском: незакрытый фенс в чанке модель закрывает
    по-своему, и статья потом не проходит сверку структуры.
    """
    parts, buf, in_code = [], [], False
    for line in text.split('\n'):
        fence = line.lstrip().startswith('```')
        if not in_code and not fence and is_boundary(line) and buf:
            parts.append('\n'.join(buf))
            buf = []
        if fence:
            in_code = not in_code
        buf.append(line)
    if buf:
        parts.append('\n'.join(buf))
    return parts


def _paragraphs_keeping_code(text: str) -> list:
    """Абзацы текста, где каждый блок ``` остаётся одним неделимым куском."""
    return [p for p in _split_outside_code(text, lambda ln: ln.strip() == '') if p.strip()]


CLAUDE_SYSTEM_PROMPT = """Ты профессиональный технический переводчик документации Dynatrace с английского на русский.
Ты работаешь как чистый преобразователь текста: на вход markdown, на выход только его перевод.

ЖЁСТКИЕ ПРАВИЛА:
1. Структура сохраняется 1:1: YAML frontmatter, уровни заголовков, списки, таблицы, порядок строк. Число заголовков ровно как в оригинале: если один и тот же заголовок повторён дважды, в переводе он тоже повторяется дважды, схлопывать нельзя.
2. Содержимое блоков кода (```), inline-кода (`...`), URL, якорей и путей файлов НЕ переводится, копируется байт в байт.
3. Плейсхолдеры вида __KEEP000__ копируются как есть.
4. Названия продуктов и компонентов Dynatrace остаются английскими (OneAgent, ActiveGate, PurePath, Smartscape, Davis AI, Cluster Management Console). Названия элементов интерфейса и ключей конфигурации тоже остаются английскими.
5. Длинные тире запрещены. Определения пишутся через запятую: «X, это Y». Допустимы запятая, двоеточие, точка, скобки.
6. Живой технический русский, без канцелярита и без калек «вы можете», пиши безлично: «можно», «нужно».
7. Ошибки и опечатки оригинала переводятся как есть, молча их не исправляй.
8. В ответе только перевод. Никаких вводных фраз, комментариев, объяснений и markdown-обёрток вокруг ответа."""

# Ответы CLI, по которым видно, что дело не в конкретном тексте, а в доступе.
_CLAUDE_AUTH_MARKERS  = ('not logged in', 'please run /login', 'invalid api key',
                         'authentication_error', 'oauth token')
_CLAUDE_LIMIT_MARKERS = ('usage limit', 'limit reached', 'rate limit',
                         'rate_limit_error', 'overloaded')


def claude_available() -> bool:
    """Есть ли смысл вообще дёргать claude -p (включён и бинарь на месте)."""
    return bool(CLAUDE_ENABLED and shutil.which(CLAUDE_BIN))


def translate_via_claude_cli(text: str, extra_rules: str = '') -> str | None:
    """Перевод через `claude -p` по подписке. None при ошибке/лимите → fallback.

    Вызов намеренно стерильный: свой system prompt вместо агентского, инструменты
    запрещены, MCP и слэш-команды выключены, рабочая директория вне репозитория,
    чтобы модель не подтягивала контекст проекта и просто переводила текст.

    extra_rules — правила под конкретный файл (например, норма заголовков в этом
    разделе корпуса), они дописываются к системному промпту.
    """
    if not claude_available():
        return None

    system_prompt = CLAUDE_SYSTEM_PROMPT
    if extra_rules:
        system_prompt += f"\n\nНОРМА ЭТОГО РАЗДЕЛА КОРПУСА (важнее общих правил):\n{extra_rules}"

    cmd = [
        CLAUDE_BIN, '-p',
        '--model', CLAUDE_MODEL,
        '--system-prompt', system_prompt,
        '--disallowed-tools', 'Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,Task,NotebookEdit',
        '--strict-mcp-config',
        '--disable-slash-commands',
        '--output-format', 'text',
    ]
    prompt = f"Переведи на русский:\n\n{text}"

    for attempt in range(2):
        try:
            proc = subprocess.run(
                cmd, input=prompt, capture_output=True, text=True,
                timeout=CLAUDE_TIMEOUT, cwd='/tmp',
            )
        except subprocess.TimeoutExpired:
            print(f"  ⏱️  claude -p: таймаут {CLAUDE_TIMEOUT}с")
            return None
        except Exception as e:
            print(f"  ❌ claude -p: не удалось запустить ({e})")
            return None

        out = (proc.stdout or '').strip()
        # Причина ошибки у CLI приходит и в stdout, и в stderr — смотрим оба.
        diag = f"{out}\n{(proc.stderr or '').strip()}".lower()

        if proc.returncode == 0 and out:
            return out

        if any(m in diag for m in _CLAUDE_AUTH_MARKERS):
            print("  🔑 claude -p: нет авторизации (нужен CLAUDE_CODE_OAUTH_TOKEN "
                  "из `claude setup-token`) — перехожу на запасные ключи")
            return None

        if any(m in diag for m in _CLAUDE_LIMIT_MARKERS) and attempt == 0:
            print(f"  ⏳ claude -p: лимит подписки, жду {CLAUDE_LIMIT_WAIT}с и пробую ещё раз")
            time.sleep(CLAUDE_LIMIT_WAIT)
            continue

        print(f"  ❌ claude -p: rc={proc.returncode} {diag.strip()[:200]}")
        return None

    return None


def translate_via_gemini(text: str) -> str | None:
    """Перевод через Gemini Flash. Возвращает None при ошибке/лимите."""
    if requests is None or not GEMINI_API_KEYS:
        return None

    prompt = TRANSLATION_PROMPT.format(text=text)
    max_retries = 5
    
    for api_key in GEMINI_API_KEYS:
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    f"{GEMINI_API_URL}?key={api_key}",
                    headers={'Content-Type': 'application/json'},
                    json={
                        'contents': [{'parts': [{'text': prompt}]}],
                        'generationConfig': {
                            'temperature': 0.3,
                            'maxOutputTokens': 8192,
                        }
                    },
                    timeout=90
                )

                if response.status_code == 429:
                    # Check if it's daily quota exhausted vs per-minute limit
                    err_text = response.text
                    if 'limit: 0' in err_text or 'quota' in err_text.lower():
                        print(f"  ⏳ Gemini дневная квота исчерпана для ключа, пробую следующий...")
                        break
                    wait = 20 * (attempt + 1)  # 20, 40, 60, 80, 100 sec
                    print(f"  ⏳ Gemini rate limit, жду {wait}с...")
                    time.sleep(wait)
                    continue

                if response.status_code == 403 or response.status_code == 401:
                    print(f"  ❌ Gemini: неверный ключ или квота исчерпана ({response.status_code}), пробую следующий...")
                    break

                if response.status_code != 200:
                    print(f"  ❌ Gemini API ошибка: {response.status_code}")
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                        continue
                    break

                data = response.json()
                candidates = data.get('candidates', [])
                if not candidates:
                    print(f"  ❌ Gemini: пустой ответ")
                    break

                # Обрезка по лимиту токенов — НЕ отдавать усечённый перевод в корпус.
                if candidates[0].get('finishReason') == 'MAX_TOKENS':
                    print(f"  ✂️  Gemini: ответ обрезан (MAX_TOKENS) — бракую, дальше")
                    return None

                translation = candidates[0]['content']['parts'][0]['text'].strip()
                time.sleep(4.0)  # Gemini free: 15 req/min = 4 sec between requests
                return translation

            except requests.Timeout:
                wait = 2 ** (attempt + 1)
                print(f"  ⏳ Gemini таймаут, жду {wait}с...")
                time.sleep(wait)
            except Exception as e:
                print(f"  ❌ Gemini исключение: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2)
                    continue
                break
                
    print(f"  ⏳ Все ключи Gemini исчерпаны — пропускаю на Groq")
    return None


def translate_via_groq(text: str) -> str | None:
    """Перевод через Groq Llama. Возвращает None при ошибке/лимите."""
    if requests is None or not GROQ_API_KEY:
        return None

    prompt = TRANSLATION_PROMPT.format(text=text)
    max_retries = 6
    for attempt in range(max_retries):
        try:
            response = requests.post(
                GROQ_API_URL,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {GROQ_API_KEY}'
                },
                json={
                    'model': 'llama-3.3-70b-versatile',
                    'messages': [{'role': 'user', 'content': prompt}],
                    'temperature': 0.3,
                    'max_tokens': 8000,
                    'top_p': 1,
                    'stream': False
                },
                timeout=90
            )

            if response.status_code == 429:
                retry_after = response.headers.get('retry-after', '')
                wait = int(retry_after) if retry_after.isdigit() else min(10 * (attempt + 1), 60)
                # Если ждать слишком долго (>60с) — сразу на следующий API
                if wait > 60:
                    print(f"  ⏳ Groq rate limit {wait}с — слишком долго, передаю следующему API")
                    return None
                print(f"  ⏳ Groq rate limit, жду {wait}с... (попытка {attempt+1}/{max_retries})")
                time.sleep(wait)
                continue

            if response.status_code != 200:
                print(f"  ❌ Groq API ошибка: {response.status_code}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return None

            result = response.json()
            if 'choices' not in result or not result['choices']:
                print(f"  ❌ Groq: пустой ответ")
                return None

            if result['choices'][0].get('finish_reason') == 'length':
                print(f"  ✂️  Groq: ответ обрезан (finish_reason=length) — бракую")
                return None

            translation = result['choices'][0]['message']['content'].strip()
            time.sleep(2.0)  # Groq: 30 req/min
            return translation

        except requests.Timeout:
            wait = 2 ** (attempt + 1)
            print(f"  ⏳ Groq таймаут, жду {wait}с...")
            time.sleep(wait)
        except Exception as e:
            print(f"  ❌ Groq исключение: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return None

    return None


def translate_via_openrouter(text: str) -> str | None:
    """Перевод через OpenRouter (бесплатные модели). 3-й fallback.
    Перебирает несколько бесплатных моделей при rate limit."""
    if requests is None or not OPENROUTER_API_KEY:
        return None

    prompt = TRANSLATION_PROMPT.format(text=text)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENROUTER_API_KEY}',
        'HTTP-Referer': 'https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website',
        'X-Title': 'Dynatrace Docs Translator'
    }

    for model in OPENROUTER_MODELS:
        for attempt in range(3):
            try:
                response = requests.post(
                    OPENROUTER_API_URL,
                    headers=headers,
                    json={
                        'model': model,
                        'messages': [{'role': 'user', 'content': prompt}],
                        'temperature': 0.3,
                        'max_tokens': 8000,
                    },
                    timeout=120
                )

                if response.status_code == 429:
                    wait = min(15 * (attempt + 1), 45)
                    print(f"  ⏳ OpenRouter [{model}] rate limit, жду {wait}с...")
                    time.sleep(wait)
                    continue

                if response.status_code != 200:
                    err = response.json().get('error', {}).get('message', '')[:80]
                    print(f"  ❌ OpenRouter [{model}] ошибка {response.status_code}: {err}")
                    break  # Попробовать следующую модель

                result = response.json()
                if 'choices' not in result or not result['choices']:
                    print(f"  ❌ OpenRouter [{model}]: пустой ответ")
                    break

                if result['choices'][0].get('finish_reason') == 'length':
                    print(f"  ✂️  OpenRouter [{model}]: обрезан (length) — след. модель")
                    break

                translation = result['choices'][0]['message']['content'].strip()
                time.sleep(2.0)
                print(f"  ✅ OpenRouter [{model}]")
                return translation

            except requests.Timeout:
                print(f"  ⏳ OpenRouter [{model}] таймаут, повтор...")
                time.sleep(5)
            except Exception as e:
                print(f"  ❌ OpenRouter [{model}] исключение: {e}")
                break

    return None


def translate_text(text: str, source_file: str, extra_rules: str = '') -> str:
    """
    Переводит текст. Стратегия:
    1. Проверяем кеш
    2. Защищаем brand-термины плейсхолдерами
    3. Пробуем claude -p по подписке (основной)
    4. Fallback на Gemini Flash (если подписка недоступна)
    5. Fallback на Groq, затем на OpenRouter
    6. Восстанавливаем термины + пост-фикс ошибок
    7. Возвращаем None если недоступны все (файл не трогаем)
    """
    # Правила раздела входят в ключ: один и тот же текст с другой нормой
    # заголовков должен переводиться заново, а не браться из кеша.
    key_src = f"{text}\x00{extra_rules}"
    cache_key = f"{source_file}:{hashlib.sha256(key_src.encode('utf-8')).hexdigest()[:16]}"
    if cache_key in cache:
        print(f"  ↻ Из кеша")
        # Пост-фикс даже для кешированных (на случай старых ошибок)
        return post_fix_known_errors(cache[cache_key])

    # Защищаем термины плейсхолдерами
    protected_text, term_mapping = protect_terms(text)

    translation = None

    # 1. Основной путь — подписка Claude Code
    if claude_available():
        print(f"  🤖 Перевод через claude -p ({CLAUDE_MODEL})...")
        translation = translate_via_claude_cli(protected_text, extra_rules)
        if translation:
            print(f"  ✅ claude успешно!")

    # 2. Fallback на Gemini (бесплатный ключ)
    if translation is None and GEMINI_API_KEY:
        print(f"  🌟 Fallback: Gemini Flash...")
        translation = translate_via_gemini(protected_text)
        if translation:
            print(f"  ✅ Gemini успешно!")

    # 3. Fallback на Groq
    if translation is None and GROQ_API_KEY:
        print(f"  🔄 Fallback: Groq Llama 3.3 70B...")
        translation = translate_via_groq(protected_text)
        if translation:
            print(f"  ✅ Groq успешно!")

    # 4. Fallback на OpenRouter (бесплатные модели)
    if translation is None and OPENROUTER_API_KEY:
        print(f"  🔄 Fallback: OpenRouter (Llama 3.3 70B free)...")
        translation = translate_via_openrouter(protected_text)
        if translation:
            print(f"  ✅ OpenRouter успешно!")

    # 5. Все провайдеры недоступны — возвращаем None (НЕ записываем оригинал!)
    if translation is None:
        print(f"  ⚠️  Все API недоступны — пропускаю файл")
        return None

    # Восстанавливаем brand-термины и фиксим известные ошибки
    translation = restore_terms(translation, term_mapping)
    translation = post_fix_known_errors(translation)

    # Сохраняем в кеш
    cache[cache_key] = translation
    return translation


def translate_file(en_file: Path):
    """Перевод одного файла"""
    relative_path = en_file.relative_to(EN_DIR)
    ru_file = RU_DIR / relative_path

    print(f"\n📄 {relative_path}")

    if ru_file.exists():
        en_mtime = en_file.stat().st_mtime
        ru_mtime = ru_file.stat().st_mtime
        if ru_mtime > en_mtime:
            print(f"  ✓ Уже переведен (пропуск)")
            return

    try:
        with open(en_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Ошибка чтения: {e}")
        return

    if len(content) > MAX_CHUNK_CHARS:
        print(f"  📏 Большой файл ({len(content)} символов) — разбиваю на части...")
        chunks = split_into_chunks(content)
        translated_parts = []
        for ci, chunk in enumerate(chunks, 1):
            print(f"  📦 Часть {ci}/{len(chunks)}...")
            result = translate_text(chunk, f"{relative_path}#chunk{ci}")
            if result is None:
                print(f"  ⚠️  Не удалось перевести часть {ci} — пропускаю файл")
                return
            translated_parts.append(result)
        translated = '\n\n'.join(translated_parts)
    else:
        translated = translate_text(content, str(relative_path))
        if translated is None:
            return

    try:
        ru_file.parent.mkdir(parents=True, exist_ok=True)
        with open(ru_file, 'w', encoding='utf-8') as f:
            f.write(translated)
        print(f"  ✅ Сохранено!")
    except Exception as e:
        print(f"  ❌ Ошибка записи: {e}")


def main():
    print("=" * 70)
    print("🌐 ПЕРЕВОД ДОКУМЕНТАЦИИ DYNATRACE")
    print("=" * 70)

    # Статус ключей
    if GEMINI_API_KEY:
        print("✅ Gemini Flash — АКТИВЕН (основной, 1500 req/day)")
    else:
        print("⚠️  GEMINI_API_KEY не задан — Gemini пропускается")

    if GROQ_API_KEY:
        print("✅ Groq Llama 3.3 70B — АКТИВЕН (fallback 1, 100K tokens/day)")
    else:
        print("⚠️  GROQ_API_KEY не задан — Groq пропускается")

    if OPENROUTER_API_KEY:
        print("✅ OpenRouter (Llama 3.3 free) — АКТИВЕН (fallback 2)")
    else:
        print("⚠️  OPENROUTER_API_KEY не задан — OpenRouter пропускается")

    if not GEMINI_API_KEY and not GROQ_API_KEY and not OPENROUTER_API_KEY:
        print("\n❌ Ни один API ключ не задан! Перевод невозможен.")
        print("   GEMINI_API_KEY    → https://aistudio.google.com/apikey")
        print("   GROQ_API_KEY      → https://console.groq.com")
        print("   OPENROUTER_API_KEY → https://openrouter.ai/keys")
        return

    print("=" * 70)
    print()

    if not EN_DIR.exists():
        print(f"❌ Директория не найдена: {EN_DIR}")
        return

    en_files = list(EN_DIR.rglob('*.md'))
    if not en_files:
        print(f"❌ Нет файлов для перевода в {EN_DIR}")
        return

    print(f"📚 Найдено файлов: {len(en_files)}")
    print()

    translated = 0
    skipped = 0
    errors = 0
    start_time = time.time()

    for i, en_file in enumerate(en_files, 1):
        print(f"[{i}/{len(en_files)}]", end=" ")
        try:
            before_skipped = skipped
            translate_file(en_file)
            translated += 1
        except KeyboardInterrupt:
            print("\n\n⚠️  Прервано пользователем")
            break
        except Exception as e:
            print(f"  ❌ Ошибка: {e}")
            errors += 1

        if i % 10 == 0:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)

    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print("📊 ГОТОВО")
    print("=" * 70)
    print(f"✅ Обработано: {translated}")
    print(f"❌ Ошибок:    {errors}")
    print(f"⏱️  Время:     {int(elapsed//60)}м {int(elapsed%60)}с")
    print()

    # Автоматически обновляем nav в mkdocs.yml
    try:
        import subprocess
        update_nav_script = Path(__file__).parent / 'update_nav.py'
        if update_nav_script.exists():
            print("🔄 Обновляю nav в mkdocs.yml...")
            result = subprocess.run(
                [sys.executable, str(update_nav_script)],
                capture_output=True, text=True, encoding='utf-8'
            )
            if result.returncode == 0:
                print("✅ Nav обновлён!")
            else:
                print(f"⚠️  Nav не обновлён: {result.stderr[:200]}")
    except Exception as e:
        print(f"⚠️  Ошибка обновления nav: {e}")


if __name__ == '__main__':
    main()
