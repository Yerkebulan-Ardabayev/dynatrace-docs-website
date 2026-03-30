---
title: Extend Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace
scraped: 2026-03-06T21:10:28.052302
---

# Extend Dynatrace


* Latest Dynatrace
* 3-min read
* Published Mar 05, 2018

Dynatrace is an open and extensible platform. You can extend the observability data collected out of the box with data provided by observability standards and frameworks such as OpenTelemetry and Prometheus. And you can also extend Dynatrace analytics capabilities by extending its Smartscape topology and its domain workflows and entity screens via extensions. You can also export data to third-party systems via the APIs and integrations with problem notification systems.

This section focuses on extending telemetry data and creating extensions to centralize and automate the configuration of the data you collect.

[![Dynatrace Developer](https://dt-cdn.net/images/developer-logo-1288bebd8d.svg "Dynatrace Developer")

### Build the apps you need

With Dynatrace AppEngine, you have the ability to build custom functionality on top of all the observability data ingested into Dynatrace in the form of custom apps. Head over to Dynatrace Developer for the tools and support you need to create incredible apps with minimal effort.](https://developer.dynatrace.com/?internal_source=doc&internal_medium=link&internal_campaign=cross)

## Metrics

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OpenTelemetry

Send OpenTelemetry metrics to Dynatrace](opentelemetry.md "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.")[![Micrometer](https://dt-cdn.net/images/mircrometer-d91d5ac640.svg "Micrometer")

### Micrometer

Collect Micrometer metrics from JVM applications](extend-dynatrace/extend-metrics/ingestion-methods/micrometer.md "Learn how to send Micrometer metrics to Dynatrace.")[![Prometheus](https://dt-cdn.net/images/prometheus-b1fab729ac.svg "Prometheus")

### Prometheus

Send Prometheus metrics to Dynatrace](extend-dynatrace/extend-metrics/ingestion-methods/prometheus.md "Learn how to extend observability in Dynatrace with Prometheus metrics.")[![StatsD](https://dt-cdn.net/images/statsd-icon-bigger-800-72b34b3823.png "StatsD")

### StatsD

Send StatsD metrics to Dynatrace](extend-dynatrace/extend-metrics/ingestion-methods/statsd.md "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client.")[![Telegraf](https://dt-cdn.net/images/techn-icon-telegraf-ba9e70e8d6.svg "Telegraf")

### Telegraf

Send Telegraf metrics to Dynatrace](extend-dynatrace/extend-metrics/ingestion-methods/telegraf.md "Ingest Telegraf metrics into Dynatrace.")### Oracle Database

Extend your application observability into data acquired directly from your Oracle Database layer.[![Microsoft SQL Server](https://dt-cdn.net/images/techn-icon-microsoft-sqlserver-60740bd3fa.svg "Microsoft SQL Server")

### Microsoft SQL Server Database

Extend your application observability into data acquired directly from your Microsoft SQL Server layer.](extensions/supported-extensions/data-sources/sql/microsoft-sql.md "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![SNMP](https://dt-cdn.net/images/techn-icon-snmp-43de4f1139.svg "SNMP")

### SNMP

Learn how to monitor your network devices using SNMP.](extensions/supported-extensions/data-sources/snmp.md "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![WMI](https://dt-cdn.net/images/techn-icon-microsoft-e15d516aaf.svg "WMI")

### WMI

Learn how to monitor your devices exposing Windows Management Instrumentation using WMI.](extensions/supported-extensions/data-sources/wmi.md "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")[![JMX](https://dt-cdn.net/images/techn-icon-java-3016283f6a.svg "JMX")

### JMX

Extend observability of your Java applications with JMX metrics.](extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions.md "Learn how to extend Dynatrace monitoring to include applications you've instrumented with JMX.")### Scripting integration

Extend metric observability via Dynatrace' scripting integration.### Metric ingestion API

Extend metric observability via Dynatrace's open Metric APIs.

## Logs

[![FluentD](https://dt-cdn.net/images/techn-icon-fluentd-5634f339de.svg "FluentD")

### FluentD

Learn how to extend log observability in Dynatrace with Fluentd as an alternative to OneAgent-based log collection.](../analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s.md "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.")[![Logstash](https://dt-cdn.net/images/elastic-logstash-a3afbd4913.svg "Logstash")

### Logstash

Learn how to extend log observability in Dynatrace with Logstash as an alternative to OneAgent-based log collection.](https://github.com/dynatrace-oss/logstash-output-dynatrace)### Log ingestion API

Extend log observability via Dynatrace open Log APIs.

## Distributed traces

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OpenTelemetry

Learn how to extend observability with OpenTelemetry tracing.](dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel.md "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.")[![Opentracing](https://dt-cdn.net/images/techn-icon-opentracing-936f2ba1cd.svg "Opentracing")

### OpenTracing

Learn how to extend observability in Dynatrace with OpenTracing.](extend-dynatrace/extend-tracing/opentracing.md "Learn how to integrate OpenTracing with Dynatrace.")### OneAgent SDK

Learn how to extend observability in Dynatrace with the OneAgent SDK.

## Extensions

By leveraging the observability standards and frameworks listed below, you can send metrics, traces, logs, and user experience data to Dynatrace.

Thanks to the declarative manner and the centralized and automated deployment and distribution of the extensions, you can now ingest this data more easily at scale and derive the topological context along with the topology definition. You can use extensions to start monitoring a new technology that is not yet covered by Dynatrace or introduce a new configuration in your environment (for example, organize data into dashboards, create new alerts, and introduce complex metrics).

### Extensions 2.0

Learn how to extend observability using a declarative Extensions 2.0 framework.

## User experience and behavior

### Dynatrace OpenKit

Learn how to extend observability into your mobile and web application with Dynatrace OpenKit.

## OpenTelemetry

OpenTelemetry is an observability framework for cloud-native software used for instrumenting frameworks and components and exporting telemetry data (traces, metrics and logs). [Dynatrace is a key contributorï»¿](https://www.dynatrace.com/news/blog/dynatrace-joins-the-opentelemetry-project/) to this open source project.

You can use OpenTelemetry in Dynatrace into Dynatrace.") to:

* Extend Dynatrace technology coverage for technologies that are not supported out of the box by OneAgent
* Enrich telemetry data with additional spans and metrics

### Basics

Understand how OpenTelemetry makes observability possible across today's complex architectures and technologies. into Dynatrace.")### Metrics

Learn how to extend observability into metrics ingested from OpenTelemetry. into Dynatrace.")### Traces

Learn how to extend observability into traces ingested from OpenTelemetry. into Dynatrace.")