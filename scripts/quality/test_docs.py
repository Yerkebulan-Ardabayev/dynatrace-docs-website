#!/usr/bin/env python3
"""
Automated documentation test suite.
Run: python scripts/quality/test_docs.py
Or:  python -m pytest scripts/quality/test_docs.py -v
"""
import re
import sys
import yaml
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
MKDOCS_CONFIG = PROJECT_ROOT / "mkdocs.yml"

# CJK character range
CJK_PATTERN = re.compile(r"[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff]")

# CSS artifact pattern
CSS_PATTERN = re.compile(r"\.css-[a-z0-9]+-[a-z]+")


class TestResult:
    def __init__(self, name: str, passed: bool, message: str = ""):
        self.name = name
        self.passed = passed
        self.message = message

    def __str__(self):
        status = "PASS" if self.passed else "FAIL"
        msg = f" — {self.message}" if self.message else ""
        return f"  [{status}] {self.name}{msg}"


class _SafeLoaderIgnoreUnknown(yaml.SafeLoader):
    """YAML loader that ignores unknown Python tags (e.g. !!python/name)."""
    pass

_SafeLoaderIgnoreUnknown.add_multi_constructor(
    "tag:yaml.org,2002:python/",
    lambda loader, suffix, node: None,
)


def load_nav_files(config_path: Path) -> list:
    """Extract all file paths from mkdocs.yml navigation."""
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=_SafeLoaderIgnoreUnknown)

    files = []
    _extract_nav_files(config.get("nav", []), files)
    return files


def _extract_nav_files(items, files, depth=0):
    """Recursively extract file paths from nav structure."""
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(value, str):
                        files.append({"path": value, "title": key, "depth": depth})
                    elif isinstance(value, list):
                        _extract_nav_files(value, files, depth + 1)
            elif isinstance(item, str):
                files.append({"path": item, "title": "", "depth": depth})


def test_all_nav_files_exist() -> TestResult:
    """Every file in mkdocs.yml nav must exist on disk."""
    nav_files = load_nav_files(MKDOCS_CONFIG)
    missing = []

    for entry in nav_files:
        path = entry["path"]
        full_path = DOCS_DIR / path
        # Handle directory references (ending with /)
        if path.endswith("/"):
            if not full_path.is_dir():
                missing.append(path)
        elif not full_path.exists():
            missing.append(path)

    if missing:
        return TestResult(
            "nav_files_exist",
            False,
            f"{len(missing)} missing: {', '.join(missing[:5])}",
        )
    return TestResult("nav_files_exist", True, f"{len(nav_files)} files OK")


def test_no_duplicate_nav_entries() -> TestResult:
    """No file should appear twice in navigation."""
    nav_files = load_nav_files(MKDOCS_CONFIG)
    seen = {}
    duplicates = []

    for entry in nav_files:
        path = entry["path"]
        if path in seen:
            duplicates.append(path)
        seen[path] = True

    if duplicates:
        return TestResult(
            "no_duplicate_nav",
            False,
            f"{len(duplicates)} duplicates: {', '.join(duplicates[:5])}",
        )
    return TestResult("no_duplicate_nav", True)


def test_max_nav_depth() -> TestResult:
    """Navigation should not exceed 4 levels depth."""
    nav_files = load_nav_files(MKDOCS_CONFIG)
    max_depth = max(entry["depth"] for entry in nav_files) if nav_files else 0

    if max_depth > 4:
        deep_items = [
            entry["title"] for entry in nav_files if entry["depth"] > 4
        ]
        return TestResult(
            "max_nav_depth",
            False,
            f"Max depth is {max_depth} (limit: 4). Items: {', '.join(deep_items[:3])}",
        )
    return TestResult("max_nav_depth", True, f"Max depth: {max_depth}")


