"""
Dynatrace Release Tracker.
Monitors Dynatrace release notes and downloads new versions.
"""
import json
import hashlib
import re
import requests
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
from bs4 import BeautifulSoup


class ReleaseTracker:
    """Tracks Dynatrace releases and manages version history."""

    RELEASE_PAGES = {
        "saas": "https://docs.dynatrace.com/whats-new/changelog",
        "oneagent": "https://docs.dynatrace.com/whats-new/oneagent-release-notes",
        "activegate": "https://docs.dynatrace.com/whats-new/activegate-release-notes",
    }

    def __init__(self, registry_path: Path, docs_dir: Path):
        self.registry_path = registry_path
        self.docs_dir = docs_dir
        self.registry: Dict[str, Any] = self._load_registry()

    def _load_registry(self) -> Dict[str, Any]:
        """Load release registry from disk."""
        if self.registry_path.exists():
            try:
                with open(self.registry_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass

        return {
            "last_check": None,
            "releases": [],
        }

    def _save_registry(self):
        """Save registry to disk."""
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)
        self.registry["last_check"] = datetime.now().isoformat()
        with open(self.registry_path, "w", encoding="utf-8") as f:
            json.dump(self.registry, f, indent=2, ensure_ascii=False)

    def check_for_updates(self) -> List[Dict[str, str]]:
        """
        Check Dynatrace release pages for new releases.
        Returns list of new releases found.
        NEVER overwrites existing release files.
        """
        new_releases = []

        for release_type, url in self.RELEASE_PAGES.items():
            try:
                releases = self._scrape_releases(url, release_type)
                for release in releases:
                    if not self._is_known(release):
                        new_releases.append(release)
                        self._register_release(release)
            except Exception as e:
                print(f"[WARN] Failed to check {release_type}: {e}")

        if new_releases:
            self._save_registry()

        return new_releases

    def _scrape_releases(self, url: str, release_type: str) -> List[Dict[str, str]]:
        """Scrape release notes from a Dynatrace page."""
        releases = []

        try:
            response = requests.get(url, timeout=30, headers={
                "User-Agent": "DynatraceDocs/1.0 (Documentation Pipeline)"
            })
            if response.status_code != 200:
                return releases

            soup = BeautifulSoup(response.text, "html.parser")

            # Find version headings (h2 or h3 with version numbers)
            version_pattern = re.compile(r"(\d+\.\d+(?:\.\d+)?)")
            headings = soup.find_all(["h2", "h3"])

            for heading in headings:
                text = heading.get_text(strip=True)
                version_match = version_pattern.search(text)
                if version_match:
                    version = version_match.group(1)

                    # Get content until next heading
                    content_parts = []
                    sibling = heading.find_next_sibling()
                    while sibling and sibling.name not in ["h2", "h3"]:
                        content_parts.append(str(sibling))
                        sibling = sibling.find_next_sibling()

                    content = "\n".join(content_parts)
                    content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]

                    releases.append({
                        "version": version,
                        "type": release_type,
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "title": text,
                        "content_hash": content_hash,
                        "source_url": url,
                        "content_md": self._html_to_markdown(content),
                    })

        except Exception as e:
            print(f"[ERROR] Scraping {url}: {e}")

        return releases

    def _html_to_markdown(self, html: str) -> str:
        """Simple HTML to Markdown conversion."""
        try:
            from markdownify import markdownify
            return markdownify(html, heading_style="ATX")
        except ImportError:
            # Fallback: strip HTML tags
            soup = BeautifulSoup(html, "html.parser")
            return soup.get_text()

    def _is_known(self, release: Dict[str, str]) -> bool:
        """Check if release is already in registry."""
        for known in self.registry["releases"]:
            if (
                known["version"] == release["version"]
                and known["type"] == release["type"]
            ):
                return True
        return False

    def _register_release(self, release: Dict[str, str]):
        """Add release to registry and save to file."""
        entry = {
            "version": release["version"],
            "type": release["type"],
            "date": release["date"],
            "title": release["title"],
            "source_url": release["source_url"],
            "content_hash": release["content_hash"],
            "translated": False,
            "translation_date": None,
            "files": {
                "en": f"en/whats-new/{release['type']}/{release['version']}.md",
            },
        }

        # Save the release note as a Markdown file
        en_path = self.docs_dir / entry["files"]["en"]
        en_path.parent.mkdir(parents=True, exist_ok=True)

        # NEVER overwrite existing files
        if not en_path.exists():
            content = f"""---
title: "{release['title']}"
version: "{release['version']}"
type: "{release['type']}"
date: "{release['date']}"
source: "{release['source_url']}"
---

# {release['title']}

{release.get('content_md', '')}
"""
            en_path.write_text(content, encoding="utf-8")
            print(f"  New release: {release['type']} {release['version']}")

        self.registry["releases"].append(entry)

    def get_untranslated(self) -> List[Dict[str, Any]]:
        """Get list of releases that haven't been translated yet."""
        return [r for r in self.registry["releases"] if not r.get("translated")]

    def mark_translated(self, version: str, release_type: str, ru_path: str):
        """Mark a release as translated."""
        for release in self.registry["releases"]:
            if release["version"] == version and release["type"] == release_type:
                release["translated"] = True
                release["translation_date"] = datetime.now().isoformat()
                release["files"]["ru"] = ru_path
                break
        self._save_registry()

    def generate_changelog(self, output_path: Path, lang: str = "ru"):
        """Generate a combined changelog page from all releases."""
        releases = sorted(
            self.registry["releases"],
            key=lambda r: r.get("date", ""),
            reverse=True,
        )

        content = "---\ntitle: История изменений Dynatrace\n---\n\n"
        content += "# История изменений Dynatrace\n\n"

        current_type = None
        for release in releases:
            if release["type"] != current_type:
                current_type = release["type"]
                content += f"\n## {current_type.upper()}\n\n"

            status = "RU" if release.get("translated") else "EN"
            content += f"- **{release['version']}** ({release.get('date', 'N/A')}) [{status}] — {release.get('title', '')}\n"

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
