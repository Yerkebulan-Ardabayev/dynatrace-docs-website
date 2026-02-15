---
title: Events powered by Grail overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/events
scraped: 2026-02-15T21:17:36.637514
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

Built-in event kind

Relevant capability

Ingest & Process

Retain[1](#fn-1-1-def)

Query

Dynatrace Intelligence problems and events

Full-Stack Monitoring

Included

First 15 months are included

Included

Kubernetes warning events

Kubernetes Platform Monitoring

60 warning events per pod-hour are included

First 15 months are included

Queries generated from within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** are included

Built-in security events

Runtime Vulnerability Analytics (RVA)

Included

First 3 years are included

Queries generated from within ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** are included

1

Retention beyond the included timeframe is billable as Events powered by Grail - Retain.

## Events - Ingest & Process feature overview

Here's what's included with the Ingest & Process data-usage dimension:

Concept

Explanation

Data delivery

Delivery of events via OneAgent, RUM JavaScript, or Generic Event Ingestion API (via ActiveGate)

Topology enrichment

Enrichment of events with data source and topology metadata

Data transformation

* Add, edit, or drop any business event attribute
* Perform mathematical transformations on numerical values (for example, creating new attributes based on calculations of existing fields)
* Extract business, infrastructure, application, or other data from raw business events.
  This can be a single character, string, number, array of values, or other.
  Extracted data can be turned into a new field, allowing additional querying, filtering, etc.
* Mask sensitive data by replacing specific business attributes with a masked string

Data-retention control

Manage data retention periods of incoming events based on bucket assignment rules

Conversion to timeseries

Create metrics from event attributes (note that creating custom metrics generates additional consumption beyond the consumption for ingestion and processing.)

## Events - Retain feature overview

Here's what's included with the Retain data-usage dimension:

Concept

Explanation

Data availability

Retained data is accessible for analysis and querying until the end of the retention period.
Events retention is defined at the bucket level, ensuring tailored retention periods for specific events.

Retention periods

Choose a retention period

* 10 days (10 days)
* 2 weeks (15 days)
* 1 month (35 days) (this is the default period)
* 3 months (95 days)
* 1 year (372 days)
* 15 months (462 days)
* 3 years (1,102 days)
* 5 years (1,832 days)
* 7 years (2,562 days)
* 10 years (3,657 days)

## Events - Query feature overview

Query data usage occurs when:

* Submitting custom DQL queries in the Logs & Events viewer in advanced mode.
* Business Observability Apps (Business Flow, Salesforce Insights, and Carbon Impact)
* Executing DQL queries in Notebooks, Dashboards, Workflows, Custom apps, and via API.

Here's what's included with the Query data-usage dimension:

Concept

Explanation

On-read parsing

* Use DQL to query historical events in storage and extract business, infrastructure, or other data across any timeframe, and use extracted data for follow-up analysis.
* No upfront indexes or schema required for on-read parsing

Aggregation

Perform aggregation, summarization, or statistical analysis of data in events across specific timeframes or time patterns (for example, data occurrences in 30-second or 10-minute intervals), mathematical, or logical functions.

Reporting

Create reports or summaries with customized fields (columns) by adding, modifying, or dropping existing event attributes.

Context

Use DQL to analyze event data in context with relevant data on the Dynatrace platform, for example, user sessions or distributed traces.

## Related topics

* [Log events](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-events "Create log events based on log data and use them in problem detection.")
* [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
* [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.")
* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)