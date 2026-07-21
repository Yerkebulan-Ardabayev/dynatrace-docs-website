#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Перенос изменений В ССЫЛКАХ из английского оригинала в русский перевод.

Зачем. Dynatrace массово проставляет в свои ссылки трекинговый параметр
(`?dt=m`). Для detect_changes это изменение содержимого, поэтому сотня статей
попадает в очередь на перевод, хотя текст не тронут ни на слово. Гнать их через
модель это часы работы и лишний риск: каждая новая генерация может уронить
разметку, которую прошлый перевод держал верно.

Что делает. Для статей, где английский оригинал отличается от прежней версии
ТОЛЬКО параметром у ссылок, тот же параметр проставляется в русском файле, а
запись в реестре хэшей двигается вперёд. Модель не вызывается вообще.

    python scripts/sync_link_params.py --since 0e682481          # посмотреть
    python scripts/sync_link_params.py --since 0e682481 --apply  # применить
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from detect_changes import file_hash, text_hash, load_hash_registry, save_hash_registry
from translate_changed import _structure_defect

BASE_DIR = Path(__file__).parent.parent
EN_DIR = BASE_DIR / "docs" / "managed"
RU_DIR = BASE_DIR / "docs" / "managed-ru"

# URL с трекинговым параметром: захватываем базу и сам параметр отдельно.
URL_WITH_PARAM = re.compile(r"(https?://[^\s)\]\"'<>]+?)(\?dt=[A-Za-z0-9_,-]+)")
STRIP_PARAM = re.compile(r"(https?://[^\s)\]\"'<>]+?)\?dt=[A-Za-z0-9_,-]+")


def strip_params(text: str) -> str:
    return STRIP_PARAM.sub(r"\1", text)


def old_version(rel: str, since: str) -> str | None:
    """Английский файл на момент базовой ревизии."""
    res = subprocess.run(
        ["git", "show", f"{since}:docs/managed/{rel}"],
        capture_output=True, text=True, cwd=BASE_DIR,
    )
    return res.stdout if res.returncode == 0 else None


def patch_ru(ru_text: str, en_new: str) -> tuple[str, int]:
    """Проставляет в русском тексте те же параметры ссылок, что в оригинале."""
    patched, count = ru_text, 0
    for base, param in set(URL_WITH_PARAM.findall(en_new)):
        # Меняем только адрес, за которым идёт закрывающая скобка, кавычка,
        # пробел или конец строки: иначе `.../x` подменил бы префикс в `.../xy`.
        pattern = re.compile(re.escape(base) + r"(?=[)\]\s\"'<]|$)")
        patched, n = pattern.subn(base + param, patched)
        count += n
    return patched, count


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--since", required=True,
                    help="ревизия, с которой сверяем английский оригинал")
    ap.add_argument("--apply", action="store_true",
                    help="записать изменения (без флага только отчёт)")
    args = ap.parse_args()

    registry = load_hash_registry()
    touched = skipped = defects = 0

    for en_file in sorted(EN_DIR.rglob("*.md")):
        rel = str(en_file.relative_to(EN_DIR))
        ru_file = RU_DIR / rel
        if not ru_file.exists():
            continue

        en_new = en_file.read_text(encoding="utf-8")
        if registry.get(rel) == file_hash(en_file):
            continue  # перевод уже соответствует этому состоянию

        en_old = old_version(rel, args.since)
        if en_old is None:
            continue
        # Берём только те статьи, где кроме параметра ссылок не изменилось НИЧЕГО.
        if strip_params(en_old) != strip_params(en_new):
            skipped += 1
            continue

        ru_text = ru_file.read_text(encoding="utf-8")
        patched, n = patch_ru(ru_text, en_new)
        touched += 1

        # Структуру всё равно сверяем. Если перевод разошёлся с оригиналом ЕЩЁ ДО
        # нас (наследие ручного перевода: пропавшая ссылка, лишний заголовок), то
        # двигать реестр нельзя: статья будет помечена актуальной, и дефект
        # останется в корпусе навсегда. Ссылки чиним, а саму статью оставляем в
        # очереди, её выправит обычный перевод.
        defect = _structure_defect(en_new, patched)
        mark = "патч" if args.apply else "нашёл"
        if defect:
            defects += 1
            print(f"{mark}: {rel} ({n} ссылок) — В ОЧЕРЕДЬ, старое расхождение: {defect}")
        else:
            print(f"{mark}: {rel} ({n} ссылок)")

        if args.apply:
            if patched != ru_text:
                tmp = ru_file.with_suffix(ru_file.suffix + ".tmp")
                tmp.write_text(patched, encoding="utf-8")
                tmp.replace(ru_file)
            if not defect:
                registry[rel] = file_hash(en_file)
            else:
                # Именно СТАРЫЙ хэш, а не удаление записи: детект считает статью
                # устаревшей по НЕСОВПАДЕНИЮ хэшей, а при отсутствии записи он
                # её просто не увидит, и дефект спрячется вместо починки.
                registry[rel] = text_hash(en_old)

    if args.apply:
        save_hash_registry(registry)

    print(f"\nстатей с изменением только в ссылках: {touched}")
    print(f"статей с содержательными правками (их переводим): {skipped}")
    print(f"из пропатченных оставлено в очереди из-за старых расхождений: {defects}")
    if not args.apply:
        print("это был сухой прогон, для записи добавь --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
