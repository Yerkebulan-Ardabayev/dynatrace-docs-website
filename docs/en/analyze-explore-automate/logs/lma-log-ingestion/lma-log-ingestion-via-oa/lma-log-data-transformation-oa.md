---
title: Automatic log enrichment
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa
scraped: 2026-02-15T21:15:52.458899
---

# Automatic log enrichment

# Automatic log enrichment

* Latest Dynatrace
* Tutorial
* 4-min read
* Published Jan 03, 2023

Dynatrace enables you to transform logs ingested via OneAgent.

## Transform the OneAgent-ingested logs

During log ingest via OneAgent, the severity of logs is determined.

### Log severity

By default, the log event severity is detected through a keyword search performed on the first 100 characters of the log content, within the first two lines of text.

To adjust these limits

1. Go to **Settings**.
2. Select **Log Monitoring** > **Advanced log settings**.
3. Adjust the following settings as needed.

   * **Severity search chars limit** is the number of characters in each log line, starting from the first character, to search for severity.
   * **Severity search lines limit** is the number lines in each log entry, starting from the first line, to search for severity.

There are 19 keywords that correspond with 9 severity levels as per the table below:

Keyword

Severity level

trace

DEBUG

debug

DEBUG

fine

DEBUG

finer

DEBUG

finest

DEBUG

notice

NOTICE

info

INFO

information

INFO

warn

WARN

warning

WARN

severe\_warning

WARN

severe

SEVERE

err

ERROR

error

ERROR

crit

CRITICAL

critical

CRITICAL

alert

ALERT

fatal

EMERGENCY

emerg

EMERGENCY

A match occurs and severity is determined when

1. The keyword found is a single word/phrase from the above list, and it is preceded and followed by a space.
2. The keyword found is a single word/phrase from the above list, and it is preceded and followed by one of the four predefined non-alphanumeric symbols, as in the example below:

* `[error]`
* `{error}`
* `{{error}}`
* `<error>`

## Transform all types of logs

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
The `level` severity key in the generic log ingestion API request parameter contains the value `serious`.

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
* [`span_id`](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.")
* `status`
* [`trace_id`](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.")
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

## Resource attributes

All log entries are enriched with host-level resource attributes, such as host tags, cloud attributes, Kubernetes attributes, and more.  
For more details and the full list of host-level attributes, see [Resource attributes](/docs/platform/oneagent/resource-attributes "Any signal that uses a given resource, such as host or process group, is enriched with certain attributes coming from the resource.").  
Kubernetes-specific metadata enrichment is described in [Metadata enrichment of all telemetry originating from Kubernetes workloads](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes").

## Attributes automatically extracted from log content via OneAgent

OneAgent automatically extract attributes found in form `[!dt key1=value1, key2=value2]` and the section itself is removed from content.

For instance:

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=aa764ee37ebaa764ee37eaa764ee37e, dt.span_id=b93ede8b93ede8]
```

will result in additional `dt.trace_id` and `dt.span_id` attributes for log record and actuall content sent will be:

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597
```

## Related topics

* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")