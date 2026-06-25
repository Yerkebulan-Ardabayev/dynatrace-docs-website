# -*- coding: utf-8 -*-
"""
L4-IF.34 build script: GCP supported-service-metrics-new/ (35 files).

Repetitive template (100% byte-uniform boilerplate across all files, verified):
  frontmatter / H1 x2 / tag-line / intro / Prerequisites / Add services /
  View metrics / Metric table (4-col) / Related topics.

Per-file variation only in: title, read-time, published date, metric-table
service name, and the data rows. Everything else is exact-match boilerplate.

Canon (verified against the 2170-file managed-ru corpus):
  - Table policy mirrors Azure cloud-metrics precedent: HEADER translated
    (Имя / Единица измерения), but "Name" column VALUES kept EN (findability +
    product-UI display names), "Unit" column VALUES translated. Identifier
    columns (Feature set, GCP metric identifier) kept EN.
  - source:/scraped: byte-identical. URLs byte-identical. LF, no BOM.
  - em-dash = 0 (§0).
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN_DIR = os.path.join(
    ROOT,
    "docs",
    "managed",
    "ingest-from",
    "google-cloud-platform",
    "gcp-integrations",
    "gcp-supported-service-metrics-new",
)
RU_DIR = os.path.join(
    ROOT,
    "docs",
    "managed-ru",
    "ingest-from",
    "google-cloud-platform",
    "gcp-integrations",
    "gcp-supported-service-metrics-new",
)

# ---- exact-match boilerplate lines (EN -> RU) -------------------------------
EXACT = {
    "## Prerequisites": "## Предварительные условия",
    "## Add services and feature sets Optional": "## Добавление сервисов и наборов функций Необязательно",
    "## View metrics": "## Просмотр метрик",
    "## Metric table": "## Таблица метрик",
    "## Related topics": "## Связанные темы",
    "Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.": "Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.",
    '[Set up integration](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")': '[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")',
    'After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").': 'После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").',
    "For a list of feature sets available for this service, see [Metric table](#table).": "Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).",
    'After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.': 'После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.',
    '* [Google Cloud integrations](/managed/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")': '* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")',
    "* How-to guide": "* Практическое руководство",
}

# table header (two casing variants -> one RU header)
HEADER = {
    "| Feature set | Name | Unit | GCP metric identifier |": "| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |",
    "| Feature Set | Name | Unit | GCP metric identifier |": "| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |",
}

# Unit column VALUES (translated; Count/Byte/MilliSecond/Percent confirmed in
# Azure corpus, others are the consistent extensions).
UNIT = {
    "Count": "Количество",
    "Byte": "Байт",
    "MilliSecond": "Миллисекунда",
    "MicroSecond": "Микросекунда",
    "Second": "Секунда",
    "Percent": "Процент",
    "Unspecified": "Не указано",
    "GibiByte": "Гибибайт",
    "GigaByte": "Гигабайт",
    "BytePerSecond": "Байт/с",
    "PerSecond": "1/с",
    "Day": "День",
    "": "",
}

MONTHS = {
    "Jan": "января",
    "Feb": "февраля",
    "Mar": "марта",
    "Apr": "апреля",
    "May": "мая",
    "Jun": "июня",
    "Jul": "июля",
    "Aug": "августа",
    "Sep": "сентября",
    "Oct": "октября",
    "Nov": "ноября",
    "Dec": "декабря",
}

RE_READ = re.compile(r"^\* (\d+)-min read$")
RE_PUB = re.compile(r"^\* Published ([A-Z][a-z]{2}) (\d{1,2}), (\d{4})$")
RE_TABLEINTRO = re.compile(r"^The following feature sets are available for (.+)\.$")
RE_DATAROW = re.compile(r"^\|.*\|$")

warnings = []


def translate_title(t):
    """'X monitoring' -> 'Мониторинг X'; keep product names EN."""
    if t == "Operations: Cloud Monitoring & Logging":
        return t  # Google product-suite name, keep EN
    dep = ""
    if t.endswith(" (deprecated)"):
        dep = " (устарело)"
        t = t[: -len(" (deprecated)")]
    if t.endswith(" monitoring"):
        return "Мониторинг " + t[: -len(" monitoring")] + dep
    warnings.append("UNHANDLED TITLE: " + t)
    return t + dep


def translate_line(line, ctx):
    # frontmatter passthrough (byte-identical) for source/scraped/---
    if ctx["fm"]:
        if line == "---":
            ctx["fm"] = False if ctx["seen_close"] else ctx["fm"]
            if ctx["seen_close"]:
                ctx["fm"] = False
            else:
                ctx["seen_close"] = True
            return line
        if line.startswith("title: "):
            return "title: " + translate_title(line[len("title: ") :])
        return line  # source:, scraped: -> identical

    if line == "":
        return line
    # H1
    if line.startswith("# "):
        return "# " + translate_title(line[2:])
    # exact boilerplate
    if line in EXACT:
        return EXACT[line]
    # table header
    if line in HEADER:
        return HEADER[line]
    # table separator
    if set(line.replace("|", "").replace("-", "").replace(" ", "")) == set():
        return line  # | --- | --- | ... | passthrough
    # tag-line read time
    m = RE_READ.match(line)
    if m:
        return "* Чтение: {} мин".format(m.group(1))
    # tag-line published date
    m = RE_PUB.match(line)
    if m:
        mon = MONTHS.get(m.group(1), m.group(1))
        return "* Опубликовано {} {} {} г.".format(int(m.group(2)), mon, m.group(3))
    # metric-table intro
    m = RE_TABLEINTRO.match(line)
    if m:
        return "Для {} доступны следующие наборы функций.".format(m.group(1))
    # data row: translate ONLY the Unit column (index 3), keep others EN.
    # Header + separator are already handled above, so any remaining 6-cell
    # pipe-row here is a metric data row (identifiers may be googleapis.com OR
    # netapp.com, so do not gate on a specific host).
    if RE_DATAROW.match(line):
        cells = line.split("|")
        # cells: ['', ' fs ', ' name ', ' unit ', ' id ', '']
        if len(cells) == 6:
            unit_raw = cells[3].strip()
            if unit_raw in UNIT:
                cells[3] = " {} ".format(UNIT[unit_raw]) if UNIT[unit_raw] else "  "
            else:
                warnings.append("UNKNOWN UNIT '{}' in: {}".format(unit_raw, line))
            return "|".join(cells)
        warnings.append("DATAROW col!=6 ({}): {}".format(len(cells), line))
        return line
    # anything else -> warn, passthrough
    warnings.append("UNMATCHED: " + line)
    return line


def process(fname):
    en_path = os.path.join(EN_DIR, fname)
    ru_path = os.path.join(RU_DIR, fname)
    with open(en_path, "r", encoding="utf-8") as f:
        text = f.read()  # universal-newline -> \n
    lines = text.split("\n")
    ctx = {"fm": lines[0] == "---", "seen_close": False}
    out = []
    for ln in lines:
        out.append(translate_line(ln.rstrip("\r"), ctx))
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "wb") as f:
        f.write("\n".join(out).encode("utf-8"))
    return len(lines), len(out)


def main():
    files = sorted(f for f in os.listdir(EN_DIR) if f.endswith(".md"))
    total = 0
    for fn in files:
        en_n, ru_n = process(fn)
        flag = "OK" if en_n == ru_n else "LINE-MISMATCH!"
        if en_n != ru_n:
            print("  {}  EN={} RU={}  {}".format(fn, en_n, ru_n, flag))
        total += 1
    print("Processed {} files.".format(total))
    if warnings:
        print("\n=== WARNINGS ({}) ===".format(len(warnings)))
        for w in warnings[:60]:
            print("  " + w)
    else:
        print("No warnings: every line matched a rule.")


if __name__ == "__main__":
    main()
