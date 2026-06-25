# -*- coding: utf-8 -*-
"""Shared OTel collector use-cases translation canon (L4-IF.69).

Reuses the S boilerplate + norm/read_lf from the L4-IF.68 builder verbatim so the
whole use-cases subtree stays byte-consistent on shared lines. Each per-file
builder only adds the lines unique to that recipe leaf:

    from _otel_canon import S, SUB, build_one, qa_one
    TRANS = {  ...unique lines...,  **S }
    PASS  = {"### Receivers", "### Processors", "### Exporters"}
    if __name__ == "__main__":
        build_one(SUB, "enrich.md", TRANS, PASS)
        qa_one(SUB, "enrich.md")

Deterministic engine guarantees STRUCTURE (line-parity / URL / fence / heading /
em-dash=0 / mojibake=0). WORD quality (term consistency, calques, awkwardness) is
caught by the manual critical review after the batch.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

from _build_otel_uc_l4if68 import S, norm, read_lf  # exact boilerplate reuse

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/opentelemetry/collector/use-cases"


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def build_one(rel_dir, fname, trans, passset=frozenset()):
    en_path = os.path.join(BASE, "managed", rel_dir, fname)
    ru_path = os.path.join(BASE, "managed-ru", rel_dir, fname)
    en_lines = read_lf(en_path).split("\n")
    tmap = {norm(k): v for k, v in trans.items()}
    pset = {norm(k) for k in passset}
    out = []
    in_fence = False
    for ln in en_lines:
        raw = ln.strip()
        st = norm(raw)
        if raw.startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence or st == "" or st == "---":
            out.append(ln)
            continue
        if raw.startswith("source:") or raw.startswith("scraped:"):
            out.append(ln)
            continue
        if st in tmap:
            indent = ln[: len(ln) - len(ln.lstrip())]
            out.append(indent + tmap[st])
            continue
        if st in pset:
            out.append(ln)
            continue
        raise SystemExit(f"[{fname}] UNTRANSLATED: {ln!r}")

    assert len(out) == len(en_lines), f"{fname}: parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK  {fname}: {len(out)} lines -> {ru_path}")


# ---------------------------------------------------------------------------
# QA  (mirrors _qa_otel_uc_l4if68.py)
# ---------------------------------------------------------------------------
CYR = re.compile(r"[А-Яа-яЁё]")
EMDASH = "—"
BOM = "﻿"
MOJI = ["â", "Â", "ï»¿", "â€", "Ã", "ï", "»", "¿", "’", "‘", "“", "”", "…"]
URL_RE = re.compile(r"\]\(([^)\s]+)")
HEAD_RE = re.compile(r"^(#{1,6})\s")
FENCE_RE = re.compile(r"^\s*```")
CAP_PHRASE = re.compile(r"[A-Z][a-z]+(\s+[a-z]+){2,}")
EN_LOWER_RUN = re.compile(r"\b[a-z]+(\s+[a-z]+){3,}\b")

ALLOW_EN_LINE = {
    "### Receivers",
    "### Processors",
    "### Exporters",
    "### Connectors",
    "### FluentD",
    "### Jaeger",
    "### Journald",
    "### Prometheus",
    "### Zipkin",
}


def _read(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def _urls(text):
    return sorted(URL_RE.findall(text))


def _fences(lines):
    return [i for i, l in enumerate(lines) if FENCE_RE.match(l)]


def _code_blocks(lines):
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


def _headings(lines):
    return [l for l in lines if HEAD_RE.match(l)]


def qa_one(rel_dir, fname, verbose=True):
    en = _read(os.path.join(BASE, "managed", rel_dir, fname))
    ru = _read(os.path.join(BASE, "managed-ru", rel_dir, fname))
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

    if _urls(en) != _urls(ru):
        only_en = sorted(set(_urls(en)) - set(_urls(ru)))
        only_ru = sorted(set(_urls(ru)) - set(_urls(en)))
        msgs.append(("FAIL", f"URL mismatch EN-only={only_en} RU-only={only_ru}"))

    if _fences(el) != _fences(rl):
        msgs.append(("FAIL", f"fence positions EN={_fences(el)} RU={_fences(rl)}"))
    if _code_blocks(el) != _code_blocks(rl):
        msgs.append(("FAIL", "code-block content differs from EN"))

    eh = [HEAD_RE.match(l).group(1) for l in _headings(el)]
    rh = [HEAD_RE.match(l).group(1) for l in _headings(rl)]
    if eh != rh:
        msgs.append(("FAIL", f"heading levels EN={eh} RU={rh}"))

    for pat in (
        r"\bвы можете\b",
        r"\bвы должны\b",
        r"\bВы можете\b",
        r"\bВы должны\b",
        r"\bвы хотите\b",
        r"\bВы хотите\b",
    ):
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
    status = "PASS" if not fails else "FAIL"
    if verbose:
        print(f"[{status}] {fname}  (lines {len(rl)}, warns {len(warns)})")
        for t, m in msgs:
            print(f"    [{t}] {m}")
    return len(fails), len(warns), msgs


if __name__ == "__main__":
    # Self-test: QA an already-shipped sibling (must be PASS 0/0).
    qa_one(SUB, "jaeger.md")
