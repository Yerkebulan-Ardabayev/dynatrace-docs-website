#!/usr/bin/env python3
"""
NotebookLM Auto-Sync Agent
===========================
Automated pipeline: Markdown -> PDF -> NotebookLM upload.
After docs are updated/translated, this script:
1. Merges markdown files by topic into PDFs
2. Uploads PDFs to NotebookLM via CLI
3. If notebook is full (source limit), creates a new notebook
4. Registers new notebooks in Claude Code library

Usage (PowerShell):
    python notebooklm-sync.py                    # Full sync
    python notebooklm-sync.py --upload-only      # Skip PDF conversion, just upload
    python notebooklm-sync.py --convert-only     # Only convert MD to PDF
    python notebooklm-sync.py --dry-run          # Preview what would happen
    python notebooklm-sync.py --notebook-url URL # Upload to specific notebook
"""

import os
import sys
import json
import subprocess
import argparse
import hashlib
import re
from pathlib import Path
from datetime import datetime

# ============================================================
# CONFIGURATION - edit these to match your setup
# ============================================================
SCRIPT_DIR = Path(__file__).parent.resolve()
DOCS_DIR = SCRIPT_DIR / "docs"
PDF_OUTPUT_DIR = SCRIPT_DIR / "notebooklm-pdfs"
STATE_FILE = SCRIPT_DIR / "notebooklm-pdfs" / ".sync_state.json"

# NotebookLM limits
MAX_SOURCES_PER_NOTEBOOK = 290  # Leave buffer (limit is 300)
MAX_FILE_SIZE_MB = 50  # NotebookLM file size limit

# Default notebook URLs - add yours here
DEFAULT_NOTEBOOKS = {
    "dynatrace-docs": "https://notebooklm.google.com/notebook/69555b82-2e88-4295-99fd-4cf405151883",
    "dynatrace-managed": "https://notebooklm.google.com/notebook/b7bff042-3c4f-49a5-8026-c178e1340a85",
}

# Topic grouping rules
TOPIC_DIRS = {
    "managed": "Managed",
    "managed-ru": "Managed-RU",
    "common": "Common",
    "ru": "RU",
    "en": "EN",
}


# ============================================================
# STATE MANAGEMENT
# ============================================================
def load_state():
    """Load sync state (tracks what's already uploaded)."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding='utf-8'))
    return {
        "last_sync": None,
        "uploaded_files": {},  # filename -> {hash, notebook_url, upload_date}
        "notebooks": {},      # url -> {name, source_count, created_date}
    }

def save_state(state):
    """Save sync state."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state["last_sync"] = datetime.now().isoformat()
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding='utf-8')

def file_hash(filepath):
    """Get MD5 hash of file to detect changes."""
    h = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


