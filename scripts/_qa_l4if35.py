# -*- coding: utf-8 -*-
"""L4-IF.35 QA: 5 GCP metric-leaf monitoring pages + 5 GCP hub pages.

Reuses the L4-IF.34 framework (line-parity, frontmatter byte-eq with \\r-norm,
em-dash=0, mojibake/BOM=0, URL-identity, code-fence parity, heading parity,
calque, EN-leftover prose scan). For the 5 metric leaves it additionally runs the
4-column metric-table integrity check (cols 1/2/4 EN-identical, col 3 canonical
Unit, pipe-count parity). Hubs skip the metric-table check (their tables are
covered by URL-identity + structural checks).
"""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
GCP = "ingest-from/google-cloud-platform/gcp-integrations"

METRIC_LEAVES = [
    f"{GCP}/cloudrun/cloud-run-monitoring.md",
    f"{GCP}/gcp-functions/cloud-functions-monitoring.md",
    f"{GCP}/google-app-engine/app-engine-monitoring.md",
    f"{GCP}/google-compute-engine/compute-engine-monitoring.md",
    f"{GCP}/google-gke/google-kubernetes-engine-monitoring.md",
]
HUBS = [
    f"{GCP}/gcp-functions.md",
    f"{GCP}/google-compute-engine.md",
    f"{GCP}/google-app-engine.md",
    f"{GCP}/gcp-guide.md",
    f"{GCP}/gcp-supported-service-metrics-new.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
EMDASH = "—"
BOM = "﻿"
# mojibake lead bytes / C1 controls (guillemets U+00AB/U+00BB are legitimate)
MOJI = ["â", "ï", "Ã"] + [chr(c) for c in range(0x80, 0xA0)]
URL_RE = re.compile(r"\]\(([^)\s]+)")
HEAD_RE = re.compile(r"^(#{1,6})\s")
FENCE_RE = re.compile(r"^```")
ROW_RE = re.compile(r"^\|.*\|$")
SEP_RE = re.compile(r"^\|[\s\-|]+\|$")
CAP_PHRASE = re.compile(r"[A-Z][a-z]+(\s+[a-z]+){2,}")
EN_LOWER_RUN = re.compile(r"\b[a-z]+(\s+[a-z]+){3,}\b")

UNIT = {
    "Count": "Количество",
    "Byte": "Байт",
    "MilliSecond": "Миллисекунда",
    "MicroSecond": "Микросекунда",
    "NanoSecond": "Наносекунда",
    "Second": "Секунда",
    "Percent": "Процент",
    "Unspecified": "Не указано",
    "MebiByte": "Мебибайт",
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


def urls(t):
    return sorted(URL_RE.findall(t))


def fences(lines):
    return [i for i, l in enumerate(lines) if FENCE_RE.match(l)]


def headings(lines):
    return [l for l in lines if HEAD_RE.match(l)]


def metric_rows(lines):
    out = []
    for i, l in enumerate(lines):
        if ROW_RE.match(l) and not SEP_RE.match(l):
            if "metric identifier" in l or "Идентификатор метрики" in l:
                continue
            out.append((i, l))
    return out


def check(rel, is_leaf):
    en = read(os.path.join(BASE, "managed", rel))
    ru = read(os.path.join(BASE, "managed-ru", rel))
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
            msgs.append(("FAIL", f"mojibake U+{ord(m):04X} at {ln}"))
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
    eh = [HEAD_RE.match(l).group(1) for l in headings(el)]
    rh = [HEAD_RE.match(l).group(1) for l in headings(rl)]
    if eh != rh:
        msgs.append(("FAIL", f"heading levels EN={eh} RU={rh}"))

    if is_leaf:
        edr, rdr = metric_rows(el), metric_rows(rl)
        if len(edr) != len(rdr):
            msgs.append(("FAIL", f"data-row count EN={len(edr)} RU={len(rdr)}"))
        else:
            for (ei, eline), (ri, rline) in zip(edr, rdr):
                ec, rc = eline.split("|"), rline.split("|")
                if len(ec) != len(rc) or len(ec) != 6:
                    msgs.append(
                        ("FAIL", f"L{ri + 1} pipe/col count EN={len(ec)} RU={len(rc)}")
                    )
                    continue
                for ci, label in ((1, "feature set"), (2, "name"), (4, "identifier")):
                    if ec[ci] != rc[ci]:
                        msgs.append(
                            (
                                "FAIL",
                                f"L{ri + 1} col '{label}' changed EN={ec[ci]!r} RU={rc[ci]!r}",
                            )
                        )
                eu, rru = ec[3].strip(), rc[3].strip()
                exp = UNIT.get(eu)
                if exp is None:
                    msgs.append(("WARN", f"L{ri + 1} unknown EN unit {eu!r}"))
                elif rru != exp:
                    msgs.append(
                        (
                            "FAIL",
                            f"L{ri + 1} unit EN={eu!r}->RU={rru!r} expected {exp!r}",
                        )
                    )

    for pat in (r"\bвы можете\b", r"\bвы должны\b", r"\bВы можете\b", r"\bВы должны\b"):
        for i, l in enumerate(rl):
            if re.search(pat, l):
                msgs.append(("WARN", f"calque '{pat}' L{i + 1}: {l.strip()[:60]}"))

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
            msgs.append(("WARN", f"EN-leftover suspect L{i + 1}: {s[:60]}"))

    fails = [m for t, m in msgs if t == "FAIL"]
    warns = [m for t, m in msgs if t == "WARN"]
    status = "PASS" if not fails else "FAIL"
    kind = "leaf" if is_leaf else "hub "
    print(
        f"[{status}] {kind} {rel.split('/')[-1]:48s} (lines {len(rl)}, warns {len(warns)})"
    )
    for t, m in msgs:
        print(f"    [{t}] {m}")
    return len(fails), len(warns)


def main():
    tf = tw = 0
    for rel in METRIC_LEAVES:
        f, w = check(rel, True)
        tf += f
        tw += w
    for rel in HUBS:
        f, w = check(rel, False)
        tf += f
        tw += w
    print(
        f"\n=== TOTAL: {tf} FAIL, {tw} WARN across {len(METRIC_LEAVES) + len(HUBS)} files ==="
    )


if __name__ == "__main__":
    main()
