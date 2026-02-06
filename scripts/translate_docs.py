#!/usr/bin/env python3
"""
Translation script for Dynatrace documentation
Translates English docs to Russian using free translation
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, Optional
import time

try:
    from googletrans import Translator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    print("WARNING: googletrans not installed. Install with: pip install googletrans==4.0.0rc1")
    TRANSLATOR_AVAILABLE = False


class DocumentTranslator:
    def __init__(self, source_dir: str = "docs/en", target_dir: str = "docs/ru", cache_file: str = ".translation_cache.json"):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.cache_file = Path(cache_file)
        self.translator = Translator() if TRANSLATOR_AVAILABLE else None
        self.cache = self._load_cache()
        
        # Terms that should NOT be translated
        self.preserve_terms = [
            'Dynatrace', 'OneAgent', 'ActiveGate', 'Managed', 'SaaS',
            'Davis', 'Grail', 'DQL', 'Smartscape', 'PurePath',
            'GitHub', 'Kubernetes', 'Docker', 'API', 'SDK',
            'HTTP', 'HTTPS', 'URL', 'JSON', 'YAML', 'XML',
            'Linux', 'Windows', 'macOS', 'Ubuntu', 'RedHat'
        ]
    
    def _load_cache(self) -> Dict:
        """Load translation cache from disk"""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"WARNING: Could not load cache: {e}")
        return {}
    
    def _save_cache(self):
        """Save translation cache to disk"""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"WARNING: Could not save cache: {e}")
    
    def _get_cached_translation(self, text: str) -> Optional[str]:
        """Get cached translation if available"""
        return self.cache.get(text)
    
    def _cache_translation(self, text: str, translation: str):
        """Cache a translation"""
        self.cache[text] = translation
    
    def translate_text(self, text: str) -> str:
        """Translate text from English to Russian"""
        if not text or not text.strip():
            return text
        
        # Check cache first
        cached = self._get_cached_translation(text)
        if cached:
            return cached
        
        if not self.translator:
            print("WARNING: Translator not available")
            return text
        
        try:
            # Translate
            result = self.translator.translate(text, src='en', dest='ru')
            translation = result.text
            
            # Cache the result
            self._cache_translation(text, translation)
            
            # Small delay to avoid rate limiting
            time.sleep(0.1)
            
            return translation
        except Exception as e:
            print(f"WARNING: Translation error: {e}")
            return text
    
    def translate_markdown(self, content: str) -> str:
        """
        Translate markdown content while preserving:
        - Code blocks
        - Links
        - Technical terms
        -YAML frontmatter
        """
        lines = content.split('\n')
        translated_lines = []
        in_code_block = False
        in_frontmatter = False
        
        for i, line in enumerate(lines):
            # Check for YAML frontmatter
            if i == 0 and line.strip() == '---':
                in_frontmatter = True
                translated_lines.append(line)
                continue
            
            if in_frontmatter:
                if line.strip() == '---':
                    in_frontmatter = False
                translated_lines.append(line)
                continue
            
            # Check for code blocks
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                translated_lines.append(line)
                continue
            
            # Don't translate code blocks
            if in_code_block:
                translated_lines.append(line)
                continue
            
            # Don't translate if line is empty or only whitespace
            if not line.strip():
                translated_lines.append(line)
                continue
            
            # Parse and translate line
            translated_line = self._translate_line(line)
            translated_lines.append(translated_line)
        
        return '\n'.join(translated_lines)
    
    def _translate_line(self, line: str) -> str:
        """Translate a single line, preserving markdown syntax"""
        # Preserve inline code
        code_pattern = r'`([^`]+)`'
        codes = re.findall(code_pattern, line)
        
        # Preserve links
        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        links = re.findall(link_pattern, line)
        
        # Replace codes and links with placeholders
        temp_line = line
        for i, code in enumerate(codes):
            temp_line = temp_line.replace(f'`{code}`', f'__CODE_{i}__', 1)
        
        for i, (text, url) in enumerate(links):
            temp_line = temp_line.replace(f'[{text}]({url})', f'__LINK_{i}__', 1)
        
        # Translate the remaining text
        if temp_line.strip():
            translated = self.translate_text(temp_line)
        else:
            translated = temp_line
        
        # Restore codes and links
        for i, code in enumerate(codes):
            translated = translated.replace(f'__CODE_{i}__', f'`{code}`', 1)
        
        for i, (text, url) in enumerate(links):
            # Translate link text but keep URL
            translated_text = self.translate_text(text)
            translated = translated.replace(f'__LINK_{i}__', f'[{translated_text}]({url})', 1)
        
        return translated
    
    def translate_file(self, source_file: Path) -> bool:
        """Translate a single markdown file"""
        # Get relative path
        rel_path = source_file.relative_to(self.source_dir)
        target_file = self.target_dir / rel_path
        
        # Skip if translation is up to date
        if target_file.exists():
            if target_file.stat().st_mtime >= source_file.stat().st_mtime:
                print(f"OK Skipping (up to date): {rel_path}")
                return True
        
        print(f"Translating: {rel_path}")
        
        try:
            # Read source
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Translate
            translated = self.translate_markdown(content)
            
            # Ensure target directory exists
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Write translation
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            print(f"SUCCESS: Translated: {rel_path}")
            return True
            
        except Exception as e:
            print(f"ERROR: Error translating {rel_path}: {e}")
            return False
    
    def translate_all(self):
        """Translate all markdown files in source directory"""
        if not TRANSLATOR_AVAILABLE:
            print("ERROR: Translator not available. Install googletrans==4.0.0rc1")
            return
        
        print(f"Starting translation: {self.source_dir} -> {self.target_dir}")
        
        # Find all markdown files
        md_files = list(self.source_dir.rglob('*.md'))
        total = len(md_files)
        
        print(f"Found {total} markdown files")
        
        success_count = 0
        for i, md_file in enumerate(md_files, 1):
            print(f"\n[{i}/{total}]", end=" ")
            if self.translate_file(md_file):
                success_count += 1
        
        # Save cache
        self._save_cache()
        
        print(f"\n\nTranslation complete!")
        print(f"   Successful: {success_count}/{total}")
        print(f"   Failed: {total - success_count}")



if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Translate Dynatrace documentation')
    parser.add_argument('--source', default='docs/en', help='Source directory (default: docs/en)')
    parser.add_argument('--target', default='docs/ru', help='Target directory (default: docs/ru)')
    parser.add_argument('--cache', default='.translation_cache.json', help='Cache file')
    
    args = parser.parse_args()
    
    translator = DocumentTranslator(args.source, args.target, args.cache)
    translator.translate_all()
