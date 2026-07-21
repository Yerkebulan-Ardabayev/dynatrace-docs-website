#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate only changed articles detected by detect_changes.py.

Reads changes_report.json and translates new/updated articles.
Uses the same translation engine as translate_docs_groq.py.

Usage:
    python scripts/translate_changed.py \
        --report changes_report.json \
        --max-articles 50
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

# Import translation functions from existing script
sys.path.insert(0, str(Path(__file__).parent))
from translate_docs_groq import (
    translate_text, split_into_chunks, post_fix_known_errors,
    cache, CACHE_FILE, MAX_CHUNK_CHARS,
    claude_available, CLAUDE_MODEL,
    GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY,
)
# Реестр хэшей ведём здесь: запись «RU сделан от этого EN» имеет право появиться
# только после успешного перевода (см. комментарий в detect_changes.py).
from detect_changes import file_hash, load_hash_registry, save_hash_registry

# Канонический корпус — Dynatrace MANAGED. Пишем перевод ТОЛЬКО в docs/managed-ru
# и только для реально изменившихся файлов, с гейтом _validate_translation ПЕРЕД
# записью (см. translate_single_file), чтобы не затереть готовые 2698 файлов.
BASE_DIR = Path(__file__).parent.parent
EN_DIR = BASE_DIR / "docs" / "managed"
RU_DIR = BASE_DIR / "docs" / "managed-ru"


# Английские преамбулы, которыми LLM иногда предваряет перевод вместо чистого текста.
_EN_PREAMBLE = (
    "sure", "here is", "here's", "certainly", "of course", "okay", "ok,",
    "translation:", "translated text", "i'll translate", "i will translate",
    "below is",
)


def _strip_code(text: str) -> str:
    """Текст без блоков и inline-кода: там скобки и ссылки не наши."""
    return re.sub(r"`[^`\n]*`", "", re.sub(r"```.*?```", "", text, flags=re.DOTALL))


# Скрейпер сеет невидимый ﻿ внутри ссылок (`[текст﻿](url)`). Модель его
# иногда не переносит, на вёрстку это не влияет, поэтому при сверке структуры
# просто выкидываем такие символы с обеих сторон.
_INVISIBLE = re.compile(r"[﻿​‎‏]")

# Класс URL закрыт скобками намеренно: без этого `[url﻿](url)` из корпуса
# читался как ОДИН адрес вместе с `](`, и любое расхождение в невидимом символе
# выглядело как потерянная ссылка.
_URL_RE = re.compile(r"https?://[^\s\[\]()<>\"']+")


def _normalize_dashes(source: str, translated: str) -> str:
    """Убирает длинные тире из перевода, не трогая код.

    Правило проекта: длинных тире в тексте нет. Модель ставит их сама даже там,
    где в оригинале обычный дефис (12 штук в статье при 0 в оригинале), и на
    повторные попытки с подсказкой не реагирует, поэтому чиним детерминированно,
    а не уговорами. Если оригинал разделяет дефисом, ставим дефис (так вернее),
    иначе запятую, а после жирного лейбла двоеточие.
    """
    if "—" not in translated:
        return translated

    def fix(seg: str) -> str:
        if " - " in source:
            seg = seg.replace(" — ", " - ")
        seg = re.sub(r"(\*\*|`)\s+—\s+", r"\1: ", seg)
        seg = seg.replace(" — это ", ", это ")
        seg = seg.replace(" — ", ", ")
        return seg.replace("—", "-")

    parts = re.split(r"(```.*?```|`[^`\n]*`)", translated, flags=re.DOTALL)
    parts[::2] = [fix(p) for p in parts[::2]]
    return "".join(parts)


