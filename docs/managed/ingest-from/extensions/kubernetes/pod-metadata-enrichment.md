---
title: Monitored pod Kubernetes metadata enrichment
source: https://docs.dynatrace.com/managed/ingest-from/extensions/kubernetes/pod-metadata-enrichment
---

# Monitored pod Kubernetes metadata enrichment

# Monitored pod Kubernetes metadata enrichment

* Explanation
* 2-min read
* Published Aug 25, 2026

The Extension Execution Controller (EEC) automatically enriches signals from extensions running on Kubernetes—metrics, logs, and events—with Kubernetes pod metadata.

## How enrichment works

When an extension sends a signal, the `device.address` attribute identifies the monitored pod—the database or service pod the extension collects data from. The EEC resolves that pod from its local metadata cache and fills in the following attributes for the monitored pod's Kubernetes context, if not already set:

| Attribute | Description |
| --- | --- |
| `k8s.cluster.uid` | Unique identifier of the cluster |
| `k8s.cluster.name` | Name of the cluster |
| `k8s.namespace.name` | Namespace the monitored pod belongs to |
| `k8s.pod.name` | Name of the monitored pod |
| `k8s.pod.uid` | Unique identifier of the monitored pod |
| `k8s.node.name` | Node the monitored pod runs on |
| `k8s.container.name` | Name of the container within the monitored pod |
| `k8s.workload.kind` | Workload type, for example `Deployment` or `StatefulSet` |
| `k8s.workload.name` | Name of the workload managing the monitored pod |

## Enable pod tracking

For the EEC to resolve a monitored pod, label that pod with `extensions.dynatrace.com/metadata=true`. The EEC skips pods without this label and forwards their signals without Kubernetes metadata.

Apply the label to the pods your extensions monitor:

```
metadata:



labels:



extensions.dynatrace.com/metadata: "true"
```