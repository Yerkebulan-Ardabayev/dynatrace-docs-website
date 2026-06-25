#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA for the L4-IF.49 AWS storage/network batch. Reuses e44 QA checks verbatim
(line-parity, frontmatter byte-eq, em-dash, mojibake/BOM, URL multiset, heading
parity, fence byte-identity, DESC-NOCYR, pure-Latin-heading, EN-prose-leftover)
over _aws_batch49.txt."""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
import _qa_aws_l4if44 as Q
HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    files = [x.strip() for x in open(os.path.join(HERE, "_aws_batch49.txt"), encoding="utf-8") if x.strip()]
    for f in files:
        Q.qa_file(f)
    print(f"QA AWS L4-IF.49: {len(files)} files | FAIL={len(Q.problems)} WARN={len(Q.warnings)}")
    if Q.problems:
        print("--- FAIL ---")
        for p in Q.problems:
            print(" ", p)
    if Q.warnings:
        print("--- WARN ---")
        for w in Q.warnings[:80]:
            print(" ", w)
    return 1 if Q.problems else 0

if __name__ == "__main__":
    sys.exit(main())
