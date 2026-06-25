# -*- coding: utf-8 -*-
"""Orchestrator independent generic LATIN-RUN net for L4-AB (L4Y#3:
generic stripped-Latin-run > curated SUSPECT). Strips code fences, inline
code, **bold**, link URLs, EN-invariant lines (title/#/* Reference/
* Published/source/scraped), ALLOWED_EN headings, L3G type-headings &
tab-labels, then flags any line with a run of >=5 consecutive Latin words
(English prose that escaped translation). Prints file:line + the run for
manual adjudication (some are legit EN-lock link-text / object enum prose)."""

import re, glob, os

RU = "docs/managed-ru/dynatrace-api/configuration-api"
SA = f"{RU}/service-api"
files = (
    [
        f"{RU}/service-api.md",
        f"{SA}/detection-rules.md",
        f"{SA}/failure-detection.md",
        f"{SA}/custom-services-api.md",
    ]
    + sorted(glob.glob(f"{SA}/detection-rules/**/*.md", recursive=True))
    + sorted(glob.glob(f"{SA}/failure-detection/**/*.md", recursive=True))
    + sorted(glob.glob(f"{SA}/custom-services-api/**/*.md", recursive=True))
)
files = [f for f in dict.fromkeys(files) if os.path.isfile(f)]

ALLOWED_EN_LINE = re.compile(
    r"^\s*(title:|source:|scraped:|# |#### Curl|## Validate payload|"
    r"\* Reference|\* Published|### [A-Z_]+$|#### [A-Z_]+$|"
    r"\| Parameters \||\| JSON model \||Parameters$|JSON model$)"
)
CYR = re.compile(r"[А-Яа-яЁё]")
# >=5 consecutive ascii-letter words (allows ', -, /) = suspicious EN prose
RUN = re.compile(r"(?:\b[A-Za-z][A-Za-z'\-/]*\b(?:\s+|$)){5,}")

flags = 0
for fp in files:
    with open(fp, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    infence = False
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if s == "```":
            infence = not infence
            continue
        if infence or not s:
            continue
        if ALLOWED_EN_LINE.match(s):
            continue
        # strip inline code, bold, link URLs (keep link text), images alt kept
        t = re.sub(r"`[^`]*`", " ", ln)
        t = re.sub(r"\*\*[^*]*\*\*", " ", t)
        t = re.sub(r"\]\([^)]*\)", "] ", t)  # drop (url "title") keep text
        t = re.sub(r"https?://\S+", " ", t)
        t = re.sub(r"[#>|*\-\[\]!]", " ", t)
        for m in RUN.finditer(t):
            run = m.group(0).strip()
            # ignore if the run is mostly a single CamelCase/UPPER token group
            words = run.split()
            if len(words) < 5:
                continue
            flags += 1
            print(f"{fp}:{i}: {run[:160]}")
print(f"\n=== {flags} Latin-run flags across {len(files)} files ===")
