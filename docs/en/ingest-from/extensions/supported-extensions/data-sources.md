---
title: Understand extensions data sources
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources
scraped: 2026-02-17T21:27:22.646450
---

# Understand extensions data sources

# Understand extensions data sources

* Latest Dynatrace
* Explanation
* 5-min read
* Published Oct 24, 2025

In Dynatrace, a data source is a predefined, technology-specific method for collecting monitoring data from external systems or services using Dynatrace Extensions framework, either by [exensions provided by Dynatrace](/docs/ingest-from/extensions/supported-extensions "Learn more about the supported extensions.") or [custom extensions developed by you](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.").

The extensions data source simplifies monitoring by providing a declarative, technology-specific way to ingest data.

Itâs optimized for common use cases (like SQL, WMI, or Prometheus) while still allowing flexibility through the Python data source for custom scenarios.

## Data source is declarative

The extensions define what to monitor and how to connect to the data source, rather than writing detailed scripts or custom logic for data collection.

## Data source is opinionated

Dynatrace provides a specific, optimized way to retrieve data from each supported technology, ensuring consistency, highest security standards, and best practices for monitoring.

## Types of data sources

Dynatrace offers built-in data sources for widely used technologies, each tailored to specific protocols, APIs, or data collection methods:

### SQL data source

Used to collect metrics or query results from relational databases.

Declaratively configured to run SQL queries against a database and retrieve structured data (for example, query performance, table sizes, connection pools).

See [SQL extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/sql "Extend observability in Dynatrace with declarative metrics ingested from SQL-based extensions.").

### WMI data source

Leverages Windows Management Instrumentation (WMI) to monitor Windows systems.

Provides access to performance counters, system metrics, and hardware details in a standardized way.

See [Manage WMI extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.").

### Prometheus data source

Designed to scrape metrics from Prometheus-compatible endpoints.

Ideal for ingesting time-series data from applications or services exposing Prometheus metrics.

See

### SNMP data source

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your SNMP-monitored devices. To this end, Dynatrace enables you to bring SNMP data into Dynatrace at scale and within the context of all other data.

You can also extend your insights into data related to SNMP traps issued in your infrastructure.

See [Manage SNMP extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.").

### Python data source (the flexible option)

Allows you to write custom Python scripts to collect data from technologies not covered by other data sources.

This is especially useful when you need to interact with custom APIs, proprietary systems, or niche technologies.