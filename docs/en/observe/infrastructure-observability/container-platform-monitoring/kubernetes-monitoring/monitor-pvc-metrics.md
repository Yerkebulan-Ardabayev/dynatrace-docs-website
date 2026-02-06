---
title: Monitor persistent volume claims on Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-pvc-metrics
scraped: 2026-02-06T16:26:41.845142
---

# Monitor persistent volume claims on Kubernetes/OpenShift

# Monitor persistent volume claims on Kubernetes/OpenShift

* 2-min read
* Updated on Jul 09, 2024

This page outlines the minimum version requirements for basic persistent volume claims monitoring capabilities.

Dynatrace version 1.294 +

ActiveGate version 1.289+

In Kubernetes, persistent data is stored in [persistent volume claims (PVCs)ï»¿](https://dt-url.net/n403y11). Dynatrace provides you the needed insights into your persistent volume claims capacity.

* Dynatrace provides **Kubernetes persistent volume claims** preset dashboards that allow you to analyze your persistent volume claims based on total capacity, usage, remaining free space, and growth rates.
* Templates for custom alerts enable you to alert on related issues, such as persistent volume claims running out of free space or growing in an unusual manner.

To start monitoring persistent volume claims, see below.

## Enablement

PVC monitoring is a built-in feature and does not need to be enabled manually.

## Permissions

Make sure that the `get` rule and the `nodes/metrics` resources are enabled in the Kubernetes ClusterRole. If you're monitoring PVCs with an ActiveGate running outside of the cluster, you'll also need the `nodes/proxy` permission.

Example:

![Example PVC permissions](https://dt-cdn.net/images/screenshot-1-1215-23c529f37c.png)

## Dashboarding

Dynatrace provides a pre-configured dashboard that covers the following use-cases:

* Show namespaces with most / least free space
* Show namespaces with biggest growth rate
* Show top 10 list of the biggest PVCs
* Show capacity / usage per namespace

![Example PVC dashboard](https://dt-cdn.net/images/kubernetes-persistent-volume-claims-dashboard-1357-3d62f7e8b3.png)

## Limitations

This feature is available only if your Kubernetes cluster is [connected to a local Kubernetes API endpoint](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "Monitor the Kubernetes API using Dynatrace").

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")