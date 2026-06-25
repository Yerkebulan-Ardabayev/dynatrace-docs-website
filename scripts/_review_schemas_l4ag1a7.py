# -*- coding: utf-8 -*-
"""Review-script for L4-AG.1a.7 batch (anchor: L4-AG.1a.6 review canon)."""

import io, os, re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-hyperscaler-authentication-connections-azure.md",
    "builtin-disk-options.md",
    "builtin-mainframe-txmonitoring.md",
    "builtin-rum-web-key-performance-metric-load-actions.md",
    "builtin-container-technology.md",
    "builtin-oneagent-side-masking-settings.md",
    "builtin-anomaly-detection-kubernetes-pvc.md",
    "builtin-appsec-code-level-vulnerability-rule-settings.md",
    "builtin-appsec-third-party-vulnerability-rule-settings.md",
    "builtin-failure-detection-service-http-parameters.md",
]

# Heuristic: a line is "english leftover" if it has 2+ ascii words and no Cyrillic,
# excluding code-blocks, table separators, headers etc.
EN_LEFTOVER_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_'\- ]+[A-Za-z0-9](\.|:|!|\?)?$")
CYRILLIC_RE = re.compile(r"[А-Яа-яЁё]")


def find_em_dash(text):
    return [
        (i + 1, ln)
        for i, ln in enumerate(text.split("\n"))
        if "—" in ln  # em-dash
    ]


def find_calque_and(text):
    # ", и " or ", или " — flag only true 3+ element enumerations.
    hits = []
    for i, ln in enumerate(text.split("\n"), 1):
        for needle in (", и ", ", или "):
            if needle in ln:
                # Count preceding commas in the same sentence-fragment to avoid
                # false-positives on participial closes / compound sentences.
                pre = ln.split(needle)[0]
                # crude: at least one other comma in the run-up suggests 3+ items
                if pre.count(",") >= 1:
                    hits.append((i, needle, ln.strip()[:120]))
    return hits


def find_mojibake_drift(en_data, ru_data):
    en_single = en_data.count(b"\xc3\xa2") - en_data.count(b"\xc3\xa2\xc2\x80\xc2\x99")
    en_triple = en_data.count(b"\xc3\xa2\xc2\x80\xc2\x99")
    en_doubleB = en_data.count(b"\xc3\x82\xc2\xae")
    en_bomj = en_data.count(
        b"\xef\xbb\xbf"
    )  # mojibake-BOM inside text (not at offset 0)
    if en_data.startswith(b"\xef\xbb\xbf"):
        en_bomj -= 1  # we strip real BOM, not a drift
    ru_single = ru_data.count(b"\xc3\xa2") - ru_data.count(b"\xc3\xa2\xc2\x80\xc2\x99")
    ru_triple = ru_data.count(b"\xc3\xa2\xc2\x80\xc2\x99")
    ru_doubleB = ru_data.count(b"\xc3\x82\xc2\xae")
    ru_bomj = ru_data.count(b"\xef\xbb\xbf")
    if ru_data.startswith(b"\xef\xbb\xbf"):
        ru_bomj -= 1
    return {
        "single": (en_single, ru_single),
        "triple": (en_triple, ru_triple),
        "doubleB": (en_doubleB, ru_doubleB),
        "bomj": (en_bomj, ru_bomj),
    }


def check_struct(ru_text):
    issues = []
    if "## Authentication" in ru_text:
        issues.append("`## Authentication` leftover")
    if "The element has these enums" in ru_text:
        issues.append("`The element has these enums` enum-phrase leftover")
    if "| Property | Type | Description | Required |" in ru_text:
        issues.append(
            "`| Property | Type | Description | Required |` table-header leftover"
        )
    return issues


def main():
    issues = []
    for rel in PILOT:
        en_path = os.path.join(EN, rel)
        ru_path = os.path.join(RU, rel)
        en_text = io.open(en_path, "r", encoding="utf-8").read().replace("\r\n", "\n")
        ru_text = io.open(ru_path, "r", encoding="utf-8").read()
        en_data = open(en_path, "rb").read()
        ru_data = open(ru_path, "rb").read()
        # 1. em-dash
        dashes = find_em_dash(ru_text)
        for ln_no, ln in dashes:
            issues.append((rel, ln_no, "em-dash in RU", ln.strip()[:120]))
        # 2. struct leftover
        for msg in check_struct(ru_text):
            issues.append((rel, 0, "struct leftover", msg))
        # 3. mojibake drift
        moji = find_mojibake_drift(en_data, ru_data)
        for kind, (en_c, ru_c) in moji.items():
            if en_c != ru_c:
                issues.append(
                    (
                        rel,
                        0,
                        f"mojibake drift {kind}",
                        f"EN={en_c}, RU={ru_c} (drift acceptable if EN-paragraph fully replaced)",
                    )
                )
        # 4. calque ", и " / ", или "
        for ln_no, needle, snippet in find_calque_and(ru_text):
            issues.append((rel, ln_no, f"possible calque {needle!r}", snippet))
    print(f"Total issues found: {len(issues)}")
    for rel, ln, kind, snippet in issues:
        print(f"  [{rel}:{ln}] {kind}: {snippet}")
    print()
    print("OK" if not issues else "REVIEW NEEDED — inspect each issue manually")


if __name__ == "__main__":
    main()
