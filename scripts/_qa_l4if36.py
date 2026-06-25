# -*- coding: utf-8 -*-
"""L4-IF.36 QA: 5 GCP gcp-guide walkthrough/concept pages.

Reuses the L4-IF.35 framework (line-parity, frontmatter byte-eq with \\r-norm,
em-dash=0, mojibake/BOM=0, URL-identity, fence-position parity, heading parity,
calque, EN-leftover prose scan) and ADDS two hardening checks:
  * code-fence CONTENT byte-identity (commands/YAML inside ``` must be untouched)
  * table-row integrity: rows with NO Cyrillic must be byte-identical to EN
    (catches a corrupted identifier in the services/dimension tables); rows WITH
    Cyrillic only need matching pipe count (structure preserved).
Full unicode report -> _qa_l4if36_out.txt; stdout stays ASCII-only.
"""

import io
import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
GG = "ingest-from/google-cloud-platform/gcp-integrations/gcp-guide"

FILES = [
    f"{GG}/migrate-gcp-function-1-to-k8s-1.md",
    f"{GG}/monitor-multiple-projects.md",
    f"{GG}/migrate-gcp-function.md",
    f"{GG}/deploy-k8/self-monitoring-gcp.md",
    f"{GG}/deploy-k8/gcp-autodiscovery.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
EMDASH = "—"
BOM = "﻿"
MOJI = ["â", "ï", "Ã"] + [chr(c) for c in range(0x80, 0xA0)]
URL_RE = re.compile(r"\]\(([^)\s]+)")
HEAD_RE = re.compile(r"^(#{1,6})\s")
FENCE_RE = re.compile(r"^\s*```")
ROW_RE = re.compile(r"^\|.*\|$")
SEP_RE = re.compile(r"^\|[\s\-|]+\|$")
CAP_PHRASE = re.compile(r"[A-Z][a-z]+(\s+[a-z]+){2,}")
EN_LOWER_RUN = re.compile(r"\b[a-z]+(\s+[a-z]+){3,}\b")

OUT = io.StringIO()


def log(s):
    OUT.write(s + "\n")


def read(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def urls(t):
    return sorted(URL_RE.findall(t))


def fences(lines):
    return [i for i, l in enumerate(lines) if FENCE_RE.match(l)]


def headings(lines):
    return [l for l in lines if HEAD_RE.match(l)]


def check(rel):
    en = read(os.path.join(BASE, "managed", rel))
    ru = read(os.path.join(BASE, "managed-ru", rel))
    el, rl = en.split("\n"), ru.split("\n")
    msgs = []

    if len(el) != len(rl):
        msgs.append(("FAIL", f"line-parity EN={len(el)} RU={len(rl)}"))
    for key in ("source:", "scraped:"):
        if [l for l in el if l.startswith(key)] != [l for l in rl if l.startswith(key)]:
            msgs.append(("FAIL", f"frontmatter {key} mismatch"))
    # title must be translated (Cyrillic present)
    rt = [l for l in rl if l.startswith("title:")]
    if rt and not CYR.search(rt[0]):
        msgs.append(("WARN", f"title not translated: {rt[0]}"))

    if EMDASH in ru:
        ln = [i + 1 for i, l in enumerate(rl) if EMDASH in l]
        msgs.append(("FAIL", f"em-dash at {ln}"))
    for m in MOJI:
        if m in ru:
            ln = [i + 1 for i, l in enumerate(rl) if m in l]
            msgs.append(("FAIL", f"mojibake U+{ord(m):04X} at {ln}"))
    if BOM in ru:
        ln = [i + 1 for i, l in enumerate(rl) if BOM in l]
        msgs.append(("FAIL", f"BOM at {ln}"))

    if urls(en) != urls(ru):
        msgs.append(
            (
                "FAIL",
                f"URL mismatch EN-only={sorted(set(urls(en)) - set(urls(ru)))} "
                f"RU-only={sorted(set(urls(ru)) - set(urls(en)))}",
            )
        )

    ef, rf = fences(el), fences(rl)
    if ef != rf:
        msgs.append(("FAIL", f"fence positions differ EN={ef} RU={rf}"))
    else:
        for k in range(0, len(ef) - 1, 2):
            a, b = ef[k], ef[k + 1]
            if el[a + 1 : b] != rl[a + 1 : b]:
                for j in range(a + 1, b):
                    if el[j] != rl[j]:
                        msgs.append(
                            (
                                "FAIL",
                                f"code-fence content changed L{j + 1}: "
                                f"EN={el[j]!r} RU={rl[j]!r}",
                            )
                        )
                        break

    eh = [HEAD_RE.match(l).group(1) for l in headings(el)]
    rh = [HEAD_RE.match(l).group(1) for l in headings(rl)]
    if eh != rh:
        msgs.append(("FAIL", f"heading levels EN={eh} RU={rh}"))

    # table-row integrity (aligned by position; parity guaranteed above)
    if len(el) == len(rl):
        inb = False
        for i, (e, r) in enumerate(zip(el, rl)):
            if FENCE_RE.match(r):
                inb = not inb
                continue
            if inb:
                continue
            if ROW_RE.match(r) and not SEP_RE.match(r):
                if not CYR.search(r):
                    if e != r:
                        msgs.append(
                            (
                                "FAIL",
                                f"identifier-row L{i + 1} changed: EN={e!r} RU={r!r}",
                            )
                        )
                elif e.count("|") != r.count("|"):
                    msgs.append(
                        (
                            "FAIL",
                            f"pipe-count L{i + 1} EN={e.count('|')} RU={r.count('|')}",
                        )
                    )

    # calque (soft)
    for pat in (r"\bвы можете\b", r"\bвы должны\b", r"\bВы можете\b", r"\bВы должны\b"):
        for i, l in enumerate(rl):
            if re.search(pat, l):
                msgs.append(("WARN", f"calque '{pat}' L{i + 1}: {l.strip()[:70]}"))

    # EN-leftover prose scan (soft)
    inb = False
    for i, l in enumerate(rl):
        if FENCE_RE.match(l):
            inb = not inb
            continue
        if inb or ROW_RE.match(l):
            continue
        s = l.strip()
        if not s or CYR.search(l):
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
    log(
        f"[{status}] {rel.split('/')[-1]:42s} (lines {len(rl)}, "
        f"fails {len(fails)}, warns {len(warns)})"
    )
    for t, m in msgs:
        log(f"    [{t}] {m}")
    return len(fails), len(warns), status


def main():
    tf = tw = 0
    npass = 0
    for rel in FILES:
        f, w, st = check(rel)
        tf += f
        tw += w
        npass += st == "PASS"
    log(f"\n=== TOTAL: {tf} FAIL, {tw} WARN; {npass}/{len(FILES)} PASS ===")
    report = OUT.getvalue()
    with open(
        os.path.join(os.path.dirname(__file__), "_qa_l4if36_out.txt"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(report)
    # ASCII-only stdout summary
    print(f"QA L4-IF.36: {tf} FAIL, {tw} WARN, {npass}/{len(FILES)} PASS")
    print("full report -> scripts/_qa_l4if36_out.txt")


if __name__ == "__main__":
    main()
