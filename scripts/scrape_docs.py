#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dynatrace Documentation Scraper
Скачивает всю документацию с docs.dynatrace.com и конвертирует в Markdown
"""

import os
import sys
import json
import time
import hashlib
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

# Configuration
BASE_URL = "https://www.dynatrace.com/support/help/"
OUTPUT_DIR = Path("dynatrace-docs")
CACHE_DIR = OUTPUT_DIR / ".cache"
MAX_PAGES = None  # None = unlimited, or set number for testing
DELAY_SECONDS = 1  # Delay between requests to be polite
TEST_MODE = False  # Set True for testing on small subset

# Create directories
OUTPUT_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

class DynatraceDocScraper:
    def __init__(self, base_url, output_dir, max_pages=None, test_mode=False):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.max_pages = max_pages if not test_mode else 50
        self.test_mode = test_mode
        
        self.visited_urls = set()
        self.to_visit = [base_url]
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Statistics
        self.stats = {
            'pages_downloaded': 0,
            'pages_converted': 0,
            'errors': 0,
            'start_time': datetime.now()
        }
        
        # Load cache
        self.cache_file = CACHE_DIR / "pages_cache.json"
        self.cache = self.load_cache()
    
    def load_cache(self):
        """Load page cache to avoid re-downloading unchanged pages"""
        if self.cache_file.exists():
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_cache(self):
        """Save page cache"""
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, indent=2)
    
    def get_url_hash(self, url):
        """Get hash of URL for caching"""
        return hashlib.md5(url.encode()).hexdigest()
    
    def is_valid_url(self, url):
        """Check if URL should be scraped"""
        parsed = urlparse(url)
        
        # Must be from dynatrace.com
        if 'dynatrace.com' not in parsed.netloc:
            return False
        
        # Must have /docs/ or /support/help/ in path
        if not ('/docs/' in url or '/support/help/' in url):
            return False
        
        # Skip certain paths
        skip_paths = [
            '/blog/', '/community/', '/resources/',
            '/downloads/', '/trial/', '/pricing/',
            'support.dynatrace.com', 'university.dynatrace.com',
            'developer.dynatrace.com'
        ]
        if any(skip in url for skip in skip_paths):
            return False
        
        # Skip anchors and queries
        if '#' in url:
            return False
        
        # Allow queries for now (some docs use them)
        return True
    
    def get_page_content(self, url):
        """Download page content"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")
            self.stats['errors'] += 1
            return None
    
    def extract_links(self, soup, current_url):
        """Extract all valid links from page"""
        links = set()
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(current_url, link['href'])
            if self.is_valid_url(absolute_url):
                links.add(absolute_url)
        return links
    
    def convert_to_markdown(self, html_content, url):
        """Convert HTML to Markdown"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find main content area (adjust selector based on actual Dynatrace docs structure)
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
        
        if not main_content:
            # Fallback to body
            main_content = soup.find('body')
        
        if not main_content:
            return None
        
        # Get title
        title_tag = soup.find('h1') or soup.find('title')
        title = title_tag.get_text().strip() if title_tag else "Untitled"
        
        # Convert to markdown
        markdown = md(str(main_content), heading_style="ATX")
        
        # Add metadata header
        header = f"""---
title: {title}
source: {url}
scraped: {datetime.now().isoformat()}
---

# {title}

