"""
Navigation updater for mkdocs.yml.
Automatically updates navigation based on translated files.
"""
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any

from .config import MKDOCS_CONFIG, DOCS_DIR


class _SafeLoaderIgnoreUnknown(yaml.SafeLoader):
    """YAML loader that ignores unknown Python tags (e.g. !!python/name)."""
    pass

_SafeLoaderIgnoreUnknown.add_multi_constructor(
    "tag:yaml.org,2002:python/",
    lambda loader, suffix, node: None,
)


class NavUpdater:
    """Updates mkdocs.yml navigation when new translations are available."""

    def __init__(self, config_path: Path = MKDOCS_CONFIG, docs_dir: Path = DOCS_DIR):
        self.config_path = config_path
        self.docs_dir = docs_dir

    def _load_config(self):
        """Load mkdocs.yml with safe handling of Python tags."""
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=_SafeLoaderIgnoreUnknown)

    def find_untranslated_nav_entries(self) -> List[Dict[str, str]]:
        """
        Find nav entries that point to en/ but have a ru/ translation available.
        Returns list of {en_path, ru_path, title}.
        """
        config = self._load_config()

        nav = config.get("nav", [])
        upgradeable = []
        self._scan_nav(nav, upgradeable)
        return upgradeable

    def _scan_nav(self, items: Any, upgradeable: List[Dict[str, str]]):
        """Recursively scan nav for upgradeable entries."""
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    for title, value in item.items():
                        if isinstance(value, str) and value.startswith("en/"):
                            # Check if ru/ version exists
                            ru_path = "ru/" + value[3:]
                            if (self.docs_dir / ru_path).exists():
                                upgradeable.append({
                                    "title": title,
                                    "en_path": value,
                                    "ru_path": ru_path,
                                })
                        elif isinstance(value, list):
                            self._scan_nav(value, upgradeable)

    def upgrade_to_russian(self, dry_run: bool = True) -> List[Dict[str, str]]:
        """
        Replace en/ paths with ru/ paths in nav where translations exist.
        Returns list of changes made.
        """
        upgradeable = self.find_untranslated_nav_entries()

        if not upgradeable or dry_run:
            return upgradeable

        # Read config as text to preserve formatting
        with open(self.config_path, "r", encoding="utf-8") as f:
            content = f.read()

        for entry in upgradeable:
            content = content.replace(entry["en_path"], entry["ru_path"])

        with open(self.config_path, "w", encoding="utf-8") as f:
            f.write(content)

        return upgradeable

    def list_nav_stats(self) -> Dict[str, int]:
        """Get statistics about nav language distribution."""
        config = self._load_config()

        stats = {"total": 0, "ru": 0, "en": 0, "managed": 0, "other": 0}
        nav = config.get("nav", [])
        self._count_nav(nav, stats)
        return stats

    def _count_nav(self, items: Any, stats: Dict[str, int]):
        """Count nav entries by language."""
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    for title, value in item.items():
                        if isinstance(value, str):
                            stats["total"] += 1
                            if value.startswith("ru/"):
                                stats["ru"] += 1
                            elif value.startswith("en/"):
                                stats["en"] += 1
                            elif value.startswith("managed/"):
                                stats["managed"] += 1
                            else:
                                stats["other"] += 1
                        elif isinstance(value, list):
                            self._count_nav(value, stats)
