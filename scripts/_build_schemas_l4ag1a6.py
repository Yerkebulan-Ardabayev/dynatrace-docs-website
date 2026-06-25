# -*- coding: utf-8 -*-
"""L4-AG.1a.6 builder: 37 builtin-*.md schema-table files (3.0-3.5 KB) from
docs/managed/dynatrace-api/environment-api/settings/schemas/.

Anchor canon: L4-AG.1a.5 _build_schemas_l4ag1a5.py.

Includes the openpipeline-*-pipeline-groups family (12 files, identical
schema description, identical nested StageConfig + PipelineGroupComposition).
Also includes 3 deprecated attribute schemas (span-attribute,
span-event-attribute, resource-attribute) with identical Masking enum-prefix.

Mojibake byte-keys preserved verbatim:
  - process-process-monitoring `thatâ€™s` triple-mojibake (U+00E2 U+0080 U+0099)
  - log-events `DavisÂ®` double-B mojibake (U+00C2 U+00AE)
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

# Triple-mojibake apostrophe (3 chars => 6 bytes UTF-8).
Q = chr(0xE2) + chr(0x80) + chr(0x99)
# Double-mojibake registered trademark (`Â®`, 2 chars U+00C2 U+00AE => 4 bytes).
RM = chr(0xC2) + chr(0xAE)

PILOT = [
    "builtin-process-visibility.md",
    "builtin-span-context-propagation.md",
    "builtin-synthetic-http-advanced-execution.md",
    "builtin-rum-provider-breakdown.md",
    "builtin-process-process-monitoring.md",
    "builtin-span-attribute.md",
    "builtin-hyperscaler-authentication-connections-aws.md",
    "builtin-logmonitoring-sensitive-data-masking-settings.md",
    "builtin-cloud-kubernetes.md",
    "builtin-span-event-attribute.md",
    "builtin-rum-web-request-errors.md",
    "builtin-openpipeline-logs-pipeline-groups.md",
    "builtin-openpipeline-spans-pipeline-groups.md",
    "builtin-ibmmq-queue-managers.md",
    "builtin-synthetic-multiprotocol-performance-thresholds.md",
    "builtin-issue-tracking-integration.md",
    "builtin-openpipeline-events-pipeline-groups.md",
    "builtin-endpoint-detection-rules.md",
    "builtin-logmonitoring-log-events.md",
    "builtin-openpipeline-metrics-pipeline-groups.md",
    "builtin-logmonitoring-log-storage-settings.md",
    "builtin-logmonitoring-log-agent-feature-flags.md",
    "builtin-openpipeline-bizevents-pipeline-groups.md",
    "builtin-openpipeline-events-sdlc-pipeline-groups.md",
    "builtin-openpipeline-user-events-pipeline-groups.md",
    "builtin-openpipeline-davis-events-pipeline-groups.md",
    "builtin-openpipeline-usersessions-pipeline-groups.md",
    "builtin-openpipeline-system-events-pipeline-groups.md",
    "builtin-openpipeline-davis-problems-pipeline-groups.md",
    "builtin-openpipeline-events-security-pipeline-groups.md",
    "builtin-openpipeline-security-events-pipeline-groups.md",
    "builtin-anomaly-detection-disk-rules.md",
    "builtin-rum-ip-mappings.md",
    "builtin-service-detection-rules.md",
    "builtin-rum-web-key-performance-metric-xhr-actions.md",
    "builtin-failure-detection-environment-rules.md",
    "builtin-resource-attribute.md",
]

# Schema heading display-name. EN product/tech terms kept where canonical.
# Family openpipeline-*-pipeline-groups: 12 unique display names with (kind).
DISPLAY_NAME = {
    "Process instance snapshots": "Снимки экземпляров процессов",
    "Span context propagation": "Распространение контекста span",
    "Advanced settings": "Дополнительные настройки",
    "Provider breakdown": "Разбивка по провайдерам",
    "Process group monitoring": "Мониторинг process group",
    "Span attributes": "Атрибуты span",
    "Connections to AWS environments": "Подключения к AWS-окружениям",
    "Sensitive data masking": "Маскирование чувствительных данных",
    "Connection settings": "Параметры подключения",
    "Span events": "События span",
    "Request errors": "Ошибки запросов",
    "Pipeline Groups configuration (logs)": "Конфигурация Pipeline Groups (logs)",
    "Pipeline Groups configuration (spans)": "Конфигурация Pipeline Groups (spans)",
    "IBM MQ queue managers": "Менеджеры очередей IBM MQ",
    "Performance thresholds": "Пороги производительности",
    "Issue-tracking for releases": "Issue-tracking для релизов",
    "Pipeline Groups configuration (events)": "Конфигурация Pipeline Groups (events)",
    "Endpoint detection": "Обнаружение endpoint'ов",
    "Log events": "События лога",
    "Pipeline Groups configuration (metrics)": "Конфигурация Pipeline Groups (metrics)",
    "Log ingest rules": "Правила ingest логов",
    "Log module feature flags": "Feature flags модуля логов",
    "Pipeline Groups configuration (bizevents)": "Конфигурация Pipeline Groups (bizevents)",
    "Pipeline Groups configuration (events.sdlc)": "Конфигурация Pipeline Groups (events.sdlc)",
    "Pipeline Groups configuration (user.events)": "Конфигурация Pipeline Groups (user.events)",
    "Pipeline Groups configuration (davis.events)": "Конфигурация Pipeline Groups (davis.events)",
    "Pipeline Groups configuration (usersessions)": "Конфигурация Pipeline Groups (usersessions)",
    "Pipeline Groups configuration (system.events)": "Конфигурация Pipeline Groups (system.events)",
    "Pipeline Groups configuration (davis.problems)": "Конфигурация Pipeline Groups (davis.problems)",
    "Pipeline Groups configuration (events.security)": "Конфигурация Pipeline Groups (events.security)",
    "Pipeline Groups configuration (security.events)": "Конфигурация Pipeline Groups (security.events)",
    "Disk anomaly detection rules": "Правила обнаружения аномалий дисков",
    "Map IP addresses to locations": "Сопоставление IP-адресов с локациями",
    "Service detection": "Обнаружение сервисов",
    "Apdex configuration for XHR actions": "Настройка Apdex для XHR-действий",
    "Failure detection rules": "Правила обнаружения сбоев",
    "Resource attributes": "Атрибуты ресурса",
}

# Whole-line schema descriptions (replaced as `\n` + EN + `\n` -> `\n` + RU + `\n`).
SCHEMA_DESC = {
    # 1. process-visibility
    "If this feature is enabled, Dynatrace examines the most resource-consuming processes running on your host and the processes monitored by **Process availability**.": "Если эта функция включена, Dynatrace исследует наиболее ресурсоёмкие процессы, запущенные на хосте, и процессы, мониторимые через **Process availability**.",
    "When a triggering event occurs, metrics reported 10 minutes before and 10 minutes after the event for those processes are sent to the cluster.": "Когда происходит триггерное событие, метрики этих процессов за 10 минут до и 10 минут после события отправляются в кластер.",
    "A graph of the resource consumption by process is available.": "Доступен график потребления ресурсов по процессам.",
    "If **Process instance snapshots** is triggered by **Process availability**, you can see the behavior of processes before they ended, and whether they restarted within 10 minutes.": "Если **Process instance snapshots** запускается через **Process availability**, можно увидеть поведение процессов перед их завершением, а также перезапустились ли они в течение 10 минут.",
    "Reported process metrics:": "Сообщаемые метрики процесса:",
    "* CPU usage (%)": "* Использование CPU (%)",
    "* Memory usage (B)": "* Использование памяти (B)",
    "* Incoming network traffic (KB)": "* Входящий сетевой трафик (KB)",
    "* Outgoing network traffic (KB)": "* Исходящий сетевой трафик (KB)",
    "Metrics are reported once per minute and cover the number of processes defined in **Reported processes limit**.": "Метрики сообщаются раз в минуту и покрывают количество процессов, заданное в **Reported processes limit**.",
    "Each host can report up to 60 minutes of these metrics per day. When the limit is exceeded, metrics aren't sent even when a new event arises.": "Каждый хост может сообщать до 60 минут таких метрик в день. При превышении лимита метрики не отправляются, даже если возникает новое событие.",
    "Events triggering **Process instance snapshots**:": "События, запускающие **Process instance snapshots**:",
    "* High host CPU usage": "* Высокое использование CPU хоста",
    "* High system load": "* Высокая нагрузка системы",
    "* High host memory usage": "* Высокое использование памяти хоста",
    "* High packet drop rates": "* Высокий процент потери пакетов",
    "* High NIC utilization rates": "* Высокая утилизация NIC",
    "* High number of NIC errors": "* Большое количество ошибок NIC",
    "* Manual requests": "* Ручные запросы",
    "* Process availability events": "* События Process availability",
    "For details, see [Process instance snapshots](https://dt-url.net/yw02uea)": "Подробнее см. [Process instance snapshots](https://dt-url.net/yw02uea)",
    # 2. span-context-propagation
    "Context propagation enables you to connect PurePaths through OpenTelemetry. Define rules to enable context propagation for certain spans within OneAgent.": "Распространение контекста позволяет соединять PurePath'ы через OpenTelemetry. Задайте правила, чтобы включить распространение контекста для определённых span внутри OneAgent.",
    "Note: This config does not apply to Trace ingest.": "Примечание: эта конфигурация не применяется к Trace ingest.",
    # 3. synthetic-http-advanced-execution
    "Fine-tune your HTTP monitor's execution with custom settings. These settings will override the default values. For more information, visit [Advanced settings for HTTP monitors](https://dt-url.net/wa034cl).": "Тонко настройте выполнение HTTP-монитора пользовательскими параметрами. Эти настройки переопределяют значения по умолчанию. Подробнее см. [Advanced settings for HTTP monitors](https://dt-url.net/wa034cl).",
    # 4. rum-provider-breakdown
    "Set up rules that define how your applications' downloaded content resources (images, CSS, third party widgets, and more) are displayed and categorized for analysis.": "Настройте правила, определяющие как загружаемые ресурсы контента приложений (изображения, CSS, сторонние виджеты и т.п.) отображаются и категоризируются для анализа.",
    "Dynatrace uses the provider host names of downloaded resources to categorize content resources into either third party resources, CDN resources, or first party resources.": "Dynatrace использует имена хостов провайдеров загруженных ресурсов, чтобы категоризировать ресурсы контента как сторонние, CDN или first-party.",
    "Dynatrace auto-detects over 1,000 content providers out-of-the-box, including Google, Amazon, Facebook, and many more. There's nothing you need to do to set up detection of resources. If you can't find your provider in the list below, you can add it manually. To learn more, visit [Configure 3rd-party and CDN content detection](https://dt-url.net/on02tdo).": "Dynatrace автоматически определяет более 1000 провайдеров контента «из коробки», включая Google, Amazon, Facebook и многих других. Никаких действий для настройки определения ресурсов не требуется. Если вашего провайдера нет в списке ниже, добавьте его вручную. Подробнее см. [Configure 3rd-party and CDN content detection](https://dt-url.net/on02tdo).",
    # 5. process-process-monitoring
    "Dynatrace OneAgent automatically monitors all process groups detected in your environment (processes running during OneAgent installation must be restarted to initiate monitoring).": "Dynatrace OneAgent автоматически мониторит все process group, обнаруженные в окружении (процессы, работающие во время установки OneAgent, должны быть перезапущены для запуска мониторинга).",
    "OneAgent additionally provides deep monitoring for all processes that it can monitor at the request- and PurePath levels.": "OneAgent дополнительно предоставляет deep monitoring для всех процессов, которые он может мониторить на уровне request и PurePath.",
    # 6+10+37. span-attribute / span-event-attribute / resource-attribute — identical deprecation note (no \n+EN+\n match needed via SCHEMA_DESC; handled by paragraph-level replace)
    "We replaced this setting with Allowed attributes (`<your-dynatrace-url>/builtin:attribute-allow-list`) and Attribute data masking (`<your-dynatrace-url>/builtin:attribute-masking`) and migrated your data. This setting will be removed soon.": "Эту настройку заменили на Allowed attributes (`<your-dynatrace-url>/builtin:attribute-allow-list`) и Attribute data masking (`<your-dynatrace-url>/builtin:attribute-masking`), данные перенесены. Эта настройка скоро будет удалена.",
    "Changes in this setting will still be migrated to the new ones, but please be aware that we are not able to migrate certain changes such as attribute deletions.": "Изменения в этой настройке по-прежнему переносятся в новые, но учтите: некоторые изменения, например удаления атрибутов, перенести нельзя.",
    # 7. hyperscaler-authentication-connections-aws
    "Connections to AWS for Dynatrace integrations": "Подключения к AWS для интеграций Dynatrace",
    # 8. logmonitoring-sensitive-data-masking-settings
    "Create rules to mask any information you consider to be sensitive. Masking is done on OneAgent, and no personal data is sent or stored on Dynatrace server.": "Создавайте правила маскирования любой информации, которую считаете чувствительной. Маскирование выполняется на OneAgent, никакие персональные данные не отправляются и не хранятся на сервере Dynatrace.",
    # 9. cloud-kubernetes
    "Connect to Kubernetes or OpenShift for enhanced observability. Learn more about Kubernetes or OpenShift in our documentation.": "Подключайтесь к Kubernetes или OpenShift для расширенной наблюдаемости. Подробнее о Kubernetes или OpenShift см. в нашей документации.",
    # 11. rum-web-request-errors
    "Create capture and detection rules to include request errors in your Apdex calculations or Davis AI problem detection and analysis.": "Создавайте правила захвата и обнаружения, чтобы включить ошибки запросов в расчёты Apdex или в обнаружение и анализ проблем Davis AI.",
    "For more details, see [Configure request errors](https://dt-url.net/13020hh).": "Подробнее см. [Configure request errors](https://dt-url.net/13020hh).",
    # 12-13+16+19-20+22-30. openpipeline-*-pipeline-groups — identical schema desc
    "Contains configuration of a pipeline group": "Содержит конфигурацию pipeline group",
    # 14. ibmmq-queue-managers
    "Dynatrace needs to know the IBM MQ definition of your alias queues, remote queues, and cluster queues for the end-to-end tracing. Without this information, Dynatrace can still trace all requests but producer and consumer services would not be stitched together.": "Dynatrace нужно знать определения IBM MQ для alias-очередей, удалённых очередей и cluster-очередей для end-to-end-трассировки. Без этой информации Dynatrace по-прежнему трассирует все запросы, но producer- и consumer-сервисы не будут сшиты вместе.",
    # 15. synthetic-multiprotocol-performance-thresholds
    "Dynatrace generates a new problem if this synthetic monitor exceeds any of the performance thresholds below in {violatingSamples} of the {samples} most recent request executions at a given location, unless there is an open maintenance window for the synthetic monitor. Multiple locations with {violatingSamples} such violations can be included in a problem. The problem is closed if no performance threshold is violated in the {dealertingSamples} most recent request executions at each of the previously affected locations.": "Dynatrace генерирует новую проблему, если этот синтетический монитор превышает любой из порогов производительности ниже в {violatingSamples} из {samples} последних прогонов запросов в данной локации, если нет открытого maintenance window для синтетического монитора. В одну проблему могут включаться несколько локаций с {violatingSamples} такими нарушениями. Проблема закрывается, если ни один порог производительности не нарушается в {dealertingSamples} последних прогонах запросов в каждой из ранее затронутых локаций.",
    # 16. issue-tracking-integration
    "Query any issue-tracking system to pull issue statistics for monitored entities into Dynatrace for release analysis. For details, see [Issue-tracking integration](https://dt-url.net/releasesissuetracker).": "Опрашивайте любую issue-tracking-систему, чтобы загружать статистику по issue для мониторимых сущностей в Dynatrace для анализа релизов. Подробнее см. [Issue-tracking integration](https://dt-url.net/releasesissuetracker).",
    # 18. endpoint-detection-rules
    "Define rules to detect requests on endpoints based on span attributes defined in the [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields) and custom attributes. Rules are evaluated in order and the first matching rule applies.": "Задайте правила обнаружения запросов на endpoint'ах на основе атрибутов span, определённых в [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields), и пользовательских атрибутов. Правила вычисляются по порядку, применяется первое совпавшее правило.",
    # 19. logmonitoring-log-events — has double-B mojibake `DavisÂ®`
    "Configure log patterns that trigger events for alerting and Davis"
    + RM
    + " analysis. Note that log event detection incurs [billing costs](https://dt-url.net/hk03ulj)": "Настройте паттерны логов, запускающие события для оповещений и анализа Davis"
    + RM
    + ". Учтите: обнаружение событий лога влечёт [billing costs](https://dt-url.net/hk03ulj).",
    # 21. logmonitoring-log-storage-settings
    "You can include and exclude specific log sources for analysis by Dynatrace Log Monitoring. The ingest of log records is based on below rules that use matchers like log path, log levels, process groups, k8s specific selectors and more.": "Включайте и исключайте конкретные источники логов для анализа в Dynatrace Log Monitoring. Ingest записей логов работает по правилам ниже, которые используют сопоставители (log path, log levels, process groups, k8s-специфичные селекторы и т.п.).",
    "To ingest logs, create a new ingest rule. Use suggestions or type in the log source. You can review available log sources on the Process Group Instance screens. You need to define a custom log source if the required log source is not listed.": "Чтобы загружать логи, создайте новое правило ingest. Используйте подсказки или введите источник лога вручную. Доступные источники логов можно посмотреть на экранах Process Group Instance. Если нужного источника нет в списке, задайте пользовательский источник лога.",
    # 22. logmonitoring-log-agent-feature-flags
    "Unlock new features of the Log module in Dynatrace.": "Откройте новые возможности модуля Log в Dynatrace.",
    "For more details, check our [documentation](https://dt-url.net/ib22wr3).": "Подробнее см. [documentation](https://dt-url.net/ib22wr3).",
    # 32. anomaly-detection-disk-rules
    'Dynatrace automatically detects infrastructure-related performance anomalies such as low disk-space conditions. Use these settings (and the Infrastructure settings (`<your-dynatrace-url>//ui/settings/builtin:anomaly-detection.infrastructure-disks "Visit Infrastructure anomaly detection settings"`)) to configure detection sensitivity, set alert thresholds, or disable alerting for disks.': 'Dynatrace автоматически обнаруживает инфраструктурные аномалии производительности, например нехватку места на диске. Используйте эти настройки (и настройки Infrastructure (`<your-dynatrace-url>//ui/settings/builtin:anomaly-detection.infrastructure-disks "Visit Infrastructure anomaly detection settings"`)) для настройки чувствительности обнаружения, задания порогов оповещений или отключения оповещений по дискам.',
    # 33. rum-ip-mappings
    "If you don't see performance data for some of your customers on the world map, it may be because those customers have private IP addresses. You can map such private IP addresses to geographic regions to make them visible on the map. You can even override settings for customer IP addresses if necessary for mapping purposes.": "Если на карте мира нет данных производительности для части клиентов, причина может быть в том, что у этих клиентов приватные IP-адреса. Можно сопоставить такие приватные IP-адреса с географическими регионами, чтобы они стали видны на карте. При необходимости можно даже переопределить настройки для IP-адресов клиентов.",
    "Granularity of regional performance analysis increases as the number of detected user requests goes up in a specific region (continent, country, state, or city). You can even override auto-detected IP addresses if necessary to improve mapping accuracy.": "Гранулярность регионального анализа производительности растёт по мере увеличения количества обнаруженных пользовательских запросов в конкретном регионе (континент, страна, штат или город). При необходимости можно переопределить автоматически обнаруженные IP-адреса для повышения точности сопоставления.",
    "Dynatrace uses an IP address to geolocation mapping service offered by [MaxMind GeoIP2](https://dt-url.net/6a21pxd). The names for regions and cities are following the [GeoNames database](https://dt-url.net/tz41pwz).": "Dynatrace использует сервис сопоставления IP-адресов с геолокацией от [MaxMind GeoIP2](https://dt-url.net/6a21pxd). Имена регионов и городов следуют [GeoNames database](https://dt-url.net/tz41pwz).",
    "To find out which names and IDs are used out of the box, use the geographic regions REST API (`<your-dynatrace-url>//rest-api-doc/index.jsp?urls.primaryName=Environment%20API%20v2#/Geographic%20regions`).": "Чтобы узнать какие имена и ID используются «из коробки», воспользуйтесь geographic regions REST API (`<your-dynatrace-url>//rest-api-doc/index.jsp?urls.primaryName=Environment%20API%20v2#/Geographic%20regions`).",
    # 34. service-detection-rules
    "Define rules to detect and name services based on resource attributes defined in the [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields) and custom attributes. Rules are evaluated in order and the first matching rule applies.": "Задайте правила обнаружения и именования сервисов на основе атрибутов ресурсов, определённых в [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields), и пользовательских атрибутов. Правила вычисляются по порядку, применяется первое совпавшее правило.",
    # 35. rum-web-key-performance-metric-xhr-actions
    "Select a key performance metric and set the Tolerating and Frustrated performance thresholds to [refine the Apdex calculations](https://dt-url.net/apdex-thresholds) for this application.": "Выберите ключевую метрику производительности и задайте пороги Tolerating и Frustrated, чтобы [refine the Apdex calculations](https://dt-url.net/apdex-thresholds) для этого приложения.",
    # 36. failure-detection-environment-rules
    "Configure rules which services certain failure detection parameters (`<your-dynatrace-url>//ui/settings/builtin:failure-detection.environment.parameters`) should apply to. For more information please refer to [Failure detection settings](https://dt-url.net/7v034gp).": "Настройте правила, к каким сервисам должны применяться конкретные параметры обнаружения сбоев (`<your-dynatrace-url>//ui/settings/builtin:failure-detection.environment.parameters`). Подробнее см. [Failure detection settings](https://dt-url.net/7v034gp).",
    "These settings are not applied to [Unified services](https://dt-url.net/gy03cmt).": "Эти настройки не применяются к [Unified services](https://dt-url.net/gy03cmt).",
}

# Parameter table col-1 labels (translated when present).
PARAM_LABEL = {
    # Common cross-batch
    "Enabled": "Включено",
    "Name": "Имя",
    "Type": "Тип",
    "URL": "URL",
    "Description": "Описание",
    "Pattern": "Шаблон",
    "Key": "Ключ",
    "Value": "Значение",
    "Source": "Источник",
    "Matcher": "Сопоставитель",
    "Matchers": "Сопоставители",
    "Rule": "Правило",
    "Rule name": "Имя правила",
    "Rule action": "Действие правила",
    "Property": "Свойство",
    "Mode": "Режим",
    "Operator": "Оператор",
    "Active": "Активно",
    "Attribute": "Атрибут",
    "Masking": "Маскирование",
    "Color": "Цвет",
    "Technology": "Технология",
    "Composition": "Композиция",
    # 1. process-visibility
    "Enable Process instance snapshots": "Включить Process instance snapshots",
    "Reported processes limit": "Лимит сообщаемых процессов",
    # 2. span-context-propagation
    "Context Propagation Rule": "Правило распространения контекста",
    "Comparison Type": "Тип сравнения",
    "Case sensitive": "С учётом регистра",
    # 3. synthetic-http-advanced-execution
    "Request timeout (ms)": "Таймаут запроса (мс)",
    "Connect timeout (ms)": "Таймаут подключения (мс)",
    "Maximum header size (B)": "Максимальный размер заголовка (B)",
    "Monitor execution timeout (ms)": "Таймаут выполнения монитора (мс)",
    "Script execution timeout (ms)": "Таймаут выполнения скрипта (мс)",
    "Maximum request body size (B)": "Максимальный размер тела запроса (B)",
    "Maximum custom script size (B)": "Максимальный размер пользовательского скрипта (B)",
    "Maximum response body size (B)": "Максимальный размер тела ответа (B)",
    "Maximum size of response body read by custom script (B)": "Максимальный размер тела ответа, читаемого пользовательским скриптом (B)",
    "DNS query timeout (ms)": "Таймаут DNS-запроса (мс)",
    # 4. rum-provider-breakdown
    "Resource name": "Имя ресурса",
    "Resource type": "Тип ресурса",
    "Specify an URL for the provider's brand icon": "Укажите URL иконки бренда провайдера",
    "Domain name pattern": "Шаблон доменного имени",
    "Submit this provider-pattern to improve auto-detection": "Отправить шаблон провайдера для улучшения автоопределения",
    "Type your domain name pattern": "Введите шаблон доменного имени",
    # 5. process-process-monitoring
    "Enable automatic deep monitoring": "Включить автоматический deep monitoring",
    # 7. hyperscaler-authentication-connections-aws
    "Connection Type": "Тип подключения",
    "AWS IAM Role ARN": "ARN роли AWS IAM",
    "Consumers": "Потребители",
    # 8. logmonitoring-sensitive-data-masking-settings
    "Search expression": "Поисковое выражение",
    "Masking type": "Тип маскирования",
    "Replacement": "Замена",
    # 9. cloud-kubernetes
    "Connect containerized ActiveGate to local Kubernetes API endpoint": "Подключить контейнеризованный ActiveGate к локальному endpoint Kubernetes API",
    "Kubernetes cluster ID": "ID Kubernetes-кластера",
    "Kubernetes API URL Target": "URL Kubernetes API",
    "Kubernetes Bearer Token": "Bearer-токен Kubernetes",
    "ActiveGate Group": "Группа ActiveGate",
    "Require valid certificates for communication with API server (recommended)": "Требовать валидные сертификаты для связи с API-сервером (рекомендуется)",
    "Verify hostname in certificate against Kubernetes API URL": "Проверять имя хоста в сертификате с URL Kubernetes API",
    # 11. rum-web-request-errors
    "Ignore request errors in Apdex calculations": "Игнорировать ошибки запросов в расчётах Apdex",
    "Match by error code": "Сопоставление по коду ошибки",
    "Match by errors that have failed image requests": "Сопоставление по ошибкам с failed image requests",
    "Match by errors that have CSP violations": "Сопоставление по ошибкам с CSP-нарушениями",
    "Filter settings": "Настройки фильтра",
    "Capture settings": "Настройки захвата",
    "Filter by URL": "Фильтр по URL",
    "Capture this error": "Захватывать эту ошибку",
    "Include error in Apdex calculations": "Включать ошибку в расчёты Apdex",
    "Include error in Davis AI problem detection and analysis": "Включать ошибку в обнаружение и анализ проблем Davis AI",
    # 12+ openpipeline-*-pipeline-groups (12 files, identical)
    "Display name": "Отображаемое имя",
    "Pipelines wrapped by this group": "Pipeline'ы, обёрнутые этой группой",
    "stage configuration of the member pipelines": "Конфигурация stage для pipeline'ов-членов",
    "Stage configuration type": "Тип конфигурации stage",
    "include stages": "Включаемые stage",
    "exclude stages": "Исключаемые stage",
    "Placeholder for the wrapped pipeline": "Placeholder для обёрнутого pipeline",
    "Pipeline ID": "ID pipeline",
    "stage configuration for this pipelines": "Конфигурация stage для этих pipeline'ов",
    # 14. ibmmq-queue-managers
    "Queue manager name": "Имя менеджера очередей",
    "Clusters": "Кластеры",
    "Alias queues": "Alias-очереди",
    "Remote queues": "Удалённые очереди",
    "Cluster queues": "Cluster-очереди",
    "Alias queue name": "Имя alias-очереди",
    "Base queue name": "Имя базовой очереди",
    "Cluster visibility": "Видимость в кластере",
    "Local queue name": "Имя локальной очереди",
    "Remote queue name": "Имя удалённой очереди",
    "Remote queue manager name": "Имя удалённого менеджера очередей",
    "Cluster visibilities": "Видимости в кластерах",
    # 15. synthetic-multiprotocol-performance-thresholds
    "Generate a problem and send an alert on performance threshold violations": "Генерировать проблему и отправлять оповещение при нарушении порогов производительности",
    "Performance thresholds": "Пороги производительности",
    "Threshold (in ms)": "Порог (в мс)",
    "Step index": "Индекс шага",
    "Aggregation type": "Тип агрегации",
    "Number of violating request executions in analyzed sliding window": "Количество нарушающих прогонов запросов в анализируемом скользящем окне",
    "Number of request executions in analyzed sliding window (sliding window size)": "Количество прогонов запросов в анализируемом скользящем окне (размер окна)",
    "Number of most recent non-violating request executions that closes the problem": "Количество последних ненарушающих прогонов запросов, закрывающих проблему",
    # 16. issue-tracking-integration
    "Issue label": "Метка issue",
    "Issue query": "Запрос issue",
    "Issue type": "Тип issue",
    "Issue-tracking system": "Issue-tracking-система",
    "Target URL": "Целевой URL",
    "Username": "Имя пользователя",
    "Password": "Пароль",
    "Token": "Токен",
    # 18. endpoint-detection-rules
    "Matching condition": "Условие сопоставления",
    "If condition matches": "Если условие совпало",
    "Endpoint name template": "Шаблон имени endpoint",
    # 19. logmonitoring-log-events
    "Summary": "Сводка",
    "Event template": "Шаблон события",
    "Title": "Заголовок",
    "Event type": "Тип события",
    "Allow merge": "Разрешить merge",
    "Properties": "Свойства",
    # 21. logmonitoring-log-storage-settings
    "Send to storage": "Отправлять в storage",
    # 22. logmonitoring-log-agent-feature-flags
    "Collect all container logs": "Собирать все логи контейнеров",
    "Collect Journald logs": "Собирать логи Journald",
    "Support for structured data in Windows Event Logs": "Поддержка структурированных данных в Windows Event Logs",
    "Add IIS Application Pool context to Logs": "Добавлять контекст IIS Application Pool в логи",
    # 32. anomaly-detection-disk-rules
    "Metric to alert on": "Метрика для оповещения",
    "Alert if lower than": "Оповестить, если меньше чем",
    "Alert if higher than": "Оповестить, если больше чем",
    "Sample limit": "Лимит выборки",
    "Disk name filter": "Фильтр по имени диска",
    "Host filter": "Фильтр по хостам",
    "Minimum number of violating samples": "Минимальное количество нарушающих выборок",
    "... within the last": "...в последних",
    "Matching text": "Текст для сопоставления",
    # 33. rum-ip-mappings
    "Single IP or IP range start address": "Один IP или начальный адрес диапазона",
    "IP range end": "Конец диапазона IP",
    "Country": "Страна",
    "Region": "Регион",
    "City": "Город",
    "Latitude": "Широта",
    "Longitude": "Долгота",
    # 34. service-detection-rules
    "Service name template": "Шаблон имени сервиса",
    "Additional service detection attributes": "Дополнительные атрибуты обнаружения сервиса",
    # 35. rum-web-key-performance-metric-xhr-actions
    "Key performance metric": "Ключевая метрика производительности",
    "Key performance metric thresholds": "Пороги ключевой метрики производительности",
    "Fallback metric thresholds": "Пороги fallback-метрики",
    "Tolerating threshold": "Порог Tolerating",
    "Frustrated threshold": "Порог Frustrated",
    "Tolerating threshold [sec]": "Порог Tolerating [сек]",
    "Frustrated threshold [sec]": "Порог Frustrated [сек]",
    # 36. failure-detection-environment-rules
    "Rule description": "Описание правила",
    "Failure detection parameters": "Параметры обнаружения сбоев",
    "Conditions": "Условия",
    "Condition to check the attribute against": "Условие проверки атрибута",
    "Predicate type": "Тип предиката",
    "Names": "Имена",
    "Service types": "Типы сервисов",
    "Management zones": "Management zones",
    "Tags (exact match)": "Теги (точное совпадение)",
    "Tag keys": "Ключи тегов",
    # 37. resource-attribute
    "Attribute key allow-list": "Allow-list ключей атрибутов",
    "Attribute key": "Ключ атрибута",
}

# Parameter table col-3 descriptions (when not just `-` and not enum-tail).
PARAM_DESC = {
    # 1. process-visibility
    "The maximum amount of processes that host may report is **100**": "Максимальное количество процессов, которое может сообщать хост: **100**",
    # 2. span-context-propagation
    "evaluated at context injection": "вычисляется при инжекции контекста",
    "affects value": "влияет на значение",
    "affects value and key": "влияет на значение и ключ",
    # 3. synthetic-http-advanced-execution
    "Supported values are between 1 000 and 60 000 ms": "Поддерживаемые значения: от 1 000 до 60 000 мс",
    "Supported values are between 10 240 and 61 440 bytes": "Поддерживаемые значения: от 10 240 до 61 440 байт",
    "Supported values are between 10 000 and 300 000 ms": "Поддерживаемые значения: от 10 000 до 300 000 мс",
    "Supported values are between 1 000 and 10 000 ms": "Поддерживаемые значения: от 1 000 до 10 000 мс",
    "Supported values are between 10 240 and 102 400 bytes": "Поддерживаемые значения: от 10 240 до 102 400 байт",
    "Supported values are between 51 200 and 20 971 520 bytes": "Поддерживаемые значения: от 51 200 до 20 971 520 байт",
    # 4. rum-provider-breakdown
    "Use a ends-with pattern for this content provider's domain": "Используйте шаблон ends-with для домена этого провайдера контента",
    "Send the patterns of this provider to Dynatrace to help us improve 3rd-party detection.": "Отправить шаблоны этого провайдера в Dynatrace, чтобы помочь улучшить 3rd-party-обнаружение.",
    # 5. process-process-monitoring — large prose with triple-mojibake `thatâ€™s`
    "By disabling automatic deep monitoring the Dynatrace OneAgent will only deep monitor processes that are covered by a respective deep monitoring rule or where monitoring is enabled explicitly. Disabling only works if all installed Agents have version 1.123 or higher.  With automatic monitoring enabled, you can create rules that define exceptions to automatic process detection and monitoring. With automatic monitoring disabled, you can define rules that identify specific processes that should be monitored. Rules are applied in the order listed in the custom and built-in process monitoring rules settings. This means that you can construct complex operations for fine-grain control over the processes that are monitored in your environment. For example, you might define an inclusion rule that"
    + Q
    + 's followed by an exclusion rule covering the same process. Once created, monitoring rules can be enabled/disabled at any time. The rules will only take effect after restart of the processes in question. Alternatively, you can disable automatic monitoring entirely and instead define "Include" rules for those processes you want to monitor.': 'Отключив автоматический deep monitoring, Dynatrace OneAgent будет deep-мониторить только те процессы, которые покрыты соответствующим правилом deep monitoring или для которых мониторинг включён явно. Отключение работает, только если все установленные агенты имеют версию 1.123 или выше.  При включённом автоматическом мониторинге можно создавать правила, описывающие исключения из автоматического обнаружения и мониторинга процессов. При отключённом автоматическом мониторинге можно задавать правила, идентифицирующие конкретные процессы, которые надо мониторить. Правила применяются в том порядке, в котором они перечислены в настройках пользовательских и встроенных правил мониторинга процессов. Это позволяет конструировать сложные операции для тонкого контроля над процессами, мониторимыми в окружении. Например, можно задать правило включения, за которым следует правило исключения, покрывающее тот же процесс. После создания правила мониторинга можно включать и выключать в любой момент. Правила вступают в силу только после перезапуска соответствующих процессов. Альтернативно можно полностью отключить автоматический мониторинг и вместо этого задать правила "Include" для тех процессов, которые надо мониторить.',
    # 6+10+37. span-attribute / span-event-attribute / resource-attribute — identical Masking enum-prefix
    "Key of the span attribute to store": "Ключ атрибута span, который надо хранить",
    "Key of the span event attribute to store": "Ключ атрибута события span, который надо хранить",
    "If this is true, the value of the specified key is stored.": "Если true, значение указанного ключа сохраняется.",
    "The attribute key **service.name** and attribute keys in the namespace **dt.** are always allow-listed.": "Ключ атрибута **service.name** и ключи атрибутов в namespace **dt.** всегда в allow-list.",
    "If this attribute contains confidential data, turn on masking to conceal its value from users  Introduce more granular control over the visibility of attribute values.  Choose **Do not mask** to allow every user to see the actual value and use it in defining other configurations.  Choose **Mask entire value** to hide the whole value of this attribute from everyone who does not have 'View sensitive request data' permission. These attributes can't be used to define other configurations. Choose **Mask only confidential data** to apply automatic masking strategies to your data. These strategies include, for example, credit card numbers, IBAN, IPs, email-addresses, etc. It may not be possible to recognize all sensitive data so please always make sure to verify that sensitive data is actually masked. If sensitive data is not recognized, please use **Mask entire value** instead. Users with 'View sensitive request data' permission will be able to see the entire value, others only the non-sensitive parts. These attributes can't be used to define other configurations.": "Если этот атрибут содержит конфиденциальные данные, включите маскирование, чтобы скрыть его значение от пользователей.  Внедрите более гранулярный контроль над видимостью значений атрибутов.  Выберите **Do not mask**, чтобы все пользователи видели реальное значение и могли использовать его в других конфигурациях.  Выберите **Mask entire value**, чтобы полностью скрыть значение этого атрибута от всех, у кого нет права 'View sensitive request data'. Такие атрибуты нельзя использовать для других конфигураций. Выберите **Mask only confidential data**, чтобы применить автоматические стратегии маскирования. Стратегии охватывают, например, номера кредитных карт, IBAN, IP, email-адреса и т.п. Распознать все чувствительные данные может быть невозможно, поэтому всегда проверяйте, что чувствительные данные действительно замаскированы. Если чувствительные данные не распознаны, используйте **Mask entire value**. Пользователи с правом 'View sensitive request data' увидят значение целиком; остальные только нечувствительные части. Такие атрибуты нельзя использовать для других конфигураций.",
    # 7. hyperscaler-authentication-connections-aws
    "The name of the connection": "Имя подключения",
    "AWS Authentication mechanism to be used by the connection": "Механизм аутентификации AWS, используемый подключением",
    "The ARN of the AWS role that should be assumed": "ARN роли AWS, которую следует принять",
    "Dynatrace integrations that can use this connection": "Интеграции Dynatrace, которые могут использовать это подключение",
    # 8. logmonitoring-sensitive-data-masking-settings
    "Maximum one capture group is allowed. If none was given, the whole expression will be treated as a capture group.": "Допускается максимум одна capture-группа. Если она не задана, всё выражение трактуется как capture-группа.",
    # 9. cloud-kubernetes
    "Renaming the cluster breaks configurations that are based on its name (e.g., management zones, and alerting).": "Переименование кластера ломает конфигурации, опирающиеся на его имя (например, management zones и alerting).",
    "For more information on local Kubernetes API monitoring, see the [documentation](https://dt-url.net/6q62uep).  Enable this toggle when the ActiveGate is deployed to the same Kubernetes clusters you want to monitor. Disable it if you want to monitor a different Kubernetes cluster.": "Подробнее о мониторинге локального Kubernetes API см. [documentation](https://dt-url.net/6q62uep).  Включите этот переключатель, если ActiveGate развёрнут в тех же Kubernetes-кластерах, которые вы хотите мониторить. Отключите, если хотите мониторить другой Kubernetes-кластер.",
    "Unique ID of the cluster, the containerized ActiveGate is deployed to. Defaults to the UUID of the kube-system namespace. The cluster ID of containerized ActiveGates is shown on the Deployment status screen.": "Уникальный ID кластера, в котором развёрнут контейнеризованный ActiveGate. По умолчанию равен UUID namespace kube-system. ID кластера контейнеризованного ActiveGate показан на экране Deployment status.",
    'Get the API URL for [Kubernetes](https://dt-url.net/kz23snj "Kubernetes") or [OpenShift](https://dt-url.net/d623xgw "OpenShift").': 'Получите API URL для [Kubernetes](https://dt-url.net/kz23snj "Kubernetes") или [OpenShift](https://dt-url.net/d623xgw "OpenShift").',
    'Create a bearer token for [Kubernetes](https://dt-url.net/og43szq "Kubernetes") or [OpenShift](https://dt-url.net/7l43xtp "OpenShift").': 'Создайте bearer-токен для [Kubernetes](https://dt-url.net/og43szq "Kubernetes") или [OpenShift](https://dt-url.net/7l43xtp "OpenShift").',
    # 11. rum-web-request-errors
    "[View more details](https://dt-url.net/hd580p2k)": "[View more details](https://dt-url.net/hd580p2k)",
    # 14. ibmmq-queue-managers
    "Name of the cluster(s) this queue manager is part of": "Имя кластера/кластеров, в который входит этот менеджер очередей",
    "Name of the cluster(s) this alias should be visible in": "Имя кластера/кластеров, в которых должен быть виден этот alias",
    "Name of the cluster(s) this local definition of the remote queue should be visible in": "Имя кластера/кластеров, в которых должно быть видно это локальное определение удалённой очереди",
    "Name of the cluster(s) this local queue should be visible in": "Имя кластера/кластеров, в которых должна быть видна эта локальная очередь",
    # 16. issue-tracking-integration
    "Set a label to identify these issues, for example, `release_blocker` or `non-critical`": "Задайте метку для идентификации этих issue, например `release_blocker` или `non-critical`",
    "You can use the following placeholders to automatically insert values from the **Release monitoring** page in your query: `{NAME}`, `{VERSION}`, `{STAGE}`, `{PRODUCT}`.": "Можно использовать следующие placeholder'ы, чтобы автоматически подставлять значения со страницы **Release monitoring** в запрос: `{NAME}`, `{VERSION}`, `{STAGE}`, `{PRODUCT}`.",
    "Select the issue type to be displayed.": "Выберите тип отображаемой issue.",
    "Select the issue-tracking system you want to query.": "Выберите issue-tracking-систему, которую хотите опрашивать.",
    "For Jira, use the base URL (for example, https://jira.yourcompany.com); for GitHub, use the repository URL (for example, https://github.com/org/repo); for GitLab, use the specific project API for a single project (for example, https://gitlab.com/api/v4/projects/:projectId), and the specific group API for a multiple projects (for example, https://gitlab.com/api/v4/groups/:groupId); for ServiceNow, use your company instance URL (for example, https://yourinstance.service-now.com/)": "Для Jira используйте базовый URL (например, https://jira.yourcompany.com); для GitHub URL репозитория (например, https://github.com/org/repo); для GitLab project-specific API для одного проекта (например, https://gitlab.com/api/v4/projects/:projectId) и group-specific API для нескольких проектов (например, https://gitlab.com/api/v4/groups/:groupId); для ServiceNow URL вашего инстанса (например, https://yourinstance.service-now.com/)",
    # 18. endpoint-detection-rules + 34. service-detection-rules
    "If enabled, the rule will be evaluated.": "Если включено, правило будет вычисляться.",
    "Limits the scope of the endpoint detection rule using [DQL matcher](https://dt-url.net/l603wby) conditions on span and resource attributes.  A rule is applied only if the condition matches, otherwise the ruleset evaluation continues.  If empty, the condition will always match.": "Ограничивает область правила обнаружения endpoint через условия [DQL matcher](https://dt-url.net/l603wby) на атрибутах span и ресурсов.  Правило применяется только если условие совпало, иначе вычисление набора правил продолжается.  Если поле пустое, условие всегда совпадает.",
    "Specify attribute placeholders in curly braces, e.g. {http.route} or {rpc.method}.  Attribute value placeholders should be specified in curly braces, e.g. {http.route}, {rpc.method}. All attributes used in the placeholder are required for the rule to apply. If any of them is missing, the rule will not be applied and ruleset evaluation continues.  If the resolved endpoint name on a given span is empty, the request will be ignored.": "Укажите placeholder'ы атрибутов в фигурных скобках, например {http.route} или {rpc.method}.  Placeholder'ы значений атрибутов следует указывать в фигурных скобках, например {http.route}, {rpc.method}. Все атрибуты, использованные в placeholder, обязательны для применения правила. Если хотя бы один отсутствует, правило не применяется, и вычисление набора правил продолжается.  Если разрешённое имя endpoint на данном span пустое, запрос игнорируется.",
    "Limits the scope of the service detection rule using [DQL matcher](https://dt-url.net/l603wby) conditions on resource attributes.  A rule is applied only if the condition matches, otherwise the ruleset evaluation continues.  If empty, the condition will always match.": "Ограничивает область правила обнаружения сервиса через условия [DQL matcher](https://dt-url.net/l603wby) на атрибутах ресурсов.  Правило применяется только если условие совпало, иначе вычисление набора правил продолжается.  Если поле пустое, условие всегда совпадает.",
    "Specify resource attribute placeholders in curly braces, e.g. {service.name} or {k8s.workload.name}.  All attributes used in the placeholder are required for the rule to apply. If any of them is missing, the rule will not be applied and ruleset evaluation continues.  All resolved attribute values contribute to the final service ID.": "Укажите placeholder'ы атрибутов ресурсов в фигурных скобках, например {service.name} или {k8s.workload.name}.  Все атрибуты, использованные в placeholder, обязательны для применения правила. Если хотя бы один отсутствует, правило не применяется, и вычисление набора правил продолжается.  Все разрешённые значения атрибутов вносят вклад в финальный ID сервиса.",
    "Add resource attribute keys (e.g. service.namespace or k8s.workload.kind) that also detect unique services but are not included in the displayed service name.  Attributes specified here are required to apply the rule. If any of them is missing, the rule will not be applied and ruleset evaluation continues.  All attribute values contribute to the final service ID.": "Добавьте ключи атрибутов ресурсов (например service.namespace или k8s.workload.kind), которые также обнаруживают уникальные сервисы, но не включаются в отображаемое имя сервиса.  Указанные здесь атрибуты обязательны для применения правила. Если хотя бы один отсутствует, правило не применяется, и вычисление набора правил продолжается.  Все значения атрибутов вносят вклад в финальный ID сервиса.",
    # 19. logmonitoring-log-events — has Davis double-mojibake
    "The textual summary of the log event entry": "Текстовая сводка записи log event",
    "The title of the event to trigger. Type '{' for placeholder hints.": "Заголовок события, которое надо запустить. Введите '{' для подсказок по placeholder.",
    "The description of the event to trigger. Type '{' for placeholder hints.": "Описание события, которое надо запустить. Введите '{' для подсказок по placeholder.",
    "The event type to trigger.": "Тип события, которое надо запустить.",
    "Davis"
    + RM
    + " AI will try to merge this event into existing problems, otherwise a new problem will always be created.": "Davis"
    + RM
    + " AI попытается слить это событие в существующие проблемы, иначе всегда будет создаваться новая проблема.",
    "Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2](https://dt-url.net/9622g1w).": "Набор дополнительных key-value-свойств, прикрепляемых к запущенному событию. Доступные ключи свойств можно получить через [Events API v2](https://dt-url.net/9622g1w).",
    "Type 'dt.' for key hints.": "Введите 'dt.' для подсказок по ключам.",
    "Type '{' for placeholder hints.": "Введите '{' для подсказок по placeholder.",
    # 21. logmonitoring-log-storage-settings
    "If `true` matching logs will be included in storage. If `false` matching logs will be excluded from storage.": "Если `true`, совпавшие логи включаются в storage. Если `false`, совпавшие логи исключаются из storage.",
    # 22. logmonitoring-log-agent-feature-flags
    'Enable OneAgent to collect all container logs in Kubernetes environments. This setting enables:  * Detection and collection of logs from short-lived containers and processes in Kubernetes. * Detection and collection of logs from any processes in containers in Kubernetes. Up until now only processes detected by OneAgent are covered with the Log module. * Log events decoration according to semantic dictionary.   **Note:** The matcher "Deployment name" in the log sources configuration will be ignored and needs to be replaced with "Workload name", requires **Dynatrace Operator 1.4.2+**.  For more details, check our [documentation](https://dt-url.net/jn02ey0).': 'Разрешить OneAgent собирать все логи контейнеров в Kubernetes-окружениях. Эта настройка включает:  * Обнаружение и сбор логов с короткоживущих контейнеров и процессов в Kubernetes. * Обнаружение и сбор логов с любых процессов в контейнерах в Kubernetes. До сих пор модулем Log покрывались только процессы, обнаруженные OneAgent. * Декорирование log events согласно semantic dictionary.   **Примечание:** сопоставитель "Deployment name" в конфигурации источников лога будет игнорироваться, его надо заменить на "Workload name". Требуется **Dynatrace Operator 1.4.2+**.  Подробнее см. [documentation](https://dt-url.net/jn02ey0).',
    "Enable OneAgent to collect logs from Journald on Linux systems. This setting enables:  * Detection and to have logs ingested matching ingest rule is required.": "Разрешить OneAgent собирать логи из Journald на Linux-системах. Эта настройка включает:  * Обнаружение; для приёма логов требуется совпавшее правило ingest.",
    "Enable OneAgent to collect data from Event Logs in the User Data and Event Data sections.": "Разрешить OneAgent собирать данные из Event Logs в секциях User Data и Event Data.",
    "Enable OneAgent to assign logs to the appropriate IIS application pools when an unambiguous IIS configuration is detected.": "Разрешить OneAgent привязывать логи к соответствующим IIS application pool при однозначно определённой IIS-конфигурации.",
    # 32. anomaly-detection-disk-rules
    "Only alert if the threshold was violated in at least *n* of the last *m* samples": "Оповещать только если порог был нарушен минимум в *n* из последних *m* выборок",
    "Only apply to disks whose name matches": "Применять только к дискам с совпавшим именем",
    "Only apply to hosts that have the following tags": "Применять только к хостам с указанными тегами",
    # 33. rum-ip-mappings
    "The country code of the location.  Use the alpha-2 code of the [ISO 3166-2 standard](https://dt-url.net/iso3166-2), (for example, `AT` for Austria or `PL` for Poland).": "Код страны локации.  Используйте alpha-2-код [ISO 3166-2 standard](https://dt-url.net/iso3166-2) (например, `AT` для Австрии или `PL` для Польши).",
    "The region code of the location.  For the [USA](https://dt-url.net/iso3166us) or [Canada](https://dt-url.net/iso3166ca) use ISO 3166-2 state codes without `US-` or `CA-` prefix.  For the rest of the world use [FIPS 10-4 codes](https://dt-url.net/fipscodes) without country prefix.": "Код региона локации.  Для [USA](https://dt-url.net/iso3166us) и [Canada](https://dt-url.net/iso3166ca) используйте коды штатов ISO 3166-2 без префиксов `US-` или `CA-`.  Для остального мира используйте [FIPS 10-4 codes](https://dt-url.net/fipscodes) без префикса страны.",
    "The city name of the location.": "Имя города локации.",
    # 35. rum-web-key-performance-metric-xhr-actions
    "Set the Tolerating and Frustrated performance thresholds for this action type.": "Задайте пороги производительности Tolerating и Frustrated для этого типа действия.",
    "If the selected key performance metric is not detected, the **User action duration** metric is used instead.": "Если выбранная ключевая метрика производительности не обнаружена, используется метрика **User action duration**.",
    "If the key performance metric is below this value, the action is assigned to the Satisfied performance zone.": "Если ключевая метрика производительности ниже этого значения, действие относится к зоне производительности Satisfied.",
    "If the key performance metric is above this value, the action is assigned to the Frustrated performance zone.": "Если ключевая метрика производительности выше этого значения, действие относится к зоне производительности Frustrated.",
    "If **User action duration** is below this value, the action is assigned to the Satisfied performance zone.": "Если **User action duration** ниже этого значения, действие относится к зоне производительности Satisfied.",
    "If **User action duration** is above this value, the action is assigned to the Frustrated performance zone.": "Если **User action duration** выше этого значения, действие относится к зоне производительности Frustrated.",
    # 36. failure-detection-environment-rules
    "The attribute to be checked.": "Проверяемый атрибут.",
}

# Structural canon (shared with L4-AG.1a.1-5 / L4-AF).
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
    # Empty label (col-1 starts with backtick) is allowed; just translate cdesc.
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
        print("%-65s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY:", "OK" if bad == 0 else f"BAD ({bad})")
