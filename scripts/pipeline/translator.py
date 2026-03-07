"""
Multi-provider translation engine with fallback chain.
Supports Gemini Flash, Groq, and OpenRouter.
"""
import re
import time
import json
import requests
from pathlib import Path
from typing import Optional, List, Dict, Tuple

from .config import (
    PROVIDERS,
    GEMINI_API_KEY,
    GROQ_API_KEY,
    OPENROUTER_API_KEY,
    TRANSLATION_MAX_CHUNK_SIZE,
    TRANSLATION_MAX_RETRIES,
    TRANSLATION_RATE_LIMIT,
    TERMINOLOGY_FILE,
)
from .terminology import TerminologyEngine
from .cache_manager import CacheManager


class TranslationProvider:
    """Base class for translation API providers."""

    def __init__(self, name: str, api_key: str, model: str, endpoint: str, rate_limit: int):
        self.name = name
        self.api_key = api_key
        self.model = model
        self.endpoint = endpoint
        self.rate_limit = rate_limit
        self._last_request_time = 0

    def _rate_limit_wait(self):
        """Wait to respect rate limits."""
        elapsed = time.time() - self._last_request_time
        min_interval = 60.0 / self.rate_limit
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        self._last_request_time = time.time()

    def translate(self, text: str, source_lang: str = "en", target_lang: str = "ru") -> Optional[str]:
        """Translate text. Returns translated text or None on failure."""
        raise NotImplementedError


class GeminiProvider(TranslationProvider):
    """Google Gemini Flash translation provider."""

    def translate(self, text: str, source_lang: str = "en", target_lang: str = "ru") -> Optional[str]:
        self._rate_limit_wait()

        prompt = self._build_prompt(text, source_lang, target_lang)

        try:
            url = f"{self.endpoint}/{self.model}:generateContent?key={self.api_key}"
            response = requests.post(
                url,
                json={"contents": [{"parts": [{"text": prompt}]}]},
                headers={"Content-Type": "application/json"},
                timeout=60,
            )

            if response.status_code == 200:
                data = response.json()
                candidates = data.get("candidates", [])
                if candidates:
                    return candidates[0]["content"]["parts"][0]["text"]
            else:
                print(f"[Gemini] Error {response.status_code}: {response.text[:200]}")
                return None
        except Exception as e:
            print(f"[Gemini] Exception: {e}")
            return None

    def _build_prompt(self, text: str, source_lang: str, target_lang: str) -> str:
        return f"""Translate the following technical documentation from {source_lang} to {target_lang}.

RULES:
1. Preserve ALL Markdown formatting exactly (headers, links, code blocks, tables, admonitions)
2. Do NOT translate code inside ``` blocks
3. Do NOT translate product names: Dynatrace, OneAgent, ActiveGate, Grail, Davis, DQL, Monaco, etc.
4. Do NOT translate URLs or file paths
5. Keep technical terms consistent
6. Preserve frontmatter (--- blocks) as-is
7. Output ONLY the translated text, no explanations

TEXT:
{text}"""


class GroqProvider(TranslationProvider):
    """Groq (Llama) translation provider."""

    def translate(self, text: str, source_lang: str = "en", target_lang: str = "ru") -> Optional[str]:
        self._rate_limit_wait()

        prompt = f"""Translate this technical documentation from {source_lang} to {target_lang}.
Preserve all Markdown formatting, code blocks, links, and product names (Dynatrace, OneAgent, etc.).
Output ONLY the translation.

{text}"""

        try:
            response = requests.post(
                self.endpoint,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1,
                    "max_tokens": 8000,
                },
                timeout=60,
            )

            if response.status_code == 200:
                data = response.json()
                return data["choices"][0]["message"]["content"]
            else:
                print(f"[Groq] Error {response.status_code}: {response.text[:200]}")
                return None
        except Exception as e:
            print(f"[Groq] Exception: {e}")
            return None


class OpenRouterProvider(TranslationProvider):
    """OpenRouter translation provider (free models)."""

    def translate(self, text: str, source_lang: str = "en", target_lang: str = "ru") -> Optional[str]:
        self._rate_limit_wait()

        prompt = f"""Translate this technical documentation from {source_lang} to {target_lang}.
Preserve all Markdown formatting, code blocks, links, and product names.
Output ONLY the translation.

{text}"""

        try:
            response = requests.post(
                self.endpoint,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1,
                },
                timeout=90,
            )

            if response.status_code == 200:
                data = response.json()
                return data["choices"][0]["message"]["content"]
            else:
                print(f"[OpenRouter] Error {response.status_code}")
                return None
        except Exception as e:
            print(f"[OpenRouter] Exception: {e}")
            return None


