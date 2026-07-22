---
title: Configure metadata enrichment
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment
---

# Configure metadata enrichment

# Configure metadata enrichment

* How-to guide
* 3-min read
* Updated on Jun 25, 2026

Metadata enrichment attaches Kubernetes metadata—cluster, namespace, workload, pod, and container identifiers—to telemetry signals. The mechanism differs by mode:

* **OneAgent injection**: Dynatrace Operator writes metadata to the enrichment directory at `/var/lib/dynatrace/enrichment` and to the `metadata.dynatrace.com` pod annotation.
* **OTLP exporter injection**: Dynatrace Operator injects `OTEL_RESOURCE_ATTRIBUTES` environment variables and the `metadata.dynatrace.com` pod annotation.
* **Standalone `metadataEnrichment`**: Dynatrace Operator writes metadata to the enrichment directory at `/var/lib/dynatrace/enrichment` and the `metadata.dynatrace.com` pod annotation.

## Prerequisites

* Dynatrace Operator is installed and running in your Kubernetes cluster.
* A valid DynaKube is applied to your cluster.

## How to enable

1. Enable OneAgent injection

OneAgent injection automatically enables metadata enrichment. Configure it in your DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



oneAgent:



cloudNativeFullStack: {}
```

To verify, inspect any injected pod and look for the `metadata.dynatrace.com` annotation containing a JSON object with the enriched Kubernetes metadata:

```
kubectl get pod <pod-name> -n <namespace> -o yaml
```

2. Enable OTLP exporter injection

OTLP exporter injection automatically enables metadata enrichment for OTLP signals. Dynatrace Operator appends Kubernetes metadata to the `OTEL_RESOURCE_ATTRIBUTES` environment variable on injected pods and writes it to the `metadata.dynatrace.com` pod annotation.

Configure it in your DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



otlpExporterConfiguration:



signals:



metrics: {}



traces: {}



logs: {}
```

For full setup instructions and verification steps, see [Enable automatic OpenTelemetry OTLP exporter configuration](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.").

3. Enable standalone metadata enrichment

Dynatrace Operator writes Kubernetes metadata to enrichment directory files at `/var/lib/dynatrace/enrichment` and to the `metadata.dynatrace.com` pod annotation.

Use this when deploying with `classicFullStack`, standalone `logMonitoring`, `telemetryIngest`, or a Kubernetes monitoring ActiveGate.

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



metadataEnrichment:



enabled: true
```

To limit metadata enrichment to specific namespaces, add a `namespaceSelector`:

```
spec:



metadataEnrichment:



enabled: true



namespaceSelector:



matchLabels:



inject: metadata  # only namespaces with this label receive enrichment
```

Label the namespaces you want to include:

```
kubectl label namespace <namespace> inject=metadata
```

To verify, confirm the files appear in injected pods:

1. dt\_metadata.properties

```
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

For code examples on reading these files, see [Enrich ingested data with Dynatrace-specific dimensions](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").

## Set resource attributes in the DynaKube

Dynatrace Operator version 1.10.0+

You can define additional resource attributes in your DynaKube. Dynatrace Operator propagates these to telemetry signals without requiring namespace labels or pod annotations.

Three fields control where the attributes get injected:

* `.spec.resourceAttributes`—applied to all signals: OneAgent injection, OTLP exporter injection, standalone log monitoring, and ActiveGate.
* `.spec.oneAgent.<mode>.additionalResourceAttributes`—applied to OneAgent signals only. Takes precedence over duplicate keys in `.spec.resourceAttributes`.
* `.spec.otlpExporterConfiguration.additionalResourceAttributes`—applied to OTLP telemetry only. Takes precedence over duplicate keys in `.spec.resourceAttributes`.

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



resourceAttributes:



aws.account.id: 123456789012



oneAgent:



cloudNativeFullStack:



additionalResourceAttributes:



my.team: platform



namespaceSelector:



matchLabels:



my.app.com/oneagent: "true"



otlpExporterConfiguration:



additionalResourceAttributes:



my.team: platform



namespaceSelector:



matchLabels:



example.com/source: otel



signals:



metrics: {}



traces: {}



logs: {}
```

Dynatrace Operator propagates the merged attributes as follows:

* **OneAgent injection**: Dynatrace Operator writes attributes to `dt_node_metadata.properties` for OneAgents, and to `dt_metadata.properties`, `dt_metadata.json`, and the `metadata.dynatrace.com` pod annotation for injected pods.
* **OTLP exporter injection**: Dynatrace Operator appends attributes to `OTEL_RESOURCE_ATTRIBUTES` and the `metadata.dynatrace.com` pod annotation for injected pods.
* **Standalone log monitoring and ActiveGate**: Dynatrace Operator applies `.spec.resourceAttributes` directly. Mode-specific `additionalResourceAttributes` does not affect these components.

A soft limit of 10 attributes applies across `.spec.resourceAttributes` and `additionalResourceAttributes` combined—Dynatrace Operator logs a warning when you exceed this limit.

Conflicting keys with concurrent OneAgent and OTLP injection

When both OneAgent injection and OTLP exporter injection are active on the same pod, both write to the shared `metadata.dynatrace.com` JSON annotation. Having the same key defined in both sections will result in undefined behavior. You must use distinct keys across OneAgent and OTLP `additionalResourceAttributes` when both are active on the same pod to avoid unpredictable behavior.

### Attribute key sanitization

For pod injection use cases (OneAgent injection and OTLP exporter injection), Dynatrace Operator propagates attributes as Kubernetes pod annotations in the form `metadata.dynatrace.com/<key>`. Kubernetes annotation key suffixes must consist of valid DNS label characters, so Dynatrace Operator sanitizes attribute keys by replacing any invalid characters before writing them to annotations.

Dynatrace Operator validates attribute keys and reports the following:

* **Warning**: The key contains characters Dynatrace Operator replaces during sanitization - Dynatrace Operator renames the key but still writes the annotation.
* **Error**: The sanitized key is an empty string - Dynatrace Operator drops the key.
* **Error**: Two keys produce the same sanitized value - the result is a collision.
* **Error**: The sanitized key exceeds 63 characters - this violates the Kubernetes annotation name-segment limit for `metadata.dynatrace.com/<key>`.

For the full parameter reference, see the [DynaKube API reference](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

## Learn more

* [Enrich ingested data with Dynatrace-specific dimensions](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")