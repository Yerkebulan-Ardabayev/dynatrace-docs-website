---
title: Platform extensions overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/platform-extensions
scraped: 2026-03-06T21:36:49.590243
---

# Platform extensions overview (DPS)


* Latest Dynatrace
* Overview
* 16-min read
* Updated on Jan 12, 2026

As of January 12, 2026, SaaS platform extensions will no longer be part of the rate card for any new DPS subscription signed on or after that date.
Existing DPS customers will continue to have access to the SaaS platform extensions capabilities.

This page describes the different platform extensions and the features that they provide with a DPS subscription.

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* Custom Events Classic
* Custom Metrics Classic
* Custom Traces Classic
* Log Monitoring Classic
* Serverless Functions Classic

Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.

## Custom Metrics Classic feature overview

You can extend the value of Dynatrace by defining, enabling or ingesting custom metrics.
Dynatrace enables you to integrate third-party data sources, ingest custom metrics via API, leverage extensions, cloud integrations, and more.

Here is a non-exhaustive list of custom metric types:

* Metrics ingested from Amazon CloudWatch, Azure Monitor, or Google Cloud Operations Cloud for Cloud services monitoring
* Metrics ingested from remote extensions for monitoring of databases, network devices, queues, and more
* All API-ingested metrics
* Calculated service metrics, custom DEM metrics, and log metrics

## Log Monitoring Classic feature overview

Dynatrace can ingest log records.
A log record is recognized in one of the following ways:

* Timestamp
* JSON Object

## Custom Traces Classic feature overview

You can ingest traces into Dynatrace using OpenTelemetry exporters into Dynatrace.") for applications running on hosts that don't have OneAgent installed.
These distributed traces are sent via the Trace Ingest API.

## Custom Events Classic feature overview

You have the option to configure custom events and/or event-ingestion channels.

Custom created/ingested or subscribed events that might be configured for an environment include:

* Any custom event sent to Dynatrace using the Events API v2.
* Any custom event (such as a Kubernetes event) created from log messages by a [log processing rule](../../analyze-explore-automate/logs/lma-classic-log-processing.md#lmc-log-processing-rules "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").

## Serverless Functions Classic feature overview

Dynatrace enables end-to-end observability of serverless Cloud functions based on monitoring data coming from traces, metrics, and logs.

Dynatrace also allows you to ingest logs from your serverless cloud functions.

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)