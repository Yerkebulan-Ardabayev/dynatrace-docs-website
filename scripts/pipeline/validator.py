"""
Translation and documentation validator.
Validates quality of translations, Markdown structure, and link integrity.
"""
import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from .config import DOCS_DIR, DOCS_EN, DOCS_RU, VALIDATION_CJK_PATTERN


class ValidationIssue:
    """Represents a single validation issue."""

    def __init__(self, file: str, line: int, severity: str, message: str, rule: str):
        self.file = file
        self.line = line
        self.severity = severity  # "error", "warning", "info"
        self.message = message
        self.rule = rule

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file": self.file,
            "line": self.line,
            "severity": self.severity,
            "message": self.message,
            "rule": self.rule,
        }

    def __str__(self):
        return f"[{self.severity.upper()}] {self.file}:{self.line} ({self.rule}) {self.message}"


class DocumentValidator:
    """Validates documentation quality and consistency."""

    def __init__(self, docs_dir: Path = DOCS_DIR):
        self.docs_dir = docs_dir
        self.issues: List[ValidationIssue] = []

    def validate_all(self, strict: bool = False) -> List[ValidationIssue]:
        """Run all validation checks."""
        self.issues = []

        # Validate Russian translations
        ru_dir = self.docs_dir / "ru"
        if ru_dir.exists():
            for md_file in ru_dir.rglob("*.md"):
                self._validate_translation(md_file)

        # Validate Markdown structure across all docs
        for md_file in self.docs_dir.rglob("*.md"):
            self._validate_markdown(md_file)

        # Validate internal links
        self._validate_links()

        if strict:
            # In strict mode, warnings become errors
            for issue in self.issues:
                if issue.severity == "warning":
                    issue.severity = "error"

        return self.issues

    def _validate_translation(self, file_path: Path):
        """Validate a translated file for quality issues."""
        try:
            content = file_path.read_text(encoding="utf-8")
        except (IOError, UnicodeDecodeError):
            self.issues.append(
                ValidationIssue(
                    str(file_path), 0, "error", "Cannot read file", "file-read"
                )
            )
            return

        lines = content.split("\n")

        for i, line in enumerate(lines, 1):
            # Check for CJK characters in Russian translations
            cjk_match = re.search(VALIDATION_CJK_PATTERN, line)
            if cjk_match:
                self.issues.append(
                    ValidationIssue(
                        str(file_path),
                        i,
                        "error",
                        f"CJK character found: '{cjk_match.group()}'",
                        "no-cjk",
                    )
                )

            # Check for broken Markdown links (missing opening bracket)
            if re.match(r"^[А-Яа-яЁё\w\s]+\]\(", line):
                self.issues.append(
                    ValidationIssue(
                        str(file_path),
                        i,
                        "error",
                        "Markdown link missing opening '['",
                        "broken-link-syntax",
                    )
                )

            # Check for duplicate H1 headings
            if line.startswith("# ") and i > 1:
                prev_h1 = [
                    j
                    for j, l in enumerate(lines[:i - 1], 1)
                    if l.startswith("# ") and l.strip() == line.strip()
                ]
                if prev_h1:
                    self.issues.append(
                        ValidationIssue(
                            str(file_path),
                            i,
                            "warning",
                            f"Duplicate H1 heading (first at line {prev_h1[0]})",
                            "duplicate-h1",
                        )
                    )

    def _validate_markdown(self, file_path: Path):
        """Validate general Markdown structure."""
        try:
            content = file_path.read_text(encoding="utf-8")
        except (IOError, UnicodeDecodeError):
            return

        lines = content.split("\n")

        # Check for empty file (only frontmatter)
        content_without_frontmatter = re.sub(
            r"^---\n.*?\n---\n?", "", content, flags=re.DOTALL
        ).strip()
        if not content_without_frontmatter:
            self.issues.append(
                ValidationIssue(
                    str(file_path),
                    0,
                    "warning",
                    "File is empty (only frontmatter)",
                    "empty-file",
                )
            )

        # Check for CSS artifacts
        for i, line in enumerate(lines, 1):
            if re.search(r"\.css-[a-z0-9]+-", line):
                self.issues.append(
                    ValidationIssue(
                        str(file_path),
                        i,
                        "warning",
                        "CSS artifact found (scraper issue)",
                        "css-artifact",
                    )
                )
                break  # Only report once per file

    def _validate_links(self):
        """Validate internal link targets exist."""
        for md_file in self.docs_dir.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
            except (IOError, UnicodeDecodeError):
                continue

            # Find relative Markdown links
            links = re.findall(r"\[.*?\]\(((?!http|#|mailto).*?\.md.*?)\)", content)
            for link in links:
                # Remove anchors and query strings
                link_path = link.split("#")[0].split("?")[0]
                if not link_path:
                    continue

                target = (md_file.parent / link_path).resolve()
                if not target.exists():
                    line_num = 0
                    for i, line in enumerate(content.split("\n"), 1):
                        if link in line:
                            line_num = i
                            break
                    self.issues.append(
                        ValidationIssue(
                            str(md_file),
                            line_num,
                            "warning",
                            f"Broken link target: {link}",
                            "broken-link",
                        )
                    )

    def generate_report(self, output_path: Optional[Path] = None) -> Dict[str, Any]:
        """Generate validation report."""
        report = {
            "timestamp": __import__("datetime").datetime.now().isoformat(),
            "total_issues": len(self.issues),
            "errors": len([i for i in self.issues if i.severity == "error"]),
            "warnings": len([i for i in self.issues if i.severity == "warning"]),
            "info": len([i for i in self.issues if i.severity == "info"]),
            "issues": [i.to_dict() for i in self.issues],
            "issues_by_rule": {},
        }

        # Group by rule
        for issue in self.issues:
            if issue.rule not in report["issues_by_rule"]:
                report["issues_by_rule"][issue.rule] = 0
            report["issues_by_rule"][issue.rule] += 1

        if output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2, ensure_ascii=False)

        return report


