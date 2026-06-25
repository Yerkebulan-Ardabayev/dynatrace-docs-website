---
title: Troubleshooting monitoring interruptions
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-monitoring-interruptions
scraped: 2026-05-12T12:13:48.167125
---

# Troubleshooting monitoring interruptions

# Troubleshooting monitoring interruptions

* 4-min read
* Updated on Aug 20, 2025

A monitoring interruption is a situation where the majority of your installed OneAgents lose their connection with the Dynatrace server and usually manifests itself as a lack of visibility in terms of both availability and performance monitoring.

This doesn't necessarily mean an outage of your servers though. In case of a monitoring interruption, Dynatrace automatically suppresses all **Host unavailable** problems and alerts you to the monitoring interruption. All hosts are set to the availability state **Unmonitored** for the duration of the monitoring outage. Monitoring interruption alerts do have a special severity filter within your alerting profiles. The `Monitoring unavailable alert` severity level allows you to create a filter and then deliver these highly critical alerts to your monitoring operations teams.

Monitoring interruptions can have different root causes depending on the type of Dynatrace deployment you're running. Dynatrace SaaS environments are administered by the Dynatrace DevOps team, who post all operational issues to [dynatrace.status.ioï»¿](https://dynatrace.status.io/). For environments running in Dynatrace Managed deployments, it's most likely that the monitoring interruption is caused by an issue within your own data center or network configuration.

Regardless of the type of Dynatrace deployment, a common cause of monitoring interruptions is ActiveGate operating issues. To minimize the risk of interruptions caused by ActiveGate, you can use [ActiveGate self-monitoring metrics](/managed/ingest-from/dynatrace-activegate/activegate-sfm-metrics "Explore ActiveGate self-monitoring  metrics.") to assess the health of your ActiveGates in a timely manner.

## Monitoring interruption in a Dynatrace environment

This situation is detected whenever a Dynatrace environment loses the connection to its OneAgents. We highly recommend checking the following issues within your own network configuration:

* Check whether a recent change in your network or firewall configuration blocks the outgoing monitoring traffic of your OneAgents.
* In case you are routing OneAgent traffic through an ActiveGate, check the operational status of your ActiveGates.

The following is an example alert for a monitoring interruption within a Dynatrace environment.

![Monitoring interruption](https://dt-cdn.net/images/environment-562-c944edfad8.png)

Monitoring interruption

### Monitoring unavailable alert detection

Monitoring unavailable status means that the Dynatrace server didn't receive the heartbeats of your monitored hosts for more than 3 minutes.

* Possible causes include network outages within your data centers, incorrect ActiveGate configuration, and incorrect firewall configuration.
* If the issue is resolved, the monitoring unavailable status should reset after 2 hours.