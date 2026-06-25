#!/usr/bin/env python3
"""Make each RU file's trailing-newline state match its EN source (line-parity).

claude -p's Write tends to add one trailing newline the EN source lacks, which
shows up as a +1 line-parity diff. This post-pass aligns the final-newline byte
to the EN source. Pure trailing-newline normalization, no content change.
"""

from pathlib import Path

EN = Path("docs/managed")
RU = Path("docs/managed-ru")

fixed = 0
for ru in RU.rglob("*.md"):
    rel = ru.relative_to(RU)
    en = EN / rel
    if not en.exists():
        continue
    rub = ru.read_bytes()
    en_has_nl = EN.joinpath(rel).read_bytes().endswith(b"\n")
    # also normalize Windows CRLF -> LF (claude -p sometimes writes CRLF)
    new = rub.replace(b"\r\n", b"\n").rstrip(b"\r\n") + (b"\n" if en_has_nl else b"")
    if new != rub:
        ru.write_bytes(new)
        fixed += 1

print(f"normalized trailing newline: {fixed} files")