class NavValidator:
    """Validates mkdocs.yml navigation against actual files."""

    def __init__(self, mkdocs_config: Path, docs_dir: Path):
        self.config_path = mkdocs_config
        self.docs_dir = docs_dir
        self.issues: List[ValidationIssue] = []

    def validate(self) -> List[ValidationIssue]:
        """Validate all nav entries point to existing files."""
        import yaml

        self.issues = []

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
        except Exception as e:
            self.issues.append(
                ValidationIssue(
                    str(self.config_path),
                    0,
                    "error",
                    f"Cannot parse mkdocs.yml: {e}",
                    "config-parse",
                )
            )
            return self.issues

        nav = config.get("nav", [])
        self._check_nav_items(nav, depth=0)
        return self.issues

    def _check_nav_items(self, items, depth: int):
        """Recursively check nav items."""
        if depth > 4:
            self.issues.append(
                ValidationIssue(
                    str(self.config_path),
                    0,
                    "warning",
                    f"Navigation depth exceeds 4 levels (at depth {depth})",
                    "nav-depth",
                )
            )

        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    for key, value in item.items():
                        if isinstance(value, str):
                            # Check if file exists
                            file_path = self.docs_dir / value
                            if not file_path.exists() and not (self.docs_dir / value).is_dir():
                                self.issues.append(
                                    ValidationIssue(
                                        str(self.config_path),
                                        0,
                                        "error",
                                        f"Nav entry '{key}' points to non-existent: {value}",
                                        "nav-missing-file",
                                    )
                                )
                            # Check title length
                            if len(key) > 60:
                                self.issues.append(
                                    ValidationIssue(
                                        str(self.config_path),
                                        0,
                                        "warning",
                                        f"Nav title too long ({len(key)} chars): '{key[:50]}...'",
                                        "nav-title-length",
                                    )
                                )
                        elif isinstance(value, list):
                            self._check_nav_items(value, depth + 1)
                elif isinstance(item, str):
                    file_path = self.docs_dir / item
                    if not file_path.exists():
                        self.issues.append(
                            ValidationIssue(
                                str(self.config_path),
                                0,
                                "error",
                                f"Nav entry points to non-existent: {item}",
                                "nav-missing-file",
                            )
                        )
