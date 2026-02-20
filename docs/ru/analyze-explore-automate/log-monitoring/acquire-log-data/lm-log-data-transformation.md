---
title: Automatic log enrichment (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation
scraped: 2026-02-20T21:27:22.587626
---

# Automatic log enrichment (Logs Classic)

# Automatic log enrichment (Logs Classic)

* Explanation
* 3-min read
* Updated on Apr 07, 2023

Log Monitoring Classic

For the newest Dynatrace version, see [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.").

Dynatrace enables you to transform logs ingested both via OneAgent and API.

## Transform the API-ingested logs

Log ingestion API automatically transforms `status`, `severity`, `level`, and `syslog.severity` severity keys to the `loglevel` attribute.

The input values for the `status`, `severity`, `level`, and `syslog.severity` severity keys are transformed (transformation is not case sensitive) into output values for the `loglevel` attribute based on the mapping below:

Input value

Output value

Example value

Begins with `emerg` or `f`

`EMERGENCY`

`Emergency`, `fail`, `Failure`

Begins with `e` excluding `emerg`

`ERROR`

`Error`, `error`

Begins with `a`

`ALERT`

`alarm`, `Alert`

Begins with `c`

`CRITICAL`

`Critical`, `crucial`

Begins with `s`

`SEVERE`

`Severe`, `serious`

Begins with `w`

`WARN`

`warn`, `Warning`

Begins with `n`

`NOTICE`

`note`, `Notice`

Begins with `i`

`INFO`

`Info`, `information`

Begins with `d` or `trace` or `verbose`

`DEBUG`

`debug`, `TRACE`, `Verbose`

## Transform all types of logs

This transformation applies both to OneAgent-ingested logs and API-ingested logs.

Additionally, for each log event, a `status` attribute is created with a value that is a sum of `loglevel` values based on the following grouping:

Included `loglevel` values

Combined `status` attribute value

`SEVERE`, `ERROR`, `CRITICAL`, `ALERT`, `FATAL`, `EMERGENCY`

`ERROR`

`WARN`

`WARN`

`INFO`, `TRACE`, `DEBUG`, `NOTICE`

`INFO`

`NONE`

`NONE`

For example:
The `level` severity key in the Log ingestion API request parameter contains the value `serious`.

1. The `level` severity key is transformed into the `loglevel` attribute with the `serious` value mapped to `SEVERE` based on the above table.
2. The `loglevel` attribute containing the `SEVERE` value is grouped into `status` attribute. Based on the grouping table above, the `status` attribute will contain the `ERROR` value.
3. For the log event details, the log viewer will report the following:

* **status** - `ERROR`
* **loglevel** - `SEVERE`

## Attributes added during a log ingest via OneAgent

During the log ingestion via OneAgent, the following attributes are added automatically:

### General attributes (via OneAgent)

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

### dt entity model attributes (via OneAgent)

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

## Related topics

* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")