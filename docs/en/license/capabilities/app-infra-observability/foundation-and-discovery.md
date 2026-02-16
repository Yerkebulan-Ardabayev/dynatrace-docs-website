---
title: Calculate your consumption of Foundation & Discovery (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/app-infra-observability/foundation-and-discovery
scraped: 2026-02-16T09:26:22.967775
---

# Calculate your consumption of Foundation & Discovery (DPS)

# Calculate your consumption of Foundation & Discovery (DPS)

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Dec 10, 2025

Dynatrace OneAgent can be configured for Foundation & Discovery mode, which provides basic monitoring for your hosts (for example, host health, disk status, and OS service status).
Unlike other tools that provide basic monitoring, Foundation & Discovery leverages core OneAgent features: discovery and topology.

Foundation & Discovery mode detects process-to-process communication and populates the [Smartscape topology](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") accordingly.
This provides important clues for AIOps which is included with OneAgent, see [DavisÂ® AI automatic root cause analysis](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") for details.

Broad deployment of Foundation & Discovery mode enables you to select the right monitoring mode for each of your hosts.
A hostâs criticality can be determined based on which processes, technologies, externally accessible services, and topological connections.

OneAgent in all modes also includes automated [log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages."), which consumes [Log Management and Analytics](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

### Host hours

The unit of measure for calculating consumption of host monitoring in Foundation & Discovery mode is a host hour.
Each instance of Dynatrace OneAgent installed and running on an operating system instance (deployed on either a physical or virtual machine) with Foundation & Discovery mode enabled consumes host hours.
The longer that a host is monitored, the more host hours are consumed.
Consumption is independent from a host's memory size.

Host-hour cost of Foundation & Discovery

While Foundation & Discovery and Infrastructure Monitoring both use host hours as their unit of measure for calculating monitoring consumption, Foundation & Discovery has a lower cost per host hour, reflecting its limited capabilities.
For details on [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/), see your rate card, or speak to your Dynatrace account manager.

#### Billing granularity for host-hour consumption

Dynatrace is built for elastic cloud-native environments where hosts and services are rapidly spun up and destroyed.
Therefore, billing granularity for host-hour consumption is based on 15-minute intervals.
When a host is monitored for fewer than 15 minutes in an interval, host-hour consumption is rounded up to 15 minutes before consumption is calculated.

The image below illustrates how host-hour consumption per host, calculated at 15-minute intervals.

![Foundation & Discovery consumption calculation](https://dt-cdn.net/images/discovery-consumption-1974-85ac28a179.webp)

### Metrics

Foundation & Discovery includes basic built-in metrics.
Unlike Full-Stack and Infrastructure Monitoring, Foundation & Discovery doesnât offer included custom metrics.
For more information, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Find out more about the available monitoring modes when using OneAgent.").

## Consumption details: Foundation & Discovery

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Foundation & Discovery.
To use these metrics, in ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer**, enter `DPS` in the **Search** field.
These metrics are also available via the Environment API and your **Account Management** portal (**Usage summary** > **Foundation & Discovery** > **Actions** > **View details**).

(DPS) Foundation & Discovery billing usage
:   Key: `builtin:billing.foundation_and_discovery.usage`

    Dimension: count

    Resolution: 15 min

    Description: Total number of host hours in Foundation & Discovery mode, counted in 15 min intervals.

(DPS) Foundation & Discovery billing usage per host
:   Key: `builtin:billing.foundation_and_discovery.usage_per_host`

    Dimension: `dt.entity.host`

    Resolution: 15 min

    Description: Host hours per host in Foundation & Discovery mode, counted in 15 min intervals.

(DPS) Ingested metric data points for Foundation & Discovery
:   Key: `builtin:billing.foundation_and_discovery.metric_data_points.ingested`

    Dimension: count

    Resolution: 15 min

    Description: Number of metric data points aggregated over all Foundation & Discovery monitored hosts.

(DPS) Ingested metric data points for Foundation & Discovery per host
:   Key: `builtin:billing.foundation_and_discovery.metric_data_points.ingested_by_host`

    Dimension: `dt.entity.host`

    Resolution: 15 min

    Description: Number of metric data points split per Foundation & Discovery monitored host.

## Related topics

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)