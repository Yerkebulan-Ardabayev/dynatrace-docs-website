#!/usr/bin/env python3
"""
Sanitize scraped documentation to remove secret-like patterns
that trigger GitHub Push Protection.

These are NOT real secrets — they are example values from Dynatrace documentation.
GitHub Secret Scanning cannot distinguish between real secrets and documentation examples.
"""

import re
import sys
from pathlib import Path

# Patterns that GitHub Secret Scanning detects.
# IMPORTANT: Replacement strings must NOT match the secret patterns themselves,
# otherwise GitHub Push Protection will block this file too.
SECRET_PATTERNS = [
    # Slack Incoming Webhook URLs (replace entire URL with placeholder text)
    (
        r'https://hooks\.slack\.com/services/T[A-Za-z0-9]+/B[A-Za-z0-9]+/[A-Za-z0-9]+',
        '<SLACK_WEBHOOK_URL_PLACEHOLDER>'
    ),
    # Generic Slack webhook URLs
    (
        r'https://hooks\.slack\.com/[^\s"\'<>]+',
        '<SLACK_WEBHOOK_URL_PLACEHOLDER>'
    ),
    # Dynatrace API Tokens (dt0c01. prefix, 24+ chars)
    (
        r'dt0c01\.[A-Z0-9]{24,}\.[A-Z0-9]{64}',
        '<DYNATRACE_API_TOKEN_PLACEHOLDER>'
    ),
    # Dynatrace Internal Tokens
    (
        r'dt0[a-z]\d{2}\.[a-zA-Z0-9_-]{24,}\.[a-zA-Z0-9_-]{64}',
        '<DYNATRACE_TOKEN_PLACEHOLDER>'
    ),
    # Generic Dynatrace token pattern (shorter)
    (
        r'dt0[a-z]\d{2}\.[a-zA-Z0-9_-]{14,}',
        '<DYNATRACE_TOKEN_PLACEHOLDER>'
    ),
    # Google API Keys
    (
        r'AIza[A-Za-z0-9_-]{35}',
        '<GOOGLE_API_KEY_PLACEHOLDER>'
    ),
    # Groq API Keys (gsk_ prefix)
    (
        r'gsk_[A-Za-z0-9]{48,}',
        '<GROQ_API_KEY_PLACEHOLDER>'
    ),
]


def sanitize_file(file_path: Path) -> bool:
    """Sanitize a single file. Returns True if file was modified."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        return False

    original = content
    for pattern, replacement in SECRET_PATTERNS:
        content = re.sub(pattern, replacement, content)

    if content != original:
        file_path.write_text(content, encoding='utf-8')
        return True
    return False


def sanitize_directory(docs_dir: str) -> int:
    """Sanitize all markdown files in directory. Returns count of modified files."""
    path = Path(docs_dir)
    if not path.exists():
        print(f"Directory not found: {docs_dir}")
        return 0

    modified = 0
    files = list(path.rglob('*.md')) + list(path.rglob('*.json'))

    for f in files:
        if sanitize_file(f):
            modified += 1
            print(f"  Sanitized: {f.relative_to(path)}")

    print(f"\nSanitized {modified} files out of {len(files)} total")
    return modified


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Sanitize secrets from scraped docs')
    parser.add_argument('--docs-dir', default='docs', help='Docs directory to sanitize')
    args = parser.parse_args()

    count = sanitize_directory(args.docs_dir)
    print(f"Done. {count} file(s) sanitized.")
    sys.exit(0)
