#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate English title: fields in /docs/ru/ YAML frontmatter to Russian.
Uses Groq API (primary) with Gemini and OpenRouter as fallbacks.
"""

import os
import sys
import io
import re
import json
import time
import hashlib
import requests
from pathlib import Path

# Fix Windows console encoding
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

# ─── Load .env ───────────────────────────────────────────────────────────────
def _load_dotenv():
    env_paths = [
        Path(__file__).parent.parent / '.env',
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

GROQ_API_KEY       = os.environ.get('GROQ_API_KEY', '')
GEMINI_API_KEYS    = [v for k, v in os.environ.items() if k.startswith('GEMINI_API_KEY') and v]
GEMINI_API_KEY     = GEMINI_API_KEYS[0] if GEMINI_API_KEYS else ''
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')

GROQ_API_URL       = 'https://api.groq.com/openai/v1/chat/completions'
GEMINI_API_URL     = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'
OPENROUTER_MODELS  = [
    'google/gemma-3-27b-it:free',
    'meta-llama/llama-3.3-70b-instruct:free',
    'microsoft/phi-4-reasoning-plus:free',
    'qwen/qwen3-8b:free',
]

# ─── Paths ────────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).parent.parent
RU_DIR       = PROJECT_ROOT / 'docs' / 'ru'
CACHE_FILE   = PROJECT_ROOT / '.translation_titles_cache.json'
LOG_FILE     = PROJECT_ROOT / 'translation_titles.log'

# ─── Cache ────────────────────────────────────────────────────────────────────
cache: dict = {}
if CACHE_FILE.exists():
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            cache = json.load(f)
    except Exception:
        cache = {}

def save_cache():
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

# ─── Protected terms (brand names, tech terms) ───────────────────────────────
PROTECTED_TERMS = [
    # Dynatrace products — longest first
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
    # Other tech
    'GitHub', 'GitLab', 'Terraform', 'Prometheus', 'OpenTelemetry',
    'Linux', 'Windows', 'macOS',
]

def protect_terms(text: str) -> tuple:
    mapping = {}
    counter = 0
    for term in PROTECTED_TERMS:
        pattern = re.compile(re.escape(term))
        if pattern.search(text):
            placeholder = f'__KEEP{counter:03d}__'
            mapping[placeholder] = term
            text = pattern.sub(placeholder, text)
            counter += 1
    return text, mapping

def restore_terms(text: str, mapping: dict) -> str:
    for placeholder, term in mapping.items():
        text = text.replace(placeholder, term)
    return text

def post_fix_errors(text: str) -> str:
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

# ─── Translation prompt ───────────────────────────────────────────────────────
TITLE_PROMPT = """\
Translate the following Dynatrace documentation page title from English to Russian.

Rules:
- Translate ONLY the descriptive words; keep product/brand/technology names exactly as-is.
- Words like __KEEP000__, __KEEP001__, etc. are placeholders — do NOT translate them, leave exactly as-is.
- Do NOT add quotes or extra punctuation.
- Return ONLY the translated title, nothing else — no comments, no "Here is the translation:", just the title.

Common translation patterns (use them):
  "Configure X"           → "Настройка X"
  "How to configure X"    → "Как настроить X"
  "X monitoring"          → "Мониторинг X"
  "Getting started with X"→ "Начало работы с X"
  "X overview"            → "Обзор X"
  "Install X"             → "Установка X"
  "Troubleshoot X"        → "Устранение неполадок X"
  "Manage X"              → "Управление X"
  "Set up X"              → "Настройка X"
  "Enable X"              → "Включение X"
  "X reference"           → "Справочник X"
  "Analyze X"             → "Анализ X"
  "Create X"              → "Создание X"
  "What's new in X"       → "Что нового в X"
  "Data X"                → "Данные X"
  "X integration"         → "Интеграция X"
  "X deployment"          → "Развертывание X"

