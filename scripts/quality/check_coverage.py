#!/usr/bin/env python3
"""
Translation Coverage Gate.
Checks that the ratio of translated files meets a minimum threshold.
Used as a deploy gate in CI/CD pipeline.

Exit codes:
    0 — coverage >= threshold (deploy allowed)
    1 — coverage < threshold (deploy blocked)
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone


def calculate_coverage(source_dir: Path, target_dir: Path) -> dict:
    """
    Calculate translation coverage by comparing source and target directories.

    Returns dict with:
        total_source:   number of .md files in source
        total_target:   number of .md files in target
        missing:        list of relative paths missing from target
        empty:          list of target files that are nearly empty (<50 chars)
        coverage_pct:   percentage of source files that have a non-empty translation
    """
    source_files = set()
    for f in source_dir.rglob("*.md"):
        source_files.add(f.relative_to(source_dir))

    target_files = set()
    for f in target_dir.rglob("*.md"):
        target_files.add(f.relative_to(target_dir))

    missing = sorted(str(f) for f in source_files - target_files)

    # Check for empty/near-empty translations
    empty = []
    for rel in source_files & target_files:
        target_file = target_dir / rel
        try:
            content = target_file.read_text(encoding="utf-8").strip()
            # Consider files with <50 chars (just frontmatter or placeholder) as empty
            if len(content) < 50:
                empty.append(str(rel))
        except Exception:
            empty.append(str(rel))

    valid_translations = len(source_files) - len(missing) - len(empty)
    total = len(source_files)
    coverage_pct = (valid_translations / total * 100) if total > 0 else 100.0

    return {
        "total_source": total,
        "total_target": len(target_files),
        "valid_translations": valid_translations,
        "missing_count": len(missing),
        "empty_count": len(empty),
        "missing": missing[:50],  # Limit output
        "empty": empty[:20],
        "coverage_pct": round(coverage_pct, 1),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    parser = argparse.ArgumentParser(description="Translation coverage gate")
    parser.add_argument(
        "--threshold",
        type=float,
        default=80.0,
        help="Minimum coverage percentage (default: 80)",
    )
    parser.add_argument(
        "--source-dir",
        default="docs/en",
        help="Source documentation directory (default: docs/en)",
    )
    parser.add_argument(
        "--target-dir",
        default="docs/ru",
        help="Target translation directory (default: docs/ru)",
    )
    parser.add_argument(
        "--report",
        help="Optional: save coverage report as JSON file",
    )
    args = parser.parse_args()

    source_dir = Path(args.source_dir)
    target_dir = Path(args.target_dir)

    if not source_dir.exists():
        print(f"ERROR: Source directory not found: {source_dir}")
        sys.exit(1)

    if not target_dir.exists():
        print(f"WARNING: Target directory not found: {target_dir}")
        print(f"Coverage: 0.0% (threshold: {args.threshold}%)")
        sys.exit(1)

    result = calculate_coverage(source_dir, target_dir)

    # Print report
    print("=" * 60)
    print("TRANSLATION COVERAGE REPORT")
    print("=" * 60)
    print(f"  Source files (en):     {result['total_source']}")
    print(f"  Target files (ru):     {result['total_target']}")
    print(f"  Valid translations:    {result['valid_translations']}")
    print(f"  Missing translations:  {result['missing_count']}")
    print(f"  Empty/broken files:    {result['empty_count']}")
    print(f"  Coverage:              {result['coverage_pct']}%")
    print(f"  Threshold:             {args.threshold}%")
    print("=" * 60)

    if result["missing_count"] > 0:
        print(f"\nMissing files (first {min(50, result['missing_count'])}):")
        for f in result["missing"][:50]:
            print(f"  - {f}")

    if result["empty_count"] > 0:
        print(f"\nEmpty/broken files (first {min(20, result['empty_count'])}):")
        for f in result["empty"][:20]:
            print(f"  - {f}")

    # Save report if requested
    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nReport saved to: {args.report}")

    # Gate decision
    if result["coverage_pct"] >= args.threshold:
        print(f"\nCOVERAGE GATE: PASSED ({result['coverage_pct']}% >= {args.threshold}%)")
        sys.exit(0)
    else:
        print(f"\nCOVERAGE GATE: FAILED ({result['coverage_pct']}% < {args.threshold}%)")
        sys.exit(1)


if __name__ == "__main__":
    main()
