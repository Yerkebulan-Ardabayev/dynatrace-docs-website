# -*- coding: utf-8 -*-
"""Mojibake audit for L4-AG.1a.13 batch."""

import io, os

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
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

# bytes-level patterns
PATTERNS = {
    "bom_utf8": b"\xef\xbb\xbf",  # only at start = real BOM
    "single_a": b"\xc3\xa2",  # â
    "triple_apos": b"\xc3\xa2\xc2\x80\xc2\x99",  # '
    "triple_endash": b"\xc3\xa2\xc2\x80\xc2\x93",  # –
    "triple_emdash": b"\xc3\xa2\xc2\x80\xc2\x94",  # —
    "triple_nbhyph": b"\xc3\xa2\xc2\x80\xc2\x91",  # ‑
    "triple_lquote": b"\xc3\xa2\xc2\x80\xc2\x9c",  # "
    "triple_rquote": b"\xc3\xa2\xc2\x80\xc2\x9d",  # "
    "double_B_R": b"\xc3\x82\xc2\xae",  # Â®
    "double_dec_warn": b"\xc3\xa2\xc2\x9a\xc2\xa0\xc3\xaf\xc2\xb8\xc2\x8f",  # ⚠️
    "mojibake_bom_inline": b"\xc3\xaf\xc2\xbb\xc2\xbf",  # ï»¿ encoded
}


def hex_around(data: bytes, idx: int, span: int = 24) -> str:
    lo = max(0, idx - span)
    hi = min(len(data), idx + span)
    return data[lo:hi].hex()


def main():
    total = {k: 0 for k in PATTERNS}
    per_file = {}
    for rel in FILES:
        with open(os.path.join(EN, rel), "rb") as f:
            raw = f.read()
        row = {}
        for k, pat in PATTERNS.items():
            cnt = raw.count(pat)
            row[k] = cnt
            total[k] += cnt
        # single_a real = total occurrences minus those embedded in triples
        triple_share = (
            row["triple_apos"]
            + row["triple_endash"]
            + row["triple_emdash"]
            + row["triple_nbhyph"]
            + row["triple_lquote"]
            + row["triple_rquote"]
        )
        row["single_a_real"] = row["single_a"] - triple_share
        per_file[rel] = row

    # print summary
    cols = [
        "bom_utf8",
        "single_a",
        "single_a_real",
        "triple_apos",
        "triple_endash",
        "triple_emdash",
        "triple_nbhyph",
        "triple_lquote",
        "triple_rquote",
        "double_B_R",
        "double_dec_warn",
        "mojibake_bom_inline",
    ]
    print("%-60s %s" % ("file", " ".join("%4s" % c[:4] for c in cols)))
    for rel, row in per_file.items():
        print("%-60s %s" % (rel, " ".join("%4d" % row[c] for c in cols)))
    print()
    print("TOTAL:")
    for c in cols:
        if c == "single_a_real":
            tot = total["single_a"] - (
                total["triple_apos"]
                + total["triple_endash"]
                + total["triple_emdash"]
                + total["triple_nbhyph"]
                + total["triple_lquote"]
                + total["triple_rquote"]
            )
            print("  %-22s %d" % (c, tot))
        else:
            print("  %-22s %d" % (c, total[c]))


if __name__ == "__main__":
    main()
