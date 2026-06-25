---
title: Settings API - Disk anomaly detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-disk-rules
scraped: 2026-05-12T11:44:52.451281
---

# Settings API - Disk anomaly detection rules schema table

# Settings API - Disk anomaly detection rules schema table

* Published Dec 05, 2023

### Правила обнаружения аномалий дисков (`builtin:anomaly-detection.disk-rules)`

Dynatrace автоматически обнаруживает инфраструктурные аномалии производительности, например нехватку места на диске. Используйте эти настройки (и настройки Infrastructure (`<your-dynatrace-url>//ui/settings/builtin:anomaly-detection.infrastructure-disks "Visit Infrastructure anomaly detection settings"`)) для настройки чувствительности обнаружения, задания порогов оповещений или отключения оповещений по дискам.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.disk-rules` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.disk-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.disk-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.disk-rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Включено `enabled` | boolean | - | Required |
| Метрика для оповещения `metric` | enum | Возможные значения: * `LOW_DISK_SPACE` * `LOW_INODES` * `READ_TIME_EXCEEDING` * `WRITE_TIME_EXCEEDING` | Required |
| Оповестить, если меньше чем `thresholdPercent` | float | - | Required |
| Оповестить, если больше чем `thresholdMilliseconds` | float | - | Required |
| Лимит выборки `sampleLimit` | [SampleLimit](#SampleLimit) | Оповещать только если порог был нарушен минимум в *n* из последних *m* выборок | Required |
| Фильтр по имени диска `diskNameFilter` | [DiskNameFilter](#DiskNameFilter) | Применять только к дискам с совпавшим именем | Required |
| Фильтр по хостам `tagFilters` | set | Применять только к хостам с указанными тегами | Required |

##### Объект `SampleLimit`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Минимальное количество нарушающих выборок `violatingSamples` | integer | - | Required |
| ...в последних `samples` | integer | - | Required |

##### Объект `DiskNameFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оператор `operator` | enum | Возможные значения: * `CONTAINS` * `DOES_NOT_CONTAIN` * `EQUALS` * `DOES_NOT_EQUAL` * `STARTS_WITH` * `DOES_NOT_START_WITH` | Required |
| Текст для сопоставления `value` | text | - | Optional |