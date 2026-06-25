# -*- coding: utf-8 -*-
"""Final critical review for all 7 L4-AG.1a.15 files."""

import re, io, os

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"
FILES = [
    "builtin-infrastructure-disk-edge-anomaly-detectors.md",
    "builtin-management-zones.md",
    "builtin-os-services-monitoring.md",
    "builtin-tags-auto-tagging.md",
    "builtin-anomaly-detection-infrastructure-hosts.md",
    "builtin-appsec-notification-integration.md",
    "builtin-problem-notifications.md",
]

EN_LIKELY_LEFTOVER = [
    " has to match a required format",
    " Matches string with wildcards",
    " Matches if ",
    " Matches services ",
    "Available logic operations",
    "Use one of the following values",
    "must be escaped with a tilde",
    "Toggle the switch",
    "By default, Dynatrace",
    "The element has these enums",
    "Type 'dt.' for key hints",
    "Type '{' for placeholder hints",
    "Type '{' for placeholder suggestions",
    "Available placeholders:",
    "Detect ",
    "Detection mode for",
    "Alert if ",
    "Receive/transmit ",
    "Note that policies",
    "In order to set up",
    "Please provide feedback",
    "Set up alerts for",
    "Dynatrace automatically detects",
    "For each Management",
    "Management zones enable",
    "Management zone rules are",
    "Tags simplify",
    "Rule-based tags behave",
    "Tagging rules are",
    "Set of additional key-value",
    "Set of rules to scope",
    "Specify disk total space",
    "Host resource attributes are dimensions",
    "Starting from agent ",
    "When enabled,",
    "If this field is empty then",
    "Integrate security notifications",
    "Integrate Dynatrace problem notifications",
    "This is the content your notification",
    "In case a value of a security",
    "In case a value of an attack",
    "Security notifications contain sensitive",
    "The subject of the email",
    "The template of the email",
    "Set up an incoming WebHook",
    "Send email if problem",
    "The channel (for example",
    "The summary of the Jira",
    "The description of the Jira",
    "The URL of the Jira",
    "The username of the Jira",
    "The API token for the Jira",
    "The project key of the Jira",
    "The type of the Jira",
    "The content of the message.",
    "The content of the notification",
    "The API key to access OpsGenie",
    "The region domain of the OpsGenie",
    "The name of the PagerDuty",
    "The Events API key to access",
    "The API key for the target Splunk",
    "The routing key, defining",
    "The application key for the Trello",
    "The authorization token for",
    "The card text and problem placeholders",
    "The description of the Trello",
    "The ServiceNow instance identifier",
    "The URL of the on-premise ServiceNow",
    "The username of the ServiceNow",
    "The password to the ServiceNow",
    "Account username",
    "Account password",
    "The URL of the target job template",
    "The scope of access you are",
    "If false, the client credentials",
    "To authenticate your integration",
    "A list of the additional HTTP",
    "The name of the HTTP header",
    "Use additional HTTP headers",
    "Select an alerting profile",
]

lines = []
total_em = 0
total_bomj = 0
total_enum = 0
total_auth = 0
total_param = 0
total_single = 0
total_calque = 0
total_real_sig = 0
for f in FILES:
    b = io.open(f"{RU}/{f}", "rb").read()
    t = b.decode("utf-8")
    em = t.count(chr(0x2014))
    bomj = b.count(b"\xc3\xaf\xc2\xbb\xc2\xbf") + b.count(b"\xef\xbb\xbf")
    enum_left = t.count("The element has these enums")
    auth_left = t.count("## Authentication")
    param_left = t.count("## Parameters")
    single_a = (
        b.count(b"\xc3\xa2")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x93")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x99")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x94")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x91")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x9c")
        - b.count(b"\xc3\xa2\xc2\x80\xc2\x9d")
    )
    calque_n = len(re.findall(r"(, и \w+|, или \w+)", t))
    sig_hits = []
    for w in EN_LIKELY_LEFTOVER:
        n = t.count(w)
        if n:
            sig_hits.append(f"{w}({n})")
    total_em += em
    total_bomj += bomj
    total_enum += enum_left
    total_auth += auth_left
    total_param += param_left
    total_single += single_a
    total_calque += calque_n
    total_real_sig += len(sig_hits)
    status = (
        "OK"
        if (
            em == 0
            and bomj == 0
            and enum_left == 0
            and auth_left == 0
            and param_left == 0
            and single_a == 0
            and not sig_hits
        )
        else "ATTN"
    )
    lines.append(f"--- {f} ---")
    lines.append(
        f"em={em} BOMJ={bomj} ENUM={enum_left} Auth={auth_left} Param={param_left} "
        f"single_a={single_a} calque={calque_n} sigs={len(sig_hits)} [{status}]"
    )
    if sig_hits:
        for s in sig_hits:
            lines.append(f"  SIG: {s}")
            # show first context
            base = s.split("(")[0]
            idx = t.find(base)
            if idx >= 0:
                lines.append("    ctx: " + t[max(0, idx - 30) : min(len(t), idx + 120)])
    lines.append("")

lines.append(
    f"TOTAL: em={total_em} BOMJ={total_bomj} ENUM={total_enum} Auth={total_auth} "
    f"Param={total_param} single_a={total_single} calque={total_calque} sigs={total_real_sig}"
)

io.open("scripts/_review_l4ag1a15_final_report.txt", "w", encoding="utf-8").write(
    "\n".join(lines)
)
print("Final report written.")
