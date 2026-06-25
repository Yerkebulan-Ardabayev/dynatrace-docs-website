---
title: Settings API - Timestamp/Splitting patterns schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-timestamp-configuration
scraped: 2026-05-12T11:46:28.572535
---

# Settings API - Timestamp/Splitting patterns schema table

# Settings API - Timestamp/Splitting patterns schema table

* Published Dec 05, 2023

### Шаблоны временной метки и разбиения (`builtin:logmonitoring.timestamp-configuration)`

Dynatrace OneAgent распознаёт ряд форматов временных меток в записях логов. Если в записи лога используются нестандартные временные метки, задайте их ниже. Это обеспечит качество данных для анализа.
Распознавание временной метки также влияет на корректное разбиение лога. Если временная метка не обнаружена или формат лога не позволяет автораспознавание, соседние строки могут быть объединены в одну запись лога (учитываются и отступы).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.timestamp-configuration` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.timestamp-configuration` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.timestamp-configuration` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.timestamp-configuration` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Активно `enabled` | boolean | - | Required |
| Имя `config-item-title` | text | - | Required |
| Шаблон даты и времени `date-time-pattern` | text | - | Required |
| Часовой пояс `timezone` | text | - | Required |
| Лимит поиска временной метки `date-search-limit` | integer | Задаёт количество символов в каждой строке лога (начиная с первого символа), в которых ищется временная метка. | Optional |
| Пропускать строки с отступом `skip-indented-lines` | boolean | Не парсить временные метки в строках, начинающихся с пробельного символа | Optional |
| `matchers` | Set<[Matcher](#Matcher)> | - | Required |
| Шаблон границы записи `entry-boundary` | [EntryBoundary](#EntryBoundary) | Опциональное поле. Введите фрагмент текста строки, с которой начинается запись. Wildcard не поддерживаются, текст трактуется буквально. | Optional |
| Распознавать JSON-формат `json-configuration` | [JSONConfiguration](#JSONConfiguration) | - | Optional |

##### Объект `Matcher`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Атрибут `attribute` | enum | Возможные значения: * `dt.entity.process_group` * `log.source` * `log.source.origin` * `host.tag` * `k8s.container.name` * `k8s.namespace.name` * `k8s.deployment.name` * `k8s.pod.annotation` * `k8s.pod.label` * `k8s.workload.name` * `k8s.workload.kind` * `container.name` * `dt.entity.container_group` * `process.technology` | Required |
| Оператор `operator` | enum | Возможные значения: * `MATCHES` | Required |
| `values` | set | - | Required |

##### Объект `EntryBoundary`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `pattern` | text | - | Optional |

##### Объект `JSONConfiguration`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `formatDetection` | boolean | - | Optional |