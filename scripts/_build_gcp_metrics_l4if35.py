# -*- coding: utf-8 -*-
"""
L4-IF.35 build script: GCP per-service monitoring leaves (5 files, cross-dir).

Same byte-uniform boilerplate as L4-IF.34 (gcp-supported-service-metrics-new/),
but these 5 leaves live under different parent dirs:
  gcp-integrations/cloudrun/cloud-run-monitoring.md
  gcp-integrations/gcp-functions/cloud-functions-monitoring.md
  gcp-integrations/google-app-engine/app-engine-monitoring.md
  gcp-integrations/google-compute-engine/compute-engine-monitoring.md
  gcp-integrations/google-gke/google-kubernetes-engine-monitoring.md

Deltas vs L4-IF.34:
  - explicit file list (cross-dir) instead of os.listdir(one dir);
  - UNIT += NanoSecond -> Наносекунда, MebiByte -> Мебибайт
    (consistent with Микро/Милли and Гиби/Гига; verified absent from map);
  - SPECIAL_TITLES for the two '... with Operations suite metrics monitoring'
    headings (generic 'X monitoring' rule would leave English mid-title).

Canon identical to L4-IF.34: table HEADER translated, "Name" VALUES kept EN
(findability), "Unit" VALUES translated, Feature set / GCP identifier kept EN.
source:/scraped: byte-identical. LF, no BOM. em-dash = 0.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_EN = os.path.join(ROOT, "docs", "managed", "ingest-from", "google-cloud-platform")
BASE_RU = os.path.join(
    ROOT, "docs", "managed-ru", "ingest-from", "google-cloud-platform"
)

FILES = [
    "gcp-integrations/cloudrun/cloud-run-monitoring.md",
    "gcp-integrations/gcp-functions/cloud-functions-monitoring.md",
    "gcp-integrations/google-app-engine/app-engine-monitoring.md",
    "gcp-integrations/google-compute-engine/compute-engine-monitoring.md",
    "gcp-integrations/google-gke/google-kubernetes-engine-monitoring.md",
]

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

HEADER = {
    "| Feature set | Name | Unit | GCP metric identifier |": "| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |",
    "| Feature Set | Name | Unit | GCP metric identifier |": "| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |",
}

UNIT = {
    "Count": "Количество",
    "Byte": "Байт",
    "MilliSecond": "Миллисекунда",
    "MicroSecond": "Микросекунда",
    "NanoSecond": "Наносекунда",
    "Second": "Секунда",
    "Percent": "Процент",
    "Unspecified": "Не указано",
    "MebiByte": "Мебибайт",
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

# Two titles where the generic 'X monitoring' -> 'Мониторинг X' rule would leave
# 'with Operations suite metrics' in English mid-phrase. Operations suite is a
# Google product name (kept EN), the descriptive 'with ... metrics' is translated.
SPECIAL_TITLES = {
    "Google App Engine with Operations suite metrics monitoring": "Мониторинг Google App Engine с метриками Operations suite",
    "Google Compute Engine with Operations suite metrics monitoring": "Мониторинг Google Compute Engine с метриками Operations suite",
}

RE_READ = re.compile(r"^\* (\d+)-min read$")
RE_PUB = re.compile(r"^\* Published ([A-Z][a-z]{2}) (\d{1,2}), (\d{4})$")
RE_UPD = re.compile(r"^\* Updated on ([A-Z][a-z]{2}) (\d{1,2}), (\d{4})$")
RE_TABLEINTRO = re.compile(r"^The following feature sets are available for (.+)\.$")
RE_DATAROW = re.compile(r"^\|.*\|$")

warnings = []


def translate_title(t):
    if t in SPECIAL_TITLES:
        return SPECIAL_TITLES[t]
    if t == "Operations: Cloud Monitoring & Logging":
        return t
    dep = ""
    if t.endswith(" (deprecated)"):
        dep = " (устарело)"
        t = t[: -len(" (deprecated)")]
    if t.endswith(" monitoring"):
        return "Мониторинг " + t[: -len(" monitoring")] + dep
    warnings.append("UNHANDLED TITLE: " + t)
    return t + dep


def translate_line(line, ctx):
    if ctx["fm"]:
        if line == "---":
            if ctx["seen_close"]:
                ctx["fm"] = False
            else:
                ctx["seen_close"] = True
            return line
        if line.startswith("title: "):
            return "title: " + translate_title(line[len("title: ") :])
        return line

    if line == "":
        return line
    if line.startswith("# "):
        return "# " + translate_title(line[2:])
    if line in EXACT:
        return EXACT[line]
    if line in HEADER:
        return HEADER[line]
    if set(line.replace("|", "").replace("-", "").replace(" ", "")) == set():
        return line  # separator passthrough
    m = RE_READ.match(line)
    if m:
        return "* Чтение: {} мин".format(m.group(1))
    m = RE_PUB.match(line)
    if m:
        mon = MONTHS.get(m.group(1), m.group(1))
        return "* Опубликовано {} {} {} г.".format(int(m.group(2)), mon, m.group(3))
    m = RE_UPD.match(line)
    if m:
        mon = MONTHS.get(m.group(1), m.group(1))
        return "* Обновлено {} {} {} г.".format(int(m.group(2)), mon, m.group(3))
    m = RE_TABLEINTRO.match(line)
    if m:
        return "Для {} доступны следующие наборы функций.".format(m.group(1))
    if RE_DATAROW.match(line):
        cells = line.split("|")
        if len(cells) == 6:
            unit_raw = cells[3].strip()
            if unit_raw in UNIT:
                cells[3] = " {} ".format(UNIT[unit_raw]) if UNIT[unit_raw] else "  "
            else:
                warnings.append("UNKNOWN UNIT '{}' in: {}".format(unit_raw, line))
            return "|".join(cells)
        warnings.append("DATAROW col!=6 ({}): {}".format(len(cells), line))
        return line
    warnings.append("UNMATCHED: " + line)
    return line


def process(rel):
    en_path = os.path.join(BASE_EN, rel)
    ru_path = os.path.join(BASE_RU, rel)
    with open(en_path, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    ctx = {"fm": lines[0] == "---", "seen_close": False}
    out = [translate_line(ln.rstrip("\r"), ctx) for ln in lines]
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "wb") as f:
        f.write("\n".join(out).encode("utf-8"))
    return len(lines), len(out)


def main():
    for rel in FILES:
        en_n, ru_n = process(rel)
        flag = "OK" if en_n == ru_n else "LINE-MISMATCH!"
        print("  {:60s} EN={} RU={}  {}".format(rel.split("/")[-1], en_n, ru_n, flag))
    print("Processed {} files.".format(len(FILES)))
    if warnings:
        print("\n=== WARNINGS ({}) ===".format(len(warnings)))
        for w in warnings[:60]:
            print("  " + w)
    else:
        print("No warnings: every line matched a rule.")


if __name__ == "__main__":
    main()
