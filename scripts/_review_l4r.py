#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Critical review for batch L4R (configuration-api orphan parents + supported-services twin).
Canon: L99 (config-api), L98/L100 (force-sync code-fences EN->RU + line/heading/fence/table parity),
L101 (period-by-source), L4L/L4Q (deprecated banner verbatim from endpoint RU), CLAUDE rule #0 (no em-dash).

Files:
  parents (no code-fence): aws-privatelink.md, data-privacy-api.md,
                           k8s-credentials-api-api.md, maintenance-windows-api.md
  supported-services (3 code-fences each): aws-supported-services.md, azure-supported-services.md
"""

import os, re, sys

EN = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website\docs\managed\dynatrace-api\configuration-api"
RU = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website\docs\managed-ru\dynatrace-api\configuration-api"

PARENTS = [
    "aws-privatelink.md",
    "data-privacy-api.md",
    "k8s-credentials-api-api.md",
    "maintenance-windows-api.md",
]
SUPPORTED = ["aws-supported-services.md", "azure-supported-services.md"]
ALL = PARENTS + SUPPORTED

# banner canon locked from already-translated endpoint files (must match verbatim)
BANNER_K8S = (
    "Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "
    '"Узнайте, что предлагает Dynatrace Settings API.") со schema '
    "[Kubernetes connection settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "
    '"Просмотр таблицы schema builtin:cloud.kubernetes окружения мониторинга через Dynatrace API.") '
    "(`builtin:cloud.kubernetes`) и "
    "[Kubernetes platform monitoring settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "
    '"Просмотр таблицы schema builtin:cloud.kubernetes.monitoring окружения мониторинга через Dynatrace API.") '
    "(`builtin:cloud.kubernetes.monitoring`)."
)
BANNER_MW = (
    "Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "
    '"Узнайте, что предлагает Dynatrace Settings API.") со schema **Maintenance windows** '
    "(`builtin:alerting.maintenance-window`)."
)

MOJIBAKE = ["Â", "Ã", "ï»¿", "â€", "﻿", "â\x80", "Ð\x9f", "â€”", "â€“"]
ALLOWED_EN_HEADERS = {"#### Curl"}  # L99 ALLOWED_EN
EN_INVARIANT_PREFIXES = ("* Reference", "* Published ", "* Updated on ")

defects = []


def rd(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def lines(s):
    return s.split("\n")


def code_fence_spans(ls):
    """Return list of (start_idx, end_idx) inclusive for ``` fenced blocks."""
    spans, open_i = [], None
    for i, l in enumerate(ls):
        if l.strip() == "```":
            if open_i is None:
                open_i = i
            else:
                spans.append((open_i, i))
                open_i = None
    if open_i is not None:
        defects.append(("FENCE-UNBALANCED", "open ``` without close"))
    return spans


