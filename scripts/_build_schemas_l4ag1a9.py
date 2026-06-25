# -*- coding: utf-8 -*-
"""L4-AG.1a.9 builder: 12 builtin-*.md schema-table files (3.76-4.43 KB) from
docs/managed/dynatrace-api/environment-api/settings/schemas/.

Anchor canon: L4-AG.1a.8 _build_schemas_l4ag1a8.py.

Highlights:
  - 3 файла с triple-mojibake apostrophe (U+00E2 U+0080 U+0099 = bytes c3 a2 c2 80 c2 99):
    monitoring-slo (`organizationâ€™s`), rum-web-enablement (`thereâ€™s`),
    service-detection-v2-for-oneagent (3× `opt-inâ€™s`). Ключи через chr()
    конкатенацию по L4-AG.1a.4 канону.
  - 2 файла с single-mojibake (U+00E2 = bytes c3 a2): declarativegrouping
    (4× `$contains(svc) â Matches if...` en-dash), url-path-pattern-matching-rules
    (6× `asâis`, `lowâvolatility`, `Catchâall`, `Nonâmatches`,
    `highâcardinality`). Ключи с прямым символом chr(0xE2).
  - Twin pair: custom-metrics ↔ user-action-custom-metrics — общие
    PARAM_LABEL/MetricValue/Filter nested; уникальные SCHEMA_DESC и dimensions-
    конкретные PARAM_DESC.
  - mojibake-BOM `ï»¿` съедается `_normalize` (канон L4-AG.1a.7). Ключи БЕЗ BOMJ.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-monitoring-slo.md",
    "builtin-rum-web-enablement.md",
    "builtin-service-detection-v2-for-oneagent.md",
    "builtin-custom-metrics.md",
    "builtin-synthetic-multiprotocol-config.md",
    "builtin-user-action-custom-metrics.md",
    "builtin-metric-metadata.md",
    "builtin-declarativegrouping.md",
    "builtin-rum-web-automatic-injection.md",
    "builtin-anomaly-detection-infrastructure-disks.md",
    "builtin-logmonitoring-log-agent-configuration.md",
    "builtin-url-path-pattern-matching-rules.md",
]

# Triple-mojibake apostrophe `'` (U+2019): 6 bytes (c3 a2 c2 80 c2 99), 3 chars (U+00E2 U+0080 U+0099)
TM = chr(0xE2) + chr(0x80) + chr(0x99)
# Triple-mojibake en-dash `–` (U+2013): bytes c3 a2 c2 80 c2 93 — declarativegrouping line 61
TM_ENDASH = chr(0xE2) + chr(0x80) + chr(0x93)
# Triple-mojibake non-breaking hyphen `‑` (U+2011): bytes c3 a2 c2 80 c2 91 — url-path-pattern line 46
TM_NBHYPHEN = chr(0xE2) + chr(0x80) + chr(0x91)
# Single-mojibake: 2 bytes (c3 a2), 1 char (U+00E2) — unused in this batch
SM = chr(0xE2)

DISPLAY_NAME = {
    "Service-level objective definitions": "Описания целей уровня обслуживания (SLO)",
    "Enablement and cost control": "Включение и контроль затрат",
    "Service Detection v2 for OneAgent": "Service Detection v2 для OneAgent",
    "User session custom metrics": "Пользовательские метрики на основе user-сессий",
    "Network Availability monitor config": "Конфигурация Network Availability-монитора",
    "User action custom metrics": "Пользовательские метрики на основе user-действий",
    "Metric metadata": "Метаданные метрики",
    "Declarative process grouping": "Декларативная группировка процессов",
    "Automatic injection": "Автоматическая инъекция",
    "Anomaly detection for infrastructure: Disk": "Обнаружение аномалий инфраструктуры: диски",
    "Advanced log settings": "Расширенные параметры логов",
    "URL path pattern matching": "Сопоставление шаблонов URL-путей",
}

SCHEMA_DESC = {
    # 1. monitoring-slo (triple-mojibake `organizationâ€™s`)
    "Define custom [Service-level objectives"
    + chr(0xEF)
    + chr(0xBB)
    + chr(0xBF):  # mojibake-BOM in original, stripped by _normalize so key WITHOUT it
    "",  # placeholder, real entry below (we cannot have BOMJ in key)
    "Define custom [Service-level objectives](https://dt-url.net/slos) (SLOs) to assist in fulfilling your organization"
    + TM
    + "s service-level agreements. Create up to 10000 custom SLOs for this Dynatrace environment.": "Задайте пользовательские [Service-level objectives](https://dt-url.net/slos) (SLO), чтобы помочь в выполнении соглашений об уровне обслуживания вашей организации. Создайте до 10000 пользовательских SLO для этого Dynatrace-окружения.",
    # 2. rum-web-enablement
    "Turn on Real User Monitoring and Session Replay. Configure cost and traffic control settings.": "Включите Real User Monitoring и Session Replay. Настройте параметры контроля затрат и трафика.",
    # 3. service-detection-v2-for-oneagent (3 paragraphs + Important)
    "Enabling SDv2 for OneAgent will use the same attribute-based rules as OpenTelemetry for detecting services, endpoints, and failures. Refer to the [SDv2 documentation](https://dt-url.net/5e0309z) for more information.": "Включение SDv2 для OneAgent задействует те же attribute-based правила, что и OpenTelemetry, для обнаружения сервисов, эндпоинтов и failure. Подробнее см. в [SDv2 documentation](https://dt-url.net/5e0309z).",
    "This is a **Public Preview** feature. You must complete the [access request form and agree to preview terms](https://dt-url.net/cb300tiz) before enabling.": "Это **Public Preview**-функция. До включения необходимо заполнить [access request form and agree to preview terms](https://dt-url.net/cb300tiz).",
    "**Important**": "**Важно**",
    "The services matching your conditions will get new metric keys, breaking existing API queries, dashboards, and service names. Custom, opaque, third party, database, and message queue services are detected differently in SDv2. Analysis views for service to database and message queue operations will be announced in upcoming releases.": "Сервисы, попадающие под ваши условия, получат новые ключи метрик, что сломает существующие API-запросы, дашборды и имена сервисов. Custom, opaque, third party, database и message queue-сервисы в SDv2 определяются иначе. Аналитические представления для операций service-to-database и message queue будут анонсированы в будущих релизах.",
    # 4. custom-metrics (3 paragraphs)
    "With user-session custom metrics (see [documentation](https://dt-url.net/3i03u3s)), you can extract business-level KPI metrics from user session data. Metrics can then be saved as timeseries and consumed (without interpolation) by your custom charts, alerting mechanisms or the Metrics REST API (`<your-dynatrace-url>//rest-api-doc/?urls.primaryName=Environment+API+v2#/Metrics`).": "С помощью пользовательских метрик user-сессий (см. [documentation](https://dt-url.net/3i03u3s)) можно извлекать business-level KPI-метрики из данных user-сессий. Метрики затем можно сохранять как timeseries и потреблять (без интерполяции) в пользовательских графиках, механизмах оповещений или Metrics REST API (`<your-dynatrace-url>//rest-api-doc/?urls.primaryName=Environment+API+v2#/Metrics`).",
    "To explore collected metrics, go to Data explorer (`<your-dynatrace-url>//ui/data-explorer`).": "Для изучения собранных метрик перейдите в Data explorer (`<your-dynatrace-url>//ui/data-explorer`).",
    "To create a custom event based on a custom metric, go to Custom events for alerting (`<your-dynatrace-url>//#settings/anomalydetection/metricevents`).": "Чтобы создать пользовательское событие на основе пользовательской метрики, перейдите в Custom events for alerting (`<your-dynatrace-url>//#settings/anomalydetection/metricevents`).",
    # 5. synthetic-multiprotocol-config
    "Network Availability monitor": "Network Availability-монитор",
    # 6. user-action-custom-metrics (3 paragraphs; first is unique due to "user action" wording)
    "With user action custom metrics (see [documentation](https://dt-url.net/3i03u3s)), you can extract business-level KPI metrics from user action data. Metrics can then be saved as timeseries and consumed (without interpolation) by your custom charts, alerting mechanisms or the Metrics REST API (`<your-dynatrace-url>//rest-api-doc/?urls.primaryName=Environment+API+v2#/Metrics`).": "С помощью пользовательских метрик user-действий (см. [documentation](https://dt-url.net/3i03u3s)) можно извлекать business-level KPI-метрики из данных user-действий. Метрики затем можно сохранять как timeseries и потреблять (без интерполяции) в пользовательских графиках, механизмах оповещений или Metrics REST API (`<your-dynatrace-url>//rest-api-doc/?urls.primaryName=Environment+API+v2#/Metrics`).",
    # 7. metric-metadata
    '[Custom metrics metadata](https://dt-url.net/k603stq "Custom metrics metadata") allows you to provide additional information for your metric.': '[Custom metrics metadata](https://dt-url.net/k603stq "Custom metrics metadata") позволяет указать дополнительные сведения о метрике.',
    # 8. declarativegrouping (4 paragraphs)
    "Dynatrace automatically monitors process groups that are of known technology types or that consume significant resources. With declarative process grouping, you can automatically monitor additional technologies.": "Dynatrace автоматически мониторит process group известных типов технологий или потребляющие значительные ресурсы. С декларативной группировкой процессов вы можете автоматически мониторить дополнительные технологии.",
    "To add a new process group, you must first define the technology type. The technology type can be a generic technology name or a custom name. Each technology type can be associated with multiple process groups.": "Чтобы добавить новую process group, сначала задайте тип технологии. Тип может быть общим именем технологии или пользовательским. С каждым типом технологии можно связать несколько process group.",
    "Next, give your process group a unique name and identifier. This name is used to identify the process group throughout your Dynatrace environment. Finally, add detection rules so that Dynatrace can automatically identify processes that belong in this group.": "Затем дайте process group уникальное имя и идентификатор. Это имя используется для идентификации process group во всём Dynatrace-окружении. Наконец, добавьте правила обнаружения, чтобы Dynatrace автоматически распознавал процессы, входящие в эту группу.",
    "For complete details, see [Declarative process grouping](https://dt-url.net/j142w57)": "Полные подробности см. в [Declarative process grouping](https://dt-url.net/j142w57)",
    # 9. rum-web-automatic-injection
    "Dynatrace OneAgent automatically injects the RUM JavaScript into the HTML head of monitored application pages. Use this page to control and adjust the injection.": "Dynatrace OneAgent автоматически инжектит RUM-JavaScript в HTML-head страниц мониторимых приложений. На этой странице можно управлять инъекцией и настраивать её.",
    # 10. anomaly-detection-infrastructure-disks
    "Dynatrace automatically detects infrastructure-related performance anomalies such as low disk-space conditions. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for disks.": "Dynatrace автоматически обнаруживает связанные с инфраструктурой аномалии производительности, например нехватку места на диске. Используйте эти параметры для настройки чувствительности обнаружения, задания порогов оповещений или отключения оповещений для дисков.",
    # 11. logmonitoring-log-agent-configuration
    "Configure OneAgent options for Dynatrace Log Monitoring": "Настройте параметры OneAgent для Dynatrace Log Monitoring",
    # 12. url-path-pattern-matching-rules
    "Define rules to match URL patterns out of URL paths. See [Service Detection v2 documentation](https://dt-url.net/sy035si)": "Задайте правила для извлечения URL-шаблонов из URL-путей. См. [Service Detection v2 documentation](https://dt-url.net/sy035si)",
}

# Drop the placeholder entry from earlier definition mistake (Python dict literal keeps last value;
# здесь мы просто удаляем ключ-«заглушку», который остался для документации намерения)
SCHEMA_DESC.pop(
    "Define custom [Service-level objectives" + chr(0xEF) + chr(0xBB) + chr(0xBF),
    None,
)


PARAM_LABEL = {
    # Shared
    "Enabled": "Включено",
    "Active": "Активно",
    "Name": "Имя",
    "Description": "Описание",
    "Value": "Значение",
    "Values": "Значения",
    "Operator": "Оператор",
    "Tags": "Теги",
    "Comment": "Комментарий",
    # 1. monitoring-slo
    "SLO name": "Имя SLO",
    "Metric name": "Имя метрики",
    "Define the metric expression that measures the success rate of this SLO": "Задайте выражение метрики, измеряющее success rate этого SLO",
    "Evaluation type": "Тип вычисления",
    "Entity selector": "Селектор сущностей",
    "Timeframe during which the SLO is to be evaluated": "Временной диапазон, в котором вычисляется SLO",
    "Target percentage": "Целевой процент",
    "Warning percentage": "Процент предупреждения",
    "Burn rate visualization enabled": "Включена визуализация burn rate",
    "Fast-burn threshold": "Порог fast-burn",
    # 2. rum-web-enablement
    "Real User Monitoring": "Real User Monitoring",
    "Session Replay": "Session Replay",
    "User Interactions": "User Interactions",
    "Enable Real User Monitoring Classic": "Включить Real User Monitoring Classic",
    "Enable New Real User Monitoring Experience": "Включить новый опыт Real User Monitoring",
    "Cost and traffic control": "Контроль затрат и трафика",
    "Enable Session Replay Classic": "Включить Session Replay Classic",
    "Enable New Session Replay Experience": "Включить новый опыт Session Replay",
    "Enable User Interactions": "Включить User Interactions",
    # 3. service-detection-v2-for-oneagent
    "Enable Service detection v2 for Kubernetes workloads": "Включить Service Detection v2 для Kubernetes-workload",
    "Matching condition for Kubernetes workloads": "Условие сопоставления для Kubernetes-workload",
    "Enable Service detection v2 for FaaS": "Включить Service Detection v2 для FaaS",
    "Matching condition for FaaS": "Условие сопоставления для FaaS",
    "Matching condition for any workload": "Условие сопоставления для любого workload",
    # 4+6. custom-metrics + user-action-custom-metrics (twin)
    "Enable custom metric": "Включить пользовательскую метрику",
    "Metric key": "Ключ метрики",
    "Value type to be extracted": "Тип извлекаемого значения",
    "Add a dimension": "Добавить dimension",
    "Add a filter": "Добавить фильтр",
    "Field name": "Имя поля",
    # 5. synthetic-multiprotocol-config
    "Monitor enabled": "Монитор включён",
    "Monitor description": "Описание монитора",
    "Steps": "Шаги",
    "Monitor properties": "Свойства монитора",
    "Step name": "Имя шага",
    "Request type": "Тип запроса",
    "Target list": "Список целей",
    "Target filter": "Фильтр целей",
    "Configuration properties": "Свойства конфигурации",
    "Step-level constraints": "Ограничения уровня шага",
    "Request-level configuration": "Конфигурация уровня запроса",
    "Pre-execution script": "Скрипт перед выполнением",
    "Post-execution script": "Скрипт после выполнения",
    "Property key": "Ключ свойства",
    "Property value": "Значение свойства",
    "Constraint type": "Тип ограничения",
    "Properties": "Свойства",
    "Request constraints": "Ограничения запроса",
    "Pattern matcher": "Сопоставитель шаблона",
    # 7. metric-metadata
    "Display name": "Отображаемое имя",
    "Unit": "Единица",
    "Unit display format": "Формат отображения единицы",
    "Metric properties": "Свойства метрики",
    "Metric dimensions": "Dimensions метрики",
    "Source entity type": "Тип сущности-источника",
    "Minimum value": "Минимальное значение",
    "Maximum value": "Максимальное значение",
    "Root cause relevant": "Релевантна для root cause",
    "Impact relevant": "Релевантна для impact",
    "Value type": "Тип значения",
    "Latency": "Задержка",
    "Dimension key": "Ключ dimension",
    # 8. declarativegrouping
    "Monitored technology name": "Имя мониторимой технологии",
    "Define the process group": "Задайте process group",
    "Process group display name": "Отображаемое имя process group",
    "Process group identifier": "Идентификатор process group",
    "Report process group": "Сообщать о process group",
    "Define detection rules": "Задайте правила обнаружения",
    "Select process property": "Выберите свойство процесса",
    "Condition": "Условие",
    # 9. rum-web-automatic-injection
    "Real User Monitoring code source": "Источник Real User Monitoring-кода",
    "Snippet format": "Формат сниппета",
    "Cache control headers": "Заголовки cache control",
    "Specify path for RUM monitoring code": "Укажите путь для RUM monitoring-кода",
    "Load the monitoring code": "Загружать monitoring-код",
    "Script execution attribute": "Атрибут выполнения скрипта",
    "Optimize the value of cache control headers for use with Dynatrace Real User Monitoring": "Оптимизировать значение заголовков cache control для использования с Dynatrace Real User Monitoring",
    # 10. anomaly-detection-infrastructure-disks
    "Disk": "Диск",
    "Detect low disk space": "Обнаруживать нехватку места на диске",
    "Detection mode for low disk space": "Режим обнаружения нехватки места на диске",
    "Detect slow-running disks": "Обнаруживать медленные диски",
    "Detection mode for slow running disks": "Режим обнаружения медленных дисков",
    "Detect low inodes number available": "Обнаруживать нехватку доступных inode",
    "Detection mode for low inodes number available": "Режим обнаружения нехватки доступных inode",
    "Alert if free disk space is lower than this percentage in 3 out of 5 samples": "Оповещать, если свободное место на диске ниже этого процента в 3 из 5 замеров",
    "Alert if disk read time or write time is higher than this threshold in 3 out of 5 samples": "Оповещать, если время чтения или записи на диск выше этого порога в 3 из 5 замеров",
    "Alert if the percentage of available inodes is lower than this threshold in 3 out of 5 samples": "Оповещать, если процент доступных inode ниже этого порога в 3 из 5 замеров",
    # 11. logmonitoring-log-agent-configuration
    "Detect open log files": "Обнаруживать открытые лог-файлы",
    "Detect system logs": "Обнаруживать системные логи",
    "Detect logs of containerized applications": "Обнаруживать логи контейнеризованных приложений",
    "Detect IIS logs": "Обнаруживать IIS-логи",
    "Detect logs on network file systems": "Обнаруживать логи на сетевых файловых системах",
    "Allow OneAgent to monitor Dynatrace logs": "Разрешить OneAgent мониторить Dynatrace-логи",
    "Detect container time zones": "Обнаруживать часовые пояса контейнеров",
    "Default timezone for agents": "Часовой пояс по умолчанию для агентов",
    "Timestamp search limit": "Лимит поиска временной метки",
    "Severity search chars limit": "Лимит поиска severity по символам",
    "Severity search lines limit": "Лимит поиска severity по строкам",
    "Maximum number of log sources per process group instance": "Максимальное число источников логов на один process group instance",
    "Windows Event Log query timeout": "Таймаут запроса Windows Event Log",
    "Minimal log file size to perform binary detection.": "Минимальный размер лог-файла для бинарного обнаружения.",
    # 12. url-path-pattern-matching-rules
    "Rule": "Правило",
    "Rule name": "Имя правила",
    "Matching condition": "Условие сопоставления",
    "URL path patterns": "Шаблоны URL-путей",
}

PARAM_DESC = {
    # 1. monitoring-slo
    "The description of the SLO": "Описание SLO",
    'For details, see the Metrics page (`<your-dynatrace-url>//ui/metrics "Metrics page"`).': 'Подробнее см. на Metrics page (`<your-dynatrace-url>//ui/metrics "Metrics page"`).',
    'Select "Aggregate" to have the measurements of this success metric aggregated into a single percentage-rate metric.': 'Выберите "Aggregate", чтобы измерения этой success-метрики агрегировались в одну метрику percentage-rate.',
    'Set a filter parameter (entitySelector) on any GET call to evaluate this SLO against specific services only (for example, type("SERVICE")). For details, see the [Entity Selector documentation](https://dt-url.net/entityselector).': 'Задайте параметр фильтра (entitySelector) в любом GET-вызове, чтобы вычислять этот SLO только для конкретных сервисов (например, type("SERVICE")). Подробнее см. в [Entity Selector documentation](https://dt-url.net/entityselector).',
    "Define the timeframe during which the SLO is to be evaluated. For the timeframe you can enter expressions like -1h (last hour), -1w (last week) or complex expressions like -2d to now (last two days), -1d/d to now/d (beginning of yesterday to beginning of today).": "Задайте временной диапазон, в котором будет вычисляться SLO. В качестве диапазона можно вводить выражения вида -1h (последний час), -1w (последняя неделя) или сложные выражения вида -2d to now (последние два дня), -1d/d to now/d (от начала вчерашнего дня до начала сегодняшнего).",
    "Set the target value of the SLO. A percentage below this value indicates a failure.": "Задайте целевое значение SLO. Процент ниже этого значения означает failure.",
    "Set the warning value of the SLO. At the warning state the SLO is fulfilled. However, it is getting close to a failure.": "Задайте значение SLO для предупреждения. В состоянии warning SLO ещё выполняется, но приближается к failure.",
    "The threshold defines when a burn rate is marked as fast-burning (high-emergency). Burn rates lower than this threshold (and greater than 1) are highlighted as slow-burn (low-emergency).": "Порог определяет, когда burn rate помечается как fast-burning (high-emergency). Burn rate ниже этого порога (и больше 1) выделяется как slow-burn (low-emergency).",
    # 2. rum-web-enablement (triple-mojibake in last param)
    "Capture and analyze all user actions within your application. Enable [Real User Monitoring (RUM)](https://dt-url.net/1n2b0prq) to monitor and improve your application's performance, identify errors, and gain insight into your user's behavior and experience.": "Захватывайте и анализируйте все действия пользователей внутри приложения. Включите [Real User Monitoring (RUM)](https://dt-url.net/1n2b0prq), чтобы мониторить и улучшать производительность приложения, выявлять ошибки и получать представление о поведении и опыте ваших пользователей.",
    "[Session Replay](https://dt-url.net/session-replay) captures all user interactions within your application and replays them in a movie-like experience while providing [best-in-class security and data protection](https://dt-url.net/b303zxj).": "[Session Replay](https://dt-url.net/session-replay) захватывает все взаимодействия пользователей с приложением и воспроизводит их как в фильме, обеспечивая при этом [best-in-class security and data protection](https://dt-url.net/b303zxj).",
    "Percentage of user sessions captured and analyzed": "Процент захватываемых и анализируемых user-сессий",
    "Before enabling, Dynatrace checks your system against the prerequisites for [Session Replay Classic](https://dt-url.net/ma3m0psf).": "Перед включением Dynatrace проверяет систему на соответствие требованиям для [Session Replay Classic](https://dt-url.net/ma3m0psf).",
    "[Percentage of user sessions recorded with Session Replay Classic](https://dt-url.net/sr-cost-traffic-control). For example, if you have 50% for RUM and 50% for Session Replay Classic, it results in 25% of sessions recorded with Session Replay Classic.": "[Процент user-сессий, записанных через Session Replay Classic](https://dt-url.net/sr-cost-traffic-control). Например, при 50% для RUM и 50% для Session Replay Classic получится 25% сессий, записанных через Session Replay Classic.",
    "Capture user interactions within your frontend, including all clicks and taps. During the Early Access period, there"
    + TM
    + "s no cost associated with this feature.": "Захватывайте взаимодействия пользователей во frontend, включая все клики и тапы. В период Early Access эта функция предоставляется без затрат.",
    # 3. service-detection-v2-for-oneagent (3× triple-mojibake `opt-inâ€™s`)
    "Limits the opt-in"
    + TM
    + "s scope by filtering with [DQL matcher](https://dt-url.net/l603wby) conditions on a selected set of attributes.  Service detection v2 is only applied if this condition matches. Allowed attributes: Resource attributes, and custom attributes. If empty, the condition will always match.": "Ограничивает scope opt-in фильтрацией [DQL matcher](https://dt-url.net/l603wby)-условиями по выбранному набору атрибутов.  Service detection v2 применяется только если это условие совпало. Допустимые атрибуты: Resource attributes и custom attributes. Если поле пустое, условие всегда совпадает.",
    "Limits the opt-in"
    + TM
    + "s scope by filtering with [DQL matcher](https://dt-url.net/l603wby) conditions on a selected set of attributes. Resource attributes must be present.  Service detection v2 is only applied if this condition matches. Allowed attributes: Resource attributes, and custom attributes. If empty, the condition will always match. If the set of resource attributes is missing or empty, the condition will be considered not to match.": "Ограничивает scope opt-in фильтрацией [DQL matcher](https://dt-url.net/l603wby)-условиями по выбранному набору атрибутов. Resource attributes должны присутствовать.  Service detection v2 применяется только если это условие совпало. Допустимые атрибуты: Resource attributes и custom attributes. Если поле пустое, условие всегда совпадает. Если набор resource attributes отсутствует или пуст, условие считается несовпавшим.",
    # 4. custom-metrics
    "Defines the type of value to be extracted from the user session. When using **User session counter**, the number of user sessions is counted (similar to count(\\*) when using USQL). When using **User session field value**, the value of a user session field is extracted.": "Задаёт тип значения, извлекаемого из user-сессии. При использовании **User session counter** подсчитывается число user-сессий (аналогично count(\\*) в USQL). При использовании **User session field value** извлекается значение поля user-сессии.",
    'Defines the fields that are used as dimensions. A dimension is a collection of reference information about a metric data point that is of interest to your business. Dimensions are parameters like "browserFamily", "userType", "country". For example, using "userType" as a dimension allows you to split chart data based on user types.': 'Задаёт поля, используемые как dimensions. Dimension, это набор справочной информации о точке данных метрики, представляющий интерес для бизнеса. Dimensions, это параметры вроде "browserFamily", "userType", "country". Например, использование "userType" в качестве dimension позволяет разбивать данные графика по типам пользователей.',
    'Defines the filters for the user session. Filters apply at the moment of extracting the data and only sessions that satisfy the filtering criteria will be used to extract the custom metrics. You will not be able to modify these filters in the metric data explorer. For example, using "userType equals REAL\\_USER" will give you only data from real users, while forcing the synthetic sessions to be ignored.': 'Задаёт фильтры для user-сессии. Фильтры применяются в момент извлечения данных, и для извлечения пользовательских метрик используются только сессии, удовлетворяющие критериям фильтрации. Эти фильтры нельзя изменить в metric data explorer. Например, "userType equals REAL\\_USER" даст данные только от реальных пользователей, исключая synthetic-сессии.',
    # 5. synthetic-multiprotocol-config
    "Option not supported yet": "Опция пока не поддерживается",
    'All steps in the monitor must be the same request type. Learn more about request types in [Dynatrace documentation](https://dt-url.net/0803zt8 "Visit Dynatrace documentation")': 'Все шаги монитора должны быть одного типа запроса. Подробнее о типах запросов см. в [Dynatrace documentation](https://dt-url.net/0803zt8 "Visit Dynatrace documentation")',
    'See syntax and examples in [Dynatrace documentation](https://dt-url.net/3443zor "Visit Dynatrace documentation")': 'Синтаксис и примеры см. в [Dynatrace documentation](https://dt-url.net/3443zor "Visit Dynatrace documentation")',
    'See possible configuration properties in [Dynatrace documentation](https://dt-url.net/gq83z4l "Visit Dynatrace documentation")': 'Возможные свойства конфигурации см. в [Dynatrace documentation](https://dt-url.net/gq83z4l "Visit Dynatrace documentation")',
    'See possible step-level constraints in [Dynatrace documentation](https://dt-url.net/x3a3zev "Visit Dynatrace documentation")': 'Возможные ограничения уровня шага см. в [Dynatrace documentation](https://dt-url.net/x3a3zev "Visit Dynatrace documentation")',
    'See possible request-level configurations in [Dynatrace documentation](https://dt-url.net/b803zmi "Visit Dynatrace documentation")': 'Возможные конфигурации уровня запроса см. в [Dynatrace documentation](https://dt-url.net/b803zmi "Visit Dynatrace documentation")',
    # 6. user-action-custom-metrics
    "Defines the type of value to be extracted from the user action. When using **user action counter**, the number of user actions is counted (similar to count(\\*) when using USQL). When using **user action field value**, the value of a user action field is extracted.": "Задаёт тип значения, извлекаемого из user-действия. При использовании **user action counter** подсчитывается число user-действий (аналогично count(\\*) в USQL). При использовании **user action field value** извлекается значение поля user-действия.",
    'Defines the fields that are used as dimensions. A dimension is a collection of reference information about a metric data point that is of interest to your business. Dimensions are parameters like "application", "type", "apdexCategory". For example, using "type" as a dimension allows you to split chart data based on the user action type.': 'Задаёт поля, используемые как dimensions. Dimension, это набор справочной информации о точке данных метрики, представляющий интерес для бизнеса. Dimensions, это параметры вроде "application", "type", "apdexCategory". Например, использование "type" в качестве dimension позволяет разбивать данные графика по типу user-действия.',
    'Defines the filters for the user action. Filters apply at the moment of extracting the data and only sessions that satisfy the filtering criteria will be used to extract the custom metrics. You will not be able to modify these filters in the metric data explorer. For example, using "type equals Xhr" will give you only data from xhr actions, while forcing the rest of user actions of different types to be ignored.': 'Задаёт фильтры для user-действия. Фильтры применяются в момент извлечения данных, и для извлечения пользовательских метрик используются только сессии, удовлетворяющие критериям фильтрации. Эти фильтры нельзя изменить в metric data explorer. Например, "type equals Xhr" даст данные только от xhr-действий, исключая user-действия других типов.',
    # 7. metric-metadata
    "The raw value is stored in bits or bytes. The user interface can display it in these numeral systems:  Binary: 1 MiB = 1024 KiB = 1,048,576 bytes  Decimal: 1 MB = 1000 kB = 1,000,000 bytes  If not set, the decimal system is used.": "Сырое значение хранится в битах или байтах. Пользовательский интерфейс может отображать его в этих системах счисления:  Binary: 1 MiB = 1024 KiB = 1 048 576 байт  Decimal: 1 MB = 1000 kB = 1 000 000 байт  Если не задано, используется decimal-система.",
    "Define metadata per metric dimension.": "Задайте метаданные для каждого dimension метрики.",
    "Specifies which entity dimension should be used as the primary dimension. The property can only be configured for metrics ingested with the Metrics API.": "Указывает, какой entity dimension использовать как primary dimension. Свойство можно настроить только для метрик, принятых через Metrics API.",
    "The minimum allowed value of the metric.": "Минимально допустимое значение метрики.",
    "The maximum allowed value of the metric.": "Максимально допустимое значение метрики.",
    "Whether (true or false) the metric is related to a root cause of a problem.  A root-cause relevant metric represents a strong indicator for a faulty component.": "Связана ли метрика (true или false) с root cause проблемы.  Метрика, релевантная для root cause, является сильным индикатором сбойного компонента.",
    "Whether (true or false) the metric is relevant to a problem's impact.  An impact-relevant metric is highly dependent on other metrics and changes because an underlying root-cause metric has changed.": "Релевантна ли метрика (true или false) для impact проблемы.  Метрика, релевантная для impact, сильно зависит от других метрик и изменяется из-за изменения нижележащей root-cause-метрики.",
    "The type of the metric's value. You have these options:  score: A score metric is a metric where high values indicate a good situation, while low values indicate trouble. An example of such a metric is a success rate.  error: An error metric is a metric where high values indicate trouble, while low values indicate a good situation. An example of such a metric is an error count.": "Тип значения метрики. Доступные варианты:  score: метрика, у которой высокие значения означают хорошую ситуацию, а низкие, проблему. Пример: success rate.  error: метрика, у которой высокие значения означают проблему, а низкие, хорошую ситуацию. Пример: счётчик ошибок.",
    "The latency of the metric, in minutes.  The latency is the expected reporting delay (for example, caused by constraints of cloud vendors or other third-party data sources) between the observation of a metric data point and its availability in Dynatrace.  The allowed value range is from 1 to 60 minutes.": "Задержка метрики в минутах.  Задержка, это ожидаемая задержка передачи (например, из-за ограничений cloud-провайдеров или других сторонних источников данных) между наблюдением точки данных метрики и её доступностью в Dynatrace.  Допустимый диапазон значений, от 1 до 60 минут.",
    # 8. declarativegrouping
    "Note: Reported only in full-stack, infrastructure and discovery modes.": "Примечание: передаётся только в режимах full-stack, infrastructure и discovery.",
    "Enter a descriptive process group display name and a unique identifier that Dynatrace can use to recognize this process group.": "Введите описательное отображаемое имя process group и уникальный идентификатор, по которым Dynatrace будет распознавать эту process group.",
    "This identifier is used by Dynatrace to recognize this process group.": "Этот идентификатор используется Dynatrace для распознавания этой process group.",
    "This property tells OneAgent a condition for reporting the created Process group to Dynatrace.": "Это свойство сообщает OneAgent условие, при котором созданная Process group передаётся в Dynatrace.",
    "Define process detection rules by selecting a process property and a condition. Each process group can have multiple detection rules associated with it.": "Задайте правила обнаружения процессов, выбрав свойство процесса и условие. С каждой process group можно связать несколько правил обнаружения.",
    # declarativegrouping :61 — triple-mojibake en-dash `–` (U+2013) as separator inside bullet list (4×)
    "* $contains(svc) "
    + TM_ENDASH
    + " Matches if svc appears anywhere in the process property value. * $eq(svc.exe) "
    + TM_ENDASH
    + " Matches if svc.exe matches the process property value exactly. * $prefix(svc) "
    + TM_ENDASH
    + " Matches if app matches the prefix of the process property value. * $suffix(svc.py) "
    + TM_ENDASH
    + " Matches if svc.py matches the suffix of the process property value.  For example, $suffix(svc.py) would detect processes named loyaltysvc.py and paymentssvc.py.  For more details, see [Declarative process grouping](https://dt-url.net/j142w57).": "* $contains(svc), совпадает, если svc встречается в любом месте значения свойства процесса. * $eq(svc.exe), совпадает, если svc.exe в точности равно значению свойства процесса. * $prefix(svc), совпадает, если app совпадает с префиксом значения свойства процесса. * $suffix(svc.py), совпадает, если svc.py совпадает с суффиксом значения свойства процесса.  Например, $suffix(svc.py) обнаружит процессы с именами loyaltysvc.py и paymentssvc.py.  Подробнее см. в [Declarative process grouping](https://dt-url.net/j142w57).",
    # 9. rum-web-automatic-injection
    "*Code Snippet:* OneAgent injects an inline script that initializes Dynatrace and dynamically downloads the monitoring code into your application. Use when you want to inject the monitoring code in deferred mode.  *Inline Code:* OneAgent injects the configuration and the monitoring code inline into your application. Use this injection type when you need to keep the number of web requests at a minimum.  *OneAgent JavaScript Tag:* OneAgent injects a JavaScript tag into your application, containing the configuration and a link to the monitoring code. This is our default injection type, since it's most versatile.  *OneAgent JavaScript tag with SRI:* OneAgent injects the configuration, a reference to an external file containing the monitoring code, and a hash that allows the browser to verify the integrity of the monitoring code before executing it.  Compare the different [injection formats](https://dt-url.net/vx5g0ptn).": "*Code Snippet:* OneAgent инжектит inline-скрипт, который инициализирует Dynatrace и динамически загружает monitoring-код в ваше приложение. Используйте, если нужно инжектить monitoring-код в deferred-режиме.  *Inline Code:* OneAgent инжектит конфигурацию и monitoring-код inline в ваше приложение. Используйте этот тип инъекции, когда нужно минимизировать число web-запросов.  *OneAgent JavaScript Tag:* OneAgent инжектит в ваше приложение JavaScript-тег, содержащий конфигурацию и ссылку на monitoring-код. Это наш тип инъекции по умолчанию как самый универсальный.  *OneAgent JavaScript tag with SRI:* OneAgent инжектит конфигурацию, ссылку на внешний файл с monitoring-кодом и хеш, позволяющий браузеру проверить целостность monitoring-кода до его выполнения.  Сравните разные [форматы инъекции](https://dt-url.net/vx5g0ptn).",
    "Specify the URL path under which the RUM monitoring code is requested. By default, the path is set to the root or the context root. A custom URL path may be necessary if your server operates behind a firewall.": "Укажите URL-путь, по которому запрашивается RUM monitoring-код. По умолчанию путь установлен в root или context root. Пользовательский URL-путь может потребоваться, если ваш сервер работает за firewall.",
    "Add the `async` attribute to download the monitoring code in parallel with parsing the page, and execute it immediately upon availability.  Add the `defer` attribute to execute the monitoring code after the page has finished parsing.": "Добавьте атрибут `async`, чтобы загружать monitoring-код параллельно с парсингом страницы и выполнять его немедленно по доступности.  Добавьте атрибут `defer`, чтобы выполнять monitoring-код после завершения парсинга страницы.",
    "[How to ensure timely configuration updates for automatic injection?](https://dt-url.net/m9039ea)": "[Как обеспечить своевременные обновления конфигурации для автоматической инъекции?](https://dt-url.net/m9039ea)",
    # 11. logmonitoring-log-agent-configuration
    "Automatically detect logs written by important processes. For more details, check our [documentation](https://dt-url.net/7v02z76)": "Автоматически обнаруживать логи, записываемые важными процессами. Подробнее см. в [documentation](https://dt-url.net/7v02z76)",
    "Linux: syslog, message log Windows: system, application, security event logs": "Linux: syslog, message log Windows: system, application, security event logs",
    "Allows detection of log messages written to the containerized application's stdout/stderr streams.": "Позволяет обнаруживать сообщения логов, записываемые в потоки stdout/stderr контейнеризованного приложения.",
    "Allows detection of logs and event logs written by IIS server.": "Позволяет обнаруживать логи и event logs, записываемые IIS-сервером.",
    "Allows detection of logs written to mounted network storage drives. Applies only to Linux hosts. For Windows operating system it's always enabled.": "Позволяет обнаруживать логи, записываемые на смонтированные сетевые накопители. Применяется только к Linux-хостам. Для Windows-систем включено всегда.",
    "Enabling this option may affect your licensing costs. For more details, see [documentation](https://dt-url.net/7v02z76).": "Включение этой опции может повлиять на лицензионные затраты. Подробнее см. в [documentation](https://dt-url.net/7v02z76).",
    "Enables automatic detection of timezone in container's logs if it is not explicitly defined in content or configured.": "Включает автоматическое обнаружение часового пояса в логах контейнера, если он не задан явно в контенте или в конфигурации.",
    "Default timezone for agent if more specific configurations is not defined.": "Часовой пояс по умолчанию для агента, если не задана более конкретная конфигурация.",
    "Defines the number of characters in every log line (starting from the first character in the line) where the timestamp is searched.": "Задаёт количество символов в каждой строке лога (начиная с первого символа), в которых ищется временная метка.",
    "Defines the number of characters in every log line (starting from the first character in the line) where severity is searched.": "Задаёт количество символов в каждой строке лога (начиная с первого символа), в которых ищется severity.",
    "Defines the number of the first lines of every log entry where severity is searched.": "Задаёт количество первых строк каждой записи лога, в которых ищется severity.",
    "Defines the maximum number of log group instances per entity after which, the new automatic ones wouldn't be added.": "Задаёт максимальное число log group instances на одну сущность, после которого новые автоматические instances не добавляются.",
    "Defines the maximum timeout value, in seconds, for the query extracting Windows Event Logs": "Задаёт максимальное значение таймаута (в секундах) для запроса, извлекающего Windows Event Logs",
    "Defines the minimum number of bytes in log file required for binary detection.": "Задаёт минимальное число байт в лог-файле, необходимое для бинарного обнаружения.",
    # 12. url-path-pattern-matching-rules
    "If enabled, the rule will be evaluated.": "Если включено, правило будет вычисляться.",
    "Limits the scope of the service splitting rule using [DQL matcher](https://dt-url.net/l603wby) conditions on resource attributes.  A rule is applied only if the condition matches, otherwise the ruleset evaluation continues.  If empty, the condition will always match.": "Ограничивает scope правила service splitting [DQL matcher](https://dt-url.net/l603wby)-условиями по resource attributes.  Правило применяется только если условие совпало, иначе вычисление ruleset продолжается.  Если поле пустое, условие всегда совпадает.",
    # The big URL-pattern PARAM_DESC — triple-mojibake non-breaking hyphen `‑` (U+2011) in 6 places
    "First matching pattern defines the resulting url.path.pattern attribute value.  A URL path pattern describes how a raw URL path (for example, `/path/123`) is generalized into a stable template (for example, `/path/{id}`). It operates on path segments (parts between `/`) and is used to produce low"
    + TM_NBHYPHEN
    + "volatility values for the `url.path.pattern` attribute.  Patterns are matched against a normalized path that always starts with a single leading `/`. Matching is case sensitive.  Syntax Patterns are written as a sequence of segments separated by `/`:  * Literal segments + Match an exact path segment and are copied as"
    + TM_NBHYPHEN
    + "is.   + Example: `/api/items` matches only paths whose first two segments are `api` and `items`. * `{placeholder}` + Matches exactly one path segment and outputs the placeholder name in braces.   + Use this to hide variable parts like IDs or other dynamic identifiers.   + Example: `/api/items/{id}` matches `/api/items/123` or `/api/items/abc` and produces `/api/items/{id}`. * `_` + Variable segment that matches exactly one path segment and keeps the original value in the result.   + A common use is versioned APIs where the version should remain visible.   + Example: `/api/_/getAll` matches `/api/v1/getAll` or `/api/v2/getAll` and produces `/api/v1/getAll` or `/api/v2/getAll` respectively. * `*` + Catch"
    + TM_NBHYPHEN
    + "all that matches zero or more trailing segments.   + Must be the last token in the pattern.   + Example: `/internal/*` matches `/internal`, `/internal/service`, `/internal/service/operation/extra` and produces `/internal/*`.  Examples  * `/api/items/{id}` + Matches: `/api/items/1`, `/api/items/xyz`   + Non"
    + TM_NBHYPHEN
    + "matches: `/api/items`, `/api/items/1/details` * `/api/_/getAll` + Matches: `/api/v1/getAll`, `/api/v2/getAll` * `/internal/*` + Matches any path starting with `/internal`, regardless of depth.  Use these patterns to replace high"
    + TM_NBHYPHEN
    + "cardinality parts of your URLs (IDs, version numbers, deep internal paths) with placeholders or catch"
    + TM_NBHYPHEN
    + "alls while keeping the overall structure of the endpoint recognizable.": "Первый совпавший шаблон определяет результирующее значение атрибута url.path.pattern.  Шаблон URL-пути описывает, как сырой URL-путь (например, `/path/123`) обобщается в стабильный template (например, `/path/{id}`). Работает с сегментами пути (частями между `/`) и используется для получения low-volatility-значений атрибута `url.path.pattern`.  Шаблоны сопоставляются с нормализованным путём, который всегда начинается с одного ведущего `/`. Сопоставление чувствительно к регистру.  Синтаксис. Шаблоны записываются как последовательность сегментов, разделённых `/`:  * Литеральные сегменты + Совпадают с точным сегментом пути и копируются как есть.   + Пример: `/api/items` совпадает только с путями, у которых первые два сегмента: `api` и `items`. * `{placeholder}` + Совпадает ровно с одним сегментом пути и выводит имя placeholder в фигурных скобках.   + Используется, чтобы скрыть переменные части вроде ID или других динамических идентификаторов.   + Пример: `/api/items/{id}` совпадает с `/api/items/123` или `/api/items/abc` и даёт `/api/items/{id}`. * `_` + Переменный сегмент, совпадающий ровно с одним сегментом пути и сохраняющий исходное значение в результате.   + Типичное применение, версионируемые API, где версия должна оставаться видимой.   + Пример: `/api/_/getAll` совпадает с `/api/v1/getAll` или `/api/v2/getAll` и даёт соответственно `/api/v1/getAll` или `/api/v2/getAll`. * `*` + Catch-all, совпадающий с нулём или более trailing-сегментов.   + Должен быть последним токеном шаблона.   + Пример: `/internal/*` совпадает с `/internal`, `/internal/service`, `/internal/service/operation/extra` и даёт `/internal/*`.  Примеры  * `/api/items/{id}` + Совпадения: `/api/items/1`, `/api/items/xyz`   + Не совпадения: `/api/items`, `/api/items/1/details` * `/api/_/getAll` + Совпадения: `/api/v1/getAll`, `/api/v2/getAll` * `/internal/*` + Совпадения с любым путём, начинающимся на `/internal`, на любой глубине.  Используйте эти шаблоны, чтобы заменить high-cardinality-части URL (ID, номера версий, глубокие внутренние пути) на placeholder'ы или catch-all-конструкции, сохраняя общую структуру эндпоинта узнаваемой.",
}

# Structural canon (shared with L4-AG.1a.1-8 / L4-AF).
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
    if label and label not in PARAM_LABEL:
        return None
    new_label = PARAM_LABEL.get(label, label)
    d = cdesc
    ei = d.find(ENUM_PHRASE[0])
    marker_len = len(ENUM_PHRASE[0])
    if ei == -1:
        ei = d.find(ENUM_PHRASE[1])
        marker_len = len(ENUM_PHRASE[1])
    if ei != -1:
        head = d[:ei].rstrip()
        enum_tail = d[ei + marker_len :]
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


NESTED_HEADING_RE = _re.compile(r"^##### The (`[^`]+`) object$")


def _nested_heading(line):
    m = NESTED_HEADING_RE.match(line)
    if not m:
        return None
    return "##### Объект " + m.group(1)


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    t = io.open(src, "r", encoding="utf-8", newline="").read()
    t = _normalize(t)
    for en, ru in SCHEMA_DESC.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    for en, ru in STRUCT:
        t = t.replace(en, ru)
    t = t.replace(ENUM_PHRASE[0], ENUM_PHRASE[1])
    out = []
    for line in t.split("\n"):
        nl = _heading(line) or _nested_heading(line) or _param_row(line)
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
        print("%-72s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY:", "OK" if bad == 0 else f"BAD ({bad})")
