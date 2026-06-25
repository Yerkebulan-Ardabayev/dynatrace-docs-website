# -*- coding: utf-8 -*-
"""L4-IF.62 QA: setup-on-k8s/guides/deployment-and-configuration/
resource-management batch (3 files).
Checks line-parity, frontmatter byte-eq, em-dash=0, mojibake=0, BOM=0,
URL-identity, code-fence byte-identity, heading-level parity, calque/leftover.
Framework copied from _qa_meta_l4if58.py.
"""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management"

# (rel_dir, filename)
FILES = [
    (SUB, "ag-resource-limits.md"),
    (SUB, "dto-resource-limits.md"),
    (SUB, "probe-timeout.md"),
]

CYR = re.compile(r"[А-Яа-яЁё]")
EMDASH = "—"
BOM = "﻿"
MOJI = ["â", "Â", "ï»¿", "â€", "Ã", "’", "‘", "“", "”", "…", "ï", "»", "¿"]
URL_RE = re.compile(r"\]\(([^)\s]+)")
HEAD_RE = re.compile(r"^(#{1,6})\s")
FENCE_RE = re.compile(r"^```")
CAP_PHRASE = re.compile(r"[A-Z][a-z]+(\s+[a-z]+){2,}")
EN_LOWER_RUN = re.compile(r"\b[a-z]+(\s+[a-z]+){3,}\b")

# Full lines that legitimately stay (mostly) English: product/identifier names,
# YAML-key bullets, UI-label steps, code-ish table rows.
ALLOW_EN_LINE = {
    # dto: bare feature-flag/identifier line and product/component headings
    "applicationMonitoring",
    "* **Dynatrace Operator**",
    "* **Webhook**",
    "* **CSI driver**",
    # ag: mode/observability bullets that are product feature names
    "* Kubernetes platform monitoring only",
    # ag: sizing table rows (pure identifiers/numbers, no prose)
    "| < 1000 ( Small ) | requests: 200m(limits: 1000m) | requests: 6Gilimits: 6Gi |",
    "| < 5000 ( Medium ) | requests: 1000m(limits: 2000m) | requests: 10Gi limits: 10Gi |",
    "| < 20000 ( Large ) | requests: 2000m(limits: 4000m) | requests: 12Gi limits: 12Gi |",
    "| < 1000 ( Small ) | requests: 250m(limits: 1000m) | requests: 2Gi limits: 2Gi | 3 |",
    "| < 5000 ( Medium ) | requests: 500m(limits: 2000m) | requests: 4Gi limits: 4Gi | 3 |",
    "| < 20000 ( Large ) | requests: 1000m(limits: 4000m) | requests: 6Gi limits: 6Gi | 6 |",
}


def read(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def urls(text):
    return sorted(URL_RE.findall(text))


def fences(lines):
    return [i for i, l in enumerate(lines) if FENCE_RE.match(l)]


def code_blocks(lines):
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
for rel_dir, rel in FILES:
    en = read(os.path.join(BASE, "managed", rel_dir, rel))
    ru = read(os.path.join(BASE, "managed-ru", rel_dir, rel))
    el, rl = en.split("\n"), ru.split("\n")
    msgs = []

    if len(el) != len(rl):
        msgs.append(("FAIL", f"line-parity EN={len(el)} RU={len(rl)}"))

    for key in ("source:", "scraped:"):
        ev = [l for l in el if l.startswith(key)]
        rv = [l for l in rl if l.startswith(key)]
        if ev != rv:
            msgs.append(("FAIL", f"frontmatter {key} mismatch EN={ev} RU={rv}"))

    n = ru.count(EMDASH)
    if n:
        ln = [i + 1 for i, l in enumerate(rl) if EMDASH in l]
        msgs.append(("FAIL", f"em-dash x{n} at lines {ln}"))

    for m in MOJI:
        if m in ru:
            ln = [i + 1 for i, l in enumerate(rl) if m in l]
            msgs.append(("FAIL", f"mojibake {m!r} at lines {ln}"))
    if BOM in ru:
        msgs.append(("FAIL", "BOM present"))

    if urls(en) != urls(ru):
        only_en = sorted(set(urls(en)) - set(urls(ru)))
        only_ru = sorted(set(urls(ru)) - set(urls(en)))
        msgs.append(("FAIL", f"URL mismatch EN-only={only_en} RU-only={only_ru}"))

    if fences(el) != fences(rl):
        msgs.append(("FAIL", f"fence positions EN={fences(el)} RU={fences(rl)}"))
    if code_blocks(el) != code_blocks(rl):
        msgs.append(("FAIL", "code-block content differs from EN"))

    eh = [HEAD_RE.match(l).group(1) for l in headings(el)]
    rh = [HEAD_RE.match(l).group(1) for l in headings(rl)]
    if eh != rh:
        msgs.append(("FAIL", f"heading levels EN={eh} RU={rh}"))

    for pat in (r"\bвы можете\b", r"\bвы должны\b", r"\bВы можете\b", r"\bВы должны\b"):
        for i, l in enumerate(rl):
            if re.search(pat, l):
                msgs.append(("WARN", f"calque '{pat}' L{i + 1}: {l.strip()[:70]}"))

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
        bare = re.sub(r"\[[^\]]*\]\([^)]*\)", "", l)
        bare = re.sub(r"`[^`]*`", "", bare)
        bare = re.sub(r"https?://\S+", "", bare)
        bare = re.sub(r"[*#>\-+|]", " ", bare).strip()
        if CAP_PHRASE.search(bare) or EN_LOWER_RUN.search(bare):
            msgs.append(("WARN", f"EN-leftover suspect L{i + 1}: {s[:70]}"))

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
