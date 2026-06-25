# -*- coding: utf-8 -*-
"""L4-IF.33 QA: setup-on-k8s/how-it-works batch (6 files).
Checks line-parity, frontmatter byte-eq, em-dash=0, mojibake=0, URL-identity,
code-fence byte-identity, heading parity, calque/leftover scans.
Reuses framework of _qa_l4if32.py + enhanced EN-leftover detectors (L4-IF.32).
"""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/how-it-works"
FILES = [
    "kubernetes-monitoring.md",
    "cloud-native-fullstack.md",
    "application-monitoring.md",
    "other-deployment-modes/classic-fullstack.md",
    "other-deployment-modes/host-monitoring.md",
    "components/dynatrace-operator.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
EMDASH = "—"
ENDASH = "–"
BOM = "﻿"
MOJI = ["â", "Â", "ï»¿", "â€", "Ã", "’", "‘", "“", "”", "…"]
URL_RE = re.compile(r"\]\(([^)\s]+)")  # link/image targets
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")  # image srcs (subset)
HEAD_RE = re.compile(r"^(#{1,6})\s")
FENCE_RE = re.compile(r"^```")
# EN-leftover detectors (L4-IF.32)
CAP_PHRASE = re.compile(r"[A-Z][a-z]+(\s+[a-z]+){2,}")  # Capitalized + 2+ lc words
EN_LOWER_RUN = re.compile(
    r"\b[a-z]+(\s+[a-z]+){3,}\b"
)  # 4+ lowercase EN words in a row

# legit EN terms that may appear alone on a line / in prose (not leftovers)
ALLOW_EN_LINE = {
    "# Dynatrace Operator",
    "## Operator",
    "## Webhook",
    "## CSI driver",
    "k8s-monitoring",
    "cloud-native",
    "host-monitoring",
    "classic-full-stack",
    "auto-injection",
    "diagram title",
    "Container build-time injection",
    "# Full-stack observability",
    "# Application observability",
    "# Classic Full-Stack monitoring",
    "# Host monitoring",
    "title: Dynatrace Operator",
    "title: Full-stack observability",
    "title: Application observability",
    "title: Classic Full-Stack monitoring",
    "title: Host monitoring",
}


def read(p):
    # Normalize CRLF->LF: repo index is LF (core.autocrlf=true); working-tree
    # CRLF on EN is a checkout artifact, not a content difference.
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def urls(text):
    return sorted(URL_RE.findall(text))


def fences(lines):
    return [i for i, l in enumerate(lines) if FENCE_RE.match(l)]


def code_blocks(lines):
    """return list of (content lines) inside ``` ... ``` blocks"""
    blocks, inb, cur = [], False, []
    for l in lines:
        if FENCE_RE.match(l):
            if inb:
                blocks.append(cur)
                cur = []
            inb = not inb
            continue
        if inb:
            cur.append(l)
    return blocks


def headings(lines):
    return [l for l in lines if HEAD_RE.match(l)]


total_warn = 0
total_fail = 0
for rel in FILES:
    en = read(os.path.join(BASE, "managed", SUB, rel))
    ru = read(os.path.join(BASE, "managed-ru", SUB, rel))
    el, rl = en.split("\n"), ru.split("\n")
    msgs = []

    # 1 line parity
    if len(el) != len(rl):
        msgs.append(("FAIL", f"line-parity EN={len(el)} RU={len(rl)}"))

    # 2 frontmatter source/scraped byte-eq
    for key in ("source:", "scraped:"):
        ev = [l for l in el if l.startswith(key)]
        rv = [l for l in rl if l.startswith(key)]
        if ev != rv:
            msgs.append(("FAIL", f"frontmatter {key} mismatch EN={ev} RU={rv}"))

    # 3 em-dash
    n = ru.count(EMDASH)
    if n:
        ln = [i + 1 for i, l in enumerate(rl) if EMDASH in l]
        msgs.append(("FAIL", f"em-dash x{n} at lines {ln}"))

    # 4 mojibake / BOM
    for m in MOJI:
        if m in ru:
            ln = [i + 1 for i, l in enumerate(rl) if m in l]
            msgs.append(("FAIL", f"mojibake {m!r} at lines {ln}"))
    if BOM in ru:
        msgs.append(("FAIL", "BOM present"))

    # 5 URL identity
    if urls(en) != urls(ru):
        only_en = sorted(set(urls(en)) - set(urls(ru)))
        only_ru = sorted(set(urls(ru)) - set(urls(en)))
        msgs.append(("FAIL", f"URL mismatch EN-only={only_en} RU-only={only_ru}"))

    # 6 code-fence parity + byte-identical block content
    if fences(el) != fences(rl):
        msgs.append(("FAIL", f"fence positions EN={fences(el)} RU={fences(rl)}"))
    if code_blocks(el) != code_blocks(rl):
        msgs.append(("FAIL", "code-block content differs from EN"))

    # 7 heading parity (count + level structure)
    eh = [HEAD_RE.match(l).group(1) for l in headings(el)]
    rh = [HEAD_RE.match(l).group(1) for l in headings(rl)]
    if eh != rh:
        msgs.append(("FAIL", f"heading levels EN={eh} RU={rh}"))

    # 8 calque check
    for pat in (r"\bвы можете\b", r"\bвы должны\b", r"\bВы можете\b"):
        for i, l in enumerate(rl):
            if re.search(pat, l):
                msgs.append(("WARN", f"calque '{pat}' L{i + 1}: {l.strip()[:70]}"))

    # 9 EN-leftover scan (skip code blocks, urls-only, allowed EN lines/terms)
    inb = False
    for i, l in enumerate(rl):
        if FENCE_RE.match(l):
            inb = not inb
            continue
        if inb:
            continue
        s = l.strip()
        if not s or s in ALLOW_EN_LINE:
            continue
        if CYR.search(l):
            continue
        # line has zero Cyrillic: strip md/url/code then test for EN prose
        bare = re.sub(r"\[[^\]]*\]\([^)]*\)", "", l)  # links
        bare = re.sub(r"`[^`]*`", "", bare)  # inline code
        bare = re.sub(r"https?://\S+", "", bare)  # bare urls
        bare = re.sub(r"[*#>\-+|]", " ", bare).strip()
        if CAP_PHRASE.search(bare) or EN_LOWER_RUN.search(bare):
            msgs.append(("WARN", f"EN-leftover suspect L{i + 1}: {s[:70]}"))

    # report
    fails = [m for t, m in msgs if t == "FAIL"]
    warns = [m for t, m in msgs if t == "WARN"]
    total_fail += len(fails)
    total_warn += len(warns)
    status = "PASS" if not fails else "FAIL"
    print(f"[{status}] {rel}  (lines {len(rl)}, warns {len(warns)})")
    for t, m in msgs:
        print(f"    [{t}] {m}")

print(
    f"\n=== TOTAL: {total_fail} FAIL, {total_warn} WARN across {len(FILES)} files ==="
)
