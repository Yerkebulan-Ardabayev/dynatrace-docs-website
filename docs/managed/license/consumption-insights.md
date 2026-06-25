---
title: Get detailed consumption insights
source: https://docs.dynatrace.com/managed/license/consumption-insights
scraped: 2026-05-12T11:37:22.818149
---

# Get detailed consumption insights

# Get detailed consumption insights

* How-to guide
* 11-min read
* Published Mar 31, 2025

This section summarizes how to identify the root causes of increased usage per DPS capability and how to resolve issues with unwanted or excessive consumption.
Most DPS capabilities offer a set of DPS consumption metrics that can be analyzed in the Data Explorer to help identify increases in related costs.

## Full-Stack Monitoring

### Potential root cause

* The number of hosts monitored with Full-Stack Monitoring might have increased.
* The memory footprint of hosts monitored with Full-Stack Monitoring might have increased.

### How to verify

Use Data Explorer to chart (DPS) Full-Stack Monitoring billing usage per host and split by hosts to determine if there was an increase in the number of hosts monitored with Full-Stack Monitoring or if the memory footprint of the monitored hosts increased, and if so, to see which hosts are affected.

### Resolution options

Disable host monitoring on unintentionally monitored Full-Stack hosts or switch to Infrastructure Monitoring for non-critical hosts.

## Infrastructure Monitoring

### Potential root cause

The number of hosts monitored with Infrastructure Monitoring increased.

### How to verify

Use Data Explorer to chart (DPS) Infrastructure Monitoring billing usage to determine if there was an increase in the number of hosts monitored with Infrastructure Monitoring.

### Resolution options

Disable host monitoring on unintentionally monitored hosts or switch to Foundation & Discovery for non-critical hosts.

## Code Monitoring

### Potential root causes

* New hosts/containers were detected under the existing rules.
* Monitored hosts/containers are running for longer than they need to be.

### How to verify

* Check the Observability for Developers settings and monitoring rules to see if any hosts/containers have been instrumented with Code Monitoring.
* Use Account Management for an environment-level view of usage.
* Use Notebooks for deep insights into which specific hosts/containers are responsible for the increase.

### Resolution options

* Use Observability for Developers rules to include only business-critical services and applications.
* If there is no need to access code-level data, disable Code Monitoring at the environment level.

## Runtime Vulnerability Analytics (RVA)

### Potential root cause

* Application Security monitoring was enabled with Third-party or Code-Level Vulnerability Analytics.
* Application Security monitoring rules changed, which led to an increased number of monitored hosts.
* New hosts matching existing Application Security monitoring criteria were detected and are now monitored.
* Monitored hosts running for longer periods of time.
* Monitored hosts were assigned more memory.

### How to verify

* Check the Application Security settings and monitoring rules.
* Use the Security Overview app to see the current host coverage stats.
* Use Account Management for an environment view on usage and Data Explorer for deep insights into which hosts are responsible for the increase (for example, `(DPS) Runtime Vulnerability Analytics billing usage per host`, split by host).

### Resolution options

* Adjust Application Security monitoring rules to include only business-critical services and applications in your environment.
* Disable monitoring for unused or non-critical technologies (for example, .NET, and Go).
* Disable Code-level Vulnerability Analytics if there is no need for custom code monitoring.
* Disable Third-party Vulnerability Analytics to permanently turn off Application Security monitoring.

## Runtime Application Protection (RAP)

### Potential root cause

* Application Security monitoring was enabled with Runtime Application Protection.
* Application Security monitoring rules changed, which led to increased number of monitored hosts.
* New hosts matching existing Application Security monitoring criteria were detected and are now monitored.
* Monitored hosts running for longer periods of time.
* Monitored hosts were assigned more memory.

### How to verify

* Check the Application Security settings and monitoring rules.
* Use Account Management for an environment view on usage and Data Explorer for deep insights on which hosts are responsible for the increase (for example, `(DPS) Runtime Vulnerability Analytics billing usage per host`, split by host).

### Resolution options

* Adjust Application Security monitoring rules to only include business-critical services and applications in your environment.
* Disable monitoring for unused or non-critical technologies (for example, .NET, and Go).
* Disable Runtime Application Protection to permanently turn off Application Security protection.

## Real User Monitoring (RUM)

### Potential root cause

Increased number of Sessions because of:

* Enabling of RUM on more frontend applications
* Increasing capture rate to 100% (if it was lower before)
* Increased traffic on customer frontends

### How to verify

In Data Explorer, chart the `(DPS) Real-user monitoring (web and/or mobile) billing usage by frontend application` metric to see

* The number of frontend applications with enabled RUM
* The Capture Rate per frontend application

### Resolution options

* Reduce capture rate.
* Disable RUM on a selected frontend application.

