---
title: DDUs for custom Davis events
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/davis-data-units/ddu-events
scraped: 2026-03-06T21:32:03.536928
---

# DDUs for custom Davis events


* Classic
* 2-min read
* Published Jul 09, 2021

While there are no additional costs or licensing involved in the default monitoring and reporting of built-in event types via OneAgent or cloud integrations, you have the option to configure custom events and/or event-ingestion channels. Such event-related customizations do result in the consumption of Davis data units."). Custom Davis event ingestion consumes DDUs because it requires significantly more processing and analytical power than does built-in event ingestion via OneAgent of cloud integrations.

## Custom Davis event types that consume DDUs

Custom created/ingested or subscribed events that you might configure for your environment and thereby consume DDUs include:

* Any custom event sent to Dynatrace using the Events API v2 or the [OneAgent API](../../../ingest-from/extend-dynatrace/extend-events.md#oneagent "Learn how to extend event observability in Dynatrace.")
* Any custom event (such as a Kubernetes event) created from log messages by a log event extraction rule

## How DDU consumption is calculated for custom Davis events

DDU consumption for custom Davis events is equivalent to custom metric data point licensing. Every ingested custom event consumes 0.001 DDU. This also applies to updates custom events already sent.

Davis data unit pools

Davis data units pools for events.") allow you to set hard limits on your DDU consumption for events. Go to **Settings** > **Consumption** > **Davis data units pools** and turn on **Enable limit** in the **Events** section to set an annual or monthly limit.

## FAQ

### What can cause consumption shown as entity "Not related to a monitored entity"

The consumption can be caused by events v2 API if no entity selector is provided. See Events v2.

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)