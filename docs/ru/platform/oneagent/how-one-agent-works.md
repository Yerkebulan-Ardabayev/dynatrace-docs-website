---
title: How OneAgent works
source: https://www.dynatrace.com/docs/platform/oneagent/how-one-agent-works
scraped: 2026-03-01T21:11:59.466466
---

# How OneAgent works

# How OneAgent works

* Latest Dynatrace
* 2-min read
* Published Oct 13, 2018

OneAgent comprises a set of specialized processes that run on each monitored host. It collects metrics from the operating system on which it runs, and compares the metrics to expected performance values. The most important metrics are then reported to Dynatrace.

## Processes

In addition, OneAgent detects which processes run on each host and collects performance metrics for the most important processes. OneAgent can also perform more detailed monitoring of specific technologies (such as Java, Node.js, .NET, and others) by injecting itself into those processes and monitoring their performance from within. This provides you with code-level insights into the services that your applications rely on.

## Real user monitoring

To deliver Real User Monitoring, OneAgent injects a JavaScript tag into the HTML of each application page that is rendered by your web servers. With these JavaScript tags in placeâalong with a corresponding module that is automatically installed on your web server and requires no configurationâOneAgent is able to monitor the response times and performance experienced by your customers in their mobile and desktop browsers.

## Log monitoring

OneAgent is also capable of monitoring the log files of a specific host or a specific process group. It can discover and analyze system or process-created logs. Depending on your configuration, you can store these log files, which makes the log data available independently of the log files themselves. This can be beneficial in the following situations:

* Short log-retention periods
* Volatile log storage
* Legal requirements to keep logs archived centrally

## Network

OneAgent can dig deeper and get network metrics at the process level. Thanks to process-to-process monitoring of network communications Dynatrace can:

* Ensure high-quality process communications over networks.
* Understand your network topology in dynamic environments.
* Monitor process-level network capacity.
* Perform integrated network health monitoring.

## Communication

Communication from OneAgent to Dynatrace is outbound only and Dynatrace never initiates communication with OneAgent. Because of this, when using Dynatrace, there is no need to open ports for inbound communication.  
OneAgent can connect directly to Dynatrace Cluster or it can communicate via one or more [Dynatrace ActiveGates](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."). Simultaneous connection via multiple ActiveGates is possible. OneAgent determines which ActiveGates to communicate through based on the information it receives from Dynatrace Cluster.

OneAgent reports its collected data via HTTP/S requests to the ActiveGates or the Dynatrace Cluster. If [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.") is enabled, the OneAgent will create a WebSocket session to the ActiveGates or the Cluster to allow realtime communication and reporting of its collected snapshots. WebSocket sessions are multiplexed by the ActiveGates to limit network load and are load balanced by the OneAgents.