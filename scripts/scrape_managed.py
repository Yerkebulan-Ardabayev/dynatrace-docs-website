#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dynatrace MANAGED Documentation Scraper
Скачивает документацию Managed с фокусом на нужные разделы
"""

import os
import sys
import json
import time
import hashlib
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse
from datetime import datetime
import io

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm

# Encoding fix
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# === КОНФИГУРАЦИЯ ДЛЯ MANAGED ===

# Главные URL для Managed документации
MANAGED_URLS = [
    "https://docs.dynatrace.com/managed",
    "https://docs.dynatrace.com/managed/installation",
    "https://docs.dynatrace.com/managed/configuration", 
    "https://docs.dynatrace.com/managed/operations",
    "https://docs.dynatrace.com/managed/security",
    "https://docs.dynatrace.com/managed/update",
    "https://docs.dynatrace.com/managed/backup",
    "https://docs.dynatrace.com/managed/cluster",
]

# Дополнительные важные разделы (общие для Managed и SaaS)
COMMON_URLS = [
    "https://docs.dynatrace.com/docs/platform/davis-ai",
    "https://docs.dynatrace.com/docs/platform/grail",
    "https://docs.dynatrace.com/docs/observe/infrastructure-observability",
    "https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent",
    "https://docs.dynatrace.com/docs/manage",
]

# SaaS справочно (отдельная папка)
SAAS_URLS = [
    "https://docs.dynatrace.com/docs/discover-dynatrace",
    "https://docs.dynatrace.com/docs/observe",
]

OUTPUT_DIR = Path("../docs")
MANAGED_DIR = OUTPUT_DIR / "managed"
COMMON_DIR = OUTPUT_DIR / "common"  
SAAS_DIR = OUTPUT_DIR / "saas-reference"

DELAY_SECONDS = 1.0
MAX_PAGES_PER_SECTION = 100


class ManagedDocsScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        })
        
        self.visited = set()
        self.stats = {
            'managed': 0,
            'common': 0,
            'saas': 0,
            'errors': 0
        }
    
    def is_managed_url(self, url):
        """Check if URL is from Managed section"""
        return '/managed' in url.lower()
    
    def get_page(self, url):
        """Download page content"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"  ❌ Error: {e}")
            self.stats['errors'] += 1
            return None
    
    def extract_links(self, soup, base_url, section_filter=None):
        """Extract valid documentation links"""
        links = set()
        for a in soup.find_all('a', href=True):
            href = a['href']
            absolute = urljoin(base_url, href)
            
            # Only dynatrace.com docs
            if 'docs.dynatrace.com' not in absolute:
                continue
            
            # Remove anchors
            if '#' in absolute:
                absolute = absolute.split('#')[0]
            
            # Apply section filter
            if section_filter and section_filter not in absolute:
                continue
            
            if absolute not in self.visited:
                links.add(absolute)
        
        return links
    
    def html_to_markdown(self, html, url):
        """Convert HTML to clean Markdown"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find main content
        content = (
            soup.find('main') or 
            soup.find('article') or 
            soup.find('div', {'class': 'content'}) or
            soup.find('div', {'role': 'main'})
        )
        
        if not content:
            content = soup.find('body')
        
        if not content:
            return None
        
        # Get title
        title = "Документация"
        h1 = soup.find('h1')
        if h1:
            title = h1.get_text().strip()
        
        # Convert to markdown
        markdown = md(str(content), heading_style="ATX", strip=['script', 'style', 'nav'])
        
        # Add frontmatter
        result = f"""---
title: "{title}"
source: {url}
updated: {datetime.now().strftime('%Y-%m-%d')}
---

# {title}

{markdown}
"""
        return result
    
    def get_output_path(self, url, base_dir):
        """Get file path for URL"""
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        # Remove common prefixes
        for prefix in ['docs/', 'managed/', 'docs/managed/']:
            if path.startswith(prefix):
                path = path[len(prefix):]
        
        if not path:
            path = 'index'
        
        # Create path
        parts = path.split('/')
        if len(parts) > 1:
            dir_path = base_dir / Path(*parts[:-1])
            filename = parts[-1]
        else:
            dir_path = base_dir
            filename = parts[0]
        
        if not filename.endswith('.md'):
            filename += '.md'
        
        dir_path.mkdir(parents=True, exist_ok=True)
        return dir_path / filename
    
    def scrape_section(self, start_urls, output_dir, section_name, section_filter=None, max_pages=100):
        """Scrape a documentation section"""
        print(f"\n{'='*60}")
        print(f"📚 Скачивание: {section_name}")
        print(f"{'='*60}")
        
        to_visit = deque(start_urls)
        downloaded = 0

        with tqdm(total=max_pages, desc=section_name) as pbar:
            while to_visit and downloaded < max_pages:
                url = to_visit.popleft()
                
                if url in self.visited:
                    continue
                
                self.visited.add(url)
                pbar.set_postfix_str(url[-40:])
                
                html = self.get_page(url)
                if not html:
                    continue
                
                # Convert and save
                markdown = self.html_to_markdown(html, url)
                if markdown:
                    output_path = self.get_output_path(url, output_dir)
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(markdown)
                    downloaded += 1
                    pbar.update(1)
                
                # Extract more links
                soup = BeautifulSoup(html, 'html.parser')
                new_links = self.extract_links(soup, url, section_filter)
                to_visit.extend(new_links)
                
                time.sleep(DELAY_SECONDS)
        
        print(f"✅ Скачано: {downloaded} страниц")
        return downloaded
    
    def run(self):
        """Main scraping process"""
        print("="*60)
        print("🎯 DYNATRACE MANAGED DOCUMENTATION SCRAPER")
        print("="*60)
        print()
        print("Фокус: Managed (главное) + Common + SaaS (справочно)")
        print()
        
        start_time = datetime.now()
        
        # Create directories
        MANAGED_DIR.mkdir(parents=True, exist_ok=True)
        COMMON_DIR.mkdir(parents=True, exist_ok=True)
        SAAS_DIR.mkdir(parents=True, exist_ok=True)
        
        # 1. Scrape Managed (MAIN FOCUS)
        self.stats['managed'] = self.scrape_section(
            MANAGED_URLS, 
            MANAGED_DIR, 
            "MANAGED (Главное)",
            section_filter='managed',
            max_pages=200
        )
        
        # 2. Scrape Common sections
        self.stats['common'] = self.scrape_section(
            COMMON_URLS,
            COMMON_DIR,
            "Общее (OneAgent, Davis AI)",
            max_pages=100
        )
        
        # 3. Scrape SaaS (reference only)
        self.stats['saas'] = self.scrape_section(
            SAAS_URLS,
            SAAS_DIR,
            "SaaS (справочно)",
            max_pages=50
        )
        
        # Print final stats
        duration = datetime.now() - start_time
        print()
        print("="*60)
        print("📊 ИТОГО")
        print("="*60)
        print(f"📁 Managed: {self.stats['managed']} страниц")
        print(f"📁 Общее: {self.stats['common']} страниц")
        print(f"📁 SaaS: {self.stats['saas']} страниц")
        print(f"❌ Ошибок: {self.stats['errors']}")
        print(f"⏱️  Время: {duration}")
        print()
        
        total = self.stats['managed'] + self.stats['common'] + self.stats['saas']
        return total


if __name__ == "__main__":
    scraper = ManagedDocsScraper()
    total = scraper.run()
    print(f"✅ Готово! Скачано {total} страниц")
