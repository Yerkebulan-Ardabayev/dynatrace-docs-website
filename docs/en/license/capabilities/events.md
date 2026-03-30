---
title: Events powered by Grail overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/events
scraped: 2026-03-06T21:24:51.504563
---

# Events powered by Grail overview (DPS)


* Latest Dynatrace
* Overview
* 5-min read
* Updated on Jan 28, 2026

This page describes the different Events-related capabilities and the features that they provide with a DPS subscription.

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* Events - Ingest & Process
* Events - Retain
* Events - Query

Dynatrace provides monitoring and reporting of

* Built-in event types via OneAgent or cloud integrations.
* Custom events and/or event-ingestion channels.
  These include

  + Any custom event sent to Dynatrace via the Events API v2 or the [OneAgent API](../../ingest-from/extend-dynatrace/extend-events.md#oneagent "Learn how to extend event observability in Dynatrace.").
  + Any custom event (such as a Kubernetes event) created from log messages by a [log processing rule](../../analyze-explore-automate/logs/lma-classic-log-processing.md#lmc-log-processing-rules "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").
  + Any custom event created in a processing step in OpenPipeline.

The consumption of all events is billable, except for certain included events, as described in the "Included events" table below.

List of billable event types

The following events are billable:

* Business events
* SDLC events
* Custom events, including

  + Security events
  + Davis events
  + Kubernetes warning events
  + Generic custom events
  + Customer-defined custom events

Included events

The table below describes events that are included with a separate rate-card capability package.

1

Retention beyond the included timeframe is billable as Events powered by Grail - Retain.

## Events - Ingest & Process feature overview

Here's what's included with the Ingest & Process data-usage dimension:

## Events - Retain feature overview

Here's what's included with the Retain data-usage dimension:

## Events - Query feature overview

Query data usage occurs when:

* Submitting custom DQL queries in the Logs & Events viewer in advanced mode.
* Business Observability Apps (Business Flow, Salesforce Insights, and Carbon Impact)
* Executing DQL queries in Notebooks, Dashboards, Workflows, Custom apps, and via API.

Here's what's included with the Query data-usage dimension:

## Related topics

* Log events
* Metric events
* Events API v2
* What is Dynatrace Grail?
* License Dynatrace, the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)