def _structure_defect(source: str, translated: str) -> str:
    """Структурные расхождения перевода с оригиналом. Пусто, если всё сошлось.

    Ловит то, что модель роняет на длинных статьях: съеденную скобку ссылки
    (`Перейти в **X**](url)` вместо `[**X**](url)` — ссылка рендерится как текст),
    потерянный фенс кода, пропавший URL. Проверка стоит ДО записи в корпус:
    иначе битый перевод затирает готовый файл, а батч встаёт на гейте целиком.
    """
    src = _INVISIBLE.sub("", _strip_code(source))
    dst = _INVISIBLE.sub("", _strip_code(translated))

    if (src.count("[") - src.count("]")) != (dst.count("[") - dst.count("]")):
        return "баланс квадратных скобок разошёлся с оригиналом (сломана ссылка)"
    if source.count("```") != translated.count("```"):
        return f"фенсы кода: было {source.count('```')}, стало {translated.count('```')}"

    lost = sorted(set(_URL_RE.findall(src)) - set(_URL_RE.findall(dst)))
    if lost:
        return f"потеряны URL ({len(lost)}), первый: {lost[0][:60]}"

    # Длинные тире в русском тексте запрещены (правило оформления проекта).
    # Промпт про это говорит, но модель изредка их всё равно ставит: за день
    # просочилось 54 штуки в 12 статей, и заметил это человек, а не проверка.
    # В коде тире законно, поэтому смотрим текст без код-блоков.
    dashes = dst.count("—")
    if dashes:
        return f"длинные тире в переводе ({dashes} шт.), заменяются запятой или двоеточием"

    # Заголовки строго 1:1, включая повторы. Скрейпер дублирует H1 почти во всех
    # статьях (2881 файл), и корпус этот повтор сохраняет (2746 из 2762), а модель
    # иногда «прибирается» и схлопывает два заголовка в один.
    h_src = len(re.findall(r"^#{1,6} ", src, re.M))
    h_dst = len(re.findall(r"^#{1,6} ", dst, re.M))
    if h_src != h_dst:
        return f"заголовков было {h_src}, стало {h_dst}"
    return ""


def _validate_translation(source: str, translated: str) -> tuple[bool, str]:
    """Гейт ПЕРЕД записью в корпус (HIGH аудита): не пустой, есть кириллица, не
    короче 25% оригинала (ловит усечение), не начинается с англ-преамбулы LLM.
    Возвращает (ok, причина). Плохой перевод НЕ должен затирать готовый файл.
    """
    if not translated or not translated.strip():
        return False, "пустой перевод"
    t = translated.strip()
    if not re.search(r"[а-яА-ЯёЁ]", t):
        return False, "нет кириллицы (похоже, не переведено)"
    if len(t) < 0.25 * len(source):
        return False, f"слишком коротко ({len(t)} vs {len(source)} симв., возможна обрезка)"
    head = t.lstrip("#*_> \n").lower()[:40]
    if any(head.startswith(p) for p in _EN_PREAMBLE):
        return False, "начинается с английской преамбулы LLM"
    return True, "ok"


_ZONE_HEADING_NORM: dict | None = None


def zone_heading_norm() -> dict:
    """Доля русских H1 по разделам уже переведённого корпуса.

    Норма НЕ единая: в `deliver` и `dynatrace-api` заголовки исторически
    остаются английскими (0% и 16% русских H1), в `analyze-explore-automate`
    и `manage` переводятся почти всегда (99% и 97%). Поэтому правило берём из
    самого корпуса, а не из общих соображений, иначе свежий перевод начнёт
    расходиться с сотнями готовых соседей.
    """
    global _ZONE_HEADING_NORM
    if _ZONE_HEADING_NORM is None:
        stats: dict[str, list[int]] = {}
        for f in RU_DIR.rglob("*.md"):
            m = re.search(r"^# (.+)$", f.read_text(encoding="utf-8", errors="replace"), re.M)
            if not m:
                continue
            zone = f.relative_to(RU_DIR).parts[0]
            pair = stats.setdefault(zone, [0, 0])
            pair[0 if re.search(r"[а-яё]", m.group(1), re.I) else 1] += 1
        _ZONE_HEADING_NORM = {
            z: ru / (ru + en) for z, (ru, en) in stats.items() if (ru + en) >= 5
        }
    return _ZONE_HEADING_NORM


