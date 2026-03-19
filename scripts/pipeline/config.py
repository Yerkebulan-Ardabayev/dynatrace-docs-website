"""
Pipeline configuration module.
Centralizes all settings, paths, and API configuration.

Architecture:
- Scrape: downloads English docs from docs.dynatrace.com
- Detect: finds new/updated articles that need translation
- Notify: creates GitHub Issue with list of articles to translate
- Place: helper to correctly place manual translations and update nav
- AI: stays only as chat assistant on the site (Groq widget)
"""
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not required in CI validation

# === Paths ===
PROJECT_ROOT = Path(__file__).parent.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
DOCS_EN = DOCS_DIR / "en"
DOCS_RU = DOCS_DIR / "ru"
DOCS_MANAGED = DOCS_DIR / "managed"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
MKDOCS_CONFIG = PROJECT_ROOT / "mkdocs.yml"

# === Change Tracking ===
CHANGE_TRACKING_DIR = SCRIPTS_DIR / ".change_tracking"
HASH_REGISTRY_FILE = CHANGE_TRACKING_DIR / "hash_registry.json"

# === Scraper Settings ===
DYNATRACE_DOCS_URL = "https://docs.dynatrace.com"
SCRAPE_MAX_PAGES = int(os.getenv("SCRAPE_MAX_PAGES", "1000"))
SCRAPE_DELAY_SECONDS = 1.0
SCRAPE_CACHE_FILE = SCRIPTS_DIR / "dynatrace-docs" / ".cache" / "pages_cache.json"

# === AI Chat Assistant (Groq — site widget only) ===
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# === Validation Settings ===
VALIDATION_CJK_PATTERN = r"[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff]"  # CJK chars

# === Release Monitoring ===
RELEASE_NOTES_URL = "https://docs.dynatrace.com/whats-new"
RELEASE_REGISTRY_FILE = DOCS_DIR / "releases" / "registry.json"

# === CI/CD ===
GIT_AUTHOR_NAME = "github-actions[bot]"
GIT_AUTHOR_EMAIL = "github-actions[bot]@users.noreply.github.com"
