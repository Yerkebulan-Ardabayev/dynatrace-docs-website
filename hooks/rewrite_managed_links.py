"""Перезапись абсолютных ссылок /managed/... в контенте страниц.

Проблема (аудит 2026-07-08): скрейп-корпус ссылается абсолютными путями вида
/managed/<topic> (~15 400 ссылок в ~2 500 файлах). MkDocs абсолютные ссылки не
трогает, и на GitHub Pages (base /dynatrace-docs-website/) КАЖДАЯ такая ссылка
уводила на https://<host>/managed/... -> 404. Т.е. внутренняя перелинковка
сайта не работала целиком.

Правило перезаписи (на этапе HTML, per-page):
  1) страница managed-ru/<topic>.md есть в сборке -> ОТНОСИТЕЛЬНАЯ внутренняя
     ссылка (работает и на GitHub Pages, и при локальной раздаче из подпути);
  2) страницы нет (например, ещё не переведена; таких ~200 после каждого
     upstream-дрейфа) -> живой первоисточник https://docs.dynatrace.com/managed/...
     Так ссылка ведёт на реальный EN-контент вместо 404, а после перевода
     страницы автоматически становится внутренней.

Якоря (#...) и query сохраняются. Ссылки, чей target отсутствует и в upstream
(мёртвые в самом источнике), чинятся в исходных .md, а не здесь.
"""

import posixpath
import re
from urllib.parse import urljoin

from mkdocs.utils import get_relative_url

UPSTREAM = "https://docs.dynatrace.com"

# href="/managed" или href="/managed/...", с возможными ?query и #anchor
_HREF_RE = re.compile(r'href="(/managed(?:/[^"]*)?)"')

# относительные href на страницы (не схемы, не корневые, не якоря)
_REL_HREF_RE = re.compile(r'href="((?!https?://|mailto:|javascript:|data:|tel:|/|#)[^"]+)"')

# у страничных URL нет расширения; всё с расширением (css/js/png/...) не трогаем
_HAS_EXT_RE = re.compile(r"\.[A-Za-z0-9]{1,6}$")


def _split_target(raw: str):
    """/managed/foo/bar#a?b -> (путь без якоря/query, хвост '#a'/'?b...')."""
    tail = ""
    path = raw
    for sep in ("#", "?"):
        if sep in path:
            path, rest = path.split(sep, 1)
            tail = sep + rest + tail if not tail else sep + rest + tail
    return path, tail


def _local_page(files, rest: str):
    """Включённый в сборку File для managed-ru/<rest>, либо None."""
    candidates = (
        [f"managed-ru/{rest}.md", f"managed-ru/{rest}/index.md"]
        if rest
        else ["managed-ru/index.md"]
    )
    for cand in candidates:
        f = files.get_file_from_path(cand)
        if f is None:
            continue
        # exclude_docs-файлы числятся в коллекции, но в сборку не попадают
        incl = getattr(f, "inclusion", None)
        if incl is not None and not incl.is_included():
            continue
        return f
    return None


def on_page_content(html, page, config, files):
    def repl_abs(m):
        raw = m.group(1)
        path, tail = _split_target(raw)
        rest = path[len("/managed"):].strip("/")
        f = _local_page(files, rest)
        if f is not None:
            rel = get_relative_url(f.url, page.file.url)
            return f'href="{rel}{tail}"'
        # локального перевода нет -> живой первоисточник (EN)
        return f'href="{UPSTREAM}{path}{tail}"'

    html = _HREF_RE.sub(repl_abs, html)

    def repl_rel(m):
        """Относительная ссылка на страницу корпуса, которой нет в сборке
        (например, непереведённый sprint) -> живой первоисточник. Существующие
        страницы и ассеты не трогаем."""
        raw = m.group(1)
        path, tail = _split_target(raw)
        if not path or _HAS_EXT_RE.search(path):
            return m.group(0)
        resolved = urljoin("/" + page.file.url, path).lstrip("/")
        resolved = posixpath.normpath(resolved)
        if not resolved.startswith("managed-ru/"):
            return m.group(0)
        rest = resolved[len("managed-ru/"):].strip("/")
        if _local_page(files, rest) is not None:
            return m.group(0)
        return f'href="{UPSTREAM}/managed/{rest}{tail}"'

    return _REL_HREF_RE.sub(repl_rel, html)
