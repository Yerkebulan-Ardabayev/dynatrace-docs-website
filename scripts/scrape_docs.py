#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dynatrace Documentation Scraper
Скачивает всю документацию с docs.dynatrace.com и конвертирует в Markdown
"""

import os
import re
import sys
import json
import time
import hashlib
from collections import deque
from email.utils import formatdate
from pathlib import Path
from urllib.parse import urljoin, urlparse
from datetime import datetime
import io

import requests
from requests.adapters import HTTPAdapter
try:
    from urllib3.util.retry import Retry
except ImportError:  # старая раскладка urllib3
    from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm

# Sentinel returned by get_page_content when server replies 304 Not Modified
NOT_MODIFIED = "__NOT_MODIFIED__"

# Encoding fix
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Configuration — Managed-only scope (Dynatrace itself decides what's applicable to Managed
# by placing it under /managed/ — anything outside is SaaS-only or shared without Managed warranty)
BASE_URL = os.environ.get("DYNATRACE_DOCS_URL", "https://docs.dynatrace.com/managed/")
DEFAULT_OUTPUT_DIR = "dynatrace-docs"
MAX_PAGES = None  # None = unlimited, or set number for testing
DELAY_SECONDS = 0.5  # Пауза между запросами. Было 1с, но после отказа от
# If-Modified-Since (B7) каждый прогон тянет ВСЕ ~2700 стр. заново, и при 1с полный
# обход не влезал в timeout-minutes джобы (ночной sync отменялся на 60-й минуте).
# 0.5с (~2 req/s) + Retry на 429 = вежливо и укладываемся с запасом.
TEST_MODE = False  # Set True for testing on small subset

# Каталоги НЕ создаются на импорте: реальный output задаётся через --output
# (в CI это docs/managed). Иначе импорт молча плодил бы каталог dynatrace-docs/
# в CWD, а кэш уходил бы не туда, куда пишутся сами страницы.


class DynatraceDocScraper:
    def __init__(self, base_url, output_dir, max_pages=None, test_mode=False):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        # Кэш живёт рядом с выходным деревом (output_dir/.cache), а не в фиксированном
        # ./dynatrace-docs/.cache. Так --output docs/managed кладёт кэш туда же, куда
        # пишет страницы, и не создаёт левый каталог dynatrace-docs/ в корне репо.
        self.cache_dir = self.output_dir / ".cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        # 0 трактуем как unlimited (как и обещает описание инпута воркфлоу): раньше
        # max_pages=0 давало условие "downloaded < 0" == False -> 0 страниц (B6 аудита).
        self.max_pages = 50 if test_mode else (None if max_pages == 0 else max_pages)
        self.test_mode = test_mode
        # Полнота обхода: cleanup_orphans удаляет ТОЛЬКО при полном успешном обходе.
        # Прерван по лимиту max_pages или очередь не опустела -> обход НЕ полный.
        self.crawl_complete = False

        self.visited_urls = set()
        self.to_visit = deque([base_url])
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        )
        # Retry с экспоненциальным backoff на 429/5xx и обрывах связи (P1-9 аудита):
        # без него одиночная 502/timeout от docs.dynatrace.com теряла страницу
        # насовсем. respect_retry_after_header чтит Retry-After при 429.
        _retry = Retry(
            total=4,
            backoff_factor=1.0,
            status_forcelist=[429, 500, 502, 503, 504],
            respect_retry_after_header=True,
        )
        _adapter = HTTPAdapter(max_retries=_retry)
        self.session.mount("https://", _adapter)
        self.session.mount("http://", _adapter)

        # Statistics
        self.stats = {
            "pages_downloaded": 0,
            "pages_converted": 0,
            "pages_unchanged": 0,  # 304 Not Modified — skipped re-download
            "errors": 0,
            "start_time": datetime.now(),
        }

        # Load cache
        self.cache_file = self.cache_dir / "pages_cache.json"
        self.cache = self.load_cache()

    def load_cache(self):
        """Load page cache to avoid re-downloading unchanged pages"""
        if self.cache_file.exists():
            with open(self.cache_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_cache(self):
        """Save page cache"""
        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(self.cache, f, indent=2)

    def get_url_hash(self, url):
        """Get hash of URL for caching"""
        return hashlib.md5(url.encode()).hexdigest()

    def is_valid_url(self, url):
        """Check if URL should be scraped"""
        parsed = urlparse(url)

        # Must be from dynatrace.com
        if "dynatrace.com" not in parsed.netloc:
            return False

        # Managed-only scope: /managed/ is Dynatrace's own authoritative marker for
        # what applies to Managed. Anything outside is SaaS-only or shared-without-warranty.
        if "/managed/" not in url:
            return False

        # Must be a documentation page
        if not (
            "/docs/" in url
            or "/support/help/" in url
            or "docs.dynatrace.com" in parsed.netloc
        ):
            return False

        # Skip certain paths
        skip_paths = [
            "/blog/",
            "/community/",
            "/resources/",
            "/downloads/",
            "/trial/",
            "/pricing/",
            "support.dynatrace.com",
            "university.dynatrace.com",
            "developer.dynatrace.com",
        ]
        if any(skip in url for skip in skip_paths):
            return False

        # Skip anchors and queries
        if "#" in url:
            return False

        # Allow queries for now (some docs use them)
        return True

    def get_page_content(self, url, local_mtime=None):
        """Download page content. If local_mtime is provided, send If-Modified-Since header
        and return NOT_MODIFIED sentinel when server replies 304 (page unchanged since last scrape).
        """
        headers = {}
        if local_mtime is not None:
            headers["If-Modified-Since"] = formatdate(local_mtime, usegmt=True)
        try:
            response = self.session.get(url, timeout=30, headers=headers)
            if response.status_code == 304:
                return NOT_MODIFIED
            response.raise_for_status()
            # requests falls back to ISO-8859-1 when the server sends no charset,
            # which mangles UTF-8 punctuation (… ' " – —) into mojibake (â€¦ etc.).
            # docs.dynatrace.com serves UTF-8, so force it on the bad fallback.
            if not response.encoding or response.encoding.lower() == "iso-8859-1":
                response.encoding = "utf-8"
            return response.text
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")
            self.stats["errors"] += 1
            return None

    def extract_links(self, soup, current_url):
        """Extract all valid links from page"""
        links = set()
        for link in soup.find_all("a", href=True):
            absolute_url = urljoin(current_url, link["href"])
            if self.is_valid_url(absolute_url):
                links.add(absolute_url)
        return links

    def extract_links_from_markdown(self, md_text, current_url):
        """Extract links from locally cached .md when server returned 304 (no fresh HTML to parse).
        Used so BFS can keep crawling even when page wasn't re-downloaded.
        """
        links = set()
        # Match [text](url) — both relative (resolved via urljoin) and absolute
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s#]+)", md_text):
            href = m.group(1).strip()
            if not href:
                continue
            absolute_url = urljoin(current_url, href)
            if self.is_valid_url(absolute_url):
                links.add(absolute_url)
        return links

    def convert_to_markdown(self, html_content, url):
        """Convert HTML to Markdown"""
        soup = BeautifulSoup(html_content, "html.parser")

        # Find main content area (adjust selector based on actual Dynatrace docs structure)
        main_content = (
            soup.find("main")
            or soup.find("article")
            or soup.find("div", class_="content")
        )

        if not main_content:
            # Fallback to body
            main_content = soup.find("body")

        if not main_content:
            return None

        # Get title
        title_tag = soup.find("h1") or soup.find("title")
        title = title_tag.get_text().strip() if title_tag else "Untitled"

        # Convert to markdown
        markdown = md(str(main_content), heading_style="ATX")

        # Add metadata header.
        # НЕ пишем волатильный `scraped:` таймстемп (B3 аудита, предпочтительный
        # вариант «не писать в файл вовсе»): иначе КАЖДЫЙ пере-скрейп менял бы все
        # ~2700 файлов, и Stage 5 `git add docs/managed/` коммитил бы тысячи файлов
        # с одним лишь изменившимся таймстемпом на каждую пару реальных правок.
        # detect_changes всё равно игнорирует этот field, а verify_corpus его
        # отсутствие допускает. Время последнего скрейпа живёт в кэше/registry.
        header = f"""---
