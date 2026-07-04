#!/usr/bin/env python3
"""L4-IF.75: derive RU for managed-cluster/api-references/cluster-api (30 files)
from the ALREADY-SHIPPED translated twins under dynatrace-api/cluster-api.

The pending files are degraded scrapes of the same docs pages: twin has an extra
header block (# Title x2 + * Published) and links-with-tooltips where pending has
plain text. Twin RU holds line-parity with twin EN, so:

  pending EN line --norm-equal--> twin EN line --parity--> twin RU line

norm = demoji + strip markdown links to text + collapse whitespace.
Derivation per pending line:
  * fence line / inside fence -> pending EN line VERBATIM (code = own source)
  * blank -> blank
  * norm-equal aligned -> twin RU line, links kept only if URL present in the
    pending line (URL-identity against PENDING), re-indented to pending, demoji,
    em-dash auto-fix
  * else -> OVERRIDES dict (auth boilerplate: pending has plain
    "see Cluster API - Authentication." instead of the twin's link)
Frontmatter: pending's own (source/updated), title VALUE from twin RU.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "docs" / "managed"
RU = ROOT / "docs" / "managed-ru"
PEND_PREFIX = "managed-cluster/api-references/cluster-api"
TWIN_PREFIX = "dynatrace-api/cluster-api"

LINK = re.compile(r'\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
FENCE = re.compile(r"^\s*```")
MOJI = ("ï»¿", "﻿")  # 'ï»¿' and raw BOM char


def demoji(s):
    for m in MOJI:
        s = s.replace(m, "")
    return s


def strip_links(s):
    return LINK.sub(lambda m: m.group(1), s)


def norm(s):
    return re.sub(r"\s+", " ", strip_links(demoji(s))).strip()


def split_fm(t):
    t = t.replace("\r\n", "\n")
    if t.startswith("---"):
        end = t.index("\n---", 3)
        return t[: end + 4].split("\n"), t[end + 4 :].lstrip("\n")
    return [], t


# pending plain-text auth boilerplate (twin has a link instead) -> RU without link,
# wording grounded on the shipped twin RU sentence (28x corpus, comma variant, no em-dash)
OVERRIDES = {
    "To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see Cluster API - Authentication.":
        "Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.",
    "To execute this request, you need the **Cluster token management** (`ClusterTokenManagement`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see Cluster API - Authentication.":
        "Для выполнения этого запроса API-токену нужно разрешение **Cluster token management** (`ClusterTokenManagement`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.",
    "To learn how to obtain and use it, see Cluster API - Authentication.":
        "Как его получить и использовать, смотрите Cluster API - Authentication.",
}

# em-dash auto-fixes applied to derived RU lines (per CLAUDE.md §0)
EMDASH_FIX = [
    ("использовать — смотрите", "использовать, смотрите"),
    ("OK — экспорт", "OK: экспорт"),
    ("## Пример — ", "## Пример: "),
    ("*Synthetic node* — это", "*Synthetic node*, это"),
]


def derive_line(ru_line, pend_line):
    ru = demoji(ru_line)
    pend_urls = set(m.group(2) for m in LINK.finditer(pend_line))

    def repl(m):
        text, url = m.group(1), m.group(2)
        return m.group(0) if url in pend_urls else text

    ru = LINK.sub(repl, ru)
    for a, b in EMDASH_FIX:
        ru = ru.replace(a, b)
    indent = pend_line[: len(pend_line) - len(pend_line.lstrip())]
    return indent + ru.strip()


def build_one(rel):
    import difflib

    pend_p = EN / rel
    sub = str(rel).replace(PEND_PREFIX, TWIN_PREFIX)
    twin_en_p, twin_ru_p = EN / sub, RU / sub
    pfm, pbody = split_fm(pend_p.read_text(encoding="utf-8"))
    _, tbody = split_fm(twin_en_p.read_text(encoding="utf-8"))
    rfm, rbody = split_fm(twin_ru_p.read_text(encoding="utf-8"))
    pl, tl, rl = pbody.split("\n"), tbody.split("\n"), rbody.split("\n")
    assert len(tl) == len(rl), f"twin parity broken: {sub}"

    pn = [norm(x) for x in pl]
    tn = [norm(x) for x in tl]
    sm = difflib.SequenceMatcher(None, pn, tn, autojunk=False)
    amap = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                amap[i1 + k] = j1 + k

    # second chance: unmatched pending line whose norm appears in twin uniquely-derivable
    tn_index = {}
    for j, x in enumerate(tn):
        tn_index.setdefault(x, []).append(j)

    out, untranslated, emdash_left = [], [], []
    in_fence = False
    for i, line in enumerate(pl):
        if FENCE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if not line.strip():
            out.append("")
            continue
        j = amap.get(i)
        if j is None:
            cands = tn_index.get(pn[i], [])
            derived = {derive_line(rl[jj], line) for jj in cands}
            if len(derived) == 1:
                j = cands[0]
        if j is not None:
            ru = derive_line(rl[j], line)
        else:
            ov = OVERRIDES.get(norm(line))
            if ov is None:
                untranslated.append((i, line))
                out.append(line)
                continue
            indent = line[: len(line) - len(line.lstrip())]
            ru = indent + ov
        if "—" in ru:
            emdash_left.append((i, ru))
        out.append(ru)

    # frontmatter: pending's own, title VALUE from twin RU
    ru_title = next((l.split(":", 1)[1].strip() for l in rfm if l.startswith("title:")), None)
    fm = []
    for l in pfm:
        if l.startswith("title:") and ru_title is not None:
            fm.append(f'title: "{ru_title}"' if '"' in l else f"title: {ru_title}")
        else:
            fm.append(l)

    text = "\n".join(fm) + "\n\n" + "\n".join(out)
    if not text.endswith("\n"):
        text += "\n"
    dst = RU / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8", newline="\n")
    return untranslated, emdash_left


def main():
    pend = sorted(
        p.relative_to(EN) for p in (EN / PEND_PREFIX).parent.rglob("cluster-api*/**/*.md")
    )
    # rglob above misses the hub file at .../cluster-api/cluster-api-v2.md? build explicit list
    pend = sorted(
        p.relative_to(EN) for p in (EN / PEND_PREFIX).rglob("*.md")
    )
    ok = True
    for rel in pend:
        unt, emd = build_one(rel)
        status = "OK "
        if unt:
            ok = False
            status = "UNT"
        print(f"{status} {rel}")
        for i, l in unt:
            print(f"    UNTRANSLATED L{i+1}: {l[:160]!r}")
        for i, l in emd:
            print(f"    EMDASH-LEFT  L{i+1}: {l[:160]!r}")
    print("\nfiles:", len(pend))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
