---
title: Configure enrichment directory
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment
scraped: 2026-02-17T21:24:53.915060
---

# Configure enrichment directory

# Configure enrichment directory

* Latest Dynatrace
* 2-min read
* Published Jul 28, 2023

Metadata enrichment is an optional feature that enhances monitoring signals by adding supplementary metadata.

## What you will learn

This guide explains how to configure and enable metadata enrichment in the Dynatrace Operator. By following this guide, you will be able to:

* Verify the correct application of enriched metadata for various use cases.
* Associate logs and metrics with specific entities like pods, processes, etc.

## Prerequisites

* Dynatrace Operator is installed and running in your Kubernetes cluster.
* A valid DynaKube is applied to your cluster.

## Steps

1. Enable metadata enrichment

To enable metadata enrichment, modify your DynaKube YAML:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



metadataEnrichment:



enabled: true
```

If using additional features like ActiveGate or OneAgent, your configuration may include:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



metadataEnrichment:



enabled: true



oneAgent:



cloudNativeFullStack: (or other mode)



...



activeGate:



capabilities:



- routing



...
```

2. Use namespace selector

Optional

To limit metadata enrichment to specific namespaces, add the `namespaceSelector` field to your configuration:

```
metadataEnrichment:



enabled: true



namespaceSelector:



matchLabels:



team: finance
```

This configuration applies metadata enrichment only to namespaces labeled with `team=finance`.

3. Verify enrichment directory

Confirm that the enrichment directory in injected Pods reflects the metadata attributes you've configured.

Enrichment files are stored in the following directory: `/var/lib/dynatrace/enrichment`

This directory holds the enrichment files `dt_metadata.json` and `dt_metadata.properties`

The files look like this:

1. dt\_metadata.properties

```
dt.entity.kubernetes_cluster=<kubernetes-cluster-id>



dt.kubernetes.cluster.id=<cluster-id>



dt.kubernetes.workload.kind=<workload-kind>



dt.kubernetes.workload.name=<workload-name>



k8s.cluster.name=<cluster-name>



k8s.cluster.uid=<cluster-uid>



k8s.container.name=<container-name>



k8s.namespace.name=<namespace-name>



k8s.node.name=<node-name>



k8s.pod.name=<pod-name>



k8s.pod.uid=<pod-uid>



k8s.workload.kind=<workload-kind>



k8s.workload.name=<workload-name>
```

2. dt\_metadata.json

```
{



"dt.entity.kubernetes_cluster": "<kubernetes-cluster-id>",



"dt.kubernetes.cluster.id": "<cluster-id>",



"dt.kubernetes.workload.kind": "<workload-kind>",



"dt.kubernetes.workload.name": "<workload-name>",



"k8s.cluster.name": "<cluster-name>",



"k8s.cluster.uid": "<cluster-uid>",



"k8s.container.name": "<container-name>",



"k8s.namespace.name": "<namespace-name>",



"k8s.node.name": "<node-name>",



"k8s.pod.name": "<pod-name>",



"k8s.pod.uid": "<pod-uid>",



"k8s.workload.kind": "<workload-kind>",



"k8s.workload.name": "<workload-name>"



}
```

**Please note:** The enrichment files will be used for various enrichments automatically, if there is OneAgent enabled. If there is no OneAgent enabled, the enrichment files and their content have to be used manually.

For more details, see [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

## Learn more

* [Dynatrace documentation: metadata enrichment files](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")

By following these steps, you can fully leverage metadata enrichment to enhance your Kubernetes monitoring and achieve better insights.