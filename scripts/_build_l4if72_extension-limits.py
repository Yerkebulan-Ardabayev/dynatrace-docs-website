# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/extension-limits.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions"

TRANS = {
    "# Extensions limits": "# Ограничения Extensions",
    "* How-to guide": "* Практическое руководство",
    "* 5-min read": "* Чтение: 5 мин",
    "* Updated on Apr 09, 2026": "* Обновлено 9 апреля 2026 г.",
    "This page lists the default limits of the Dynatrace Extensions Framework. These limits ensure optimal performance and resource management, so make sure you're aware of them before you start using extensions.": "На этой странице перечислены ограничения по умолчанию для Dynatrace Extensions Framework. Эти ограничения обеспечивают оптимальную производительность и управление ресурсами, поэтому ознакомьтесь с ними до начала использования расширений.",
    "### Extension": "### Расширение",
    "| Type | Limit | Description |": "| Тип | Предел | Описание |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| --- | --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- | --- |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| --- | --- | --- | --- |": "| --- | --- | --- | --- |",
    "| Dashboards | 10 | The maximum number of dashboards you can define for a single extension. |": "| Dashboards | 10 | Максимальное количество дашбордов, которое можно определить для одного расширения. |",
    "| Alerts | Dynatrace version 1.304+ 100 Dynatrace version 1.303 and earlier 10 | The maximum number of alerts for a single extension. |": "| Alerts | Dynatrace версии 1.304+ 100, Dynatrace версии 1.303 и ранее 10 | Максимальное количество оповещений для одного расширения. |",
    "| Metrics (total for the extension) | 500 | The limit of metrics you can define for the entire extension. |": "| Метрики (всего для расширения) | 500 | Предел количества метрик, которое можно определить для всего расширения. |",
    "| Metrics (per level) | 100 | The limit of metrics you can define for each level (extension, group, subgroup) of declarative extensions. |": "| Метрики (на уровень) | 100 | Предел количества метрик, которое можно определить для каждого уровня (расширение, группа, подгруппа) декларативных расширений. |",
    "| ZIP package size | 25 MB | The limit for a single extension ZIP package. |": "| Размер ZIP-пакета | 25 МБ | Предел размера одного ZIP-пакета расширения. |",
    "| Configurations handled by ActiveGate or OneAgent | 100 | The limit of configurations that can be run simultaneously either on ActiveGate or OneAgent. For remote activation, one configuration can be split into buckets, and each bucket is treated as a separate configuration. |": "| Конфигурации, обрабатываемые ActiveGate или OneAgent | 100 | Предел количества конфигураций, которые могут выполняться одновременно на ActiveGate или OneAgent. При удалённой активации одна конфигурация может разбиваться на блоки, каждый из которых рассматривается как отдельная конфигурация. |",
    "### Data source type": "### Тип источника данных",
    "| Type | SNMP | SNMP traps | WMI | Prometheus | SQL |": "| Тип | SNMP | SNMP traps | WMI | Prometheus | SQL |",
    "| --- | --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- | --- |",
    "| Groups | 10 | 10 | 10 | 10 | 20 |": "| Группы | 10 | 10 | 10 | 10 | 20 |",
    "| Subgroups[1](#fn-1-1-def) | 10 | N/A | 25 | 10 | 20 |": "| Подгруппы[1](#fn-1-1-def) | 10 | Н/Д | 25 | 10 | 20 |",
    "| Dimensions[2](#fn-1-2-def) | 25 | 5 | 25 | 25 | 25 |": "| Измерения[2](#fn-1-2-def) | 25 | 5 | 25 | 25 | 25 |",
    "1": "1",
    "The number of subgroups each group can contain. For some data sources, adding subgroups is not available.": "Количество подгрупп, которое может содержать каждая группа. Для некоторых источников данных добавление подгрупп недоступно.",
    "2": "2",
    "The number of dimensions can be defined in the extension YAML file for each level (extension, group, subgroup).": "Количество измерений, которое можно определить в файле YAML расширения для каждого уровня (расширение, группа, подгруппа).",
    "In Kubernetes environments, only JMX extensions are supported.": "В средах Kubernetes поддерживаются только расширения JMX.",
    "### Environment": "### Окружение",
    "| Extensions | 250 | Number of extensions that can be added to a given Dynatrace environment. |": "| Расширения | 250 | Количество расширений, которые можно добавить в конкретное окружение Dynatrace. |",
    "| Extension versions | 10 | Your environment can manage 10 versions of a single extension. |": "| Версии расширений | 10 | Окружение может управлять 10 версиями одного расширения. |",
    "| Monitoring configurations per extension | 100 | Based on a single environment configuration. Each of the monitoring configurations runs in parallel. |": "| Конфигурации мониторинга на расширение | 100 | Основано на одной конфигурации окружения. Каждая конфигурация мониторинга выполняется параллельно. |",
    "### Device monitoring configuration per data source": "### Конфигурация мониторинга устройства на источник данных",
    "#### Remote activation": "#### Удалённая активация",
    "This feature is automatically enabled for WMI, Prometheus, SNMP, and SQL extensions, while for other types of extensions, its activation depends on the specific extension.": "Эта функция включается автоматически для расширений WMI, Prometheus, SNMP и SQL, тогда как для других типов расширений её активация зависит от конкретного расширения.",
    "| Devices[1](#fn-2-1-def) | 20,000 | 100 | 20,000[2](#fn-2-2-def) | 20,000 | 20,000 |": "| Устройства[1](#fn-2-1-def) | 20 000 | 100 | 20 000[2](#fn-2-2-def) | 20 000 | 20 000 |",
    "You can define up to 20,000 devices for a single monitoring configuration. Configurations are split into buckets, with a default size of 100 devices per bucket. Each bucket of devices is polled independently as a separate process on one of the ActiveGates in a group.": "Для одной конфигурации мониторинга можно определить до 20 000 устройств. Конфигурации разбиваются на блоки с размером по умолчанию 100 устройств в каждом. Каждый блок устройств опрашивается независимо как отдельный процесс на одном из ActiveGate в группе.",
    "Remote WMI monitoring is limited to 100 queries, no matter how many devices are in the configuration. If more devices are configured, you may experience performance issues and gaps in monitoring data.": "Удалённый мониторинг WMI ограничен 100 запросами независимо от количества устройств в конфигурации. При настройке большего числа устройств возможны проблемы с производительностью и пробелы в данных мониторинга.",
    "### Metric ingestion": "### Приём метрик",
    "| Entity | Limit | Description |": "| Сущность | Предел | Описание |",
    "| Metric key length, characters | 250 | The total length of the metric key, including the prefix. |": "| Длина ключа метрики, символов | 250 | Общая длина ключа метрики, включая префикс. |",
    "| Dimension key length, characters | 100 | The total length of the dimension key. |": "| Длина ключа измерения, символов | 100 | Общая длина ключа измерения. |",
    "| Dimension value length, characters | 255 | The total length of the dimension value. |": "| Длина значения измерения, символов | 255 | Общая длина значения измерения. |",
    "| Number of dimensions per line | 50 | The number of dimensions in a single line of the payload. |": "| Количество измерений в строке | 50 | Количество измерений в одной строке полезной нагрузки. |",
    "| Total number of possible metric keys per environment | 100,000 | The maximum number of metric keys that can be registered in Dynatrace. |": "| Общее количество возможных ключей метрик на окружение | 100 000 | Максимальное количество ключей метрик, которые можно зарегистрировать в Dynatrace. |",
    "| Number of tuples per month per metric | 1,000,000 | The maximum number of tuples (unique metric-dimension key-dimension value-payload type combinations) for each metric key for the last 30 days. |": "| Количество кортежей в месяц на метрику | 1 000 000 | Максимальное количество кортежей (уникальных комбинаций метрика-ключ измерения-значение измерения-тип полезной нагрузки) для каждого ключа метрики за последние 30 дней. |",
    "| Number of tuples per month for all custom metrics | 50,000,000 | The maximum number of tuples (unique metric-dimension key-dimension value-payload type combinations) for all custom metrics for the last 30 days. |": "| Количество кортежей в месяц для всех пользовательских метрик | 50 000 000 | Максимальное количество кортежей (уникальных комбинаций метрика-ключ измерения-значение измерения-тип полезной нагрузки) для всех пользовательских метрик за последние 30 дней. |",
    "| Length of line, characters | 50,000 | The maximum length of a single line of the payload. |": "| Длина строки, символов | 50 000 | Максимальная длина одной строки полезной нагрузки. |",
    "There's also a limit to the number of metrics that Dynatrace can ingest.": "Существует также ограничение на количество метрик, которые Dynatrace может принять.",
    "| Channel | Limit |": "| Канал | Предел |",
    "| --- | --- |": "| --- | --- |",
    '| [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.") | Per minute per OneAgent instance:  OneAgent version 1.213 and earlier 1,000  OneAgent version 1.215+ 100,000 |': '| [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте Dynatrace API для получения метрик отслеживаемых объектов.") | В минуту на экземпляр OneAgent: OneAgent версии 1.213 и ранее 1 000, OneAgent версии 1.215+ 100 000 |',
    '| [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") | There\'s no limit to the metric number, but [API throttling](/managed/dynatrace-api/basics/access-limit#throttling "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.") applies. |': '| [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Принимайте пользовательские метрики в Dynatrace через Metrics v2 API.") | Ограничения на количество метрик нет, но действует [регулирование API](/managed/dynatrace-api/basics/access-limit#throttling "Узнайте об ограничениях полезной нагрузки и регулировании запросов, которые могут повлиять на использование Dynatrace API."). |',
    "### Resource consumption": "### Потребление ресурсов",
    "In the following tables:": "В следующих таблицах:",
    "* Soft limit: Once this limit is reached, the Extension Execution Controller (EEC) no longer accepts new configuration requests.": "* Мягкий предел: при достижении этого предела Extension Execution Controller (EEC) перестаёт принимать новые запросы конфигурации.",
    "* Hard limit: Once reached, the EEC will terminate existing configuration processes until the resource usage becomes lower.": "* Жёсткий предел: при достижении EEC завершает существующие процессы конфигурации до тех пор, пока потребление ресурсов не снизится.",
    "* Per instance: Each data source process represents a single extension activation assigned to a given host or an ActiveGate group.": "* На экземпляр: каждый процесс источника данных представляет одну активацию расширения, назначенную конкретному хосту или группе ActiveGate.",
    "* Per configuration: Shows the consumption volume for one data source in OneAgent and ActiveGate.": "* На конфигурацию: показывает объём потребления для одного источника данных в OneAgent и ActiveGate.",
    "* For all data source processes: Refers to the sum of the resources consumed by the EEC and all data source processes in OneAgent and ActiveGate.": "* Для всех процессов источников данных: сумма ресурсов, потребляемых EEC и всеми процессами источников данных в OneAgent и ActiveGate.",
    "#### OneAgent": "#### OneAgent",
    "##### Per instance": "##### На экземпляр",
    "| Performance profile | CPU | RAM |": "| Профиль производительности | CPU | RAM |",
    "| Default | 2% | 100 MB |": "| Default | 2% | 100 МБ |",
    "| High limits | 5% | 200 MB |": "| High limits | 5% | 200 МБ |",
    "##### For all data source processes": "##### Для всех процессов источников данных",
    "| Performance profile | CPU (Soft limit) | RAM (Soft limit) | CPU (Hard limit) | RAM (Hard limit) |": "| Профиль производительности | CPU (мягкий предел) | RAM (мягкий предел) | CPU (жёсткий предел) | RAM (жёсткий предел) |",
    "| Default | None | None | 5% | 15% |": "| Default | None | None | 5% | 15% |",
    "| High limits | None | None | 15% | 25% |": "| High limits | None | None | 15% | 25% |",
    "#### ActiveGate": "#### ActiveGate",
    "##### Per configuration": "##### На конфигурацию",
    "| Default | 5% | 500 MB |": "| Default | 5% | 500 МБ |",
    "| High limits | 15% | 700 MB |": "| High limits | 15% | 700 МБ |",
    '| [Dedicated](/managed/ingest-from/extensions/advanced-configuration/dedicated-performance-profile "Configure the dedicated performance profile mode to optimize the performance of your ActiveGate host.") | 30% | 1500 MB |': '| [Dedicated](/managed/ingest-from/extensions/advanced-configuration/dedicated-performance-profile "Настройте режим выделенного профиля производительности для оптимизации производительности хоста ActiveGate.") | 30% | 1500 МБ |',
    "| Default | 10% | 20% | 20% | 30% |": "| Default | 10% | 20% | 20% | 30% |",
    "| High limits | 45% | 30% | 60% | 40% |": "| High limits | 45% | 30% | 60% | 40% |",
    '| [Dedicated](/managed/ingest-from/extensions/advanced-configuration/dedicated-performance-profile "Configure the dedicated performance profile mode to optimize the performance of your ActiveGate host.") | 70% | 50% | 85% | 70% |': '| [Dedicated](/managed/ingest-from/extensions/advanced-configuration/dedicated-performance-profile "Настройте режим выделенного профиля производительности для оптимизации производительности хоста ActiveGate.") | 70% | 50% | 85% | 70% |',
    "### Generic types and relationship": "### Универсальные типы и связи",
    "Managing multiple extensions in Dynatrace can lead to encountering limits related to generic types and relationship settings. To prevent these potential issues, see the table below.": "Управление несколькими расширениями в Dynatrace может приводить к ограничениям, связанным с настройками универсальных типов и связей. Для предотвращения возможных проблем см. таблицу ниже.",
    "| Value count limits | Default value | Soft limit | Hard limit |": "| Ограничения количества значений | Значение по умолчанию | Мягкий предел | Жёсткий предел |",
    "| `builtin:monitoredentities.generic.relation` | 100 | 500 | 500 |": "| `builtin:monitoredentities.generic.relation` | 100 | 500 | 500 |",
    "| `builtin:monitoredentities.generic.type` | 100 | None | 500 |": "| `builtin:monitoredentities.generic.type` | 100 | None | 500 |",
}

PASS = {
    "title: Extensions limits",
}

if __name__ == "__main__":
    build_one(REL, "extension-limits.md", TRANS, PASS)
    qa_one(REL, "extension-limits.md")
