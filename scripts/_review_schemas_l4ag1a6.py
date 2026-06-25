# -*- coding: utf-8 -*-
"""L4-AG.1a.6 reviewer: 37 builtin-*.md schema-table files.

Checks:
  1. Line-parity EN vs RU (EXACT)
  2. em-dash (—, U+2014) in RU file — leftover from EN OR introduced by translator
     (Lesson L4-AG.1a.5 #2: auto-review catches em-dash in *my* translations too)
  3. BOM-leftover (U+FEFF + 3-byte EF BB BF)
  4. Single-mojibake `\xc3\xa2` and triple `\xc3\xa2\xc2\x80\xc2\x99` (preserved key)
  5. ENUM marker leftover EN (`The element has these enums`)
  6. `## Authentication` leftover EN
  7. EN-leftover critical terms (whole-word) inside RU schema text:
       VMware, vCenter, ESXi, DDU, IBM, CICS, IMS, SameSite, PurePath, FQCN,
       Tolerable/Frustrating/Satisfactory etc. — kept verbatim (verify still present)
  8. Calque EN-comma `, и `, `, или ` (Lesson L4-AG.1a.5 #3)
"""

import io, os, re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

FILES = [
    "builtin-process-visibility.md",
    "builtin-span-context-propagation.md",
    "builtin-synthetic-http-advanced-execution.md",
    "builtin-rum-provider-breakdown.md",
    "builtin-process-process-monitoring.md",
    "builtin-span-attribute.md",
    "builtin-hyperscaler-authentication-connections-aws.md",
    "builtin-logmonitoring-sensitive-data-masking-settings.md",
    "builtin-cloud-kubernetes.md",
    "builtin-span-event-attribute.md",
    "builtin-rum-web-request-errors.md",
    "builtin-openpipeline-logs-pipeline-groups.md",
    "builtin-openpipeline-spans-pipeline-groups.md",
    "builtin-ibmmq-queue-managers.md",
    "builtin-synthetic-multiprotocol-performance-thresholds.md",
    "builtin-issue-tracking-integration.md",
    "builtin-openpipeline-events-pipeline-groups.md",
    "builtin-endpoint-detection-rules.md",
    "builtin-logmonitoring-log-events.md",
    "builtin-openpipeline-metrics-pipeline-groups.md",
    "builtin-logmonitoring-log-storage-settings.md",
    "builtin-logmonitoring-log-agent-feature-flags.md",
    "builtin-openpipeline-bizevents-pipeline-groups.md",
    "builtin-openpipeline-events-sdlc-pipeline-groups.md",
    "builtin-openpipeline-user-events-pipeline-groups.md",
    "builtin-openpipeline-davis-events-pipeline-groups.md",
    "builtin-openpipeline-usersessions-pipeline-groups.md",
    "builtin-openpipeline-system-events-pipeline-groups.md",
    "builtin-openpipeline-davis-problems-pipeline-groups.md",
    "builtin-openpipeline-events-security-pipeline-groups.md",
    "builtin-openpipeline-security-events-pipeline-groups.md",
    "builtin-anomaly-detection-disk-rules.md",
    "builtin-rum-ip-mappings.md",
    "builtin-service-detection-rules.md",
    "builtin-rum-web-key-performance-metric-xhr-actions.md",
    "builtin-failure-detection-environment-rules.md",
    "builtin-resource-attribute.md",
]

EM_DASH = chr(0x2014)
BOM_CHAR = chr(0xFEFF)
SINGLE_MOJI = b"\xc3\xa2"
TRIPLE_MOJI = b"\xc3\xa2\xc2\x80\xc2\x99"
DOUBLE_B_MOJI = b"\xc3\x82\xc2\xae"


def main():
    issues_total = 0
    for rel in FILES:
        en_path = os.path.join(EN, rel)
        ru_path = os.path.join(RU, rel)
        en = (
            io.open(en_path, "r", encoding="utf-8", newline="")
            .read()
            .replace("\r\n", "\n")
        )
        ru = io.open(ru_path, "r", encoding="utf-8", newline="").read()
        ru_bytes = io.open(ru_path, "rb").read()
        en_lines = en.split("\n")
        ru_lines = ru.split("\n")
        file_issues = []
        # 1. parity
        if len(en_lines) != len(ru_lines):
            file_issues.append(f"PARITY EN={len(en_lines)} RU={len(ru_lines)}")
        # 2. em-dash (translation should NOT introduce, EN-leftover already detected via diff)
        for i, line in enumerate(ru_lines, 1):
            if EM_DASH in line:
                file_issues.append(f"EM-DASH at line {i}: {line[:80]}")
        # 3. BOM
        bom_count = ru.count(BOM_CHAR)
        if bom_count:
            file_issues.append(f"BOM-leftover x{bom_count}")
        # 4. mojibake preserved (verify identical count vs EN)
        en_b = io.open(en_path, "rb").read()
        for name, key in (
            ("single-moji", SINGLE_MOJI),
            ("triple-moji", TRIPLE_MOJI),
            ("double-B-moji", DOUBLE_B_MOJI),
        ):
            en_n = en_b.count(key)
            ru_n = ru_bytes.count(key)
            if en_n != ru_n:
                file_issues.append(f"{name} count drift EN={en_n} RU={ru_n}")
        # 5. ENUM marker leftover
        if "The element has these enums" in ru:
            file_issues.append("ENUM leftover EN: 'The element has these enums'")
        # 6. `## Authentication` leftover
        if "\n## Authentication\n" in ru:
            file_issues.append("`## Authentication` leftover EN")
        # 7. EN-locks verification (terms that MUST appear in RU if they appear in EN)
        LOCKS = [
            "VMware",
            "vCenter",
            "ESXi",
            "IBM MQ",
            "CICS",
            "IMS",
            "SameSite",
            "PurePath",
            "FQCN",
            "OneAgent",
            "Tolerable",
            "Frustrating",
            "Satisfactory",
            "Apdex",
            "ActiveGate",
            "PostgreSQL",
            "OpenTelemetry",
            "Davis",
            "Settings API",
            "Kubernetes",
            "OpenShift",
            "Journald",
        ]
        for term in LOCKS:
            if term in en and term not in ru:
                file_issues.append(f"LOCK '{term}' dropped (in EN, not in RU)")
        # 8. Calque comma `, и ` / `, или `
        for needle in (", и ", ", или "):
            ix = ru.find(needle)
            if ix != -1:
                ctx_start = max(0, ix - 30)
                ctx = ru[ctx_start : ix + len(needle) + 30].replace("\n", " ")
                # Skip benign cases: ", и " inside a numbered list "; 1, и 2" — actually never benign in our prose.
                # Allow if preceded by ":" or "—" (which we banned, so safe).
                file_issues.append(f"CALQUE '{needle}' found, ctx: ...{ctx}...")
        if file_issues:
            print(f"\n=== {rel} ===")
            for s in file_issues:
                print("  -", s)
            issues_total += len(file_issues)
    print(f"\n\nTOTAL ISSUES: {issues_total}")


if __name__ == "__main__":
    main()
