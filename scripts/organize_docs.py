#!/usr/bin/env python3
"""
Organize scraped documentation into proper MkDocs structure
Separates Managed docs from general docs
"""

import shutil
from pathlib import Path
import re


def organize_docs(source_dir: str = "../dynatrace-link-finder/dynatrace-docs", target_en: str = "docs/en"):
    """Organize scraped docs into MkDocs structure"""
    source = Path(source_dir)
    target = Path(target_en)
    
    if not source.exists():
        print(f"❌ Source directory not found: {source}")
        return
    
    print(f"Organizing documentation...")
    print(f"   Source: {source}")
    print(f"   Target: {target}")
    
    # Create target directory
    target.mkdir(parents=True, exist_ok=True)
    
    # Find all markdown files
    md_files = list(source.rglob('*.md'))
    total = len(md_files)
    
    print(f"\nFound {total} markdown files")
    
    managed_count = 0
    general_count = 0
    
    for md_file in md_files:
        rel_path = md_file.relative_to(source)
        
        # Check if this is a Managed doc
        is_managed = _is_managed_doc(md_file)
        
        if is_managed:
            # Move to managed subfolder
            target_path = target / 'managed' / rel_path
            managed_count += 1
        else:
            # Move to general docs
            target_path = target / rel_path
            general_count += 1
        
        # Create parent directory
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy file
        shutil.copy2(md_file, target_path)
    
    print(f"\nOrganization complete!")
    print(f"   Managed docs: {managed_count}")
    print(f"   General docs: {general_count}")
    print(f"   Total: {total}")


def _is_managed_doc(file_path: Path) -> bool:
    """Check if document is about Dynatrace Managed"""
    # Check file path
    path_str = str(file_path).lower()
    if 'managed' in path_str:
        return True

    # Check file content (scan 3000 chars for better detection)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(3000)

        content_lower = content.lower()

        # Check source URL in frontmatter (most reliable signal)
        source_match = re.search(r'source:\s*(https?://\S+)', content)
        if source_match:
            source_url = source_match.group(1).lower()
            if '/managed' in source_url or 'docs.dynatrace.com/managed' in source_url:
                return True

        # Keywords that indicate Managed documentation
        managed_keywords = [
            'dynatrace managed',
            'managed deployment',
            'managed cluster',
            'managed installation',
            'on-premises deployment',
            'self-hosted',
            'cluster management console',
            'mission control',
            'managed node',
            'cluster node',
            'managed server',
        ]

        for keyword in managed_keywords:
            if keyword in content_lower:
                return True

    except Exception as e:
        print(f"⚠️ Could not read {file_path}: {e}")

    return False


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Organize scraped documentation')
    parser.add_argument('--source', default='../dynatrace-link-finder/dynatrace-docs', 
                       help='Source directory with scraped docs')
    parser.add_argument('--target', default='docs/en',
                       help='Target English docs directory')
    
    args = parser.parse_args()
    
    organize_docs(args.source, args.target)
