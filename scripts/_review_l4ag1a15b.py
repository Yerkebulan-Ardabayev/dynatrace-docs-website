# -*- coding: utf-8 -*-
"""L4-AG.1a.15b review script — output to file."""

import re, io

RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"
FILES = [
    "builtin-appsec-notification-integration.md",
    "builtin-problem-notifications.md",
]
SIG_WORDS = [
    "Alert if",
    "Choose whether",
    "Note that",
    "Available placeholders",  # raw EN form
    "Type '{' for placeholder",  # raw EN form
    "**Note:** Security notifications",  # raw EN form
    "In case a value of",  # raw EN form
    "The subject of the email",
    "The template of the email",
    "The content of the message",
    "The content of the notification",
    "The summary of the Jira",
    "The description of the Jira",
    "The URL of the Jira",
    "The username of the Jira",
    "Set up an incoming WebHook",
    "Send email if problem",
    "The channel (for example",
    "**{SecurityProblemId}**: The unique",
    "**{Title}**: A short summary",
    "**{Description}**: A more detailed",
    "**{CvssScore}**: CVSS score",
    "**{DavisSecurityScore}**: [Davis",
    "**{Severity}**: The security",
    "**{SecurityProblemUrl}**: URL",
    "**{AffectedEntities}**: Details",
    "**{ManagementZones}**: Comma-separated",
    "**{Tags}**: Comma-separated",
    "**{Tags}**: Comma separated",
    "**{Exposed}**: Describes",
    "**{DataAssetsReachable}**: Describes",
    "**{ExploitAvailable}**: Describes",
    "**{AttackDisplayId}**: The unique",
    "**{Title}**: Location of",
    "**{Type}**: The type of attack",
    "**{AttackUrl}**: URL of",
    "**{ProcessGroupId}**: Details",
    "**{EntryPoint}**: The entry",
    "**{Status}**: The status",
    "**{Timestamp}**: When the attack",
    "**{VulnerabilityName}**: Name",
    "**{ImpactedEntities}**: Details",
    "**{ImpactedEntity}**: A short",
    "**{ImpactedEntityNames}**: The entity",
    "**{NamesOfImpactedEntities}**: The names",
    "**{PID}**: Unique system",
    "**{ProblemDetailsHTML}**: All",
    "**{ProblemDetailsJSONv2}**: Problem",
    "**{ProblemDetailsJSON}**: Problem",
    "**{ProblemDetailsMarkdown}**: All",
    "**{ProblemDetailsText}**: All",
    "**{ProblemID}**: Display",
    "**{ProblemImpact}**: Impact",
    "**{ProblemSeverity}**: Severity",
    "**{ProblemTitle}**: Short",
    "**{ProblemURL}**: URL of",
    "**{State}**: Problem state",
]

report = []
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
    calque_contexts = []
    for m in re.finditer(r"(, и \w+|, или \w+)", t):
        s, e = m.span()
        calque_contexts.append(t[max(0, s - 60) : min(len(t), e + 60)])
    sig_hits = []
    for w in SIG_WORDS:
        n = t.count(w)
        if n:
            sig_hits.append(f"{w}({n})")
    report.append(
        f"--- {f} ---\n"
        f"em-dash={em}, mojibake-BOM={bomj}, ENUM-left={enum_left}, "
        f"Auth-left={auth_left}, Param-left={param_left}, single_a={single_a}\n"
        f"calque hits ({len(calque_contexts)}):\n"
        + "\n".join("  " + c for c in calque_contexts)
        + ("\n" if calque_contexts else "")
        + f"signal-words hits:\n  "
        + "\n  ".join(sig_hits)
        + "\n"
    )

io.open("scripts/_review_l4ag1a15b_report.txt", "w", encoding="utf-8").write(
    "\n".join(report)
)
print("Report written.")
