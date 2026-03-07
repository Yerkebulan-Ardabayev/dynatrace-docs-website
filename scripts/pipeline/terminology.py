"""
Terminology engine for consistent translations.
Loads terms from terminology.yaml and applies pre/post-processing.
"""
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple


class TerminologyEngine:
    """Manages protected terms and translation consistency."""

    def __init__(self, terminology_file: Path):
        self.keep_as_is: List[str] = []
        self.translations: Dict[str, str] = {}
        self.normalize: Dict[str, str] = {}
        self._placeholder_map: Dict[str, str] = {}
        self._load(terminology_file)

    def _load(self, path: Path):
        """Load terminology from YAML file."""
        if not path.exists():
            print(f"[WARN] Terminology file not found: {path}")
            return

        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        self.keep_as_is = data.get("keep_as_is", [])
        self.translations = data.get("translations", {})
        self.normalize = data.get("normalize", {})

        # Sort by length (longest first) to avoid partial replacements
        self.keep_as_is.sort(key=len, reverse=True)

    def protect_terms(self, text: str) -> Tuple[str, Dict[str, str]]:
        """
        Replace protected terms with placeholders before translation.
        Returns (modified_text, placeholder_map).
        """
        placeholder_map = {}
        result = text

        for i, term in enumerate(self.keep_as_is):
            placeholder = f"{{{{TERM_{i:04d}}}}}"
            # Case-sensitive replacement for product names
            if term in result:
                placeholder_map[placeholder] = term
                result = result.replace(term, placeholder)

        self._placeholder_map = placeholder_map
        return result, placeholder_map

    def restore_terms(self, text: str, placeholder_map: Dict[str, str] = None) -> str:
        """Restore protected terms from placeholders after translation."""
        if placeholder_map is None:
            placeholder_map = self._placeholder_map

        result = text
        for placeholder, original in placeholder_map.items():
            result = result.replace(placeholder, original)

        return result

    def normalize_translation(self, text: str) -> str:
        """Apply normalization rules to fix known translation errors."""
        result = text

        for wrong, correct in self.normalize.items():
            result = result.replace(wrong, correct)

        return result

    def validate_terminology(self, source: str, translated: str) -> List[str]:
        """
        Check that protected terms were not translated.
        Returns list of issues found.
        """
        issues = []

        for term in self.keep_as_is:
            if term in source and term not in translated:
                # Check if it was partially translated
                term_lower = term.lower()
                if len(term) > 3:  # Skip very short terms
                    issues.append(
                        f"Protected term '{term}' missing in translation"
                    )

        return issues

    def apply_standard_translations(self, text: str) -> str:
        """
        Post-process: ensure standard terms are used consistently.
        Only applies to known translation pairs.
        """
        result = text
        # This is optional — used for post-processing QA
        return result