def heading_rule_for(rel_path: str) -> str:
    """Правило по заголовкам для конкретной статьи (пусто, если норма размыта)."""
    zone = Path(rel_path).parts[0]
    share = zone_heading_norm().get(zone)
    if share is None:
        return ""
    if share >= 0.7:
        return ("Заголовок H1 и поле title во frontmatter переводи на русский "
                "(в этом разделе так сделано в большинстве готовых статей).")
    if share <= 0.3:
        return ("Заголовок H1 и поле title во frontmatter оставь английскими, "
                "как в оригинале (в этом разделе так сделано во всех готовых статьях). "
                "Текст статьи при этом переводится полностью.")
    return ""


_RETRY_HINT = (
    "\n\nПРЕДЫДУЩАЯ ПОПЫТКА СЛОМАЛА РАЗМЕТКУ. Особое внимание синтаксису ссылок: "
    "у каждой ссылки обязаны быть обе скобки, `[текст](url)`, открывающую `[` "
    "терять нельзя. Число блоков кода и все URL сохраняются без изменений."
)


def _translate_whole(content: str, en_file: Path, extra_rules: str,
                     retry_hint: str = "") -> str | None:
    """Перевод файла целиком, при необходимости по чанкам.

    retry_hint идёт в КАЖДЫЙ чанк, а не только в первый. Он входит в ключ кеша,
    поэтому иначе повтор вытаскивал из кеша тот же битый чанк: скобку роняет
    обычно не первый чанк, а середина статьи.
    """
    if len(content) <= MAX_CHUNK_CHARS:
        return translate_text(content, str(en_file.name), extra_rules + retry_hint)

    chunks = split_into_chunks(content)
    parts = []
    for i, chunk in enumerate(chunks, 1):
        print(f"  chunk {i}/{len(chunks)}...")
        # Правило заголовков осмысленно только для первого чанка: H1 и
        # frontmatter живут там, дальше пойдут подзаголовки тела.
        rules = (extra_rules if i == 1 else "") + retry_hint

        # Сверяем и перезапрашиваем КАЖДЫЙ чанк отдельно. Иначе один сорвавшийся
        # кусок заставлял переводить статью целиком заново, и на длинных текстах
        # это не сходилось никогда: шанс, что все девять чанков подряд выйдут
        # чистыми, мал, а стоимость попытки максимальная.
        result = None
        for attempt in (1, 2, 3):
            candidate = translate_text(
                chunk, f"{en_file.name}#chunk{i}",
                rules if attempt == 1 else rules + _RETRY_HINT,
            )
            if candidate is None:
                print(f"  FAILED chunk {i}")
                return None
            candidate = _normalize_dashes(chunk, candidate)
            defect = _structure_defect(chunk, candidate)
            if not defect:
                result = candidate
                break
            print(f"    чанк {i}: {defect}, попытка {attempt}/3")
        if result is None:
            print(f"  FAILED chunk {i}: структура не выправилась за 3 попытки")
            return None
        parts.append(result)
    return "\n\n".join(parts)


def translate_single_file(en_file: Path, ru_file: Path, extra_rules: str = "") -> bool:
    """Translate a single file. Returns True on success."""
    try:
        content = en_file.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  ERROR reading {en_file}: {e}")
        return False

    # Две попытки: модель изредка роняет скобку ссылки на длинной статье. Подсказка
    # во второй попытке заодно меняет ключ кеша, иначе вернулся бы тот же битый
    # результат. Если и она не сходится — файл пропускаем, он останется в очереди,
    # а батч продолжит работу (одна статья не должна блокировать остальные).
    translated = None
    for attempt in (1, 2):
        candidate = _translate_whole(
            content, en_file, extra_rules, "" if attempt == 1 else _RETRY_HINT
        )
        if candidate is None:
            return False
        candidate = _normalize_dashes(content, candidate)
        defect = _structure_defect(content, candidate)
        if not defect:
            translated = candidate
            break
        print(f"  структура не сошлась ({defect}), попытка {attempt}/2")
    if translated is None:
        print(f"  SKIP: {ru_file.name} не перезаписываю, статья остаётся в очереди")
        return False

    ok, reason = _validate_translation(content, translated)
    if not ok:
        print(f"  REJECT ({reason}) — не перезаписываю {ru_file.name}")
        return False

    # Атомарная запись: пишем во временный файл и заменяем цель через os.replace.
    # Обрыв посреди записи не оставит наполовину перезаписанный готовый managed-ru.
    ru_file.parent.mkdir(parents=True, exist_ok=True)
    tmp = ru_file.with_suffix(ru_file.suffix + ".tmp")
    tmp.write_text(translated, encoding="utf-8")
    os.replace(tmp, ru_file)
    return True


