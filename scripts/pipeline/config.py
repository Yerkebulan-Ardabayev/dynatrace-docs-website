"""
Pipeline configuration module.
Centralizes all settings, paths, and API configuration.
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
CACHE_DIR = SCRIPTS_DIR / ".translation_cache"
TERMINOLOGY_FILE = SCRIPTS_DIR / "terminology.yaml"
MKDOCS_CONFIG = PROJECT_ROOT / "mkdocs.yml"

# === API Keys ===
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

# === Scraper Settings ===
DYNATRACE_DOCS_URL = "https://docs.dynatrace.com"
SCRAPE_MAX_PAGES = int(os.getenv("SCRAPE_MAX_PAGES", "1000"))
SCRAPE_DELAY_SECONDS = 1.0
SCRAPE_CACHE_FILE = SCRIPTS_DIR / "dynatrace-docs" / ".cache" / "pages_cache.json"

# === Translation Settings ===
TRANSLATION_TARGET_LANG = "ru"
TRANSLATION_SOURCE_LANG = "en"
TRANSLATION_MAX_CHUNK_SIZE = 3000  # chars per chunk
TRANSLATION_RATE_LIMIT = 8  # requests per minute
TRANSLATION_MAX_RETRIES = 3
TRANSLATION_CACHE_TTL_DAYS = 30  # re-check after N days

# === Translation Provider Priority ===
PROVIDERS = [
    {
        "name": "gemini-flash",
        "api_key_env": "GEMINI_API_KEY",
        "model": "gemini-2.0-flash",
        "endpoint": "https://generativelanguage.googleapis.com/v1beta/models",
        "rate_limit": 15,  # req/min
        "daily_limit": 1500,
    },
    {
        "name": "groq",
        "api_key_env": "GROQ_API_KEY",
        "model": "llama-3.3-70b-versatile",
        "endpoint": "https://api.groq.com/openai/v1/chat/completions",
        "rate_limit": 8,
        "daily_limit": 100,  # ~100K tokens
    },
    {
        "name": "openrouter",
        "api_key_env": "OPENROUTER_API_KEY",
        "model": "google/gemma-3-27b-it:free",
        "endpoint": "https://openrouter.ai/api/v1/chat/completions",
        "rate_limit": 5,
        "daily_limit": 50,
    },
]

# === Validation Settings ===
VALIDATION_MAX_LENGTH_RATIO = 1.5  # translated text should be <=150% of source
VALIDATION_MIN_LENGTH_RATIO = 0.5  # translated text should be >=50% of source
VALIDATION_CJK_PATTERN = r"[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff]"  # CJK chars

# === Release Monitoring ===
RELEASE_NOTES_URL = "https://docs.dynatrace.com/whats-new"
RELEASE_REGISTRY_FILE = DOCS_DIR / "releases" / "registry.json"

# === CI/CD ===
GIT_AUTHOR_NAME = "github-actions[bot]"
GIT_AUTHOR_EMAIL = "github-actions[bot]@users.noreply.github.com"
