# -*- coding: utf-8 -*-
"""Review-script for L4-AG.1a.11 batch (anchor: L4-AG.1a.9 review canon).

Checks: em-dash in RU, struct leftover (`## Authentication`, ENUM-phrase,
table-header), calque `, и `/`, или ` (excluding 2-element coordinations),
mojibake drift count (RU should be 0 for single/triple/doubleB, BOMJ scrubbed
by _normalize). `single_a leftover` heuristic ловит ВСЕ типы triple (общий
c3 a2 префикс) - канон L4-AG.1a.9.
"""

import io, os

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-ownership-teams.md",
    "builtin-anomaly-detection-kubernetes-node.md",
    "builtin-anomaly-detection-kubernetes-namespace.md",
    "builtin-elasticsearch-user-session-export-settings-v2.md",
    "builtin-preferences-privacy.md",
    "builtin-process-group-cloud-application-workload-detection.md",
    "builtin-processavailability.md",
    "builtin-failure-detection-environment-parameters.md",
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
    triple_apos = text.count(chr(0xE2) + chr(0x80) + chr(0x99))
    triple_endash = text.count(chr(0xE2) + chr(0x80) + chr(0x93))
    triple_nbhyphen = text.count(chr(0xE2) + chr(0x80) + chr(0x91))
    a_total = text.count(chr(0xE2))
    single = a_total - triple_apos - triple_endash - triple_nbhyphen
    doubleB = text.count(chr(0xC2) + chr(0xAE))
    return {
        "BOM": bom,
        "BOMJ": bomj,
        "single_a": single,
        "triple_apos": triple_apos,
        "triple_endash": triple_endash,
        "triple_nbhyphen": triple_nbhyphen,
        "doubleB": doubleB,
    }


def main():
    issues = []
    for rel in PILOT:
        ru_path = os.path.join(RU, rel)
        en_path = os.path.join(EN, rel)
        ru_text = io.open(ru_path, "r", encoding="utf-8").read()
        en_text = io.open(en_path, "r", encoding="utf-8").read()
        for ln_no, ln in find_em_dash(ru_text):
            issues.append((rel, ln_no, "em-dash in RU", ln.strip()[:140]))
        for msg in check_struct(ru_text):
            issues.append((rel, 0, "struct leftover", msg))
        for ln_no, needle, snippet in find_calque_and(ru_text):
            issues.append((rel, ln_no, f"possible calque {needle!r}", snippet))
        en_m = count_mojibake(en_text)
        ru_m = count_mojibake(ru_text)
        for k in (
            "BOM",
            "BOMJ",
            "single_a",
            "triple_apos",
            "triple_endash",
            "triple_nbhyphen",
            "doubleB",
        ):
            if ru_m[k] > 0:
                issues.append(
                    (rel, 0, f"mojibake leftover {k}", f"EN={en_m[k]} RU={ru_m[k]}")
                )
    print(f"Total issues found: {len(issues)}")
    for rel, ln, kind, snippet in issues:
        print(f"  {rel}:{ln}  {kind}  {snippet}")


if __name__ == "__main__":
    main()
