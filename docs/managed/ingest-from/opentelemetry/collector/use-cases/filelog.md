---
title: Ingest logs from files with the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/filelog
---

# Ingest logs from files with the OTel Collector

# Ingest logs from files with the OTel Collector

* How-to guide
* 3-min read
* Updated on Apr 09, 2026

The following configuration example shows how to configure a Collector instance to monitor log files and send their log entries to the Dynatrace backend.

## Prerequisites

* One of the following Collector distributions with the [Filelog receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/receiver/filelogreceiver):

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



file_log:



include: [ /path/to/file.log ]



start_at: beginning



operators:



- type: regex_parser



regex: '^(?P<time>\d{4}-\d{2}-\d{2}) (?P<sev>[A-Z]*) (?P<msg>.*)$'



timestamp:



parse_from: attributes.time



layout: '%Y-%m-%d'



severity:



parse_from: attributes.sev



exporters:



otlp_http/dynatrace:



endpoint: ${env:DT_ENDPOINT}



headers:



"Authorization": "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



logs:



receivers: [file_log]



processors: []



exporters: [otlp_http/dynatrace]
```

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Sample log file

For the demo configuration above, we parse the file `file.log` with the following format:

```
1970-01-01 INFO Something routine



1970-01-01 ERROR Some error occurred!



1970-01-01 DEBUG Some details...
```

Each line starts with an ISO 8601 timestamp, followed by the entry's severity level, and finishes with the log message.

We parse each line into its individual parts with the following regular expression:

```
^(?P<time>\d{4}-\d{2}-\d{2}) (?P<sev>[A-Z]*) (?P<msg>.*)$
```

Apart from the two start (`^`) and end (`$`) of line assertions, we have the following named capture groups:

* `(?P<time>\d{4}-\d{2}-\d{2})`—Names its capture group `time` and matches a typical ISO 8601 timestamp.
* `(?P<sev>[A-Z]*)`—Names its capture group `sev` and matches an arbitrary number of Latin uppercase characters.
* `(?P<msg>.*)`—Names its capture group `msg` and matches an arbitrary number of characters.

## Components

For our configuration, we use the following components.

### Receivers

Under `receivers`, we specify the `filelog` receiver as active receiver component for our Collector instance.

The Filelog receiver supports a number of [configuration parameters﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.155.0/receiver/filelogreceiver/README.md), which enable you to customize its behavior. For our example, we use the following:

* `include`—Specifies the path pattern of the files we want to ingest.
* `start_at`—Specifies if the receiver should read from the beginning of the file or, for the most recent entries only, the end.
* `operators`—Configures the operators we apply to each log entry. For our example, we use the [regex\_parser﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.155.0/pkg/stanza/docs/operators/regex_parser.md) operator to extract information using a regular expression.

  + `regex`—Specifies the actual regular expression. By using named capture groups (`(?P<name>)`), the receiver makes the captured data available in `attributes` under the respective name.
  + `timestamp`—Specifies where to take the entry's timestamp from (the `time` field of the regular expression) and the date format.
  + `severity`—Specifies where to take the entry's severity level from (the `sev` field of the regular expression).

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.155.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble our receiver and exporter objects into a traces pipeline, which will continuously monitor the configured files and ingest their entries into Dynatrace using OTLP.

## Limits and limitations

Logs are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information, see [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Ingest FluentD data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Configure the OpenTelemetry Collector to ingest FluentD data.")
* [Ingest syslog data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")