# -*- coding: utf-8 -*-
"""Review-script for L4-AG.1a.8 batch (anchor: L4-AG.1a.7 review canon)."""

import io, os, re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-kubernetes-generic-metadata-enrichment.md",
    "builtin-appsec-third-party-vulnerability-kubernetes-label-rule-settings.md",
    "builtin-logmonitoring-timestamp-configuration.md",
    "builtin-davis-anomaly-detectors.md",
    "builtin-anomaly-detection-rum-mobile-crash-rate-increase.md",
    "builtin-logmonitoring-custom-log-source-settings.md",
    "builtin-anomaly-detection-rum-custom-crash-rate-increase.md",
    "builtin-container-built-in-monitoring-rule.md",
    "builtin-cloud-kubernetes-monitoring.md",
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
                    hits.append((i, needle, ln.strip()[:120]))
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


def main():
    issues = []
    for rel in PILOT:
        ru_path = os.path.join(RU, rel)
        ru_text = io.open(ru_path, "r", encoding="utf-8").read()
        for ln_no, ln in find_em_dash(ru_text):
            issues.append((rel, ln_no, "em-dash in RU", ln.strip()[:120]))
        for msg in check_struct(ru_text):
            issues.append((rel, 0, "struct leftover", msg))
        for ln_no, needle, snippet in find_calque_and(ru_text):
            issues.append((rel, ln_no, f"possible calque {needle!r}", snippet))
    print(f"Total issues found: {len(issues)}")
    for rel, ln, kind, snippet in issues:
        print(f"  [{rel}:{ln}] {kind}: {snippet}")
    print()
    print("OK" if not issues else "REVIEW NEEDED")


if __name__ == "__main__":
    main()