## RUM with Session Replay

### Potential root cause

Increased number of sessions with Session Replay, because:

* Turned on Session Replay on more applications
* Increased capture rate to 100%
* Increased traffic on customer applications

### How to verify

In Data Explorer, chart the `(DPS) Real-user monitoring (web) with Session Replay billing usage by application` metric to see

* The number of applications with Session Replay turned on
* The Capture Rate per application

### Resolution options

* Disable Session Replay on applications.
* Reduce capture rate.

## Browser monitor / clickpath

### Potential root cause

Increased number of executions because:

* New monitors were added, or frequency increased, or customer starting executing it from higher number of locations
* Clickpath definition change, adding more steps triggering web request or XHR

### How to verify

* Validate with team which synthetic monitor configuration changes were performed recently.
* Check the configuration.

### Resolution options

To limit consumption, consider limiting the number of executions by reducing the number of monitors, frequency, number of locations used, or the number of steps. Alternatively, disable some monitors.

## Third-party Synthetic API

### Potential root cause

More test results ingested to Dynatrace with Synthetic Third-party API.

### How to verify

* Check if there are new Third-party test results.
* Check if for earlier existing Third-party test where there was an increase in the frequency or number of locations.

### Resolution options

Consider how consumption can be limited by decreasing the amount of data ingested with Synthetic Third-Party API.

## HTTP monitor

### Potential root cause

Increased number of executions because:

* New monitors were added, the frequency increased, or the customer started to execute the monitor from a higher number of locations
* Multistep HTTP monitor configuration change, more steps have been added

### How to verify

* Validate with team which synthetic monitor configuration changes were performed recently.
* Check the configuration.

### Resolution options

Consider how you can limit the number of executions by reducing the number of monitors, frequency, number of locations used, or the number of steps.
Alternatively, disable some monitors.

## Custom Metrics Classic

### Potential root cause

* **Problem**: Unexpected increase in custom metrics.
* **Root cause**: a certain custom metric generates high consumption of metric data points.

### How to verify

Use Data Explorer to

* Chart (DPS) Recorded metric data points per metric key if there was an increase in metric data points consumption.
* Discover which custom metric started reporting an increased number of metric data points.

### Resolution options

* If a custom metric comes from a cloud service, go to Settings and add/delete the custom metric from the cloud service.
* If a custom metric comes from an extension, go to monitoring configurations of the extension and disable the feature set for the custom metric.

## Log Monitoring Classic

### Potential root cause

* **Problem**: Unexpected increase in logs ingest.
* **Root cause**: Someone enabled ingest of all logs in logs ingest rules.

### How to verify

In Data Explorer, chart the `(DPS) Total Log Monitoring Classic billing usage` metric to see if there was an increase in total number of log records.

### Resolution options

* Use OneAgent filtering features to ingest relevant logs.
* Add granular access control for logs configuration.

## Custom Traces Classic

### Potential root cause

* Increased load for existing entities (for example, Black Friday scenarios).
* Increased number of monitored entities.

### How to verify

* Determine entities emitting traces by charting the `builtin:billing.custom_traces_classic.usage_by_entity:splitBy("dt.entity.monitored_entity"):auto:splitBy():count` metric in Data Explorer.
* Identify trace volume by entity charting the `builtin:billing.custom_traces_classic.usage_by_entity:splitBy("dt.entity.monitored_entity")` metric in Data Explorer.

### Resolution options

Evaluate for which entities tracing is needed and consider reducing the number of monitored entities.

## Custom Events Classic

### Potential root cause

Someone is sending more data to the API endpoint.

## Serverless Functions Classic

### Potential root cause

* Increased load for existing serverless functions (for example, Black Friday scenarios).
* Increased number of monitored serverless functions.

### How to verify

* Look into the average number of invocations by function using the average of the `builtin:billing.serverless_functions_classic.usage_by_function` metric in Data Explorer.
* Look whether total number of monitored functions has increased by using the count for the `builtin:billing.serverless_functions_classic.usage_by_function` metric in Data Explorer.

### Resolution options

Evaluate for which serverless functions tracing is needed and consider using metrics only where appropriate.
Alternatively, reduce the number of monitored functions.

## Additional consideration for Workflows

A workflow can cause cost increases for any licensing capability depending on what the workflow does and how it is configured.
For example, a cost increase in Query and AppEngine Functions may be caused by a workflow that starts every minute.
This might be a misconfiguration or intentional.
Either way, it requires consideration of Workflows in addition to the individual capability (Query or AppEngine Function in this example).

## Related topics

* [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.")
* [Access your DPS cost overview](/managed/license/cost-overview "View license and subscription usage and consumption history for Dynatrace SaaS, Dynatrace Managed, and the Dynatrace platform subscription model.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)