# ============================================================
# MARKDOWN TO PDF CONVERSION
# ============================================================
def convert_md_to_pdf(docs_dir, output_dir):
    """Convert markdown files to PDFs grouped by topic."""
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
        from reportlab.lib.enums import TA_LEFT
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except ImportError:
        print("ERROR: reportlab not installed. Run: pip install reportlab")
        return []

    # Font setup
    FONT_NAME = 'Helvetica'
    for font_path in [
        'C:/Windows/Fonts/arial.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont('CustomFont', font_path))
                FONT_NAME = 'CustomFont'
                bold_path = font_path.replace('.ttf', 'bd.ttf').replace('DejaVuSans.ttf', 'DejaVuSans-Bold.ttf')
                if os.path.exists(bold_path):
                    pdfmetrics.registerFont(TTFont('CustomFont-Bold', bold_path))
            except Exception:
                pass
            break

    output_dir.mkdir(parents=True, exist_ok=True)
    created_pdfs = []

    # Collect topics
    topics = {}
    for dir_name, prefix in TOPIC_DIRS.items():
        topic_dir = docs_dir / dir_name
        if not topic_dir.exists():
            continue
        for subdir in sorted(topic_dir.iterdir()):
            if subdir.is_dir():
                files = sorted(subdir.rglob('*.md'))
                if files:
                    topic_key = f"{prefix}-{subdir.name}"
                    topics[topic_key] = files
            elif subdir.suffix == '.md':
                topic_key = f"{prefix}-root"
                topics.setdefault(topic_key, []).append(subdir)

    print(f"\nFound {len(topics)} topics, converting to PDF...")

    for topic, md_files in sorted(topics.items()):
        output_file = output_dir / f"{topic}.pdf"

        # Build PDF
        try:
            styles = getSampleStyleSheet()
            doc = SimpleDocTemplate(str(output_file), pagesize=A4,
                                    topMargin=15*mm, bottomMargin=15*mm,
                                    leftMargin=15*mm, rightMargin=15*mm)
            story = []

            # Title
            story.append(Spacer(1, 30))
            title_text = f"Dynatrace: {topic}"
            title_text = title_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            story.append(Paragraph(title_text, styles['Title']))
            story.append(Paragraph(
                f"{len(md_files)} documents | Generated {datetime.now().strftime('%Y-%m-%d')}",
                styles['Normal']))
            story.append(PageBreak())

            for i, md_file in enumerate(md_files):
                try:
                    content = md_file.read_text(encoding='utf-8', errors='ignore')
                    # Clean for reportlab
                    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
                    content = re.sub(r'\[([^\]]*)\]\([^\)]*\)', r'\1', content)
                    content = re.sub(r'<[^>]+>', '', content)
                    content = content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

                    # Skip frontmatter
                    lines = content.split('\n')
                    if lines and lines[0].strip() == '---':
                        for j in range(1, len(lines)):
                            if lines[j].strip() == '---':
                                lines = lines[j+1:]
                                break

                    rel_path = str(md_file.relative_to(docs_dir))
                    safe_path = rel_path.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    story.append(Paragraph(f"Source: {safe_path}", styles['Heading2']))
                    story.append(Spacer(1, 6))

                    # Add content as paragraphs
                    para_text = []
                    for line in lines:
                        line = line.strip()
                        if not line:
                            if para_text:
                                text = ' '.join(para_text)
                                try:
                                    story.append(Paragraph(text, styles['Normal']))
                                except Exception:
                                    pass
                                para_text = []
                            continue

                        heading_match = re.match(r'^(#{1,6})\s+(.+)', line)
                        if heading_match:
                            if para_text:
                                text = ' '.join(para_text)
                                try:
                                    story.append(Paragraph(text, styles['Normal']))
                                except Exception:
                                    pass
                                para_text = []
                            level = min(len(heading_match.group(1)), 3)
                            heading_styles = {1: 'Heading1', 2: 'Heading2', 3: 'Heading3'}
                            try:
                                story.append(Paragraph(heading_match.group(2), styles[heading_styles[level]]))
                            except Exception:
                                pass
                        elif line.startswith('```'):
                            continue
                        else:
                            para_text.append(line)

                    if para_text:
                        text = ' '.join(para_text)
                        try:
                            story.append(Paragraph(text, styles['Normal']))
                        except Exception:
                            pass

                    if i < len(md_files) - 1:
                        story.append(PageBreak())
                except Exception as e:
                    print(f"  Warning: skipped {md_file.name}: {e}")

            doc.build(story)
            size_mb = output_file.stat().st_size / (1024*1024)
            print(f"  {topic}.pdf ({len(md_files)} files, {size_mb:.1f} MB)")
            created_pdfs.append(output_file)

        except Exception as e:
            print(f"  ERROR creating {topic}.pdf: {e}")

    print(f"\nCreated {len(created_pdfs)} PDFs in {output_dir}")
    return created_pdfs


# ============================================================
# NOTEBOOKLM UPLOAD
# ============================================================
def get_notebook_source_count(notebook_url):
    """Try to get source count for a notebook."""
    # This would need notebooklm CLI or API
    # For now return from state
    return 0

def upload_to_notebooklm(pdf_files, notebook_url, state, dry_run=False):
    """Upload PDF files to NotebookLM using CLI."""
    uploaded = []
    failed = []

    for pdf_file in pdf_files:
        fname = pdf_file.name
        current_hash = file_hash(pdf_file)

        # Check if already uploaded and unchanged
        if fname in state["uploaded_files"]:
            if state["uploaded_files"][fname]["hash"] == current_hash:
                print(f"  SKIP (unchanged): {fname}")
                continue

        size_mb = pdf_file.stat().st_size / (1024*1024)
        if size_mb > MAX_FILE_SIZE_MB:
            print(f"  SKIP (too large {size_mb:.1f}MB): {fname}")
            failed.append(fname)
            continue

        if dry_run:
            print(f"  DRY-RUN would upload: {fname} ({size_mb:.1f} MB)")
            continue

        print(f"  Uploading: {fname} ({size_mb:.1f} MB)...", end=' ')
        sys.stdout.flush()

        try:
            result = subprocess.run(
                ['notebooklm', 'source', 'add', str(pdf_file),
                 '--notebook', notebook_url],
                capture_output=True, text=True, timeout=120
            )

            if result.returncode == 0:
                print("OK")
                state["uploaded_files"][fname] = {
                    "hash": current_hash,
                    "notebook_url": notebook_url,
                    "upload_date": datetime.now().isoformat(),
                    "size_mb": round(size_mb, 2)
                }
                uploaded.append(fname)
                save_state(state)
            else:
                error_msg = result.stderr.strip() or result.stdout.strip()
                print(f"FAILED: {error_msg[:100]}")
                failed.append(fname)

                # Check if notebook is full
                if 'limit' in error_msg.lower() or 'full' in error_msg.lower():
                    print("\n  Notebook appears full! Need to create a new one.")
                    return uploaded, failed, True  # Signal: need new notebook

        except subprocess.TimeoutExpired:
            print("TIMEOUT")
            failed.append(fname)
        except FileNotFoundError:
            print("\n  ERROR: 'notebooklm' CLI not found!")
            print("  Install it: pip install 'notebooklm-py[browser]'")
            return uploaded, failed, False

    return uploaded, failed, False


def create_new_notebook(name):
    """Create a new NotebookLM notebook via CLI."""
    try:
        result = subprocess.run(
            ['notebooklm', 'create', name],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            # Parse notebook URL from output
            output = result.stdout.strip()
            url_match = re.search(r'https://notebooklm\.google\.com/notebook/[a-f0-9-]+', output)
            if url_match:
                return url_match.group(0)
            print(f"  Created notebook but couldn't parse URL from: {output}")
        else:
            print(f"  Failed to create notebook: {result.stderr}")
    except Exception as e:
        print(f"  Error creating notebook: {e}")
    return None


def register_in_claude_code(notebook_url, name, topics_list):
    """Register notebook in Claude Code's MCP library."""
    # Write to the library.json used by notebooklm MCP
    library_paths = [
        Path.home() / '.local' / 'share' / 'notebooklm-mcp' / 'library.json',
        Path.home() / '.claude' / 'skills' / 'notebooklm' / 'data' / 'library.json',
    ]

    for lib_path in library_paths:
        try:
            if lib_path.exists():
                library = json.loads(lib_path.read_text(encoding='utf-8'))
            else:
                lib_path.parent.mkdir(parents=True, exist_ok=True)
                library = {"notebooks": []}

            # Check if already exists
            existing = [n for n in library.get("notebooks", []) if n.get("url") == notebook_url]
            if existing:
                print(f"  Already registered in {lib_path}")
                continue

            # Add new entry
            notebook_id = name.lower().replace(' ', '-')[:30]
            library.setdefault("notebooks", []).append({
                "id": notebook_id,
                "url": notebook_url,
                "name": name,
                "description": f"Auto-synced Dynatrace documentation: {name}",
                "topics": topics_list,
                "use_cases": ["Dynatrace documentation queries", "Technical reference"],
                "added_date": datetime.now().isoformat()
            })

            lib_path.write_text(json.dumps(library, indent=2, ensure_ascii=False), encoding='utf-8')
            print(f"  Registered in Claude Code library: {lib_path}")
        except Exception as e:
            print(f"  Warning: couldn't update {lib_path}: {e}")


# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description='NotebookLM Auto-Sync Agent')
    parser.add_argument('--convert-only', action='store_true', help='Only convert MD to PDF')
    parser.add_argument('--upload-only', action='store_true', help='Only upload existing PDFs')
    parser.add_argument('--dry-run', action='store_true', help='Preview without changes')
    parser.add_argument('--notebook-url', help='Upload to specific notebook URL')
    parser.add_argument('--force', action='store_true', help='Re-upload even if unchanged')
    args = parser.parse_args()

    print("=" * 60)
    print("  NotebookLM Auto-Sync Agent")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    state = load_state()

    if args.force:
        state["uploaded_files"] = {}

    # Step 1: Convert MD to PDF
    if not args.upload_only:
        print("\n[STEP 1] Converting Markdown to PDF...")
        pdf_files = convert_md_to_pdf(DOCS_DIR, PDF_OUTPUT_DIR)
    else:
        pdf_files = sorted(PDF_OUTPUT_DIR.glob('*.pdf'))
        print(f"\n[STEP 1] Skipped conversion. Found {len(pdf_files)} existing PDFs.")

    if not pdf_files:
        print("No PDFs to upload. Done.")
        return

    # Step 2: Upload to NotebookLM
    if not args.convert_only:
        print("\n[STEP 2] Uploading to NotebookLM...")

        notebook_url = args.notebook_url or DEFAULT_NOTEBOOKS.get("dynatrace-docs")
        if not notebook_url:
            print("ERROR: No notebook URL specified. Use --notebook-url or edit DEFAULT_NOTEBOOKS")
            return

        uploaded, failed, need_new = upload_to_notebooklm(
            pdf_files, notebook_url, state, args.dry_run
        )

        # If notebook is full, create new one
        if need_new and not args.dry_run:
            print("\n[STEP 2b] Creating new notebook...")
            timestamp = datetime.now().strftime('%Y%m%d')
            new_name = f"Dynatrace Docs Overflow {timestamp}"
            new_url = create_new_notebook(new_name)

            if new_url:
                print(f"  New notebook: {new_url}")
                # Register in Claude Code
                register_in_claude_code(new_url, new_name,
                    ["Dynatrace", "monitoring", "observability", "documentation"])
                # Upload remaining files
                remaining = [f for f in pdf_files if f.name not in
                    [u for u in uploaded] and f.name not in failed]
                if remaining:
                    upload_to_notebooklm(remaining, new_url, state, args.dry_run)

        print(f"\n  Uploaded: {len(uploaded)}")
        print(f"  Failed: {len(failed)}")
        print(f"  Skipped (unchanged): {len(pdf_files) - len(uploaded) - len(failed)}")

    save_state(state)

    print("\n" + "=" * 60)
    print("  Sync complete!")
    print("=" * 60)
    print(f"\n  PDFs: {PDF_OUTPUT_DIR}")
    print(f"  State: {STATE_FILE}")
    if state.get("last_sync"):
        print(f"  Last sync: {state['last_sync']}")


if __name__ == '__main__':
    main()
