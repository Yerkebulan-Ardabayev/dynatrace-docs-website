#!/usr/bin/env python3
"""
Detect new and updated documentation articles.

Канонический корпус — Dynatrace MANAGED: docs/managed (EN) -> docs/managed-ru (RU).
Сравнивает английский Managed-источник с русским Managed-переводом и находит:
- NEW articles: есть в managed/ но нет в managed-ru/
- UPDATED articles: managed/ изменился с прошлой синхронизации (несовпадение хэша)
- OUTDATED translations: managed-ru/ есть, но managed/ изменён позже перевода

Generates a JSON report and a Markdown report for GitHub Issues.
Issue contains direct clickable links to files on GitHub for convenience.

Usage:
    python scripts/detect_changes.py \
        --source-dir docs/managed \
        --target-dir docs/managed-ru \
        --repo Yerkebulan-Ardabayev/dynatrace-docs-website \
        --report changes_report.json \
        --markdown changes_report.md
"""
import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


# Hash registry file — stores SHA256 hashes of en/ files from last sync
HASH_REGISTRY = Path(__file__).parent / ".change_tracking" / "hash_registry.json"


def text_hash(text: str) -> str:
    """Тот же хэш, что у file_hash, но по строке (нужен для старых версий из git)."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            head = "".join(
                ln for ln in text[:end].splitlines(keepends=True)
                if not ln.lstrip().startswith("scraped:")
            )
            text = head + text[end:]
    return hashlib.sha256(text.encode("utf-8", "surrogateescape")).hexdigest()[:16]


def file_hash(path: Path) -> str:
    """SHA256 хэш содержимого файла БЕЗ волатильной строки frontmatter `scraped:`.

    scrape_docs.py штампует `scraped: <datetime.now()>` в каждый файл при каждом
    скрейпе. Хэш сырых байт помечал бы КАЖДЫЙ пере-скрейпленный файл как
    «изменённый», даже когда реальный контент не менялся -> ложные «updated»,
    сожжённая квота перевода, churn коммитов (B3 аудита 2026-07-07). Исключаем
    только эту одну строку; title/source/тело остаются в хэше.
    """
    text = path.read_text(encoding="utf-8", errors="surrogateescape")
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            head = "".join(
                ln for ln in text[:end].splitlines(keepends=True)
                if not ln.lstrip().startswith("scraped:")
            )
            text = head + text[end:]
    return hashlib.sha256(text.encode("utf-8", "surrogateescape")).hexdigest()[:16]


def load_hash_registry() -> dict:
    """Load previous hash registry."""
    if HASH_REGISTRY.exists():
        with open(HASH_REGISTRY, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_hash_registry(registry: dict):
    """Save hash registry atomically."""
    HASH_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    tmp = HASH_REGISTRY.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    tmp.replace(HASH_REGISTRY)


def extract_title(md_file: Path) -> str:
    """Extract title from markdown frontmatter or first H1."""
    try:
        content = md_file.read_text(encoding="utf-8")
        # Try frontmatter title
        if content.startswith("---"):
            end = content.find("---", 3)
            if end > 0:
                frontmatter = content[3:end]
                for line in frontmatter.split("\n"):
                    if line.strip().startswith("title:"):
                        return line.split(":", 1)[1].strip().strip("'\"")
        # Try first H1
        for line in content.split("\n"):
            if line.startswith("# "):
                return line[2:].strip()
    except Exception:
        pass
    return md_file.stem.replace("-", " ").replace("_", " ").title()


def extract_summary(md_file: Path, max_lines: int = 10) -> str:
    """
    Extract a content summary from a markdown file.
    Returns first meaningful paragraphs (skipping frontmatter, headings, lists markers).
    Useful for release notes — captures what changed and why.
    """
    try:
        content = md_file.read_text(encoding="utf-8")
        # Skip frontmatter
        if content.startswith("---"):
            end = content.find("---", 3)
            if end > 0:
                content = content[end + 3:]

        lines = []
        for line in content.strip().split("\n"):
            stripped = line.strip()
            # Skip empty lines, breadcrumbs, images, HTML
            if not stripped:
                continue
            if stripped.startswith(("![", "<", "---", "| ---", "|  |")):
                continue
            # Skip single-word nav breadcrumbs like "* Release notes"
            if stripped.startswith("* ") and len(stripped) < 40:
                continue
            # Include headings (## Version...) and content
            lines.append(stripped)
            if len(lines) >= max_lines:
                break

        return "\n".join(lines) if lines else ""
    except Exception:
        return ""


def is_release_note(rel_path: str) -> bool:
    """Check if a file is a release note (whats-new section)."""
    return rel_path.startswith("whats-new/") or "release-note" in rel_path.lower()


def detect_section(rel_path: str) -> str:
    """Determine documentation section from file path."""
    parts = rel_path.split("/")
    if len(parts) > 1:
        section_map = {
            "observe": "Наблюдение (Observe)",
            "manage": "Управление (Manage)",
            "platform": "Платформа (Platform)",
            "deliver": "Доставка (Deliver)",
            "ingest-from": "Сбор данных (Ingest)",
            "analyze-explore-automate": "Анализ и автоматизация",
            "discover-dynatrace": "Знакомство с Dynatrace",
            "dynatrace-api": "Dynatrace API",
            "dynatrace-intelligence": "Dynatrace Intelligence",
        }
        return section_map.get(parts[0], parts[0].replace("-", " ").title())
    return "Корень"


def detect_changes(source_dir: Path, target_dir: Path,
                   update_registry: bool = True) -> dict:
    """
    Detect all changes between source (managed/) and target (managed-ru/) directories.

    Returns dict with:
        new_articles:     list of articles in source without target counterpart
        updated_articles: list of articles where source changed since last sync
        new_count:        number of new articles
        updated_count:    number of updated articles
        total_changes:    total articles needing translation
    """
    # Префиксы путей для отчёта/GitHub-ссылок берём из реальных каталогов, а не
    # хардкодим docs/en|docs/ru — иначе при Managed-корпусе ссылки вели бы в SaaS-дерево.
    src_prefix = source_dir.as_posix().rstrip("/")
    tgt_prefix = target_dir.as_posix().rstrip("/")

    prev_hashes = load_hash_registry()
    current_hashes = {}

    new_articles = []
    updated_articles = []
    # Статьи, по которым работа ещё НЕ сделана: их запись в реестре не двигаем.
    pending = set()

    # Scan all English source files
    if not source_dir.exists():
        print(f"ERROR: Source directory not found: {source_dir}")
        return {"new_articles": [], "updated_articles": [], "new_count": 0,
                "updated_count": 0, "total_changes": 0}

    source_files = sorted(source_dir.rglob("*.md"))

    for src_file in source_files:
        rel = str(src_file.relative_to(source_dir))
        current_hash = file_hash(src_file)
        current_hashes[rel] = current_hash

        ru_file = target_dir / rel
        title = extract_title(src_file)
        section = detect_section(rel)

        article_info = {
            "path": rel,
            "title": title,
            "section": section,
            "en_path": f"{src_prefix}/{rel}",
            "ru_path": f"{tgt_prefix}/{rel}",
            "hash": current_hash,
        }

        # For release notes, extract content summary
        if is_release_note(rel):
            summary = extract_summary(src_file, max_lines=15)
            if summary:
                article_info["summary"] = summary
                article_info["is_release"] = True

        # Case 1: No Russian translation exists → NEW
        if not ru_file.exists():
            article_info["type"] = "new"
            new_articles.append(article_info)
            pending.add(rel)
            continue

        # Case 2: English file changed since last sync → UPDATED
        prev_hash = prev_hashes.get(rel)
        if prev_hash and prev_hash != current_hash:
            article_info["type"] = "updated"
            article_info["prev_hash"] = prev_hash
            updated_articles.append(article_info)
            pending.add(rel)
            continue

        # Case 3 (mtime-эвристика) УДАЛЕНА (B7/P1-9 аудита): в CI git ставит время
        # чекаута ВСЕМ файлам, поэтому сравнение mtime en/ru даёт мусорный сигнал и
        # давало ложные «updated». Детект теперь только по hash_registry: при
        # пустом реестре (первый прогон) существующие переводы считаются
        # актуальными, а реальные апстрим-изменения ловятся хэшем на следующих
        # прогонах (реестр переживает прогоны через стабильный cache key).

    # Реестр означает «от какого EN-хэша сделан текущий RU», а НЕ «что скрейпер
    # видел в прошлый раз». Поэтому запись двигаем только для статей, по которым
    # работы нет; для new/updated оставляем прежнее значение, а актуальный хэш
    # проставит translate_changed.py после успешного перевода.
    #
    # Раньше реестр двигался здесь для ВСЕХ файлов, поэтому один прогон без
    # перевода стирал дрейф из радара навсегда: 904 статьи 08.07 и 327 статей
    # 20.07 были показаны в issue ровно один раз и больше никогда не всплывали.
    if update_registry:
        next_hashes = {
            rel: (prev_hashes.get(rel, h) if rel in pending else h)
            for rel, h in current_hashes.items()
        }
        save_hash_registry(next_hashes)

    result = {
        "new_articles": new_articles,
        "updated_articles": updated_articles,
        "new_count": len(new_articles),
        "updated_count": len(updated_articles),
        "total_changes": len(new_articles) + len(updated_articles),
        "total_source_files": len(source_files),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    return result


def generate_markdown_report(result: dict, repo: str = "") -> str:
    """
    Generate a Markdown report suitable for a GitHub Issue.

    Args:
        result: detection result dict
        repo: GitHub repo in format "owner/repo" for clickable links
    """
    lines = []
    date = datetime.now().strftime("%Y-%m-%d")

    # GitHub base URL for file links
    gh_base = f"https://github.com/{repo}/blob/main" if repo else ""

    lines.append(f"## Отчёт об обновлениях документации — {date}")
    lines.append("")
    lines.append(f"Обнаружено **{result['total_changes']}** статей, требующих перевода:")
    lines.append(f"- Новых статей: **{result['new_count']}**")
    lines.append(f"- Обновлённых статей: **{result['updated_count']}**")
    lines.append(f"- Всего исходных файлов (en): **{result['total_source_files']}**")
    lines.append("")

    # New articles by section
    if result["new_articles"]:
        lines.append("### 🆕 Новые статьи")
        lines.append("")

        sections = {}
        for art in result["new_articles"]:
            sec = art["section"]
            sections.setdefault(sec, []).append(art)

        for sec_name in sorted(sections.keys()):
            articles = sections[sec_name]
            lines.append(f"**{sec_name}** ({len(articles)} шт.)")
            lines.append("")
            for art in articles[:30]:
                if gh_base:
                    link = f"[{art['title']}]({gh_base}/{art['en_path']})"
                    lines.append(f"- [ ] {link} — `{art['path']}`")
                else:
                    lines.append(f"- [ ] `{art['path']}` — {art['title']}")
            if len(articles) > 30:
                lines.append(f"- ... и ещё {len(articles) - 30} файлов")
            lines.append("")

    # Updated articles
    if result["updated_articles"]:
        lines.append("### 🔄 Обновлённые статьи (перевод устарел)")
        lines.append("")

        sections = {}
        for art in result["updated_articles"]:
            sec = art["section"]
            sections.setdefault(sec, []).append(art)

        for sec_name in sorted(sections.keys()):
            articles = sections[sec_name]
            lines.append(f"**{sec_name}** ({len(articles)} шт.)")
            lines.append("")
            for art in articles[:30]:
                if gh_base:
                    link = f"[{art['title']}]({gh_base}/{art['en_path']})"
                    lines.append(f"- [ ] {link} — `{art['path']}`")
                else:
                    lines.append(f"- [ ] `{art['path']}` — {art['title']}")
            if len(articles) > 30:
                lines.append(f"- ... и ещё {len(articles) - 30} файлов")
            lines.append("")

    if result["total_changes"] == 0:
        lines.append("✅ Все статьи актуальны. Переводов не требуется.")
        lines.append("")

    # Instructions
    lines.append("---")
    lines.append("### 📋 Как перевести")
    lines.append("")
    lines.append("Открой чат с Claude (Cowork) и напиши одно из:")
    lines.append("")
    lines.append("```")
    lines.append("переведи observe/dashboards.md")
    lines.append("```")
    lines.append("```")
    lines.append("переведи всё новое")
    lines.append("```")
    lines.append("")
    lines.append("Claude сам прочитает файл, переведёт, сохранит в `docs/managed-ru/` и обновит навигацию.")
    lines.append("Тебе останется только `git push` — сайт обновится автоматически.")
    lines.append("")
    lines.append("_Автоматически сгенерировано пайплайном синхронизации._")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Detect documentation changes")
    parser.add_argument("--source-dir", default="docs/managed",
                        help="English Managed source directory")
    parser.add_argument("--target-dir", default="docs/managed-ru",
                        help="Russian Managed translation directory")
    parser.add_argument("--report", help="Output JSON report path")
    parser.add_argument("--markdown", help="Output Markdown report path")
    parser.add_argument("--no-registry-update", action="store_true",
                        help="Только посчитать очередь, не трогая реестр хэшей. "
                             "Нужен CI: реестром владеет локальный переводчик, и "
                             "запись из двух мест ломает учёт переведённого.")
    parser.add_argument("--repo", default="",
                        help="GitHub repo (owner/name) for clickable links in report")
    args = parser.parse_args()

    source_dir = Path(args.source_dir)
    target_dir = Path(args.target_dir)

    result = detect_changes(source_dir, target_dir,
                            update_registry=not args.no_registry_update)

    # Print summary
    print("=" * 60)
    print("CHANGE DETECTION REPORT")
    print("=" * 60)
    print(f"  Source files (en):     {result['total_source_files']}")
    print(f"  New articles:          {result['new_count']}")
    print(f"  Updated articles:      {result['updated_count']}")
    print(f"  Total needing work:    {result['total_changes']}")
    print("=" * 60)

    # Save JSON report
    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nJSON report saved to: {args.report}")

    # Save Markdown report
    if args.markdown:
        md_report = generate_markdown_report(result, repo=args.repo)
        with open(args.markdown, "w", encoding="utf-8") as f:
            f.write(md_report)
        print(f"Markdown report saved to: {args.markdown}")

    # Return non-zero if there are changes (for CI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
