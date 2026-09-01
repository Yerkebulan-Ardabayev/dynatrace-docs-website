---
title: Platform extensions overview (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/platform-extensions
---

# Platform extensions overview (DPS)

# Platform extensions overview (DPS)

* Overview
* 16-min read
* Updated on Jan 12, 2026

Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.

## Custom Metrics Classic feature overview

You can extend the value of Dynatrace by defining, enabling or ingesting custom metrics.
Dynatrace enables you to integrate third-party data sources, ingest custom metrics via API, leverage extensions, cloud integrations, and more.

Here is a non-exhaustive list of custom metric types:

* Metrics ingested from Amazon CloudWatch, Azure Monitor, or Google Cloud Operations Cloud for Cloud services monitoring
* Metrics ingested from remote extensions for monitoring of databases, network devices, queues, and more
* All API-ingested metrics
* Calculated service metrics, custom DEM metrics, and log metrics

For information about how Custom Metrics Classic consumption translates to your DPS license commit, see [Custom Metrics Classic (DPS)](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

## Log Monitoring Classic feature overview

Dynatrace can ingest log records.
A log record is recognized in one of the following ways:

* Timestamp
* JSON Object

For information about how Log Monitoring Classic consumption translates to your DPS license commit, see [Log Monitoring Classic (DPS)](/managed/license/capabilities/platform-extensions/log-monitoring-classic "Learn how your consumption of the Dynatrace Log Monitoring Classic DPS capability is billed and charged.").

## Custom Traces Classic feature overview

You can [ingest traces](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") into Dynatrace using [OpenTelemetry exporters](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") for applications running on hosts that don't have OneAgent installed.
These distributed traces are sent via the [Trace Ingest API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

For information about how Custom Traces Classic consumption translates to your DPS license commit, see [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions/custom-traces-classic "Learn how your consumption of the Dynatrace Custom Traces Classic DPS capability is billed and charged.").

## Custom Events Classic feature overview

You have the option to configure custom events and/or event-ingestion channels.

Custom created/ingested or subscribed events that might be configured for an environment include:

* Any custom event sent to Dynatrace using the [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").
* Any custom event (such as a Kubernetes event) created from log messages by a [log processing rule](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

For information about how Custom Events Classic consumption translates to your DPS license commit, see [Custom Events Classic (DPS)](/managed/license/capabilities/platform-extensions/custom-events-classic "Learn how your consumption of the Dynatrace Custom Events Classic DPS capability is billed and charged.").

## Serverless Functions Classic feature overview

Dynatrace enables end-to-end observability of serverless Cloud functions based on monitoring data coming from traces, metrics, and logs.

Dynatrace also allows you to ingest logs from your serverless cloud functions.

For information about how Serverless Functions Classic consumption translates to your DPS license commit, see [Serverless Functions Classic (DPS)](/managed/license/capabilities/platform-extensions/serverless-functions-classic "Learn how your consumption of the Dynatrace Serverless Functions Classic DPS capability is billed and charged.").

## Related topics

* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)