def test_no_cjk_in_russian() -> TestResult:
    """Russian files should not contain CJK characters."""
    ru_dir = DOCS_DIR / "ru"
    if not ru_dir.exists():
        return TestResult("no_cjk_in_russian", True, "No ru/ directory")

    issues = []
    for md_file in ru_dir.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            for i, line in enumerate(content.split("\n"), 1):
                if CJK_PATTERN.search(line):
                    rel = md_file.relative_to(DOCS_DIR)
                    issues.append(f"{rel}:{i}")
        except (IOError, UnicodeDecodeError):
            pass

    if issues:
        return TestResult(
            "no_cjk_in_russian",
            False,
            f"{len(issues)} CJK occurrences: {', '.join(issues[:5])}",
        )
    return TestResult("no_cjk_in_russian", True)


def test_no_broken_markdown_links() -> TestResult:
    """Check for broken Markdown link syntax (missing [)."""
    ru_dir = DOCS_DIR / "ru"
    if not ru_dir.exists():
        return TestResult("markdown_links", True, "No ru/ directory")

    issues = []
    pattern = re.compile(r"^[А-Яа-яЁё\w\s]+\]\(")

    for md_file in ru_dir.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            for i, line in enumerate(content.split("\n"), 1):
                if pattern.match(line.strip()):
                    rel = md_file.relative_to(DOCS_DIR)
                    issues.append(f"{rel}:{i}")
        except (IOError, UnicodeDecodeError):
            pass

    if issues:
        return TestResult(
            "markdown_links",
            False,
            f"{len(issues)} broken links: {', '.join(issues[:5])}",
        )
    return TestResult("markdown_links", True)


def test_no_empty_pages() -> TestResult:
    """No .md file should be empty or only contain frontmatter."""
    empty = []

    for md_file in DOCS_DIR.rglob("*.md"):
        # Skip notebooklm and other generated dirs
        rel = str(md_file.relative_to(DOCS_DIR))
        if any(skip in rel for skip in ["notebooklm", "DYNATRACE_MANAGED_FULL"]):
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
            # Remove frontmatter
            body = re.sub(r"^---\n.*?\n---\n?", "", content, flags=re.DOTALL).strip()
            if not body:
                empty.append(rel)
        except (IOError, UnicodeDecodeError):
            pass

    if empty:
        return TestResult(
            "no_empty_pages",
            False,
            f"{len(empty)} empty: {', '.join(empty[:5])}",
        )
    return TestResult("no_empty_pages", True)


def test_no_css_artifacts() -> TestResult:
    """No .md file should contain CSS artifacts from scraping."""
    issues = []

    for md_file in DOCS_DIR.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            if CSS_PATTERN.search(content):
                rel = md_file.relative_to(DOCS_DIR)
                issues.append(str(rel))
        except (IOError, UnicodeDecodeError):
            pass

    if issues:
        return TestResult(
            "no_css_artifacts",
            False,
            f"{len(issues)} files with CSS: {', '.join(issues[:5])}",
        )
    return TestResult("no_css_artifacts", True)


def test_nav_titles_length() -> TestResult:
    """Nav titles should be under 60 characters."""
    nav_files = load_nav_files(MKDOCS_CONFIG)
    long_titles = []

    for entry in nav_files:
        if len(entry["title"]) > 60:
            long_titles.append(f"'{entry['title'][:50]}...' ({len(entry['title'])} chars)")

    if long_titles:
        return TestResult(
            "nav_title_length",
            False,
            f"{len(long_titles)} too long: {long_titles[0]}",
        )
    return TestResult("nav_title_length", True)


def run_all_tests() -> int:
    """Run all tests and print results."""
    print("=" * 60)
    print("DOCUMENTATION TEST SUITE")
    print("=" * 60)

    tests = [
        test_all_nav_files_exist,
        test_no_duplicate_nav_entries,
        test_max_nav_depth,
        test_no_cjk_in_russian,
        test_no_broken_markdown_links,
        test_no_empty_pages,
        test_no_css_artifacts,
        test_nav_titles_length,
    ]

    results = []
    for test_fn in tests:
        try:
            result = test_fn()
        except Exception as e:
            result = TestResult(test_fn.__name__, False, f"Exception: {e}")
        results.append(result)
        print(result)

    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)

    print()
    print(f"Results: {passed} passed, {failed} failed, {len(results)} total")
    print("=" * 60)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
