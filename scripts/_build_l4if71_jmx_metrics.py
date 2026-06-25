# -*- coding: utf-8 -*-
"""Builder for zos-java-custom-jmx-metrics.md (L4-IF.71 canon)."""

import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring"
FN = "zos-java-custom-jmx-metrics.md"

# EN source uses plain ASCII — no scraping mojibake in this file.
# JMX metric names, MBean attributes, field names (name/source/domain/
# keyProperties/attribute/attributePath/allowAdditionalKeys/calculateDelta/
# calculateRate/aggregation/splittings/keyProperty), aggregation values
# (SUM/AVG/MIN/MAX), and concrete metric identifiers
# (java.lang.CurrentThreadCount, java.lang.HeapMemoryUsage,
# java.lang.MemoryPoolUsage) are EN-lock per corpus convention
# (see install-zos-java.md tables where metric names stay EN).
# WARN on those lines from qa_one is legitimate — they contain only EN prose
# that is intentionally kept verbatim (field descriptions in table cells that
# are purely EN technical identifiers).

TRANS = {
    # --- frontmatter ---
    "title: Monitor JMX metrics on z/OS": "title: Мониторинг метрик JMX в z/OS",
    # --- h1 (appears twice) ---
    "# Monitor JMX metrics on z/OS": "# Мониторинг метрик JMX в z/OS",
    # --- metadata ---
    "* 5-min read": "* Чтение: 5 мин",
    "* Published Sep 06, 2022": "* Опубликовано 6 сентября 2022 г.",
    # --- intro paragraph ---
    "JMX (Java Management Extensions) is handy for monitoring applications built using Java. With the OneAgent z/OS Java code module, you can monitor any metric in your JVM that is exposed via an MBean.": "JMX (Java Management Extensions) удобен для мониторинга приложений, созданных на Java. С помощью кодового модуля z/OS Java OneAgent можно отслеживать любую метрику JVM, доступную через MBean.",
    # --- bullets under intro ---
    '* Every monitored custom JMX metric consumes Davis data units. The concept of [Included metrics per host unit](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") isn\'t applicable for monitored LPARs on z/OS. To learn more about Davis data units, see [DDUs for metrics](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").': '* Каждая отслеживаемая пользовательская метрика JMX потребляет Davis data units. Концепция [Included metrics per host unit](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Узнайте, как рассчитывается потребление Davis data units и связанные расходы на мониторируемые метрики.") неприменима для мониторируемых LPAR в z/OS. Подробнее о Davis data units см. в разделе [DDUs for metrics](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Узнайте, как рассчитывается потребление Davis data units и связанные расходы на мониторируемые метрики.").',
    "* [PMI (Performance Monitoring Infrastructure)\xef\xbb\xbf](https://www.ibm.com/docs/en/was/9.0.5?topic=health-performance-monitoring-infrastructure-pmi) for the IBM WebSphere Application Server is currently not supported.": "* [PMI (Performance Monitoring Infrastructure)](https://www.ibm.com/docs/en/was/9.0.5?topic=health-performance-monitoring-infrastructure-pmi) для IBM WebSphere Application Server в настоящее время не поддерживается.",
    # --- ## Definition ---
    "## Definition": "## Определение",
    "The `customJmxMetrics` attribute defines a list of [metrics](#metrics) to be monitored. To get started, add the `customJmxMetrics` attribute to your `dtconfig.json` file as shown in the following example.": "Атрибут `customJmxMetrics` задаёт список [метрик](#metrics) для мониторинга. Чтобы начать, добавьте атрибут `customJmxMetrics` в файл `dtconfig.json`, как показано в следующем примере.",
    'Typically, you\'ve created the `dtconfig.json` file during the [z/OS Java code module installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Set up Java monitoring on z/OS using the Java module.") and have set the attributes `Tenant`, `ClusterID`, and `zdcName` to your environment.': 'Как правило, файл `dtconfig.json` создаётся при [установке кодового модуля z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Настройте мониторинг Java в z/OS с помощью модуля Java."), где задаются атрибуты `Tenant`, `ClusterID` и `zdcName` для вашего окружения.',
    # --- ## Metrics ---
    "## Metrics": "## Метрики",
    "Each metric has the following mandatory attributes:": "Каждая метрика имеет следующие обязательные атрибуты:",
    "| Field | Type | Description |": "| Поле | Тип | Описание |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| `name` | String | Sets the name of the metric in Dynatrace. It must start with a letter. Only alphanumeric characters or `.` are allowed. |": "| `name` | String | Задаёт имя метрики в Dynatrace. Должно начинаться с буквы. Допустимы только буквенно-цифровые символы или `.`. |",
    "| `source` | Object | Specifies how the metric is collected. For details, see the [Source](#source) section below. |": "| `source` | Object | Определяет способ сбора метрики. Подробнее см. раздел [Source](#source) ниже. |",
    # --- ## Source ---
    "## Source": "## Source",
    "The source specifies how a metric is collected using JMX. Each source has the following mandatory attributes:": "Source определяет, как метрика собирается с помощью JMX. Каждый source имеет следующие обязательные атрибуты:",
    "| `domain` | String | Domain name of the MBean. It can contain wildcards (`*`). |": "| `domain` | String | Имя домена MBean. Может содержать символы подстановки (`*`). |",
    "| `keyProperties` | Key, Value pairs | Key properties of the MBean. Values can contain wildcards (`*`). |": "| `keyProperties` | Key, Value pairs | Ключевые свойства MBean. Значения могут содержать символы подстановки (`*`). |",
    "| `attribute` | String | Name of the attribute that contains the metric value. |": "| `attribute` | String | Имя атрибута, содержащего значение метрики. |",
    "Optional source attributes are:": "Необязательные атрибуты source:",
    "| `attributePath` | String | See [CompositeData] below.(#compositedata) |": "| `attributePath` | String | См. раздел [CompositeData] ниже.(#compositedata) |",
    "| `allowAdditionalKeys` | Boolean | If true, additional key properties other than those specified in `keyProperties` are allowed but ignored. If false, the `keyProperties` need to match exactly; additional keys in the name will lead to a mismatch. |": "| `allowAdditionalKeys` | Boolean | Если `true`, дополнительные ключевые свойства помимо указанных в `keyProperties` допустимы, но игнорируются. Если `false`, `keyProperties` должны совпадать точно; дополнительные ключи приведут к несовпадению. |",
    "| `calculateDelta` | bool | If true, calculate the change in values of the given attribute. Value = attribute(t) - attribute(t-1). This is useful for monotonically increasing values. |": "| `calculateDelta` | bool | Если `true`, вычисляется изменение значений указанного атрибута. Значение = attribute(t) - attribute(t-1). Полезно для монотонно возрастающих значений. |",
    "| `calculateRate` | bool | If true, calculate the rate of changes per second. This is used in combination with `calculateDelta` to convert an absolute attribute (for example, Request Count) to a rate (for example, Requests per Second). Value = attribute / query interval. |": "| `calculateRate` | bool | Если `true`, вычисляется скорость изменений в секунду. Используется вместе с `calculateDelta` для преобразования абсолютного атрибута (например, Request Count) в скорость (например, Requests per Second). Значение = attribute / интервал запроса. |",
    "| `aggregation` | String | Aggregates multiple values if more than one MBean matches the domain and key property filter. Default aggregation is `SUM`. Available aggregations are: `SUM`, `AVG`, `MIN`, `MAX`. For example, you can use this attribute to aggregate all `MemoryPools` and calculate their `SUM` or `MAX` value. |": "| `aggregation` | String | Агрегирует несколько значений, если более одного MBean соответствует фильтру домена и ключевых свойств. Агрегация по умолчанию: `SUM`. Доступные агрегации: `SUM`, `AVG`, `MIN`, `MAX`. Например, можно агрегировать все `MemoryPools` и вычислять значение `SUM` или `MAX`. |",
    "| `splittings` | List | Set [splittings](#splittings). |": "| `splittings` | List | Задаёт [splittings](#splittings). |",
    # --- ### AttributePath (CompositeData) ---
    "### AttributePath (CompositeData)": "### AttributePath (CompositeData)",
    "To extract values of individual keys returned as `CompositeData` type by an attribute, you need to use the `attributePath` mechanism and point to the key you're interested in.": "Чтобы извлечь значения отдельных ключей, возвращаемых атрибутом с типом `CompositeData`, используйте механизм `attributePath` и укажите нужный ключ.",
    "For example, `HeapMemoryUsage` is a `CompositeData` type that returns the following list of value-key pairs:": "Например, `HeapMemoryUsage` имеет тип `CompositeData` и возвращает следующий список пар ключ-значение:",
    "If you want to extract the value of `used` from the `HeapMemoryUsage` attribute, point the `attributePath` to the `used` key.": "Чтобы извлечь значение `used` из атрибута `HeapMemoryUsage`, укажите в `attributePath` ключ `used`.",
    # --- ### Splittings ---
    "### Splittings": "### Splittings",
    "Splittings can be used to define additional dimensions for a metric.": "Splittings позволяют задавать дополнительные измерения для метрики.",
    "Each splitting has the following mandatory attributes:": "Каждый splitting имеет следующие обязательные атрибуты:",
    "| `name` | String | Sets the name for this dimension. |": "| `name` | String | Задаёт имя измерения. |",
    "| `keyProperty` | String | Defines which key property of the `ObjectName` of an MBean is used for splitting. See the `keyProperties` attribute of the [source](#source). |": "| `keyProperty` | String | Определяет, какое ключевое свойство `ObjectName` MBean используется для splitting. См. атрибут `keyProperties` раздела [source](#source). |",
    "The following example shows how to define a metric providing multiple dimensions within a single metric definition:": "Следующий пример показывает, как задать метрику с несколькими измерениями в рамках одного определения метрики:",
    "Based on this metric definition, the following MBeans:": "На основе этого определения метрики следующие MBeans:",
    "* `java.lang:type=MemoryPool,name=G1 Eden Space`": "* `java.lang:type=MemoryPool,name=G1 Eden Space`",
    "* `java.lang:type=MemoryPool,name=G1 Survivor Space`": "* `java.lang:type=MemoryPool,name=G1 Survivor Space`",
    "will result in a single metric in Dynatrace with two dimensions:": "дадут в Dynatrace одну метрику с двумя измерениями:",
    "* `java.lang.MemoryPoolUsage` with the dimension `memory_type=G1 Eden Space`": "* `java.lang.MemoryPoolUsage` с измерением `memory_type=G1 Eden Space`",
    "* `java.lang.MemoryPoolUsage` with the dimension `memory_type=G1 Survivor Space`": "* `java.lang.MemoryPoolUsage` с измерением `memory_type=G1 Survivor Space`",
    # --- ## Monitoring ---
    "## Monitoring": "## Мониторинг",
    'Go to [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") to analyze and chart your custom JMX metrics. If needed, you can pin your charts to a dashboard. In the following example, you can see the `java.lang.MemoryPoolUsage` metric split by the dimension `memory_type`:': 'Перейдите в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужной информации.") для анализа и построения графиков пользовательских метрик JMX. При необходимости можно закрепить графики на дашборде. В следующем примере показана метрика `java.lang.MemoryPoolUsage` с разбивкой по измерению `memory_type`:',
    "![Data Explorer with z/OS JMX metrics](https://dt-cdn.net/images/data-explorer-1643-7696285fbf.png)": "![Data Explorer с метриками JMX z/OS](https://dt-cdn.net/images/data-explorer-1643-7696285fbf.png)",
    "Data Explorer with z/OS JMX metrics": "Data Explorer с метриками JMX z/OS",
    'To get a list of metrics available in your monitoring environment, Go to **Metrics** to open the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."). In the following example, you can see the three metrics that we have created above:': 'Чтобы получить список метрик, доступных в вашем окружении мониторинга, перейдите в **Metrics** для открытия [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."). В следующем примере показаны три метрики, созданные выше:',
    "![Metrics browser with z/OS JMX metrics](https://dt-cdn.net/images/metrics-browser-1636-1096adef93.png)": "![Metrics browser с метриками JMX z/OS](https://dt-cdn.net/images/metrics-browser-1636-1096adef93.png)",
    "Metrics browser with z/OS JMX metrics": "Metrics browser с метриками JMX z/OS",
    # --- ## Related topics ---
    "## Related topics": "## Связанные темы",
    '* [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.")': '* [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace.")',
    '* [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")': '* [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужной информации.")',
}

# Lines that must remain verbatim EN.
# MBean field names in table cells (name/source/domain/keyProperties/attribute/
# attributePath/allowAdditionalKeys/calculateDelta/calculateRate/aggregation/
# splittings/keyProperty) are already embedded in pipe-table rows translated
# above via backtick. No standalone EN-only non-code lines remain after the
# TRANS dict above.
PASS = set()

if __name__ == "__main__":
    build_one(REL, FN, TRANS, PASS)
    qa_one(REL, FN)
