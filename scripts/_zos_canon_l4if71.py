# -*- coding: utf-8 -*-
"""Shared z/OS OneAgent translation canon (L4-IF.71).

Reuses norm/read_lf from _otel_canon (durable: shared canon module crosses dirs).
Three entry points used by the per-file builders:

    from _zos_canon_l4if71 import build_one, build_messages, qa_one

* build_one(rel_dir, fname, TRANS, PASS)         -> prose files (dumb line-parity dict)
* build_messages(rel_dir, fname, PROSE, META, PASS) -> z/OS message files (bullet
      `* **Full message** - X`). Engine auto-translates the four fixed labels and
      keeps the Full message VALUE verbatim (literal system output). Subagent only
      supplies PROSE (EN value -> RU) for Explanation/System action/User response
      and META (everything else: title/#/read/intro/continuation/Related-topics).
      Message-ID headings (`## ZDC000I`) pass through EN automatically.
* qa_one(rel_dir, fname) -> structural QA (parity/URL/fence/heading/em-dash/
      mojibake/BOM/calque/leftover) with z/OS ALLOW_EN_LINE.

Deterministic engine guarantees STRUCTURE; WORD quality (term consistency,
calques, awkwardness) is caught by the manual critical review after the batch.
Grounded on shipped siblings ims-messages.md / zos-java-messages.md /
install-zremote.md.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _otel_canon import norm, read_lf  # exact reuse

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")

MSG_LABEL = {
    "Full message": "Полное сообщение",
    "Explanation": "Пояснение",
    "System action": "Действие системы",
    "User response": "Реакция пользователя",
}
_MSG_RE = re.compile(
    r"^\*\s+\*\*(Full message|Explanation|System action|User response)\*\*\s+-\s+(.*)$"
)
HEAD_RE = re.compile(r"^(#{1,6})\s")
# A message-ID heading like `## ZDC000I`, `### ZDTP001S`, `## ZDTJ12A` — caps+digits.
_MSGID_RE = re.compile(r"^#{1,6}\s+[A-Z]{2,}[A-Z0-9]*\d[A-Z0-9]*\s*$")


def _demoji(s):
    """Reverse one level of double-encoded UTF-8 mojibake (scraping artifact).

    EN sources from the scraper occasionally double-encode special chars
    (`â\\x80¦` for …, `â\\x80\\x93` for –, `â\\x80\\x9c` for “). A latin1
    round-trip fixes them. Guard on the â/Ã/Â marker so clean lines (incl.
    already-fixed … which is not latin1-encodable) pass through untouched.
    Used for BOTH matching EN keys and emitting kept-EN/Full-message lines, so
    per-file builders can write CLEAN EN keys and RU output is always clean.
    """
    if not any(c in s for c in ("â", "Ã", "Â")):
        return s
    try:
        return s.encode("latin1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s


def _write(ru_path, out, en_lines, fname):
    assert len(out) == len(en_lines), f"{fname}: parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK  {fname}: {len(out)} lines -> {ru_path}")


def build_one(rel_dir, fname, trans, passset=frozenset()):
    en_path = os.path.join(BASE, "managed", rel_dir, fname)
    ru_path = os.path.join(BASE, "managed-ru", rel_dir, fname)
    en_lines = read_lf(en_path).split("\n")
    tmap = {norm(_demoji(k)): v for k, v in trans.items()}
    pset = {norm(_demoji(k)) for k in passset}
    out, in_fence = [], False
    for ln in en_lines:
        raw = _demoji(ln.strip())
        st = norm(raw)
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence or st == "" or st == "---":
            # code/blank/--- pass through verbatim, but demoji cleans scraping
            # mojibake inside code blocks (guard => real code stays byte-identical)
            out.append(_demoji(ln))
            continue
        if raw.startswith("source:") or raw.startswith("scraped:"):
            out.append(ln)
            continue
        indent = ln[: len(ln) - len(ln.lstrip())]
        if st in tmap:
            out.append(indent + tmap[st])
            continue
        if st in pset:
            out.append(indent + raw)
            continue
        raise SystemExit(f"[{fname}] UNTRANSLATED: {ln!r}")
    _write(ru_path, out, en_lines, fname)


def build_messages(rel_dir, fname, prose, meta, passset=frozenset()):
    en_path = os.path.join(BASE, "managed", rel_dir, fname)
    ru_path = os.path.join(BASE, "managed-ru", rel_dir, fname)
    en_lines = read_lf(en_path).split("\n")
    pmap = {norm(_demoji(k)): v for k, v in prose.items()}
    mmap = {norm(_demoji(k)): v for k, v in meta.items()}
    pset = {norm(_demoji(k)) for k in passset}
    out, in_fence = [], False
    for ln in en_lines:
        raw = _demoji(ln.strip())
        st = norm(raw)
        indent = ln[: len(ln) - len(ln.lstrip())]
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence or st == "" or st == "---":
            out.append(_demoji(ln))
            continue
        if raw.startswith("source:") or raw.startswith("scraped:"):
            out.append(ln)
            continue
        # message-ID heading -> passthrough EN
        if _MSGID_RE.match(raw):
            out.append(indent + raw)
            continue
        # `* **label** - value`
        m = _MSG_RE.match(raw)
        if m:
            label, rest = m.group(1), m.group(2)
            ru_label = MSG_LABEL[label]
            if label == "Full message":
                out.append(f"{indent}* **{ru_label}** - {rest}")
                continue
            rn = norm(rest)
            if rn in pmap:
                out.append(f"{indent}* **{ru_label}** - {pmap[rn]}")
                continue
            raise SystemExit(f"[{fname}] UNTRANSLATED PROSE ({label}): {rest!r}")
        # everything else via META (title/#/read/intro/continuation/Related)
        if st in mmap:
            out.append(indent + mmap[st])
            continue
        if st in pset:
            out.append(indent + raw)
            continue
        raise SystemExit(f"[{fname}] UNTRANSLATED META: {ln!r}")
    _write(ru_path, out, en_lines, fname)


# ---------------------------------------------------------------------------
# QA
# ---------------------------------------------------------------------------
CYR = re.compile(r"[А-Яа-яЁё]")
EMDASH = "—"
BOM = "﻿"
# Bare â/Ã/Â/BOM-mojibake: none occur in legitimate EN/RU/command text in this
# corpus, so they reliably flag scraping mojibake. NB: « » … smart-quotes are
# legitimate (Russian guillemets / kept-EN literals) and are NOT mojibake.
MOJI = ["â", "Ã", "Â", "ï»¿"]
URL_RE = re.compile(r"\]\(([^)\s]+)")
FENCE_RE = re.compile(r"^\s*```")
CAP_PHRASE = re.compile(r"[A-Z][a-z]+(\s+[a-z]+){2,}")
EN_LOWER_RUN = re.compile(r"\b[a-z]+(\s+[a-z]+){3,}\b")

# z/OS lines that are legitimately all-EN (message IDs handled separately).
ALLOW_EN_LINE = set()


def _read(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def _urls(t):
    return sorted(URL_RE.findall(t))


def _fences(ls):
    return [i for i, l in enumerate(ls) if FENCE_RE.match(l)]


def _code_blocks(ls):
    blocks, inb, cur = [], False, []
    for l in ls:
        if FENCE_RE.match(l):
            if inb:
                blocks.append(cur)
                cur = []
            inb = not inb
            continue
        if inb:
            cur.append(l)
    return blocks


def _headings(ls):
    return [l for l in ls if HEAD_RE.match(l)]


def qa_one(rel_dir, fname, verbose=True):
    en = _read(os.path.join(BASE, "managed", rel_dir, fname))
    ru = _read(os.path.join(BASE, "managed-ru", rel_dir, fname))
    el, rl = en.split("\n"), ru.split("\n")
    msgs = []

    if len(el) != len(rl):
        msgs.append(("FAIL", f"line-parity EN={len(el)} RU={len(rl)}"))

    for key in ("source:", "scraped:"):
        ev = [l for l in el if l.startswith(key)]
        rv = [l for l in rl if l.startswith(key)]
        if ev != rv:
            msgs.append(("FAIL", f"frontmatter {key} mismatch"))

    n = ru.count(EMDASH)
    if n:
        ln = [i + 1 for i, l in enumerate(rl) if EMDASH in l]
        msgs.append(("FAIL", f"em-dash x{n} at {ln[:8]}"))

    for m in MOJI:
        if m in ru:
            ln = [i + 1 for i, l in enumerate(rl) if m in l]
            msgs.append(("FAIL", f"mojibake {m!r} at {ln[:8]}"))
    if ru.startswith(BOM):
        msgs.append(("FAIL", "BOM present"))
    # U+FEFF mid-content: scraping artifact from EN `ï»¿` that the demoji guard
    # skips (no â/Ã/Â) and the 3-char MOJI pattern misses once decoded to the
    # single char U+FEFF. Canon L4-IF.66 #3 = strip in RU. (L4-IF.74 blindspot.)
    nfeff = ru.count("﻿")
    if nfeff:
        lnf = [i + 1 for i, l in enumerate(rl) if "﻿" in l]
        msgs.append(("FAIL", f"U+FEFF BOM mid-content x{nfeff} at {lnf[:8]}"))

    if _urls(en) != _urls(ru):
        only_en = sorted(set(_urls(en)) - set(_urls(ru)))
        only_ru = sorted(set(_urls(ru)) - set(_urls(en)))
        msgs.append(
            ("FAIL", f"URL mismatch EN-only={only_en[:3]} RU-only={only_ru[:3]}")
        )

    if _fences(el) != _fences(rl):
        msgs.append(("FAIL", f"fence positions differ"))
    # demoji both sides: EN code blocks may carry scraping mojibake that RU
    # legitimately cleans (L4-IF.63 canon); compare on the cleaned form.
    en_cb = [[_demoji(l) for l in b] for b in _code_blocks(el)]
    ru_cb = [[_demoji(l) for l in b] for b in _code_blocks(rl)]
    if en_cb != ru_cb:
        msgs.append(("FAIL", "code-block content differs from EN"))

    eh = [HEAD_RE.match(l).group(1) for l in _headings(el)]
    rh = [HEAD_RE.match(l).group(1) for l in _headings(rl)]
    if eh != rh:
        msgs.append(("FAIL", f"heading levels differ EN={len(eh)} RU={len(rh)}"))

    for pat in (
        r"\bвы можете\b",
        r"\bвы должны\b",
        r"\bВы можете\b",
        r"\bВы должны\b",
        r"\bвы хотите\b",
        r"\bВы хотите\b",
    ):
        for i, l in enumerate(rl):
            if re.search(pat, l):
                msgs.append(("WARN", f"calque '{pat}' L{i + 1}: {l.strip()[:70]}"))

    inb = False
    for i, l in enumerate(rl):
        if FENCE_RE.match(l):
            inb = not inb
            continue
        if inb:
            continue
        s = l.strip()
        if not s or s in ALLOW_EN_LINE or _MSGID_RE.match(s):
            continue
        if CYR.search(l):
            continue
        bare = re.sub(r"\[[^\]]*\]\([^)]*\)", "", l)
        bare = re.sub(r"`[^`]*`", "", bare)
        bare = re.sub(r"https?://\S+", "", bare)
        bare = re.sub(r"[*#>\-+|]", " ", bare).strip()
        if CAP_PHRASE.search(bare) or EN_LOWER_RUN.search(bare):
            msgs.append(("WARN", f"EN-leftover suspect L{i + 1}: {s[:70]}"))

    fails = [m for t, m in msgs if t == "FAIL"]
    warns = [m for t, m in msgs if t == "WARN"]
    status = "PASS" if not fails else "FAIL"
    if verbose:
        print(f"[{status}] {fname}  (lines {len(rl)}, warns {len(warns)})")
        for t, m in msgs:
            print(f"    [{t}] {m}")
    return len(fails), len(warns), msgs


if __name__ == "__main__":
    # Self-test: QA a shipped sibling message file (must be PASS).
    qa_one(
        "ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages",
        "zos-java-messages.md",
    )
