#!/usr/bin/env python3
"""
Генерация файлов для Google NotebookLM.

Стратегия: ТОЛЬКО русские переводы из docs/ru/
- Английские файлы НЕ включаются
- Группировка по разделу (2й уровень папки)
- По мере добавления новых переводов — перегенерировать и перезалить

NotebookLM лимиты:
- Макс 300 источников на ноутбук
- Макс 500,000 слов на источник
"""

import sys
import io
from pathlib import Path
from datetime import datetime

if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

MAX_WORDS_PER_FILE = 400_000
PROJECT_ROOT = Path(__file__).parent.parent
RU_DIR  = PROJECT_ROOT / 'docs' / 'ru'
OUT_DIR = PROJECT_ROOT / 'docs' / 'notebooklm'


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8', errors='ignore').strip()
    except Exception:
        return ''


def word_count(text: str) -> int:
    return len(text.split())


def get_group_key(rel_path: Path) -> str:
    parts = rel_path.parts
    if len(parts) >= 2:
        # Убираем .md из названия папки-группы (артефакт путей типа explorer.md/subfile)
        section = parts[0]
        subsection = parts[1].replace('.md', '')
        return f"{section}/{subsection}"
    return parts[0].replace('.md', '') if parts else 'root'


def collect_ru_groups() -> dict:
    """Собираем только RU файлы, группируем по разделу."""
    groups = {}
    for ru_file in sorted(RU_DIR.rglob('*.md')):
        rel = ru_file.relative_to(RU_DIR)
        key = get_group_key(rel)
        if key not in groups:
            groups[key] = []
        groups[key].append((rel, ru_file))
    return groups


def combine_group(entries: list, group_name: str) -> str:
    lines = [
        f"# Документация Dynatrace: {group_name}",
        f"Язык: Русский (RU)",
        f"Сгенерировано: {datetime.now().strftime('%Y-%m-%d')}",
        f"Файлов в разделе: {len(entries)}",
        "---",
        "",
    ]
    for rel, fpath in entries:
        content = read_file(fpath)
        if not content:
            continue
        lines.append(f"## {rel.as_posix()}")
        lines.append("")
        lines.append(content)
        lines.append("")
        lines.append("---")
        lines.append("")
    return '\n'.join(lines)


def write_group(key: str, entries: list) -> int:
    safe_name = key.replace('/', '__').replace('\\', '__')
    combined = combine_group(entries, key)
    words = word_count(combined)
    written = 0

    if words <= MAX_WORDS_PER_FILE:
        out_file = OUT_DIR / f"{safe_name}.md"
        out_file.write_text(combined, encoding='utf-8')
        print(f"  ✅ {safe_name}.md  ({len(entries)} файлов, {words:,} слов)")
        written = 1
    else:
        part_num = 1
        cur_entries, cur_words = [], 0
        for rel, fpath in entries:
            content = read_file(fpath)
            fw = word_count(content)
            if cur_words + fw > MAX_WORDS_PER_FILE and cur_entries:
                part_text = combine_group(cur_entries, f"{key} (часть {part_num})")
                out_file = OUT_DIR / f"{safe_name}__part{part_num}.md"
                out_file.write_text(part_text, encoding='utf-8')
                print(f"  ✅ {out_file.name}  ({len(cur_entries)} файлов, {cur_words:,} слов)")
                written += 1
                part_num += 1
                cur_entries, cur_words = [], 0
            cur_entries.append((rel, fpath))
            cur_words += fw
        if cur_entries:
            part_text = combine_group(cur_entries, f"{key} (часть {part_num})")
            out_file = OUT_DIR / f"{safe_name}__part{part_num}.md"
            out_file.write_text(part_text, encoding='utf-8')
            print(f"  ✅ {out_file.name}  ({len(cur_entries)} файлов, {cur_words:,} слов)")
            written += 1

    return written


def generate():
    print("=" * 60)
    print("  📚 Генерация файлов для NotebookLM")
    print("  Язык: ТОЛЬКО РУССКИЙ (docs/ru/)")
    print("=" * 60)

    if not RU_DIR.exists():
        print(f"❌ Не найдена директория: {RU_DIR}")
        sys.exit(1)

    # Очищаем выходную папку
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    deleted = sum(1 for f in OUT_DIR.glob('*.md') if not f.unlink())
    if deleted:
        print(f"\n  🗑️  Удалено старых файлов: {deleted}")

    groups = collect_ru_groups()
    total_docs = sum(len(v) for v in groups.values())

    print(f"\n  🇷🇺 Переведённых файлов: {total_docs}")
    print(f"  📂 Разделов: {len(groups)}")
    print(f"\n  Генерирую...")

    total_files = 0
    for key in sorted(groups.keys()):
        total_files += write_group(key, groups[key])

    all_out = list(OUT_DIR.glob('*.md'))
    total_size_mb = sum(f.stat().st_size for f in all_out) / 1024 / 1024

    print()
    print("=" * 60)
    print(f"  ✅ Готово!")
    print(f"  📁 Файлов для NotebookLM: {total_files}")
    print(f"  💾 Размер: {total_size_mb:.1f} MB")
    print(f"  🚫 Английских файлов: 0")
    print(f"  🚫 Дублей: 0")
    print(f"  📊 Лимит NotebookLM: 300 (использовано {total_files})")
    if total_files > 300:
        print(f"  ⚠️  Превышен лимит! NotebookLM примет только первые 300.")
    print("=" * 60)
    print(f"\n  💡 По мере перевода новых файлов запускайте снова:")
    print(f"     python scripts/generate_notebooklm.py")


if __name__ == '__main__':
    generate()
