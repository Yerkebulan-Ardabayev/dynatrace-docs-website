# -*- coding: utf-8 -*-
"""L4-IF.72 -- wmi-tutorial-03.md  (metric metadata)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial"

TRANS = {
    # H1 (duplicated)
    "# WMI tutorial - metric metadata": "# WMI tutorial - метаданные метрик",
    # meta
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Mar 30, 2022": "* Опубликовано 30 марта 2022 г.",
    # intro
    "With just the data source present in the extension, metric collection is rather raw: all metrics are referenced by key and everything appears without any measurement unit, which can make it confusing.": "Если в расширении определён только источник данных, сбор метрик минимален: все метрики идентифицируются только по ключу и отображаются без единиц измерения, что затрудняет их восприятие.",
    "The `metrics` section of the extension is there to define additional metadata for metrics. We can define the following:": "Раздел `metrics` расширения служит для определения дополнительных метаданных метрик. Доступны следующие поля:",
    "* `displayName` - Human-readable name of metric": "* `displayName`: понятное имя метрики",
    "* `description` - A description of what this metric actually represents": "* `description`: описание того, что измеряет данная метрика",
    "* `unit` - Measurement unit of the metric": "* `unit`: единица измерения метрики",
    "* `tags` - How we can easily find this metric in the Metrics catalog": "* `tags`: теги для быстрого поиска метрики в каталоге метрик",
    "* `metricProperties`": "* `metricProperties`",
    "+ `minValue` - The minimum possible value for the metric": "+ `minValue`: минимально возможное значение метрики",
    "+ `maxValue` - The maximum possible value for the metric": "+ `maxValue`: максимально возможное значение метрики",
    "+ `impactRelevant` - Whether this metric depends on other metric anomalies to form the root cause of a Problem": "+ `impactRelevant`: указывает, зависит ли данная метрика от аномалий других метрик для формирования первопричины проблемы",
    "+ `rootCauseRelevant` - Whether this metric on its own can be the root cause of a Problem": "+ `rootCauseRelevant`: указывает, может ли данная метрика самостоятельно быть первопричиной проблемы",
    "+ `valueType` - Whether high values are good (`score`) or bad (`error`)": "+ `valueType`: определяет, являются ли высокие значения положительными (`score`) или отрицательными (`error`)",
    # Define section
    "## Define metadata": "## Определение метаданных",
    "1. Add the `metrics` section to your `extension.yaml` using the template below.": "1. Добавьте раздел `metrics` в файл `extension.yaml` по приведённому шаблону.",
    "2. Define metadata for every metric collected.": "2. Определите метаданные для каждой собираемой метрики.",
    "3. At minimum, define `displayName`, `description`, and `unit`": "3. Укажите как минимум `displayName`, `description` и `unit`.",
    "4. Package and upload a new version of your extension": "4. Соберите и загрузите новую версию пакета расширения.",
    "5. Validate metadata.": "5. Проверьте метаданные.",
    'For more information on the WMI data source syntax, see [WMI data source reference](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference "Learn about WMI extensions in the Extensions framework.").': 'Дополнительные сведения о синтаксисе источника данных WMI см. в разделе [Справочник по источнику данных WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference "Узнайте о расширениях WMI в платформе Extensions framework.").',
    # Results
    "## Results": "## Результаты",
    'You should now see the metadata reflected in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."):': 'Метаданные должны отобразиться в [браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики в браузере метрик Dynatrace."):',
    "![result](https://dt-cdn.net/images/wmi-tutorial-metadata-1280-c5b9547495.png)": "![result](https://dt-cdn.net/images/wmi-tutorial-metadata-1280-c5b9547495.png)",
    "result": "result",
    '**Next step**: [Custom topology](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-04 "Learn about WMI extensions in the Extensions framework.")': '**Следующий шаг**: [Пользовательская топология](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-04 "Узнайте о расширениях WMI в платформе Extensions framework.")',
}

PASS = {
    "title: WMI tutorial - metric metadata",
}

if __name__ == "__main__":
    build_one(REL, "wmi-tutorial-03.md", TRANS, PASS)
    qa_one(REL, "wmi-tutorial-03.md")
