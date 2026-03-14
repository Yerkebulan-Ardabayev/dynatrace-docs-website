#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parallel title translation for /docs/ru/ frontmatter.
Splits work by top-level section, runs N workers in parallel.
Each worker uses a dedicated Gemini API key (if available) to maximise throughput.
Falls back to Groq → OpenRouter when Gemini is exhausted.
"""

import os
import sys
import io
import re
import json
import time
import hashlib
import threading
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# ── Windows console encoding ──────────────────────────────────────────────────
if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# ── Load .env ─────────────────────────────────────────────────────────────────
def _load_dotenv():
    for env_path in [
        Path(__file__).parent.parent / '.env',
        Path(__file__).parent / '.env',
        Path('.env'),
    ]:
        if env_path.exists():
            with open(env_path, encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        k, _, v = line.partition('=')
                        k = k.strip(); v = v.strip().strip('"').strip("'")
                        if k and k not in os.environ:
                            os.environ[k] = v
            break

_load_dotenv()

# ── API keys ──────────────────────────────────────────────────────────────────
GROQ_API_KEY       = os.environ.get('GROQ_API_KEY', '')
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')
GEMINI_API_KEYS    = [v for k, v in sorted(os.environ.items())
                      if k.startswith('GEMINI_API_KEY') and v]

GROQ_URL        = 'https://api.groq.com/openai/v1/chat/completions'
GEMINI_URL      = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
OPENROUTER_URL  = 'https://openrouter.ai/api/v1/chat/completions'
OPENROUTER_MODELS = [
    'google/gemma-3-27b-it:free',
    'meta-llama/llama-3.3-70b-instruct:free',
    'microsoft/phi-4-reasoning-plus:free',
    'qwen/qwen3-8b:free',
]

# ── Paths ─────────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).parent.parent
RU_DIR       = PROJECT_ROOT / 'docs' / 'ru'
CACHE_FILE   = PROJECT_ROOT / '.translation_titles_cache.json'
LOG_FILE     = PROJECT_ROOT / 'translation_titles.log'

# ── Thread-safe cache ─────────────────────────────────────────────────────────
_cache_lock = threading.Lock()
cache: dict = {}
if CACHE_FILE.exists():
    try:
        with open(CACHE_FILE, encoding='utf-8') as f:
            cache = json.load(f)
    except Exception:
        cache = {}

def save_cache():
    with _cache_lock:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)

# ── Groq rate-limiter (one shared token bucket) ───────────────────────────────
_groq_lock = threading.Lock()
_groq_last  = 0.0
GROQ_INTERVAL = 2.2   # ~27 req/min safely

def _groq_wait():
    global _groq_last
    with _groq_lock:
        now = time.time()
        gap = GROQ_INTERVAL - (now - _groq_last)
        if gap > 0:
            time.sleep(gap)
        _groq_last = time.time()

# ── Log file (append, thread-safe) ───────────────────────────────────────────
_log_lock = threading.Lock()
_log_fh   = None

def log_write(line: str):
    with _log_lock:
        if _log_fh:
            _log_fh.write(line + '\n')
            _log_fh.flush()

# ── Protected terms ───────────────────────────────────────────────────────────
PROTECTED_TERMS = [
    'Cluster Management Console', 'Real User Monitoring',
    'Synthetic Monitoring', 'Session Replay', 'Service Flow',
    'Management Zone', 'Mission Control', 'Host Group', 'Host Unit',
    'OneAgent', 'ActiveGate', 'Smartscape', 'PurePath', 'Davis AI',
    'AppEngine', 'Dynatrace', 'Extensions', 'Environment',
    'Grail', 'DQL', 'CMC', 'Hub',
    'Kubernetes', 'OpenShift', 'Docker', 'Ansible', 'Helm',
    'REST API', 'gRPC', 'AWS', 'Azure', 'GCP',
    'API', 'SDK', 'JSON', 'YAML', 'XML',
    'GitHub', 'GitLab', 'Terraform', 'Prometheus', 'OpenTelemetry',
    'Linux', 'Windows', 'macOS',
    'PagerDuty', 'ServiceNow', 'Jira', 'Slack',
    'Monaco', 'Ansible', 'Chef', 'Puppet',
]

def protect_terms(text: str) -> tuple:
    mapping = {}
    counter = 0
    for term in PROTECTED_TERMS:
        if re.search(re.escape(term), text, re.IGNORECASE):
            placeholder = f'__KEEP{counter:03d}__'
            mapping[placeholder] = re.search(re.escape(term), text, re.IGNORECASE).group(0)
            text = re.sub(re.escape(term), placeholder, text, flags=re.IGNORECASE)
            counter += 1
    return text, mapping

def restore_terms(text: str, mapping: dict) -> str:
    for ph, term in mapping.items():
        text = text.replace(ph, term)
    return text

POST_FIXES = {
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

def post_fix(text: str) -> str:
    for wrong, correct in POST_FIXES.items():
        text = text.replace(wrong, correct)
    return text

# ── Translation prompt ────────────────────────────────────────────────────────
PROMPT = """\
Translate the following Dynatrace documentation page title from English to Russian.

