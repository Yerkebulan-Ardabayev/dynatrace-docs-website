---
title: Автоматическое обогащение журналов (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation
scraped: 2026-03-06T21:33:08.142213
---

# Автоматическое обогащение журналов (Logs Classic)

# Автоматическое обогащение журналов (Logs Classic)

* Classic
* Объяснение
* 3-минутное чтение
* Обновлено 07 апреля 2023 г.

Мониторинг журналов Classic

Для самой новой версии Dynatrace см. [Автоматическое обогащение журналов](../../logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa.md "Общее получение журналов автоматически преобразует журнальные данные в выходные значения для атрибута loglevel.").

Dynatrace позволяет преобразовывать журналы, полученные как через OneAgent, так и через API.

## Преобразование журналов, полученных через API

Получение журналов API автоматически преобразует ключи серьёзности `status`, `severity`, `level` и `syslog.severity` в атрибут `loglevel`.

Входные значения для ключей серьёзности `status`, `severity`, `level` и `syslog.severity` преобразуются (преобразование не зависит от регистра) в выходные значения для атрибута `loglevel` на основе приведенной ниже сопоставления:

## Преобразование всех типов журналов

Это преобразование применяется как к журналам, полученным через OneAgent, так и к журналам, полученным через API.

Кроме того, для каждого события журнала создается атрибут `status` со значением, которое представляет собой сумму значений `loglevel` на основе следующей группировки:

Например:
Ключ серьёзности `level` в параметре запроса получения журналов API содержит значение `serious`.

1. Ключ серьёзности `level` преобразуется в атрибут `loglevel` со значением `serious`, сопоставленным с `SEVERE` на основе таблицы выше.
2. Атрибут `loglevel` со значением `SEVERE` группируется в атрибут `status`. На основе таблицы группировки выше атрибут `status` будет содержать значение `ERROR`.
3. Для деталей события журнала просмотрщик журналов отчетывает следующее:

* **status** - `ERROR`
* **loglevel** - `SEVERE`

## Атрибуты, добавленные во время получения журнала через OneAgent

Во время получения журнала через OneAgent добавляются следующие атрибуты автоматически:

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

* [Получение журналов API](../../logs/lma-log-ingestion/lma-log-ingestion-via-api.md "Потоковое получение журнальных данных в Dynatrace с помощью API и преобразование его в осмысленные сообщения журнала.")
* [Получение журналов через OneAgent](../../logs/lma-log-ingestion/lma-log-ingestion-via-oa.md "Получение журнальных данных в Dynatrace с помощью OneAgent и преобразование его в осмысленные сообщения журнала.")