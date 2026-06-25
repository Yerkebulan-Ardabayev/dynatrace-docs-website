# -*- coding: utf-8 -*-
"""QA for L4-IF.39 batch (7 files). Checks canon invariants RU vs EN."""

import os, re

EN_ROOT = "docs/managed"
RU_ROOT = "docs/managed-ru"

FILES = [
    "index.md",
    "observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes.md",
    "observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services.md",
    "observe/infrastructure-observability/vmware-vsphere-monitoring.md",
    "analyze-explore-automate/metrics-classic/self-monitoring-metrics.md",
    "license/dps-for-hybrid.md",
    "secure/application-security/vulnerability-analytics/vulnerability-evaluation.md",
]

CYR = re.compile(r"[Ѐ-ӿ]")
URL = re.compile(r"\]\(([^)\s]+)")  # link/image target up to space or )
HEAD = re.compile(r"^(#+)\s")
MOJI = ["﻿", "â", "Ã", "€", "ƒ", "…\x80"]
# EN-leftover blind-spot: strip markup, then look for >=3 latin words run w/o cyrillic
STRIP = [
    re.compile(r"`[^`]*`"),  # code spans
    re.compile(r"!\[[^\]]*\]\([^)]*\)"),  # images
    re.compile(r"\[([^\]]*)\]\([^)]*\)"),  # links -> keep display text
    re.compile(r"\*\*[^*]+\*\*"),  # bold (UI labels)
    re.compile(r"https?://\S+"),
    re.compile(r"/managed/\S+"),
]
LATINRUN = re.compile(r"(?:[A-Za-z][A-Za-z.\-/]*\s+){2,}[A-Za-z][A-Za-z.\-/]*")


def rd(p):
    return [ln.replace("\r", "") for ln in open(p, encoding="utf-8").read().split("\n")]


def fences(lines):
    """return set of indexes that are fence marker/interior, and the slice list"""
    idx = set()
    infence = False
    for i, c in enumerate(lines):
        st = c.strip()
        isf = st.startswith("```")
        if infence:
            idx.add(i)
            if isf:
                infence = False
        elif isf:
            idx.add(i)
            infence = True
    return idx


def qa(rel):
    en = rd(os.path.join(EN_ROOT, rel))
    ru = rd(os.path.join(RU_ROOT, rel))
    fails, warns = [], []

    # 1 line parity
    if len(en) != len(ru):
        fails.append("LINE-PARITY %d != %d" % (len(en), len(ru)))
        return fails, warns  # rest unreliable

    # 2 frontmatter source/scraped/--- byte-eq
    for i in (0, 2, 3, 4):
        if en[i] != ru[i]:
            fails.append("FRONTMATTER L%d: %r != %r" % (i + 1, en[i], ru[i]))
    # title translated
    if ru[1] == en[1] or not ru[1].startswith("title:"):
        warns.append("TITLE not translated: %r" % ru[1])

    # 3 em-dash = 0
    for i, c in enumerate(ru, 1):
        if "—" in c:
            fails.append("EM-DASH L%d: %r" % (i, c))

    # 4 mojibake / BOM = 0 in RU
    for i, c in enumerate(ru, 1):
        for m in MOJI:
            if m in c:
                fails.append("MOJIBAKE L%d %r in %r" % (i, m, c[:60]))

    # 5 URL identity (multiset of link/image targets per file)
    eu = sorted(URL.findall("\n".join(en)))
    rufound = sorted(URL.findall("\n".join(ru)))
    if eu != rufound:
        only_en = [x for x in eu if x not in rufound]
        only_ru = [x for x in rufound if x not in eu]
        if only_en or only_ru:
            fails.append(
                "URL-MISMATCH only_en=%s only_ru=%s" % (only_en[:6], only_ru[:6])
            )

    # 6 heading level parity
    for i, (a, b) in enumerate(zip(en, ru), 1):
        ma, mb = HEAD.match(a), HEAD.match(b)
        if bool(ma) != bool(mb):
            fails.append("HEADING-SHAPE L%d en=%r ru=%r" % (i, a[:40], b[:40]))
        elif ma and mb and len(ma.group(1)) != len(mb.group(1)):
            fails.append("HEADING-LEVEL L%d en=%r ru=%r" % (i, a[:40], b[:40]))

    # 7 code-fence interior byte-identity
    fi = fences(en)
    for i in sorted(fi):
        if en[i] != ru[i]:
            fails.append("FENCE L%d en=%r ru=%r" % (i + 1, en[i][:50], ru[i][:50]))

    # 8 EN-leftover blind-spot scan (WARN)
    is_index = rel == "index.md"
    for i, c in enumerate(ru, 1):
        if i - 1 in fi:
            continue
        if is_index and c.startswith("["):
            continue  # card grids legit EN
        s = c
        for rx in STRIP:
            s = rx.sub(lambda m: m.group(1) if m.re.groups else " ", s)
        if CYR.search(c):
            # has cyrillic; flag only if a long latin run survives stripping AND no cyr in that run
            for run in LATINRUN.findall(s):
                if (
                    not CYR.search(run)
                    and len(run.split()) >= 3
                    and "dsfm" not in run
                    and "builtin" not in run
                ):
                    warns.append("EN-RUN L%d: %r" % (i, run.strip()[:60]))
        else:
            st = s.strip()
            if LATINRUN.search(st):
                warns.append("EN-NOCYR L%d: %r" % (i, c.strip()[:70]))
    return fails, warns


if __name__ == "__main__":
    tf = tw = 0
    for rel in FILES:
        fails, warns = qa(rel)
        tf += len(fails)
        tw += len(warns)
        tag = "PASS" if not fails else "FAIL"
        print("[%s] %s" % (tag, rel.split("/")[-1]))
        for f in fails:
            print("   FAIL", f)
        for w in warns:
            print("   warn", w)
    print("\n== TOTAL FAIL=%d WARN=%d ==" % (tf, tw))