Rules:
- Translate ONLY descriptive words; keep product/brand/technology names exactly as-is.
- Placeholders like __KEEP000__, __KEEP001__ must NOT be translated — leave exactly as-is.
- Do NOT add quotes or extra punctuation.
- Return ONLY the translated title, nothing else.

Common patterns:
  "Configure X"            → "Настройка X"
  "X monitoring"           → "Мониторинг X"
  "Getting started with X" → "Начало работы с X"
  "X overview"             → "Обзор X"
  "Install X"              → "Установка X"
  "Troubleshoot X"         → "Устранение неполадок X"
  "Manage X"               → "Управление X"
  "Set up X"               → "Настройка X"
  "Enable X"               → "Включение X"
  "X reference"            → "Справочник X"
  "Analyze X"              → "Анализ X"
  "Create X"               → "Создание X"
  "What's new in X"        → "Что нового в X"
  "X integration"          → "Интеграция X"
  "X deployment"           → "Развертывание X"
  "X release notes"        → "Примечания к выпуску X"
  "X requirements"         → "Требования X"
  "X tutorial"             → "Руководство X"

Title to translate:
{title}"""

# ── API callers ───────────────────────────────────────────────────────────────

def call_gemini(title_protected: str, api_key: str) -> str | None:
    if not api_key:
        return None
    prompt = PROMPT.format(title=title_protected)
    for attempt in range(4):
        try:
            resp = requests.post(
                f"{GEMINI_URL}?key={api_key}",
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
                    return None  # key exhausted
                wait = 20 * (attempt + 1)
                time.sleep(wait)
                continue
            if resp.status_code in (401, 403):
                return None
            if resp.status_code != 200:
                if attempt < 3:
                    time.sleep(2 ** attempt)
                    continue
                return None
            data = resp.json()
            candidates = data.get('candidates', [])
            if not candidates:
                return None
            text = candidates[0]['content']['parts'][0]['text'].strip()
            text = text.strip('"').strip("'")
            time.sleep(4.2)  # ~14 req/min per key
            return text
        except requests.Timeout:
            time.sleep(5)
        except Exception:
            break
    return None


def call_groq(title_protected: str) -> str | None:
    if not GROQ_API_KEY:
        return None
    _groq_wait()
    prompt = PROMPT.format(title=title_protected)
    for attempt in range(4):
        try:
            resp = requests.post(
                GROQ_URL,
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
                wait = int(retry_after) if retry_after.isdigit() else min(15 * (attempt + 1), 60)
                if wait > 90:
                    return None
                time.sleep(wait)
                continue
            if resp.status_code != 200:
                if attempt < 3:
                    time.sleep(2 ** attempt)
                    continue
                return None
            text = resp.json()['choices'][0]['message']['content'].strip()
            text = text.strip('"').strip("'")
            return text
        except requests.Timeout:
            time.sleep(4)
        except Exception:
            break
    return None


def call_openrouter(title_protected: str) -> str | None:
    if not OPENROUTER_API_KEY:
        return None
    prompt = PROMPT.format(title=title_protected)
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
                    OPENROUTER_URL, headers=headers,
                    json={
                        'model': model,
                        'messages': [{'role': 'user', 'content': prompt}],
                        'temperature': 0.2,
                        'max_tokens': 200,
                    },
                    timeout=30,
                )
                if resp.status_code == 429:
                    time.sleep(min(15 * (attempt + 1), 45))
                    continue
                if resp.status_code != 200:
                    break
                result = resp.json()
                if 'choices' not in result or not result['choices']:
                    break
                text = result['choices'][0]['message']['content'].strip()
                text = text.strip('"').strip("'")
                time.sleep(2.0)
                return text
            except requests.Timeout:
                time.sleep(5)
            except Exception:
                break
    return None

# ── Main translation logic ────────────────────────────────────────────────────

def translate_title(title: str, gemini_key: str = '') -> str | None:
    """Translate a single title. Uses cache. gemini_key is per-worker."""
    cache_key = hashlib.md5(title.encode('utf-8')).hexdigest()
    with _cache_lock:
        if cache_key in cache:
            return cache[cache_key]

    protected, mapping = protect_terms(title)

    translation = None
    if gemini_key:
        translation = call_gemini(protected, gemini_key)
    if translation is None and GROQ_API_KEY:
        translation = call_groq(protected)
    if translation is None and OPENROUTER_API_KEY:
        translation = call_openrouter(protected)

    if translation is None:
        return None

    translation = restore_terms(translation, mapping)
    translation = post_fix(translation)
    if not translation.strip():
        return None

    with _cache_lock:
        cache[cache_key] = translation
    return translation


def needs_translation(title: str) -> bool:
    return not bool(re.search(r'[а-яёА-ЯЁ]', title))


def parse_frontmatter_title(content: str):
    """Returns (title, abs_start, abs_end) or (None, -1, -1)."""
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return None, -1, -1
    fm_content = fm_match.group(1)
    title_match = re.search(r'^(title:\s*)(.+)$', fm_content, re.MULTILINE)
    if not title_match:
        return None, -1, -1
    raw = title_match.group(2).strip()
    title = raw.strip('"').strip("'")
    fm_content_start = content.index(fm_match.group(1))
    abs_start = fm_content_start + title_match.start(2)
    abs_end   = fm_content_start + title_match.end(2)
    return title, abs_start, abs_end


def process_file(filepath: Path, gemini_key: str) -> str:
    """Process one file. Returns 'ok', 'skip', or 'error'."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return f'error:read:{e}'

    title, abs_start, abs_end = parse_frontmatter_title(content)
    if title is None:
        return 'skip:no_title'
    if not needs_translation(title):
        return 'skip:already_ru'

    translated = translate_title(title, gemini_key)
    if translated is None:
        return 'skip:api_fail'

    # Sanity: must contain Cyrillic unless fully protected
    if not re.search(r'[а-яёА-ЯЁ]', translated):
        if translated.strip() == title.strip():
            return 'skip:protected'
        return 'skip:no_cyrillic'

    new_content = content[:abs_start] + translated + content[abs_end:]
    try:
        filepath.write_text(new_content, encoding='utf-8')
    except Exception as e:
        return f'error:write:{e}'

    rel = filepath.relative_to(PROJECT_ROOT)
    log_write(f"{rel} | {title} -> {translated}")
    return f'ok:{title} -> {translated}'


