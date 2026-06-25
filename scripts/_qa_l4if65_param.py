# -*- coding: utf-8 -*-
"""L4-IF.64 UNIFIED QA (5 reference files); +hyphenated-identifier drop in EN-leftover scan.
Based on L4-IF.63 QA: 18 setup-on-k8s files (deployment 16 + extend-observability-k8s 2).
Trustworthy final gate. Same engine as _qa_l4if62_all.py (strip-aware fence, » excluded
from mojibake). Full rel paths under docs/managed[-ru]/.
"""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")

FILES = [
    "ingest-from/setup-on-k8s/reference/dynakube-parameters.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
EMDASH = "—"
BOM = "﻿"
MOJI = [
    "â",
    "Â",
    "ï»¿",
    "â€",
    "Ã",
    "Â¿",
    "Ã¯",
]  # standalone » removed (legit guillemet)
URL_RE = re.compile(r"\]\(([^)\s]+)")
HEAD_RE = re.compile(r"^(#{1,6})\s")
FENCE_RE = re.compile(r"^\s*```")
CAP_PHRASE = re.compile(r"[A-Z][a-z]+(\s+[a-z]+){2,}")
EN_LOWER_RUN = re.compile(r"\b[a-z]+(\s+[a-z]+){3,}\b")

ALLOW_EN_LINE = {
    "Host monitoring",
    "Classic fullstack",
    "Cloud native fullstack",
    "Application monitoring",
    "Metadata enrichment",
    "Cloud-native full-stack monitoring",
    "Cloud-native full stack",
    "Classic full stack",
    "Kubernetes",
    "OpenShift",
    "Linux",
    "Windows",
    # by-rule EN (verified benign): product-name heading, image alt-text, bare yaml filenames
    "## SUSE Container as a Service (CaaS)",
    "OneAgent installation page with URL to be modified",
    "kubernetes-monitoring-service-account.yaml",
    "kubernetes-monitoring-and-routing.yaml",
    "## Dynatrace Operator security context constraints",
}


def read(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def demoji(s):
    """Repair classic 'UTF-8 decoded as cp1252' mojibake (and strip BOM) so code-block
    comparison ignores scrape-corruption that the RU side legitimately cleaned (e.g. EN
    `â\\x88\\x9a` -> proper `√`). Pure-ASCII and Cyrillic lines pass through unchanged,
    so REAL code alteration is still caught."""
    s = s.replace("﻿", "").replace("ï»¿", "")
    try:
        # EN scrape corrupted UTF-8 as latin1 (C1 controls present), so reverse via latin1.
        return s.encode("latin1", errors="strict").decode("utf-8", errors="strict")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s


def urls(t):
    return sorted(URL_RE.findall(t))


def fences(ls):
    return [i for i, l in enumerate(ls) if FENCE_RE.match(l)]


def code_blocks(ls):
    blocks, inb, cur = [], False, []
    for l in ls:
        if FENCE_RE.match(l):
            if inb:
                blocks.append(cur)
                cur = []
            inb = not inb
            continue
        if inb:
            cur.append(demoji(l))
    return blocks


def headings(ls):
    return [l for l in ls if HEAD_RE.match(l)]


total_warn = total_fail = 0
for rel in FILES:
    enp = os.path.join(BASE, "managed", rel)
    rup = os.path.join(BASE, "managed-ru", rel)
    if not os.path.exists(rup):
        print(f"[MISSING] {rel}")
        total_fail += 1
        continue
    en, ru = read(enp), read(rup)
    el, rl = en.split("\n"), ru.split("\n")
    msgs = []

    if len(el) != len(rl):
        msgs.append(("FAIL", f"line-parity EN={len(el)} RU={len(rl)}"))
    for key in ("source:", "scraped:"):
        if [l for l in el if l.startswith(key)] != [l for l in rl if l.startswith(key)]:
            msgs.append(("FAIL", f"frontmatter {key} mismatch"))
    if EMDASH in ru:
        ln = [i + 1 for i, l in enumerate(rl) if EMDASH in l]
        msgs.append(("FAIL", f"em-dash at {ln}"))
    for m in MOJI:
        if m in ru:
            ln = [i + 1 for i, l in enumerate(rl) if m in l]
            msgs.append(("FAIL", f"mojibake {m!r} at {ln}"))
    if BOM in ru:
        msgs.append(("FAIL", "BOM present"))
    if urls(en) != urls(ru):
        msgs.append(
            (
                "FAIL",
                f"URL mismatch EN-only={sorted(set(urls(en)) - set(urls(ru)))} RU-only={sorted(set(urls(ru)) - set(urls(en)))}",
            )
        )
    if fences(el) != fences(rl):
        msgs.append(("FAIL", "fence positions differ"))
    if code_blocks(el) != code_blocks(rl):
        # report which block index differs
        ecb, rcb = code_blocks(el), code_blocks(rl)
        diff_idx = [i for i in range(min(len(ecb), len(rcb))) if ecb[i] != rcb[i]]
        msgs.append(("FAIL", f"code-block content differs from EN (blocks {diff_idx})"))
    eh = [HEAD_RE.match(l).group(1) for l in headings(el)]
    rh = [HEAD_RE.match(l).group(1) for l in headings(rl)]
    if eh != rh:
        msgs.append(("FAIL", "heading levels differ"))

    for pat in (
        r"\bвы можете\b",
        r"\bвы должны\b",
        r"\bВы можете\b",
        r"\bВы должны\b",
        r"\bвы хотите\b",
        r"\bВы хотите\b",
        r"\bвам нужно\b",
        r"\bвам необходимо\b",
    ):
        for i, l in enumerate(rl):
            if re.search(pat, l):
                msgs.append(("WARN", f"calque L{i + 1}: {l.strip()[:65]}"))

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
        bare = re.sub(r"[A-Za-z]+(?:-[A-Za-z]+)+", " ", bare)  # drop hyphenated identifiers (dynatrace-csi-driver, certs-dir)
        bare = re.sub(r"[*#>\-+|]", " ", bare).strip()
        if CAP_PHRASE.search(bare) or EN_LOWER_RUN.search(bare):
            msgs.append(("WARN", f"EN-leftover L{i + 1}: {s[:75]}"))

    fails = [m for t, m in msgs if t == "FAIL"]
    warns = [m for t, m in msgs if t == "WARN"]
    total_fail += len(fails)
    total_warn += len(warns)
    status = "PASS" if not fails else "FAIL"
    mark = "" if not (fails or warns) else "  <<<"
    print(f"[{status}] {rel}  (lines {len(rl)}, F{len(fails)} W{len(warns)}){mark}")
    for t, m in msgs:
        print(f"    [{t}] {m}")

print(
    f"\n=== TOTAL: {total_fail} FAIL, {total_warn} WARN across {len(FILES)} files ==="
)
