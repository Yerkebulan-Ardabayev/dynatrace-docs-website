# -*- coding: utf-8 -*-
"""L4-AG.1a.7 builder: 10 builtin-*.md schema-table files (3.5-3.8 KB) from
docs/managed/dynatrace-api/environment-api/settings/schemas/.

Anchor canon: L4-AG.1a.6 _build_schemas_l4ag1a6.py.

Notable mojibake in this batch:
  - mojibake-BOM `ï»¿` (U+00EF U+00BB U+00BF) embedded inside hyperlink texts
    in 5/10 files. Translation drops the mojibake-BOM in RU equivalents
    (line-parity preserved, mojibake-drift acceptable per L4-AG.1a.6 lesson 1).
  - mojibake `â ï¸` (warning emoji ⚠️ double-decoded) preserved verbatim
    in disk-options PARAM_DESC long prose since translated cdesc replaces
    whole-string.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

# Mojibake BOM embedded in hyperlink texts (6 bytes UTF-8).
BOMJ = chr(0xEF) + chr(0xBB) + chr(0xBF)
# Mojibake warning emoji ⚠️ — double-decoded U+26A0 U+FE0F.
# Real bytes: c3 a2 c2 9a c2 a0 c3 af c2 b8 c2 8f
# (6 chars: U+00E2 U+009A U+00A0 U+00EF U+00B8 U+008F) — visually `â ï¸`.
WARN = chr(0xE2) + chr(0x9A) + chr(0xA0) + chr(0xEF) + chr(0xB8) + chr(0x8F)

PILOT = [
    "builtin-hyperscaler-authentication-connections-azure.md",
    "builtin-disk-options.md",
    "builtin-mainframe-txmonitoring.md",
    "builtin-rum-web-key-performance-metric-load-actions.md",
    "builtin-container-technology.md",
    "builtin-oneagent-side-masking-settings.md",
    "builtin-anomaly-detection-kubernetes-pvc.md",
    "builtin-appsec-code-level-vulnerability-rule-settings.md",
    "builtin-appsec-third-party-vulnerability-rule-settings.md",
    "builtin-failure-detection-service-http-parameters.md",
]

# Schema heading display-name.
DISPLAY_NAME = {
    "Connections to Azure environments": "Подключения к Azure-окружениям",
    "Disk options": "Параметры диска",
    "Transaction monitoring": "Мониторинг транзакций",
    "Apdex configuration for load actions": "Настройка Apdex для load-действий",
    "Container monitoring": "Мониторинг контейнеров",
    "OneAgent side masking": "Маскирование на стороне OneAgent",
    "Kubernetes persistent volume claim anomaly detection": "Обнаружение аномалий Kubernetes persistent volume claim",
    "Vulnerability Analytics: Monitoring rules for code-level vulnerabilities": "Vulnerability Analytics: правила мониторинга для уязвимостей уровня кода",
    "Vulnerability Analytics: Monitoring rules for third-party vulnerabilities": "Vulnerability Analytics: правила мониторинга для third-party-уязвимостей",
    "HTTP failure detection parameters": "Параметры обнаружения HTTP-сбоев",
}

# Whole-line schema descriptions (replaced as \n + EN + \n -> \n + RU + \n).
SCHEMA_DESC = {
    # 1. hyperscaler-authentication-connections-azure
    "Connections to Azure for Dynatrace integrations": "Подключения к Azure для интеграций Dynatrace",
    # 2. disk-options
    "Disk options settings control the visibility of local disks on your hosts.": "Параметры диска управляют видимостью локальных дисков на хостах.",
    # 3. mainframe-txmonitoring
    "Define additional monitoring settings for CICS and IMS transactions.": "Задайте дополнительные параметры мониторинга для транзакций CICS и IMS.",
    # 4. rum-web-key-performance-metric-load-actions
    # NOTE: mojibake-BOM `ï»¿` is stripped by _normalize() BEFORE SCHEMA_DESC
    # passes, so EN keys must NOT contain BOMJ (canon: L4-AG.1a.7 lesson).
    "Select a key performance metric and set the Tolerating and Frustrated performance thresholds to [refine the Apdex calculations](https://dt-url.net/apdex-thresholds) for this application.": "Выберите ключевую метрику производительности и задайте пороги Tolerating и Frustrated, чтобы [refine the Apdex calculations](https://dt-url.net/apdex-thresholds) для этого приложения.",
    # 5. container-technology
    "Enable/disable automatic injection of code modules into specific containers.": "Включайте и отключайте автоматическую инъекцию модулей кода в конкретные контейнеры.",
    'Dynatrace OneAgent automatically monitors all processes that are running on your monitored hosts. Within container environments (for example, Kubernetes, OpenShift, Cloud Foundry, or Docker), OneAgent automatically injects code modules into containerized processes to provide out of the box full-stack visibility into applications running within containers. Enabling auto-injection provides deep monitoring for all processes within containers, at both the request- and PurePath levels. If disabled, OneAgent will not inject into a container of a specific type at all. Dynatrace provides complete control over automatic injection of code modules into the container technologies listed below. For full details see [Supported container versions](https://dt-url.net/lmy0p0j "Visit Dynatrace support center").': 'Dynatrace OneAgent автоматически мониторит все процессы, запущенные на мониторимых хостах. В контейнерных окружениях (например, Kubernetes, OpenShift, Cloud Foundry или Docker) OneAgent автоматически инъецирует модули кода в контейнеризованные процессы, чтобы обеспечить full-stack-наблюдаемость «из коробки» для приложений, работающих внутри контейнеров. Включение auto-injection даёт deep monitoring для всех процессов в контейнерах на уровнях request и PurePath. При отключении OneAgent не будет инъецировать в контейнеры конкретного типа вообще. Dynatrace даёт полный контроль над автоматической инъекцией модулей кода в перечисленные ниже контейнерные технологии. Подробности см. [Supported container versions](https://dt-url.net/lmy0p0j "Visit Dynatrace support center").',
    # 6. oneagent-side-masking-settings
    "Use the settings on this page to exclude sensitive data from exceptions and URLs captured directly by OneAgent, so it never leaves your environment. The settings below are executed directly on the OneAgent and will exclude the data points from being sent to Dynatrace servers. These data points will no longer be available to you in Dynatrace.": "Используйте параметры на этой странице, чтобы исключить чувствительные данные из исключений и URL, захватываемых напрямую OneAgent, так чтобы они не покидали окружение. Параметры ниже выполняются непосредственно на OneAgent и исключают точки данных из отправки на серверы Dynatrace. Эти точки данных больше не будут доступны в Dynatrace.",
    "Note: The RUM JavaScript is **not** affected by these settings!": "Примечание: RUM JavaScript эти параметры **не** затрагивают!",
    "A detailed reference and change log can be found [here](https://dt-url.net/kd039dm).": "Подробный справочник и журнал изменений см. [here](https://dt-url.net/kd039dm).",
    # 7. anomaly-detection-kubernetes-pvc
    "Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes persistent volume claims. Changing thresholds resets the observation period. Additional information can be found on our [documentation page](https://dt-url.net/wq02okj#persistent-volume-claims).": "Dynatrace автоматически обнаруживает широкий спектр распространённых проблем, связанных с Kubernetes. Используйте эти параметры для настройки оповещений по вашим Kubernetes persistent volume claim. Изменение порогов сбрасывает период наблюдения. Подробности см. на [documentation page](https://dt-url.net/wq02okj#persistent-volume-claims).",
    # 8+9. appsec-{code-level,third-party}-vulnerability-rule-settings
    "The global code-level vulnerability detection control defines the default per technology for all process groups. To override the default, define custom monitoring rules here. Note that monitoring rules are ordered; the first matching rule applies.": "Глобальный контроль обнаружения уязвимостей уровня кода задаёт значение по умолчанию для каждой технологии для всех process group. Чтобы переопределить значение по умолчанию, задайте здесь пользовательские правила мониторинга. Правила мониторинга упорядочены: применяется первое совпавшее правило.",
    "The global third-party vulnerability detection control defines the default per technology for all process groups. To override the default, define custom monitoring rules here. Note that monitoring rules are ordered; the first matching rule applies.": "Глобальный контроль обнаружения third-party-уязвимостей задаёт значение по умолчанию для каждой технологии для всех process group. Чтобы переопределить значение по умолчанию, задайте здесь пользовательские правила мониторинга. Правила мониторинга упорядочены: применяется первое совпавшее правило.",
    # 10. failure-detection-service-http-parameters
    "Dynatrace failure detection automatically detects the vast majority of error conditions in your environment. However, detected service errors don't necessarily mean that the underlying requests have failed. There may be cases where the default service failure detection settings don't meet your particular needs. In such cases, you can configure the settings provided below. Please note that these settings are not applicable to services of type 'Span service'. For complete details, see [configure service failure detection](https://dt-url.net/ys5k0p4y).": "Dynatrace failure detection автоматически обнаруживает подавляющее большинство ошибок в окружении. Однако обнаруженные ошибки сервиса не обязательно означают, что соответствующие запросы провалились. Бывают случаи, когда параметры обнаружения сбоев сервиса по умолчанию не отвечают конкретным потребностям, в таких случаях можно настроить параметры ниже. Учтите: эти параметры не применяются к сервисам типа 'Span service'. Подробности см. [configure service failure detection](https://dt-url.net/ys5k0p4y).",
}

# Parameter table col-1 labels (translated when present).
PARAM_LABEL = {
    # Shared
    "Enabled": "Включено",
    "Name": "Имя",
    "Description": "Описание",
    "Key": "Ключ",
    "Value": "Значение",
    "Source": "Источник",
    "Matcher": "Сопоставитель",
    "Operator": "Оператор",
    "Title": "Заголовок",
    "Comment": "Комментарий",
    # 1. hyperscaler-authentication-connections-azure
    "Connection Type": "Тип подключения",
    "Directory (tenant) ID": "ID каталога (tenant)",
    "Application (client) ID": "ID приложения (client)",
    "Client secret": "Client secret",
    "Consumers": "Потребители",
    # 2. disk-options
    "Show all NFS mount points": "Показывать все NFS-точки монтирования",
    "Disable NFS disk monitoring": "Отключить мониторинг NFS-дисков",
    "Enable tmpfs disk monitoring": "Включить мониторинг tmpfs-дисков",
    "Exclude disks": "Исключённые диски",
    "Operating system": "Операционная система",
    "Disk or mount point path": "Путь к диску или точке монтирования",
    "File system type": "Тип файловой системы",
    # 3. mainframe-txmonitoring
    "Monitor all incoming web requests": "Мониторить все входящие web-запросы",
    "Monitor all EXCI requests from CICS Transaction Gateway": "Мониторить все EXCI-запросы от CICS Transaction Gateway",
    "Group CICS regions that belong to the same CICSPlex": "Группировать CICS-регионы из одного CICSPlex",
    "Create CICS services based on transaction IDs": "Создавать CICS-сервисы на основе transaction ID",
    "Group IMS regions that belong to the same subsystem": "Группировать IMS-регионы из одной подсистемы",
    "Create IMS services based on transaction IDs": "Создавать IMS-сервисы на основе transaction ID",
    "PurePath node limit: maximum number of nodes per CICS/IMS program call": "Лимит узлов PurePath: максимальное число узлов на вызов CICS/IMS-программы",
    # 4. rum-web-key-performance-metric-load-actions
    "Key performance metric": "Ключевая метрика производительности",
    "Key performance metric thresholds": "Пороги ключевой метрики производительности",
    "Fallback metric thresholds": "Пороги fallback-метрики",
    "Tolerating threshold": "Порог Tolerating",
    "Frustrated threshold": "Порог Frustrated",
    "Tolerating threshold [sec]": "Порог Tolerating [сек]",
    "Frustrated threshold [sec]": "Порог Frustrated [сек]",
    # 5. container-technology
    "BOSH Process Manager (BPM) containers": "Контейнеры BOSH Process Manager (BPM)",
    "Containerd containers": "Контейнеры Containerd",
    "CRI-O containers": "Контейнеры CRI-O",
    "Docker containers": "Контейнеры Docker",
    "Docker for Windows Server containers": "Контейнеры Docker для Windows Server",
    "Garden containers": "Контейнеры Garden",
    "Winc for Windows Server containers": "Контейнеры Winc для Windows Server",
    "Podman containers": "Контейнеры Podman",
    # 6. oneagent-side-masking-settings
    "Email addresses": "Email-адреса",
    "Query parameters": "Параметры запроса",
    "Financial and payment card numbers": "Финансовые номера и номера платёжных карт",
    "IDs and numbers": "ID и числа",
    # 7. anomaly-detection-kubernetes-pvc
    "Detect low disk space (MiB)": "Обнаружение нехватки места на диске (MiB)",
    "Detect low disk space (%)": "Обнаружение нехватки места на диске (%)",
    "the available disk space is below": "доступное место на диске меньше",
    "for at least": "минимум в течение",
    "within the last": "в последних",
    # 8+9. appsec-{code-level,third-party}-vulnerability-rule-settings
    "Rule name": "Имя правила",
    "Step 1: Select code-level vulnerability detection behavior": "Шаг 1: выберите поведение обнаружения уязвимостей уровня кода",
    "Step 1: Select third-party vulnerability detection behavior": "Шаг 1: выберите поведение обнаружения third-party-уязвимостей",
    "Step 2: Specify where the rule is applied (optional)": "Шаг 2: укажите, где применяется правило (опционально)",
    "Step 3: Leave comment (optional)": "Шаг 3: оставьте комментарий (опционально)",
    "Code-level vulnerability control": "Контроль уязвимостей уровня кода",
    "Third-party vulnerability control": "Контроль third-party-уязвимостей",
    "Resource attribute key": "Ключ атрибута ресурса",
    "Resource attribute value": "Значение атрибута ресурса",
    # 10. failure-detection-service-http-parameters
    "Override global failure detection settings": "Переопределять глобальные параметры обнаружения сбоев",
    "HTTP response codes": "HTTP-коды ответа",
    "HTTP 404 (broken links)": "HTTP 404 (битые ссылки)",
    "HTTP response codes which indicate an error on the server side": "HTTP-коды ответа, указывающие на ошибку на стороне сервера",
    "Treat missing HTTP response code as server side errors": "Считать отсутствие HTTP-кода ответа ошибкой сервера",
    "HTTP response codes which indicate client side errors": "HTTP-коды ответа, указывающие на ошибки клиента",
    "Treat missing HTTP response code as client side error": "Считать отсутствие HTTP-кода ответа ошибкой клиента",
    "Consider 404 HTTP response codes as failures": "Считать HTTP-коды ответа 404 сбоями",
    "Rules for broken links to related domains": "Правила для битых ссылок на связанные домены",
}

# Parameter table col-3 descriptions (when not just `-` and not enum-tail).
PARAM_DESC = {
    # 1. hyperscaler-authentication-connections-azure
    "The name of the connection": "Имя подключения",
    "Azure Authentication mechanism to be used by the connection": "Механизм аутентификации Azure, используемый подключением",
    "Directory (tenant) ID of Microsoft Entra ID": "Directory (tenant) ID Microsoft Entra ID",
    "Application (client) ID of your app registered in Microsoft Azure App registrations": "Application (client) ID вашего приложения, зарегистрированного в Microsoft Azure App registrations",
    "Client secret of your app registered in Microsoft Azure App registrations": "Client secret вашего приложения, зарегистрированного в Microsoft Azure App registrations",
    "Dynatrace integrations that can use this connection": "Интеграции Dynatrace, которые могут использовать это подключение",
    "Consumers that can use the connection": "Потребители, которые могут использовать это подключение",
    # 2. disk-options
    "When disabled OneAgent will try to deduplicate some of nfs mount points. Disabled by default, applies only to Linux hosts.  Applies only to Linux hosts": "При отключении OneAgent будет пытаться дедуплицировать часть nfs-точек монтирования. По умолчанию отключено, применяется только к Linux-хостам.  Применяется только к Linux-хостам",
    "Deactivate NFS monitoring on all supported systems": "Деактивировать мониторинг NFS на всех поддерживаемых системах",
    "Activate tmpfs monitoring on Linux systems": "Активировать мониторинг tmpfs на Linux-системах",
    "OneAgent automatically detects and monitors all your mount points, however you can create exception rules to remove disks from the monitoring list.  Certain filesystems are always excluded as monitoring of them is not useful. For example, autofs, proc, cgroup, tmpfs.  "
    + WARN
    + " Filtering is done before resolving symbolic links.": "OneAgent автоматически обнаруживает и мониторит все точки монтирования, при этом можно создавать правила-исключения для удаления дисков из списка мониторинга.  Некоторые файловые системы всегда исключаются, так как их мониторинг бесполезен. Например, autofs, proc, cgroup, tmpfs.  "
    + WARN
    + " Фильтрация выполняется до разрешения символьных ссылок.",
    "**Disk or mount point path field:** the path to where the disk to be excluded from monitoring is mounted. Examples:  * /mnt/my\\_disk * /staff/emp1 * C:\\ * /staff/\\* * /disk\\*  "
    + WARN
    + " Mount point paths are case sensitive!  The wildcard in **/staff/**\\* means to exclude every child folder of /staff.  The wildcard in **/disk**\\* means to exclude every mount point starting with /disk, for example /disk1, /disk99, /diskabc  "
    + WARN
    + " Filtering is done before resolving symbolic links.": "**Поле «Путь к диску или точке монтирования»:** путь, по которому смонтирован диск, исключаемый из мониторинга. Примеры:  * /mnt/my\\_disk * /staff/emp1 * C:\\ * /staff/\\* * /disk\\*  "
    + WARN
    + " Пути точек монтирования регистрозависимы!  Wildcard в **/staff/**\\* означает исключение каждой дочерней папки /staff.  Wildcard в **/disk**\\* означает исключение каждой точки монтирования, начинающейся на /disk, например /disk1, /disk99, /diskabc  "
    + WARN
    + " Фильтрация выполняется до разрешения символьных ссылок.",
    "**File system type field:** the type of the file system to be excluded from monitoring. Examples:  * ext4 * ext3 * btrfs * ext\\*  "
    + WARN
    + " Starting from **OneAgent 1.299+** file system types are not case sensitive!  The wildcard in the last example means to exclude matching file systems such as types ext4 and ext3": "**Поле «Тип файловой системы»:** тип файловой системы, исключаемой из мониторинга. Примеры:  * ext4 * ext3 * btrfs * ext\\*  "
    + WARN
    + " Начиная с **OneAgent 1.299+** типы файловых систем нечувствительны к регистру!  Wildcard в последнем примере означает исключение совпавших файловых систем, например типов ext4 и ext3",
    # 3. mainframe-txmonitoring
    "Dynatrace automatically traces incoming web requests when they are called by already-monitored services. Enable this setting to monitor all incoming web requests. We recommend enabling it only over a short period of time.": "Dynatrace автоматически трассирует входящие web-запросы, когда их вызывают уже мониторимые сервисы. Включите этот параметр, чтобы мониторить все входящие web-запросы. Рекомендуем включать его только на короткое время.",
    "If enabled, the CICS Transaction Gateway sensor will trace all EXCI requests including those that are using the TCP/IP or SNA protocol.": "Если включено, сенсор CICS Transaction Gateway будет трассировать все EXCI-запросы, в том числе использующие протокол TCP/IP или SNA.",
    "If enabled, CICS regions belonging to the same CICSPlex will be grouped into a single process group. If disabled, a process group will be created for each CICS region.": "Если включено, CICS-регионы из одного CICSPlex будут сгруппированы в одну process group. Если отключено, для каждого CICS-региона будет создана отдельная process group.",
    "If enabled, a CICS service will be created for each monitored transaction ID within a process group. If disabled, a CICS service will be created for each monitored CICS region within a process group. We recommend enabling it only when the CICS regions are grouped by their CICSPlex.": "Если включено, для каждого мониторимого transaction ID внутри process group будет создан CICS-сервис. Если отключено, для каждого мониторимого CICS-региона внутри process group будет создан CICS-сервис. Рекомендуем включать только если CICS-регионы сгруппированы по CICSPlex.",
    "If enabled, IMS regions belonging to the same subsystem will be grouped into a single process group. If disabled, a process group will be created for each IMS region.": "Если включено, IMS-регионы из одной подсистемы будут сгруппированы в одну process group. Если отключено, для каждого IMS-региона будет создана отдельная process group.",
    "If enabled, an IMS service will be created for each monitored transaction ID within a process group. If disabled, an IMS service will be created for each monitored IMS region within a process group. We recommend enabling it only when the IMS regions are grouped by their subsystem.": "Если включено, для каждого мониторимого transaction ID внутри process group будет создан IMS-сервис. Если отключено, для каждого мониторимого IMS-региона внутри process group будет создан IMS-сервис. Рекомендуем включать только если IMS-регионы сгруппированы по подсистемам.",
    "We recommend the default limit of 500 nodes. The value 0 means unlimited number of nodes.": "Рекомендуем лимит по умолчанию 500 узлов. Значение 0 означает неограниченное число узлов.",
    # 4. rum-web-key-performance-metric-load-actions
    "Set the Tolerating and Frustrated performance thresholds for this action type.": "Задайте пороги производительности Tolerating и Frustrated для этого типа действия.",
    "If the selected key performance metric is not detected, the **User action duration** metric is used instead.": "Если выбранная ключевая метрика производительности не обнаружена, используется метрика **User action duration**.",
    "If the key performance metric is below this value, the action is assigned to the Satisfied performance zone.": "Если ключевая метрика производительности ниже этого значения, действие относится к зоне производительности Satisfied.",
    "If the key performance metric is above this value, the action is assigned to the Frustrated performance zone.": "Если ключевая метрика производительности выше этого значения, действие относится к зоне производительности Frustrated.",
    "If **User action duration** is below this value, the action is assigned to the Satisfied performance zone.": "Если **User action duration** ниже этого значения, действие относится к зоне производительности Satisfied.",
    "If **User action duration** is above this value, the action is assigned to the Frustrated performance zone.": "Если **User action duration** выше этого значения, действие относится к зоне производительности Frustrated.",
    # 5. container-technology
    "Platform: Cloud Foundry  Status: Released  Operating system: Linux  Min agent version: 1.159": "Платформа: Cloud Foundry  Статус: Released  ОС: Linux  Мин. версия агента: 1.159",
    "Platform: Kubernetes  Status: Released  Operating system: Linux  Min agent version: 1.169": "Платформа: Kubernetes  Статус: Released  ОС: Linux  Мин. версия агента: 1.169",
    "Platform: Kubernetes  Status: Released  Operating system: Linux  Min agent version: 1.163": "Платформа: Kubernetes  Статус: Released  ОС: Linux  Мин. версия агента: 1.163",
    "Platform: Docker and Kubernetes  Status: Released  Operating system: Linux": "Платформа: Docker и Kubernetes  Статус: Released  ОС: Linux",
    "Platform: Docker  Status: Early adopter  Operating system: Windows  Min agent version: 1.149": "Платформа: Docker  Статус: Early adopter  ОС: Windows  Мин. версия агента: 1.149",
    "Platform: Cloud Foundry  Status: Released  Operating system: Linux  Min agent version: 1.133": "Платформа: Cloud Foundry  Статус: Released  ОС: Linux  Мин. версия агента: 1.133",
    "Platform: Cloud Foundry  Status: Early adopter  Operating system: Windows  Min agent version: 1.175": "Платформа: Cloud Foundry  Статус: Early adopter  ОС: Windows  Мин. версия агента: 1.175",
    "Platform: Podman  Status: Released  Operating system: Linux  Min agent version: 1.267": "Платформа: Podman  Статус: Released  ОС: Linux  Мин. версия агента: 1.267",
    # 6. oneagent-side-masking-settings
    "Exclude email addresses from URLs and exceptions  Enables masking of emails and user information in URLs and exceptions.  Examples: https://the-internet.com/mail/admin@the-internet.com/newItems -> https://the-internet.com/mail//newItems (`<your-dynatrace-url>/`)  ftp://user:hunter2@domain.com -> ftp://@domain.com (`<your-dynatrace-url>/`) (Domain is not masked, as it's recognised as part of the authority.)": "Исключить email-адреса из URL и исключений.  Включает маскирование email и пользовательских данных в URL и исключениях.  Примеры: https://the-internet.com/mail/admin@the-internet.com/newItems -> https://the-internet.com/mail//newItems (`<your-dynatrace-url>/`)  ftp://user:hunter2@domain.com -> ftp://@domain.com (`<your-dynatrace-url>/`) (Домен не маскируется, так как распознан как часть authority.)",
    "Exclude query parameters from URLs and web requests  Enables masking values of query parameters in URLs.  Example: **?key1=value1&key2=value2** -> **?key1=&key2=**.": "Исключить параметры запроса из URL и web-запросов.  Включает маскирование значений параметров запроса в URL.  Пример: **?key1=value1&key2=value2** -> **?key1=&key2=**.",
    "Exclude IBANs and payment card numbers from URLs and exceptions  Enables masking of IBAN- and payment card-like strings (numbers).  Example: https://the-internet.com/CC/1234 4321 5678 8756/test (`<your-dynatrace-url>/`) -> https://the-internet.com/CC//test (`<your-dynatrace-url>/`)": "Исключить IBAN и номера платёжных карт из URL и исключений.  Включает маскирование строк (чисел), похожих на IBAN и номера платёжных карт.  Пример: https://the-internet.com/CC/1234 4321 5678 8756/test (`<your-dynatrace-url>/`) -> https://the-internet.com/CC//test (`<your-dynatrace-url>/`)",
    "Exclude hexadecimal IDs and consecutive numbers above 5 digits from URLs and exceptions  Numbers can contain symbols **-**, **.**, **:**, ' '(whitespace) between digits, these are not counted. Maximum value is 255.  Example: https://the-internet.com/IP/123:12:32:65 -> https://the-internet.com/IP/ (`<your-dynatrace-url>/`)": "Исключить шестнадцатеричные ID и последовательные числа длиной более 5 цифр из URL и исключений.  Между цифрами числа могут содержать символы **-**, **.**, **:**, ' '(пробел), они не учитываются. Максимальное значение: 255.  Пример: https://the-internet.com/IP/123:12:32:65 -> https://the-internet.com/IP/ (`<your-dynatrace-url>/`)",
    # 7. anomaly-detection-kubernetes-pvc
    "Alerts on low disk space in megabytes for a persistent volume claim.": "Оповещает о нехватке места на диске (в мегабайтах) для persistent volume claim.",
    "Alerts on low disk space in % for a persistent volume claim.": "Оповещает о нехватке места на диске (в %) для persistent volume claim.",
    "Alert if": "Оповестить, если",
    # 8+9. appsec-*-vulnerability-rule-settings (shared)
    "When you add multiple conditions, the rule applies if all conditions apply.  If you want the rule to apply only to a subset of your environment, provide the resource attributes that should be used to identify that part of the environment.": "При добавлении нескольких условий правило применяется, если применяются все условия.  Если правило должно применяться только к части окружения, укажите атрибуты ресурсов, по которым эту часть окружения нужно определить.",
    # 10. failure-detection-service-http-parameters
    "HTTP 404 response codes are thrown when a web server can't find a certain page. 404s are classified as broken links on the client side and therefore aren't considered to be service failures. By enabling this setting, you can have 404s treated as server-side service failures.": "HTTP-коды ответа 404 возвращаются, когда web-сервер не находит определённую страницу. 404 классифицируются как битые ссылки на стороне клиента и поэтому не считаются сбоями сервиса. Включив этот параметр, можно трактовать 404 как сбои сервиса на стороне сервера.",
    "If your application relies on other hosts at other domains, add the associated domain names here. Once configured, Dynatrace will consider 404s thrown by hosts at these domains to be service failures related to your application.": "Если приложение зависит от других хостов на других доменах, добавьте сюда соответствующие доменные имена. После настройки Dynatrace будет считать 404, возвращаемые хостами на этих доменах, сбоями сервиса, связанными с вашим приложением.",
}

# Structural canon (shared with L4-AG.1a.1-6 / L4-AF).
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
        print("%-65s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY:", "OK" if bad == 0 else f"BAD ({bad})")
