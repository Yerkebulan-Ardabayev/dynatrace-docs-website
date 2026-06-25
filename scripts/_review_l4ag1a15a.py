# -*- coding: utf-8 -*-
"""L4-AG.1a.15a review script — output to file."""

import re, io, os

RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"
FILES = [
    "builtin-infrastructure-disk-edge-anomaly-detectors.md",
    "builtin-management-zones.md",
    "builtin-os-services-monitoring.md",
    "builtin-tags-auto-tagging.md",
    "builtin-anomaly-detection-infrastructure-hosts.md",
]
SIG_WORDS = [
    "Alert if",
    "Choose whether",
    "Note that",
    "Dynatrace learns",
    "Matches if",
    "Matches services",
    "Matches string",
    "When enabled,",
    "Detect ",
    "Detection mode for",
    "Receive/transmit ",
    "Toggle the switch",
    "Set of additional",
    "Set of rules",
    "Specify disk",
    "Host resource attributes are",
    "Tagging rules are",
    "Depending on environment-size",
    "Management zones enable",
    "For each Management",
    "For value suggestions",
    "Management zone rules",
    "Set up alerts for OS",
    "Please provide feedback",
    "In order to set up",
    "Dynatrace automatically detects",
    "The number of",
    "By default, Dynatrace",
    "Tags simplify",
    "In dynamic or large",
]

report = []
for f in FILES:
    b = io.open(f"{RU}/{f}", "rb").read()
    t = b.decode("utf-8")
    em = t.count(chr(0x2014))
    bomj = b.count(b"\xc3\xaf\xc2\xbb\xc2\xbf") + b.count(b"\xef\xbb\xbf")
    enum_left = t.count("The element has these enums")
    auth_left = t.count("## Authentication")
    param_left = t.count("## Parameters")
    single_a = (
        b.count(b"\xc3\xa2")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x93")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x99")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x94")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x91")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x9c")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x9d")
    )
    # calque
    calque_hits = re.findall(r"(, и \w+|, или \w+)", t)
    calque_contexts = []
    for m in re.finditer(r"(, и \w+|, или \w+)", t):
        s, e = m.span()
        calque_contexts.append(t[max(0, s - 60) : min(len(t), e + 60)])
    sig_hits = []
    for w in SIG_WORDS:
        n = t.count(w)
        if n:
            sig_hits.append(f"{w}({n})")
            for m in re.finditer(re.escape(w), t):
                s, e = m.span()
                sig_hits.append("  ctx: " + t[max(0, s - 60) : min(len(t), e + 60)])
    report.append(
        f"--- {f} ---\n"
        f"em-dash={em}, mojibake-BOM={bomj}, ENUM-left={enum_left}, "
        f"Auth-left={auth_left}, Param-left={param_left}, single_a={single_a}\n"
        f"calque hits ({len(calque_hits)}):\n"
        + "\n".join("  " + c for c in calque_contexts)
        + ("\n" if calque_contexts else "")
        + f"signal-words hits:\n"
        + "\n".join(sig_hits)
        + "\n"
    )

io.open("scripts/_review_l4ag1a15a_report.txt", "w", encoding="utf-8").write(
    "\n".join(report)
)
print("Report written.")