# ── Worker: processes a list of files with its own Gemini key ─────────────────

def worker(files: list, gemini_key: str, worker_id: int,
           counters: dict, counter_lock: threading.Lock):
    translated = 0
    skipped    = 0
    errors     = 0
    for i, filepath in enumerate(files):
        result = process_file(filepath, gemini_key)
        if result.startswith('ok:'):
            translated += 1
            msg = result[3:]
        elif result.startswith('error:'):
            errors += 1
            msg = f'ERROR: {result}'
        else:
            skipped += 1
            msg = None

        with counter_lock:
            counters['translated'] += (1 if result.startswith('ok:') else 0)
            counters['skipped']    += (1 if result.startswith('skip:') else 0)
            counters['errors']     += (1 if result.startswith('error:') else 0)
            done = counters['translated'] + counters['skipped'] + counters['errors']
            total = counters['total']
            if msg or (i % 20 == 0):
                pct = done * 100 // total if total else 0
                status = f"[W{worker_id}] [{done}/{total} {pct}%]"
                if msg:
                    print(f"{status} {msg}", flush=True)
                else:
                    print(f"{status} (progress)", flush=True)

        # Save cache every 25 files per worker
        if (i + 1) % 25 == 0:
            save_cache()

    return translated, skipped, errors


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    global _log_fh

    print("=" * 70)
    print("PARALLEL TITLE TRANSLATION — /docs/ru/")
    print("=" * 70)

    # Show API status
    key_info = []
    for i, k in enumerate(GEMINI_API_KEYS):
        key_info.append(f"GEMINI_{i}")
    print(f"  Gemini keys : {len(GEMINI_API_KEYS)} ({', '.join(key_info) or 'none'})")
    print(f"  Groq        : {'ACTIVE' if GROQ_API_KEY else 'not set'}")
    print(f"  OpenRouter  : {'ACTIVE' if OPENROUTER_API_KEY else 'not set'}")

    if not any([GEMINI_API_KEYS, GROQ_API_KEY, OPENROUTER_API_KEY]):
        print("ERROR: No API keys. Cannot translate.")
        return

    # ── Collect files needing translation ─────────────────────────────────────
    print(f"\nScanning {RU_DIR} ...")
    all_files = sorted(RU_DIR.rglob('*.md'))
    to_translate = []
    for filepath in all_files:
        try:
            content = filepath.read_text(encoding='utf-8')
        except Exception:
            continue
        title, _, _ = parse_frontmatter_title(content)
        if title and needs_translation(title):
            to_translate.append(filepath)

    total = len(to_translate)
    print(f"Found {total} files with English titles.\n")
    if not to_translate:
        print("Nothing to do.")
        return

    # ── Split by top-level section ────────────────────────────────────────────
    sections: dict[str, list] = {}
    for f in to_translate:
        try:
            rel = f.relative_to(RU_DIR)
            section = rel.parts[0] if len(rel.parts) > 1 else '__root__'
        except Exception:
            section = '__root__'
        sections.setdefault(section, []).append(f)

    section_names = sorted(sections.keys())
    print(f"Sections ({len(section_names)}):")
    for s in section_names:
        print(f"  {s}: {len(sections[s])} files")
    print()

    # ── Assign Gemini key to each worker ──────────────────────────────────────
    # Number of workers = max(sections, available gemini keys+1) but cap at 8
    n_keys   = len(GEMINI_API_KEYS)
    n_workers = min(max(n_keys, 1), 8)
    print(f"Workers: {n_workers}")

    # Distribute files evenly across workers (sort sections by size desc, greedy bin packing)
    worker_files: list[list] = [[] for _ in range(n_workers)]
    worker_sizes = [0] * n_workers
    sorted_sections = sorted(section_names, key=lambda s: -len(sections[s]))
    for s in sorted_sections:
        # Assign to the worker with fewest files so far
        min_idx = worker_sizes.index(min(worker_sizes))
        worker_files[min_idx].extend(sections[s])
        worker_sizes[min_idx] += len(sections[s])

    # Assign gemini keys round-robin
    worker_keys = []
    for i in range(n_workers):
        key = GEMINI_API_KEYS[i % n_keys] if n_keys else ''
        worker_keys.append(key)

    # ── Shared counters ───────────────────────────────────────────────────────
    counters = {'translated': 0, 'skipped': 0, 'errors': 0, 'total': total}
    counter_lock = threading.Lock()

    # ── Open log file ─────────────────────────────────────────────────────────
    _log_fh = open(LOG_FILE, 'a', encoding='utf-8')
    log_write(f"\n{'='*70}")
    log_write(f"Parallel run started. Files: {total} | Workers: {n_workers}")
    log_write('='*70)

    start = time.time()

    # ── Run workers in parallel ───────────────────────────────────────────────
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = []
        for wid in range(n_workers):
            if not worker_files[wid]:
                continue
            fut = executor.submit(
                worker,
                worker_files[wid],
                worker_keys[wid],
                wid + 1,
                counters,
                counter_lock,
            )
            futures.append(fut)

        results = [f.result() for f in as_completed(futures)]

    # ── Final save & report ───────────────────────────────────────────────────
    save_cache()
    _log_fh.close()

    elapsed = time.time() - start
    total_translated = sum(r[0] for r in results)
    total_skipped    = sum(r[1] for r in results)
    total_errors     = sum(r[2] for r in results)

    print()
    print("=" * 70)
    print("DONE")
    print("=" * 70)
    print(f"  Translated : {total_translated}")
    print(f"  Skipped    : {total_skipped}")
    print(f"  Errors     : {total_errors}")
    print(f"  Elapsed    : {int(elapsed//60)}m {int(elapsed%60)}s")
    print(f"  Log        : {LOG_FILE}")
    print(f"  Cache      : {CACHE_FILE}")


if __name__ == '__main__':
    main()
