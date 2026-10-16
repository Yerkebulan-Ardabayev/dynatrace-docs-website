---
title: Configure metadata enrichment
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment
---

# Configure metadata enrichment

# Configure metadata enrichment

* How-to guide
* 3-min read
* Updated on Oct 02, 2026

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
kubectl get pod <pod-name> -n <namespace> -o jsonpath='{.metadata.annotations.metadata\.dynatrace\.com}'
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

For code examples on reading these files, see [Enrich ingested data with Dynatrace-specific dimensions](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Enrich telemetry you send directly to Dynatrace by reading host and Kubernetes resource attributes from the OneAgent and Dynatrace Operator enrichment files.").

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

This limit is about how many attributes you define in the DynaKube; a separate limit governs how many resource attributes Dynatrace stores on each entity—see [Resource attribute limits and excluded keys](/managed/ingest-from/dynatrace-oneagent/resource-attributes#ra-limits "Understand the resource attributes stored on Dynatrace Managed hosts, processes, and containers, including configuration, filtering, and storage limits.").

Conflicting keys with concurrent OneAgent and OTLP injection

When both OneAgent injection and OTLP exporter injection are active on the same pod, both write to the shared `metadata.dynatrace.com` JSON annotation. Having the same key defined in both sections will result in undefined behavior. You must use distinct keys across OneAgent and OTLP `additionalResourceAttributes` when both are active on the same pod to avoid unpredictable behavior.

### Attribute key sanitization

Before merging resource attributes into these targets, Dynatrace Operator sanitizes each key: it replaces any character outside `a-zA-Z0-9-_.` and strips leading or trailing non-alphanumeric characters.

Dynatrace Operator validates attribute keys and reports the following:

* **Warning**: The key contains characters Dynatrace Operator replaces during sanitization - Dynatrace Operator renames the key but still applies the attribute.
* **Error**: The sanitized key is an empty string - Dynatrace Operator drops the key.
* **Error**: Two keys produce the same sanitized value - the result is a collision.
* **Error**: The sanitized key exceeds 63 characters.

For the full parameter reference, see the [DynaKube API reference](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

Dynatrace Operator writes these attributes into each injected pod, so Dynatrace reports them for the monitored processes and containers there, not for the host. After they reach a process group or container group entity, you can also use them as rule conditions.

Fewer keys reach the entity than enrich your telemetry. Dynatrace stores keys that use the `primary_tags.` prefix, such as `primary_tags.team`. Dynatrace also stores recognized primary Grail fields that don't start with `dt.`, such as `aws.account.id`, `azure.subscription`, or `k8s.cluster.name`.

Keys that start with `dt.`, including `dt.host_group.id`, still enrich telemetry but are never stored as resource attributes on the entity. You can't match these keys in resource-attribute rules or the entity selector.

Any other key—`my.team` in the example above, for instance—still enriches the telemetry the pod sends, but isn't stored on the process or container entity, so you can't match it in a rule or filter by it in the entity selector. The same applies to the keys you set through pod, workload, and namespace annotations: write the attribute key after the annotation prefix, as in `metadata.dynatrace.com/primary_tags.team`. You can restrict a management zone to the entities that report a given attribute, and you can apply tags to them automatically—see [management-zone rules](/managed/manage/identity-access-management-classic/permission-management/management-zones/management-zone-rules#resource-attribute-conditions "Define management-zone rules to control access to monitored entities, logs, and metrics using entity conditions, dimensional data, and entity selectors.") and [automatically applied tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags#resource-attribute-conditions "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.").

## Learn more

* [Enrich ingested data with Dynatrace-specific dimensions](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Enrich telemetry you send directly to Dynatrace by reading host and Kubernetes resource attributes from the OneAgent and Dynatrace Operator enrichment files.")

* [Resource attributes](/managed/ingest-from/dynatrace-oneagent/resource-attributes "Understand the resource attributes stored on Dynatrace Managed hosts, processes, and containers, including configuration, filtering, and storage limits.")
* [Management-zone rules](/managed/manage/identity-access-management-classic/permission-management/management-zones/management-zone-rules#resource-attribute-conditions "Define management-zone rules to control access to monitored entities, logs, and metrics using entity conditions, dimensional data, and entity selectors.")
* [Define and apply tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags#resource-attribute-conditions "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.")