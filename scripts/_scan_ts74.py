# -*- coding: utf-8 -*-
"""Scan a managed/ EN file and list every translatable line NOT yet covered by
an optional existing builder's TRANS/PASS. Reproduces build_one's filtering
(fence/blank/---/source/scraped/demoji/norm) so the printed set is exactly what
build_one still needs. Dedup by norm, first-appearance order.

Usage:
    python3 _scan_ts74.py <rel_dir> <fname> [builder.py]
"""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _otel_canon import norm, read_lf
import _zos_canon_l4if71 as eng

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")


def load_builder_maps(builder_path):
    """Exec a per-file builder with build_one/qa_one mocked, capture TRANS/PASS."""
    cap = {"trans": {}, "pass": set()}

    def fake_build_one(rel_dir, fname, trans, passset=frozenset()):
        cap["trans"] = dict(trans)
        cap["pass"] = set(passset)

    orig_bo, orig_qa = eng.build_one, eng.qa_one
    eng.build_one = fake_build_one
    eng.qa_one = lambda *a, **k: (0, 0, [])
    try:
        spec = importlib.util.spec_from_file_location("_b_probe", builder_path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
    finally:
        eng.build_one, eng.qa_one = orig_bo, orig_qa
    return cap["trans"], cap["pass"]


def main():
    rel_dir, fname = sys.argv[1], sys.argv[2]
    covered = set()
    if len(sys.argv) > 3:
        trans, passset = load_builder_maps(sys.argv[3])
        covered = {norm(eng._demoji(k)) for k in trans} | {
            norm(eng._demoji(k)) for k in passset
        }
        print(f"# builder covers {len(covered)} norm-keys", file=sys.stderr)

    en_lines = read_lf(os.path.join(BASE, "managed", rel_dir, fname)).split("\n")
    in_fence = False
    seen = set()
    missing = []
    for ln in en_lines:
        raw = eng._demoji(ln.strip())
        st = norm(raw)
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or st == "" or st == "---":
            continue
        if raw.startswith("source:") or raw.startswith("scraped:"):
            continue
        if st in covered or st in seen:
            continue
        seen.add(st)
        missing.append(raw)
    print(f"# {fname}: {len(missing)} uncovered translatable lines", file=sys.stderr)
    for r in missing:
        print(f"    {r!r}: ,")


if __name__ == "__main__":
    main()
