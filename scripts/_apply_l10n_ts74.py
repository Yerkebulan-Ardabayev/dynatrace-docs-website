# -*- coding: utf-8 -*-
"""Post-pass localization for L4-IF.74 batch: translate EN link-tooltips left
behind RU link-text (blindspot #9). Builds a URL -> canonical-RU-tooltip map from
the shipped managed-ru corpus (most frequent Cyrillic tooltip per URL) and
rewrites `](url "EN tooltip")` -> `](url "RU tooltip")` in the batch .md files.
Idempotent. Same accepted pattern as _apply_l10n_azure.py (L4-IF.73)."""
import os
import re
import sys
from collections import Counter

BASE = os.path.join(os.path.dirname(__file__), "..", "docs", "managed-ru")
CYR = re.compile(r"[А-Яа-яЁё]")
# capture (url, tooltip) from `](url "tooltip")`
LINK = re.compile(r'\]\((/[^)\s]+|https?://[^)\s]+)\s+"([^"]+)"\)')

TS = "ingest-from/technology-support"
CP = "ingest-from/setup-on-container-platforms"
TARGETS = [
    f"{CP}/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy.md",
    f"{CP}/kubernetes/legacy/deploy-oneagent-operator-openshift-legacy.md",
    f"{TS}/application-software/go/support/go-known-limitations.md",
    f"{TS}/application-software/java/quarkus.md",
    f"{TS}/application-software/java/graalvm-native-image.md",
    f"{TS}/application-software/nginx.md",
    f"{TS}/application-software/nginx/kong-gateway.md",
    f"{TS}/known-solutions-and-workarounds.md",
]

# Manual fallback for URLs whose canonical RU tooltip isn't in the corpus.
MANUAL = {
    "Deploy Dynatrace Operator on Kubernetes": "Развёртывание Dynatrace Operator в Kubernetes",
    "Monitor Kubernetes/OpenShift with Dynatrace.": "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.",
    "Store Dynatrace images in private registries": "Хранение образов Dynatrace в приватных реестрах",
    "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components.": "Эта страница поможет вам справиться с трудностями, которые могут возникнуть при работе с Dynatrace Operator и его компонентами.",
}

# UI-icon tooltips kept EN by design (not defects) — don't report as unresolved.
SKIP = {"More", "Settings", "Step", "Access Tokens"}


def build_url_map():
    """url -> most common Cyrillic tooltip across the whole managed-ru corpus."""
    per_url = {}
    for root, _, files in os.walk(BASE):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            with open(os.path.join(root, fn), encoding="utf-8") as f:
                txt = f.read()
            for url, tt in LINK.findall(txt):
                if CYR.search(tt):
                    per_url.setdefault(url, Counter())[tt] += 1
    return {u: c.most_common(1)[0][0] for u, c in per_url.items()}


def main():
    umap = build_url_map()
    total = 0
    unresolved = Counter()
    for rel in TARGETS:
        p = os.path.join(BASE, rel)
        with open(p, encoding="utf-8") as f:
            text = f.read()

        def repl(m):
            nonlocal total
            url, tt = m.group(1), m.group(2)
            if CYR.search(tt) or tt.strip() in SKIP:
                return m.group(0)  # already RU, or kept-EN UI icon
            ru = umap.get(url) or MANUAL.get(tt)
            if not ru:
                unresolved[tt] += 1
                return m.group(0)
            total += 1
            return f']({url} "{ru}")'

        new = LINK.sub(repl, text)
        if new != text:
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(new)
            print(f"  patched {rel.split('/')[-1]}")
    print(f"\n=== {total} tooltips localized ===")
    if unresolved:
        print("UNRESOLVED (need manual map):")
        for tt, n in unresolved.most_common():
            print(f"  x{n}  {tt}")


if __name__ == "__main__":
    main()
