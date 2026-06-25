# -*- coding: utf-8 -*-
"""L4-AG.1a.15a builder: 5 builtin schema-table 12-16KB.

Состав батча (5 файлов, разнородные но с twin-pair'ами):
  - builtin-infrastructure-disk-edge-anomaly-detectors.md (12.2KB)
  - builtin-management-zones.md (12.9KB)
  - builtin-os-services-monitoring.md (12.3KB)
  - builtin-tags-auto-tagging.md (12.0KB)
  - builtin-anomaly-detection-infrastructure-hosts.md (16.3KB)

Twin pair management-zones <-> tags-auto-tagging: общий AttributeCondition
(огромный entityType enum + key enum + operator enum). Twin-like disk-edge
<-> os-services-monitoring: общие `$X(...) - Matches ...` bullet-описания
match-pattern (triple-en-dash mojibake).

Канон L4-AG.1a.14c сохранён (chr() для triple-mojibake, _normalize чистит
mojibake-BOM вне зависимости от позиции, empty-label rows разрешены в
_param_row, ENUM-leftover EN не допускается).

Mojibake-аудит EN:
  - triple-en-dash `-` (U+2013, bytes c3 a2 c2 80 c2 93): disk-edge 24 +
    os-services 35 = 59 в bullet-separator паттерна L4-AG.1a.9.
  - mojibake-BOM `i.»¿` чистится `_normalize` (двойно-декодированная форма
    chr(0xEF)+chr(0xBB)+chr(0xBF) = 3 chars).
  - Иных типов нет (single 0 real, triple-apos/em/nbh/lq/rq 0, double-B 0,
    double-decoded WARN 0).

Lesson L4-AG.1a.9: TM_ENDASH через chr(0xE2)+chr(0x80)+chr(0x93) канон.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-infrastructure-disk-edge-anomaly-detectors.md",
    "builtin-management-zones.md",
    "builtin-os-services-monitoring.md",
    "builtin-tags-auto-tagging.md",
    "builtin-anomaly-detection-infrastructure-hosts.md",
]

TM_ENDASH = chr(0xE2) + chr(0x80) + chr(0x93)  # triple-en-dash mojibake

DISPLAY_NAME = {
    "Anomaly detection for infrastructure: Disk Edge": "Обнаружение аномалий инфраструктуры: Disk Edge",
    "Management zones settings": "Настройки management zones",
    "OS services monitoring": "Мониторинг OS services",
    "Automatically applied tags": "Автоматически применяемые tags",
    "Anomaly detection for infrastructure: Host": "Обнаружение аномалий инфраструктуры: Host",
}

SCHEMA_DESC = {
    # disk-edge: 4 параграфа (description + 2 bold blocks + footer link)
    "The *Disk Edge* feature within Dynatrace provides automatic detection of performance anomalies related to disk infrastructure.": "Функция *Disk Edge* в Dynatrace обеспечивает автоматическое обнаружение аномалий производительности, связанных с дисковой инфраструктурой.",
    "Use these settings to tailor detection sensitivity based on disk characteristics such as disk name, total space, filesystem type, disk type, and/or custom metadata. Defining custom properties can help with post processing of the event.": "Используйте эти настройки для адаптации чувствительности обнаружения на основе характеристик диска: имени диска, общего размера, типа файловой системы, типа диска и/или custom metadata. Определение custom properties помогает при post-processing события.",
    "**Policy Hierarchy and Scope**": "**Иерархия и Scope политик**",
    "The order of policies establishes a hierarchical structure. Disk is assigned to the first policy it matches to (based on disk name, total space, filesystem type, disk type, and/or metadata) according to the policies hierarchy.": "Порядок политик задаёт иерархическую структуру. Диск назначается на первую политику, которой он соответствует (по имени диска, общему размеру, типу файловой системы, типу диска и/или metadata), согласно иерархии политик.",
    "Policies can be defined within Host, Host Group and Tenant scope. Lower scope has priority over the higher one.": "Политики можно определять в scope Host, Host Group и Tenant. Более низкий scope имеет приоритет над более высоким.",
    "To learn more about Disk Edge visit its [official documentation](https://dt-url.net/diskEdgeDoc).": "Подробнее о Disk Edge см. [official documentation](https://dt-url.net/diskEdgeDoc).",
    # management-zones: 5 параграфов
    "Management zones enable defining fine grained access rights to parts of an environment. A Management zone consists of a set of entities like applications, hosts, process groups, or services.": "Management zones позволяют задавать точечные права доступа к частям environment. Management zone состоит из набора entities, таких как applications, hosts, process groups или services.",
    "For each Management zone you can define which user groups have access to them. This way you can ensure the confidentiality of certain parts of an environment and still keep an end to end view across all components for the users that need it.": "Для каждой Management zone можно определить, какие группы пользователей имеют к ней доступ. Так обеспечивается конфиденциальность отдельных частей environment с сохранением сквозного представления по всем компонентам для пользователей, которым оно нужно.",
    'For value suggestions based on entity data and preview functionality, environment-wide "Access environment" permission is required.': 'Для подсказки значений на основе данных entity и функции preview требуется environment-wide разрешение "Access environment".',
    "Management zone rules are executed periodically in the background, for a limited timeframe. Any entity that matches a management zone rule will receive the specific zone assigned to it, while removing zones from entities that no longer match. Be aware that for any condition that requires the relationship between multiple entities, all entities in this scope need to be present in this timeframe!": "Правила management zone периодически выполняются в фоне в течение ограниченного timeframe. Любая entity, удовлетворяющая правилу management zone, получит назначенную zone, при этом zones снимаются с entities, которые перестают подходить. Учтите: для любого условия, требующего связи между несколькими entities, все entities этого scope должны присутствовать в данном timeframe!",
    "Depending on environment-size, rule count (Management zones, as well as tagging and naming rules) and rule complexity, the application of all management zones might be delayed!": "В зависимости от размера environment, количества правил (Management zones, а также tagging и naming rules) и их сложности, применение всех management zones может задерживаться!",
    # os-services-monitoring: 4 параграфа
    "Set up alerts for OS services in undesirable states both for Windows and Linux systemd.": "Настройка оповещений для OS services в нежелательных состояниях для Windows и Linux systemd.",
    "Note: If monitoring is turned on for full availability metric, custom metric consumption takes place. Refer to [documentation](https://dt-url.net/vl03xzk) for more details.": "Note: при включении мониторинга для full availability metric происходит расход custom metric. Подробнее см. [documentation](https://dt-url.net/vl03xzk).",
    "Please provide feedback to us about this feature on [Dynatrace Community](https://dt-url.net/nl02tbm).": "Оставьте отзыв об этой функции в [Dynatrace Community](https://dt-url.net/nl02tbm).",
    "In order to set up the alert for a certain group of OS services, you must first define a new policy. Specify which service's states you would like to be alerted about and then add detection rules in order to tell Dynatrace which exact OS services you are interested in. You may specify multiple detection rules.": "Чтобы настроить оповещение для определённой группы OS services, сначала создайте новую политику. Укажите, о каких состояниях службы вы хотите получать оповещения, затем добавьте detection rules, чтобы указать Dynatrace, какие именно OS services вас интересуют. Можно задать несколько detection rules.",
    "Note that policies are specified for each of supported operating systems individually and that some of the parameters and properties vary between them.": "Note: политики задаются для каждой поддерживаемой OS отдельно, и часть параметров и свойств между ними различается.",
    # tags-auto-tagging: 6 параграфов
    "Tags simplify searches for related services, process groups, and hosts. They also facilitate the collection of related metrics into meaningful groups for analysis.": "Tags упрощают поиск связанных services, process groups и hosts. Они также облегчают сбор связанных metrics в осмысленные группы для анализа.",
    "In dynamic or large environments, manual tagging of such entities is often impractical. In such cases, it's recommended that you use automated rule-based tags.": "В динамических или крупных environments ручное тегирование таких entities часто непрактично. В этих случаях рекомендуется использовать автоматические rule-based tags.",
    "Rule-based tags behave just like manually-applied tags, except they're applied automatically to new entities that match defined rules. Automated rule-based tags can't be removed manually from individual services, process groups, or hosts. Rule-based tags are removed automatically once an entity no longer matches a defined rule.": "Rule-based tags ведут себя как теги, применённые вручную, только применяются автоматически к новым entities, которые соответствуют заданным правилам. Автоматические rule-based tags нельзя снять вручную с отдельных services, process groups или hosts. Rule-based tag снимается автоматически, когда entity перестаёт соответствовать правилу.",
    "Tagging rules are executed periodically in the background, for a limited timeframe. Any entity that matches a tagging rule will receive the specific tag, while removing tags from entities that no longer match. Be aware that for any condition that requires the relationship between multiple entities, all entities in this scope need to be present in this timeframe!": "Tagging rules периодически выполняются в фоне в течение ограниченного timeframe. Любая entity, удовлетворяющая tagging rule, получит соответствующий tag, при этом tags снимаются с entities, которые перестают подходить. Учтите: для любого условия, требующего связи между несколькими entities, все entities этого scope должны присутствовать в данном timeframe!",
    "Depending on environment-size, rule count (tagging rules, as well as management zone and naming rules) and rule complexity, the application of all tags might be delayed! For faster, unchanging tagging, please utilize the tagging REST API!": "В зависимости от размера environment, количества правил (tagging rules, а также management zone и naming rules) и их сложности, применение всех tags может задерживаться! Для более быстрого и неизменного tagging используйте tagging REST API!",
    # anomaly-detection-infrastructure-hosts: 1 параграф
    "Dynatrace automatically detects infrastructure-related performance anomalies such as high CPU saturation and memory outages. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for hosts.": "Dynatrace автоматически обнаруживает аномалии производительности, связанные с инфраструктурой, такие как высокая загрузка CPU и нехватка памяти. Используйте эти настройки для настройки чувствительности обнаружения, задания порогов alerting или отключения alerting для hosts.",
    '(For value suggestions based on entity data and preview functionality, environment-wide "Access environment" permission is required.)': '(Для подсказки значений на основе данных entity и функции preview требуется environment-wide разрешение "Access environment".)',
}

PARAM_LABEL = {
    # common
    "Enabled": "Включено",
    "Description": "Описание",
    "Properties": "Свойства",
    "Key": "Ключ",
    "Value": "Значение",
    "Condition": "Условие",
    "Operator": "Оператор",
    "Tag": "Тег",
    "Type": "Тип",
    # disk-edge
    "Policy name": "Имя политики",
    "Operating system": "Операционная система",
    "Alerts": "Оповещения",
    "Disk name filters": "Фильтры имени диска",
    "Detection rules": "Правила обнаружения",
    "Trigger": "Триггер",
    "Rule scope": "Scope правила",
    "Disk property": "Свойство диска",
    "Disk total space thresholds": "Пороги общего размера диска",
    "Filesystem condition": "Условие файловой системы",
    "Resource attribute": "Resource attribute",
    "Violating samples": "Sample-нарушения",
    "Evaluation window size for violating samples": "Размер окна оценки для sample-нарушений",
    "Dealerting samples": "Sample-дезалертинга",
    "Evaluation window size for dealerting samples": "Размер окна оценки для sample-дезалертинга",
    "Threshold above (optional)": "Порог сверху (необязательно)",
    "Threshold below (optional)": "Порог снизу (необязательно)",
    "Key must exist": "Ключ должен существовать",
    # management-zones / tags-auto-tagging (twin)
    "Management zone name": "Имя management zone",
    "Tag name": "Имя tag",
    "Rules": "Правила",
    "Rule type": "Тип правила",
    "Entity selector": "Entity selector",
    "Rule applies to": "Правило применяется к",
    "Conditions": "Условия",
    "Apply to underlying hosts of matching services": "Применять к нижележащим hosts подходящих services",
    "Apply to underlying process groups of matching services": "Применять к нижележащим process groups подходящих services",
    "Apply to underlying hosts of matching process groups": "Применять к нижележащим hosts подходящих process groups",
    "Apply to all services provided by the process groups": "Применять ко всем services, предоставляемым process groups",
    "Apply to processes running on matching hosts": "Применять к процессам, работающим на подходящих hosts",
    "Apply to custom devices in a custom device group": "Применять к custom devices в custom device group",
    "Apply to services provided by matching Azure entities": "Применять к services, предоставляемым подходящими Azure entities",
    "Apply to process groups connected to matching Azure entities": "Применять к process groups, связанным с подходящими Azure entities",
    "Property": "Свойство",
    "Key source": "Источник ключа",
    "Dynamic key": "Динамический ключ",
    "Case sensitive": "С учётом регистра",
    "Optional tag value": "Необязательное значение tag",
    "Value Normalization": "Нормализация значения",
    # os-services-monitoring
    "System": "Система",
    "Rule name": "Имя правила",
    "Monitor": "Мониторить",
    "Alert": "Оповещение",
    "Alert if service is not installed": "Оповещать, если служба не установлена",
    "Service status condition for alerting": "Условие статуса службы для alerting",
    "Alerting delay": "Задержка alerting",
    "Service property": "Свойство службы",
    # anomaly-detection-infrastructure-hosts
    "Hosts": "Hosts",
    "Network": "Network",
    "Detect host or monitoring connection lost problems": "Обнаруживать потерю связи с host или monitoring",
    "Graceful host shutdowns": "Корректные shutdown host'ов",
    "Detect CPU saturation on host": "Обнаруживать CPU saturation на host",
    "Detection mode for CPU saturation": "Режим обнаружения для CPU saturation",
    "Detect High System Load on host": "Обнаруживать High System Load на host",
    "Detection mode for High System Load": "Режим обнаружения для High System Load",
    "Detect high memory usage on host": "Обнаруживать высокое использование памяти на host",
    "Detection mode for high memory usage": "Режим обнаружения для высокого использования памяти",
    "Detect high GC activity": "Обнаруживать высокую активность GC",
    "Detection mode for high GC activity": "Режим обнаружения для высокой активности GC",
    "Detect Java out of memory problem": "Обнаруживать проблему Java out of memory",
    "Detection mode for Java out of memory problem": "Режим обнаружения для проблемы Java out of memory",
    "Detect Java out of threads problem": "Обнаруживать проблему Java out of threads",
    "Detection mode for Java out of threads problem": "Режим обнаружения для проблемы Java out of threads",
    "Detect high number of dropped packets": "Обнаруживать большое число dropped packets",
    "Detection mode for high number of dropped packets": "Режим обнаружения для большого числа dropped packets",
    "Detect high number of network errors": "Обнаруживать большое число сетевых ошибок",
    "Detection mode for high number of network errors": "Режим обнаружения для большого числа сетевых ошибок",
    "Detect high network utilization": "Обнаруживать высокую загрузку сети",
    "Detection mode for high network utilization": "Режим обнаружения для высокой загрузки сети",
    "Detect TCP connectivity problems for process": "Обнаруживать проблемы TCP connectivity для процесса",
    "Detection mode for TCP connectivity problems": "Режим обнаружения для проблем TCP connectivity",
    "Detect high retransmission rate": "Обнаруживать высокую частоту retransmission",
    "Detection mode for high retransmission rate": "Режим обнаружения для высокой частоты retransmission",
    "Alert if the CPU usage is higher than this threshold for the defined amount of samples": "Оповещать, если использование CPU выше этого порога в течение заданного количества samples",
    "Alert if the System Load divided by the number of logical CPU cores is higher than this threshold for the defined amount of samples.": "Оповещать, если System Load, делённый на число логических CPU cores, выше этого порога в течение заданного количества samples.",
    "Alert if the memory usage on Windows is higher than this threshold": "Оповещать, если использование памяти на Windows выше этого порога",
    "Alert if the memory usage on Unix systems is higher than this threshold": "Оповещать, если использование памяти на Unix-системах выше этого порога",
    "Alert if the memory page fault rate on Windows is higher than this threshold for the defined amount of samples": "Оповещать, если частота memory page faults на Windows выше этого порога в течение заданного количества samples",
    "Alert if the memory page fault rate on Unix systems is higher than this threshold for the defined amount of samples": "Оповещать, если частота memory page faults на Unix-системах выше этого порога в течение заданного количества samples",
    "Alert if GC time is higher than this threshold": "Оповещать, если GC time выше этого порога",
    "Alert if the GC suspension is higher than this threshold": "Оповещать, если GC suspension выше этого порога",
    "Alert if the number of Java out-of-memory exceptions is at least this value": "Оповещать, если число Java out-of-memory exceptions не меньше этого значения",
    "Alert if the number of Java out-of-threads exceptions is at least this value": "Оповещать, если число Java out-of-threads exceptions не меньше этого значения",
    "Receive/transmit dropped packet percentage threshold": "Порог процента receive/transmit dropped packets",
    "Total packets rate threshold": "Порог общей частоты пакетов",
    "Receive/transmit error packet percentage threshold": "Порог процента receive/transmit error packets",
    "Alert if sent/received traffic utilization is higher than this threshold for the defined amount of samples": "Оповещать, если использование sent/received traffic выше этого порога в течение заданного количества samples",
    "New connection failure threshold": "Порог отказов новых connection",
    "Number of failed connections threshold": "Порог количества failed connections",
    "Retransmission rate threshold": "Порог частоты retransmission",
    "Number of retransmitted packets threshold": "Порог количества retransmitted packets",
}

PARAM_DESC = {
    # disk-edge / os-services-monitoring twin: match-pattern bullets (TM_ENDASH)
    # Все эти строки содержат `$X(...)` + TM_ENDASH + " Matches ...".
    # Триплет TM_ENDASH = chr(0xE2)+chr(0x80)+chr(0x93) = U+2013 (en-dash) в mojibake.
    "Disk will be included in this policy if **any** of the filters match  Disk name filter has to match a required format.  * `$match(/zSecure/snapshot?/*)` "
    + TM_ENDASH
    + " Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(/log/)` "
    + TM_ENDASH
    + " Matches if `/log/` appears anywhere in disk name. * `$eq(/)` "
    + TM_ENDASH
    + " Matches if `/` matches the disk name exactly. * `$prefix(/srv/)` "
    + TM_ENDASH
    + " Matches if `/srv/` matches the prefix of disk name. * `$suffix(/backup)` "
    + TM_ENDASH
    + " Matches if `/backup` matches the suffix of disk name.  Available logic operations:  * `$not($eq(/usr))` "
    + TM_ENDASH
    + " Matches if the disk name is different from `/usr`. * `$and($prefix(/var),$suffix(/backup))` "
    + TM_ENDASH
    + " Matches if disk name starts with `/var` and ends with `/backup`. * `$or($prefix(/home/),$eq(/root))` "
    + TM_ENDASH
    + " Matches if disk name starts with `/home` or equals `/root`.  Brackets **(** and **)** that are part of the matched disk name **must be escaped with a tilde (~)**": "Диск попадает в эту политику, если совпадает **любой** из фильтров. Фильтр имени диска должен соответствовать требуемому формату. * `$match(/zSecure/snapshot?/*)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(/log/)`, совпадает, если `/log/` встречается в имени диска. * `$eq(/)`, совпадает, если `/` равно имени диска. * `$prefix(/srv/)`, совпадает, если `/srv/` является префиксом имени диска. * `$suffix(/backup)`, совпадает, если `/backup` является суффиксом имени диска. Доступные логические операции: * `$not($eq(/usr))`, совпадает, если имя диска отличается от `/usr`. * `$and($prefix(/var),$suffix(/backup))`, совпадает, если имя диска начинается с `/var` и заканчивается на `/backup`. * `$or($prefix(/home/),$eq(/root))`, совпадает, если имя диска начинается с `/home` или равно `/root`. Скобки **(** и **)**, которые являются частью имени диска, **должны экранироваться тильдой (~)**",
    "Set of rules to scope which disks the policy applies to. Rules can match based on disk properties (total space, filesystem, disk type) or host resource attributes. Each disk property type can be defined at most once per policy.": "Набор правил для определения, к каким дискам применяется политика. Правила могут срабатывать по свойствам диска (общий размер, файловая система, тип диска) или host resource attributes. Каждый тип свойства диска можно задать не более одного раза на политику.",
    "Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2](https://dt-url.net/9622g1w). Additionally any Host resource attribute can be dynamically substituted (agent 1.325+)": "Набор дополнительных key-value свойств, прикрепляемых к создаваемому event. Доступные ключи свойств можно получить через [Events API v2](https://dt-url.net/9622g1w). Дополнительно любой Host resource attribute может подставляться динамически (agent 1.325+)",
    "Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2](https://dt-url.net/9622g1w). Additionally any Host resource attribute can be dynamically substituted (agent 1.325+).": "Набор дополнительных key-value свойств, прикрепляемых к создаваемому event. Доступные ключи свойств можно получить через [Events API v2](https://dt-url.net/9622g1w). Дополнительно любой Host resource attribute может подставляться динамически (agent 1.325+).",
    "Select the operating systems on which policy should be applied": "Выберите OS, на которых применяется политика",
    "Starting from agent 1.335 **disk** detection rules are supported.": "Начиная с agent 1.335 поддерживаются detection rules для **disk**.",
    "Specify disk total space range in GiB": "Укажите диапазон общего размера диска в GiB",
    "Disk filesystem will be included in this policy if **any** of the filters match  Disk filesystem has to match a required format.  * `$match(ext*)` "
    + TM_ENDASH
    + " Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(fs)` "
    + TM_ENDASH
    + " Matches if `fs` appears anywhere in the filesystem type. * `$eq(ext4)` "
    + TM_ENDASH
    + " Matches if `ext4` matches the filesystem type exactly. * `$prefix(ext)` "
    + TM_ENDASH
    + " Matches if `ext` matches the prefix of the filesystem type. * `$suffix(fs)` "
    + TM_ENDASH
    + " Matches if `fs` matches the suffix of the filesystem type.  Available logic operations:  * `$not($eq(tmpfs))` "
    + TM_ENDASH
    + " Matches if the filesystem type is different from `tmpfs`. * `$and($prefix(ext),$suffix(4))` "
    + TM_ENDASH
    + " Matches if filesystem type starts with `ext` and ends with `4`. * `$or($eq(xfs),$eq(btrfs))` "
    + TM_ENDASH
    + " Matches if filesystem type equals `xfs` or `btrfs`.  Brackets **(** and **)** that are part of the matched filesystem type **must be escaped with a tilde (~)**": "Файловая система диска попадает в эту политику, если совпадает **любой** из фильтров. Тип файловой системы должен соответствовать требуемому формату. * `$match(ext*)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(fs)`, совпадает, если `fs` встречается в типе файловой системы. * `$eq(ext4)`, совпадает, если `ext4` равно типу файловой системы. * `$prefix(ext)`, совпадает, если `ext` является префиксом типа файловой системы. * `$suffix(fs)`, совпадает, если `fs` является суффиксом типа файловой системы. Доступные логические операции: * `$not($eq(tmpfs))`, совпадает, если тип файловой системы отличается от `tmpfs`. * `$and($prefix(ext),$suffix(4))`, совпадает, если тип файловой системы начинается с `ext` и заканчивается на `4`. * `$or($eq(xfs),$eq(btrfs))`, совпадает, если тип файловой системы равен `xfs` или `btrfs`. Скобки **(** и **)**, которые являются частью типа файловой системы, **должны экранироваться тильдой (~)**",
    "Host resource attributes are dimensions enriching the host including custom metadata which are user-defined key-value pairs that you can assign to hosts monitored by Dynatrace.  By defining custom metadata, you can enrich the monitoring data with context specific to your organization's needs, such as environment names, team ownership, application versions, or any other relevant details.  See [Define tags and metadata for hosts](https://dt-url.net/w3hv0kbw).  Note: Starting from version 1.325 host resource attributes are supported in addition to host custom metadata.": "Host resource attributes, это dimensions, обогащающие host, включая custom metadata (пользовательские key-value пары, которые можно присваивать hosts, мониторимым Dynatrace). Через custom metadata можно дополнять данные мониторинга контекстом, специфичным для нужд организации: имена environment, ответственность команд, версии приложения и т.д. См. [Define tags and metadata for hosts](https://dt-url.net/w3hv0kbw). Note: начиная с версии 1.325 host resource attributes поддерживаются наряду с host custom metadata.",
    "If this field is empty then there is no lower limit  Minimum total disk space in GiB": "Если поле пустое, нижний предел отсутствует. Минимальный общий размер диска в GiB",
    "If this field is empty then there is no upper limit  Maximum total disk space in GiB": "Если поле пустое, верхний предел отсутствует. Максимальный общий размер диска в GiB",
    "When enabled, the condition requires a resource attribute to exist and match the constraints; when disabled, the key is optional but must still match the constrains if it is present.": "Когда включено, условие требует, чтобы resource attribute существовал и удовлетворял ограничениям; когда выключено, ключ необязателен, но при наличии всё равно должен удовлетворять ограничениям.",
    "This string has to match a required format.  * `$match(ver*_1.2.?)` "
    + TM_ENDASH
    + " Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(production)` "
    + TM_ENDASH
    + " Matches if `production` appears anywhere in the host metadata value. * `$eq(production)` "
    + TM_ENDASH
    + " Matches if `production` matches the host metadata value exactly. * `$prefix(production)` "
    + TM_ENDASH
    + " Matches if `production` matches the prefix of the host metadata value. * `$suffix(production)` "
    + TM_ENDASH
    + " Matches if `production` matches the suffix of the host metadata value.  Available logic operations:  * `$not($eq(production))` "
    + TM_ENDASH
    + " Matches if the host metadata value is different from `production`. * `$and($prefix(production),$suffix(main))` "
    + TM_ENDASH
    + " Matches if host metadata value starts with `production` and ends with `main`. * `$or($prefix(production),$suffix(main))` "
    + TM_ENDASH
    + " Matches if host metadata value starts with `production` or ends with `main`.  Brackets **(** and **)** that are part of the matched property **must be escaped with a tilde (~)**": "Строка должна соответствовать требуемому формату. * `$match(ver*_1.2.?)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(production)`, совпадает, если `production` встречается в значении host metadata. * `$eq(production)`, совпадает, если `production` равно значению host metadata. * `$prefix(production)`, совпадает, если `production` является префиксом значения host metadata. * `$suffix(production)`, совпадает, если `production` является суффиксом значения host metadata. Доступные логические операции: * `$not($eq(production))`, совпадает, если значение host metadata отличается от `production`. * `$and($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` и заканчивается на `main`. * `$or($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` или заканчивается на `main`. Скобки **(** и **)**, которые являются частью свойства, **должны экранироваться тильдой (~)**",
    # eventThresholds (общий для disk-edge sample-pair + anomaly-detection-infrastructure-hosts)
    "The number of **10-second samples** within the evaluation window that must exceed the threshold to trigger an event": "Количество **10-секундных samples** в окне оценки, которые должны превысить порог для триггера event",
    "The number of **10-second samples** that form the sliding evaluation window to detect violating samples.": "Количество **10-секундных samples**, образующих скользящее окно оценки для обнаружения sample-нарушений.",
    "The number of **10-second samples** within the evaluation window that must be lower than the threshold to close an event": "Количество **10-секундных samples** в окне оценки, которые должны быть ниже порога для закрытия event",
    "The number of **10-second samples** that form the sliding evaluation window for dealerting.": "Количество **10-секундных samples**, образующих скользящее окно оценки для дезалертинга.",
    # management-zones / tags-auto-tagging
    "**Be careful when renaming** - if there are policies that are referencing this Management zone, they will need to be adapted to the new name!": "**Будьте осторожны при переименовании**: если есть политики, ссылающиеся на эту Management zone, их потребуется адаптировать под новое имя!",
    "Learn more about the [Entity selector](https://dt-url.net/apientityselector).": "Подробнее об [Entity selector](https://dt-url.net/apientityselector).",
    "Format: `[CONTEXT]tagKey:tagValue`": "Формат: `[CONTEXT]tagKey:tagValue`",
    "Type '{' for placeholder suggestions.  Placeholders containing ' /' must be enclosed in quotation marks.  For example: {\"placeholder/etc\"}": "Введите '{' для подсказок placeholder. Placeholders, содержащие ' /', должны быть заключены в кавычки. Пример: {\"placeholder/etc\"}",
    # os-services-monitoring
    "Toggle the switch in order to enable or disable availability metric monitoring for this policy. Availability metrics produce custom metrics. Refer to [documentation](https://dt-url.net/vl03xzk) for consumption examples. Each monitored service consumes one custom metric.  **The feature can't be configured on hosts in Discovery mode**": "Включите или выключите switch для включения/отключения мониторинга availability metric для этой политики. Availability metrics порождают custom metrics. Примеры расхода см. в [documentation](https://dt-url.net/vl03xzk). Каждый мониторимый service потребляет одну custom metric. **Функция недоступна для настройки на hosts в режиме Discovery**",
    "Toggle the switch in order to enable or disable alerting for this policy": "Включите или выключите switch для включения/отключения alerting для этой политики",
    "By default, Dynatrace does not alert if the service is not installed. Toggle the switch to enable or disable this feature": "По умолчанию Dynatrace не оповещает, если служба не установлена. Включите или выключите switch, чтобы включить или отключить эту функцию",
    "This string has to match a required format. See [OS services monitoring](https://dt-url.net/vl03xzk).  * `$eq(paused)` "
    + TM_ENDASH
    + " Matches services that are in paused state.  Available logic operations:  * `$not($eq(paused))` "
    + TM_ENDASH
    + " Matches services that are in state different from paused. * `$or($eq(paused),$eq(running))` "
    + TM_ENDASH
    + " Matches services that are either in paused or running state.  Use one of the following values as a parameter for this condition:  * `running` * `stopped` * `start_pending` * `stop_pending` * `continue_pending` * `pause_pending` * `paused`": "Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$eq(paused)`, совпадает со службами в состоянии paused. Доступные логические операции: * `$not($eq(paused))`, совпадает со службами в состоянии, отличном от paused. * `$or($eq(paused),$eq(running))`, совпадает со службами либо в состоянии paused, либо running. Используйте одно из следующих значений как параметр для условия: * `running` * `stopped` * `start_pending` * `stop_pending` * `continue_pending` * `pause_pending` * `paused`",
    "This string has to match a required format. See [OS services monitoring](https://dt-url.net/vl03xzk).  * `$eq(failed)` "
    + TM_ENDASH
    + " Matches services that are in failed state.  Available logic operations:  * `$not($eq(active))` "
    + TM_ENDASH
    + " Matches services with state different from active. * `$or($eq(inactive),$eq(failed))` "
    + TM_ENDASH
    + " Matches services that are either in inactive or failed state.  Use one of the following values as a parameter for this condition:  * `reloading` * `activating` * `deactivating` * `failed` * `inactive` * `active`": "Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$eq(failed)`, совпадает со службами в состоянии failed. Доступные логические операции: * `$not($eq(active))`, совпадает со службами в состоянии, отличном от active. * `$or($eq(inactive),$eq(failed))`, совпадает со службами либо в состоянии inactive, либо failed. Используйте одно из следующих значений как параметр для условия: * `reloading` * `activating` * `deactivating` * `failed` * `inactive` * `active`",
    "The number of **10-second measurement cycles** before alerting is triggered  Set this value to control the speed of alerting. One is the lowest setting equal to one 10-second sample. If you set this value to 30, alerting is triggered after 5 minutes.": "Количество **10-секундных циклов измерений** до срабатывания alerting. Этим значением управляйте скоростью alerting. Минимальное значение 1 равно одному 10-секундному sample. Если задать 30, alerting сработает через 5 минут.",
    "This string has to match a required format. See [OS services monitoring](https://dt-url.net/vl03xzk).  * `$match(ip?tables*)` "
    + TM_ENDASH
    + " Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(ssh)` "
    + TM_ENDASH
    + " Matches if `ssh` appears anywhere in the service's property value. * `$eq(sshd)` "
    + TM_ENDASH
    + " Matches if `sshd` matches the service's property value exactly. * `$prefix(ss)` "
    + TM_ENDASH
    + " Matches if `ss` matches the prefix of the service's property value. * `$suffix(hd)` "
    + TM_ENDASH
    + " Matches if `hd` matches the suffix of the service's property value.  Available logic operations:  * `$not($eq(sshd))` "
    + TM_ENDASH
    + " Matches if the service's property value is different from `sshd`. * `$and($prefix(ss),$suffix(hd))` "
    + TM_ENDASH
    + " Matches if service's property value starts with `ss` and ends with `hd`. * `$or($prefix(ss),$suffix(hd))` "
    + TM_ENDASH
    + " Matches if service's property value starts with `ss` or ends with `hd`.  Brackets **(** and **)** that are part of the matched property **must be escaped with a tilde (~)**": "Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$match(ip?tables*)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(ssh)`, совпадает, если `ssh` встречается в значении свойства службы. * `$eq(sshd)`, совпадает, если `sshd` равно значению свойства службы. * `$prefix(ss)`, совпадает, если `ss` является префиксом значения свойства службы. * `$suffix(hd)`, совпадает, если `hd` является суффиксом значения свойства службы. Доступные логические операции: * `$not($eq(sshd))`, совпадает, если значение свойства службы отличается от `sshd`. * `$and($prefix(ss),$suffix(hd))`, совпадает, если значение свойства службы начинается с `ss` и заканчивается на `hd`. * `$or($prefix(ss),$suffix(hd))`, совпадает, если значение свойства службы начинается с `ss` или заканчивается на `hd`. Скобки **(** и **)**, которые являются частью свойства, **должны экранироваться тильдой (~)**",
    "This string has to match a required format. See [OS services monitoring](https://dt-url.net/vl03xzk).  * `$eq(manual)` "
    + TM_ENDASH
    + " Matches services that are started manually.  Available logic operations:  * `$not($eq(auto))` "
    + TM_ENDASH
    + " Matches services with startup type different from Automatic. * `$or($eq(auto),$eq(manual))` "
    + TM_ENDASH
    + " Matches if service's startup type is either Automatic or Manual.  Use one of the following values as a parameter for this condition:  * `manual` for Manual * `manual_trigger` for Manual (Trigger Start) * `auto` for Automatic * `auto_delay` for Automatic (Delayed Start) * `auto_trigger` for Automatic (Trigger Start) * `auto_delay_trigger` for Automatic (Delayed Start, Trigger Start) * `disabled` for Disabled": "Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$eq(manual)`, совпадает со службами, запускаемыми вручную. Доступные логические операции: * `$not($eq(auto))`, совпадает со службами с типом запуска, отличным от Automatic. * `$or($eq(auto),$eq(manual))`, совпадает, если тип запуска службы Automatic либо Manual. Используйте одно из следующих значений как параметр для условия: * `manual` для Manual * `manual_trigger` для Manual (Trigger Start) * `auto` для Automatic * `auto_delay` для Automatic (Delayed Start) * `auto_trigger` для Automatic (Trigger Start) * `auto_delay_trigger` для Automatic (Delayed Start, Trigger Start) * `disabled` для Disabled",
    "This string has to match a required format. See [OS services monitoring](https://dt-url.net/vl03xzk).  * `$eq(enabled)` "
    + TM_ENDASH
    + " Matches services with startup type equal to enabled.  Available logic operations:  * `$not($eq(enabled))` "
    + TM_ENDASH
    + " Matches services with startup type different from enabled. * `$or($eq(enabled),$eq(disabled))` - Matches services that are either enabled or disabled.  Use one of the following values as a parameter for this condition:  * `enabled` * `enabled-runtime` * `static` * `disabled`": "Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$eq(enabled)`, совпадает со службами с типом запуска enabled. Доступные логические операции: * `$not($eq(enabled))`, совпадает со службами с типом запуска, отличным от enabled. * `$or($eq(enabled),$eq(disabled))`, совпадает со службами либо enabled, либо disabled. Используйте одно из следующих значений как параметр для условия: * `enabled` * `enabled-runtime` * `static` * `disabled`",
    "Type 'dt.' for key hints.": "Введите 'dt.' для подсказок ключей.",
    "Type '{' for placeholder hints.": "Введите '{' для подсказок placeholder.",
    # anomaly-detection-infrastructure-hosts
    "Detection of high CPU saturation is not available on AIX hosts": "Обнаружение высокого CPU saturation недоступно на AIX hosts",
    "Detection High System Load is available only on AIX hosts.": "Обнаружение High System Load доступно только на AIX hosts.",
    "Alert if **both** the memory usage and the memory page fault rate thresholds are exceeded on Windows or on Unix systems": "Оповещать, если **оба** порога (использование памяти и частота memory page faults) превышены на Windows или Unix-системах",
    "You may also configure high GC activity alerting for .NET processes on extensions events page (`<your-dynatrace-url>//#settings/anomalydetection/extensionevents`).": "Также можно настроить alerting для высокой активности GC для .NET-процессов на странице extensions events (`<your-dynatrace-url>//#settings/anomalydetection/extensionevents`).",
    "Alert if the GC time **or** the GC suspension is exceeded": "Оповещать, если превышено GC time **или** GC suspension",
    "Alert if the dropped packet percentage is higher than the specified threshold **and** the total packets rate is higher than the defined threshold for the defined amount of samples": "Оповещать, если процент dropped packets выше заданного порога **и** общая частота пакетов выше заданного порога в течение заданного количества samples",
    "Alert if the receive/transmit error packet percentage is higher than the specified threshold **and** the total packets rate is higher than the defined threshold for the defined amount of samples": "Оповещать, если процент receive/transmit error packets выше заданного порога **и** общая частота пакетов выше заданного порога в течение заданного количества samples",
    "Alert if the percentage of new connection failures is higher than the specified threshold **and** the number of failed connections is higher than the defined threshold for the defined amount of samples": "Оповещать, если процент отказов новых connection выше заданного порога **и** количество failed connections выше заданного порога в течение заданного количества samples",
    "Alert if the retransmission rate is higher than the specified threshold **and** the number of retransmitted packets is higher than the defined threshold for the defined amount of samples": "Оповещать, если частота retransmission выше заданного порога **и** количество retransmitted packets выше заданного порога в течение заданного количества samples",
}

STRUCT = [
    ("* Published Dec 05, 2023", "* Опубликовано 5 декабря 2023"),
    ("* Published Jul 31, 2024", "* Опубликовано 31 июля 2024"),
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
    (
        "`HOST` - Host  `HOST_GROUP` - Host Group  `environment`",
        "`HOST` - Host  `HOST_GROUP` - Host Group  `environment`",
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
        print("%-66s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY MISMATCH:", bad)