for fn in ALL:
    enp, rup = os.path.join(EN, fn), os.path.join(RU, fn)
    if not os.path.exists(rup):
        defects.append((fn, "RU file MISSING"))
        continue
    en, ru = rd(enp), rd(rup)
    el, rl = lines(en), lines(ru)

    # 1. line parity (EN == RU line count) -- structural canon L100
    if len(el) != len(rl):
        defects.append((fn, f"LINE-PARITY EN={len(el)} RU={len(rl)}"))

    # 2. heading parity (count of #, ##, ###, #### per level)
    for lvl in ("#### ", "### ", "## ", "# "):
        ec = sum(1 for l in el if l.startswith(lvl))
        rc = sum(1 for l in rl if l.startswith(lvl))
        if ec != rc:
            defects.append((fn, f"HEADING-PARITY '{lvl.strip()}' EN={ec} RU={rc}"))

    # 3. table-row parity
    e_tr = sum(1 for l in el if l.lstrip().startswith("|"))
    r_tr = sum(1 for l in rl if l.lstrip().startswith("|"))
    if e_tr != r_tr:
        defects.append((fn, f"TABLE-ROW-PARITY EN={e_tr} RU={r_tr}"))

    # 4. fence parity + force-sync (EN code-fence content must be byte-identical in RU)
    es, rs = code_fence_spans(el), code_fence_spans(rl)
    if len(es) != len(rs):
        defects.append((fn, f"FENCE-COUNT EN={len(es)} RU={len(rs)}"))
    else:
        for (ea, eb), (ra, rb) in zip(es, rs):
            eblk, rblk = el[ea : eb + 1], rl[ra : rb + 1]
            if eblk != rblk:
                defects.append(
                    (
                        fn,
                        f"FENCE-DRIFT lines EN[{ea + 1}:{eb + 1}] != RU[{ra + 1}:{rb + 1}]",
                    )
                )

    # 5. em-dash (CLAUDE rule #0) -- never self-add em/en dash
    for i, l in enumerate(rl):
        if "—" in l or "–" in l:
            # allow only if same char present in EN same line index
            en_l = el[i] if i < len(el) else ""
            if ("—" in l and "—" not in en_l) or ("–" in l and "–" not in en_l):
                defects.append((fn, f"EM-DASH self-added line {i + 1}: {l[:80]}"))

    # 6. mojibake / BOM
    for i, l in enumerate(rl):
        for m in MOJIBAKE:
            if m in l:
                defects.append((fn, f"MOJIBAKE '{m}' line {i + 1}: {l[:60]}"))

    # 7. EN-invariants identical (title frontmatter, H1x2, * Reference, * Published/Updated)
    #    config-api L99: title + H1x2 + Reference + Published/Updated = EN-verbatim
    e_title = next((l for l in el if l.startswith("title:")), None)
    r_title = next((l for l in rl if l.startswith("title:")), None)
    if e_title != r_title:
        defects.append((fn, f"TITLE not EN-verbatim: EN={e_title!r} RU={r_title!r}"))
    e_h1 = [l for l in el if re.match(r"^# \S", l)]
    r_h1 = [l for l in rl if re.match(r"^# \S", l)]
    if e_h1 != r_h1:
        defects.append((fn, f"H1 not EN-verbatim: EN={e_h1} RU={r_h1}"))
    for pref in EN_INVARIANT_PREFIXES:
        e_inv = [l for l in el if l.startswith(pref)]
        r_inv = [l for l in rl if l.startswith(pref)]
        if e_inv != r_inv:
            defects.append((fn, f"INVARIANT '{pref.strip()}' EN={e_inv} RU={r_inv}"))

    # 8. URL preservation: every (url) and "anchor" from EN must appear in RU
    en_urls = set(re.findall(r"\]\((/[^\s\)\"]+|https?://[^\s\)\"]+)", en))
    ru_urls = set(re.findall(r"\]\((/[^\s\)\"]+|https?://[^\s\)\"]+)", ru))
    miss = en_urls - ru_urls
    if miss:
        defects.append((fn, f"URL-LOST: {sorted(miss)[:4]}"))

    # 9. leftover-EN section headers (## / ### / #### that are still English prose)
    for i, l in enumerate(rl):
        s = l.strip()
        if re.match(r"^#{2,4}\s", s):
            txt = s.lstrip("#").strip()
            if txt in ALLOWED_EN_HEADERS or s in ALLOWED_EN_HEADERS:
                continue
            # heuristic: header that is pure ASCII English words and not a known EN-lock token
            if re.match(r"^[A-Za-z][A-Za-z0-9 '`/-]+$", txt) and txt not in ("Curl",):
                # allow EN-lock feature tokens inside heading (credentials, maintenance window, allowlist)
                low = txt.lower()
                if any(
                    tok in low
                    for tok in (
                        "credential",
                        "maintenance window",
                        "allowlist",
                        "privatelink",
                    )
                ):
                    continue
                defects.append((fn, f"LEFTOVER-EN header line {i + 1}: {s}"))

    # 10. no leftover raw English boilerplate sentences (L99 prose must be translated)
    EN_BOILER = [
        "The request produces an",
        "The request consumes an",
        "To execute this request, you need an access token",
        "The request doesn't provide any configurable parameters",
        "In this example, the request lists",
        "The API token is passed in the",
        "This API is deprecated. Use the",
        "Lists all",
        "Get an overview of",
        "Get the parameters of",
        "enables you to manage",
        "you no longer need",
    ]
    in_fence = set()
    for a, b in rs:
        in_fence.update(range(a, b + 1))
    for i, l in enumerate(rl):
        if i in in_fence:
            continue
        for b in EN_BOILER:
            if b in l:
                defects.append((fn, f"LEFTOVER-EN-PROSE line {i + 1}: {l[:70]!r}"))
                break

# banner-verbatim checks (must equal endpoint-locked canon)
k8s = rd(os.path.join(RU, "k8s-credentials-api-api.md"))
if BANNER_K8S not in k8s:
    defects.append(
        ("k8s-credentials-api-api.md", "BANNER not verbatim-match endpoint RU canon")
    )
mw = rd(os.path.join(RU, "maintenance-windows-api.md"))
if BANNER_MW not in mw:
    defects.append(
        ("maintenance-windows-api.md", "BANNER not verbatim-match endpoint RU canon")
    )

# period-by-source spot check (L101) for supported-services element rows
for fn in SUPPORTED:
    en, ru = rd(os.path.join(EN, fn)), rd(os.path.join(RU, fn))
    for key in ("cloudProviderServiceType", "displayName", "entityType", "name"):
        em = re.search(rf"\| {key} \| string \| (.+?) \|", en)
        rm = re.search(rf"\| {key} \| string \| (.+?) \|", ru)
        if em and rm:
            ep, rp = (
                em.group(1).rstrip().endswith("."),
                rm.group(1).rstrip().endswith("."),
            )
            if ep != rp:
                defects.append((fn, f"L101 period mismatch '{key}': EN.={ep} RU.={rp}"))

print("=" * 64)
print(f"BATCH L4R REVIEW — {len(ALL)} files")
print("=" * 64)
if not defects:
    print("0 DEFECTS — structural + force-sync + semantic spot-check clean.")
    sys.exit(0)
for f, d in defects:
    print(f"  [{f}] {d}")
print(f"\nTOTAL DEFECTS: {len(defects)}")
sys.exit(1)
