"""QA script for L4-IF.30 technology-support language-hub batch.

3 files (per-language support hubs):
- support-model-and-issues.md (114)
- support-model-for-pivotal-platform.md (130)
- serverless-compute-services.md (153)
"""

import pathlib
import re
import sys

FILES = [
    "ingest-from/technology-support/support-model-and-issues.md",
    "ingest-from/technology-support/support-model-for-pivotal-platform.md",
    "ingest-from/technology-support/serverless-compute-services.md",
]

ROOT = pathlib.Path(__file__).resolve().parent.parent
base_en = ROOT / "docs" / "managed"
base_ru = ROOT / "docs" / "managed-ru"

URL_RE = re.compile(r"https?://[^\s)\"\\]+")
CYR_RE = re.compile("[Ѐ-ӿ]")
EN_PHRASE_RE = re.compile(
    r"(?<![\w/`-])[A-Z][a-z]{2,}(?:\s+[A-Za-z][a-z]{2,}){2,}(?![\w`])"
)

total_errors = 0
total_warns = 0
for f in FILES:
    en_text = (base_en / f).read_text(encoding="utf-8")
    ru_text = (base_ru / f).read_text(encoding="utf-8")
    en_lines = en_text.split("\n")
    ru_lines = ru_text.split("\n")
    errors = []
    warns = []

    if len(en_lines) != len(ru_lines):
        errors.append(f"line-parity: EN={len(en_lines)} RU={len(ru_lines)}")

    if "—" in ru_text:
        em_lines = [i + 1 for i, l in enumerate(ru_lines) if "—" in l]
        errors.append(f"em-dash in lines {em_lines[:5]}")

    if ru_text.startswith("﻿"):
        errors.append("BOM at start")
    bad_bom = "ï»¿"
    if bad_bom in ru_text:
        errors.append(f"double-encoded BOM found ({ru_text.count(bad_bom)} times)")

    broken = re.findall(r"â[¦€\"]", ru_text)
    if broken:
        errors.append(f"broken-a mojibake: {len(broken)} occurrences")

    en_urls = sorted(URL_RE.findall(en_text))
    ru_urls = sorted(URL_RE.findall(ru_text))
    if en_urls != ru_urls:
        diff_en = set(en_urls) - set(ru_urls)
        diff_ru = set(ru_urls) - set(en_urls)
        if diff_en or diff_ru:
            errors.append(
                f"URL diff: missing_in_RU={list(diff_en)[:3]} added_in_RU={list(diff_ru)[:3]}"
            )

    if en_text.startswith("---") and ru_text.startswith("---"):
        en_fm = en_text.split("---", 2)[1]
        ru_fm = ru_text.split("---", 2)[1]
        en_keys = set(re.findall(r"^(\w+):", en_fm, re.M))
        ru_keys = set(re.findall(r"^(\w+):", ru_fm, re.M))
        if en_keys != ru_keys:
            errors.append(f"frontmatter keys differ: EN={en_keys} RU={ru_keys}")
        for key in (en_keys & ru_keys) - {"title"}:
            en_v = re.search(rf"^{key}:\s*(.+)$", en_fm, re.M)
            ru_v = re.search(rf"^{key}:\s*(.+)$", ru_fm, re.M)
            if en_v and ru_v and en_v.group(1).strip() != ru_v.group(1).strip():
                errors.append(f"frontmatter {key} changed")

    en_h = [(i, l) for i, l in enumerate(en_lines) if l.startswith("#")]
    ru_h = [(i, l) for i, l in enumerate(ru_lines) if l.startswith("#")]
    if len(en_h) != len(ru_h):
        errors.append(f"heading count: EN={len(en_h)} RU={len(ru_h)}")
    else:
        for (ei, el), (ri, rl) in zip(en_h, ru_h):
            if ei != ri:
                errors.append(f"heading line mismatch L{ei + 1} vs L{ri + 1}")
            en_lvl = len(el) - len(el.lstrip("#"))
            ru_lvl = len(rl) - len(rl.lstrip("#"))
            if en_lvl != ru_lvl:
                errors.append(f"heading level mismatch L{ei + 1}")

    en_fence = en_text.count("```")
    ru_fence = ru_text.count("```")
    if en_fence != ru_fence:
        errors.append(f"code-fence count: EN={en_fence} RU={ru_fence}")

    # EN-leftover scan
    in_code = False
    in_fm = False
    fm_count = 0
    for i, line in enumerate(ru_lines):
        stripped = line.strip()
        if stripped == "---":
            fm_count += 1
            in_fm = fm_count < 2
            continue
        if in_fm:
            continue
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        cleaned = URL_RE.sub("", line)
        cleaned = re.sub(r"`[^`]+`", "", cleaned)
        cleaned = re.sub(r"\*\*[^*]+\*\*", "", cleaned)
        cleaned = re.sub(r"!\[[^\]]*\]", "", cleaned)
        cleaned = re.sub(r"\[[^\]]+\]\([^)]*\)", "", cleaned)
        matches = EN_PHRASE_RE.findall(cleaned)
        has_cyr = bool(CYR_RE.search(line))
        if matches and not has_cyr:
            warns.append(
                f"L{i + 1}: EN-phrase={matches[0][:60]!r} | line: {line.strip()[:100]}"
            )

    status = "PASS" if not errors else "FAIL"
    total_errors += len(errors)
    total_warns += len(warns)
    print(f"\n=== {f.split('/')[-1]} ===")
    print(f"  STATUS: {status}  lines: {len(en_lines)}")
    for e in errors:
        print(f"  ERROR: {e}")
    for w in warns[:30]:
        print(f"  WARN: {w}")
    if len(warns) > 30:
        print(f"  ... +{len(warns) - 30} more warnings")

print(f"\n=== Summary: total_errors={total_errors}, total_warns={total_warns} ===")
sys.exit(1 if total_errors else 0)
