---
title: Settings API - Anomaly detection for infrastructure- Disk Edge schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-infrastructure-disk-edge-anomaly-detectors
scraped: 2026-05-12T11:49:10.464123
---

# Settings API - Anomaly detection for infrastructure- Disk Edge schema table

# Settings API - Anomaly detection for infrastructure- Disk Edge schema table

* Опубликовано 31 июля 2024 г.

### Обнаружение аномалий инфраструктуры: Disk Edge (`builtin:infrastructure.disk.edge.anomaly-detectors)`

Функция *Disk Edge* в Dynatrace обеспечивает автоматическое обнаружение аномалий производительности, связанных с дисковой инфраструктурой.
Используйте эти настройки для адаптации чувствительности обнаружения на основе характеристик диска: имени диска, общего размера, типа файловой системы, типа диска и/или custom metadata. Определение custom properties помогает при post-processing события.

**Иерархия и Scope политик**

Порядок политик задаёт иерархическую структуру. Диск назначается на первую политику, которой он соответствует (по имени диска, общему размеру, типу файловой системы, типу диска и/или metadata), согласно иерархии политик.

Политики можно определять в scope Host, Host Group и Tenant. Более низкий scope имеет приоритет над более высоким.

Подробнее о Disk Edge см. [official documentation](https://dt-url.net/diskEdgeDoc).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:infrastructure.disk.edge.anomaly-detectors` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:infrastructure.disk.edge.anomaly-detectors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:infrastructure.disk.edge.anomaly-detectors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:infrastructure.disk.edge.anomaly-detectors` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя политики `policyName` | text | - | Required |
| Включено `enabled` | boolean | - | Required |
| Операционная система `operatingSystem` | Set<[EOperatingSystem](#EOperatingSystem)> | Выберите OS, на которых применяется политика Возможные значения: * `WINDOWS` * `LINUX` * `AIX` | Required |
| Оповещения `alerts` | Set<[Alert](#Alert)> | - | Required |
| Фильтры имени диска `diskNameFilters` | set | Диск попадает в эту политику, если совпадает **любой** из фильтров. Фильтр имени диска должен соответствовать требуемому формату. * `$match(/zSecure/snapshot?/*)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(/log/)`, совпадает, если `/log/` встречается в имени диска. * `$eq(/)`, совпадает, если `/` равно имени диска. * `$prefix(/srv/)`, совпадает, если `/srv/` является префиксом имени диска. * `$suffix(/backup)`, совпадает, если `/backup` является суффиксом имени диска. Доступные логические операции: * `$not($eq(/usr))`, совпадает, если имя диска отличается от `/usr`. * `$and($prefix(/var),$suffix(/backup))`, совпадает, если имя диска начинается с `/var` и заканчивается на `/backup`. * `$or($prefix(/home/),$eq(/root))`, совпадает, если имя диска начинается с `/home` или равно `/root`. Скобки **(** и **)**, которые являются частью имени диска, **должны экранироваться тильдой (~)** | Required |
| Правила обнаружения `detectionConditions` | [detectionCondition](#detectionCondition)[] | Набор правил для определения, к каким дискам применяется политика. Правила могут срабатывать по свойствам диска (общий размер, файловая система, тип диска) или host resource attributes. Каждый тип свойства диска можно задать не более одного раза на политику. | Required |
| Свойства `eventProperties` | Set<[MetadataItem](#MetadataItem)> | Набор дополнительных key-value свойств, прикрепляемых к создаваемому event. Доступные ключи свойств можно получить через [Events API v2](https://dt-url.net/9622g1w). Дополнительно любой Host resource attribute может подставляться динамически (agent 1.325+) | Required |

##### Объект `Alert`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Триггер `trigger` | enum | Возможные значения: * `AVAILABLE_DISK_SPACE_MEBIBYTES_BELOW` * `AVAILABLE_DISK_SPACE_PERCENT_BELOW` * `AVAILABLE_INODES_NUMBER_BELOW` * `AVAILABLE_INODES_PERCENT_BELOW` * `READ_TIME_EXCEEDING` * `WRITE_TIME_EXCEEDING` * `READ_ONLY_FILE_SYSTEM` | Required |
| `thresholdPercent` | float | - | Required |
| `thresholdMilliseconds` | float | - | Required |
| `thresholdMebibytes` | float | - | Required |
| `thresholdNumber` | float | - | Required |
| `sampleCountThresholdsImmediately` | [SampleCountThresholdsImmediately](#SampleCountThresholdsImmediately) | - | Required |
| `sampleCountThresholds` | [SampleCountThresholds](#SampleCountThresholds) | - | Required |

##### Объект `detectionCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Scope правила `ruleType` | enum | Начиная с agent 1.335 поддерживаются detection rules для **disk**. Возможные значения: * `RuleTypeDisk` * `RuleTypeHost` | Required |
| Свойство диска `property` | enum | Возможные значения: * `DiskTotalSpace` * `DiskFilesystem` * `DiskType` | Required |
| Пороги общего размера диска `diskTotalCondition` | [DiskTotalSpaceThresholds](#DiskTotalSpaceThresholds) | Укажите диапазон общего размера диска в GiB | Required |
| Условие файловой системы `diskFilesystemCondition` | text | Файловая система диска попадает в эту политику, если совпадает **любой** из фильтров. Тип файловой системы должен соответствовать требуемому формату. * `$match(ext*)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(fs)`, совпадает, если `fs` встречается в типе файловой системы. * `$eq(ext4)`, совпадает, если `ext4` равно типу файловой системы. * `$prefix(ext)`, совпадает, если `ext` является префиксом типа файловой системы. * `$suffix(fs)`, совпадает, если `fs` является суффиксом типа файловой системы. Доступные логические операции: * `$not($eq(tmpfs))`, совпадает, если тип файловой системы отличается от `tmpfs`. * `$and($prefix(ext),$suffix(4))`, совпадает, если тип файловой системы начинается с `ext` и заканчивается на `4`. * `$or($eq(xfs),$eq(btrfs))`, совпадает, если тип файловой системы равен `xfs` или `btrfs`. Скобки **(** и **)**, которые являются частью типа файловой системы, **должны экранироваться тильдой (~)** | Required |
| `localDiskCondition` | enum | Возможные значения: * `LOCAL` * `REMOTE` | Required |
| Resource attribute `hostMetadataCondition` | [HostMetadataConditionType](#HostMetadataConditionType) | Host resource attributes, это dimensions, обогащающие host, включая custom metadata (пользовательские key-value пары, которые можно присваивать hosts, мониторимым Dynatrace). Через custom metadata можно дополнять данные мониторинга контекстом, специфичным для нужд организации: имена environment, ответственность команд, версии приложения и т.д. См. [Define tags and metadata for hosts](https://dt-url.net/w3hv0kbw). Note: начиная с версии 1.325 host resource attributes поддерживаются наряду с host custom metadata. | Required |

##### Объект `MetadataItem`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `metadataKey` | text | Введите 'dt.' для подсказок ключей. | Required |
| Значение `metadataValue` | text | Введите '{' для подсказок placeholder. | Required |

##### Объект `SampleCountThresholdsImmediately`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Sample-нарушения `violatingSamples` | integer | Количество **10-секундных samples** в окне оценки, которые должны превысить порог для триггера event | Required |
| Размер окна оценки для sample-нарушений `violatingEvaluationWindow` | integer | Количество **10-секундных samples**, образующих скользящее окно оценки для обнаружения sample-нарушений. | Required |
| Sample-дезалертинга `dealertingSamples` | integer | Количество **10-секундных samples** в окне оценки, которые должны быть ниже порога для закрытия event | Required |
| Размер окна оценки для sample-дезалертинга `dealertingEvaluationWindow` | integer | Количество **10-секундных samples**, образующих скользящее окно оценки для дезалертинга. | Required |

##### Объект `SampleCountThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Sample-нарушения `violatingSamples` | integer | Количество **10-секундных samples** в окне оценки, которые должны превысить порог для триггера event | Required |
| Размер окна оценки для sample-нарушений `violatingEvaluationWindow` | integer | Количество **10-секундных samples**, образующих скользящее окно оценки для обнаружения sample-нарушений. | Required |
| Sample-дезалертинга `dealertingSamples` | integer | Количество **10-секундных samples** в окне оценки, которые должны быть ниже порога для закрытия event | Required |
| Размер окна оценки для sample-дезалертинга `dealertingEvaluationWindow` | integer | Количество **10-секундных samples**, образующих скользящее окно оценки для дезалертинга. | Required |

##### Объект `DiskTotalSpaceThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог сверху (необязательно) `thresholdAbove` | integer | Если поле пустое, нижний предел отсутствует. Минимальный общий размер диска в GiB | Optional |
| Порог снизу (необязательно) `thresholdBelow` | integer | Если поле пустое, верхний предел отсутствует. Максимальный общий размер диска в GiB | Optional |

##### Объект `HostMetadataConditionType`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `hostMetadataCondition` | [HostMetadataCondition](#HostMetadataCondition) | - | Required |

##### Объект `HostMetadataCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ должен существовать `keyMustExist` | boolean | Когда включено, условие требует, чтобы resource attribute существовал и удовлетворял ограничениям; когда выключено, ключ необязателен, но при наличии всё равно должен удовлетворять ограничениям. | Required |
| Ключ `metadataKey` | text | - | Required |
| Условие `metadataCondition` | text | Строка должна соответствовать требуемому формату. * `$match(ver*_1.2.?)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(production)`, совпадает, если `production` встречается в значении host metadata. * `$eq(production)`, совпадает, если `production` равно значению host metadata. * `$prefix(production)`, совпадает, если `production` является префиксом значения host metadata. * `$suffix(production)`, совпадает, если `production` является суффиксом значения host metadata. Доступные логические операции: * `$not($eq(production))`, совпадает, если значение host metadata отличается от `production`. * `$and($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` и заканчивается на `main`. * `$or($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` или заканчивается на `main`. Скобки **(** и **)**, которые являются частью свойства, **должны экранироваться тильдой (~)** | Required |