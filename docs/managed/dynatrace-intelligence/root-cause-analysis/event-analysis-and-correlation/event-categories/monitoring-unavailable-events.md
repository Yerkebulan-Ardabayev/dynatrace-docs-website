---
title: Monitoring unavailable events
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/monitoring-unavailable-events
---

# Monitoring unavailable events

# Monitoring unavailable events

* Explanation
* 2-min read
* Updated on Feb 27, 2026

A `monitoring unavailable` event indicates a widespread monitoring interruption, where the majority of your installed OneAgents lose their connection with the Dynatrace server.

## Symptoms

This usually manifests itself as a lack of visibility in terms of both availability and performance monitoring. In case of a monitoring interruption:

* Dynatrace automatically suppresses all individual **Host unavailable** problems and alerts you to the monitoring interruption.
* All hosts are set to the availability state **Unmonitored** for the duration of the monitoring outage.

## Probable causes

Monitoring interruptions can have different root causes depending on the type of Dynatrace deployment you're running:

* Dynatrace SaaS environments are administered by the Dynatrace DevOps team, who post all operational issues to [dynatrace.status.io﻿](https://dynatrace.status.io/).
* For environments running in Dynatrace Managed deployments, it's most likely that the monitoring interruption is caused by an issue within your own data center or network configuration.

Regardless of the type of Dynatrace deployment, a common cause of monitoring interruptions is ActiveGate operating issues. To minimize the risk of interruptions caused by ActiveGate, you can use [ActiveGate self-monitoring metrics](/managed/ingest-from/dynatrace-activegate/activegate-sfm-metrics "Explore ActiveGate self-monitoring  metrics.") to assess the health of your ActiveGates in a timely manner.

## Troubleshooting

To troubleshoot a `monitoring unavailable` event, see [Troubleshooting monitoring interruptions](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-monitoring-interruptions "Learn how to deal with different types of monitoring interruptions based on the type of Dynatrace deployment you're running.").

## Problem and alert filtering

The `monitoring unavailable` severity level enables you to filter for these highly critical alerts and quickly route them to your monitoring operations teams.

### Problems

To view `monitoring unavailable` problems

1. Go to **Problems**.
2. In the **Filter by** box, select `Severity`: `Monitoring unavailable`.

For more on problems, see [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.").