---
title: ClusterRole aggregation for Kubernetes monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation
scraped: 2026-02-21T21:24:21.209960
---

# ClusterRole aggregation for Kubernetes monitoring

# ClusterRole aggregation for Kubernetes monitoring

* Latest Dynatrace
* 2-min read
* Updated on Dec 09, 2025

Dynatrace Operator version 1.8.0+

Starting with Operator version 1.8.0, the ActiveGate component uses a service account binding the `dynatrace-kubernetes-monitoring` ClusterRole. This ClusterRole is an **aggregated role** enabling simple and flexible configuration of assigned RBAC permissions. [1](#fn-1-1-def)

1

ClusterRole aggregation is a Kubernetes RBAC feature that allows you to combine multiple ClusterRoles into a single aggregated ClusterRole. The aggregating ClusterRole uses label selectors to identify which other ClusterRoles should be included. For more information, see [ClusterRole aggregation in Kubernetes documentationï»¿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles).

## Default permissions

By default, the Dynatrace Operator installation creates a `dynatrace-kubernetes-monitoring-default` ClusterRole that contains the standard set of permissions required for Kubernetes platform monitoring. This ClusterRole is automatically labeled with `rbac.dynatrace.com/aggregate-to-monitoring: "true"`, so its permissions are included in the aggregated role.

The default permissions are documented in the [security reference](/docs/ingest-from/setup-on-k8s/reference/security#activegate "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") and cover standard monitoring of:

* Pods, deployments, StatefulSets, and other workload resources.
* Services and endpoints.
* Nodes and resource metrics.
* Events and cluster information.

## Extending the ClusterRole with additional permissions

To extend the monitoring functionality beyond the default permissions, create additional ClusterRoles with the aggregation label. Any ClusterRole with the label `rbac.dynatrace.com/aggregate-to-monitoring: "true"` is automatically aggregated, and its permissions are granted to the ActiveGate service account.

### Example: Allow monitoring of sensitive data

To enable monitoring of sensitive Kubernetes objects like Secrets and ConfigMaps, create a new ClusterRole:

```
apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: dynatrace-kubernetes-monitoring-sensitive



labels:



rbac.dynatrace.com/aggregate-to-monitoring: "true"



rules:



- apiGroups:



- ""



resources:



- configmaps



- secrets



verbs:



- list



- watch



- get
```

The `rbac.dynatrace.com/aggregate-to-monitoring: "true"` label is required for your ClusterRole to be aggregated. Without this label, the permissions are not granted to the ActiveGate.

The permissions are aggregated immediately after applying the ClusterRole and take effect without requiring a restart of Operator or ActiveGate pods.