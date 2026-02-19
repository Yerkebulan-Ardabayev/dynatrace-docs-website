---
title: Topology and Smartscape API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape
scraped: 2026-02-19T21:14:18.207862
---

# Topology and Smartscape API

# Topology and Smartscape API

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

The **Topology and Smartscape** API delivers details about applications, services, process groups, and infrastructure entities that Dynatrace automatically detects and monitors within a given environment.

The returned information contains important attributes about the monitored entities as well as outgoing and incoming relationships. This family of endpoints is organized along the five major environment layers: applications, hosts, processes, process groups, and services.

### Applications

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all "List all monitored applications via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app "View a monitored application via Dynatrace API.")
* [Assign tags](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags "Assign tags to a monitored application via Dynatrace API.")
* [Get baseline data](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline "View the baseline data of a monitored application via Dynatrace API.")

### Hosts

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all "List all monitored hosts via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host "View a monitored host via Dynatrace API.")
* [Assign tags](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags "Assign tags to a monitored host via Dynatrace API.")

### Processes

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all "List all monitored processes via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-a-process "View a monitored process via Dynatrace API.")

### Process groups

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all "List all monitored process groups via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group "View a monitored process group via Dynatrace API.")
* [Assign tags](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags "Assign tags to a monitored process group via Dynatrace API.")

### Services

* [Fetch the list](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all "Lists all monitored services via Dynatrace API.")
* [Get details](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service "View a monitored service via Dynatrace API.")
* [Assign tags](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/post-tags "Assign tags to a service via Dynatrace API.")
* [Get baseline data](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline "View the baseline data of a monitored service via Dynatrace API.")

### Create a custom device

[Create a custom device](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Learn how you can use the Dynatrace API to create a custom device.") with the exact parameters you need.

### Send data to a custom device

[Report custom device metric](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.").

## Related topics

* [Visualize your environment through Smartscape Classic](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.")