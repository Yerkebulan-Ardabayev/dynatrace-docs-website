---
title: Topology and Smartscape API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape
scraped: 2026-03-06T21:12:56.066698
---

# Topology and Smartscape API


* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](entity-v2.md "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](../basics/deprecation-migration-guides/topology-v1-to-entity-v2.md "Migrate your automation to the Monitored entities API.").

The **Topology and Smartscape** API delivers details about applications, services, process groups, and infrastructure entities that Dynatrace automatically detects and monitors within a given environment.

The returned information contains important attributes about the monitored entities as well as outgoing and incoming relationships. This family of endpoints is organized along the five major environment layers: applications, hosts, processes, process groups, and services.

### Applications

* [Fetch the list](topology-and-smartscape/applications-api/get-all.md "List all monitored applications via Dynatrace API.")
* [Get details](topology-and-smartscape/applications-api/get-an-app.md "View a monitored application via Dynatrace API.")
* [Assign tags](topology-and-smartscape/applications-api/post-tags.md "Assign tags to a monitored application via Dynatrace API.")
* [Get baseline data](topology-and-smartscape/applications-api/get-baseline.md "View the baseline data of a monitored application via Dynatrace API.")

### Hosts

* [Fetch the list](topology-and-smartscape/hosts-api/get-all.md "List all monitored hosts via Dynatrace API.")
* [Get details](topology-and-smartscape/hosts-api/get-a-host.md "View a monitored host via Dynatrace API.")
* [Assign tags](topology-and-smartscape/hosts-api/post-tags.md "Assign tags to a monitored host via Dynatrace API.")

### Processes

* [Fetch the list](topology-and-smartscape/processes-api/get-all.md "List all monitored processes via Dynatrace API.")
* [Get details](topology-and-smartscape/processes-api/get-a-process.md "View a monitored process via Dynatrace API.")

### Process groups

* [Fetch the list](topology-and-smartscape/process-groups-api/get-all.md "List all monitored process groups via Dynatrace API.")
* [Get details](topology-and-smartscape/process-groups-api/get-a-process-group.md "View a monitored process group via Dynatrace API.")
* [Assign tags](topology-and-smartscape/process-groups-api/post-tags.md "Assign tags to a monitored process group via Dynatrace API.")

### Services

* [Fetch the list](topology-and-smartscape/services-api/get-all.md "Lists all monitored services via Dynatrace API.")
* [Get details](topology-and-smartscape/services-api/get-a-service.md "View a monitored service via Dynatrace API.")
* [Assign tags](topology-and-smartscape/services-api/post-tags.md "Assign tags to a service via Dynatrace API.")
* [Get baseline data](topology-and-smartscape/services-api/get-baseline.md "View the baseline data of a monitored service via Dynatrace API.")

### Create a custom device

[Create a custom device](topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api.md "Learn how you can use the Dynatrace API to create a custom device.") with the exact parameters you need.

### Send data to a custom device

[Report custom device metric](topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api.md "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.").

## Related topics

* [Visualize your environment through Smartscape Classic](../../analyze-explore-automate/smartscape-classic.md "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.")