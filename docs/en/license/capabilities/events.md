---
title: Events powered by Grail overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/events
scraped: 2026-02-27T21:19:33.573730
---

# Events powered by Grail overview (DPS)

# Events powered by Grail overview (DPS)

* Latest Dynatrace
* Overview
* 5-min read
* Updated on Jan 28, 2026

This page describes the different Events-related capabilities and the features that they provide with a DPS subscription.

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* [Events - Ingest & Process](/docs/license/capabilities/events/dps-events-ingest "Learn how your consumption of the Events powered by Grail - Ingest & Process DPS capability is billed and charged.")
* [Events - Retain](/docs/license/capabilities/events/dps-events-retain "Learn how your consumption of the Events powered by Grail - Retain DPS capability is billed and charged.")
* [Events - Query](/docs/license/capabilities/events/dps-events-query "Learn how your consumption of the Events powered by Grail - Query DPS capability is billed and charged.")

Dynatrace provides monitoring and reporting of

* Built-in event types via OneAgent or cloud integrations.
* Custom events and/or event-ingestion channels.
  These include

  + Any custom event sent to Dynatrace via the [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") or the [OneAgent API](/docs/ingest-from/extend-dynatrace/extend-events#oneagent "Learn how to extend event observability in Dynatrace.").
  + Any custom event (such as a Kubernetes event) created from log messages by a [log processing rule](/docs/analyze-explore-automate/logs/lma-classic-log-processing#lmc-log-processing-rules "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").
  + Any custom event created in a [processing step](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.") in OpenPipeline.

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

* [Log events](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-events "Create log events based on log data and use them in problem detection.")
* [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
* [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.")
* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)