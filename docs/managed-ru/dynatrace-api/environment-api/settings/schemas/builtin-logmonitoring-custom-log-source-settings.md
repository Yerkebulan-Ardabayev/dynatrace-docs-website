---
title: Settings API - Custom log sources schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-custom-log-source-settings
scraped: 2026-05-12T11:49:40.248333
---

# Settings API - Custom log sources schema table

# Settings API - Custom log sources schema table

* Published Dec 05, 2023

### Пользовательские источники логов (`builtin:logmonitoring.custom-log-source-settings)`

Добавьте пользовательские источники логов до создания правила ingest логов в случае, когда:

* процесс не является важным (то есть источник лога не определяется OneAgent автоматически)
* нужны логи Windows event logs (кроме Windows system log, Windows security log и Windows Application log)
* нужны логи AIX
* нужно разрешить бинарный контент
* используется неподдерживаемый шаблон ротации

OneAgent автоматически обнаруживает новые файлы логов для важных процессов на поддерживаемых платформах. Автоматически обнаруженные логи перечислены на экранах Process Group Instance или Host.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.custom-log-source-settings` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.custom-log-source-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.custom-log-source-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.custom-log-source-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Активно `enabled` | boolean | - | Required |
| Имя `config-item-title` | text | - | Required |
| `custom-log-source` | [CustomLogSource](#CustomLogSource) | - | Required |
| Контекст источника лога `context` | Set<[Context](#Context)> | Определять пользовательский источник лога только в контексте, если он задан | Required |

##### Объект `CustomLogSource`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип источника лога `type` | enum | Возможные значения: * `LOG_PATH_PATTERN` * `WINDOWS_EVENT_LOG` | Required |
| Принимать бинарный контент `accept-binary` | boolean | - | Optional |
| Кодировка `encoding` | text | - | Optional |
| Источник лога `values-and-enrichment` | Set<[CustomLogSourceWithEnrichment](#CustomLogSourceWithEnrichment)> | Это может быть абсолютный путь к лог-файлу(ам) с опциональными wildcard либо имя Windows Event Log. | Required |

##### Объект `Context`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Атрибут `attribute` | enum | Возможные значения: * `dt.entity.process_group` | Required |
| `values` | set | - | Required |

##### Объект `CustomLogSourceWithEnrichment`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Значения `path` | text | - | Required |
| Обогащения `enrichment` | Set<[Enrichment](#Enrichment)> | Опциональное поле, позволяющее задать атрибуты, которые обогатят логи.  ${N} можно использовать в значении атрибута, чтобы подставить значение, совпавшее с wildcard; здесь N означает номер wildcard для подстановки | Required |

##### Объект `Enrichment`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| тип `type` | enum | Возможные значения: * `attribute` | Required |
| ключ `key` | text | - | Optional |
| значение `value` | text | - | Optional |