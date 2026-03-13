---
title: Automatic log enrichment (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation
scraped: 2026-03-06T21:33:08.142213
---

# Автоматическое обогащение логов (Logs Classic)

# Автоматическое обогащение логов (Logs Classic)

* Classic
* Explanation
* 3-min read
* Updated on Apr 07, 2023

Log Monitoring Classic

Для новейшей версии Dynatrace см. [Автоматическое обогащение логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.").

Dynatrace позволяет преобразовывать логи, принятые как через OneAgent, так и через API.

## Преобразование логов, принятых через API

API приёма логов автоматически преобразует ключи серьёзности `status`, `severity`, `level` и `syslog.severity` в атрибут `loglevel`.

Входные значения ключей серьёзности `status`, `severity`, `level` и `syslog.severity` преобразуются (преобразование не чувствительно к регистру) в выходные значения атрибута `loglevel` согласно приведённому ниже сопоставлению:

## Преобразование всех типов логов

Это преобразование применяется как к логам, принятым через OneAgent, так и к логам, принятым через API.

Кроме того, для каждого события лога создаётся атрибут `status` со значением, являющимся суммой значений `loglevel` на основе следующей группировки:

Например:
Ключ серьёзности `level` в параметре запроса API приёма логов содержит значение `serious`.

1. Ключ серьёзности `level` преобразуется в атрибут `loglevel`, при этом значение `serious` сопоставляется с `SEVERE` согласно приведённой выше таблице.
2. Атрибут `loglevel` со значением `SEVERE` группируется в атрибут `status`. Согласно таблице группировки выше, атрибут `status` будет содержать значение `ERROR`.
3. В сведениях о событии лога просмотрщик логов сообщит следующее:

* **status** - `ERROR`
* **loglevel** - `SEVERE`

## Атрибуты, добавляемые при приёме логов через OneAgent

В процессе приёма логов через OneAgent автоматически добавляются следующие атрибуты:

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

* [API приёма логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Приём логов через OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")
