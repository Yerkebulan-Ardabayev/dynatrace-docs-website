# -*- coding: utf-8 -*-
"""L4-IF.62 builder: setup-on-k8s/guides/deployment-and-configuration/
resource-management batch (3 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM), no trailing newline.

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for identifier headings / EN component headings / bare strings. Any prose line
missing from both raises SystemExit -> catches leftover-EN before writing.

Note: EN sources contain Windows-1252 mojibake decoded as UTF-8:
  'â\x80\x93' = en-dash '–', 'â\x80\x94' = em-dash '—',
  'â\x80\x91' = non-breaking hyphen '‑', 'â\x80\x99' = apostrophe '’',
  'ï»¿' = BOM/zero-width.
MOJI_MAP rewrites these to clean Unicode in BOTH the EN line and TRANS keys, so
keys are authored clean and the RU output stays clean (translations carry no
em-dash regardless).
"""

import os
import re

# Map mojibake byte-runs (as decoded chars) to clean Unicode for KEY matching.
MOJI_MAP = [
    ("â", "–"),  # –  en dash
    ("â", "—"),  # —  em dash
    ("â", "‑"),  # ‑  non-breaking hyphen
    ("â", "’"),  # ’  right single quote
    ("﻿", ""),  # BOM / zero-width
    ("ï»¿", ""),  # ï»¿ mojibake BOM
]


def demoji(s):
    for bad, good in MOJI_MAP:
        s = s.replace(bad, good)
    return s


BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management"

