#!/usr/bin/env python3
"""L4-IF.75 unified QA: 30 derived cluster-api files + 8 nav mirrors.

FAIL classes: body line parity, blank positions, fence positions, code blocks
byte-identity, URL sequence identity (vs pending EN), heading count/levels,
em-dash, mojibake/BOM, frontmatter source/updated mismatch.
WARN classes (manual eyeball vs corpus norms): EN-leftover lines, tooltips
without Cyrillic (#9), mixed Cyrillic+5xEN-word runs (#17), ": это" (#11),
quantifier + bare EN noun (#12), non-adjacent modal calque (#10).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "docs" / "managed"
RU = ROOT / "docs" / "managed-ru"

LINK = re.compile(r'\]\(([^)\s]+)(?:\s+"([^"]*)")?\)')
FENCE = re.compile(r"^\s*```")
CYR = re.compile(r"[а-яА-ЯёЁ]")
HEAD = re.compile(r"^(#{1,6})\s")
EN_WORD = re.compile(r"[A-Za-z][A-Za-z'-]+")
QUANT = re.compile(r"\b(два|две|оба|обе|несколько|каждый|каждого|любой из|три) [A-Za-z]")
CALQUE = re.compile(r"\b[Вв]ы(\s+\w+)?\s+(можете|должны|хотите|сможете)\b")

API_FILES = sorted(
    p.relative_to(EN)
    for p in (EN / "managed-cluster/api-references/cluster-api").rglob("*.md")
)
NAV_FILES = [Path(f) for f in [
    "managed.md", "cluster.md", "configuration.md", "backup.md",
    "update.md", "security.md", "operations.md", "installation.md",
]]

# legit kept-EN lines on API pages (corpus norm: ## Endpoint EN 72:3)
ALLOW_EN_LINE = re.compile(
    r"^\s*(## Endpoints?$|#### Curl$|`?/api/|curl |https?://|\| *-+ *\||"
    r"#### The `|\{|\}|\[|\"|[0-9`|* .:-]*$)"
)


def split_fm(t):
    t = t.replace("\r\n", "\n")
    if t.startswith("---"):
        end = t.index("\n---", 3)
        return t[: end + 4].split("\n"), t[end + 4 :].lstrip("\n")
    return [], t


def strip_ignorable(s):
    s = re.sub(r"`[^`]*`", " ", s)          # code spans
    s = LINK.sub(") ", s)                    # link targets/tooltips
    s = re.sub(r"!?\[([^\]]*)\]", r"\1", s)  # link/img text markers
    s = re.sub(r"\*\*[^*]+\*\*", " ", s)     # bold UI labels
    return s


def fences_and_blocks(lines):
    pos, blocks, cur, in_f = [], [], [], False
    for i, l in enumerate(lines):
        if FENCE.match(l):
            pos.append(i)
            if in_f:
                blocks.append("\n".join(cur))
                cur = []
            in_f = not in_f
        elif in_f:
            cur.append(l)
    return pos, blocks


def qa_one(rel, is_nav=False):
    fails, warns = [], []
    en_fm, en_body = split_fm((EN / rel).read_text(encoding="utf-8"))
    ru_fm, ru_body = split_fm((RU / rel).read_text(encoding="utf-8"))
    el, rl = en_body.split("\n"), ru_body.split("\n")

    if len(el) != len(rl):
        fails.append(f"line parity {len(el)} vs {len(rl)}")
        return fails, warns
    for i, (a, b) in enumerate(zip(el, rl)):
        if (not a.strip()) != (not b.strip()):
            fails.append(f"blank mismatch L{i+1}")

    ef, eb = fences_and_blocks(el)
    rf, rb = fences_and_blocks(rl)
    if ef != rf:
        fails.append(f"fence positions differ {ef[:5]} vs {rf[:5]}")
    elif eb != rb:
        for k, (a, b) in enumerate(zip(eb, rb)):
            if a != b:
                fails.append(f"code block #{k+1} differs")

    eu = [m.group(1) for m in LINK.finditer(en_body)]
    ru_u = [m.group(1) for m in LINK.finditer(ru_body)]
    if is_nav:
        if eu != ru_u:
            fails.append("URL sequence differs")
    else:
        # derived files may DROP twin-only links, never add: RU urls must be subset-in-order == EN urls
        if ru_u != eu:
            fails.append(f"URL sequence differs (EN {len(eu)} vs RU {len(ru_u)})")

    eh = [(i, HEAD.match(l).group(1)) for i, l in enumerate(el) if HEAD.match(l)]
    rh = [(i, HEAD.match(l).group(1)) for i, l in enumerate(rl) if HEAD.match(l)]
    if eh != rh:
        fails.append("heading positions/levels differ")

    if "—" in ru_body:
        fails.append("em-dash present")
    for moji in ("ï»¿", "Ã", "Â\xa0", "â€"):
        if moji in ru_body:
            fails.append(f"mojibake {moji!r}")
    if ru_body.startswith("﻿") or "﻿" in ru_body:
        fails.append("BOM char in body")

    for key in ("source:", "updated:", "scraped:"):
        ev = next((l for l in en_fm if l.startswith(key)), None)
        rv = next((l for l in ru_fm if l.startswith(key)), None)
        if ev != rv:
            fails.append(f"frontmatter {key} mismatch")

    in_f = False
    for i, l in enumerate(rl):
        if FENCE.match(l):
            in_f = not in_f
            continue
        if in_f or not l.strip():
            continue
        # tooltip without Cyrillic (#9)
        for m in LINK.finditer(l):
            tt = m.group(2)
            if tt and not CYR.search(tt) and len(tt.split()) >= 2:
                warns.append(f"L{i+1} EN tooltip: {tt[:60]!r}")
        has_cyr = bool(CYR.search(l))
        stripped = strip_ignorable(l)
        words = EN_WORD.findall(stripped)
        if not has_cyr:
            if not ALLOW_EN_LINE.match(l) and len(words) >= 3:
                warns.append(f"L{i+1} EN-leftover: {l.strip()[:90]!r}")
        else:
            runs = re.findall(r"(?:[A-Za-z][A-Za-z'-]+[ ,]+){4,}[A-Za-z][A-Za-z'-]+", stripped)
            if runs:
                warns.append(f"L{i+1} mixed EN-run: {runs[0][:70]!r}")
            if ": это " in l:
                warns.append(f"L{i+1} ': это'")
            if QUANT.search(l):
                warns.append(f"L{i+1} quantifier+EN: {QUANT.search(l).group(0)!r}")
            if CALQUE.search(l):
                warns.append(f"L{i+1} calque: {CALQUE.search(l).group(0)!r}")
    return fails, warns


def main():
    total_f = total_w = 0
    for rel in list(API_FILES) + NAV_FILES:
        fails, warns = qa_one(rel, is_nav=rel in NAV_FILES)
        total_f += len(fails)
        total_w += len(warns)
        if fails or warns:
            print(f"== {rel}")
            for f in fails:
                print(f"  FAIL {f}")
            for w in warns:
                print(f"  WARN {w}")
    print(f"\nfiles={len(API_FILES)+len(NAV_FILES)} FAIL={total_f} WARN={total_w}")
    sys.exit(1 if total_f else 0)


if __name__ == "__main__":
    main()
