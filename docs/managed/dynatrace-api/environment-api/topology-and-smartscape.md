---
title: Topology and Smartscape API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape
---

# Topology and Smartscape API

# Topology and Smartscape API

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead.

The **Topology and Smartscape** API delivers details about applications, services, process groups, and infrastructure entities that Dynatrace automatically detects and monitors within a given environment.

The returned information contains important attributes about the monitored entities as well as outgoing and incoming relationships. This family of endpoints is organized along the five major environment layers: applications, hosts, processes, process groups, and services.

### Applications

* [Fetch the list](/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all "List all monitored applications via Dynatrace API.")
* [Get details](/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app "View a monitored application via Dynatrace API.")
* [Assign tags](/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags "Assign tags to a monitored application via Dynatrace API.")
* [Get baseline data](/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline "View the baseline data of a monitored application via Dynatrace API.")

### Hosts

* [Fetch the list](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all "List all monitored hosts via Dynatrace API.")
* [Get details](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host "View a monitored host via Dynatrace API.")
* [Assign tags](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags "Assign tags to a monitored host via Dynatrace API.")

### Processes

* [Fetch the list](/managed/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all "List all monitored processes via Dynatrace API.")
* [Get details](/managed/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-a-process "View a monitored process via Dynatrace API.")

### Process groups

* [Fetch the list](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all "List all monitored process groups via Dynatrace API.")
* [Get details](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group "View a monitored process group via Dynatrace API.")
* [Assign tags](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags "Assign tags to a monitored process group via Dynatrace API.")

### Services

* [Fetch the list](/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all "Lists all monitored services via Dynatrace API.")
* [Get details](/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service "View a monitored service via Dynatrace API.")
* [Assign tags](/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/post-tags "Assign tags to a service via Dynatrace API.")
* [Get baseline data](/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline "View the baseline data of a monitored service via Dynatrace API.")

### Create a custom device

[Create a custom device](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Learn how you can use the Dynatrace API to create a custom device.") with the exact parameters you need.

### Send data to a custom device

[Report custom device metric](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.").

## Related topics

* [Visualize your environment through Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.")