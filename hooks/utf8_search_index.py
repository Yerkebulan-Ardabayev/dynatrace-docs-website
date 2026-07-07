"""MkDocs post-build hook: пере-кодировать search_index.json в UTF-8.

Зачем (аудит 2026-07-07, B2/U1):
Плагин search в mkdocs пишет search_index.json через json.dumps с ensure_ascii=True,
поэтому каждая кириллическая буква превращается в `\\uXXXX`, 6 байт вместо 2 в UTF-8
(~3x раздувание на русском тексте). На полном RU-корпусе (docs/ru + docs/managed-ru)
это даёт индекс ~106 МБ > лимита GitHub 100 МБ -> deploy падает при пуше в gh-pages.

Пере-кодирование в UTF-8 (ensure_ascii=False) + компактные разделители снижает индекс
до ~50 МБ: deploy проходит, и поиск в браузере грузит вдвое меньше. Данные и структура
не меняются: это тот же валидный JSON (JSON.parse читает UTF-8 прозрачно), меняется
только байтовое представление. Идемпотентно: повторный прогон уже-UTF-8 файла безвреден.
"""
import json
import os


def on_post_build(config, **kwargs):
    path = os.path.join(config["site_dir"], "search", "search_index.json")
    if not os.path.exists(path):
        return

    before = os.path.getsize(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    after = os.path.getsize(path)

    print(
        f"[utf8_search_index] search_index.json: "
        f"{before / 1048576:.1f} MB -> {after / 1048576:.1f} MB (UTF-8, compact)"
    )
