---
title: Metadata enrichment of all telemetry originating from Kubernetes
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment
scraped: 2026-02-19T21:17:59.376210
---

# Metadata enrichment of all telemetry originating from Kubernetes

# Metadata enrichment of all telemetry originating from Kubernetes

* Latest Dynatrace
* 7-min read
* Updated on Feb 05, 2026

## Prerequisites

* Dynatrace Operator is installed and running in your Kubernetes cluster.
* A valid DynaKube is applied to your cluster.
* [Metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") is enabled.

## Use cases

* Enhance your metrics, logs, trace data, events and entities with additional information using Kubernetes namespace annotations and labels.
* Enhance your metrics, logs, trace data, events and entities with additional information using OpenTelemetry environment variables
* Enriched data can be used for [defining access control to users](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context"), or for solving [Cost Allocation](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.") in DPS.
* Enriched data can be used for pipeline routing, bucket segmentation, segmentation, and filtering.

## Security context and Cost Allocation

In Dynatrace, you can set up [policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") for fine-grained restrictions on the data level. By default, you can use `k8s.namespace.name` and `k8s.cluster.name`, but sometimes this is not enough and you need a more fine grained way to set up your boundaries.

You might already have defined such boundaries for yourself and defined them as Kubernetes labels or annotations. This feature enables you to use these at the source for your [security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context") in Dynatrace. If you have not done so already, we recommend to either use cluster or namespace name or set up a dedicated annotation for your Kubernetes workloads that serves as your security context.

Similarly Dynatrace provides a solution for [Cost Allocation](/docs/license/cost-allocation#assign-cost-centers-and-products-in-kubernetes-application-monitoring-deployments "Learn how to allocate costs to cost centers and products.") in DPS. You might already have the necessary data like department and product available in your existing Kubernetes labels or annotations. Even if not you might find it very convenient to setup up Cost Allocation as a Kubernetes annotation or label, which is what Dynatrace recommends. This feature then enables you to use these labels and annotations as the means to solving [Cost Allocation](/docs/license/cost-allocation#assign-cost-centers-and-products-in-kubernetes-application-monitoring-deployments "Learn how to allocate costs to cost centers and products.") in DPS.

The following attributes are supported:

* [`dt.security_context`](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")
* [`dt.cost.costcenter`](/docs/semantic-dictionary/fields#dynatrace "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.")
* [`dt.cost.product`](/docs/semantic-dictionary/fields#dynatrace "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.")

## Domain tags

To streamline tasks like bucket selection, segmentation, filtering, and problem routing, Dynatrace allows you to enrich your telemetry data using existing Kubernetes namespace labels or annotations. These tags are made available as domain-specific fields, such as `k8s.namespace.label.your_key` or `k8s.namespace.annotation.your_key`.

## Which data will be enriched

Data

Domain tags

Security Context

Cost Allocation

OneAgent metrics

JMX/PMI metrics collected via OneAgent

Planned

Service metrics

Kubernetes platform metrics

ActiveGate 1.331

Prometheus metrics

Planned

Planned - ActiveGate 1.333

Planned - ActiveGate 1.333

OTLP metrics

ActiveGate 1.331

Metrics collected by OpenTelemetry Collector

Logs collected by OpenTelemetry Collector

Logs collected by OneAgent log module

Logs collected by FluentBit

Smartscape Kubernetes entities

ActiveGate 1.331

Service metrics

OneAgent events

Kubernetes events

ActiveGate 1.331

## Enrichment options

Depending on the specific use case, the following enrichment options are supported:

### Use settings to use existing namespace labels and annotations (recommended)

We recommend this option, as it is the only option that enriches all signals, including Kubernetes platform metrics, events, and entitiesâunlike environment variables or manual pod annotations. Use Kubernetes enrichment rules to leverage your existing namespace labels and annotations.
The tenant configuration is applied to all Kubernetes clusters by default. However, you can override it for specific clusters if needed.

Hint: If you setup your rules before you deploy your Dynakube, you don't need to wait 45 minutes for the rules to be propagated.

1. Go to **Kubernetes App** > **Namespace** > Select your namespace to have an overview of your existing namespace labels.

   ![Namespace details opened in the K8s App, pointing to the current namespace labels](https://dt-cdn.net/images/namespace-labels-1997-2a0370e1ef.png)
2. Go to **Settings** > **Cloud and virtualization** > **Kubernetes Telemetry Enrichment**.
3. Select **Add rule**.
4. Select `Annotation` or `Label` in the **Metadata type** dropdown.
5. Enter the namespace annotation/label key in the **Source** field, following [Kubernetes conventionsï»¿](https://dt-url.net/2c02sbn):
6. To use the key of the annotation or label as field name, turn on **Enrich telemetry with label/annotation directly**.

   ![Enrich telemetry with label/annotation directly](https://dt-cdn.net/images/enrich-telemetry-with-label-annotation-directly-693-b6d33d539e.png)
7. For remapping, turn off **Enrich telemetry with label/annotation directly** and choose a value from the **Target** dropdown.

   ![Enrichment Settings for Remapping](https://dt-cdn.net/images/enrichment-settings-for-remapping-663-33a85e6613.png)
8. Select **Save changes**.
9. After creating or modifying rules, allow up to 45 minutes for the changes to take effect. Once this time has passed, restart your pods.
10. Navigate to your data and verify that the metadata is successfully enriched.

![Log details with enriched metadata](https://dt-cdn.net/images/enriched-log-652-55590251f6.png)

### Use dedicated Dynatrace metadata pod annotations

This works automatically for OneAgent and OpenTelemetry code-change scenarios.

This option is intended for scenarios where namespace labels or annotations cannot be used as a source. If both methods are present, manual annotations take precedence.

Unlike the settings-based approach, manually added pod annotations do not provide full enrichment. They will not enrich Kubernetes metrics, Kubernetes events, or entities.
For Oneagent metrics and service metrics to be enriched with these attributes, they must follow the convention `k8s.namespace.<label>/<annotation>.<key>: <value>`.

For comprehensive enrichment, the settings-based approach is recommended.

You might create the following annotations at the pod level:

```
metadata:



annotations:



metadata.dynatrace.com/dt.security_context: sre



metadata.dynatrace.com/dt.cost.costcenter: it_services



metadata.dynatrace.com/dt.cost.product: fin_app



metadata.dynatrace.com/k8s.namespace.label.domain: finance
```

The following attributes will enrich the data:

```
dt.security_context: sre



dt.cost.costcenter: it_services



dt.cost.product: fin_app



k8s.namespace.label.domain: finance
```

## OpenTelemetry setup

For OTLP setups without OneAgent, additional steps for signal enrichment are required. This can be achieved either by modifying your code to parse metadata files provided by the operator or by using environment variables.

### Enable automatic OpenTelemetry OTLP exporter configuration (recommended)

[Automatic OpenTelemetry OTLP exporter configuration](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.") is the recommended option for OTLP setups without OneAgent injection, as it provides enrichment comparable to the OneAgent case. Enable it in your DynaKube to automatically enrich your telemetry with Dynatrace metadata. This feature is available for all OpenTelemetry supported languages.

### Enrich via code changes

This option is suitable for standalone OTLP setups without OneAgent injection. For optimal results, enrich your OTLP telemetry by parsing Dynatrace metadata files and adding the metadata directly in your code, as outlined in [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions."). You can find code samples in our OpenTelemetry section, like here for [Java](/docs/ingest-from/opentelemetry/walkthroughs/java/java-manual#add-telemetry-signals-manually "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.").
This approach provides enrichment comparable to the OneAgent case.

### Enrich via environment variable

If modifying your code isn't feasible, you can use the [`OTEL_RESOURCE_ATTRIBUTES`ï»¿](https://dt-url.net/ne03unx) environment variable for enrichment. However, this method has limitations: configuration can be complex, and certain properties, like k8s.container.name and tags, must be set as static strings.

1. Create a config map for cluster level attributes

1. Store DynaKube name

```
DYNAKUBE="dynakube" # set this to the name of your DynaKube / kubectl get dynakube -n dynatrace
```

2. Get `k8s.cluster.uid`

```
K8S_CLUSTER_UID="$(kubectl get dynakube -o jsonpath='{.status.kubeSystemUUID}' -n dynatrace $DYNAKUBE)"
```

3. Get `k8s.cluster.name`

```
K8S_CLUSTER_NAME="$(kubectl get dynakube -o jsonpath='{.status.kubernetesClusterName}' -n dynatrace $DYNAKUBE)"
```

4. Get Kubernetes entity `dt.entity.kubernetes_cluster`

```
DT_ENTITY_KUBERNETES_CLUSTER="$(kubectl get dynakube -o jsonpath='{.status.kubernetesClusterMEID}' -n dynatrace $DYNAKUBE)"
```

5. Create config map in the target namespace

```
kubectl create configmap dynatrace-metadata \



--from-literal K8S_CLUSTER_UID=$K8S_CLUSTER_UID \



--from-literal K8S_CLUSTER_NAME=$K8S_CLUSTER_NAME \



--from-literal DT_ENTITY_KUBERNETES_CLUSTER=$DT_ENTITY_KUBERNETES_CLUSTER \



--namespace <YOUR_NAMESPACE>
```

2. Set K8s attributes via downward API on Pod

Adapt your Kubernetes pod specification by adding the following environment variables. You can include these in your Kubernetes Deployment or Pod manifest.

Tags and `k8s.container.name` cannot be set via downward API.
It needs to be provided as a static string.

```
envFrom:



- configMapRef:



name: dynatrace-metadata



optional: false



env:



- name: K8S_CONTAINER_NAME



value: "" # replace with actual container name



- name: K8S_POD_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.name



- name: K8S_POD_UID



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.uid



- name: K8S_POD_NAMESPACE



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.namespace



- name: K8S_WORKLOAD_KIND



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/k8s.workload.kind'] # only works when metadata enrichment is enabled



- name: K8S_WORKLOAD_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/k8s.workload.name'] # only works when metadata enrichment is enabled



- name: K8S_NODE_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: spec.nodeName



- name: DT_SECURITY_CONTEXT # only works when automatic security context enrichment is configured



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/dt.security_context']



- name: DT_COST_PRODUCT # only works when automatic cost product enrichment is configured



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/dt.cost.product']



- name: DT_COST_COSTCENTER # only works when automatic cost center enrichment is configured



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/dt.cost.costcenter']
```

3. Add attributes to `OTEL_RESOURCE_ATTRIBUTES`

This example shows all our recommended attributes. Remove attributes that are not in use.

```
- name: OTEL_RESOURCE_ATTRIBUTES



value: k8s.cluster.name=$(K8S_CLUSTER_NAME),k8s.cluster.uid=$(K8S_CLUSTER_UID),k8s.node.name=$(K8S_NODE_NAME),k8s.workload.name=$(K8S_WORKLOAD_NAME),k8s.workload.kind=$(K8S_WORKLOAD_KIND),k8s.pod.name=$(K8S_POD_NAME),k8s.pod.uid=$(K8S_POD_UID),k8s.namespace.name=$(K8S_POD_NAMESPACE),k8s.container.name=$(K8S_CONTAINER_NAME),dt.entity.kubernetes_cluster=$(DT_ENTITY_KUBERNETES_CLUSTER),dt.security_context=$(DT_SECURITY_CONTEXT),dt.cost.costcenter=$(DT_COST_COSTCENTER),dt.cost.product=$(DT_COST_PRODUCT)
```

To learn how to enrich signals with release metadata using the `OTEL_RESOURCE_ATTRIBUTES` environment variable, refer to the [version detection strategies](/docs/deliver/release-monitoring/version-detection-strategies#otel_resource_attributes "Metadata for version detection in different technologies") for detailed guidance.

## Limitations

* Limit of 20 rules per configuration scope.
* After creating or modifying rules, allow up to 45 minutes for the changes to take effect. Once this time has passed, restart your pods.
* Manually set `metadata.dynatrace.com` pod annotations take precedence.
* Manually added attributes (anything other than `dt.security_context`, `dt.cost.costcenter`, or `dt.cost.product`) do not enrich any Kubernetes metrics or Kubernetes events.
* The settings-based approach does not work in conjunction with manually applied dedicated pod annotations. Using both simultaneously may cause conflicts, leading to unexpected behavior.

## Troubleshooting

### Verify the rule definition

* Confirm that each rule points to the correct **metadata type** (`label` vs. `annotation`).
* Ensure the **source key** in the rule exactly matches the key that exists on the namespace.

### Check that the source metadata really exists

* Open the namespace in the **Dynatrace Kubernetes app** and look for the expected labels/annotations.
* Alternatively, run

  ```
  kubectl get namespace <name> -o yaml
  ```

and inspect the `metadata.labels` and `metadata.annotations` sections.

### Validate that metadata enrichment is turned on

* The feature works only if `metadataEnrichment` is enabled in your **DynaKube** configuration.
* If you specify a `namespaceSelector` in the DynaKube, make sure it matches the namespace you are testing.

### Confirm that enrichment reached the pods

* Inspect any pod in the namespace:

  ```
  kubectl get pod <pod-name> -o yaml
  ```
* Look for annotations that start with `metadata.dynatrace.com/â¦`. Their presence means the metadata is enriched.

## Examples

Rules

Rules in `builtin:kubernetes.generic.metadata.enrichment`

```
"rules":



[



{



# rule #1



"type": "Annotation",



"source": "metadata.example.com/team",



"target": "dt.security_context"



},



{



# rule #2



"type": "Label",



"source": "department",



"target": "dt.cost.costcenter"



},



{



# rule #3



"type": "Label",



"source": "app/name",



"target": "dt.cost.product"



}



{



# rule #4



"type": "Label",



"source": "domain",



"primaryGrailTag": "true"



}



]
```

Namespace

Your existing namespace labels and annotations:

```
metadata:



annotations:



metadata.example.com/team: sre



labels:



department: it_services



app/name: fin_app



domain: finance
```

Pod

The Operator will create pod annotations:

```
metadata:



annotations:



metadata.dynatrace.com:|



{



"dt.security_context": "sre",



"dt.cost.costcenter": "it_services",



"dt.cost.product": "fin_app",



"k8s.namespace.label.domain": "finance"



}
```

Telemetry

The following attributes will be enriched on the data:

```
dt.security_context: sre



dt.cost.costcenter: it_services



dt.cost.product: fin_app



k8s.namespace.label.domain: finance
```

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Configure enrichment directory](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.")