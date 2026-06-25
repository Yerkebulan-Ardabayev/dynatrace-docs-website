# -*- coding: utf-8 -*-
"""L4-AG.1a.8 builder: 9 builtin-*.md schema-table files (3.8-4.1 KB) from
docs/managed/dynatrace-api/environment-api/settings/schemas/.

Anchor canon: L4-AG.1a.7 _build_schemas_l4ag1a7.py.

Notes:
  - mojibake-BOM `ï»¿` (U+00EF U+00BB U+00BF) is stripped by _normalize()
    BEFORE SCHEMA_DESC/PARAM_DESC passes. EN keys MUST NOT contain BOMJ
    (L4-AG.1a.7 canon). RU translations also drop the mojibake-BOM.
  - Twin pair: anomaly-detection-rum-{mobile,custom}-crash-rate-increase share
    everything except DISPLAY_NAME — consolidated in one dict pass.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-kubernetes-generic-metadata-enrichment.md",
    "builtin-appsec-third-party-vulnerability-kubernetes-label-rule-settings.md",
    "builtin-logmonitoring-timestamp-configuration.md",
    "builtin-davis-anomaly-detectors.md",
    "builtin-anomaly-detection-rum-mobile-crash-rate-increase.md",
    "builtin-logmonitoring-custom-log-source-settings.md",
    "builtin-anomaly-detection-rum-custom-crash-rate-increase.md",
    "builtin-container-built-in-monitoring-rule.md",
    "builtin-cloud-kubernetes-monitoring.md",
]

DISPLAY_NAME = {
    "Kubernetes Telemetry Enrichment": "Обогащение телеметрии Kubernetes",
    "Vulnerability Analytics: Kubernetes monitoring rules for third-party vulnerabilities": "Vulnerability Analytics: правила мониторинга Kubernetes для third-party-уязвимостей",
    "Timestamp/Splitting patterns": "Шаблоны временной метки и разбиения",
    "Anomaly detectors": "Детекторы аномалий",
    "Crash rate increase settings for mobile applications": "Настройки роста crash rate для mobile-приложений",
    "Custom log sources": "Пользовательские источники логов",
    "Crash rate increase settings for custom applications": "Настройки роста crash rate для custom-приложений",
    "Built-in container monitoring rules": "Встроенные правила мониторинга контейнеров",
    "Monitoring settings": "Параметры мониторинга",
}

SCHEMA_DESC = {
    # 1. kubernetes-generic-metadata-enrichment
    "Generic metadata enrichment for Kubernetes.": "Обогащение телеметрии произвольной метадатой для Kubernetes.",
    # 2. appsec-third-party-vulnerability-kubernetes-label-rule-settings
    "The global third-party vulnerability detection control defines the default for all Kubernetes hosts. To override the default, define custom monitoring rules here. Note that monitoring rules are ordered; the first matching rule applies.": "Глобальный контроль обнаружения third-party-уязвимостей задаёт значение по умолчанию для всех Kubernetes-хостов. Чтобы переопределить значение по умолчанию, задайте здесь пользовательские правила мониторинга. Правила мониторинга упорядочены: применяется первое совпавшее правило.",
    # 3. logmonitoring-timestamp-configuration (2 paragraphs)
    "Dynatrace OneAgent detects number of timestamp formats in your log records. In case of custom timestamps included in log record define them below. This will assure data quality for analysis.": "Dynatrace OneAgent распознаёт ряд форматов временных меток в записях логов. Если в записи лога используются нестандартные временные метки, задайте их ниже. Это обеспечит качество данных для анализа.",
    "Timestamp detection also influence proper log splitting. If no timestamp is detected or log format prevents auto-timestamping, adjacent lines can be merged into single log record (also indentations are considered).": "Распознавание временной метки также влияет на корректное разбиение лога. Если временная метка не обнаружена или формат лога не позволяет автораспознавание, соседние строки могут быть объединены в одну запись лога (учитываются и отступы).",
    # 4. davis-anomaly-detectors
    "Anomaly detectors are used to automatically detect anomalies in timeseries by using thresholds or baselines.": "Детекторы аномалий используются для автоматического обнаружения аномалий во временных рядах через пороги или baseline.",
    # 5+7. anomaly-detection-rum-{mobile,custom}-crash-rate-increase (twin, identical SCHEMA_DESC)
    "Dynatrace automatically detects application-related performance anomalies such as failure rate increases. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for certain applications.": "Dynatrace автоматически обнаруживает аномалии производительности, связанные с приложениями, например рост failure rate. Используйте эти параметры для настройки чувствительности обнаружения, задания порогов оповещений или отключения оповещений для отдельных приложений.",
    'To avoid false-positive problem notifications, [automated anomaly detection](https://dt-url.net/op03t6j "Visit Dynatrace support center") is only available for applications and services that have run for at least 20% of a week (7 days).': 'Чтобы избежать ложноположительных уведомлений о проблемах, [automated anomaly detection](https://dt-url.net/op03t6j "Visit Dynatrace support center") доступно только для приложений и сервисов, проработавших как минимум 20% недели (7 дней).',
    # 6. logmonitoring-custom-log-source-settings (multi-line description with bullets)
    "Add custom log sources before creating log ingest rule in case of:": "Добавьте пользовательские источники логов до создания правила ingest логов в случае, когда:",
    "* process is not important (this mean that log source is not automatically discovered by OneAgent)": "* процесс не является важным (то есть источник лога не определяется OneAgent автоматически)",
    "* logs from Windows event logs (other than Windows system log, Windows security log, or Windows Application log)": "* нужны логи Windows event logs (кроме Windows system log, Windows security log и Windows Application log)",
    "* AIX logs": "* нужны логи AIX",
    "* allowing binary content": "* нужно разрешить бинарный контент",
    "* unsupported rotation pattern": "* используется неподдерживаемый шаблон ротации",
    "OneAgent automatically discovers new log files for important processes on supported platforms. Auto-detected logs are listed on the Process Group Instance or Host screen.": "OneAgent автоматически обнаруживает новые файлы логов для важных процессов на поддерживаемых платформах. Автоматически обнаруженные логи перечислены на экранах Process Group Instance или Host.",
    # 8. container-built-in-monitoring-rule
    "Dynatrace disables monitoring of containers that do not run any applications.": "Dynatrace отключает мониторинг контейнеров, в которых не запущены приложения.",
    # 9. cloud-kubernetes-monitoring
    "Configure the monitoring features for Kubernetes or OpenShift. Learn more about those features in our [documentation](https://dt-url.net/2ma0vhp).": "Настройте функции мониторинга для Kubernetes или OpenShift. Подробнее об этих функциях см. в [documentation](https://dt-url.net/2ma0vhp).",
}

PARAM_LABEL = {
    # Shared
    "Enabled": "Включено",
    "Active": "Активно",
    "Name": "Имя",
    "Description": "Описание",
    "Source": "Источник",
    "Title": "Заголовок",
    "Key": "Ключ",
    "Value": "Значение",
    "Matcher": "Сопоставитель",
    "Operator": "Оператор",
    "Attribute": "Атрибут",
    "Comment": "Комментарий",
    "Encoding": "Кодировка",
    "type": "тип",
    "key": "ключ",
    "value": "значение",
    # 1. kubernetes-generic-metadata-enrichment
    "Metadata type": "Тип метадаты",
    "Enrich telemetry with label/annotation directly": "Обогащать телеметрию label/annotation напрямую",
    "Target": "Цель",
    # 2. appsec-third-party-vulnerability-kubernetes-label-rule-settings
    "Rule name": "Имя правила",
    "Step 1: Select third-party vulnerability detection behavior": "Шаг 1: выберите поведение обнаружения third-party-уязвимостей",
    "Step 2: Specify where the rule is applied (optional)": "Шаг 2: укажите, где применяется правило (опционально)",
    "Step 3: Leave comment (optional)": "Шаг 3: оставьте комментарий (опционально)",
    "Third-party vulnerability control": "Контроль third-party-уязвимостей",
    "Kubernetes label key": "Ключ Kubernetes-метки",
    "Kubernetes label value": "Значение Kubernetes-метки",
    # 3. logmonitoring-timestamp-configuration
    "Date-time pattern": "Шаблон даты и времени",
    "Timezone": "Часовой пояс",
    "Timestamp search limit": "Лимит поиска временной метки",
    "Skip indented lines": "Пропускать строки с отступом",
    "Entry boundary pattern": "Шаблон границы записи",
    "Detect JSON format": "Распознавать JSON-формат",
    # 4. davis-anomaly-detectors
    "Execution settings": "Параметры выполнения",
    "Analyzer input": "Вход анализатора",
    "Event template": "Шаблон события",
    "Actor": "Актор",
    "Query offset": "Сдвиг запроса",
    "Execution delay": "Задержка выполнения",
    "Input fields": "Входные поля",
    "Event properties": "Свойства события",
    # 5+7. anomaly-detection-rum-{mobile,custom}-crash-rate-increase
    "Crash rate increase": "Рост crash rate",
    "Detect crash rate increase": "Обнаруживать рост crash rate",
    "Detection strategy for crash rate increases": "Стратегия обнаружения роста crash rate",
    "Relative threshold": "Относительный порог",
    "Absolute threshold": "Абсолютный порог",
    "Minimum number of active, non-distinctive users": "Минимальное число активных, неидентифицируемых пользователей",
    "Detection sensitivity": "Чувствительность обнаружения",
    # 6. logmonitoring-custom-log-source-settings
    "Log Source context": "Контекст источника лога",
    "Log Source type": "Тип источника лога",
    "Accept binary content": "Принимать бинарный контент",
    "Log source": "Источник лога",
    "Values": "Значения",
    "Enrichments": "Обогащения",
    # 8. container-built-in-monitoring-rule
    "Do not monitor containers where Kubernetes container name equals 'POD'": "Не мониторить контейнеры, у которых имя Kubernetes-контейнера равно 'POD'",
    "Do not monitor containers where Docker stripped image name contains 'pause-amd64'": "Не мониторить контейнеры, у которых stripped имя Docker-образа содержит 'pause-amd64'",
    "Do not monitor containers where Kubernetes namespace equals 'openshift-sdn'": "Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-sdn'",
    "Do not monitor containers where Kubernetes full pod name ends with '-build'": "Не мониторить контейнеры, у которых полное имя Kubernetes-pod заканчивается на '-build'",
    "Do not monitor containers where Kubernetes namespace equals 'openshift-ovn-kubernetes'": "Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-ovn-kubernetes'",
    "Do not monitor containers where Kubernetes namespace equals 'openshift-etcd'": "Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-etcd'",
    "Do not monitor containers where Kubernetes namespace equals 'openshift-kube-apiserver'": "Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-kube-apiserver'",
    "Do not monitor containers where Kubernetes namespace equals 'openshift-monitoring'": "Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-monitoring'",
    "Do not monitor containers where Kubernetes namespace equals 'openshift-machine-config-operator'": "Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-machine-config-operator'",
    "Do not monitor containers where Kubernetes namespace equals 'openshift-ingress-canary'": "Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-ingress-canary'",
    # 9. cloud-kubernetes-monitoring
    "Monitor Kubernetes namespaces, services, workloads, and pods": "Мониторить namespace, сервисы, workload и pod в Kubernetes",
    "Monitor annotated Prometheus exporters": "Мониторить аннотированные Prometheus-экспортёры",
    "Monitor workload and node resource metrics": "Мониторить метрики ресурсов workload и узла",
    "Monitor events": "Мониторить события",
    "Filter events": "Фильтровать события",
    "Include important events": "Включать важные события",
    "Events field selectors": "Селекторы полей событий",
    "Field selector name": "Имя селектора поля",
    "Field selector expression": "Выражение селектора поля",
    "Activate": "Активировать",
}

PARAM_DESC = {
    # 1. kubernetes-generic-metadata-enrichment (huge multi-paragraph desc)
    "Kubernetes Telemetry Enrichment empowers you to effectively tag your telemetry data using Kubernetes namespace labels and annotations. Additionally, it enables you to tag it for cost allocation and permission purposes.  Enrichment Options:  * **Enrich telemetry with label/annotation directly:** Tag your telemetry data with existing Kubernetes namespace labels or annotations. These will be made available as domain-specific fields (e.g., `k8s.namespace.label.your_key`). This allows for flexible pipeline routing, bucket selection, segmentation, and filtering. * **Security Context and Cost Allocation:** Leverage existing Kubernetes namespace labels or annotations as the basis for security context or cost allocation. This provides granular control over permissions and facilitates chargeback functionalities.  Additional Information:  * Only namespace-level labels or annotations can be used as source. * You can define up to 20 enrichment rules. * New rules may take up to 45 minutes to take effect. * Pod restarts are required after the 45 mins to ensure the changes take effect.  To learn more, please refer to our [documentation](https://dt-url.net/pn22sye).": "Обогащение телеметрии Kubernetes позволяет эффективно тегировать данные телеметрии через Kubernetes-метки и аннотации namespace. Кроме того, позволяет тегировать данные для cost allocation и управления правами.  Варианты обогащения:  * **Обогащать телеметрию label/annotation напрямую:** тегируйте данные телеметрии существующими Kubernetes-метками или аннотациями namespace. Они будут доступны как domain-specific поля (например, `k8s.namespace.label.your_key`). Это даёт гибкое pipeline-маршрутизирование, выбор bucket, сегментацию и фильтрацию. * **Security Context и Cost Allocation:** используйте существующие Kubernetes-метки или аннотации namespace как основу для security context или cost allocation. Это даёт гранулярный контроль над правами и поддерживает chargeback-функциональность.  Дополнительная информация:  * Источником могут быть только метки или аннотации уровня namespace. * Можно задать до 20 правил обогащения. * Новые правила могут вступать в силу до 45 минут. * После 45 минут требуется перезапуск pod, чтобы изменения вступили в силу.  Подробнее см. в нашей [documentation](https://dt-url.net/pn22sye).",
    "The source must follow the syntax of Kubernetes annotation/label keys as defined in the [Kubernetes documentation](https://dt-url.net/2c02sbn).  `source := (prefix/)?name`  `prefix := a-z0-9 (`/[-a-z0-9]*[a-z0-9]`)?(\\.a-z0-9 (`/[-a-z0-9]*[a-z0-9]`)?)*`  `name := ([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]`  Additionally, the name can have at most 63 characters, and the overall length of the source must not exceed 75 characters.": "Источник должен следовать синтаксису ключей Kubernetes-аннотаций и меток, описанному в [Kubernetes documentation](https://dt-url.net/2c02sbn).  `source := (prefix/)?name`  `prefix := a-z0-9 (`/[-a-z0-9]*[a-z0-9]`)?(\\.a-z0-9 (`/[-a-z0-9]*[a-z0-9]`)?)*`  `name := ([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]`  Дополнительно: имя может содержать максимум 63 символа, а общая длина source не должна превышать 75 символов.",
    "Uses the key of the annotation or label as field name directly": "Использует ключ аннотации или метки напрямую как имя поля",
    # 2. appsec-third-party-vulnerability-kubernetes-label-rule-settings (shared with appsec-*)
    "When you add multiple conditions, the rule applies if all conditions apply.  If you want the rule to apply only to a subset of your environment, provide the Kubernetes label that should be used to identify that part of the environment.": "При добавлении нескольких условий правило применяется, если применяются все условия.  Если правило должно применяться только к части окружения, укажите Kubernetes-метку, по которой эту часть окружения нужно определить.",
    # 3. logmonitoring-timestamp-configuration
    "Defines the number of characters in every log line (starting from the first character in the line) where the timestamp is searched.": "Задаёт количество символов в каждой строке лога (начиная с первого символа), в которых ищется временная метка.",
    "Don't parse timestamps in lines starting with white character": "Не парсить временные метки в строках, начинающихся с пробельного символа",
    "Optional field. Enter a fragment of the line text that starts the entry. No support for wildcards - the text is treated literally. ": "Опциональное поле. Введите фрагмент текста строки, с которой начинается запись. Wildcard не поддерживаются, текст трактуется буквально. ",
    "Optional field. Enter a fragment of the line text that starts the entry. No support for wildcards - the text is treated literally.": "Опциональное поле. Введите фрагмент текста строки, с которой начинается запись. Wildcard не поддерживаются, текст трактуется буквально.",
    # 4. davis-anomaly-detectors
    "When enabled, the anomaly detector will be active and running.": "Если включено, детектор аномалий будет активен и работать.",
    "The title of the anomaly detector": "Заголовок детектора аномалий",
    "The description of the anomaly detector": "Описание детектора аномалий",
    "The source which created the anomaly detector": "Источник, создавший детектор аномалий",
    "Defines the configuration parameters that influence how and under what context a query or evaluation is executed.": "Задаёт параметры конфигурации, влияющие на то, как и в каком контексте выполняется запрос или вычисление.",
    "Analyzer input to initialize the analyzer": "Вход анализатора для его инициализации",
    "Defines additional fields on the davis events triggered by the anomaly detector": "Задаёт дополнительные поля для davis-событий, запускаемых детектором аномалий",
    "UUID of a service user. Queries will be executed on behalf of the service user.": "UUID сервисного пользователя. Запросы выполняются от имени сервисного пользователя.",
    "Minute offset of sliding evaluation window for metrics with latency": "Сдвиг скользящего окна вычисления (в минутах) для метрик с задержкой",
    "Fixed delay between executions (in seconds)": "Фиксированная задержка между выполнениями (в секундах)",
    "Fully qualified name of the analyzer": "Полное квалифицированное имя анализатора",
    "Input fields for the specified analyzer": "Входные поля для указанного анализатора",
    "Set of additional key-value properties to be attached to the triggered event.": "Набор дополнительных key-value-свойств, прикрепляемых к запущенному событию.",
    "Analyzer input field key": "Ключ поля входа анализатора",
    "Analyzer input field value": "Значение поля входа анализатора",
    "Property key": "Ключ свойства",
    "Property value. Supports substitution of placeholders placed in curly braces {}.": "Значение свойства. Поддерживает подстановку placeholder'ов в фигурных скобках {}.",
    # 5+7. anomaly-detection-rum-{mobile,custom}-crash-rate-increase (twin shared)
    "Alert to crash rate increases when the auto-detected baseline is exceeded and the application has a minimum number of active, non-distinctive users.": "Оповещать о росте crash rate, когда автообнаруженный baseline превышен, а у приложения есть минимальное число активных, неидентифицируемых пользователей.",
    "Alert to crash rate increases when the defined threshold is exceeded and the application has a minimum number of active, non-distinctive users.": "Оповещать о росте crash rate, когда заданный порог превышен, а у приложения есть минимальное число активных, неидентифицируемых пользователей.",
    "Dynatrace learns the typical crash rate for all app versions and will create an alert if the baseline is violated by more than a specified threshold. Analysis happens based on a sliding window of 10 minutes.": "Dynatrace обучается типичному crash rate для всех версий приложения и создаёт оповещение, если baseline нарушен сильнее заданного порога. Анализ выполняется по скользящему окну в 10 минут.",
    # 6. logmonitoring-custom-log-source-settings
    "Define Custom Log Source only within context if provided": "Определять пользовательский источник лога только в контексте, если он задан",
    "It might be either an absolute path to log(s) with optional wildcards or Windows Event Log name.": "Это может быть абсолютный путь к лог-файлу(ам) с опциональными wildcard либо имя Windows Event Log.",
    "Optional field that allows to define attributes that will enrich logs  ${N} can be used in attribute value to expand the value matched by wildcards where N denotes the number of the wildcard the expand": "Опциональное поле, позволяющее задать атрибуты, которые обогатят логи.  ${N} можно использовать в значении атрибута, чтобы подставить значение, совпавшее с wildcard; здесь N означает номер wildcard для подстановки",
    # 8. container-built-in-monitoring-rule
    "Disable monitoring of platform internal pause containers in Kubernetes and OpenShift.": "Отключить мониторинг внутренних pause-контейнеров платформы в Kubernetes и OpenShift.",
    "Disable monitoring of platform internal containers in the openshift-sdn namespace.": "Отключить мониторинг внутренних контейнеров платформы в namespace openshift-sdn.",
    "Disable monitoring of intermediate containers created during image build.": "Отключить мониторинг промежуточных контейнеров, создаваемых при сборке образа.",
    "Disable monitoring of platform internal containers in the openshift-ovn-kubernetes namespace.": "Отключить мониторинг внутренних контейнеров платформы в namespace openshift-ovn-kubernetes.",
    "Disable monitoring of platform internal containers in the openshift-etcd namespace.": "Отключить мониторинг внутренних контейнеров платформы в namespace openshift-etcd.",
    "Disable monitoring of platform internal containers in the openshift-kube-apiserver namespace.": "Отключить мониторинг внутренних контейнеров платформы в namespace openshift-kube-apiserver.",
    "Disable monitoring of platform internal containers in the openshift-monitoring namespace.": "Отключить мониторинг внутренних контейнеров платформы в namespace openshift-monitoring.",
    "Disable monitoring of platform internal containers in the openshift-machine-config-operator namespace.": "Отключить мониторинг внутренних контейнеров платформы в namespace openshift-machine-config-operator.",
    "Disable monitoring of platform internal containers in the openshift-ingress-canary namespace.": "Отключить мониторинг внутренних контейнеров платформы в namespace openshift-ingress-canary.",
    # 9. cloud-kubernetes-monitoring
    "For annotation guidance, see the [documentation](https://dt-url.net/g42i0ppw).  Prometheus metrics in kubernetes environments are subject to licensing.  If you have DPS licensing see [licensing documentation](https://dt-url.net/nd0348b) for details.  If you have non-DPS licensing see [Monitoring consumption](https://dt-url.net/k8smpm) for details.": "Руководство по аннотациям см. в [documentation](https://dt-url.net/g42i0ppw).  Метрики Prometheus в Kubernetes-окружениях подпадают под лицензирование.  Если у вас DPS-лицензирование, подробности см. в [licensing documentation](https://dt-url.net/nd0348b).  Если у вас не-DPS-лицензирование, подробности см. в [Monitoring consumption](https://dt-url.net/k8smpm).",
    "Workload and node resource metrics are based on a subset of cAdvisor metrics. Depending on your Kubernetes cluster size, this may increase the CPU/memory resource consumption of your ActiveGate. Node resource metrics require ActiveGate 1.271+": "Метрики ресурсов workload и узла основаны на подмножестве cAdvisor-метрик. В зависимости от размера Kubernetes-кластера это может увеличить потребление CPU/памяти ActiveGate. Для метрик ресурсов узла требуется ActiveGate 1.271+",
    "All events are monitored unless event filters are specified. All ingested events are subject to licensing by default.  If you have a DPS license see [licensing documentation](https://dt-url.net/cee34zj) for details.  If you have a non-DPS license see [DDUs for events](https://dt-url.net/5n03vcu) for details.": "Все события мониторятся, если не заданы фильтры событий. Все принятые события по умолчанию подпадают под лицензирование.  Если у вас DPS-лицензия, подробности см. в [licensing documentation](https://dt-url.net/cee34zj).  Если у вас не-DPS-лицензия, подробности см. в [DDUs for events](https://dt-url.net/5n03vcu).",
    "Include only events specified by Events Field Selectors": "Включать только события, заданные через Events Field Selectors",
    "For a list of included events, see the [documentation](https://dt-url.net/l61d02no).  Automatically include all events that are relevant for Davis": "Список включённых событий см. в [documentation](https://dt-url.net/l61d02no).  Автоматически включать все события, релевантные для Davis",
    "Define Kubernetes event filters to ingest events into your environment. For more details, see the [documentation](https://dt-url.net/2201p0u).": "Задайте фильтры событий Kubernetes для ingest событий в окружение. Подробнее см. в [documentation](https://dt-url.net/2201p0u).",
    "The set of allowed characters for this field has been extended with ActiveGate version 1.259. For more details, see the [documentation](https://dt-url.net/7h23wuk#set-up-event-field-selectors).": "Набор допустимых символов для этого поля расширен в ActiveGate версии 1.259. Подробнее см. в [documentation](https://dt-url.net/7h23wuk#set-up-event-field-selectors).",
}

# Structural canon (shared with L4-AG.1a.1-7 / L4-AF).
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
