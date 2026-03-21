"""
Translation cache manager.
Caches translations by content hash for efficient incremental updates.
"""
import json
import hashlib
import os
import tempfile
from pathlib import Path
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any


class CacheManager:
    """Manages translation cache with hash-based invalidation."""

    def __init__(self, cache_dir: Path, ttl_days: int = 30):
        self.cache_dir = cache_dir
        self.ttl_days = ttl_days
        self.index_file = cache_dir / "index.json"
        self.stats_file = cache_dir / "stats.json"
        self._index: Dict[str, Any] = {}
        self._stats = {"hits": 0, "misses": 0, "expired": 0, "total_cached": 0}
        self._ensure_dirs()
        self._load_index()

    def _ensure_dirs(self):
        """Create cache directories if they don't exist."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        (self.cache_dir / "en").mkdir(exist_ok=True)

    def _load_index(self):
        """Load cache index from disk."""
        if self.index_file.exists():
            try:
                with open(self.index_file, "r", encoding="utf-8") as f:
                    self._index = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._index = {}

    def _save_index(self):
        """Save cache index to disk atomically (write to temp file, then rename)."""
        self._atomic_json_write(self.index_file, self._index)

    def _save_stats(self):
        """Save cache statistics."""
        self._stats["total_cached"] = len(self._index)
        self._atomic_json_write(self.stats_file, self._stats)

    @staticmethod
    def _atomic_json_write(target_path: Path, data: Any):
        """Atomically write JSON data: write to temp file, then os.replace()."""
        temp_fd = None
        temp_path = None
        try:
            temp_fd, temp_path = tempfile.mkstemp(
                dir=str(target_path.parent),
                suffix=".tmp",
            )
            with os.fdopen(temp_fd, "w", encoding="utf-8") as f:
                temp_fd = None  # os.fdopen takes ownership of fd
                json.dump(data, f, indent=2, ensure_ascii=False)
            os.replace(temp_path, str(target_path))
            temp_path = None  # replaced successfully, no cleanup needed
        except Exception:
            if temp_fd is not None:
                os.close(temp_fd)
            if temp_path is not None and os.path.exists(temp_path):
                os.unlink(temp_path)
            raise

    @staticmethod
    def content_hash(content: str, lang: str = "ru") -> str:
        """Generate SHA256 hash of content + target language."""
        key = f"{lang}:{content}"
        return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]

    def get(self, source_content: str, lang: str = "ru") -> Optional[str]:
        """
        Get cached translation if available and not expired.
        Returns translated text or None.
        """
        h = self.content_hash(source_content, lang)

        if h not in self._index:
            self._stats["misses"] += 1
            return None

        entry = self._index[h]

        # Check if source content changed
        if entry.get("source_hash") != hashlib.sha256(
            source_content.encode("utf-8")
        ).hexdigest()[:16]:
            self._stats["expired"] += 1
            return None

        # Check TTL
        cached_time = datetime.fromisoformat(entry["timestamp"])
        # Ensure timezone-aware comparison
        if cached_time.tzinfo is None:
            cached_time = cached_time.replace(tzinfo=timezone.utc)
        if datetime.now(timezone.utc) - cached_time > timedelta(days=self.ttl_days):
            self._stats["expired"] += 1
            return None

        self._stats["hits"] += 1
        return entry.get("translated")

    def put(
        self,
        source_content: str,
        translated: str,
        lang: str = "ru",
        provider: str = "unknown",
        quality_score: float = 1.0,
    ):
        """Store translation in cache."""
        h = self.content_hash(source_content, lang)
        source_h = hashlib.sha256(
            source_content.encode("utf-8")
        ).hexdigest()[:16]

        self._index[h] = {
            "source_hash": source_h,
            "translated": translated,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "provider": provider,
            "quality_score": quality_score,
            "lang": lang,
        }

        self._save_index()

    def invalidate(self, source_content: str, lang: str = "ru"):
        """Remove a specific cache entry."""
        h = self.content_hash(source_content, lang)
        if h in self._index:
            del self._index[h]
            self._save_index()

    def clear_expired(self) -> int:
        """Remove all expired entries. Returns count of removed entries."""
        now = datetime.now()
        expired_keys = []

        for h, entry in self._index.items():
            cached_time = datetime.fromisoformat(entry["timestamp"])
            if now - cached_time > timedelta(days=self.ttl_days):
                expired_keys.append(h)

        for key in expired_keys:
            del self._index[key]

        if expired_keys:
            self._save_index()

        return len(expired_keys)

    def get_stats(self) -> Dict[str, Any]:
        """Return cache statistics."""
        self._stats["total_cached"] = len(self._index)
        self._save_stats()
        return self._stats.copy()