class TranslationPipeline:
    """
    Main translation pipeline with:
    - Multi-provider fallback chain
    - Terminology protection
    - Semantic chunking
    - Caching
    - Validation
    """

    def __init__(self, cache_dir: Path, terminology_file: Path = TERMINOLOGY_FILE):
        self.terminology = TerminologyEngine(terminology_file)
        self.cache = CacheManager(cache_dir)
        self.providers: List[TranslationProvider] = []
        self._init_providers()

    def _init_providers(self):
        """Initialize translation providers based on available API keys."""
        api_keys = {
            "GEMINI_API_KEY": GEMINI_API_KEY,
            "GROQ_API_KEY": GROQ_API_KEY,
            "OPENROUTER_API_KEY": OPENROUTER_API_KEY,
        }

        provider_classes = {
            "gemini-flash": GeminiProvider,
            "groq": GroqProvider,
            "openrouter": OpenRouterProvider,
        }

        for pconfig in PROVIDERS:
            key = api_keys.get(pconfig["api_key_env"], "")
            if key:
                cls = provider_classes.get(pconfig["name"])
                if cls:
                    provider = cls(
                        name=pconfig["name"],
                        api_key=key,
                        model=pconfig["model"],
                        endpoint=pconfig["endpoint"],
                        rate_limit=pconfig["rate_limit"],
                    )
                    self.providers.append(provider)

        if not self.providers:
            print("[WARN] No translation providers available. Set API keys in .env")

    def translate_file(
        self, source_path: Path, target_path: Path, target_lang: str = "ru"
    ) -> bool:
        """
        Translate a single Markdown file.
        Returns True if successful.
        """
        try:
            content = source_path.read_text(encoding="utf-8")
        except (IOError, UnicodeDecodeError) as e:
            print(f"[ERROR] Cannot read {source_path}: {e}")
            return False

        # Check cache first
        cached = self.cache.get(content, target_lang)
        if cached:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(cached, encoding="utf-8")
            return True

        # Extract and preserve frontmatter
        frontmatter, body = self._split_frontmatter(content)

        # Split into semantic chunks
        chunks = self._semantic_split(body)

        # Translate each chunk
        translated_chunks = []
        provider_used = None

        for chunk in chunks:
            # Protect terms
            protected, pmap = self.terminology.protect_terms(chunk)

            # Try providers in order
            translated = None
            for provider in self.providers:
                translated = provider.translate(protected, "en", target_lang)
                if translated:
                    provider_used = provider.name
                    break

            if translated is None:
                print(f"[ERROR] All providers failed for chunk in {source_path}")
                return False

            # Restore protected terms
            translated = self.terminology.restore_terms(translated, pmap)
            translated = self.terminology.normalize_translation(translated)
            translated_chunks.append(translated)

        # Combine result
        translated_body = "\n".join(translated_chunks)
        result = frontmatter + translated_body if frontmatter else translated_body

        # Write output
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(result, encoding="utf-8")

        # Cache result
        self.cache.put(content, result, target_lang, provider_used or "unknown")

        return True

    def _split_frontmatter(self, content: str) -> Tuple[str, str]:
        """Split frontmatter from body."""
        match = re.match(r"^(---\n.*?\n---\n?)", content, re.DOTALL)
        if match:
            return match.group(1), content[match.end():]
        return "", content

    def _semantic_split(self, text: str, max_size: int = TRANSLATION_MAX_CHUNK_SIZE) -> List[str]:
        """
        Split text into semantic chunks by Markdown structure.
        Preserves code blocks, tables, and admonitions.
        """
        if len(text) <= max_size:
            return [text]

        chunks = []
        current_chunk = []
        current_size = 0
        in_code_block = False

        lines = text.split("\n")
        for line in lines:
            # Track code blocks
            if line.strip().startswith("```"):
                in_code_block = not in_code_block

            # Split at headers (## or ###) when not in code block
            if (
                not in_code_block
                and re.match(r"^#{1,3}\s", line)
                and current_size > 0
                and current_size + len(line) > max_size
            ):
                chunks.append("\n".join(current_chunk))
                current_chunk = [line]
                current_size = len(line)
            else:
                current_chunk.append(line)
                current_size += len(line) + 1  # +1 for newline

        if current_chunk:
            chunks.append("\n".join(current_chunk))

        return chunks

    def translate_directory(
        self, source_dir: Path, target_dir: Path, target_lang: str = "ru"
    ) -> Dict[str, int]:
        """
        Translate all Markdown files in a directory.
        Returns stats dict.
        """
        stats = {"total": 0, "translated": 0, "cached": 0, "failed": 0, "skipped": 0}

        md_files = list(source_dir.rglob("*.md"))
        stats["total"] = len(md_files)

        for source_file in md_files:
            relative = source_file.relative_to(source_dir)
            target_file = target_dir / relative

            # Skip if target already exists and is newer
            if target_file.exists():
                if target_file.stat().st_mtime >= source_file.stat().st_mtime:
                    stats["skipped"] += 1
                    continue

            print(f"  Translating: {relative}")
            if self.translate_file(source_file, target_file, target_lang):
                stats["translated"] += 1
            else:
                stats["failed"] += 1

        return stats