title: {title}
source: {url}
---

# {title}

"""
        return header + markdown

    def get_output_path(self, url):
        """Get output file path for URL"""
        # Parse URL to get the path component
        parsed = urlparse(url)
        path = parsed.path

        # Remove leading path prefixes to get relative path
        # /managed/ first — Dynatrace serves Managed docs from /managed/<topic>/...
        # so we strip it to keep local layout flat (docs/en/<topic>/...) matching existing docs/ru/.
        for prefix in ["/managed/", "/docs/", "/support/help/"]:
            if path.startswith(prefix):
                relative_path = path[len(prefix) :]
                break
        else:
            relative_path = path.strip("/")

        # Clean up path
        relative_path = relative_path.strip("/")

        # Handle empty path (homepage)
        if not relative_path:
            self.output_dir.mkdir(parents=True, exist_ok=True)
            return self.output_dir / "index.md"

        # Create directory structure — защита от path traversal: URL приходит из
        # скрейпа (ссылки на страницах), сегменты `..`/пустые/абсолютные могут
        # увести запись ЗА пределы output_dir. Отбрасываем опасные сегменты и в
        # конце проверяем, что итоговый путь остаётся внутри output_dir.
        parts = [p for p in relative_path.split("/") if p and p not in (".", "..")]
        if not parts:
            self.output_dir.mkdir(parents=True, exist_ok=True)
            return self.output_dir / "index.md"

        filename = parts[-1]
        if not filename.endswith(".md"):
            filename += ".md"
        dir_path = (
            self.output_dir.joinpath(*parts[:-1])
            if len(parts) > 1
            else self.output_dir
        )

        out_base = self.output_dir.resolve()
        final_path = (dir_path / filename).resolve()
        if not final_path.is_relative_to(out_base):
            raise ValueError(
                f"path traversal заблокирован для URL {url!r}: {final_path}"
            )

        dir_path.mkdir(parents=True, exist_ok=True)
        return dir_path / filename

    def scrape_page(self, url):
        """Scrape single page. Uses If-Modified-Since against local file mtime for incremental
        re-scrapes: if server returns 304, skips re-download AND re-write, but still extracts
        links from the local .md so BFS can keep traversing the graph.
        """
        # Check cache
        url_hash = self.get_url_hash(url)

        output_path = self.get_output_path(url)
        # If-Modified-Since НЕ шлём (B7/P1-9 аудита): в CI git ставит mtime чекаута
        # (~сейчас) ВСЕМ файлам -> сервер на "изменено с сейчас?" всегда отвечает 304
        # -> скрейпер считал всё неизменным и НИКОГДА не подхватывал апстрим. Тянем
        # страницу всегда свежей; что реально изменилось решает detect_changes по хэшу.
        html_content = self.get_page_content(url)

        # Case 1: server says page unchanged → reuse local .md, extract links from markdown
        if html_content == NOT_MODIFIED:
            self.stats["pages_unchanged"] += 1
            try:
                md_text = output_path.read_text(encoding="utf-8")
                return self.extract_links_from_markdown(md_text, url)
            except Exception as e:
                print(f"⚠️  304 but can't read local {output_path}: {e}")
                return set()

        # Case 2: network/HTTP error
        if not html_content:
            return None

        self.stats["pages_downloaded"] += 1

        # Parse HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract links for further crawling
        new_links = self.extract_links(soup, url)

        # Convert to Markdown
        markdown = self.convert_to_markdown(html_content, url)
        if not markdown:
            return new_links

        # Save to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        self.stats["pages_converted"] += 1

        # Update cache
        self.cache[url_hash] = {
            "url": url,
            "file": str(output_path),
            "scraped": datetime.now().isoformat(),
        }

        return new_links

    def run(self):
        """Main scraping loop"""
        print("=" * 80)
        print("🚀 DYNATRACE DOCUMENTATION SCRAPER")
        print("=" * 80)
        print()
        print(f"Base URL: {self.base_url}")
        print(f"Output: {self.output_dir}")
        print(f"Max pages: {self.max_pages or 'Unlimited'}")
        print(f"Test mode: {self.test_mode}")
        print()

        with tqdm(desc="Scraping", unit=" pages") as pbar:
            while self.to_visit and (
                self.max_pages is None
                or self.stats["pages_downloaded"] < self.max_pages
            ):
                url = self.to_visit.popleft()

                if url in self.visited_urls:
                    continue

                self.visited_urls.add(url)
                pbar.set_postfix_str(f"Current: {url[-50:]}")

                # Scrape page
                unchanged_before = self.stats["pages_unchanged"]
                new_links = self.scrape_page(url)
                was_304 = self.stats["pages_unchanged"] > unchanged_before

                if new_links:
                    # Add new links to queue
                    for link in new_links:
                        if link not in self.visited_urls:
                            self.to_visit.append(link)

                pbar.update(1)

                # Be polite — full delay for real downloads, shorter for 304 Not Modified
                # (304 = cheap HEAD-like response, no body, doesn't stress the server)
                time.sleep(DELAY_SECONDS if not was_304 else 0.1)

                # Save cache periodically
                if self.stats["pages_downloaded"] % 10 == 0:
                    self.save_cache()

        # Обход считается полным, только если очередь опустела сама (не упёрлись в
        # max_pages). Неполный обход = запрет на удаление orphan-файлов ниже.
        hit_page_limit = (
            self.max_pages is not None
            and self.stats["pages_downloaded"] >= self.max_pages
        )
        self.crawl_complete = (not self.to_visit) and (not hit_page_limit)

        # Final cache save
        self.save_cache()

        # Print statistics
        self.print_stats()

    def find_orphan_files(self) -> list:
        """Find local .md files whose URL was NOT visited in this scrape run.
        These are pages that existed in a previous scrape but no longer appear on
        the live site (deleted/renamed/de-indexed by Dynatrace).
        """
        # Build set of expected local paths from cache (all URLs the scraper produced files for)
        expected_paths = set()
        for entry in self.cache.values():
            file_path = entry.get("file")
            if file_path:
                expected_paths.add(Path(file_path).resolve())

        # Compare against all local .md files
        orphans = []
        for md_file in self.output_dir.rglob("*.md"):
            if md_file.resolve() not in expected_paths:
                orphans.append(md_file)
        return orphans

    def cleanup_orphans(self, dry_run: bool = True) -> int:
        """Remove local files that no longer correspond to any scraped URL.
        Returns count of files removed (or that would be removed in dry-run).
        """
        orphans = self.find_orphan_files()
        if not orphans:
            print("✅ No orphan files found")
            return 0

        print(
            f"\n🗑️  Found {len(orphans)} orphan file(s) — pages no longer on live site:"
        )
        for p in orphans[:20]:
            rel = p.relative_to(self.output_dir)
            print(f"  - {rel}")
        if len(orphans) > 20:
            print(f"  ... and {len(orphans) - 20} more")

        if dry_run:
            print(f"\n(dry-run: pass --cleanup-orphans to actually delete)")
            return len(orphans)

        # Safety: не удалять, если скрейп был неполным — иначе живые страницы, не
        # дошедшие в этот прогон (сеть/лимит), будут снесены как "orphan".
        if not self.crawl_complete:
            print(
                "\n⚠️  Обход НЕ полный (упёрлись в max_pages или очередь не опустела) "
                "— отмена удаления orphans."
            )
            return 0
        total_local = sum(1 for _ in self.output_dir.rglob("*.md"))
        if self.stats.get("errors", 0) > 0:
            print(
                f"\n⚠️  Скрейп с ошибками ({self.stats['errors']}) — отмена удаления "
                f"orphans (возможен неполный обход)."
            )
            return 0
        if total_local and len(orphans) > 0.4 * total_local:
            print(
                f"\n⚠️  Orphans {len(orphans)} из {total_local} (>40%) — похоже на "
                f"неполный скрейп, отмена удаления."
            )
            return 0

        for p in orphans:
            try:
                p.unlink()
            except Exception as e:
                print(f"  ⚠️  Failed to remove {p}: {e}")
        print(f"\n✅ Removed {len(orphans)} orphan file(s)")
        return len(orphans)

    def print_stats(self):
        """Print scraping statistics"""
        duration = datetime.now() - self.stats["start_time"]

        print()
        print("=" * 80)
        print("📊 SCRAPING STATISTICS")
        print("=" * 80)
        print(f"✅ Pages downloaded: {self.stats['pages_downloaded']}")
        print(f"✅ Pages converted: {self.stats['pages_converted']}")
        print(f"⏭️  Pages unchanged (304): {self.stats['pages_unchanged']}")
        print(f"❌ Errors: {self.stats['errors']}")
        print(f"⏱️  Duration: {duration}")
        print(f"📁 Output directory: {self.output_dir.absolute()}")
        print()
        print(
            f"Average: {self.stats['pages_downloaded'] / duration.total_seconds():.2f} pages/second"
        )
        print("=" * 80)


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="Scrape Dynatrace documentation")
    parser.add_argument("--test", action="store_true", help="Test mode (50 pages)")
    parser.add_argument("--max-pages", type=int, help="Maximum pages to scrape")
    parser.add_argument(
        "--output",
        default=None,
        help="Output directory (default: <repo>/docs/managed — канонический Managed-корпус)",
    )
    parser.add_argument(
        "--cleanup-orphans",
        action="store_true",
        help="After scrape: DELETE local .md files for URLs that no longer exist on live site",
    )
    parser.add_argument(
        "--dry-run-orphans",
        action="store_true",
        help="After scrape: LIST orphan files that would be deleted (no actual delete)",
    )

    args = parser.parse_args()

    # По умолчанию пишем прямо в канонический Managed-корпус <repo>/docs/managed,
    # независимо от CWD (в CI скрейпер запускается из scripts/). Так убирается
    # мёртвый organize-шаг: скрейп сразу раскладывается по структуре URL в docs/managed.
    if args.output:
        output_dir = args.output
    else:
        output_dir = Path(__file__).resolve().parent.parent / "docs" / "managed"

    scraper = DynatraceDocScraper(
        base_url=BASE_URL,
        output_dir=output_dir,
        max_pages=args.max_pages,
        test_mode=args.test,
    )

    scraper.run()

    if args.cleanup_orphans:
        scraper.cleanup_orphans(dry_run=False)
    elif args.dry_run_orphans:
        scraper.cleanup_orphans(dry_run=True)


if __name__ == "__main__":
    main()