Title to translate:
{title}"""


# ─── API calls ────────────────────────────────────────────────────────────────

def call_groq(title_protected: str) -> str | None:
    if not GROQ_API_KEY:
        return None
    prompt = TITLE_PROMPT.format(title=title_protected)
    for attempt in range(6):
        try:
            resp = requests.post(
                GROQ_API_URL,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {GROQ_API_KEY}',
                },
                json={
                    'model': 'llama-3.3-70b-versatile',
                    'messages': [{'role': 'user', 'content': prompt}],
                    'temperature': 0.2,
                    'max_tokens': 200,
                    'stream': False,
                },
                timeout=30,
            )
            if resp.status_code == 429:
                retry_after = resp.headers.get('retry-after', '')
                wait = int(retry_after) if retry_after.isdigit() else min(10 * (attempt + 1), 60)
                if wait > 60:
                    print(f"    [Groq] rate limit {wait}s — switching to fallback")
                    return None
                print(f"    [Groq] rate limit, waiting {wait}s...")
                time.sleep(wait)
                continue
            if resp.status_code != 200:
                print(f"    [Groq] HTTP {resp.status_code}")
                if attempt < 5:
                    time.sleep(2 ** attempt)
                    continue
                return None
            result = resp.json()
            translation = result['choices'][0]['message']['content'].strip()
            # Remove surrounding quotes if the model added them
            translation = translation.strip('"').strip("'")
            time.sleep(2.0)  # ~30 req/min
            return translation
        except requests.Timeout:
            print(f"    [Groq] timeout, retry {attempt+1}...")
            time.sleep(4)
        except Exception as e:
            print(f"    [Groq] exception: {e}")
            if attempt < 5:
                time.sleep(2)
                continue
            return None
    return None


def call_gemini(title_protected: str) -> str | None:
    if not GEMINI_API_KEY:
        return None
    prompt = TITLE_PROMPT.format(title=title_protected)
    for api_key in GEMINI_API_KEYS:
        for attempt in range(4):
            try:
                resp = requests.post(
                    f"{GEMINI_API_URL}?key={api_key}",
                    headers={'Content-Type': 'application/json'},
                    json={
                        'contents': [{'parts': [{'text': prompt}]}],
                        'generationConfig': {'temperature': 0.2, 'maxOutputTokens': 200},
                    },
                    timeout=30,
                )
                if resp.status_code == 429:
                    err = resp.text
                    if 'limit: 0' in err or 'quota' in err.lower():
                        print(f"    [Gemini] daily quota exhausted for key, trying next...")
                        break
                    wait = 20 * (attempt + 1)
                    print(f"    [Gemini] rate limit, waiting {wait}s...")
                    time.sleep(wait)
                    continue
                if resp.status_code in (401, 403):
                    print(f"    [Gemini] auth error {resp.status_code}")
                    break
                if resp.status_code != 200:
                    print(f"    [Gemini] HTTP {resp.status_code}")
                    if attempt < 3:
                        time.sleep(2 ** attempt)
                        continue
                    break
                data = resp.json()
                candidates = data.get('candidates', [])
                if not candidates:
                    break
                translation = candidates[0]['content']['parts'][0]['text'].strip()
                translation = translation.strip('"').strip("'")
                time.sleep(4.0)  # 15 req/min
                return translation
            except requests.Timeout:
                time.sleep(5)
            except Exception as e:
                print(f"    [Gemini] exception: {e}")
                break
    return None


def call_openrouter(title_protected: str) -> str | None:
    if not OPENROUTER_API_KEY:
        return None
    prompt = TITLE_PROMPT.format(title=title_protected)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENROUTER_API_KEY}',
        'HTTP-Referer': 'https://github.com/Yerkebulan-Ardabayev/dynatrace-docs-website',
        'X-Title': 'Dynatrace Docs Title Translator',
    }
    for model in OPENROUTER_MODELS:
        for attempt in range(3):
            try:
                resp = requests.post(
                    OPENROUTER_API_URL,
                    headers=headers,
                    json={
                        'model': model,
                        'messages': [{'role': 'user', 'content': prompt}],
                        'temperature': 0.2,
                        'max_tokens': 200,
                    },
                    timeout=30,
                )
                if resp.status_code == 429:
                    wait = min(15 * (attempt + 1), 45)
                    print(f"    [OpenRouter/{model}] rate limit, waiting {wait}s...")
                    time.sleep(wait)
                    continue
                if resp.status_code != 200:
                    err = ''
                    try:
                        err = resp.json().get('error', {}).get('message', '')[:80]
                    except Exception:
                        pass
                    print(f"    [OpenRouter/{model}] HTTP {resp.status_code}: {err}")
                    break
                result = resp.json()
                if 'choices' not in result or not result['choices']:
                    break
                translation = result['choices'][0]['message']['content'].strip()
                translation = translation.strip('"').strip("'")
                time.sleep(2.0)
                return translation
            except requests.Timeout:
                print(f"    [OpenRouter/{model}] timeout")
                time.sleep(5)
            except Exception as e:
                print(f"    [OpenRouter/{model}] exception: {e}")
                break
    return None


# ─── Main translation logic ───────────────────────────────────────────────────

def translate_title(title: str) -> str | None:
    """Translate a single title string to Russian. Uses cache."""
    cache_key = hashlib.md5(title.encode('utf-8')).hexdigest()
    if cache_key in cache:
        return cache[cache_key]

    # Protect brand terms
    protected, mapping = protect_terms(title)

    translation = None

    # Try Groq first (as primary per task request)
    if GROQ_API_KEY:
        translation = call_groq(protected)

    # Fallback: Gemini
    if translation is None and GEMINI_API_KEY:
        print(f"    Falling back to Gemini...")
        translation = call_gemini(protected)

    # Fallback: OpenRouter
    if translation is None and OPENROUTER_API_KEY:
        print(f"    Falling back to OpenRouter...")
        translation = call_openrouter(protected)

    if translation is None:
        return None

    # Restore brand terms
    translation = restore_terms(translation, mapping)
    translation = post_fix_errors(translation)

    # Sanity check: result should have some content
    if not translation.strip():
        return None

    cache[cache_key] = translation
    return translation


def needs_translation(title: str) -> bool:
    """Return True if title has no Cyrillic characters (is still in English)."""
    return not bool(re.search(r'[а-яёА-ЯЁ]', title))


def parse_frontmatter_title(content: str) -> tuple:
    """
    Returns (title, start_pos, end_pos) of the title value in the frontmatter,
    or (None, -1, -1) if not found.
    start_pos/end_pos are character positions for the VALUE part of 'title: <value>'.
    """
    # Match YAML frontmatter block
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return None, -1, -1

    fm_block = fm_match.group(0)
    fm_content = fm_match.group(1)

    # Find title line within frontmatter
    title_match = re.search(r'^(title:\s*)(.+)$', fm_content, re.MULTILINE)
    if not title_match:
        return None, -1, -1

    raw_title = title_match.group(2).strip()
    # Strip surrounding quotes if present
    title = raw_title.strip('"').strip("'")

    # Calculate absolute positions in the full content string
    # Position of the frontmatter group(1) start in content
    fm_content_start = content.index(fm_match.group(1))
    # Position of title value within fm_content
    title_val_start_in_fm = title_match.start(2)
    title_val_end_in_fm   = title_match.end(2)

    abs_start = fm_content_start + title_val_start_in_fm
    abs_end   = fm_content_start + title_val_end_in_fm

    return title, abs_start, abs_end


def process_file(filepath: Path, log_fh) -> bool:
    """Process a single file. Returns True if title was updated."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"    ERROR reading: {e}")
        return False

    title, abs_start, abs_end = parse_frontmatter_title(content)

    if title is None:
        return False

    if not needs_translation(title):
        return False

    # Translate
    translated = translate_title(title)
    if translated is None:
        print(f"    SKIPPED (API unavailable)")
        return False

    # Verify translation actually contains Cyrillic (sanity check)
    if not re.search(r'[а-яёА-ЯЁ]', translated):
        # Might be a pure product name like "Dynatrace API" - that's okay, keep it
        # but only if it's the same as original (fully protected)
        if translated.strip() == title.strip():
            # Fully protected term — write it as-is (no change needed)
            return False
        # Otherwise something went wrong; skip
        print(f"    SKIPPED (translation has no Cyrillic: '{translated}')")
        return False

    # Replace title value in content
    new_content = content[:abs_start] + translated + content[abs_end:]

    try:
        filepath.write_text(new_content, encoding='utf-8')
    except Exception as e:
        print(f"    ERROR writing: {e}")
        return False

    log_line = f"{filepath.relative_to(PROJECT_ROOT)} | {title} -> {translated}\n"
    log_fh.write(log_line)
    log_fh.flush()

    return True


