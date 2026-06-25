---
title: Автоматическое обогащение журналов (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation
scraped: 2026-05-12T11:53:53.523640
---

# Автоматическое обогащение журналов (Logs Classic)

# Автоматическое обогащение журналов (Logs Classic)

* Пояснение
* Чтение: 3 мин
* Обновлено 07 апреля 2023 г.

Log Monitoring Classic

Dynatrace позволяет преобразовывать журналы, принятые как через OneAgent, так и через API.

## Преобразование журналов, принятых через API

API приёма журналов автоматически преобразует ключи серьёзности `status`, `severity`, `level` и `syslog.severity` в атрибут `loglevel`.

Входные значения ключей серьёзности `status`, `severity`, `level` и `syslog.severity` преобразуются (без учёта регистра) в выходные значения атрибута `loglevel` согласно следующей таблице:

| Входное значение | Выходное значение | Пример значения |
| --- | --- | --- |
| Начинается с `emerg` или `f` | `EMERGENCY` | `Emergency`, `fail`, `Failure` |
| Начинается с `e` (кроме `emerg`) | `ERROR` | `Error`, `error` |
| Начинается с `a` | `ALERT` | `alarm`, `Alert` |
| Начинается с `c` | `CRITICAL` | `Critical`, `crucial` |
| Начинается с `s` | `SEVERE` | `Severe`, `serious` |
| Начинается с `w` | `WARN` | `warn`, `Warning` |
| Начинается с `n` | `NOTICE` | `note`, `Notice` |
| Начинается с `i` | `INFO` | `Info`, `information` |
| Начинается с `d`, `trace` или `verbose` | `DEBUG` | `debug`, `TRACE`, `Verbose` |

## Преобразование всех типов журналов

Это преобразование применяется как к журналам, принятым через OneAgent, так и к журналам, принятым через API.

Кроме того, для каждого события журнала создаётся атрибут `status` со значением, являющимся суммой значений `loglevel` согласно следующей группировке:

| Включённые значения `loglevel` | Объединённое значение атрибута `status` |
| --- | --- |
| `SEVERE`, `ERROR`, `CRITICAL`, `ALERT`, `FATAL`, `EMERGENCY` | `ERROR` |
| `WARN` | `WARN` |
| `INFO`, `TRACE`, `DEBUG`, `NOTICE` | `INFO` |
| `NONE` | `NONE` |

Например:
Ключ серьёзности `level` в параметре запроса API приёма журналов содержит значение `serious`.

1. Ключ серьёзности `level` преобразуется в атрибут `loglevel` со значением `serious`, которое сопоставляется с `SEVERE` согласно приведённой таблице.
2. Атрибут `loglevel` со значением `SEVERE` группируется в атрибут `status`. Согласно таблице группировки, атрибут `status` будет содержать значение `ERROR`.
3. В подробностях события журнала просмотрщик журналов отобразит следующее:

* **status** — `ERROR`
* **loglevel** — `SEVERE`

## Атрибуты, добавляемые при приёме журналов через OneAgent

При приёме журналов через OneAgent автоматически добавляются следующие атрибуты:

### Общие атрибуты (через OneAgent)

* `container.name`
* `container.image.name`
* `container.id`
* `dt.host_group.id`
* `dt.kubernetes.cluster.id`
* `dt.kubernetes.cluster.name`
* `dt.kubernetes.node.system_uuid`
* `dt.process.name`
* `event.type`
* `host.name`
* `k8s.cluster.name`
* `k8s.namespace.name`
* `k8s.pod.name`
* `k8s.pod.uid`
* `k8s.container.name`
* `k8s.deployment.name`
* `log.iostream`
* `loglevel`
* `log.source`
* `process.technology`
* `span_id`
* `status`
* `trace_id`
* `web_server.iis.site_id`
* `web_server.iis.site_name`
* `web_server.iis.application_pool`

### Атрибуты модели сущностей dt (через OneAgent)

* `dt.entity.cloud_application`
* `dt.entity.cloud_application_instance`
* `dt.entity.cloud_application_namespace`
* `dt.entity.container_group`
* `dt.entity.container_group_instance`
* `dt.entity.host`
* `dt.entity.kubernetes_cluster`
* `dt.entity.kubernetes_node`
* `dt.entity.process_group`
* `dt.entity.process_group_instance`
* `dt.source_entity`

## Связанные темы

* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранная функция недоступна в Dynatrace Managed.")