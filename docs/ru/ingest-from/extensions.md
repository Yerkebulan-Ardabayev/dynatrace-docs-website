---
title: Extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions
scraped: 2026-02-18T21:16:07.175574
---

# Extensions

# Extensions

* Latest Dynatrace
* Overview
* 2-min read
* Published Jun 16, 2025

## What are Extensions?

Extensions are modular packages that define how Dynatrace collects and structures telemetry data from external sources. Each extension is executed by the Extension Execution Controller (EEC), which runs in your environment.

## How do Extensions work?

Extensions let you expand Dynatrace beyond its out-of-the-box monitoring capabilities. They allow you to collect telemetry data such as metrics, events, and logs from external technologies.

With extensions, you can:

* Ingest data from technologies not natively supported.
* Create tailored monitoring logic for your environment.
* Visualize and analyze custom data.

## Why use Extensions?

Extensions are useful when you need to monitor a technology or service that Dynatrace doesnât automatically detect. They provide advanced customization and observability for nearly any data source.

### Key benefits

* Automatic distribution to ActiveGates and OneAgent with built-in failover.
* Full topology modeling, including custom entities and relationship mapping.
* Rich metric metadata for consistent context-aware monitoring.
* Possibility to create custom extensions tailored to your needs:

  + Declarative, human-readable YAML format (no coding required for featured data sources).
  + Coded extensions using Python data source for flexibility.

### Use cases

* SNMP-based monitoring: Monitor network devices.
* SQL-based monitoring: Monitor SQL databases of various vendors.
* Prometheus-based monitoring: Monitor Prometheus exporters.
* WMI-based monitoring: Monitor Windows devices.
* JMX-based monitoring: Acquire data from JMX MBeans.

## Get started with Extensions

[#### Explore supported Extensions

Learn more about the supported extensions.

* Explanation

Read this explanation](/docs/ingest-from/extensions/supported-extensions)[#### Develop your own Extensions

Develop your own Extensions in Dynatrace.

* How-to guide

Read this guide](/docs/ingest-from/extensions/develop-your-extensions)[#### Manage Extensions

Learn how to manage extensions.

* How-to guide

Read this guide](/docs/ingest-from/extensions/manage-extensions)

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub](https://www.dynatrace.com/hub/detail/extension-manager/)