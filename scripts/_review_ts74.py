# -*- coding: utf-8 -*-
"""Critical-review blindspot scanner for the L4-IF.74 batch (things structural QA
misses): untranslated tooltips behind RU link-text (#9), EN headings (#16),
X:/—это Y (#11), quantifier+EN noun (#12), calques, stray em/en-dash."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

BASE = os.path.join(os.path.dirname(__file__), "..", "docs", "managed-ru")
TS = "ingest-from/technology-support"
CP = "ingest-from/setup-on-container-platforms"
FILES = [
    f"{TS}/application-software/go/support/go-known-limitations.md",
    f"{TS}/application-software/java/quarkus.md",
    f"{TS}/application-software/java/graalvm-native-image.md",
    f"{TS}/application-software/nginx.md",
    f"{TS}/application-software/nginx/kong-gateway.md",
    f"{TS}/known-solutions-and-workarounds.md",
    f"{CP}/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy.md",
    f"{CP}/kubernetes/legacy/deploy-oneagent-operator-openshift-legacy.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
TOOLTIP = re.compile(r'\]\([^)]*?"([^"]+)"\)')
HEAD = re.compile(r"^#{1,6}\s+(.+?)\s*$")
# kept-EN tooltips/headings that are legitimately English (UI icons, product names)
TT_OK = {"More", "Settings", "Step", "Access Tokens"}
# product/tech names allowed as all-EN headings
HEAD_OK = re.compile(
    r"^(NGINX|Kong|Quarkus|GraalVM|Go|Java|Node\.js|OpenTelemetry|Cloud-native|"
    r"Classic|OneAgent|ActiveGate|Dynatrace|Prometheus|Micrometer|FIPS|Maven|Gradle|"
    r"Spring|OpenResty|Tengine|Kubernetes|OpenShift)\b"
)


def scan(rel):
    p = os.path.join(BASE, rel)
    with open(p, encoding="utf-8") as f:
        lines = f.read().split("\n")
    hits = []
    in_fence = False
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # #9 untranslated tooltip (no Cyrillic, not whitelisted)
        for tt in TOOLTIP.findall(l):
            if not CYR.search(tt) and tt.strip() not in TT_OK and len(tt) > 3:
                hits.append((i, "TOOLTIP-EN", tt[:60]))
        # #16 EN heading
        m = HEAD.match(l)
        if m and not CYR.search(m.group(1)) and not HEAD_OK.match(m.group(1)):
            hits.append((i, "HEAD-EN", m.group(1)[:60]))
        # #11 X:это / X — это
        if re.search(r":\s+это\b", l) or "— это" in l or " – это" in l:
            hits.append((i, "X:это", s[:60]))
        # dashes that should not appear (em/en-dash)
        if "—" in l or " – " in l:
            hits.append((i, "DASH", s[:60]))
        # calque
        if re.search(r"\b[Вв]ы (можете|должны|хотите)\b", l):
            hits.append((i, "CALQUE", s[:60]))
    return hits


total = 0
for rel in FILES:
    hits = scan(rel)
    total += len(hits)
    tag = rel.split("/")[-1]
    if hits:
        print(f"\n## {tag}  ({len(hits)} hits)")
        for ln, kind, txt in hits:
            print(f"  L{ln} [{kind}] {txt}")
    else:
        print(f"\n## {tag}  — clean")
print(f"\n=== {total} blindspot hits total ===")
