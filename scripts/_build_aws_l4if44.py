#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.43 - build RU for AWS aws-service-*.md (first AWS-service batch).

Strategy (L4-IF.39/42 line-keyed + column-aware + flag-guard):
  * iterate EN lines, preserve line-parity by construction
  * auto-copy: blank / frontmatter delim / source|scraped / fences(+interior) /
    table separators / image lines / image captions (caption == alt) /
    pure-non-latin lines
  * frontmatter title + H1 -> TITLE / TRANS dict
  * table rows -> column-aware by the table's header signature
  * every other latin-prose line -> TRANS dict; miss -> FLAG (kept EN, logged)
Nothing is silently left English: a non-empty FLAG list blocks writing.

Scraper mojibake is normalized on the LOOKUP KEY only (built via chr(0x..),
ASCII-only in source per L4-IF.35); EN corpus is never modified. RU written
wb / LF / no trailing newline so the markdown formatter won't touch it.
"""

import os, re, json, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUB = "ingest-from/amazon-web-services/integrate-with-aws/aws-all-services"
EN_DIR = os.path.join(ROOT, "docs/managed", SUB)
RU_DIR = os.path.join(ROOT, "docs/managed-ru", SUB)
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_PATH = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_PATH = os.path.join(HERE, "_aws_titles_l4if43.json")
BATCH_PATH = os.path.join(HERE, "_aws_batch44.txt")


def load_json(p):
    if os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    return {}


TRANS = load_json(TRANS_PATH)
TITLES = load_json(TITLE_PATH)

# ---- fixed canon (from shipped Azure metric corpus) ----
UNIT = {
    "Count": "Количество",
    "Percent": "Процент",
    "Bytes": "Байт",
    "Byte": "Байт",
    "Gigabytes": "Гигабайт",
    "Gigabyte": "Гигабайт",
    "Milliseconds": "Миллисекунда",
    "Millisecond": "Миллисекунда",
    "Seconds": "Секунда",
    "Second": "Секунда",
    "Bytes/Second": "Байт в секунду",
    "Count/Second": "Количество в секунду",
    "Megabytes": "Мегабайт",
    "Kilobytes": "Килобайт",
    "None": "None",
    "": "",
}
APPLIC = {"Applicable": "Применимо", "Not applicable": "Не применимо", "": ""}

# header signature (tuple of EN cells) -> (translated header cells, per-col action)
#   action: 'en' copy as-is | 'tr' translate via TRANS | 'unit' | 'applic'
TABLES = {
    ("Name", "Description", "Unit", "Statistics", "Dimensions", "Recommended"): (
        [
            "Имя",
            "Описание",
            "Единица измерения",
            "Статистика",
            "Измерения",
            "Рекомендуется",
        ],
        ["en", "tr", "unit", "en", "en", "applic"],
    ),
    ("Name", "Permissions"): (["Имя", "Разрешения"], ["en", "en"]),
    ("AWS service", "Preset dashboard"): (
        ["Сервис AWS", "Предустановленный дашборд"],
        ["en", "applic"],
    ),
    ("Endpoint", "Service"): (["Конечная точка", "Сервис"], ["en", "en"]),
}

FLAGS = []  # (file, lineno, text)


# scraper mojibake = UTF-8 punctuation mis-decoded as latin-1. Sequences are
# built from raw byte values via chr() so the source stays ASCII-only and the
# Write tool / formatter can't collapse the invisible 0x80 byte (L4-IF.35/37).
def _seq(*bs):
    return "".join(chr(b) for b in bs)


_DEMOJI = [
    (_seq(0xE2, 0x80, 0xA6), "…"),  # ... ellipsis
    (_seq(0xE2, 0x80, 0x99), "’"),  # ' right single quote
    (_seq(0xE2, 0x80, 0x98), "‘"),  # ' left single quote
    (_seq(0xE2, 0x80, 0x9C), "“"),  # " left double quote
    (_seq(0xE2, 0x80, 0x9D), "”"),  # " right double quote
    (_seq(0xE2, 0x80, 0x93), "–"),  # en dash
    (_seq(0xE2, 0x80, 0x94), "—"),  # em dash
    (_seq(0xEF, 0xBB, 0xBF), ""),  # BOM / zero-width
    (_seq(0xC3, 0x97), "×"),  # multiplication sign (U+00D7 mis-decoded)
]


def demoji(s):
    for bad, good in _DEMOJI:
        if bad in s:
            s = s.replace(bad, good)
    return s


def split_cells(s):
    inner = s.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [c.strip() for c in inner.split("|")]


def is_sep_row(cells):
    return all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c != "")


LAT = re.compile(r"[A-Za-z]{2,}")
IMG = re.compile(r"^!\[.*\]\(.*\)\s*$")
IMG_ALT = re.compile(r"^!\[(.*?)\]\(.*\)\s*$")


def build_file(fname):
    en_path = os.path.join(EN_DIR, fname)
    with open(en_path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out = []
    in_fm = False
    in_fence = False
    cur_actions = None
    cur_header_out = None
    last_alt = None  # alt-text of the most recent image; its caption == alt -> copy EN
    for i, line in enumerate(lines):
        s = line.strip()
        # frontmatter
        if i == 0 and s == "---":
            in_fm = True
            out.append(line)
            continue
        if in_fm:
            if s == "---":
                in_fm = False
                out.append(line)
                continue
            if s.startswith("title:"):
                t = s[len("title:") :].strip()
                ru = TITLES.get(t)
                if ru is None:
                    FLAGS.append((fname, i, "TITLE: " + t))
                    out.append(line)
                else:
                    out.append("title: " + ru)
            else:
                out.append(line)  # source/scraped/etc
            continue
        # fences
        if s.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        # blank
        if s == "":
            out.append(line)
            continue
        # image line -> remember alt so its caption can be copied as EN
        m = IMG_ALT.match(s)
        if m:
            last_alt = m.group(1).strip()
            out.append(line)
            continue
        # image caption (text == preceding image's alt) -> copy EN (canon)
        if last_alt is not None and s == last_alt:
            out.append(line)
            last_alt = None
            continue
        last_alt = None  # any other non-blank line closes the image/caption window
        # table row?
        if s.startswith("|"):
            cells = split_cells(s)
            if is_sep_row(cells):
                out.append(line)
                continue
            sig = tuple(cells)
            if sig in TABLES:
                cur_header_out, cur_actions = TABLES[sig]
                out.append("| " + " | ".join(cur_header_out) + " |")
                continue
            if cur_actions and len(cells) == len(cur_actions):
                newc = []
                for c, act in zip(cells, cur_actions):
                    if act == "en":
                        newc.append(c)
                    elif act == "applic":
                        if c in APPLIC:
                            newc.append(APPLIC[c])
                        elif c in APPLIC.values():
                            newc.append(c)
                        else:
                            FLAGS.append((fname, i, "APPLIC?: " + c))
                            newc.append(c)
                    elif act == "unit":
                        if c in UNIT:
                            newc.append(UNIT[c])
                        else:
                            FLAGS.append((fname, i, "UNIT?: " + c))
                            newc.append(c)
                    elif act == "tr":
                        if c == "":
                            newc.append("")
                        elif not LAT.search(c):
                            newc.append(c)  # pure code/number
                        else:
                            key = demoji(c)
                            if key in TRANS and TRANS[key] != "":
                                newc.append(TRANS[key])
                            else:
                                FLAGS.append((fname, i, "CELL: " + key))
                                newc.append(c)
                out.append("| " + " | ".join(newc) + " |")
                continue
            FLAGS.append((fname, i, "ROW?: " + s[:80]))
            out.append(line)
            continue
        # pure code / punctuation / number line
        if not LAT.search(s):
            out.append(line)
            continue
        # prose / heading / list
        key = demoji(s)
        if key in TRANS and TRANS[key] != "":
            indent = line[: len(line) - len(line.lstrip())]
            out.append(indent + TRANS[key])
        else:
            FLAGS.append((fname, i, key))
            out.append(line)  # keep EN, flagged
    return "\n".join(out)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    with open(BATCH_PATH, encoding="utf-8") as fh:
        files = [x.strip() for x in fh if x.strip()]
    results = {}
    for f in files:
        results[f] = build_file(f)
    if FLAGS:
        from collections import Counter

        uniq = Counter(t for (_, _, t) in FLAGS)
        skel = {
            t: ""
            for t in uniq
            if not t.startswith(("TITLE:", "UNIT?:", "APPLIC?:", "ROW?:"))
        }
        with open(
            os.path.join(HERE, "_aws_missing_l4if44.json"), "w", encoding="utf-8"
        ) as wf:
            json.dump(skel, wf, ensure_ascii=False, indent=1)
        with open(
            os.path.join(HERE, "_aws_flags_report44.txt"), "w", encoding="utf-8"
        ) as wf:
            wf.write(f"FLAGS: {len(FLAGS)} | unique: {len(uniq)}\n" + "=" * 60 + "\n")
            for t, n in uniq.most_common():
                wf.write(f"{n:3d}  {t}\n")
        print(
            f"FLAGS: {len(FLAGS)} | unique: {len(uniq)} -> scripts/_aws_flags_report44.txt"
        )
        return 1
    if mode == "build":
        n = 0
        for f, content in results.items():
            with open(os.path.join(RU_DIR, f), "wb") as wf:
                wf.write(content.encode("utf-8"))
            n += 1
        print(f"WROTE {n} RU files. 0 flags.")
    else:
        print("DRY-OK: 0 flags, not writing (mode=%s)" % mode)
    return 0


if __name__ == "__main__":
    sys.exit(main())
