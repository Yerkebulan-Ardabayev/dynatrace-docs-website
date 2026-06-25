# -*- coding: utf-8 -*-
"""L4-IF.34 QA: GCP gcp-supported-service-metrics-new/ (35 files).

Reuses _qa_l4if33 framework (line-parity, frontmatter byte-eq, em-dash=0,
mojibake/BOM=0, URL-identity, code-fence, heading parity, calque, EN-leftover)
+ a dedicated 4-column metric-table integrity check:
  per data row, EN==RU for cols 1/2/4 (Feature set / Name / identifier kept EN),
  col 3 (Unit) is the canonical RU translation (or both empty), pipe-count equal.
Table rows are excluded from the prose EN-leftover scan (Name/identifier columns
are intentionally EN).
"""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new"

CYR = re.compile(r"[А-Яа-яЁё]")
EMDASH = "—"
BOM = "﻿"
MOJI = ["â", "Â", "ï»¿", "â€", "Ã", "’", "‘", "“", "”", "…"]
URL_RE = re.compile(r"\]\(([^)\s]+)")
HEAD_RE = re.compile(r"^(#{1,6})\s")
FENCE_RE = re.compile(r"^```")
ROW_RE = re.compile(r"^\|.*\|$")
SEP_RE = re.compile(r"^\|[\s\-|]+\|$")
CAP_PHRASE = re.compile(r"[A-Z][a-z]+(\s+[a-z]+){2,}")
EN_LOWER_RUN = re.compile(r"\b[a-z]+(\s+[a-z]+){3,}\b")

# canonical Unit map (must match the build script)
UNIT = {
    "Count": "Количество",
    "Byte": "Байт",
    "MilliSecond": "Миллисекунда",
    "MicroSecond": "Микросекунда",
    "Second": "Секунда",
    "Percent": "Процент",
    "Unspecified": "Не указано",
    "GibiByte": "Гибибайт",
    "GigaByte": "Гигабайт",
    "BytePerSecond": "Байт/с",
    "PerSecond": "1/с",
    "Day": "День",
    "": "",
}


def read(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def urls(text):
    return sorted(URL_RE.findall(text))


def fences(lines):
    return [i for i, l in enumerate(lines) if FENCE_RE.match(l)]


def headings(lines):
    return [l for l in lines if HEAD_RE.match(l)]


def data_rows(lines):
    """pipe-rows that are not the header row and not the --- separator"""
    out = []
    for i, l in enumerate(lines):
        if ROW_RE.match(l) and not SEP_RE.match(l):
            # skip the header row (translated, contains 'Идентификатор' or EN header)
            if "metric identifier" in l or "Идентификатор метрики" in l:
                continue
            out.append((i, l))
    return out


FILES = sorted(
    f for f in os.listdir(os.path.join(BASE, "managed", SUB)) if f.endswith(".md")
)

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
            msgs.append(("FAIL", f"frontmatter {key} mismatch"))

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

    # 6 code-fence parity
    if fences(el) != fences(rl):
        msgs.append(("FAIL", f"fence positions differ"))

    # 7 heading parity (levels)
    eh = [HEAD_RE.match(l).group(1) for l in headings(el)]
    rh = [HEAD_RE.match(l).group(1) for l in headings(rl)]
    if eh != rh:
        msgs.append(("FAIL", f"heading levels EN={eh} RU={rh}"))

    # 8 metric-table integrity (4-col)
    edr, rdr = data_rows(el), data_rows(rl)
    if len(edr) != len(rdr):
        msgs.append(("FAIL", f"data-row count EN={len(edr)} RU={len(rdr)}"))
    else:
        for (ei, eline), (ri, rline) in zip(edr, rdr):
            ec, rc = eline.split("|"), rline.split("|")
            if len(ec) != len(rc):
                msgs.append(("FAIL", f"L{ri + 1} pipe-count EN={len(ec)} RU={len(rc)}"))
                continue
            if len(ec) != 6:
                msgs.append(("WARN", f"L{ri + 1} unexpected col count {len(ec)}"))
                continue
            # col1 feature set, col2 name, col4 identifier -> byte-identical
            for ci, label in ((1, "feature set"), (2, "name"), (4, "identifier")):
                if ec[ci] != rc[ci]:
                    msgs.append(
                        (
                            "FAIL",
                            f"L{ri + 1} col '{label}' changed: EN={ec[ci]!r} RU={rc[ci]!r}",
                        )
                    )
            # col3 unit -> canonical translation
            eu, rru = ec[3].strip(), rc[3].strip()
            exp = UNIT.get(eu, None)
            if exp is None:
                msgs.append(("WARN", f"L{ri + 1} unknown EN unit {eu!r}"))
            elif rru != exp:
                msgs.append(
                    (
                        "FAIL",
                        f"L{ri + 1} unit EN={eu!r} -> RU={rru!r}, expected {exp!r}",
                    )
                )

    # 9 calque check
    for pat in (r"\bвы можете\b", r"\bвы должны\b", r"\bВы можете\b"):
        for i, l in enumerate(rl):
            if re.search(pat, l):
                msgs.append(("WARN", f"calque '{pat}' L{i + 1}: {l.strip()[:70]}"))

    # 10 EN-leftover prose scan (skip code blocks + ALL table rows + Cyrillic lines)
    inb = False
    for i, l in enumerate(rl):
        if FENCE_RE.match(l):
            inb = not inb
            continue
        if inb or ROW_RE.match(l):  # table rows excluded (intentional EN values)
            continue
        s = l.strip()
        if not s or CYR.search(l):
            continue
        bare = re.sub(r"\[[^\]]*\]\([^)]*\)", "", l)
        bare = re.sub(r"`[^`]*`", "", bare)
        bare = re.sub(r"https?://\S+", "", bare)
        bare = re.sub(r"[*#>\-+|]", " ", bare).strip()
        # allow pure product-name lines (H1 like '# Operations: Cloud Monitoring & Logging')
        if CAP_PHRASE.search(bare) or EN_LOWER_RUN.search(bare):
            msgs.append(("WARN", f"EN-leftover suspect L{i + 1}: {s[:70]}"))

    fails = [m for t, m in msgs if t == "FAIL"]
    warns = [m for t, m in msgs if t == "WARN"]
    total_fail += len(fails)
    total_warn += len(warns)
    status = "PASS" if not fails else "FAIL"
    print(f"[{status}] {rel}  (lines {len(rl)}, rows {len(rdr)}, warns {len(warns)})")
    for t, m in msgs:
        print(f"    [{t}] {m}")

print(
    f"\n=== TOTAL: {total_fail} FAIL, {total_warn} WARN across {len(FILES)} files ==="
)