# all three files live directly in resource-management/
REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "ag-resource-limits.md": {
        "title: Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case": "title: Руководство по подбору размеров для Dynatrace ActiveGate в сценарии мониторинга Kubernetes",
        "# Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case": "# Руководство по подбору размеров для Dynatrace ActiveGate в сценарии мониторинга Kubernetes",
        "* Reference": "* Справочник",
        "* 5-min read": "* Чтение: 5 мин",
        "* Updated on Feb 18, 2026": "* Обновлено 18 февраля 2026 г.",
        "Setting appropriate resource requests (and limits, when needed) keeps Dynatrace ActiveGate instances stable and predictable. This guide details sizing methods based on scale and workload.": "Задание подходящих запросов ресурсов (и лимитов при необходимости) поддерживает экземпляры Dynatrace ActiveGate стабильными и предсказуемыми. В этом руководстве подробно описаны методы подбора размеров в зависимости от масштаба и нагрузки.",
        "A stable, healthy ActiveGate ensures continuous gap‑free monitoring data.": "Стабильный, исправный ActiveGate обеспечивает непрерывные данные мониторинга без пропусков.",
        "## Understanding the sizing drivers": "## Что влияет на размер",
        "Actual required resources increase with:": "Фактически требуемые ресурсы растут с увеличением следующих факторов:",
        "* **Number of pods**–The primary sizing driver is the number of monitored pods. The resource consumption (CPU and memory) for Dynatrace ActiveGate components scales with the number of pods primarily due to increased data processing and storage needs. As the number of monitored pods grows, the ActiveGate handles more entity data, events, and metrics, resulting in higher CPU load for ingestion and processing, as well as increased memory for caching pod-related information. This is the primary sizing driver, with consumption scaling proportionally to pod count.": "* **Число подов**. Основной фактор подбора размера, это число отслеживаемых подов. Потребление ресурсов (CPU и память) компонентами Dynatrace ActiveGate масштабируется с числом подов в первую очередь из-за возросших потребностей в обработке и хранении данных. По мере роста числа отслеживаемых подов ActiveGate обрабатывает больше данных о сущностях, событий и метрик, что приводит к более высокой нагрузке на CPU при приёме и обработке, а также к увеличению объёма памяти для кэширования информации, связанной с подами. Это основной фактор подбора размера, и потребление масштабируется пропорционально числу подов.",
        "* **Prometheus metrics volume**–The number of Prometheus annotated pods directly correlates with increased resource requirements for Dynatrace ActiveGate, primarily through higher CPU consumption. As the count of annotated pods rises, the volume of scraped metrics grows, demanding more CPU cycles for collection, aggregation, and forwarding tasks. Memory impact is secondary, as metrics are forwarded to the Dynatrace tenant without long-term storage on the ActiveGate, though it scales proportionally with peak ingest rates.": "* **Объём метрик Prometheus**. Число подов с аннотациями Prometheus напрямую коррелирует с возросшими требованиями к ресурсам Dynatrace ActiveGate, в первую очередь через более высокое потребление CPU. По мере роста числа подов с аннотациями растёт объём собираемых метрик, что требует больше циклов CPU для задач сбора, агрегации и пересылки. Влияние на память вторично, так как метрики пересылаются в тенант Dynatrace без долговременного хранения на ActiveGate, хотя оно масштабируется пропорционально пиковым скоростям приёма.",
        "* **Number of nodes**–The resource consumption (CPU and memory) for Dynatrace ActiveGate components scales with the number of nodes primarily due to increased monitoring overhead and load from node-level system pods. As the node count grows, the ActiveGate must handle more system-level data collection, entity processing, and event ingestion, leading to higher computational demands. This is a secondary driver compared to the number of pods, but it contributes proportionally to overall resource needs, especially in larger clusters where node-level monitoring adds cumulative load.": "* **Число узлов**. Потребление ресурсов (CPU и память) компонентами Dynatrace ActiveGate масштабируется с числом узлов в первую очередь из-за возросших накладных расходов мониторинга и нагрузки от системных подов уровня узла. По мере роста числа узлов ActiveGate должен обрабатывать больше сбора данных системного уровня, обработки сущностей и приёма событий, что ведёт к более высоким вычислительным требованиям. Это вторичный фактор по сравнению с числом подов, но он пропорционально вносит вклад в общие потребности в ресурсах, особенно в более крупных кластерах, где мониторинг уровня узла добавляет совокупную нагрузку.",
        "* **Number of clusters monitored**–A single ActiveGate can monitor multiple clusters, however, this deployment pattern is **not recommended**. Monitoring multiple clusters with a single ActiveGate increases both CPU and memory requirements proportionally for each additional cluster, as the ActiveGate must handle more data processing, entity management, and event ingestion across clusters. This can lead to resource contention, higher risk of throttling or OOM restarts, and potential gaps in monitoring data.": "* **Число отслеживаемых кластеров**. Один ActiveGate может отслеживать несколько кластеров, однако такая схема развёртывания **не рекомендуется**. Мониторинг нескольких кластеров одним ActiveGate пропорционально увеличивает требования как к CPU, так и к памяти на каждый дополнительный кластер, поскольку ActiveGate должен обрабатывать больше данных, управления сущностями и приёма событий по всем кластерам. Это может привести к конкуренции за ресурсы, повышенному риску троттлинга или перезапусков по нехватке памяти (OOM) и потенциальным пропускам в данных мониторинга.",
        "**We recommend a setup where one containerized ActiveGate is monitoring one Kubernetes cluster.**": "**Мы рекомендуем схему, при которой один контейнеризованный ActiveGate отслеживает один кластер Kubernetes.**",
        "This ensures optimal performance and reliability. This approach simplifies troubleshooting, avoids resource contention, and ensures predictable scaling as each ActiveGate handles only one cluster’s workload.": "Это обеспечивает оптимальную производительность и надёжность. Такой подход упрощает диагностику, исключает конкуренцию за ресурсы и обеспечивает предсказуемое масштабирование, поскольку каждый ActiveGate обслуживает нагрузку только одного кластера.",
        "## Signs of an unhealthy ActiveGate": "## Признаки неисправного ActiveGate",
        "These symptoms indicate exhausted resources and potential data loss.": "Эти симптомы указывают на исчерпанные ресурсы и возможную потерю данных.",
        "### Gaps in monitoring data": "### Пропуски в данных мониторинга",
        "ActiveGate collects different types of data independently (for example, Prometheus metrics, Kubernetes events, entities). If one collection task takes longer than 1 minute, only that data type experiences a gap for that window. Other collection tasks continue operating normally.": "ActiveGate собирает разные типы данных независимо (например, метрики Prometheus, события Kubernetes, сущности). Если одна задача сбора занимает больше 1 минуты, пропуск в этом окне возникает только для соответствующего типа данных. Остальные задачи сбора продолжают работать нормально.",
        "* Metrics will have missing data point for the given minute.": "* У метрик будет отсутствовать точка данных за данную минуту.",
        "* Events for the given collection timeframes are not available at all.": "* События за данные интервалы сбора будут полностью недоступны.",
        "* Entities may not reflect the latest updates or may be missing at all if short-living.": "* Сущности могут не отражать последние обновления или вовсе отсутствовать, если они короткоживущие.",
        "### Heavy CPU throttling": "### Сильный троттлинг CPU",
        "Sustained high throttling means insufficient CPU. Heavy throttling can cause gaps. Minor throttling is usually harmless.": "Устойчивый высокий троттлинг означает нехватку CPU. Сильный троттлинг может вызывать пропуски. Незначительный троттлинг обычно безвреден.",
        "If the throttling affects the pod serving the monitoring ActiveGate this can cause data gaps.": "Если троттлинг затрагивает под, обслуживающий ActiveGate мониторинга, это может вызвать пропуски в данных.",
        "### Out‑of‑memory restarts": "### Перезапуски по нехватке памяти (out-of-memory)",
        "If the ActiveGate is OOM-killed, data becomes unavailable until it restarts. After a restart, repeated OOM kills are likely to occur.": "Если ActiveGate завершается по OOM, данные становятся недоступны до его перезапуска. После перезапуска вероятны повторные завершения по OOM.",
        "## Monitoring and validation": "## Мониторинг и проверка",
        "The following indicators can be tracked to understand if the ActiveGate is in a healthy operational state.": "Следующие индикаторы можно отслеживать, чтобы понять, находится ли ActiveGate в исправном рабочем состоянии.",
        "* **CPU usage vs requests**–If CPU utilization consistently exceeds 85% increase the CPU request.": "* **Использование CPU относительно запросов**. Если загрузка CPU стабильно превышает 85%, увеличьте запрос CPU.",
        "* **CPU throttling** (container\\_cpu\\_cfs\\_throttled\\_periods\\_total / periods)–If throttling exceeds 10% consistently, increase the CPU request.": "* **Троттлинг CPU** (container\\_cpu\\_cfs\\_throttled\\_periods\\_total / periods). Если троттлинг стабильно превышает 10%, увеличьте запрос CPU.",
        "* **Memory working set vs requests**–If usage consistently exceeds 80%, increase the memory requests.": "* **Рабочий набор памяти относительно запросов**. Если использование стабильно превышает 80%, увеличьте запросы памяти.",
        "* **ActiveGate restart count**–After an OOM-based restart, promptly raise the configured memory to prevent recurrence.": "* **Число перезапусков ActiveGate**. После перезапуска из-за OOM незамедлительно повысьте настроенный объём памяти, чтобы предотвратить повторение.",
        "* **Processing duration / cycle time** –If the execution time of pipelines consistently exceeds 50 - 60 seconds, increase the CPU request. The pipeline execution time also depends on the amount of ingested data and other factors.": "* **Длительность обработки / время цикла**. Если время выполнения конвейеров стабильно превышает 50–60 секунд, увеличьте запрос CPU. Время выполнения конвейера также зависит от объёма принимаемых данных и других факторов.",
        "* **Garbage collection times**–Increasing garbage collection times are a clear indicator for an under-provisioned ActiveGate.": "* **Время сборки мусора**. Растущее время сборки мусора является явным индикатором недостаточно обеспеченного ресурсами ActiveGate.",
        "Metrics reference": "Справочник метрик",
        "The indicators for unhealthy ActiveGates are as following:": "Индикаторы неисправного ActiveGate следующие:",
        "| Indicator | Platform metrics for validation | Classic metrics for validation | Detail level |": "| Индикатор | Метрики Platform для проверки | Классические метрики для проверки | Уровень детализации |",
        "| CPU usage | `dt.kubernetes.container.cpu_usage` | ``` builtin:kubernetes.node.cpu_usage``builtin:kubernetes.workload.cpu_usage ``` | ActiveGate pod |": "| Использование CPU | `dt.kubernetes.container.cpu_usage` | ``` builtin:kubernetes.node.cpu_usage``builtin:kubernetes.workload.cpu_usage ``` | Под ActiveGate |",
        "| CPU requests | `dt.kubernetes.resourcequota.requests_cpu` | ``` builtin:kubernetes.node.requests_cpu``builtin:kubernetes.workload.requests_cpu ``` | ActiveGate pod |": "| Запросы CPU | `dt.kubernetes.resourcequota.requests_cpu` | ``` builtin:kubernetes.node.requests_cpu``builtin:kubernetes.workload.requests_cpu ``` | Под ActiveGate |",
        "| CPU throttling | `dt.kubernetes.container.cpu_throttled` | ``` builtin:kubernetes.workload.cpu_throttled``builtin:kubernetes.node.cpu_throttled ``` | ActiveGate pod |": "| Троттлинг CPU | `dt.kubernetes.container.cpu_throttled` | ``` builtin:kubernetes.workload.cpu_throttled``builtin:kubernetes.node.cpu_throttled ``` | Под ActiveGate |",
        "| Memory working set | `dt.kubernetes.container.memory_working_set` | ``` builtin:kubernetes.node.memory_working_set``builtin:kubernetes.workload.memory_working_set ``` | ActiveGate pod |": "| Рабочий набор памяти | `dt.kubernetes.container.memory_working_set` | ``` builtin:kubernetes.node.memory_working_set``builtin:kubernetes.workload.memory_working_set ``` | Под ActiveGate |",
        "| Memory requests | `dt.kubernetes.resourcequota.requests_memory` | ``` builtin:kubernetes.node.requests_memory``builtin:kubernetes.workload.requests_memory ``` | ActiveGate pod |": "| Запросы памяти | `dt.kubernetes.resourcequota.requests_memory` | ``` builtin:kubernetes.node.requests_memory``builtin:kubernetes.workload.requests_memory ``` | Под ActiveGate |",
        "| Restart count | `dt.kubernetes.container.restarts` | `builtin:kubernetes.container.restarts` | ActiveGate pod |": "| Число перезапусков | `dt.kubernetes.container.restarts` | `builtin:kubernetes.container.restarts` | Под ActiveGate |",
        "| OOM kills | `dt.kubernetes.container.oom_kills` | `builtin:kubernetes.container.oom_kills` | ActiveGate pod |": "| Завершения по OOM | `dt.kubernetes.container.oom_kills` | `builtin:kubernetes.container.oom_kills` | Под ActiveGate |",
        "| Processing duration | `dt.sfm.active_gate.kubernetes.pipeline_duration` | `dsfm:active_gate.kubernetes.pipeline_duration` | ActiveGate ID |": "| Длительность обработки | `dt.sfm.active_gate.kubernetes.pipeline_duration` | `dsfm:active_gate.kubernetes.pipeline_duration` | ID ActiveGate |",
        "| Garbage collection times | `dt.sfm.active_gate.jvm.gc.major_collection_time` | `dsfm:active_gate.jvm.gc.major_collection_time` | ActiveGate ID |": "| Время сборки мусора | `dt.sfm.active_gate.jvm.gc.major_collection_time` | `dsfm:active_gate.jvm.gc.major_collection_time` | ID ActiveGate |",
        "### Increasing resources": "### Увеличение ресурсов",
        "Start with the recommended values below.": "Начните с рекомендованных значений ниже.",
        "1. Verify ActiveGate health using the monitoring indicators.": "1. Проверьте исправность ActiveGate с помощью индикаторов мониторинга.",
        "2. Adjust resources as needed:": "2. При необходимости скорректируйте ресурсы:",
        "* Increase memory in 2Gi increments.": "* Увеличивайте память шагами по 2Gi.",
        "* Increase CPU in 500m increments.": "* Увеличивайте CPU шагами по 500m.",
        "3. Adjust request first and in a later step adjust the limits.": "3. Сначала скорректируйте запрос, а на следующем шаге скорректируйте лимиты.",
        "* Regarding CPU: Use limits only if required by policy.": "* Относительно CPU: используйте лимиты только если это требуется политикой.",
        "## Using a dedicated ActiveGate for Kubernetes platform monitoring": "## Использование выделенного ActiveGate для мониторинга платформы Kubernetes",
        "Splitting ActiveGate responsibilities into two groups is recommended: One group handling everything related to Kubernetes platform monitoring, including KSPM, and the other managing Agent traffic routing, telemetry ingest, and extensions. This separation provides several advantages:": "Рекомендуется разделить обязанности ActiveGate на две группы: одна группа обрабатывает всё, что связано с мониторингом платформы Kubernetes, включая KSPM, а другая управляет маршрутизацией трафика Agent, приёмом телеметрии и расширениями. Такое разделение даёт несколько преимуществ:",
        "* **Isolation**–Resource contention in one module doesn't affect the other. A spike in OneAgent traffic won't slow down Kubernetes metrics collection, and vice versa.": "* **Изоляция**. Конкуренция за ресурсы в одном модуле не влияет на другой. Всплеск трафика OneAgent не замедлит сбор метрик Kubernetes, и наоборот.",
        "* **Independent scaling**–Traffic forwarding and platform monitoring have fundamentally different scaling characteristics:": "* **Независимое масштабирование**. Пересылка трафика и мониторинг платформы имеют принципиально разные характеристики масштабирования:",
        "+ **Kubernetes platform monitoring** can only scale vertically — when cluster size grows, you increase CPU and memory resources for the corresponding ActiveGate.": "+ **Мониторинг платформы Kubernetes** может масштабироваться только вертикально: при росте размера кластера вы увеличиваете ресурсы CPU и памяти для соответствующего ActiveGate.",
        "+ **OneAgent traffic routing** can be horizontally scaled — when OneAgent traffic increases, additional routing ActiveGate replicas help distribute and share the load.": "+ **Маршрутизация трафика OneAgent** может масштабироваться горизонтально: при росте трафика OneAgent дополнительные реплики маршрутизирующего ActiveGate помогают распределять и разделять нагрузку.",
        "Separate ActiveGates let you scale each dimension independently without over‑provisioning resources. For example, you can add 3 more routing replicas to handle increased application traffic without unnecessarily increasing resources for platform monitoring.": "Отдельные ActiveGate позволяют масштабировать каждое измерение независимо без избыточного выделения ресурсов. Например, вы можете добавить ещё 3 маршрутизирующие реплики для обработки возросшего трафика приложений, не увеличивая без необходимости ресурсы для мониторинга платформы.",
        "* **Easier troubleshooting** — When issues occur, you can immediately identify whether they originate from platform monitoring or OneAgent traffic, reducing diagnosis time.": "* **Упрощённая диагностика**. При возникновении проблем вы можете сразу определить, исходят ли они от мониторинга платформы или трафика OneAgent, что сокращает время диагностики.",
        "## Sizing ActiveGate": "## Подбор размера ActiveGate",
        "Scenarios are established based on the number of pods that are monitored by a single ActiveGate. The necessary resources can be taken from the following tables.": "Сценарии определяются на основе числа подов, отслеживаемых одним ActiveGate. Необходимые ресурсы можно взять из следующих таблиц.",
        "* **Scenario S**: <1000 pods": "* **Сценарий S**: <1000 подов",
        "* **Scenario M**: 1000–5000 pods": "* **Сценарий M**: 1000–5000 подов",
        "* **Scenario L**: 5000–20000 pods": "* **Сценарий L**: 5000–20000 подов",
        "This guide does not cover environments with more than 20,000 pods. Due to the many variables involved, providing precise recommendations for such large-scale setups isn’t feasible. As a starting point, you can use the guidance for the L scenario and gradually increase resources until stable gap-free monitoring is established.": "Это руководство не охватывает окружения с более чем 20 000 подов. Из-за множества задействованных переменных дать точные рекомендации для таких крупномасштабных конфигураций невозможно. В качестве отправной точки вы можете использовать рекомендации для сценария L и постепенно увеличивать ресурсы, пока не будет налажен стабильный мониторинг без пропусков.",
        "For tailored advice, we recommend reaching out to Dynatrace Support to ensure the best configuration for your environment.": "За индивидуальными рекомендациями советуем обратиться в Dynatrace Support, чтобы обеспечить наилучшую конфигурацию для вашего окружения.",
        "### Secondary factors": "### Вторичные факторы",
        "#### Node count": "#### Число узлов",
        "As the number of nodes in your Kubernetes cluster increases, the ActiveGate needs more CPU and memory resources to handle the extra monitoring workload. This includes processing data from node-level system components and events, which adds up proportionally.": "По мере роста числа узлов в вашем кластере Kubernetes ActiveGate требуется больше ресурсов CPU и памяти для обработки дополнительной нагрузки мониторинга. Это включает обработку данных от системных компонентов уровня узла и событий, что суммируется пропорционально.",
        "We group node counts into these categories for sizing guidance:": "Для рекомендаций по размеру мы группируем число узлов на следующие категории:",
        "* Up to 25 nodes": "* До 25 узлов",
        "* Up to 100 nodes": "* До 100 узлов",
        "* Up to 500 nodes": "* До 500 узлов",
        "If your cluster has more than 100 nodes, you'll need to adjust the resource allocations upward to account for the additional demands, ensuring stable and gap-free monitoring. For clusters beyond 500 nodes, consult Dynatrace Support for tailored recommendations.": "Если в вашем кластере больше 100 узлов, вам потребуется скорректировать выделение ресурсов в сторону увеличения, чтобы учесть дополнительные потребности и обеспечить стабильный мониторинг без пропусков. Для кластеров свыше 500 узлов обратитесь в Dynatrace Support за индивидуальными рекомендациями.",
        "#### Amount of Prometheus metrics scraped": "#### Объём собираемых метрик Prometheus",
        "Dynatrace supports up to 1000 pod exporters, with each exporter able to provide up to 1000 metrics. If your environment approaches these limits, you'll need to increase the resources allocated to the ActiveGate to ensure reliable performance.": "Dynatrace поддерживает до 1000 экспортеров подов, каждый из которых может предоставлять до 1000 метрик. Если ваше окружение приближается к этим пределам, вам потребуется увеличить ресурсы, выделенные ActiveGate, чтобы обеспечить надёжную производительность.",
        "### ActiveGate for Kubernetes platform monitoring": "### ActiveGate для мониторинга платформы Kubernetes",
        "All the following use cases have actually the same requirements on the ActiveGate taking over the Kubernetes platform monitoring part.": "Все следующие сценарии использования фактически предъявляют одинаковые требования к ActiveGate, берущему на себя часть мониторинга платформы Kubernetes.",
        "* Kubernetes platform monitoring only": "* Только мониторинг платформы Kubernetes",
        "* Kubernetes platform monitoring + Application observability": "* Мониторинг платформы Kubernetes + наблюдаемость приложений",
        "* Kubernetes platform monitoring + Full-stack observability": "* Мониторинг платформы Kubernetes + полностековая наблюдаемость",
        "| Pod count | CPU resource | Memory resource |": "| Число подов | Ресурс CPU | Ресурс памяти |",
        "| < 1000 ( Small ) | requests: 200m(limits: 1000m) | requests: 6Gilimits: 6Gi |": "| < 1000 ( Small ) | requests: 200m(limits: 1000m) | requests: 6Gilimits: 6Gi |",
        "| < 5000 ( Medium ) | requests: 1000m(limits: 2000m) | requests: 10Gi limits: 10Gi |": "| < 5000 ( Medium ) | requests: 1000m(limits: 2000m) | requests: 10Gi limits: 10Gi |",
        "| < 20000 ( Large ) | requests: 2000m(limits: 4000m) | requests: 12Gi limits: 12Gi |": "| < 20000 ( Large ) | requests: 2000m(limits: 4000m) | requests: 12Gi limits: 12Gi |",
        "We recommend running ActiveGates without CPU limits.": "Мы рекомендуем запускать ActiveGate без лимитов CPU.",
        "### ActiveGate for OneAgent traffic routing and proxying": "### ActiveGate для маршрутизации и проксирования трафика OneAgent",
        "The second ActiveGate does not actively participate in Kubernetes platform monitoring but is instead used as a router/proxy on behalf of data streams originating from the OneAgent.": "Второй ActiveGate активно не участвует в мониторинге платформы Kubernetes, а вместо этого используется как маршрутизатор/прокси для потоков данных, исходящих от OneAgent.",
        "We recommend to use separate ActiveGates for traffic forwarding and platform monitoring. Traffic forwarding scales horizontally by adding replicas. Kubernetes monitoring itself does not scale horizontally; instead increase resources.": "Мы рекомендуем использовать отдельные ActiveGate для пересылки трафика и мониторинга платформы. Пересылка трафика масштабируется горизонтально путём добавления реплик. Сам мониторинг Kubernetes не масштабируется горизонтально, вместо этого увеличивайте ресурсы.",
        "This setup is required in the following use-cases:": "Такая настройка требуется в следующих сценариях использования:",
        "| Pod count | CPU resource | Memory resource | replicas |": "| Число подов | Ресурс CPU | Ресурс памяти | replicas |",
        "| < 1000 ( Small ) | requests: 250m(limits: 1000m) | requests: 2Gi limits: 2Gi | 3 |": "| < 1000 ( Small ) | requests: 250m(limits: 1000m) | requests: 2Gi limits: 2Gi | 3 |",
        "| < 5000 ( Medium ) | requests: 500m(limits: 2000m) | requests: 4Gi limits: 4Gi | 3 |": "| < 5000 ( Medium ) | requests: 500m(limits: 2000m) | requests: 4Gi limits: 4Gi | 3 |",
        "| < 20000 ( Large ) | requests: 1000m(limits: 4000m) | requests: 6Gi limits: 6Gi | 6 |": "| < 20000 ( Large ) | requests: 1000m(limits: 4000m) | requests: 6Gi limits: 6Gi | 6 |",
        "## Getting started": "## Начало работы",
        "The following examples apply the reasoning of splitting the ActiveGates into units with separate concerns. One ActiveGate is responsible for Kubernetes platform monitoring and Kubernetes security posture management, whereas the 2nd ActiveGate is then responsible for agent traffic routing, telemetry ingest and extensions.": "Следующие примеры применяют логику разделения ActiveGate на единицы с раздельными обязанностями. Один ActiveGate отвечает за мониторинг платформы Kubernetes и управление состоянием безопасности Kubernetes, тогда как 2-й ActiveGate отвечает за маршрутизацию трафика агента, приём телеметрии и расширения.",
        "Adjust requests (and limits if required) to fit your environment.": "Скорректируйте запросы (и лимиты при необходимости) под ваше окружение.",
        "The following manifests includes two DynaKube resources for configuring ActiveGates:": "Следующие манифесты включают два ресурса DynaKube для настройки ActiveGate:",
        "* **k8s-monitoring** — Configures an ActiveGate dedicated to Kubernetes platform monitoring.": "* **k8s-monitoring**: настраивает ActiveGate, выделенный для мониторинга платформы Kubernetes.",
        "* **agents** — Configures an ActiveGate that supports OneAgent, telemetry ingest, and additional features.": "* **agents**: настраивает ActiveGate, поддерживающий OneAgent, приём телеметрии и дополнительные функции.",
        "You can apply both manifests at once or apply only the DynaKube you need.": "Вы можете применить оба манифеста сразу или применить только нужный вам DynaKube.",
        "CPU limits are commented out. We recommend defining requests only so the ActiveGate can use additional CPU when available. If limits are required, set them equal to or higher than requests.": "Лимиты CPU закомментированы. Мы рекомендуем задавать только запросы, чтобы ActiveGate мог использовать дополнительный CPU при его доступности. Если лимиты требуются, задавайте их равными запросам или выше.",
        "This snippet includes configuration for Kubernetes Security Posture Management. It's a complementing, opt-in security feature next to Kubernetes platform monitoring.": "Этот фрагмент включает конфигурацию для Kubernetes Security Posture Management. Это дополняющая, подключаемая по выбору функция безопасности рядом с мониторингом платформы Kubernetes.",
        "This snippet also includes configurations for log monitoring, extensions and telemetry ingest. These sections are considered optional on a per-section basis.": "Этот фрагмент также включает конфигурации для мониторинга логов, расширений и приёма телеметрии. Эти разделы считаются необязательными в индивидуальном порядке.",
        "DynaKubes for both Kubernetes platform monitoring and OneAgent, telemetry ingest, and additional features": "DynaKube для мониторинга платформы Kubernetes, а также для OneAgent, приёма телеметрии и дополнительных функций",
    },
    "dto-resource-limits.md": {
        "title: Set resource limits for Dynatrace Operator components": "title: Задание лимитов ресурсов для компонентов Dynatrace Operator",
        "# Set resource limits for Dynatrace Operator components": "# Задание лимитов ресурсов для компонентов Dynatrace Operator",
        "* 2-min read": "* Чтение: 2 мин",
        "* Updated on Feb 27, 2026": "* Обновлено 27 февраля 2026 г.",
        "Properly configured resource limits ensure optimal performance and stability of Dynatrace Operator components while preventing resource contention in your Kubernetes cluster. This guide helps you understand how to set appropriate resource limits based on your environment size and usage patterns.": "Правильно настроенные лимиты ресурсов обеспечивают оптимальную производительность и стабильность компонентов Dynatrace Operator, предотвращая конкуренцию за ресурсы в вашем кластере Kubernetes. Это руководство помогает понять, как задавать подходящие лимиты ресурсов в зависимости от размера вашего окружения и характера использования.",
        "## Default resource limits baseline": "## Базовые лимиты ресурсов по умолчанию",
        "The provided default resource limits have been validated through performance testing. These defaults performed well in the following environment:": "Предоставленные лимиты ресурсов по умолчанию проверены нагрузочным тестированием. Эти значения по умолчанию хорошо показали себя в следующем окружении:",
        "* 25 nodes (e2-standard-32 nodetype on Google Kubernetes Engine)": "* 25 узлов (тип узла e2-standard-32 в Google Kubernetes Engine)",
        "* 20 DynaKubes": "* 20 DynaKube",
        "* 2,500 namespaces": "* 2500 пространств имён",
        "* 5,000 pods": "* 5000 подов",
        "## Resource consumption factors": "## Факторы потребления ресурсов",
        "The following five key indicators influence resource consumption across different Dynatrace Operator components:": "Следующие пять ключевых индикаторов влияют на потребление ресурсов различными компонентами Dynatrace Operator:",
        "| **Indicator** | **Dynatrace Operator** | **Webhook** | **CSI driver** |": "| **Индикатор** | **Dynatrace Operator** | **Webhook** | **CSI driver** |",
        "| Namespaces | Applicable | Applicable |  |": "| Пространства имён | Применимо | Применимо |  |",
        "| Nodes | Applicable |  |  |": "| Узлы | Применимо |  |  |",
        "| DynaKubes | Applicable |  | Applicable |": "| DynaKube | Применимо |  | Применимо |",
        "| Pods |  | Applicable | Applicable |": "| Поды |  | Применимо | Применимо |",
        "| Number of OneAgent versions |  |  | Applicable |": "| Число версий OneAgent |  |  | Применимо |",
        "### Understanding the impact indicators": "### Что означают индикаторы влияния",
        "* **Namespaces**: More namespaces increase the workload for the Operator and webhook as they need to monitor and manage resources across all namespaces.": "* **Пространства имён**: больше пространств имён увеличивают нагрузку на Operator и webhook, так как им нужно отслеживать ресурсы во всех пространствах имён и управлять ими.",
        "+ Impact:": "+ Влияние:",
        "- Increases CPU/memory usage of Operator": "- Увеличивает использование CPU/памяти Operator",
        "- Increases CPU usage of webhook": "- Увеличивает использование CPU webhook",
        "* **Nodes**: Additional nodes require more resources as the Operator keeps a list of all available nodes on the Kubernetes clusters and verifies that they match the available hosts on the Dynatrace server.": "* **Узлы**: дополнительные узлы требуют больше ресурсов, так как Operator хранит список всех доступных узлов в кластерах Kubernetes и проверяет их соответствие доступным хостам на сервере Dynatrace.",
        "* **DynaKubes**: Each DynaKube resource represents a separate Dynatrace deployment that needs individual management.": "* **DynaKube**: каждый ресурс DynaKube представляет отдельное развёртывание Dynatrace, которое требует индивидуального управления.",
        "- Increases CPU/memory usage of webhook": "- Увеличивает использование CPU/памяти webhook",
        "- Increases CPU/memory usage of CSI driver provisioner": "- Увеличивает использование CPU/памяти компонента provisioner CSI driver",
        "* **Pods**: The webhook processes admission requests for every pod, while the CSI driver handles volume mounting for pods using OneAgent.": "* **Поды**: webhook обрабатывает запросы admission для каждого пода, а CSI driver выполняет монтирование томов для подов, использующих OneAgent.",
        "- Increases CPU/memory usage of CSI driver server/liveness-probe/registrar": "- Увеличивает использование CPU/памяти компонентов server/liveness-probe/registrar CSI driver",
        "* **OneAgent versions**: The CSI driver needs to manage and provide access to different OneAgent versions, requiring additional storage and processing resources.": "* **Версии OneAgent**: CSI driver должен управлять разными версиями OneAgent и предоставлять к ним доступ, что требует дополнительных ресурсов хранения и обработки.",
        "### Minimize impacts of large number of Node": "### Минимизация влияния большого числа узлов",
        "By default, Dynatrace Operator monitors host availability in your cluster to detect expected removal of host OneAgent pods especially in scaling scenarios. This monitoring is not necessary in serverless environments.": "По умолчанию Dynatrace Operator отслеживает доступность хостов в вашем кластере, чтобы обнаруживать ожидаемое удаление подов хостового OneAgent, особенно в сценариях масштабирования. Этот мониторинг не нужен в бессерверных окружениях.",
        "#### When to disable host availability detection": "#### Когда отключать обнаружение доступности хостов",
        "This functionality is present in all versions of the Operator before 1.6.0 and it can't be turned off.": "Эта функциональность присутствует во всех версиях Operator до 1.6.0 и не может быть отключена.",
        "It can be turned off in 1.6.3 and 1.7.3 or in newer Operator versions.": "Её можно отключить в 1.6.3 и 1.7.3 или в более новых версиях Operator.",
        "applicationMonitoring": "applicationMonitoring",
        "You can reduce the Operator's resource consumption by disabling host availability detection if your DynaKubes:": "Вы можете снизить потребление ресурсов Operator, отключив обнаружение доступности хостов, если ваши DynaKube:",
        "* **only** use application-only monitoring modes and": "* используют **только** режимы мониторинга приложений и",
        "* do **not** use any of the host-based monitoring features.": "* **не** используют ни одну из функций мониторинга на основе хостов.",
        "#### How to disable host availability detection": "#### Как отключить обнаружение доступности хостов",
        "To disable host availability detection, set the following Helm value:": "Чтобы отключить обнаружение доступности хостов, задайте следующее значение Helm:",
        "This optimization can reduce CPU and memory usage of the Operator, especially in large clusters with many nodes.": "Эта оптимизация может снизить использование CPU и памяти Operator, особенно в больших кластерах с множеством узлов.",
        "**Cluster-wide setting**: `operator.hostAvailabilityDetection` affects all DynaKubes managed by the Operator. Only disable this if you are certain that **none** of your DynaKubes require host-based monitoring. Disabling it when host OneAgents are required can cause false-positive host missing warnings during node scaling or other node-related operations.": "**Настройка на уровне всего кластера**: `operator.hostAvailabilityDetection` влияет на все DynaKube, управляемые Operator. Отключайте это, только если вы уверены, что **ни один** из ваших DynaKube не требует мониторинга на основе хостов. Отключение при необходимости хостовых OneAgent может вызывать ложноположительные предупреждения об отсутствии хостов во время масштабирования узлов или других операций, связанных с узлами.",
        "## Customize resource limits": "## Настройка лимитов ресурсов",
        "While the default resource limits should be sufficient for most use cases, you can customize them based on your specific needs.": "Хотя лимитов ресурсов по умолчанию должно быть достаточно для большинства сценариев использования, вы можете настроить их под ваши конкретные потребности.",
        "Modify `values.yaml` to set resource limits for Dynatrace Operator, webhook, or CSI driver.": "Измените `values.yaml`, чтобы задать лимиты ресурсов для Dynatrace Operator, webhook или CSI driver.",
        "* **Dynatrace Operator**": "* **Dynatrace Operator**",
        "* **Webhook**": "* **Webhook**",
        "* **CSI driver**": "* **CSI driver**",
        "The CSI driver `provisioner` and `job` components do not have default resource limits specified. This allows them to use additional resources when available, improving performance.": "Для компонентов `provisioner` и `job` драйвера CSI driver не заданы лимиты ресурсов по умолчанию. Это позволяет им использовать дополнительные ресурсы при их доступности, повышая производительность.",
        'The `job` component is only used with [node-image-pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull").': 'Компонент `job` используется только с [node-image-pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка извлечения образа на узле").',
        "Note that if the limits are set too low, this can lead to increased pod startup times due to CPU throttling or, OOM kills in the CSI driver due to insufficient memory, which can prevent applications from starting.": "Обратите внимание, что если лимиты заданы слишком низкими, это может привести к увеличению времени запуска подов из-за троттлинга CPU или к завершениям по OOM в CSI driver из-за нехватки памяти, что может помешать запуску приложений.",
        "### Scaling resource limits for different environments": "### Масштабирование лимитов ресурсов для разных окружений",
        "The default resource requests and limits are designed for medium-scale environments. Use the following guidelines to adjust limits based on your environment size. These are starting recommendations—-always monitor actual resource usage in your environment and adjust accordingly.": "Запросы и лимиты ресурсов по умолчанию рассчитаны на окружения среднего масштаба. Используйте следующие рекомендации, чтобы скорректировать лимиты в зависимости от размера вашего окружения. Это начальные рекомендации: всегда отслеживайте фактическое использование ресурсов в вашем окружении и корректируйте соответственно.",
        "**Pod Quality of Service Classes**: Some components have their limits and requests set to the same value to ensure a [Guaranteed Pod Quality of Service](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed). When scaling the limits of such components, always scale the requests proportionally as well.": "**Классы Quality of Service подов**: у некоторых компонентов лимиты и запросы заданы равными, чтобы обеспечить [гарантированный класс Quality of Service пода](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed). При масштабировании лимитов таких компонентов всегда пропорционально масштабируйте и запросы.",
        "**Proportional fairness:** Having low CPU requests on a container can cause throttling due to the CPU management policy of the node. The requests serve as a **minimum guarantee**. On a heavily utilized node, therefore, containers with smaller requests will be throttled more compared to containers with larger requests, regardless of their limit. When scaling the limits, always consider scaling the requests as well.": "**Пропорциональная справедливость:** низкие запросы CPU у контейнера могут вызывать троттлинг из-за политики управления CPU на узле. Запросы служат **минимальной гарантией**. Поэтому на сильно загруженном узле контейнеры с меньшими запросами будут троттлиться сильнее по сравнению с контейнерами с большими запросами, независимо от их лимита. При масштабировании лимитов всегда рассматривайте и масштабирование запросов.",
        "The CSI driver `job` resource requests and limits do not need to scale based on environment size. They are independent of node count, pod count, and DynaKube count. However, you can adjust the CPU request to control how quickly the job completes, which determines how soon the CSI driver is ready to mount volumes:": "Запросы и лимиты ресурсов компонента `job` драйвера CSI driver не нужно масштабировать в зависимости от размера окружения. Они не зависят от числа узлов, числа подов и числа DynaKube. Тем не менее вы можете скорректировать запрос CPU, чтобы управлять тем, насколько быстро завершается job, что определяет, как скоро CSI driver будет готов монтировать тома:",
        "| CPU request | Approximate completion time |": "| Запрос CPU | Примерное время завершения |",
        "| 100m | ~1 min |": "| 100m | ~1 мин |",
        "| 200m (default) | ~30 sec |": "| 200m (по умолчанию) | ~30 сек |",
        "| 300m | ~25 sec |": "| 300m | ~25 сек |",
        "This only affects the job's `Running` duration. It doesn't impact `ContainerCreation` or `PodScheduling` times.": "Это влияет только на длительность состояния `Running` для job. Это не влияет на время `ContainerCreation` или `PodScheduling`.",
        "Starting with Dynatrace Operator version 1.9.0, the webhook's `replicas` can be customized in Helm in addition to its resource limits. This allows you to scale the Webhook horizontally in larger environments, providing better performance and availability.": "Начиная с версии Dynatrace Operator 1.9.0, параметр `replicas` webhook можно настраивать в Helm в дополнение к его лимитам ресурсов. Это позволяет масштабировать Webhook горизонтально в более крупных окружениях, обеспечивая лучшую производительность и доступность.",
        "The resource recommendation below is for two webhook replicas. If you choose to use a different number of replicas, adjust the resource limits accordingly.": "Рекомендация по ресурсам ниже рассчитана на две реплики webhook. Если вы решите использовать другое число реплик, скорректируйте лимиты ресурсов соответственно.",
        "* Example: If you want to use 3 replicas instead of 2, you can reduce the CPU/Memory requests/limits by approximately 30% while maintaining overall performance but gain higher availability.": "* Пример: если вы хотите использовать 3 реплики вместо 2, вы можете снизить запросы/лимиты CPU/памяти примерно на 30%, сохранив общую производительность, но получив более высокую доступность.",
        "For details on configuring the webhook's `replicas` and related values, see [Configure high availability](#high-availability-helm).": "Подробнее о настройке параметра `replicas` webhook и связанных значений см. [Настройка высокой доступности](#high-availability-helm).",
        "#### Large environments (> 50 nodes, > 10,000 pods)": "#### Крупные окружения (> 50 узлов, > 10 000 подов)",
        "Increase the default requests/limits by 50–100%:": "Увеличьте запросы/лимиты по умолчанию на 50–100%:",
        "* **Dynatrace Operator**:": "* **Dynatrace Operator**:",
        "+ Request: CPU 100m, Memory 128Mi": "+ Запрос: CPU 100m, память 128Mi",
        "+ Limits: CPU 200m, Memory 256Mi": "+ Лимиты: CPU 200m, память 256Mi",
        "* **Webhook**:": "* **Webhook**:",
        "+ Requests: CPU 600m, Memory 256Mi": "+ Запросы: CPU 600m, память 256Mi",
        "+ Limits: CPU 600m, Memory 256Mi": "+ Лимиты: CPU 600m, память 256Mi",
        "* **CSI driver provisioner**:": "* **provisioner CSI driver**:",
        "+ Requests: CPU 600m, Memory 200Mi": "+ Запросы: CPU 600m, память 200Mi",
        "* **CSI driver server**:": "* **server CSI driver**:",
        "+ Requests: CPU 100m, Memory 200Mi": "+ Запросы: CPU 100m, память 200Mi",
        "+ Limits: CPU 100m, Memory 200Mi": "+ Лимиты: CPU 100m, память 200Mi",
        "* **CSI driver liveness-probe**:": "* **liveness-probe CSI driver**:",
        "+ Requests: CPU 30m, Memory 50Mi": "+ Запросы: CPU 30m, память 50Mi",
        "+ Limits: CPU 30m, Memory 50Mi": "+ Лимиты: CPU 30m, память 50Mi",
        "* **CSI driver registrar**:": "* **registrar CSI driver**:",
        "#### Enterprise environments (> 100 nodes, > 25,000 pods)": "#### Окружения корпоративного масштаба (> 100 узлов, > 25 000 подов)",
        "Increase the default requests/limits by 100–200%:": "Увеличьте запросы/лимиты по умолчанию на 100–200%:",
        "* **Dynatrace Operator**: CPU 400m, Memory 512Mi": "* **Dynatrace Operator**: CPU 400m, память 512Mi",
        "+ Request: CPU 200m, Memory 256Mi": "+ Запрос: CPU 200m, память 256Mi",
        "+ Limits: CPU 400m, Memory 512Mi": "+ Лимиты: CPU 400m, память 512Mi",
        "+ Requests: CPU 1000m, Memory 512Mi": "+ Запросы: CPU 1000m, память 512Mi",
        "+ Limits: CPU 1000m, Memory 512Mi": "+ Лимиты: CPU 1000m, память 512Mi",
        "+ Requests: CPU 900m, Memory 300Mi": "+ Запросы: CPU 900m, память 300Mi",
        "+ Requests: CPU 150m, Memory 300Mi": "+ Запросы: CPU 150m, память 300Mi",
        "+ Limits: CPU 150m, Memory 300Mi": "+ Лимиты: CPU 150m, память 300Mi",
        "+ Requests: CPU 50m, Memory 70Mi": "+ Запросы: CPU 50m, память 70Mi",
        "+ Limits: CPU 50m, Memory 70Mi": "+ Лимиты: CPU 50m, память 70Mi",
    },
    "probe-timeout.md": {
        "title: Fix probe timeouts due to OneAgent injection": "title: Устранение тайм-аутов проверок работоспособности из-за инъекции OneAgent",
        "# Fix probe timeouts due to OneAgent injection": "# Устранение тайм-аутов проверок работоспособности из-за инъекции OneAgent",
        "* 1-min read": "* Чтение: 1 мин",
        "* Published May 28, 2024": "* Опубликовано 28 мая 2024 г.",
        "This guide walks you through the process of fixing timeouts in readiness- or liveness-probes due to OneAgent injecting into the probe.": "Это руководство проведёт вас через процесс устранения тайм-аутов в readiness- или liveness-probe из-за внедрения OneAgent в проверку работоспособности.",
        "## Scenario": "## Сценарий",
        "In some scenarios, a readiness- or liveness-probe is configured using an exec statement. This configuration causes OneAgent to attempt injection when the probe executable starts. This injection process introduces a slight delay in startup time, which can result in the probe timing out.": "В некоторых сценариях readiness- или liveness-probe настроена с использованием инструкции exec. Из-за такой конфигурации OneAgent пытается выполнить внедрение при запуске исполняемого файла проверки работоспособности. Этот процесс внедрения вносит небольшую задержку времени запуска, что может приводить к тайм-ауту проверки работоспособности.",
        "Consider the following example of a readiness probe:": "Рассмотрим следующий пример readiness probe:",
        "In this example, Vault is the application we want to monitor, but we want to exclude the process used as the readiness-probe from being monitored.": "В этом примере Vault, это приложение, которое мы хотим отслеживать, но мы хотим исключить из мониторинга процесс, используемый в качестве readiness-probe.",
        "## Resolution": "## Решение",
        "To resolve this issue, you can configure an exception in the settings.": "Чтобы устранить эту проблему, вы можете настроить исключение в параметрах.",
        "1. Go to **Settings** > **Processes and containers** > **Custom process monitoring rules**.": "1. Перейдите в **Settings** > **Processes and containers** > **Custom process monitoring rules**.",
        "2. Select **Add custom rule**.": "2. Выберите **Add custom rule**.",
        "3. Add an exclusion to monitoring by supplying a part of the command line arguments used by the readiness probe. To resolve the timeout in our example, use the following settings:": "3. Добавьте исключение из мониторинга, указав часть аргументов командной строки, используемых проверкой readiness probe. Чтобы устранить тайм-аут в нашем примере, используйте следующие параметры:",
        "* **Mode**: `Do not monitor`": "* **Mode**: `Do not monitor`",
        "* **Condition target**: `Command line args`": "* **Condition target**: `Command line args`",
        "* **Condition operator**: `contains`": "* **Condition operator**: `contains`",
        "* **Condition value**: `vault status`": "* **Condition value**: `vault status`",
        "4. Save your changes (this might take up to 5 minutes).": "4. Сохраните изменения (это может занять до 5 минут).",
        "Once the settings are applied to the cluster, the timeouts should be resolved.": "После применения параметров к кластеру тайм-ауты должны быть устранены.",
    },
}

