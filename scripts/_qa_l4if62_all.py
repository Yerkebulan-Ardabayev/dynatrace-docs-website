# -*- coding: utf-8 -*-
"""L4-IF.62 UNIFIED QA: all 25 setup-on-k8s/guides files (deployment-and-configuration
+ networking-security-compliance). Trustworthy final gate.

Fixes vs subagent QA copies:
- FENCE_RE = r"^\s*```"  (strip-aware → list-indented code fences detected, no false
  EN-leftover WARN on kubectl/oc/yaml-comment lines inside indented fences).
- mojibake list excludes standalone "»" (legit Russian guillemet «...»); BOM still checked.
"""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides"

FILES = [
    "deployment-and-configuration.md",
    "deployment-and-configuration/activegate-pvc.md",
    "deployment-and-configuration/cluster-role-aggregation.md",
    "deployment-and-configuration/configure-startup-probes.md",
    "deployment-and-configuration/istio-deployment.md",
    "deployment-and-configuration/monitoring-and-instrumentation/annotate.md",
    "deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx.md",
    "deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring.md",
    "deployment-and-configuration/node-image-pull.md",
    "deployment-and-configuration/resource-management/ag-resource-limits.md",
    "deployment-and-configuration/resource-management/dto-resource-limits.md",
    "deployment-and-configuration/resource-management/probe-timeout.md",
    "deployment-and-configuration/updates-and-maintenance/auto-update-components.md",
    "deployment-and-configuration/updates-and-maintenance/dto-auto-update.md",
    "deployment-and-configuration/updates-and-maintenance/update-uninstall-operator.md",
    "deployment-and-configuration/using-gitops.md",
    "networking-security-compliance/advanced-security-configurations/injection-readonly-volume.md",
    "networking-security-compliance/network-configurations.md",
    "networking-security-compliance/network-configurations/network-zones.md",
    "networking-security-compliance/security-configurations.md",
    "networking-security-compliance/security-configurations/enable-app-armor.md",
    "networking-security-compliance/security-configurations/openshift-configuration.md",
    "networking-security-compliance/security-configurations/pod-security-standards.md",
    "networking-security-compliance/security-configurations/seccomp.md",
    "networking-security-compliance/security-configurations/token-rotation.md",
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
}


def read(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


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
            cur.append(l)
    return blocks


def headings(ls):
    return [l for l in ls if HEAD_RE.match(l)]


total_warn = total_fail = 0
for rel in FILES:
    enp = os.path.join(BASE, "managed", SUB, rel)
    rup = os.path.join(BASE, "managed-ru", SUB, rel)
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
        msgs.append(("FAIL", "code-block content differs from EN"))
    eh = [HEAD_RE.match(l).group(1) for l in headings(el)]
    rh = [HEAD_RE.match(l).group(1) for l in headings(rl)]
    if eh != rh:
        msgs.append(("FAIL", f"heading levels differ"))

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
        bare = re.sub(r"[*#>\-+|]", " ", bare).strip()
        if CAP_PHRASE.search(bare) or EN_LOWER_RUN.search(bare):
            msgs.append(("WARN", f"EN-leftover L{i + 1}: {s[:65]}"))

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