def main():
    print("=" * 70)
    print("TRANSLATING TITLES in /docs/ru/")
    print("=" * 70)

    # Show API status
    if GROQ_API_KEY:
        print("  Groq Llama 3.3 70B  — ACTIVE (primary)")
    else:
        print("  GROQ_API_KEY not set — Groq skipped")
    if GEMINI_API_KEY:
        print(f"  Gemini Flash ({len(GEMINI_API_KEYS)} key(s)) — ACTIVE (fallback 1)")
    else:
        print("  GEMINI_API_KEY not set — Gemini skipped")
    if OPENROUTER_API_KEY:
        print("  OpenRouter free     — ACTIVE (fallback 2)")
    else:
        print("  OPENROUTER_API_KEY not set — OpenRouter skipped")

    if not any([GROQ_API_KEY, GEMINI_API_KEY, OPENROUTER_API_KEY]):
        print("\nERROR: No API keys available. Cannot translate.")
        return

    print("=" * 70)

    if not RU_DIR.exists():
        print(f"ERROR: {RU_DIR} does not exist")
        return

    # Collect all .md files
    all_files = sorted(RU_DIR.rglob('*.md'))
    print(f"\nScanning {len(all_files)} .md files in /docs/ru/ ...")

    # Filter to those needing translation
    to_translate = []
    for filepath in all_files:
        try:
            content = filepath.read_text(encoding='utf-8')
        except Exception:
            continue
        title, _, _ = parse_frontmatter_title(content)
        if title and needs_translation(title):
            to_translate.append(filepath)

    print(f"Found {len(to_translate)} files with English titles to translate.\n")

    if not to_translate:
        print("Nothing to do.")
        return

    translated_count = 0
    skipped_count    = 0
    error_count      = 0

    start_time = time.time()

    with open(LOG_FILE, 'w', encoding='utf-8') as log_fh:
        log_fh.write(f"Translation run started. Files to process: {len(to_translate)}\n")
        log_fh.write("=" * 70 + "\n")

        for idx, filepath in enumerate(to_translate, 1):
            # Read current title for display
            try:
                content = filepath.read_text(encoding='utf-8')
                title, _, _ = parse_frontmatter_title(content)
            except Exception:
                title = '(unreadable)'

            rel = filepath.relative_to(PROJECT_ROOT)
            print(f"[{idx}/{len(to_translate)}] {rel}")
            print(f"  Title: {title}")

            success = process_file(filepath, log_fh)
            if success:
                translated_count += 1
                # Print the new title
                try:
                    new_content = filepath.read_text(encoding='utf-8')
                    new_title, _, _ = parse_frontmatter_title(new_content)
                    print(f"  -> {new_title}")
                except Exception:
                    pass
            else:
                skipped_count += 1

            # Save cache every 20 files
            if idx % 20 == 0:
                save_cache()
                elapsed = time.time() - start_time
                rate = idx / elapsed if elapsed > 0 else 0
                remaining = (len(to_translate) - idx) / rate if rate > 0 else 0
                print(f"\n--- Progress: {idx}/{len(to_translate)} | "
                      f"Translated: {translated_count} | "
                      f"ETA: {int(remaining//60)}m {int(remaining%60)}s ---\n")

    # Final cache save
    save_cache()

    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print("DONE")
    print("=" * 70)
    print(f"  Translated: {translated_count}")
    print(f"  Skipped:    {skipped_count}")
    print(f"  Elapsed:    {int(elapsed//60)}m {int(elapsed%60)}s")
    print(f"  Log file:   {LOG_FILE}")
    print(f"  Cache file: {CACHE_FILE}")


if __name__ == '__main__':
    main()
