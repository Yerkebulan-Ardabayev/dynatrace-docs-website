"""Reusable QA for AIX L4-IF.19 batch. Usage: python _qa_aix_l4if19.py <relpath-under-managed>"""

import re
import sys
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
FENCE = "`" * 3


def load(p):
    return open(p, encoding="utf-8").read().replace("\r\n", "\n").split("\n")


def urls(lines):
    out = []
    for ln in lines:
        out += re.findall(r"\]\((/managed|https?://)[^ \")]*", ln)
    return out


def main(rel):
    en = load(os.path.join(BASE, "managed", rel))
    ru = load(os.path.join(BASE, "managed-ru", rel))
    print(f"=== {rel} ===")
    ok = True

    # 1 line parity
    if len(en) == len(ru):
        print(f"[OK] line parity {len(en)}")
    else:
        ok = False
        print(f"[FAIL] line parity EN={len(en)} RU={len(ru)}")

    # 2 url identity
    eu, rru = urls(en), urls(ru)
    print(
        "[OK] URLs identical"
        if eu == rru
        else f"[FAIL] URLs differ EN={len(eu)} RU={len(rru)}"
    )
    ok &= eu == rru

    # 3 code-fence byte identity
    infence = False
    bad = []
    for i, (a, b) in enumerate(zip(en, ru), 1):
        toggled = a.strip().startswith(FENCE)
        if infence or toggled:
            if a != b:
                bad.append(i)
        if toggled:
            infence = not infence
    print(
        "[OK] code-fence byte-identical"
        if not bad
        else f"[FAIL] code mismatch lines {bad}"
    )
    ok &= not bad

    # 4 mojibake / em-dash
    rtext = "\n".join(ru)
    for label, needle in [
        ("em-dash", "—"),
        ("BOM-efbbbf", "﻿"),
        ("BOM-double-encoded", "ï»¿"),
        ("broken-a-circumflex", "â"),
    ]:
        n = rtext.count(needle)
        print(f"[{'OK' if n == 0 else 'WARN'}] {label}: {n}")
        if needle == "—" and n:
            ok = False

    # 5 heading parity
    for lvl in ("# ", "## ", "### ", "#### "):
        ec = sum(1 for x in en if x.startswith(lvl) and not x.startswith(lvl + "#"))
        rc = sum(1 for x in ru if x.startswith(lvl) and not x.startswith(lvl + "#"))
        tag = "OK" if ec == rc else "FAIL"
        if ec != rc:
            ok = False
        print(f"[{tag}] heading '{lvl.strip()}' EN={ec} RU={rc}")

    # 6 hard-break parity (trailing 2+ spaces)
    eh = [i for i, x in enumerate(en, 1) if re.search(r"  +$", x)]
    rh = [i for i, x in enumerate(ru, 1) if re.search(r"  +$", x)]
    print(
        "[OK] hard-break parity" if eh == rh else f"[FAIL] hard-break EN={eh} RU={rh}"
    )
    ok &= eh == rh

    # 7 frontmatter source/scraped byte-eq
    for i in range(min(6, len(en))):
        if en[i].startswith(("source:", "scraped:")) and en[i] != ru[i]:
            ok = False
            print(f"[FAIL] frontmatter L{i + 1} changed")

    # 8 leftover-English prose heuristic (lines with 3+ ASCII-word run, excluding code/links/UI-bold)
    leftover = []
    for i, b in enumerate(ru, 1):
        s = b.strip()
        if (
            not s
            or s.startswith(FENCE)
            or s.startswith("source:")
            or s.startswith("scraped:")
        ):
            continue
        # strip code spans, links targets, bold UI
        t = re.sub(r"`[^`]*`", "", b)
        t = re.sub(r"\]\([^)]*\)", "", t)
        t = re.sub(r"\*\*[^*]*\*\*", "", t)
        t = re.sub(r"https?://\S+", "", t)
        if re.search(r"[a-zA-Z]+\s+[a-zA-Z]+\s+[a-zA-Z]+\s+[a-zA-Z]+", t):
            leftover.append(i)
    print(
        "[OK] no leftover-EN prose"
        if not leftover
        else f"[WARN] possible leftover-EN lines {leftover}"
    )

    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    main(sys.argv[1])
