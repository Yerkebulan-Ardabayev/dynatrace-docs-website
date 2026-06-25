# -*- coding: utf-8 -*-
"""L4-IF.72 -- wmi-tutorial-02.md  (data source)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial"

TRANS = {
    # H1 (duplicated)
    "# WMI tutorial - data source": "# WMI tutorial - источник данных",
    # meta
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Published Mar 30, 2022": "* Опубликовано 30 марта 2022 г.",
    # intro
    "To enable your extension to collect metrics and have those metrics ingested into Dynatrace, you must define a data source. In this tutorial we're using the WMI data source. This must be a section called `wmi` in your extension.": "Чтобы расширение собирало метрики и передавало их в Dynatrace, необходимо определить источник данных. В этом учебном руководстве используется источник данных WMI. Это должен быть раздел с именем `wmi` в расширении.",
    "The purpose of the `wmi` section is to define the WMI queries that retrieve your metrics, how often they should run, and how to map their results to metrics and dimensions that Dynatrace can ingest. Groups and subgroups are used to organize data and define shared properties like dimensions and running frequency.": "Раздел `wmi` определяет WMI-запросы для получения метрик, периодичность их выполнения и правила сопоставления результатов с метриками и измерениями Dynatrace. Группы и подгруппы служат для организации данных и задания общих свойств: измерений и частоты выполнения.",
    "For our extension, we're using 3 WMI Queries. We'll add them to our `extension.yaml` and ingest their result as Dynatrace metrics:": "В расширении используются 3 WMI-запроса. Их нужно добавить в `extension.yaml` и передать результаты как метрики Dynatrace:",
    "* Extract CPU Usage, User CPU, and Idle CPU for each of the host's processors (split by CPU ID).": "* Извлечь загрузку ЦП, пользовательское время и время простоя для каждого процессора хоста (разбивка по идентификатору ЦП).",
    "* Extract the Total, Sent, and Received Bytes per second for each network adapter running on the host": "* Извлечь суммарные, отправленные и полученные байты в секунду для каждого сетевого адаптера хоста.",
    "* Extract the Total, Sent, and Received Bytes per second for each network interface running on the host": "* Извлечь суммарные, отправленные и полученные байты в секунду для каждого сетевого интерфейса хоста.",
    # Tips section
    "## Tips": "## Советы",
    "### Metric best practices": "### Рекомендации по именованию метрик",
    "Prefix your metric keys with the name of the extension to avoid clashes with other metrics in Dynatrace. For this exercise, we prefix each metric key with `custom.demo.host-observability`.": "Добавляйте к ключам метрик префикс с именем расширения, чтобы избежать конфликтов с другими метриками в Dynatrace. В этом упражнении каждый ключ метрики начинается с `custom.demo.host-observability`.",
    "### Host dimension": "### Измерение хоста",
    "You can identify the host running the extension through the `this:device.host` passed as a dimension value.": "Хост, на котором выполняется расширение, можно идентифицировать с помощью значения измерения `this:device.host`.",
    "### Static dimensions": "### Статические измерения",
    "You can add dimensions that are fixed strings using the prefix `const:`.": "Измерения с фиксированными строками добавляются с помощью префикса `const:`.",
    # Define section
    "## Define your data source": "## Определение источника данных",
    "Add the `wmi` section to your `extension.yaml` using the template below.": "Добавьте раздел `wmi` в файл `extension.yaml` по приведённому шаблону.",
    "1. Create two groups called `Host` and `Network` that run every 1 min. Both groups should have a dimension that identifies the host running the extension.": "1. Создайте две группы с именами `Host` и `Network` с интервалом выполнения 1 мин. В обеих группах должно быть измерение, идентифицирующее хост.",
    "2. Create a subgroup for each WMI query given above and map the columns retrieved to metrics and dimensions.": "2. Создайте подгруппу для каждого WMI-запроса и сопоставьте полученные столбцы с метриками и измерениями.",
    "3. Add a dimension called `network.type` that takes the value `Adapter` or `Interface`, depending on the WMI query.": "3. Добавьте измерение `network.type` со значением `Adapter` или `Interface` в зависимости от WMI-запроса.",
    "4. Package a new version of your extension and upload it.": "4. Соберите новую версию пакета расширения и загрузите её.",
    "5. Configure it to monitor your Windows host. You can do it during extension activation in Dynatrace Hub.": "5. Настройте мониторинг хоста Windows. Это можно сделать при активации расширения в Dynatrace Hub.",
    "6. Give it a minute, and then validate metric collection.": "6. Подождите одну минуту и проверьте сбор метрик.",
    'For more information on the WMI data source syntax, see [WMI data source reference](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference "Learn about WMI extensions in the Extensions framework.").': 'Дополнительные сведения о синтаксисе источника данных WMI см. в разделе [Справочник по источнику данных WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference "Узнайте о расширениях WMI в платформе Extensions framework.").',
    # Results
    "## Results": "## Результаты",
    'Your six metrics should show up in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."). To find them, filter by text `custom.demo`.': 'Шесть метрик должны появиться в [браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики в браузере метрик Dynatrace."). Для их поиска отфильтруйте по тексту `custom.demo`.',
    "![result](https://dt-cdn.net/images/wmi-tutorial-metricbrowser-1590-12b46b5f17.png)": "![result](https://dt-cdn.net/images/wmi-tutorial-metricbrowser-1590-12b46b5f17.png)",
    "result": "result",
    '**Next step**: [Metric metadata](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-03 "Learn about WMI extensions in the Extensions framework.")': '**Следующий шаг**: [Метаданные метрик](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-03 "Узнайте о расширениях WMI в платформе Extensions framework.")',
}

PASS = {
    "title: WMI tutorial - data source",
}

if __name__ == "__main__":
    build_one(REL, "wmi-tutorial-02.md", TRANS, PASS)
    qa_one(REL, "wmi-tutorial-02.md")