"""
        return header + markdown
    
    def get_output_path(self, url):
        """Get output file path for URL"""
        # Parse URL to get the path component
        parsed = urlparse(url)
        path = parsed.path
        
        # Remove leading /docs/ or /support/help/
        if path.startswith('/docs/'):
            relative_path = path[6:]  # Remove '/docs/'
        elif path.startswith('/support/help/'):
            relative_path = path[14:]  # Remove '/support/help/'
        else:
            relative_path = path.strip('/')
        
        # Clean up path
        relative_path = relative_path.strip('/')
        
        # Handle empty path (homepage)
        if not relative_path:
            return self.output_dir / 'index.md'
        
        # Create directory structure
        if '/' in relative_path:
            parts = relative_path.split('/')
            dir_path = self.output_dir / Path(*parts[:-1])
            filename = parts[-1] or 'index'
        else:
            dir_path = self.output_dir
            filename = relative_path or 'index'
        
        # Ensure .md extension
        if not filename.endswith('.md'):
            filename += '.md'
        
        dir_path.mkdir(parents=True, exist_ok=True)
        return dir_path / filename
    
    def scrape_page(self, url):
        """Scrape single page"""
        # Check cache
        url_hash = self.get_url_hash(url)
        
        # Download page
        html_content = self.get_page_content(url)
        if not html_content:
            return None
        
        self.stats['pages_downloaded'] += 1
        
        # Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract links for further crawling
        new_links = self.extract_links(soup, url)
        
        # Convert to Markdown
        markdown = self.convert_to_markdown(html_content, url)
        if not markdown:
            return new_links
        
        # Save to file
        output_path = self.get_output_path(url)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        self.stats['pages_converted'] += 1
        
        # Update cache
        self.cache[url_hash] = {
            'url': url,
            'file': str(output_path),
            'scraped': datetime.now().isoformat()
        }
        
        return new_links
    
    def run(self):
        """Main scraping loop"""
        print("=" * 80)
        print("🚀 DYNATRACE DOCUMENTATION SCRAPER")
        print("=" * 80)
        print()
        print(f"Base URL: {self.base_url}")
        print(f"Output: {self.output_dir}")
        print(f"Max pages: {self.max_pages or 'Unlimited'}")
        print(f"Test mode: {self.test_mode}")
        print()
        
        with tqdm(desc="Scraping", unit=" pages") as pbar:
            while self.to_visit and (self.max_pages is None or self.stats['pages_downloaded'] < self.max_pages):
                url = self.to_visit.pop(0)
                
                if url in self.visited_urls:
                    continue
                
                self.visited_urls.add(url)
                pbar.set_postfix_str(f"Current: {url[-50:]}")
                
                # Scrape page
                new_links = self.scrape_page(url)
                
                if new_links:
                    # Add new links to queue
                    for link in new_links:
                        if link not in self.visited_urls and link not in self.to_visit:
                            self.to_visit.append(link)
                
                pbar.update(1)
                
                # Be polite
                time.sleep(DELAY_SECONDS)
                
                # Save cache periodically
                if self.stats['pages_downloaded'] % 10 == 0:
                    self.save_cache()
        
        # Final cache save
        self.save_cache()
        
        # Print statistics
        self.print_stats()
    
    def print_stats(self):
        """Print scraping statistics"""
        duration = datetime.now() - self.stats['start_time']
        
        print()
        print("=" * 80)
        print("📊 SCRAPING STATISTICS")
        print("=" * 80)
        print(f"✅ Pages downloaded: {self.stats['pages_downloaded']}")
        print(f"✅ Pages converted: {self.stats['pages_converted']}")
        print(f"❌ Errors: {self.stats['errors']}")
        print(f"⏱️  Duration: {duration}")
        print(f"📁 Output directory: {self.output_dir.absolute()}")
        print()
        print(f"Average: {self.stats['pages_downloaded'] / duration.total_seconds():.2f} pages/second")
        print("=" * 80)


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape Dynatrace documentation')
    parser.add_argument('--test', action='store_true', help='Test mode (50 pages)')
    parser.add_argument('--max-pages', type=int, help='Maximum pages to scrape')
    parser.add_argument('--output', default='dynatrace-docs', help='Output directory')
    
    args = parser.parse_args()
    
    scraper = DynatraceDocScraper(
        base_url=BASE_URL,
        output_dir=args.output,
        max_pages=args.max_pages,
        test_mode=args.test
    )
    
    scraper.run()


if __name__ == "__main__":
    main()
