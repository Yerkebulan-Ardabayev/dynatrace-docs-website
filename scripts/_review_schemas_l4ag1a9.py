# -*- coding: utf-8 -*-
"""Review-script for L4-AG.1a.9 batch (anchor: L4-AG.1a.8 review canon).

Checks: em-dash in RU, struct leftover (`## Authentication`, ENUM-phrase,
table-header), calque `, и `/`, или ` (excluding 2-element coordinations),
mojibake drift count (RU should be ≤ EN: triple/single/double-B/BOMJ).
"""

import io, os

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-monitoring-slo.md",
    "builtin-rum-web-enablement.md",
    "builtin-service-detection-v2-for-oneagent.md",
    "builtin-custom-metrics.md",
    "builtin-synthetic-multiprotocol-config.md",
    "builtin-user-action-custom-metrics.md",
    "builtin-metric-metadata.md",
    "builtin-declarativegrouping.md",
    "builtin-rum-web-automatic-injection.md",
    "builtin-anomaly-detection-infrastructure-disks.md",
    "builtin-logmonitoring-log-agent-configuration.md",
    "builtin-url-path-pattern-matching-rules.md",
]


def find_em_dash(text):
    return [(i + 1, ln) for i, ln in enumerate(text.split("\n")) if "—" in ln]


def find_calque_and(text):
    hits = []
    for i, ln in enumerate(text.split("\n"), 1):
        for needle in (", и ", ", или "):
            if needle in ln:
                pre = ln.split(needle)[0]
                if pre.count(",") >= 1:
                    hits.append((i, needle, ln.strip()[:140]))
    return hits


def check_struct(ru_text):
    issues = []
    if "## Authentication" in ru_text:
        issues.append("`## Authentication` leftover")
    if "The element has these enums" in ru_text:
        issues.append("ENUM-phrase leftover")
    if "| Property | Type | Description | Required |" in ru_text:
        issues.append("table-header leftover")
    return issues


def count_mojibake(text):
    bom = text.count(chr(0xFEFF))
    bomj = text.count(chr(0xEF) + chr(0xBB) + chr(0xBF))
    triple = text.count(chr(0xE2) + chr(0x80) + chr(0x99))
    a_total = text.count(chr(0xE2))
    single = a_total - triple  # 1-char "â"
    doubleB = text.count(chr(0xC2) + chr(0xAE))
    return {
        "BOM": bom,
        "BOMJ": bomj,
        "single_a": single,
        "triple": triple,
        "doubleB": doubleB,
    }


def main():
    issues = []
    for rel in PILOT:
        ru_path = os.path.join(RU, rel)
        en_path = os.path.join(EN, rel)
        ru_text = io.open(ru_path, "r", encoding="utf-8").read()
        en_text = io.open(en_path, "r", encoding="utf-8").read()
        # em-dash
        for ln_no, ln in find_em_dash(ru_text):
            issues.append((rel, ln_no, "em-dash in RU", ln.strip()[:140]))
        # struct leftover
        for msg in check_struct(ru_text):
            issues.append((rel, 0, "struct leftover", msg))
        # calque
        for ln_no, needle, snippet in find_calque_and(ru_text):
            issues.append((rel, ln_no, f"possible calque {needle!r}", snippet))
        # mojibake drift: RU should have ≤ EN counts (we strip BOMJ; we keep
        # single/triple inside translated text as-is because they're inside
        # mojibake-en-dash markers like `low-volatility` which we already
        # rewrote with hyphen — so RU should have 0 single/triple/doubleB)
        en_m = count_mojibake(en_text)
        ru_m = count_mojibake(ru_text)
        for k in ("BOM", "BOMJ", "single_a", "triple", "doubleB"):
            if ru_m[k] > 0:
                issues.append(
                    (rel, 0, f"mojibake leftover {k}", f"EN={en_m[k]} RU={ru_m[k]}")
                )
    print(f"Total issues found: {len(issues)}")
    for rel, ln, kind, snippet in issues:
        print(f"  [{rel}:{ln}] {kind}: {snippet}")
    print()
    print("OK" if not issues else "REVIEW NEEDED")


if __name__ == "__main__":
    main()