# Lines copied verbatim (identifier headings / EN component headings / bare).
PASS = {
    "ag-resource-limits.md": {
        "| --- | --- | --- | --- |",
        "| --- | --- | --- |",
    },
    "dto-resource-limits.md": {
        "| --- | --- | --- | --- |",
        "| --- | --- |",
    },
    "probe-timeout.md": set(),
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = REL.get(fname, SUB)
    en_path = os.path.join(BASE, "managed", sub, fname)
    ru_path = os.path.join(BASE, "managed-ru", sub, fname)
    en_lines = read_lf(en_path).split("\n")
    tmap = {demoji(k): v for k, v in TRANS[fname].items()}
    passset = {demoji(k) for k in PASS.get(fname, set())}
    out = []
    in_fence = False
    for ln in en_lines:
        stripped = demoji(ln.strip())
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence:
            out.append(ln)
            continue
        if stripped == "":
            out.append(ln)
            continue
        if stripped == "---":
            out.append(ln)
            continue
        if stripped.startswith("source:") or stripped.startswith("scraped:"):
            out.append(ln)
            continue
        if stripped in tmap:
            indent = ln[: len(ln) - len(ln.lstrip())]
            out.append(indent + tmap[stripped])
            continue
        if stripped in passset:
            out.append(ln)
            continue
        raise SystemExit(f"[{fname}] UNTRANSLATED: {ln!r}")

    assert len(out) == len(en_lines), f"{fname}: parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK  {fname}: {len(out)} lines -> {ru_path}")


if __name__ == "__main__":
    for fn in TRANS:
        build(fn)
