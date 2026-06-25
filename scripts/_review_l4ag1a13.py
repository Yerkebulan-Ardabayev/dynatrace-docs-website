# -*- coding: utf-8 -*-
"""Review L4-AG.1a.13 RU files for EN-leftovers and other defects."""

import io, os, re as _re

RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"
FILES = [
    "builtin-alerting-maintenance-window.md",
    "builtin-alerting-profile.md",
    "builtin-anomaly-detection-infrastructure-aws.md",
    "builtin-anomaly-detection-infrastructure-vmware.md",
    "builtin-anomaly-detection-kubernetes-workload.md",
    "builtin-failure-detection-rulesets.md",
    "builtin-monitoredentities-generic-type.md",
    "builtin-process-built-in-process-monitoring-rule.md",
    "builtin-process-group-detection-flags.md",
    "builtin-process-grouping-rules.md",
    "builtin-service-detection-external-web-request.md",
    "builtin-service-detection-external-web-service.md",
    "builtin-service-detection-full-web-request.md",
    "builtin-service-detection-full-web-service.md",
]

# EN-signal-word patterns. Should appear ONLY inside code/identifiers,
# not as standalone phrases in translated prose.
SIGNAL_WORDS = [
    "Alert if ",
    "Dynatrace learns ",
    "Choose whether ",
    "Choose how ",
    "Note that ",
    "Defines whether ",
    "Defines what ",
    "Define a pattern",
    "Define filters",
    "Define rulesets",
    "Define severity",
    "Define event",
    "Specify the source",
    "Specify a filter",
    "Specify a list",
    "Specify all sources",
    "If multiple values",
    "Used to ",
    "Type of entities",
    "Status codes ",
    "Evaluated attribute:",
    "Evaluated expression:",
    "Failure detection result:",
    "Override failures",
    "Custom rule based",
    "Enabling this flag",
    "Enable to ",
    "By default,",
    "Take care that",
    "When this field is empty",
    "When enabled,",
    "Pick which",
    "Detect the matching",
    "Contributors to the Service",
    "A list of conditions",
    "A short description",
    "A specific entity",
    "Add filters",
    "Send a notification",
    "Entities which",
    "Maintenance windows are",
    "Alerting profiles enable",
    "Rules are evaluated",
    "Rule conditions are evaluated",
    "All of the Contributors",
    "Dynatrace automatically detects",
    "Dynatrace automatically monitors",
    "More extensive information",
    "Looking for topology",
    "A generic type allows",
    "ID patterns are comprised",
    "Define process groups",
    "Define process detection",
    "If Dynatrace detects",
    "Set advanced options",
    "Auto reports only",
    "Valid only for",
    "Limits the scope",
    "If enabled,",
    "Define failure reasons",
    "Define escaped exceptions",
]


def main():
    total_defects = 0
    for rel in FILES:
        path = os.path.join(RU, rel)
        with io.open(path, "r", encoding="utf-8") as f:
            text = f.read()
        defects = []
        # 1. em-dash
        if " — " in text or "— " in text:
            cnt = text.count("—")
            defects.append(f"em-dash x{cnt}")
        # 2. real BOM
        if text.startswith("﻿"):
            defects.append("BOM")
        # 3. ENUM leftover
        if "The element has these enums" in text:
            cnt = text.count("The element has these enums")
            defects.append(f"ENUM EN x{cnt}")
        # 4. Authentication/Parameters EN
        if "## Authentication\n" in text or "\n## Parameters\n" in text:
            defects.append("## Authentication/Parameters EN")
        # 5. calque ", и " / ", или " (only flag — may be false positive)
        if ", и " in text:
            defects.append(f"calque ', и ' x{text.count(', и ')}")
        if ", или " in text:
            defects.append(f"calque ', или ' x{text.count(', или ')}")
        # 6. EN-signal-words
        signal_hits = []
        for w in SIGNAL_WORDS:
            if w in text:
                signal_hits.append(f"{w!r} x{text.count(w)}")
        if signal_hits:
            defects.append("EN-signal: " + "; ".join(signal_hits))
        # 7. mojibake single-a leftover (bytes-level)
        raw = text.encode("utf-8")
        single_a_real = raw.count(b"\xc3\xa2") - (
            raw.count(b"\xc3\xa2\xc2\x80\xc2\x99")
            + raw.count(b"\xc3\xa2\xc2\x80\xc2\x93")
            + raw.count(b"\xc3\xa2\xc2\x80\xc2\x94")
            + raw.count(b"\xc3\xa2\xc2\x80\xc2\x91")
            + raw.count(b"\xc3\xa2\xc2\x80\xc2\x9c")
            + raw.count(b"\xc3\xa2\xc2\x80\xc2\x9d")
            + raw.count(b"\xc3\xa2\xc2\x9a\xc2\xa0\xc3\xaf\xc2\xb8\xc2\x8f")
        )
        if single_a_real > 0:
            defects.append(f"single-a leftover x{single_a_real}")
        # 8. mojibake-BOM leftover
        if "ï»¿" in text:
            defects.append(f"mojibake-BOM ï»¿ x{text.count('ï»¿')}")
        # 9. double-B Davis
        if "Â®" in text:
            defects.append(f"double-B Â® x{text.count('Â®')}")
        # report
        if defects:
            total_defects += 1
            print(f"  ✗ {rel}")
            for d in defects:
                print(f"      - {d}")
        else:
            print(f"  ✓ {rel}")
    print()
    print(f"SUMMARY: {total_defects} files with defects out of {len(FILES)}")


if __name__ == "__main__":
    main()
