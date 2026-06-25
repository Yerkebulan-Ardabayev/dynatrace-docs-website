---
title: Timeseries API v1 - Custom metrics
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v1/custom-metrics
scraped: 2026-05-12T11:38:38.571892
---

# Timeseries API v1 - Custom metrics

# Timeseries API v1 - Custom metrics

* Reference
* Published Jul 19, 2017

The **Metrics API v1** enables you to create new kinds of network components and to register and send custom metrics for these devices.

A custom network device is any part of your environment that can't run Dynatrace OneAgent. Examples include Firewalls, DataPower gateways, cloud databases, and any other network appliance such as a proxy or gateway. By using the Dynatrace API, it's possible for your own networked box to send custom metrics into Dynatrace based on the native properties of these devices, or to write your own scripts that pull the metrics from your networked or cloud-networked box.

Dynatrace will show the custom device on the host and process level within Smartscape, as the device itself can contain a network IP address as well as listening ports. When communication is detected between a OneAgent-instrumented host and the custom device, the connection will be automatically shown within Smartscape. When your custom devices begin to send in metric values, you can use the metrics on the custom charting tile.

As Dynatrace AI and intelligent problem detection and correlation depend on topological information, each custom device should announce its position within your network infrastructure. By providing the correct IP address, along with a detailed description of the custom device properties, you enable Dynatrace to automatically map your custom device into your existing [Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.") environment.

## Monitoring consumption

[Limited custom metric ingestion and analysis](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") is included in out-of-the-box Dynatrace technology support. To arrange for additional custom metric ingestion and analysis, [contact Dynatrace Salesï»¿](https://www.dynatrace.com/contact/).