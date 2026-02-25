---
title: Adaptive Traffic Management concepts
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-concepts
scraped: 2026-02-25T21:35:26.022937
---

# Adaptive Traffic Management concepts

# Adaptive Traffic Management concepts

* Latest Dynatrace
* Explanation
* 2-min read
* Published Jan 26, 2026

This page describes different terms related to Adaptive Traffic Management.

## Adaptive Traffic Management (ATM)

ATM for Dynatrace Platform Subscription ATM for Dynatrace classic license

**Adaptive Traffic Management (ATM)** is the Dynatrace intelligent trace sampling mechanism for Full-Stack Monitoring.

OneAgent automatically manages the volume of ingested trace data via Adaptive Traffic Management. It continuously adjusts the [adaptive trace sampling rate](#adaptive-trace-sampling-rate) to keep the ingested trace data volume roughly within your [Full-Stack included trace volume](#full-stack-included-trace-volume) or your [total licensed Full-Stack trace volume](#total-licensed-full-stack-trace-volume) (only for the Dynatrace Platform Subscription). This is achieved by monitoring the ingested trace data volume from Full-Stack monitored hosts and applications. If the ingested trace data volume exceeds the allocated trace volume, Adaptive Traffic Management lowers the adaptive trace sampling rate on OneAgent, reducing the trace capture rate and the ingested trace data volume. OneAgent uses head-based sampling, where the sampling decision for each trace is made when a trace is started.

## Adaptive trace sampling rate

ATM for Dynatrace Platform Subscription ATM for Dynatrace classic license

**Adaptive trace sampling rate** is the rate at which Dynatrace OneAgents or other participating tracing agents start distributed traces, where they generally sample traces adaptively.

Adaptive Traffic Management instructs agents to initiate traces at a specific rate, for example, 1,000 per minute. This rate is continuously adjusted to keep the ingested trace data volume below a defined limit. Agents reporting a 100% trace capture rate may start fewer traces than this rate, depending on the number of application transactions. Agents reporting a trace capture rate below 100% are sampling at that rate.

With the Dynatrace Platform Subscription, you can adjust the [adaptive trace sampling rate](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-saas-dps#adjust-adaptive-trace-sampling-rate "Learn how Adaptive Traffic Management works with Dynatrace Platform Subscription (DPS) and how it manages trace sampling for Full-Stack monitored hosts and applications.") at scope level, allowing you to better control the usage of the Full-Stack Monitoring included trace volume.

## Extended trace ingest

ATM for Dynatrace Platform Subscription

**Extended trace ingest** is a billed option allowing you to extend your ingested trace volume on top of your trace volume already included in Full-Stack Monitoring.

For details, see [Extended trace ingest for Full-Stack Monitoring](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#extend-trace-ingest "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").

## Full-Stack included trace volume

ATM for Dynatrace Platform Subscription ATM for Dynatrace classic license

**Full-Stack included trace volume** is the amount of [trace data volume](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#full-stack-traces "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") included in [Full-Stack Monitoring](/docs/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").

Adaptive Traffic Management ensures that Full-Stack monitored hosts and applications stay within this licensed trace volume.

With the Dynatrace Platform Subscription, you can [extend trace ingest](#extended-trace-ingest) beyond the **Full-Stack included trace volume**. In this case, Adaptive Traffic Management ensures that Full-Stack monitored hosts and applications stay within the [total licensed Full-Stack trace volume](#total-licensed-full-stack-trace-volume).

## Total licensed Full-Stack trace volume

ATM for Dynatrace Platform Subscription

**Total licensed Full-Stack trace volume** is the sum of the trace volume included in Full-Stack Monitoring (called [Full-Stack included trace volume](#full-stack-included-trace-volume)) and trace volume added via [extended trace ingest](#extended-trace-ingest).

Adaptive Traffic Management ensures that Full-Stack monitored hosts and applications stay within the total licensed Full-Stack trace volume.

## Usable adaptive trace volume

ATM for Dynatrace Platform Subscription

**Usable adaptive trace volume** is the portion of your [total licensed Full-Stack trace volume](#total-licensed-full-stack-trace-volume) that you allocate to Adaptive Traffic Management.

To control how much of your [Full-Stack included trace volume](#full-stack-included-trace-volume) is distributed by Adaptive Traffic Management, you can [reduce the usable adaptive trace volume](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-saas-dps#reduce-usable-adaptive-trace-volume "Learn how Adaptive Traffic Management works with Dynatrace Platform Subscription (DPS) and how it manages trace sampling for Full-Stack monitored hosts and applications."). This self-service capability also enables you to allocate part of the Full-Stack included trace volume to fixed-rate sampled spans from OpenTelemetry or OneAgent. By doing this, you can manage your excess trace ingest volume more effectively.