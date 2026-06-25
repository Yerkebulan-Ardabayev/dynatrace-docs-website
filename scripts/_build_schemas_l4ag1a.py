# -*- coding: utf-8 -*-
"""L4-AG.1a pilot builder: 15 smallest builtin-*.md schema-table files in
docs/managed/dynatrace-api/environment-api/settings/schemas/.

Same schema-table CLASS as shipped L4-AF app-dynatrace-*.md (## Authentication
+ ## Parameters + Schema-ID/Scope row + GET endpoints) but with `builtin:`
prefix instead of `app:` in the `### <Name> (`builtin:...`)` heading.

EN-verbatim: frontmatter title/source/scraped, BOTH `# Settings API - X schema
table` H1 lines, `* Published <date>`, Schema-meta row (Schema ID/groups/Scope
EN-locked), endpoint GET rows, full URLs, `\\`code\\`` parameter identifiers,
type column, Required/Optional column.

Translated: schema heading display-name, schema description paragraphs,
Authentication + Parameters section heads, auth paragraph, Property/Description
column headers, parameter label cells, parameter description cells.

Anchor canon: L4-AF _build_schemas_l4af.py (auth absatz, `Возможные значения:`,
`## Аутентификация`/`## Параметры`/Property→Свойство headers).

Line-parity EXACT (EN==RU `\\n` count). No fenced code blocks. No em-dash
introduced. Literal U+EFBBBF BOM sequence INSIDE link text in 2 files
(rum-mobile-privacy + deployment-activegate-updates) is stripped (L4-AF L4M).
"""

import os, io

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-metric-query.md",
    "builtin-geo-settings.md",
    "builtin-synthetic-http-name.md",
    "builtin-rum-web-name.md",
    "builtin-rum-mobile-name.md",
    "builtin-synthetic-browser-name.md",
    "builtin-synthetic-multiprotocol-name.md",
    "builtin-alerting-connectivity-alerts.md",
    "builtin-eula-settings.md",
    "builtin-host-monitoring.md",
    "builtin-rum-mobile-privacy.md",
    "builtin-process-group-monitoring-state.md",
    "builtin-audit-log.md",
    "builtin-monitored-technologies-iis.md",
    "builtin-deployment-activegate-updates.md",
]

# Schema heading display-name (`### <Name> (`builtin:...`)`).
DISPLAY_NAME = {
    "Metric query": "Метрический запрос",
    "Geolocation settings": "Настройки геолокации",
    "Monitor name": "Имя монитора",
    "Application name": "Имя приложения",
    "Connectivity alerts": "Оповещения о связности",
    "Terms of use": "Условия использования",
    "Monitoring": "Мониторинг",
    "Privacy settings": "Настройки приватности",
    "Process group monitoring": "Мониторинг групп процессов",
    "Log audit events": "События аудита логов",
    "IIS": "IIS",
    "ActiveGate updates": "Обновления ActiveGate",
}

# Schema description lines (between heading and Schema-ID table). Whole-line
# match (`\n` + EN + `\n` -> `\n` + RU + `\n`).
SCHEMA_DESC = {
    "A stored metric query allows you to calculate the metrics' values through a metric expression.": "Сохранённый метрический запрос позволяет вычислять значения метрик через метрическое выражение.",
    "Settings related to geolocations": "Настройки, относящиеся к геолокациям",
    "Define the display name of your http monitor": "Задайте отображаемое имя HTTP-монитора",
    "Define the display name of your browser monitor": "Задайте отображаемое имя браузерного монитора",
    "Define the display name of your network availability monitor": "Задайте отображаемое имя монитора доступности сети",
    "This name is used to refer to your application throughout this Dynatrace environment. Be sure that your application has a meaningful name.": "Это имя используется для обозначения вашего приложения во всём этом окружении Dynatrace. Убедитесь, что у приложения осмысленное имя.",
    "This name is used to refer to your mobile app throughout this Dynatrace environment. Be sure that your app has a meaningful name.": "Это имя используется для обозначения вашего мобильного приложения во всём этом окружении Dynatrace. Убедитесь, что у приложения осмысленное имя.",
    "Enable or disable TCP connectivity problems for processes of this process group.": "Включите или отключите проблемы TCP-связности для процессов этой группы процессов.",
    "Display end user terms (recommended for customers that purchased via a reseller).": "Показывать условия для конечных пользователей (рекомендуется для клиентов, купивших через реселлера).",
    "See our Third party licenses (`<your-dynatrace-url>//ui/third-party-licenses`).": "См. наши сторонние лицензии (`<your-dynatrace-url>//ui/third-party-licenses`).",
    "OneAgent automatically monitors host, its processes, services and applications but you can switch off monitoring or disable auto-injection.": "OneAgent автоматически мониторит хост, его процессы, сервисы и приложения, но вы можете отключить мониторинг или auto-injection.",
    # BOM stripped by _normalize; link text becomes just `Opt-in mode`.
    "Enable user opt-in mode to allow your users to decide what types of data they are willing to share. For details, see [Opt-in mode](https://dt-url.net/9602z8z)": "Включите режим opt-in, чтобы ваши пользователи могли решать, какие типы данных они готовы предоставить. Подробнее см. [Opt-in mode](https://dt-url.net/9602z8z)",
    "Enable or disable monitoring for certain process groups": "Включите или отключите мониторинг для определённых групп процессов",
    "If enabled, Dynatrace logs all audit-related events, including logins/logouts, configuration changes, and API token changes. Please note that audit logs include personal identifiable information (PII) such as email addresses and IP addresses of Dynatrace users. Audit events can be accessed via the Dynatrace REST API.": "Если включено, Dynatrace логирует все события, связанные с аудитом, включая входы/выходы, изменения конфигурации и изменения API-токенов. Обратите внимание, что аудит-логи содержат персонально идентифицируемую информацию (PII), такую как email-адреса и IP-адреса пользователей Dynatrace. К событиям аудита можно обращаться через Dynatrace REST API.",
    "By default, IIS monitoring is enabled on all hosts. If you want to disable IIS monitoring on selected hosts, disable it on these hosts via their settings.": "По умолчанию мониторинг IIS включён на всех хостах. Если вы хотите отключить мониторинг IIS на отдельных хостах, отключите его на этих хостах через их настройки.",
    "If you want to enable IIS monitoring only on selected hosts, disable global IIS monitoring and enable it on these hosts via their settings.": "Если вы хотите включить мониторинг IIS только на отдельных хостах, отключите глобальный мониторинг IIS и включите его на этих хостах через их настройки.",
    "Configure ActiveGate update behavior. To learn more about the latest updates, visit [ActiveGate release notes](https://dt-url.net/release-notes-activegate).": "Настройте поведение обновления ActiveGate. Подробнее о последних обновлениях см. [ActiveGate release notes](https://dt-url.net/release-notes-activegate).",
}

