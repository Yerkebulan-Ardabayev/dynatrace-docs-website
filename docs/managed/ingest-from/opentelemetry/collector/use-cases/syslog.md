---
title: Ingest syslog data with the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/syslog
---

# Ingest syslog data with the OTel Collector

# Ingest syslog data with the OTel Collector

* How-to guide
* 3-min read
* Published Jan 26, 2024

The following configuration example shows how to configure a Collector instance to receive data from syslog and send it to the Dynatrace backend.

## Prerequisites

* One of the following Collector distributions with the [attributes processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/attributesprocessor) and the [Syslog receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/syslogreceiver):

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



syslog/f5:



tcp:



listen_address: "0.0.0.0:54526"



protocol: rfc5424



operators:



- type: add



field: attributes.log.source



value: syslog



- type: add



field: attributes.dt.ip_addresses



value: "1xx.xx.xx.xx1"



- type: add



field: attributes.instance.name



value: "ip-1xx-xx-x-xx9.ec2.internal"



- type: add



field: attributes.device.type



value: "f5bigip"



syslog/host:



tcp:



listen_address: "0.0.0.0:54527"



protocol: rfc5424



operators:



- type: add



field: attributes.log.source



value: syslog



- type: add



field: attributes.device.type



value: "ubuntu-syslog"



processors:



attributes:



actions:



- key: net.host.name



action: delete



- key: net.peer.name



action: delete



- key: net.peer.port



action: delete



- key: net.transport



action: delete



- key: net.host.ip



action: delete



- key: dt.ingest.port



from_attribute: net.host.port



action: upsert



- key: dt.ingest.source.ip



from_attribute: net.peer.ip



action: upsert



- key: net.peer.ip



action: delete



- key: net.host.port



action: delete



- key: syslog.hostname



from_attribute: hostname



action: upsert



- key: hostname



action: delete



- key: syslog.facility



from_attribute: facility



action: upsert



- key: facility



action: delete



- key: syslog.priority



from_attribute: priority



action: upsert



- key: priority



action: delete



- key: syslog.proc_id



from_attribute: proc_id



action: upsert



- key: proc_id



action: delete



- key: syslog.version



from_attribute: version



action: upsert



- key: version



action: delete



- key: syslog.appname



from_attribute: appname



action: upsert



- key: appname



action: delete



- key: message



action: delete



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



logs:



receivers: [syslog/f5, syslog/host]



processors: [attributes]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we use the following components.

### Receivers

Under `receivers`, we specify two instances of the `syslog` receiver as active receiver components for our Collector instance.

The Syslog receiver supports a number of [configuration parameters﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/receiver/syslogreceiver/README.md), which enable you to customize its behavior. For our example, we use the following:

* `tcp`—Specifies a TCP listener for the receiver and configures ports 54526 and 54527
* `protocol`—Specifies the RFC 5424 implementation for our receiver (alternatively, RFC 3164 is also supported)
* `operators`—Configures the operators we apply to each log entry. For our example, we use the [add﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/stanza/docs/operators/add.md) operator to add additional information.

  + `field`—Specifies the name of value we are adding
  + `value`—Specifies the content of the value we are adding

### Processors

Under `processors`, we configure the `attributes` processor to drop and adjust the indicated attributes in our OTLP request.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble our receiver, processor, and exporter objects into a logs pipeline, which uses the receiver instances to obtain syslog data and ingest it into Dynatrace using OTLP.

## Limits and limitations

Logs are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information, see [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Ingest logs from files with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")
* [Ingest FluentD data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Configure the OpenTelemetry Collector to ingest FluentD data.")
* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")