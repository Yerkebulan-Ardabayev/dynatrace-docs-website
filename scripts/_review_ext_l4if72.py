# -*- coding: utf-8 -*-
"""L4-IF.72 critical-review scanner — catches defects STRUCTURAL QA is blind to.

Blindspots (from feedback_translation_qa_blindspots):
  #9  untranslated tooltip behind a translated/any link  -> "EN tooltip"
  #15 img alt that stayed EN (alt!=caption)
  #11 over-eager `word: это` (should be `word, это`)
  #12 quantifier + indeclinable EN noun
  mixed-line: a line WITH Cyrillic that still hides a 3+ EN-word run
  EN H1/title left untranslated
  cross-file term drift (forbidden variants)
Run from repo root: python scripts/_review_ext_l4if72.py
"""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
ROOT = "ingest-from/extensions"
RU = os.path.join(BASE, "managed-ru", ROOT)

CYR = re.compile(r"[А-Яа-яЁё]")
TIP = re.compile(r'"\s*([^"]+?)\s*"\)')  # "tooltip")  after a url
ALT = re.compile(r"!\[([^\]]*)\]\(")
LINKTXT = re.compile(r"\[([^\]]+)\]\([^)]*\)")
URL = re.compile(r"https?://\S+|\]\([^)]*\)")
ENRUN = re.compile(r"\b[A-Za-z][a-z]{2,}(?:\s+[a-z]{2,}){2,}\b")  # 3+ english words

# Forbidden term variants -> canonical (cross-file drift)
DRIFT = {
    r"\bплагин": "extension/расширение (not плагин)",
    r"\bконечн\w* точк": "эндпоинт (corpus split; this batch uses эндпоинт)",
    r"\bнабор\w* возможностей": "набор функций",
    r"\bтрейс\w*": "трассировка (not трейс)",
    r"\bконвейер\w*\b": "(check: pipeline ctx)",
}

files = []
for r, _, fs in os.walk(RU):
    for fn in fs:
        if fn.endswith(".md"):
            files.append(os.path.join(r, fn))
files.sort()


def rel(p):
    return os.path.relpath(p, RU).replace("\\", "/")


def strip_code_inline(s):
    s = re.sub(r"`[^`]*`", "", s)
    s = re.sub(r"\([^)]*\)", "", s)  # url parens
    return s


hits = {
    k: []
    for k in ["tooltip", "alt", "colon_eto", "mixedEN", "enH1", "drift", "calque2"]
}

CAL2 = re.compile(
    r"\b(вы сможете|вам нужно|вам потребуется|вам необходимо|"
    r"если вы|когда вы|вы увидите|вы получите|позволяет вам|"
    r"вы хотите|вы можете|даёт вам|вы создаёте)\b",
    re.I,
)

for p in files:
    lines = open(p, encoding="utf-8").read().split("\n")
    infence = False
    for i, l in enumerate(lines):
        if l.strip().startswith("```"):
            infence = not infence
            continue
        if infence:
            continue
        ln = i + 1
        # --- untranslated tooltip ---
        for m in TIP.finditer(l):
            tip = m.group(1)
            if tip and not CYR.search(tip) and not re.fullmatch(r"[\w./:+-]+", tip):
                hits["tooltip"].append((rel(p), ln, tip[:60]))
        # --- img alt without Cyrillic (potential alt!=caption) ---
        for m in ALT.finditer(l):
            alt = m.group(1)
            if alt and not CYR.search(alt) and len(alt.split()) >= 2:
                hits["alt"].append((rel(p), ln, alt[:50]))
        # --- word: это over-correction ---
        for m in re.finditer(r"([а-яё]+):\s+это\b", l, re.I):
            hits["colon_eto"].append((rel(p), ln, l.strip()[:60]))
        # --- EN H1 / title (no Cyrillic on a heading or title line) ---
        s = l.strip()
        if (s.startswith("# ") or s.startswith("title:")) and not CYR.search(s):
            # ignore pure-identifier/product H1 (single token or .spec paths)
            body = s.lstrip("#").replace("title:", "").strip()
            if len(body.split()) >= 2:
                hits["enH1"].append((rel(p), ln, body[:60]))
        # --- mixed line: has Cyrillic but also a 3+ EN-word run ---
        if CYR.search(l):
            bare = strip_code_inline(l)
            bare = re.sub(r"[*#>|]", " ", bare)
            for m in ENRUN.finditer(bare):
                run = m.group(0)
                # skip known kept-EN product strings
                if run.lower() in ("data source", "feature set"):
                    continue
                hits["mixedEN"].append((rel(p), ln, run[:50]))
        # --- calque variants ---
        if CAL2.search(l):
            hits["calque2"].append((rel(p), ln, CAL2.search(l).group(0)))
        # --- drift terms ---
        for pat, canon in DRIFT.items():
            if re.search(pat, l, re.I):
                hits["drift"].append(
                    (rel(p), ln, f"{re.search(pat, l, re.I).group(0)} -> {canon}")
                )

for k in hits:
    print(f"\n===== {k}  ({len(hits[k])}) =====")
    for t in hits[k][:60]:
        print(f"  {t[0]}:{t[1]}  {t[2]}")