# Parameter table col-1 label (before `\`code\``).
PARAM_LABEL = {
    "Automatic updates at earliest convenience": "Автоматические обновления при первой возможности",
    "Display end user terms to new users logging in to the environment": "Показывать условия для конечных пользователей новым пользователям, входящим в окружение",
    "Display the world map": "Отображать карту мира",
    "Enable user opt-in mode": "Включить режим opt-in пользователя",
    "Log all audit-related system events": "Логировать все системные события, связанные с аудитом",
    "Monitor IIS": "Мониторить IIS",
    "Monitor description": "Описание монитора",
    "Monitor name": "Имя монитора",
    "Monitor this host": "Мониторить этот хост",
    "Monitoring state": "Состояние мониторинга",
    "Query": "Запрос",
    "TCP connectivity problems": "Проблемы TCP-связности",
    "Update app name": "Обновить имя приложения",
    "Update application name": "Обновить имя приложения",
}

# Parameter table col-3 description (when not just `-` and not enum-tail).
PARAM_DESC = {
    "Turn on monitoring to gain visibility into this host, its processes, services, and applications.": "Включите мониторинг, чтобы получить видимость этого хоста, его процессов, сервисов и приложений.",
}

# Structural canon (shared with L4-AF).
STRUCT = [
    ("Retrieve schema via Settings API", "Получить schema через Settings API"),
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    (
        "To execute this request, you need an access token with **Read settings** "
        "(`settings.read`) scope. To learn how to obtain and use it, see "
        "[Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "Для выполнения запроса необходим access token со scope **Read settings** "
        "(`settings.read`). О том, как получить и использовать токен, см. "
        "[Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    (
        "| Property | Type | Description | Required |",
        "| Свойство | Тип | Описание | Обязательный |",
    ),
]

ENUM_PHRASE = ("The element has these enums", "Возможные значения:")


def _normalize(t):
    t = t.replace("\r\n", "\n")
    t = t.replace(chr(0xFEFF), "")
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")
    return t


def _heading(line):
    """`### <Name> (`builtin:...`)` -> `### <RU name> (`builtin:...`)`."""
    marker = " (`builtin:"
    i = line.find(marker)
    if not line.startswith("### ") or i == -1:
        return None
    name = line[4:i]
    tail = line[i:]
    ru = DISPLAY_NAME.get(name)
    if ru is None:
        return None
    return "### " + ru + tail


def _param_row(line):
    """`| <Label> \`code\` | <type> | <Desc> | <Req> |`."""
    if not line.startswith("| ") or not line.endswith(" |"):
        return None
    cells = line[2:-2].split(" | ")
    if len(cells) != 4:
        return None
    c0, ctype, cdesc, creq = cells
    if "`" not in c0:
        return None
    bt = c0.find("`")
    label = c0[:bt].rstrip()
    code = c0[bt:]
    sep = c0[len(label) : bt]
    if label not in PARAM_LABEL:
        return None
    new_label = PARAM_LABEL[label]
    d = cdesc
    ei = d.find(ENUM_PHRASE[0])
    if ei != -1:
        head = d[:ei].rstrip()
        enum_tail = d[ei + len(ENUM_PHRASE[0]) :]
        if head == "" or head == "-":
            new_desc = ENUM_PHRASE[1] + enum_tail
        else:
            head_ru = PARAM_DESC.get(head, head)
            new_desc = head_ru + " " + ENUM_PHRASE[1] + enum_tail
    else:
        new_desc = "-" if d == "-" else PARAM_DESC.get(d, d)
    return (
        "| "
        + new_label
        + sep
        + code
        + " | "
        + ctype
        + " | "
        + new_desc
        + " | "
        + creq
        + " |"
    )


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    t = io.open(src, "r", encoding="utf-8", newline="").read()
    t = _normalize(t)
    for en, ru in SCHEMA_DESC.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    for en, ru in STRUCT:
        t = t.replace(en, ru)
    out = []
    for line in t.split("\n"):
        nl = _heading(line) or _param_row(line)
        out.append(nl if nl is not None else line)
    t = "\n".join(out)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return src, dst


if __name__ == "__main__":
    bad = 0
    for rel in PILOT:
        src, dst = build(rel)
        en_n = (
            io.open(src, "r", encoding="utf-8", newline="")
            .read()
            .replace("\r\n", "\n")
            .count("\n")
        )
        ru_n = io.open(dst, "r", encoding="utf-8", newline="").read().count("\n")
        flag = "" if en_n == ru_n else "  <<< PARITY MISMATCH"
        if flag:
            bad += 1
        print("%-60s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY:", "OK" if bad == 0 else f"BAD ({bad})")
