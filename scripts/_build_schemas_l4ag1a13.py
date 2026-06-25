# -*- coding: utf-8 -*-
"""L4-AG.1a.13 builder: 14 builtin-*.md schema-table files (7.5-11.3 KB).

Состав батча:
  - alerting: maintenance-window, profile
  - anomaly-detection-infrastructure: aws, vmware
  - anomaly-detection-kubernetes-workload
  - failure-detection-rulesets
  - monitoredentities-generic-type
  - process: built-in-process-monitoring-rule, group-detection-flags,
    grouping-rules
  - service-detection: external-web-request, external-web-service,
    full-web-request, full-web-service

Канон L4-AG.1a.12 (chr() для triple-mojibake, _normalize чистит mojibake-BOM
вне зависимости от позиции, empty-label rows разрешены в _param_row).

Mojibake-аудит EN:
  - BOMJ `i»?` встречается в 10/14 файлов внутри hyperlink-текстов
    ([documentation](https://...)i»?), чистится `_normalize`.
  - triple-en-dash `i` (c3 a2 c2 80 c2 93) 4 в process-grouping-rules
    (DetectionCondition $contains/$eq/$prefix/$suffix bullet-separator).
  - Иных типов нет.

Twin-quad pair: 4 service-detection файла консолидируют общие nested
(condition, serviceIdContributor, transformationSet, contextRoot,
contextIdContributor, valueOverride, transformation, reducedTransformation).

Особый файл: builtin-process-built-in-process-monitoring-rule.md содержит
80 параметров вида "Do (not )?monitor processes if X `-N`" + "Rule id: N";
обрабатывается отдельной regex-функцией `_process_rule_row`.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-alerting-maintenance-window.md",
    "builtin-alerting-profile.md",
    "builtin-anomaly-detection-infrastructure-aws.md",
    "builtin-anomaly-detection-infrastructure-vmware.md",
    "builtin-anomaly-detection-kubernetes-workload.md",
    "builtin-failure-detection-rulesets.md",
    "builtin-monitoredentities-generic-type.md",
    "builtin-process-built-in-process-monitoring-rule.md",
    "builtin-process-group-detection-flags.md",
    "builtin-process-grouping-rules.md",
    "builtin-service-detection-external-web-request.md",
    "builtin-service-detection-external-web-service.md",
    "builtin-service-detection-full-web-request.md",
    "builtin-service-detection-full-web-service.md",
]

# Triple-en-dash mojibake (used in process-grouping-rules bullet-separator):
# c3 a2 c2 80 c2 93 = U+00E2 U+0080 U+0093 = visible `i`
TM_ENDASH = chr(0xE2) + chr(0x80) + chr(0x93)

DISPLAY_NAME = {
    "Maintenance windows": "Maintenance windows",
    "Problem alerting profiles": "Профили оповещений о problem",
    "Anomaly detection for classic AWS services": "Обнаружение аномалий для классических AWS-сервисов",
    "Anomaly detection for VMware": "Обнаружение аномалий для VMware",
    "Kubernetes workload anomaly detection": "Обнаружение аномалий Kubernetes workload",
    "Failure detection": "Обнаружение сбоев",
    "Generic types": "Generic types",
    "Built-in process monitoring rules": "Встроенные правила мониторинга процессов",
    "Built-in detection rules": "Встроенные правила обнаружения",
    "Process grouping rules": "Правила группировки процессов",
    "Service detection rules for External Web Requests": "Правила обнаружения сервисов для External Web Requests",
    "Service detection rules for External Web Services": "Правила обнаружения сервисов для External Web Services",
    "Service detection rules for Full Web Requests": "Правила обнаружения сервисов для Full Web Requests",
    "Service detection rules for Full Web Services": "Правила обнаружения сервисов для Full Web Services",
}

SCHEMA_DESC = {
    # alerting-maintenance-window (BOMJ чистится перед матчем)
    'Maintenance windows are typically planned, recurring periods of system downtime during which your DevOps team can perform preventative maintenance and system upgrades outside of peak traffic hours. [Documentation](https://dt-url.net/5902ho9 "How to define a maintenance window")': 'Maintenance windows, как правило, это плановые повторяющиеся периоды downtime, в течение которых DevOps-команда выполняет профилактическое обслуживание и системные обновления вне часов пиковой нагрузки. [Documentation](https://dt-url.net/5902ho9 "How to define a maintenance window")',
    "To avoid having Dynatrace report on any performance anomalies that may result from such events, set up maintenance windows below that correspond with your organization's maintenance window schedule.": "Чтобы Dynatrace не сообщал об аномалиях производительности, вызванных такими событиями, настройте ниже maintenance windows в соответствии с графиком обслуживания вашей организации.",
    # alerting-profile
    "Alerting profiles enable you to set up fine-grained alert-filtering rules that are based on the severity, customer impact, associated tags, and/or duration of detected problems. They enable you to control exactly which conditions result in problem notifications and which don't. Alerting profiles can also be used to set up filtered problem-notification integrations with 3rd party messaging systems like Slack, Splunk On-Call, and PagerDuty.": "Профили оповещений позволяют настраивать тонкие правила фильтрации алертов на основе severity, влияния на клиента, ассоциированных тегов и/или длительности обнаруженных problems. Они дают точный контроль над тем, какие условия приводят к problem notifications, а какие нет. Профили оповещений также можно использовать для настройки фильтрованных интеграций problem-notification со сторонними мессенджерами: Slack, Splunk On-Call, PagerDuty.",
    # anomaly-detection-infrastructure-aws
    "Dynatrace automatically detects infrastructure-related performance anomalies such as high CPU saturation, memory outages, and low disk-space conditions. These settings allow you to configure detection sensitivity, set alert thresholds, or disable alerting for classic infrastructure components.": "Dynatrace автоматически обнаруживает инфраструктурные аномалии производительности, такие как высокая загрузка CPU, нехватка памяти и низкое свободное место на диске. Эти параметры позволяют настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для классических инфраструктурных компонентов.",
    # anomaly-detection-infrastructure-vmware
    "Dynatrace automatically detects infrastructure-related performance anomalies such as high CPU saturation, memory outages, and low disk-space conditions. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for infrastructure components.": "Dynatrace автоматически обнаруживает инфраструктурные аномалии производительности, такие как высокая загрузка CPU, нехватка памяти и низкое свободное место на диске. Используйте эти параметры, чтобы настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для инфраструктурных компонентов.",
    # anomaly-detection-kubernetes-workload (BOMJ чистится)
    "Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes workload. Changing thresholds resets the observation period. Additional information can be found on our [documentation page](https://dt-url.net/wq02okj#workload).": "Dynatrace автоматически обнаруживает широкий спектр типичных проблем Kubernetes. Используйте эти параметры, чтобы настроить оповещения для вашего Kubernetes workload. Изменение порогов сбрасывает observation period. Дополнительная информация на [documentation page](https://dt-url.net/wq02okj#workload).",
    # failure-detection-rulesets (BOMJ чистится)
    "Define rulesets to detect failures based on span attributes defined in the [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/model/trace) and custom attributes. Rulesets are evaluated in order and the first matching one defines the failure detection result.": "Определите rulesets для обнаружения сбоев на основе атрибутов span, описанных в [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/model/trace), и пользовательских атрибутов. Rulesets оцениваются по порядку, и первый совпавший определяет результат обнаружения сбоя.",
    # monitoredentities-generic-type (BOMJ чистится)
    'Looking for topology extraction support? Find the [topology model](https://www.dynatrace.com/support/help/shortlink/topology-model#custom-topology-model "Visit Dynatrace support center") help page here.': 'Ищете поддержку извлечения топологии? Справочную страницу см. в [topology model](https://www.dynatrace.com/support/help/shortlink/topology-model#custom-topology-model "Visit Dynatrace support center").',
    "A generic type allows to define rules for creating custom monitored entities based on ingest data.": "Generic type позволяет задать правила создания custom monitored entities на основе данных ingest.",
    # process-built-in-process-monitoring-rule
    "Enable or disable built-in monitoring rules.": "Включает или отключает встроенные правила мониторинга.",
    # process-group-detection-flags
    "Enable or disable process group detection flags": "Включает или отключает флаги обнаружения process group",
    # process-grouping-rules (BOMJ чистится в обеих ссылках)
    "Dynatrace automatically monitors process groups that are of known technology types or that consume significant resources. With process grouping rules, you can automatically monitor additional technologies.": "Dynatrace автоматически мониторит process groups известных технологических типов или потребляющие значительные ресурсы. С помощью process grouping rules можно автоматически мониторить дополнительные технологии.",
    "For more information read the [community post](https://dt-url.net/ea2319k).": "Подробнее см. в [community post](https://dt-url.net/ea2319k).",
    "Process grouping rules also work for processes that have [deep monitoring enabled](https://dt-url.net/3203vvp).": "Process grouping rules также работают для процессов с [deep monitoring enabled](https://dt-url.net/3203vvp).",
    # service-detection-external-web-request (BOMJ чистится)
    "Rules are evaluated from top to bottom, and the first matching rule applies. Rule conditions are evaluated before Service Id Contributors are applied. Note that conditions do not modify attributes of requests. If conditions match, then Service Id Contributors are applied. **All of the Contributors except for the port are always applied.** You can exclude the port contribution by disabling the switch. You can enable the transformation of other Service Id Contributors values to manage which Services are created.  \nMore extensive information on Service detection rules can be found [here](https://dt-url.net/9i03b79).": "Правила оцениваются сверху вниз, применяется первое совпавшее. Условия правил оцениваются до применения Service Id Contributors. Учтите, что условия не модифицируют атрибуты requests. Если условия совпадают, применяются Service Id Contributors. **Все Contributors, кроме порта, применяются всегда.** Вклад порта можно исключить переключателем. Можно включить трансформацию значений других Service Id Contributors, чтобы управлять тем, какие Services создаются.  \nПодробнее о Service detection rules см. [here](https://dt-url.net/9i03b79).",
    # service-detection-external-web-service / full-web-request / full-web-service (общий)
    "Rules are evaluated from top to bottom, and the first matching rule applies. Rule conditions are evaluated before Service Id Contributors are applied. Note that conditions do not modify attributes of requests. If conditions match, then Service Id Contributors are applied. **All of the Contributors are always applied.** But it is possible to influence the creation of Services by choosing how they get transformed.  \nMore extensive information on Service detection rules can be found [here](https://dt-url.net/9i03b79).": "Правила оцениваются сверху вниз, применяется первое совпавшее. Условия правил оцениваются до применения Service Id Contributors. Учтите, что условия не модифицируют атрибуты requests. Если условия совпадают, применяются Service Id Contributors. **Все Contributors применяются всегда.** Но влиять на создание Services можно, выбирая, как они трансформируются.  \nПодробнее о Service detection rules см. [here](https://dt-url.net/9i03b79).",
}

PARAM_LABEL = {
    # Shared / общие
    "Enabled": "Включено",
    "Name": "Имя",
    "Description": "Описание",
    "Type": "Тип",
    "Key": "Ключ",
    "Value": "Значение",
    "Active": "Активно",
    "Operator": "Оператор",
    "Negate": "Инвертировать",
    "Properties": "Свойства",
    "Condition": "Условие",
    "Threshold": "Порог",
    # alerting-maintenance-window
    "Maintenance type": "Тип обслуживания",
    "Problem detection and alerting": "Обнаружение problem и оповещения",
    "Disable synthetic monitor execution": "Отключить выполнение synthetic-мониторов",
    "Recurrence": "Повторяемость",
    "Entity type": "Тип сущности",
    "Entity": "Сущность",
    "Entity tags": "Теги сущности",
    "Management zones": "Management zones",
    "Start time": "Время начала",
    "End time": "Время окончания",
    "Timezone": "Часовой пояс",
    "Time window": "Временное окно",
    "Recurrence range": "Диапазон повторения",
    "Day of week": "День недели",
    "Day of month": "День месяца",
    "Start date": "Дата начала",
    "End date": "Дата окончания",
    # alerting-profile
    "Management zone": "Management zone",
    "Severity rules": "Правила severity",
    "Event filters": "Фильтры событий",
    "Problem severity level": "Уровень severity для problem",
    "Problem send delay in minutes": "Задержка отправки problem в минутах",
    "Filter problems by tag": "Фильтровать problems по тегу",
    "Tags": "Теги",
    "Filter problems by any event of source": "Фильтровать problems по любому событию источника",
    "Filter problems by a Dynatrace event type": "Фильтровать problems по типу события Dynatrace",
    "Title filter": "Фильтр по заголовку",
    "Description filter": "Фильтр по описанию",
    "Property filters": "Фильтры по свойствам",
    "Operator of the comparison": "Оператор сравнения",
    "Case sensitive": "С учётом регистра",
    # anomaly-detection-infrastructure-aws / vmware
    "Detect high CPU saturation on EC2 monitoring candidate": "Обнаруживать высокую загрузку CPU на EC2 monitoring candidate",
    "Detect high CPU utilization on RDS": "Обнаруживать высокую загрузку CPU на RDS",
    "Detect high RDS write/read latency": "Обнаруживать высокую latency записи/чтения на RDS",
    "Detect low free storage space on RDS": "Обнаруживать нехватку свободного места на RDS",
    "Detect RDS running out of memory": "Обнаруживать нехватку памяти на RDS",
    "Detect high number of backend connection errors on ELB": "Обнаруживать большое число backend connection errors на ELB",
    "Detect restarts sequence on RDS": "Обнаруживать серию рестартов на RDS",
    "Detect AWS Lambda high error rate": "Обнаруживать высокий error rate AWS Lambda",
    "Detection mode": "Режим обнаружения",
    "CPU usage is higher than": "Загрузка CPU выше",
    "Read/write latency is higher than": "Latency чтения/записи выше",
    "Free storage space divided by allocated storage is lower than": "Отношение свободного места к выделенному ниже",
    "Freeable memory is lower than": "Доступная для освобождения память ниже",
    "Swap usage is higher than": "Использование swap выше",
    "Number of backend connection errors is higher than": "Число backend connection errors выше",
    "Number of restarts per minute is equal or higher than": "Число рестартов в минуту равно или выше",
    "Failed invocations rate is higher than": "Доля неудачных вызовов выше",
    "Detect high CPU saturation on ESXi host": "Обнаруживать высокую загрузку CPU на ESXi host",
    "Detect guest CPU limit reached": "Обнаруживать достижение CPU limit гостем",
    "Detect memory saturation on ESXi host": "Обнаруживать нехватку памяти на ESXi host",
    "Detect overloaded storage on physical storage device": "Обнаруживать перегрузку физического storage-устройства",
    "Detect undersized storage device": "Обнаруживать недостаточный размер storage-устройства",
    "Detect physical storage device running slow": "Обнаруживать медленную работу физического storage-устройства",
    "Detect high number of dropped packets": "Обнаруживать большое число dropped packets",
    "Detect low datastore space": "Обнаруживать нехватку места в datastore",
    "VM CPU ready is higher than": "VM CPU ready выше",
    "At least one peak occurred when Hypervisor CPU usage was higher than": "Зафиксирован хотя бы один пик, когда загрузка CPU гипервизора была выше",
    "Hypervisor CPU usage is higher than": "Загрузка CPU гипервизора выше",
    "VM CPU usage (VM CPU Usage Mhz / VM CPU limit in Mhz) is higher than": "Загрузка CPU VM (VM CPU Usage Mhz / VM CPU limit in Mhz) выше",
    "ESXi host swap IN/OUT or compression/decompression rate is higher than": "Скорость swap IN/OUT или compression/decompression на ESXi host выше",
    "Number of command aborts is higher than": "Число command aborts выше",
    "Average queue command latency is higher than": "Средняя queue command latency выше",
    "Peak queue command latency is higher than": "Пиковая queue command latency выше",
    "Peak value for read/write latency is higher than": "Пиковое значение read/write latency выше",
    "Receive/transmit dropped packets rate on NIC is higher than": "Скорость dropped packets на NIC (receive/transmit) выше",
    "Datastore free space is lower than": "Свободное место в datastore ниже",
    # anomaly-detection-kubernetes-workload
    "Detect container restarts": "Обнаруживать перезапуски контейнеров",
    "Detect stuck deployments": "Обнаруживать зависшие deployments",
    "Detect pods stuck in pending": "Обнаруживать pods, застрявшие в pending",
    "Detect pods stuck in terminating": "Обнаруживать pods, застрявшие в terminating",
    "Detect workloads without ready pods": "Обнаруживать workloads без ready pods",
    "Detect workloads with non-ready pods": "Обнаруживать workloads с non-ready pods",
    "Detect memory usage saturation": "Обнаруживать насыщение использования памяти",
    "Detect CPU usage saturation": "Обнаруживать насыщение использования CPU",
    "Detect high CPU throttling": "Обнаруживать высокий CPU throttling",
    "Detect out-of-memory kills": "Обнаруживать out-of-memory kills",
    "Detect job failure events": "Обнаруживать события сбоя job",
    "Detect pod backoff events": "Обнаруживать события pod backoff",
    "Detect pod eviction events": "Обнаруживать события pod eviction",
    "Detect pod preemption events": "Обнаруживать события pod preemption",
    "there is at least": "имеется не менее",
    "per minute, for any": "в минуту, для любого",
    "within the last": "за последние",
    "workload stops progressing for at least": "workload не прогрессирует не менее",
    "stuck in pending state for at least": "находятся в pending не менее",
    "pod termination stops progressing for at least": "терминация pod не прогрессирует не менее",
    "workload has no ready pods for at least": "у workload нет ready pods не менее",
    "some workload pods are not ready for at least": "часть pods workload не в ready не менее",
    "amount of utilized workload memory is above": "доля используемой памяти workload выше",
    "of defined memory limits for at least": "от заданных memory limits не менее",
    "amount of utilized workload CPU is above": "доля используемого CPU workload выше",
    "of defined CPU limits for at least": "от заданных CPU limits не менее",
    "amount of CPU throttling is above": "доля CPU throttling выше",
    "of CPU usage for at least": "от использования CPU не менее",
    # failure-detection-rulesets
    "Ruleset": "Ruleset",
    "Ruleset name": "Имя ruleset",
    "Matching condition": "Условие совпадения",
    "HTTP status codes": "HTTP status codes",
    "gRPC status codes": "gRPC status codes",
    "Span status code": "Span status code",
    "Exceptions": "Exceptions",
    "Custom failure rules": "Custom-правила сбоев",
    "Status codes which indicate a failure on the server side": "Status codes, указывающие на сбой на стороне сервера",
    'Fail on span status "error"': 'Считать сбоем при span status "error"',
    "Fail on exceptions": "Считать сбоем при exceptions",
    "Rule name": "Имя правила",
    "DQL condition": "DQL-условие",
    "Force success on specific exceptions": "Принудительно success для определённых exceptions",
    "Custom success forcing rules": "Custom-правила принудительного success",
    'Force success on span status "ok"': 'Принудительно success при span status "ok"',
    "Status codes which force success on the server side": "Status codes, принудительно дающие success на стороне сервера",
    "Exception type contains": "Тип exception содержит",
    "Exception message contains": "Сообщение exception содержит",
    # process-group-detection-flags (длинные label-описания)
    "Ignore versions, builds, dates, and GUIDs in process directory names": "Игнорировать версии, сборки, даты и GUID в именах каталогов процессов",
    "Use CATALINA\\_BASE to identify Tomcat cluster nodes": "Использовать CATALINA\\_BASE для идентификации Tomcat cluster nodes",
    "Use Docker container name to distinguish multiple containers": "Использовать имя Docker-контейнера для различения нескольких контейнеров",
    "Automatically detect Cassandra clusters": "Автоматически обнаруживать Cassandra-кластеры",
    "Use Node.js script name to distinguish processes started from same directory in addition to application id.": "Использовать имя Node.js-скрипта для различения процессов, запущенных из одного каталога, в дополнение к application id.",
    "Automatically detect TIBCO BusinessWorks engines": "Автоматически обнаруживать TIBCO BusinessWorks engines",
    "Identify and name JBoss servers based on system property jboss.server.name": "Идентифицировать и именовать JBoss-серверы по system property jboss.server.name",
    "Automatically detect webMethods Integration Server": "Автоматически обнаруживать webMethods Integration Server",
    "Automatically detect Spring Boot applications": "Автоматически обнаруживать Spring Boot-приложения",
    "Automatically detect TIBCO BusinessWorks Container Edition engines": "Автоматически обнаруживать TIBCO BusinessWorks Container Edition engines",
    "Group Oracle database processes by SID": "Группировать процессы Oracle database по SID",
    "Group Oracle listener processes by name": "Группировать процессы Oracle listener по имени",
    "Automatically detect WebSphere Liberty application": "Автоматически обнаруживать WebSphere Liberty-приложение",
    "Monitor short lived processes": "Мониторить короткоживущие процессы",
    "Group IBM MQ processes by queue manager name": "Группировать процессы IBM MQ по имени queue manager",
    "Automatically detect security software": "Автоматически обнаруживать security-софт",
    "Group DB2 database processes by DB2 Instances": "Группировать процессы DB2 database по DB2 Instances",
    # monitoredentities-generic-type
    "Type name": "Имя типа",
    "Type display name": "Отображаемое имя типа",
    "Created by": "Создано",
    "List of rules": "Список правил",
    "Extracted ID pattern": "Шаблон извлекаемого ID",
    "Instance name pattern": "Шаблон имени экземпляра",
    "Icon Pattern": "Шаблон иконки",
    "Source filters": "Фильтры источников",
    "Additionally required dimensions": "Дополнительно обязательные dimensions",
    "Attributes": "Атрибуты",
    "Role": "Роль",
    "Ingest datasource type": "Тип datasource ingest",
    "Dimension key": "Dimension-ключ",
    "Dimension value pattern": "Шаблон значения dimension",
    "Attribute key": "Ключ атрибута",
    "Attribute display name": "Отображаемое имя атрибута",
    "Attribute value extraction pattern": "Шаблон извлечения значения атрибута",
    # process-grouping-rules
    "Custom technology name": "Имя custom-технологии",
    "Define the process groups": "Определить process groups",
    "1.1. Process group display name (optional)": "1.1. Отображаемое имя process group (опц.)",
    "1.2. Report process group": "1.2. Сообщать о process group",
    "1.3. Type of captured processes (optional)": "1.3. Тип захватываемых процессов (опц.)",
    "Standalone rule": "Standalone-правило",
    "3.1.1. Id type": "3.1.1. Тип id",
    "3.1.2. Process group identifier": "3.1.2. Идентификатор process group",
    "3.1.2. Property": "3.1.2. Свойство",
    "Variable name": "Имя переменной",
    "3.1.3. Advanced settings (optional)": "3.1.3. Расширенные настройки (опц.)",
    "3.2.1. Property": "3.2.1. Свойство",
    "3.2.2. Advanced settings (optional)": "3.2.2. Расширенные настройки (опц.)",
    "2.1. Property": "2.1. Свойство",
    "2.2. Variable name": "2.2. Имя переменной",
    "2.2. Condition": "2.2. Условие",
    "Delimit from (optional)": "Делимитер от (опц.)",
    "Delimit to (optional)": "Делимитер до (опц.)",
    "Ignore numbers": "Игнорировать числа",
    # service-detection-* (общие)
    "Rule name": "Имя правила",
    "Service identifier contributors": "Contributors для идентификатора сервиса",
    "Service Identifier Contributors": "Contributors для идентификатора сервиса",
    "Conditions": "Условия",
    "Application identifier": "Идентификатор приложения",
    "URL context root": "URL context root",
    "Public domain name": "Публичное доменное имя",
    "Port": "Порт",
    "Server Name": "Имя сервера",
    "Server name": "Имя сервера",
    "Web service name": "Имя web service",
    "Web service namespace": "Namespace web service",
    "Detect as web request service": "Обнаруживать как web request service",
    "URL path": "URL path",
    "Take the value of this attribute": "Взять значение этого атрибута",
    "Apply this operation": "Применить эту операцию",
    "Values": "Значения",
    "From": "От",
    "To": "До",
    "Technology": "Технология",
    "Ignore case": "Игнорировать регистр",
    "Transform this value before letting it contribute to the Service Id": "Преобразовать это значение перед вкладом в Service Id",
    "Contribution type": "Тип вклада",
    "Value override": "Переопределение значения",
    "Transformations": "Преобразования",
    "Segments to copy from URL path": "Сегменты, копируемые из URL path",
    "Copy from host name": "Брать из имени хоста",
    "Transformation type": "Тип преобразования",
    "Transformation Type": "Тип преобразования",
    "prefix": "префикс",
    "suffix": "суффикс",
    "replacement": "замена",
    "split by": "разделить по",
    "select index": "индекс выбора",
    "min digit count": "минимальное количество цифр",
    "include hexadecimal numbers": "включая шестнадцатеричные числа",
    "segment count": "количество сегментов",
    "take from end": "брать с конца",
}

PARAM_DESC = {
    # alerting-maintenance-window
    "The status of the maintenance window. If `false`, it is not considered during the maintenance window evaluation.": "Статус maintenance window. Если `false`, при вычислении maintenance window не учитывается.",
    "Add filters to limit the scope of maintenance to only select matching entities. If no filter is defined, the maintenance window is valid for the whole environment. Each filter is evaluated separately (**OR**).": "Добавьте фильтры, чтобы ограничить scope maintenance только совпадающими сущностями. Если фильтр не задан, maintenance window действует для всего environment. Каждый фильтр оценивается отдельно (**OR**).",
    "A short description of the maintenance purpose.": "Краткое описание цели обслуживания.",
    "Whether the maintenance is planned or unplanned.": "Является обслуживание плановым или внеплановым.",
    "Defines if alerting or problem generation is disabled.  * **Detect problems and alert**: Problems are generated and alerted. * **Detect problems but don't alert**: Problems are generated but no alerts are sent out. * **Disable problem detection during maintenance**: Neither problems are generated nor alerts are sent out.": "Определяет, отключаются ли оповещения или генерация problems.  * **Detect problems and alert**: Problems генерируются, оповещения отправляются. * **Detect problems but don't alert**: Problems генерируются, но оповещения не отправляются. * **Disable problem detection during maintenance**: Ни problems не генерируются, ни оповещения не отправляются.",
    "Disables the execution of the synthetic monitors that are within [the scope of this maintenance window](https://dt-url.net/0e0341m).": "Отключает выполнение synthetic-мониторов, попадающих в [the scope of this maintenance window](https://dt-url.net/0e0341m).",
    "Defines the recurrence type of the maintenance window.  * **Once**: One time maintenance window with start and end date time. * **Daily**: Maintenance window occurs every day during the configured time window. * **Weekly**: Maintenance window occurs each week on one day during the configured time window. * **Monthly**: Maintenance window occurs each month on one day during the configured time window.": "Определяет тип повторяемости maintenance window.  * **Once**: однократное maintenance window с датой и временем начала и окончания. * **Daily**: maintenance window повторяется каждый день в заданном временном окне. * **Weekly**: maintenance window повторяется раз в неделю в один и тот же день в заданном временном окне. * **Monthly**: maintenance window повторяется раз в месяц в один и тот же день в заданном временном окне.",
    "Type of entities this maintenance window should match.  If no entity type is selected all entities regardless of the type will match.": "Тип сущностей, на которые должно распространяться это maintenance window.  Если тип сущности не выбран, под фильтр попадают все сущности независимо от типа.",
    "A specific entity that should match this maintenance window.  **Note**: If an entity type filter value is set, it must be equal to the type of the selected entity. Otherwise this maintenance window will not match.": "Конкретная сущность, которая должна попадать под это maintenance window.  **Note**: если задан фильтр по типу сущности, он должен соответствовать типу выбранной сущности, иначе maintenance window не сработает.",
    "Entities which contain all of the configured tags will match this maintenance window. It is recommended to use manual tags.  **Note:** Automatically applied tags may experience delays or inconsistencies due to rule complexity and attribute variability. Entities may not be immediately tagged, impacting filter effectiveness.  It is recommended to use manual tags instead.  For more information, visit our [best practices for tagging documentation page](https://dt-url.net/8203d4x).": "Под фильтр попадут сущности, содержащие все настроенные теги. Рекомендуется использовать ручные теги.  **Note:** автоматически применяемые теги могут запаздывать или быть несогласованными из-за сложности правил и изменчивости атрибутов. Сущности могут получить тег не сразу, это влияет на эффективность фильтра.  Лучше использовать ручные теги.  Подробнее см. [best practices for tagging documentation page](https://dt-url.net/8203d4x).",
    "Entities which are part of all the configured management zones will match this maintenance window. It is recommended to use manual tags instead.  **Note:** Management zones may experience delays or inconsistencies due to rule complexity and attribute variability. Entities may not be immediately assigned to management zones, impacting filter effectiveness.  It is recommended to use manual tags instead.  For more information, visit our [best practices for management zones documentation page](https://dt-url.net/8203d4x).": "Под фильтр попадут сущности, входящие во все настроенные management zones. Вместо этого рекомендуется использовать ручные теги.  **Note:** management zones могут запаздывать или быть несогласованными из-за сложности правил и изменчивости атрибутов. Сущности могут попасть в management zone не сразу, это влияет на эффективность фильтра.  Лучше использовать ручные теги.  Подробнее см. [best practices for management zones documentation page](https://dt-url.net/8203d4x).",
    "If the selected day does not fall within the month, the maintenance window will be active on the last day of the month.": "Если выбранный день в месяце отсутствует, maintenance window будет активно в последний день месяца.",
    # alerting-profile
    "Entities which are part of the configured management zones will match this alerting profile. It is recommended to use manual tags instead.  **Note:** Management zones may experience delays or inconsistencies due to rule complexity and attribute variability. Entities may not be immediately assigned to management zones, impacting filter effectiveness.  It is recommended to use manual tags instead.  For more information, visit our [best practices for management zones documentation page](https://dt-url.net/8203d4x).": "Под фильтр попадут сущности, входящие в настроенные management zones. Вместо этого рекомендуется использовать ручные теги.  **Note:** management zones могут запаздывать или быть несогласованными из-за сложности правил и изменчивости атрибутов. Сущности могут попасть в management zone не сразу, это влияет на эффективность фильтра.  Лучше использовать ручные теги.  Подробнее см. [best practices for management zones documentation page](https://dt-url.net/8203d4x).",
    "Define severity rules for profile. A maximum of 100 severity rules is allowed.": "Задайте правила severity для профиля. Максимум 100 severity-правил.",
    "Define event filters for profile. A maximum of 100 event filters is allowed.": "Задайте фильтры событий для профиля. Максимум 100 event-фильтров.",
    "Send a notification if a problem remains open longer than X minutes.": "Отправить уведомление, если problem остаётся открытой дольше X минут.",
    "Define filters for event properties. A maximum of 20 properties is allowed.": "Задайте фильтры для свойств события. Максимум 20 свойств.",
    "Entities which contain any/all of the configured tags will match this alerting profile. It is recommended to use manual tags.  **Note:** Automatically applied tags may experience delays or inconsistencies due to rule complexity and attribute variability. Entities may not be immediately tagged, impacting filter effectiveness.  It is recommended to use manual tags instead.  For more information, visit our [best practices for tagging documentation page](https://dt-url.net/8203d4x).": "Под фильтр попадут сущности, содержащие любые/все настроенные теги. Рекомендуется использовать ручные теги.  **Note:** автоматически применяемые теги могут запаздывать или быть несогласованными из-за сложности правил и изменчивости атрибутов. Сущности могут получить тег не сразу, это влияет на эффективность фильтра.  Лучше использовать ручные теги.  Подробнее см. [best practices for tagging documentation page](https://dt-url.net/8203d4x).",
    "Type 'dt.' for key hints.": "Введите 'dt.' для подсказок по ключам.",
    # anomaly-detection-infrastructure (aws + vmware)
    "Alert if the condition is met in 3 out of 5 samples": "Оповестить, если условие выполнено в 3 из 5 samples",
    "Alert if **both** conditions is met in 3 out of 5 samples": "Оповестить, если **оба** условия выполнены в 3 из 5 samples",
    "Alert if **all three** conditions are met in 3 out of 5 samples": "Оповестить, если выполнены **все три** условия в 3 из 5 samples",
    "Alert if **any** condition is met in 3 out of 5 samples": "Оповестить, если выполнено **любое** условие в 3 из 5 samples",
    "Alert if **any** condition is met in 4 out of 5 samples": "Оповестить, если выполнено **любое** условие в 4 из 5 samples",
    "Alert if the condition is met in 2 out of 20 samples": "Оповестить, если условие выполнено в 2 из 20 samples",
    "Alert if the condition is met in 1 out of 5 samples": "Оповестить, если условие выполнено в 1 из 5 samples",
    # anomaly-detection-kubernetes-workload
    "Alert if": "Оповестить, если",
    "Evaluates workload condition 'Progressing'": "Оценивает условие workload 'Progressing'",
    "Number of pods in `Pending` phase": "Число pods в фазе `Pending`",
    "Deleted pods in 'Running' phase": "Удалённые pods в фазе 'Running'",
    "As of specific pod life cycles of different workload types, cronjobs and jobs are excluded.": "С учётом особенностей жизненного цикла pods разных типов workload, cronjobs и jobs исключены.",
    "Memory usage (working set memory) is close to limits.": "Использование памяти (working set memory) близко к limits.",
    "CPU usage is close to limits.": "Использование CPU близко к limits.",
    "The CPU throttling to limits ratio exceeds the specified threshold. Important: This alert uses throttled seconds / limits (in millicores) in contrast to Prometheus and Grafana, which use throttled periods / total periods for the throttling ratio.": "Отношение CPU throttling к limits превышает заданный порог. Важно: этот alert использует throttled seconds / limits (в millicores), в отличие от Prometheus и Grafana, где соотношение throttling считается как throttled periods / total periods.",
    "Alerts on any occurrence of Kubernetes events with reason 'BackoffLimitExceeded', 'DeadlineExceeded', or 'PodFailurePolicy'.  If 'Filter events' is enabled, make certain that you ingest events with the aforementioned reasons in order to receive alerts.": "Оповещает при любом возникновении Kubernetes-событий с reason 'BackoffLimitExceeded', 'DeadlineExceeded' или 'PodFailurePolicy'.  Если включён 'Filter events', убедитесь, что вы ingest'ите события с указанными reason, иначе оповещений не будет.",
    "Alerts on any occurrence of Kubernetes events with reason 'BackOff', as observed on pod statuses 'ImagePullBackOff', and 'CrashLoopBackOff'.  If 'Filter events' is enabled, make certain that you ingest events with the aforementioned reasons in order to receive alerts.": "Оповещает при любом возникновении Kubernetes-событий с reason 'BackOff', наблюдаемых на pod-статусах 'ImagePullBackOff' и 'CrashLoopBackOff'.  Если включён 'Filter events', убедитесь, что вы ingest'ите события с указанными reason, иначе оповещений не будет.",
    "Eviction is the process of terminating one or more pods on a node to free up resources.  Alerts on any occurrence of Kubernetes events with reason 'Evicted'.  If 'Filter events' is enabled, make certain that you ingest events with the aforementioned reasons in order to receive alerts.": "Eviction, это процесс terminating одного или нескольких pods на ноде ради освобождения ресурсов.  Оповещает при любом возникновении Kubernetes-событий с reason 'Evicted'.  Если включён 'Filter events', убедитесь, что вы ingest'ите события с указанными reason, иначе оповещений не будет.",
    "Preemption is the process of terminating pods with lower priority so that pods with higher priority can be scheduled on a node.  Alerts on any occurrence of Kubernetes events with reason 'Preempted', or 'Preempting'.  If 'Filter events' is enabled, make certain that you ingest events with the aforementioned reasons in order to receive alerts.": "Preemption, это процесс terminating pods с более низким приоритетом, чтобы pods с более высоким приоритетом можно было запланировать на ноде.  Оповещает при любом возникновении Kubernetes-событий с reason 'Preempted' или 'Preempting'.  Если включён 'Filter events', убедитесь, что вы ingest'ите события с указанными reason, иначе оповещений не будет.",
    # failure-detection-rulesets
    "If enabled, the ruleset will be evaluated.": "Если включено, ruleset будет оцениваться.",
    "Limits the scope of the failure detection ruleset using [DQL matcher](https://dt-url.net/l603wby) conditions on span and resource attributes.  A ruleset is applied only if the condition matches, otherwise the evaluation continues.  If empty, the condition will always match.": "Ограничивает scope ruleset с помощью условий [DQL matcher](https://dt-url.net/l603wby) на атрибутах span и resource.  Ruleset применяется только при совпадении условия, иначе оценка продолжается.  Если пусто, условие всегда совпадает.",
    'Evaluated attribute: `http.response.status_code`  Failure detection result: `reason="http_code"`, `verdict="failure"`': 'Оцениваемый атрибут: `http.response.status_code`  Результат обнаружения сбоя: `reason="http_code"`, `verdict="failure"`',
    'Evaluated attribute: `rpc.grpc.status_code`  Failure detection result: `reason="grpc_code"`, `verdict="failure"`': 'Оцениваемый атрибут: `rpc.grpc.status_code`  Результат обнаружения сбоя: `reason="grpc_code"`, `verdict="failure"`',
    'Evaluated attribute: `span.status_code`  Failure detection result: `reason="span_status"`, `verdict="failure"`': 'Оцениваемый атрибут: `span.status_code`  Результат обнаружения сбоя: `reason="span_status"`, `verdict="failure"`',
    'Evaluated expression: `iAny(`span.events`[][`span\\_event.name`] == "exception" and` span.events`[][`exception.escaped`] != false)`  Failure detection result: `reason="exception"`, `verdict="failure"`, `exception_ids`': 'Оцениваемое выражение: `iAny(`span.events`[][`span\\_event.name`] == "exception" and` span.events`[][`exception.escaped`] != false)`  Результат обнаружения сбоя: `reason="exception"`, `verdict="failure"`, `exception_ids`',
    'Define failure reasons based on span and request attributes.  Failure detection result: `reason="custom_rule"`, `verdict="failure"`, `custom_rule_name`': 'Задайте причины сбоев на основе атрибутов span и request.  Результат обнаружения сбоя: `reason="custom_rule"`, `verdict="failure"`, `custom_rule_name`',
    "Custom rule based on span attributes using [DQL matcher](https://dt-url.net/l603wby).": "Custom-правило на основе атрибутов span с использованием [DQL matcher](https://dt-url.net/l603wby).",
    'Evaluated attribute: `http.response.status_code`  Failure detection result: `reason="http_code"`, `verdict="success"`': 'Оцениваемый атрибут: `http.response.status_code`  Результат обнаружения сбоя: `reason="http_code"`, `verdict="success"`',
    'Evaluated attribute: `rpc.grpc.status_code`  Failure detection result: `reason="grpc_code"`, `verdict="success"`': 'Оцениваемый атрибут: `rpc.grpc.status_code`  Результат обнаружения сбоя: `reason="grpc_code"`, `verdict="success"`',
    'Evaluated attribute: `span.status_code`  Failure detection result: `reason="span_status"`, `verdict="success"`': 'Оцениваемый атрибут: `span.status_code`  Результат обнаружения сбоя: `reason="span_status"`, `verdict="success"`',
    'Define escaped exceptions that should force success.  Evaluated expression: `iAny(`span.events`[][`span\\_event.name`] == "exception" and` span.events`[][`exception.escaped`] != false)`  Failure detection result: `reason="exception"`, `verdict="success"`, `exception_ids`': 'Задайте escaped exceptions, которые должны принудительно давать success.  Оцениваемое выражение: `iAny(`span.events`[][`span\\_event.name`] == "exception" and` span.events`[][`exception.escaped`] != false)`  Результат обнаружения сбоя: `reason="exception"`, `verdict="success"`, `exception_ids`',
    'Override failures based on span and request attribute conditions.  Failure detection result: `reason="custom_rule"`, `verdict="success"`, `custom_rule_name`': 'Переопределить сбои по условиям на атрибутах span и request.  Результат обнаружения сбоя: `reason="custom_rule"`, `verdict="success"`, `custom_rule_name`',
    "Evaluated attribute: `span.events[][exception.type]`": "Оцениваемый атрибут: `span.events[][exception.type]`",
    "Evaluated attribute: `span.events[][exception.message]`": "Оцениваемый атрибут: `span.events[][exception.message]`",
    # monitoredentities-generic-type
    "Enables or disables the type": "Включает или отключает тип",
    "The entity type name. This type name must be unique and must not be changed after creation.": "Имя типа сущности. Имя должно быть уникальным и не меняться после создания.",
    "The human readable type name for this entity type.": "Человекочитаемое имя для этого типа сущности.",
    "The user or extension that created this type.": "Пользователь или расширение, создавшее этот тип.",
    "Specify a list of rules which are evaluated in order. When **any** rule matches, the entity defined according to that rule will be extracted. Subsequent rules will not be evaluated.  Rules are evaluated in the order they appear in this list. Each rule defines how to create a single entity from ingested data. It defines properties like name, identifier and other attributes which are stored as part of that entity. A rule also describes filters which need to match the ingest data in order to create an entity.  Many properties of an extraction rule use *placeholders* to dynamically evaluate and transform ingest data. Such rule properties are called *patterns* and allow combining dimension values with static text. The evaluated result is then used when extracting an entity. Each pattern may use multiple placeholders, each referring a single dimension key. During entity extraction, placeholders are replaced with the respective dimension values.  Placeholders start with `{` and end with `}` (Those characters cannot be part of the static text of a pattern). It is not allowed to nest placeholders.  **Example:**  Ingest data line: `temperature,room=5.30 gauge,min=17.1,max=17.3,sum=34.4,count=2`  ID Pattern: `ROOM_{room}`  Would evaluate to the ID `ROOM_5.30`.  **Example:**  Ingest data line: `device.packets.received,device_number=123,if=eth0 1024`  Attribute Value Extraction Pattern: `192.168.1.{device_number}`  Would evaluate to a string `192.168.1.123` and could be stored as an IP address.": "Задайте список правил, которые оцениваются по порядку. Когда совпадает **любое** правило, по нему извлекается сущность, и последующие правила не оцениваются.  Правила оцениваются в порядке их появления в этом списке. Каждое правило описывает, как создать одну сущность из ingested data. Оно задаёт свойства (имя, идентификатор и прочие атрибуты), которые сохраняются как часть сущности. Правило также описывает фильтры, которые должны совпасть с ingest data, чтобы сущность была создана.  Многие свойства extraction rule используют *placeholders* для динамической оценки и трансформации ingest data. Такие свойства называются *patterns* и позволяют комбинировать значения dimension со статическим текстом. Полученный результат используется при извлечении сущности. Один pattern может содержать несколько placeholders, каждый ссылается на свой dimension-ключ. При извлечении сущности placeholders заменяются на соответствующие значения dimension.  Placeholders начинаются с `{` и заканчиваются `}` (эти символы не могут быть частью статического текста pattern). Вложенные placeholders запрещены.  **Example:**  Ingest data line: `temperature,room=5.30 gauge,min=17.1,max=17.3,sum=34.4,count=2`  ID Pattern: `ROOM_{room}`  Даст ID `ROOM_5.30`.  **Example:**  Ingest data line: `device.packets.received,device_number=123,if=eth0 1024`  Attribute Value Extraction Pattern: `192.168.1.{device_number}`  Даст строку `192.168.1.123`, которую можно сохранить как IP-адрес.",
    "ID patterns are comprised of static text and placeholders referring to dimensions in the ingest data. An ID pattern **must** contain at least one placeholder to ensure that different entities will be created.  Take care that the pattern results in the same ID for the same entity. For example, using timestamp or counter-like dimensions as part of the ID would lead to the creation of new entities for each ingest data and is strongly discouraged!  Each dimension key referred to by an identifier placeholder must be present in order to extract an entity. If any dimension key referred to in the identifier is missing, the rule will not be considered for evaluation. If you have cases where you still want to extract the same entity type but have differently named keys, consider creating multiple rules extracting the same entity type. In this case take care that each ID pattern evaluates to the same value if the same entity should be extracted.": "ID patterns состоят из статического текста и placeholders, ссылающихся на dimensions в ingest data. ID pattern **должен** содержать хотя бы один placeholder, чтобы гарантировать создание разных сущностей.  Следите, чтобы pattern давал один и тот же ID для одной и той же сущности. Например, использование timestamp или счётчико-подобных dimension в составе ID приведёт к созданию новой сущности на каждую ingest data, и это категорически не рекомендуется.  Каждый dimension-ключ, на который ссылается placeholder идентификатора, должен присутствовать, иначе сущность не будет извлечена. Если такого dimension-ключа нет, правило не будет рассматриваться. Если требуется извлекать тот же тип сущности при разных именах ключей, создайте несколько правил, извлекающих один и тот же тип. В этом случае следите, чтобы каждый ID pattern давал одно и то же значение для одной и той же сущности.",
    "Define a pattern which is used to set the name attribute of the entity. You may define placeholders referencing data source dimensions.": "Задайте pattern, который используется для атрибута name сущности. Можно использовать placeholders, ссылающиеся на dimensions источника данных.",
    "Define a pattern which is used to set the icon attribute of the entity. The extracted values must reference barista icon ids. You may define placeholders referencing data source dimensions.": "Задайте pattern, который используется для атрибута icon сущности. Извлекаемые значения должны ссылаться на barista icon ids. Можно использовать placeholders, ссылающиеся на dimensions источника данных.",
    "Specify all sources which should be evaluated for this rule. A rule is evaluated if any of the specified source filters match.": "Задайте все источники, которые должны проверяться этим правилом. Правило срабатывает, если совпал любой из указанных фильтров источника.",
    "In addition to the dimensions already referred to in the ID pattern, you may specify additional dimensions which must be present in order to evaluate this rule.": "Помимо dimensions, на которые уже ссылается ID pattern, можно указать дополнительные dimensions, без которых правило не будет оцениваться.",
    "All attribute extraction rules will be applied and found attributes will be added to the extracted type.": "Применяются все правила извлечения атрибутов, найденные атрибуты добавляются к извлекаемому типу.",
    "If you want to extract multiple entities of the same type from a single ingest line you need to define multiple rules with different roles.": "Если из одной строки ingest требуется извлекать несколько сущностей одного типа, задайте несколько правил с разными roles.",
    "Specify the source type of the filter to identify which data source should be evaluated for ingest.": "Укажите тип источника фильтра, чтобы определить, какой источник данных проверяется на ingest.",
    "Specify a filter that needs to match in order for the extraction to happen.  Three different filters are supported: `$eq(value)` will ensure that the source matches exactly 'value', `$prefix(value)` will ensure that the source begins with exactly 'value', '$exists()' will ensure that any source with matching dimension filter exists. If your value contains the characters '(', ')' or '~', you need to escape them by adding a '~' in front of them.": "Задайте фильтр, который должен совпасть, чтобы произошло извлечение.  Поддерживаются три фильтра: `$eq(value)` гарантирует точное совпадение источника с 'value', `$prefix(value)` гарантирует, что источник начинается ровно с 'value', `$exists()` гарантирует наличие любого источника, совпадающего с dimension-фильтром. Если значение содержит символы '(', ')' или '~', их необходимо экранировать, поставив перед ними '~'.",
    "A dimension key which needs to exist in the ingest data to match this filter.": "Dimension-ключ, который должен присутствовать в ingest data, чтобы фильтр совпал.",
    "A dimension value pattern which needs to exist in the ingest data to match this filter.": "Шаблон значения dimension, который должен присутствовать в ingest data, чтобы фильтр совпал.",
    "The attribute key is the unique name of the attribute.": "Ключ атрибута, это уникальное имя атрибута.",
    "The human readable attribute name for this extraction rule. Leave blank to use the key as the display name.": "Человекочитаемое имя атрибута для этого правила извлечения. Оставьте пустым, чтобы использовать ключ в качестве отображаемого имени.",
    "Pattern for specifying the value for the extracted attribute. Can be a static value, placeholders or a combination of both. Can be a static value, placeholders or a combination of both.": "Pattern для задания значения извлекаемого атрибута. Может быть статическим значением, placeholders или их комбинацией. Может быть статическим значением, placeholders или их комбинацией.",
    "Pattern for specifying the value for the extracted attribute. Can be a static value, placeholders or a combination of both.": "Pattern для задания значения извлекаемого атрибута. Может быть статическим значением, placeholders или их комбинацией.",
    # process-built-in-process-monitoring-rule — обрабатывается через _process_rule_row
    # process-group-detection-flags
    "To determine the unique identity of each detected process, and to generate a unique name for each detected process, Dynatrace evaluates the name of the directory that each process binary is contained within. For application containers like Tomcat and JBoss, Dynatrace evaluates important directories like CATALINA\\_HOME and JBOSS\\_HOME for this information. In some automated deployment scenarios such directory names are updated automatically with new version numbers, build numbers, dates, or GUIDs. Enable this setting to ensure that automated directory name changes don't result in Dynatrace registering pre-existing processes as new processes.": "Для определения уникальной идентичности каждого обнаруженного процесса и для генерации уникального имени Dynatrace анализирует имя каталога, в котором лежит binary процесса. Для application containers вроде Tomcat и JBoss Dynatrace анализирует важные каталоги, такие как CATALINA\\_HOME и JBOSS\\_HOME. В некоторых сценариях автоматического деплоя имена таких каталогов обновляются автоматически: добавляются номера версий, сборок, даты или GUID. Включите этот параметр, чтобы автоматические переименования каталогов не приводили к тому, что Dynatrace регистрирует уже существующие процессы как новые.",
    "By default, Tomcat clusters are identified and named based on the CATALINA\\_HOME directory name. This setting results in the use of the CATALINA\\_BASE directory name to identify multiple Tomcat nodes within each Tomcat cluster. If this setting is not enabled, each CATALINA\\_HOME+CATALINA\\_BASE combination will be considered a separate Tomcat cluster. In other words, Tomcat clusters can't have multiple nodes on a single host.": "По умолчанию Tomcat-кластеры идентифицируются и именуются по имени каталога CATALINA\\_HOME. Этот параметр включает использование имени каталога CATALINA\\_BASE для идентификации нескольких Tomcat-нод внутри Tomcat-кластера. Если параметр отключён, каждая комбинация CATALINA\\_HOME+CATALINA\\_BASE будет считаться отдельным Tomcat-кластером, иначе говоря, у Tomcat-кластера не может быть нескольких нод на одном хосте.",
    "**For Docker outside container platforms only.** By default, Dynatrace uses image names as identifiers for individual process groups, with one process-group instance per host. Normally Docker container names can't serve as stable identifiers of process group instances because they are variable and auto-generated. You can however manually assign proper container names to their Docker instances. Such manually-assigned container names can serve as reliable process-group instance identifiers. This flag instructs Dynatrace to use Docker-provided names to distinguish between multiple instances of the same image. If this flag is not applied and you run multiple containers of the same image on the same host, the resulting processes will be consolidated into a single process view. **Use this flag with caution!**": "**Только для Docker вне container platforms.** По умолчанию Dynatrace использует имена образов как идентификаторы process group, по одному инстансу process-group на хост. В обычном случае имена Docker-контейнеров не подходят как стабильные идентификаторы инстансов process group, поскольку они переменные и автогенерируемые. Однако имена контейнеров можно назначить вручную, и тогда они становятся надёжными идентификаторами инстансов process-group. Этот флаг указывает Dynatrace использовать имена, выданные Docker, чтобы различать несколько инстансов одного образа. Если флаг не применён и на одном хосте запущено несколько контейнеров одного образа, соответствующие процессы будут схлопнуты в одно process view. **Применяйте флаг с осторожностью.**",
    "Enabling this flag will detect separate Cassandra process groups based on the configured Cassandra cluster name.": "Включение флага приведёт к обнаружению отдельных Cassandra process groups по настроенному имени Cassandra cluster.",
    "In older versions, Node.js applications were distinguished based on their directory name, omitting the script name. Changing this setting may change the general handling of Node.js process groups. Leave unchanged if in doubt.": "В старых версиях Node.js-приложения различались по имени каталога, имя скрипта не учитывалось. Изменение параметра может изменить общее поведение Node.js process groups. Если сомневаетесь, оставьте как есть.",
    "Enabling this flag will detect separate TIBCO BusinessWorks process groups per engine property file.": "Включение флага приведёт к обнаружению отдельных TIBCO BusinessWorks process groups по каждому engine property file.",
    "Enabling this flag will detect the JBoss server name from the system property jboss.server.name=, only if -D[Server:] is not set.": "Включение флага приведёт к определению имени JBoss server по system property jboss.server.name=, только если не задан -D[Server:].",
    "Enabling this flag will detect webMethods Integration Server including specific properties like install root and product name.": "Включение флага приведёт к обнаружению webMethods Integration Server, включая специфические свойства, такие как install root и product name.",
    "Enabling this flag will detect Spring Boot process groups based on command line and applications' configuration files.": "Включение флага приведёт к обнаружению Spring Boot process groups по командной строке и файлам конфигурации приложений.",
    "Enable to group and separately analyze the processes of each Oracle DB. Each process group receives a unique name based on the Oracle DB SID.": "Включите, чтобы группировать и отдельно анализировать процессы каждой Oracle DB. Каждая process group получает уникальное имя по SID Oracle DB.",
    "Enable to group and separately analyze the processes of each Oracle Listener. Each process group receives a unique name based on the Oracle Listener name. On Windows, this option supports listeners launched manually or running on a Windows virtual account.": "Включите, чтобы группировать и отдельно анализировать процессы каждого Oracle Listener. Каждая process group получает уникальное имя по имени Oracle Listener. На Windows этот параметр поддерживает listeners, запущенные вручную или работающие под Windows virtual account.",
    "Enabling this flag will detect separate WebSphere Liberty process groups based on java command line.": "Включение флага приведёт к обнаружению отдельных WebSphere Liberty process groups по командной строке java.",
    "Enable to monitor CPU and memory usage of short lived processes, otherwise being lost by traditional monitoring.": "Включите, чтобы мониторить использование CPU и памяти короткоживущими процессами, которые иначе теряются при классическом мониторинге.",
    "Enable to group and separately analyze the processes of each IBM MQ Queue manager instance. Each process group receives a unique name based on the queue manager instance name.": "Включите, чтобы группировать и отдельно анализировать процессы каждого инстанса IBM MQ Queue manager. Каждая process group получает уникальное имя по имени инстанса queue manager.",
    "This flag enables the detection of security software, such as anti-malware protection. The currently detected utilities are Carbon Black EDR (on Windows only), CrowdStrike Falcon XDR and Trellix Endpoint Security (former McAfee).": "Этот флаг включает обнаружение security-софта, например антивирусной защиты. Сейчас обнаруживаются Carbon Black EDR (только Windows), CrowdStrike Falcon XDR и Trellix Endpoint Security (бывший McAfee).",
    "Enable to group and separately analyze the processes of each DB2 Instance. Each process receives a unique name based on the DB2 Instance name.": "Включите, чтобы группировать и отдельно анализировать процессы каждого DB2 Instance. Каждый процесс получает уникальное имя по имени DB2 Instance.",
    # process-grouping-rules
    "Note: Reported only in full-stack, infrastructure and discovery modes.": "Note: сообщается только в full-stack, infrastructure и discovery режимах.",
    "Define process groups and processes.": "Задайте process groups и процессы.",
    "When this field is empty, OneAgent will automatically assign the process group name based on process type and properties like executable name. If you expect that multiple processes will be matched by the rule, it is highly recommended that you fill this field because it is unspecified which process will be used as the group name source.": "Если поле пустое, OneAgent автоматически назначит имя process group по типу процесса и свойствам, таким как имя исполняемого файла. Если ожидается, что правило совпадёт с несколькими процессами, настоятельно рекомендуется заполнить поле, поскольку без него неопределено, какой процесс станет источником имени группы.",
    "Auto reports only processes which are important - meaning deep monitored or with high resource usage": "Auto сообщает только о важных процессах, то есть deep monitored или с высоким потреблением ресурсов",
    "Note: Not all types can be detected at startup.  Restrict this rule to specific process types to avoid mixing deep monitored properties leading to confusing results.": "Note: не все типы можно определить при старте.  Ограничьте правило конкретными типами процессов, чтобы не смешивать свойства deep monitored и не получать запутанные результаты.",
    "Define process detection rules to select processes on which this rule will apply to. **At least one rule must be defined.**": "Задайте правила обнаружения процессов, к которым применяется это правило. **Должно быть задано хотя бы одно правило.**",
    "**3.1. Process group id source**": "**3.1. Источник id для process group**",
    "**3.2. Process id source (optional)**  Define a property that should be used to identify your process.": "**3.2. Источник id для процесса (опц.)**  Задайте свойство, по которому идентифицируется процесс.",
    "If Dynatrace detects this property at startup of a process, it will be matched to this grouping rule.": "Если Dynatrace обнаруживает это свойство при старте процесса, процесс будет сопоставлен с этим правилом группировки.",
    "* $contains(svc) "
    + TM_ENDASH
    + " Matches if svc appears anywhere in the process property value. * $eq(svc.exe) "
    + TM_ENDASH
    + " Matches if svc.exe matches the process property value exactly. * $prefix(svc) "
    + TM_ENDASH
    + " Matches if app matches the prefix of the process property value. * $suffix(svc.py) "
    + TM_ENDASH
    + " Matches if svc.py matches the suffix of the process property value.  For example, $suffix(svc.py) would detect processes named loyaltysvc.py and paymentssvc.py.  For more details, see [documentation](https://dt-url.net/j142w57).": "* $contains(svc), совпадает, если svc встречается где-либо в значении свойства процесса. * $eq(svc.exe), совпадает, если svc.exe точно совпадает со значением свойства процесса. * $prefix(svc), совпадает, если app совпадает с префиксом значения свойства процесса. * $suffix(svc.py), совпадает, если svc.py совпадает с суффиксом значения свойства процесса.  Например, $suffix(svc.py) обнаружит процессы с именами loyaltysvc.py и paymentssvc.py.  Подробнее см. [documentation](https://dt-url.net/j142w57).",
    "When enabled, matching conditions are case sensitive. When disabled, matching conditions are case insensitive": "Если включено, условия совпадения учитывают регистр. Если выключено, регистр не учитывается",
    "Valid only for **deep monitored** processes.  If this option is selected, the default Dynatrace behavior is disabled for the detected processes. Only this rule is used to separate the process group.  If this option is not selected, this rule contributes to the default Dynatrace process group detection.  [See our help page for examples.](https://dt-url.net/1722wrz)": "Действительно только для **deep monitored** процессов.  Если параметр выбран, поведение Dynatrace по умолчанию для обнаруженных процессов отключается. Для разделения process group используется только это правило.  Если параметр не выбран, правило вносит вклад в стандартное обнаружение process group Dynatrace.  [See our help page for examples.](https://dt-url.net/1722wrz)",
    "Pick which property should be used to identify your process group. You can pick a custom variable or pick an existing process property.": "Выберите свойство, по которому идентифицируется process group. Можно взять custom-переменную или существующее свойство процесса.",
    "This identifier is used by Dynatrace to recognize this process group.": "Этот идентификатор используется Dynatrace для распознавания process group.",
    "If Dynatrace detects this property at startup of a process, it will use its value to identify process groups.": "Если Dynatrace обнаруживает это свойство при старте процесса, его значение используется для идентификации process group.",
    "Set advanced options to customize delimiters and control how property values are processed.  Consider an environment with processes such as:  * `python myScript.py --env=prod12 --id=12` * `python myScript.py --env=dev2 --id=2` * etc.  To group production *(prod)* and development *(dev)* processes together you could use Command line property with:  * **Delimiter** from `--env=` to `--id` to extract `prod12`  and `dev2` * Enable **Ignore numbers** to transform `prod12` to `prod*` and `dev2` to `dev*`.": "Задайте расширенные параметры для настройки delimiters и обработки значений свойств.  Рассмотрим среду с процессами вида:  * `python myScript.py --env=prod12 --id=12` * `python myScript.py --env=dev2 --id=2` * и т.п.  Чтобы сгруппировать production *(prod)* и development *(dev)* процессы вместе, можно использовать свойство Command line с:  * **Delimiter** от `--env=` до `--id` для извлечения `prod12`  и `dev2` * включить **Ignore numbers**, чтобы преобразовать `prod12` в `prod*` и `dev2` в `dev*`.",
    "If Dynatrace detects this property at startup of a process, it will use its value to identify process groups more granular.": "Если Dynatrace обнаруживает это свойство при старте процесса, его значение используется для более гранулярной идентификации process group.",
    "(e.g. versions, hex, dates, and build numbers)": "(например, версии, hex, даты, номера сборок)",
    # service-detection-* (общие)
    "Define a management zone of the process group for which this service detection rule should be created. Note: in case of external requests/services the PG might not always be known. See [here](https://dt-url.net/9i03b79)": "Задайте management zone process group, для которого создаётся это правило обнаружения сервиса. Note: в случае external requests/services PG может быть известен не всегда. См. [here](https://dt-url.net/9i03b79)",
    "Define a management zone of the process group for which this service detection rule should be created.": "Задайте management zone process group, для которого создаётся это правило обнаружения сервиса.",
    "Contributors to the Service Identifier calculation. All of the Contributors except for the port are always applied. You can exclude the port contribution by disabling the switch.": "Contributors для вычисления Service Identifier. Все Contributors, кроме порта, применяются всегда. Вклад порта можно исключить переключателем.",
    "Contributors to the Service Identifier calculation. URL path is always applied as an Id Contributor. You can exclude the port contribution by disabling the switch.": "Contributors для вычисления Service Identifier. URL path всегда применяется как Id Contributor. Вклад порта можно исключить переключателем.",
    "Contributors to the Service Identifier calculation. All of the Contributors are always applied.": "Contributors для вычисления Service Identifier. Все Contributors применяются всегда.",
    "A list of conditions necessary for the rule to take effect. If multiple conditions are specified, they must **all** match a Request for the rule to apply. If there is no condition at all, the rule is always applied. Conditions are evaluated against attributes, but do not modify them.": "Список условий, необходимых для применения правила. Если задано несколько условий, для применения правила должны совпасть **все** для Request. Если условий нет вовсе, правило применяется всегда. Условия оцениваются по атрибутам, но не модифицируют их.",
    "Let the port contribute to the Service Id": "Позволить порту вносить вклад в Service Id",
    "If multiple values are specified, at least one of them must match for the condition to match": "Если задано несколько значений, для совпадения условия должно совпасть хотя бы одно",
    "Ignore case sensitivity for texts.": "Игнорировать регистр для текстов.",
    "Defines whether the original value should be used or if a transformation set should be used to override a value or transform it.": "Определяет, использовать исходное значение или применить набор преобразований, чтобы переопределить или трансформировать его.",
    "The value to be used instead of the detected value.": "Значение, которое будет использовано вместо обнаруженного.",
    "Choose how to transform a value before it contributes to the Service Id. Note that all of the Transformations are always applied. Transformations are applied in the order they are specified, and the output of the previous transformation is the input for the next one. The resulting value contributes to the Service Id and can be found on the **Service overview page** under **Properties and tags**.": "Выберите, как трансформировать значение перед вкладом в Service Id. Учтите, все Transformations применяются всегда. Transformations применяются в заданном порядке, выход предыдущей трансформации поступает на вход следующей. Итоговое значение вносит вклад в Service Id и доступно на **Service overview page** в **Properties and tags**.",
    "The number of segments of the URL to be kept. The URL is divided by slashes (/), the indexing starts with 1 at context root. For example, if you specify 2 for the `www.dynatrace.com/support/help/dynatrace-api/` URL, the value of `support/help` is used.": "Количество сегментов URL, которые сохраняются. URL делится слешами (/), индексация начинается с 1 у context root. Например, если задать 2 для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`.",
    "The context root is the first segment of the request URL after the Server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `/support`. The context root value can be found on the **Service overview page** under **Properties and tags**.": "Context root, это первый сегмент request URL после Server name. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `/support`. Значение context root доступно на **Service overview page** в **Properties and tags**.",
    "Use the detected host name instead of the request's domain name.": "Использовать обнаруженное host name вместо доменного имени request.",
    "Defines what kind of transformation will be applied on the original value.": "Определяет, какой тип преобразования применяется к исходному значению.",
    "How many segments should be taken.": "Сколько сегментов нужно взять.",
    "Detect the matching requests as web request services instead of web services.  This prevents detecting of matching requests as opaque web services. An opaque web request service is created instead. If you need to further modify the resulting web request service, you need to create a separate Opaque/external web request rule (`<your-dynatrace-url>/builtin:service-detection.full-web-request`).": "Обнаруживать совпадающие requests как web request services, а не web services.  Это предотвращает обнаружение совпадающих requests как opaque web services; вместо этого создаётся opaque web request service. Чтобы дополнительно модифицировать результирующий web request service, создайте отдельное Opaque/external web request rule (`<your-dynatrace-url>/builtin:service-detection.full-web-request`).",
    "Detect the matching requests as full web services (false) or web request services (true).  Setting this field to true prevents detecting of matching requests as full web services. A web request service is created instead. If you need to further modify the resulting web request service, you need to create a separate Full web request rule (`<your-dynatrace-url>/builtin:service-detection.full-web-request`).": "Обнаруживать совпадающие requests как full web services (false) или web request services (true).  Установка в true предотвращает обнаружение совпадающих requests как full web services, вместо этого создаётся web request service. Чтобы дополнительно модифицировать результирующий web request service, создайте отдельное Full web request rule (`<your-dynatrace-url>/builtin:service-detection.full-web-request`).",
}

STRUCT = [
    ("* Published Dec 05, 2023", "* Опубликовано 05 декабря 2023"),
    ("* Published Jun 30, 2025", "* Опубликовано 30 июня 2025"),
    ("* Published May 05, 2025", "* Опубликовано 05 мая 2025"),
    ("| Schema ID | Schema groups | Scope |", "| Schema ID | Группы схемы | Scope |"),
    ("Retrieve schema via Settings API", "Получить schema через Settings API"),
    ("## Authentication", "## Аутентификация"),
    ("## Parameters", "## Параметры"),
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


# Process built-in monitoring rule rows: 80+ строк с уникальными лейблами вида
# "Do (not )?monitor processes if X `-N`" + "Rule id: N". Переводим их через
# отдельную regex-функцию, чтобы не плодить 80 ключей в PARAM_LABEL.
PROCESS_RULE_RE = _re.compile(
    r"^\| (Do not monitor processes if|Do monitor processes if) (.+?) (`-\d+`) \| boolean \| Rule id: (\d+) \| Required \|$"
)
PROCESS_RULE_HEAD = {
    "Do not monitor processes if": "Не мониторить процессы, если",
    "Do monitor processes if": "Мониторить процессы, если",
}
PROCESS_RULE_TAIL_TOKENS = [
    ("EXE name equals", "имя EXE равно"),
    ("EXE name contains", "имя EXE содержит"),
    ("EXE name begins with", "имя EXE начинается с"),
    ("EXE path begins with", "путь EXE начинается с"),
    ("EXE path equals", "путь EXE равен"),
    ("PHP script exists", "существует PHP-скрипт"),
    ("ASP.NET Core application path exists", "существует путь ASP.NET Core-приложения"),
    (
        "ASP.NET Core application DLL contains",
        "DLL ASP.NET Core-приложения содержит",
    ),
    ("Go Binary Linkage equals", "Go Binary Linkage равно"),
    (
        "Node.js application base directory ends with",
        "базовый каталог Node.js-приложения заканчивается на",
    ),
    ("Node.js application equals", "Node.js-приложение равно"),
    ("Node.js script equals", "Node.js-скрипт равен"),
    ("Cloud Foundry application begins with", "Cloud Foundry-приложение начинается с"),
    ("Cloud Foundry application exists", "Cloud Foundry-приложение существует"),
    ("Kubernetes container name equals", "имя Kubernetes-контейнера равно"),
    ("Kubernetes namespace exists", "Kubernetes namespace существует"),
    ("Docker stripped image contains", "Docker stripped image содержит"),
    ("Java JAR file begins with", "Java JAR-файл начинается с"),
    ("JAR file name equals", "имя JAR-файла равно"),
    ("container name exists", "имя контейнера существует"),
    ("command line arguments contain", "аргументы командной строки содержат"),
]


def _translate_process_rule_tail(tail):
    """Translate the variable tail of a process-monitoring rule label."""
    for en, ru in PROCESS_RULE_TAIL_TOKENS:
        if tail.startswith(en):
            rest = tail[len(en) :]
            return ru + rest
    return tail


def _process_rule_row(line):
    m = PROCESS_RULE_RE.match(line)
    if not m:
        return None
    head, tail, code, rule_id = m.groups()
    new_head = PROCESS_RULE_HEAD[head]
    new_tail = _translate_process_rule_tail(tail)
    return f"| {new_head} {new_tail} {code} | boolean | Rule id: {rule_id} | Required |"


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
        nl = (
            _heading(line)
            or _nested_heading(line)
            or _process_rule_row(line)
            or _param_row(line)
        )
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