def main():
    parser = argparse.ArgumentParser(description="Translate changed articles")
    parser.add_argument("--report", required=True, help="Path to changes_report.json")
    parser.add_argument("--max-articles", type=int, default=50,
                        help="Max articles to translate (0 = unlimited)")
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        print(f"Report not found: {report_path}")
        sys.exit(1)

    report = json.load(open(report_path, "r", encoding="utf-8"))

    # Есть ли хоть один рабочий провайдер: подписка Claude или запасной ключ
    has_api = claude_available() or GEMINI_API_KEY or GROQ_API_KEY or OPENROUTER_API_KEY
    if not has_api:
        print("WARNING: нет ни claude CLI, ни ключей "
              "(GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY)")
        print("Translation skipped.")
        json.dump({"translated_count": 0, "skipped": "no_api_keys"},
                  open("translation_result.json", "w"))
        return

    # Collect articles to translate (new first, then updated)
    articles = report.get("new_articles", []) + report.get("updated_articles", [])
    if not articles:
        print("No articles to translate.")
        json.dump({"translated_count": 0}, open("translation_result.json", "w"))
        return

    max_articles = args.max_articles if args.max_articles > 0 else len(articles)
    articles = articles[:max_articles]

    print(f"Translating {len(articles)} articles...")
    print(f"Провайдеры: claude={CLAUDE_MODEL if claude_available() else 'OFF'}"
          f" | Gemini={'ON' if GEMINI_API_KEY else 'OFF'}"
          f" | Groq={'ON' if GROQ_API_KEY else 'OFF'}"
          f" | OpenRouter={'ON' if OPENROUTER_API_KEY else 'OFF'}")
    print()

    translated_count = 0
    failed_count = 0
    translated_files = []
    registry = load_hash_registry()
    start = time.time()

    for i, article in enumerate(articles, 1):
        rel_path = article["path"]
        en_file = EN_DIR / rel_path
        ru_file = RU_DIR / rel_path

        if not en_file.exists():
            print(f"[{i}/{len(articles)}] SKIP (not found): {rel_path}")
            continue

        print(f"[{i}/{len(articles)}] {rel_path}")

        ok = translate_single_file(en_file, ru_file, heading_rule_for(rel_path))
        if ok:
            translated_count += 1
            translated_files.append(rel_path)
            # Фиксируем, от какого EN-состояния сделан этот перевод. Хэш берём с
            # диска ПОСЛЕ перевода: если апстрим успел уехать, статья честно
            # останется в очереди на следующий прогон.
            registry[rel_path] = file_hash(en_file)
            print(f"  OK")
        else:
            failed_count += 1
            print(f"  FAILED")

        # Периодическое сохранение: длинный прогон должен переживать обрыв
        if i % 5 == 0:
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)
            save_hash_registry(registry)

    # Final cache save
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    save_hash_registry(registry)

    elapsed = time.time() - start
    print()
    print(f"Done: {translated_count} translated, {failed_count} failed, "
          f"{int(elapsed // 60)}m {int(elapsed % 60)}s")

    # Save result for downstream steps
    result = {
        "translated_count": translated_count,
        "failed_count": failed_count,
        "translated_files": translated_files,
        "elapsed_seconds": int(elapsed),
    }
    with open("translation_result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
