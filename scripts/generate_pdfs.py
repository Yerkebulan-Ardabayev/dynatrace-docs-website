#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate PDF files from translated Markdown documentation.

Converts Russian translations to PDF using markdown + weasyprint.
Preserves directory structure in output folder.

Usage:
    python scripts/generate_pdfs.py \
        --report translation_result.json \
        --output-dir pdf-docs

    # Or convert all ru/ docs:
    python scripts/generate_pdfs.py --all --output-dir pdf-docs
"""
import argparse
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RU_DIR = BASE_DIR / "docs" / "ru"

# HTML template for PDF generation with Russian font support
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap');

body {{
    font-family: 'Noto Sans', 'DejaVu Sans', 'Liberation Sans', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
    margin: 2cm;
    max-width: 100%;
}}

h1 {{
    font-size: 20pt;
    color: #1496ff;
    border-bottom: 2px solid #1496ff;
    padding-bottom: 8px;
    margin-top: 0;
}}

h2 {{
    font-size: 16pt;
    color: #1496ff;
    margin-top: 24px;
}}

h3 {{
    font-size: 13pt;
    color: #333;
    margin-top: 18px;
}}

code {{
    background: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 10pt;
}}

pre {{
    background: #f4f4f4;
    padding: 12px;
    border-radius: 6px;
    overflow-x: auto;
    border-left: 3px solid #1496ff;
}}

pre code {{
    background: none;
    padding: 0;
}}

table {{
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
}}

th, td {{
    border: 1px solid #ddd;
    padding: 8px 12px;
    text-align: left;
}}

th {{
    background: #1496ff;
    color: white;
    font-weight: bold;
}}

tr:nth-child(even) {{
    background: #f9f9f9;
}}

blockquote {{
    border-left: 4px solid #1496ff;
    margin: 12px 0;
    padding: 8px 16px;
    background: #f0f8ff;
    color: #555;
}}

a {{
    color: #1496ff;
    text-decoration: none;
}}

.header-meta {{
    color: #888;
    font-size: 9pt;
    margin-bottom: 24px;
}}

@page {{
    size: A4;
    margin: 2cm;
    @bottom-center {{
        content: "Dynatrace Documentation | " counter(page);
        font-size: 8pt;
        color: #999;
    }}
}}
</style>
</head>
<body>
<div class="header-meta">Dynatrace — Документация на русском | {source_path}</div>
{content}
</body>
</html>"""


def md_to_pdf(md_file: Path, pdf_file: Path) -> bool:
    """Convert a Markdown file to PDF. Returns True on success."""
    try:
        import markdown
        from weasyprint import HTML
    except ImportError as e:
        print(f"  ERROR: Missing dependency: {e}")
        print("  Install: pip install markdown weasyprint")
        return False

    try:
        md_content = md_file.read_text(encoding="utf-8")

        # Strip YAML frontmatter
        if md_content.startswith("---"):
            end = md_content.find("---", 3)
            if end > 0:
                md_content = md_content[end + 3:].strip()

        # Convert Markdown to HTML
        html_body = markdown.markdown(
            md_content,
            extensions=["tables", "fenced_code", "toc", "attr_list"],
        )

        # Determine source path for header
        try:
            source_path = str(md_file.relative_to(RU_DIR))
        except ValueError:
            source_path = md_file.name

        full_html = HTML_TEMPLATE.format(content=html_body, source_path=source_path)

        # Generate PDF
        pdf_file.parent.mkdir(parents=True, exist_ok=True)
        HTML(string=full_html).write_pdf(str(pdf_file))
        return True

    except Exception as e:
        print(f"  ERROR generating PDF: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Generate PDFs from translated docs")
    parser.add_argument("--report", help="Path to translation_result.json")
    parser.add_argument("--output-dir", default="pdf-docs",
                        help="Output directory for PDFs")
    parser.add_argument("--all", action="store_true",
                        help="Convert all ru/ docs (not just recently translated)")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)

    # Determine which files to convert
    files_to_convert = []

    if args.all:
        files_to_convert = list(RU_DIR.rglob("*.md"))
    elif args.report:
        report_path = Path(args.report)
        if report_path.exists():
            report = json.load(open(report_path, "r", encoding="utf-8"))
            for rel_path in report.get("translated_files", []):
                ru_file = RU_DIR / rel_path
                if ru_file.exists():
                    files_to_convert.append(ru_file)
        else:
            print(f"Report not found: {report_path}")
            sys.exit(1)
    else:
        print("Specify --report or --all")
        sys.exit(1)

    if not files_to_convert:
        print("No files to convert.")
        return

    print(f"Converting {len(files_to_convert)} files to PDF...")
    print(f"Output: {output_dir}/")
    print()

    success = 0
    failed = 0

    for i, md_file in enumerate(files_to_convert, 1):
        try:
            rel_path = md_file.relative_to(RU_DIR)
        except ValueError:
            rel_path = Path(md_file.name)

        pdf_path = output_dir / rel_path.with_suffix(".pdf")

        print(f"[{i}/{len(files_to_convert)}] {rel_path}", end=" ")

        if md_to_pdf(md_file, pdf_path):
            success += 1
            print("OK")
        else:
            failed += 1
            print("FAILED")

    print()
    print(f"Done: {success} PDFs generated, {failed} failed")
    print(f"Output: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
