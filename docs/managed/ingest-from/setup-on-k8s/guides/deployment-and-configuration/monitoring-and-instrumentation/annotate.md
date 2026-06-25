---
title: Configure monitoring for namespaces and pods
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate
scraped: 2026-05-12T11:37:42.018570
---

# Configure monitoring for namespaces and pods

# Configure monitoring for namespaces and pods

* 5-min read
* Updated on Mar 19, 2026

cloudNativeFullStack

applicationMonitoring

metadataEnrichment

As part of monitoring your Kubernetes cluster with cloud-native full-stack or application monitoring, when applying metadata enrichment or automatically configuring your OTLP exporters, you might want to restrict it to certain namespaces and pods.

By default, Dynatrace Operator injects into **all namespaces**, except for:

* Namespaces prefixed with `kube-` or `openshift-`.
* The namespace where Dynatrace Operator was installed.

We highly recommend using the `namespaceSelector` fields (see below) to keep full control over what is injected.

## Monitor specific namespaces

When configuring Dynatrace Operator to inject OneAgent, to apply metadata enrichment or automatically configure OTLP exporters only in certain namespaces, set the `namespaceSelector` parameter in the DynaKube custom resource.

The `namespaceSelector` and annotations described here only affect the injection done by the webhook part of Dynatrace Operator. They don't affect the Kubernetes API monitoring capabilities of ActiveGate or the host-level monitoring done by OneAgent.

For more information, see [DynaKube parameters for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") (`.spec.metadataEnrichment`, `.spec.oneAgent.cloudNativeFullStack`, `.spec.oneAgent.applicationMonitoring`, and `.spec.otlpExporterConfiguration` fields).

1. Label your namespaces.

Kubernetes

OpenShift

```
kubectl label namespace <my_namespace> dt-monitoring=true
```

```
oc label namespace <my_namespace> dt-monitoring=true
```

2. Modify your DynaKube by adding the `namespaceSelector` to specify the label for monitoring.

Metadata enrichment

Cloud-native full-stack monitoring

Application monitoring

OTLP exporter configuration

```
spec:



metadataEnrichment:



namespaceSelector:



matchLabels:



dt-monitoring: "true"
```

```
spec:



oneAgent:



cloudNativeFullStack:



namespaceSelector:



matchLabels:



dt-monitoring: "true"
```

```
spec:



oneAgent:



applicationMonitoring:



namespaceSelector:



matchLabels:



dt-monitoring: "true"
```

```
spec:



otlpExporterConfiguration:



namespaceSelector:



matchLabels:



dt-monitoring: "true"
```

For more details about configuring labels for selective monitoring, see [Labels and selectorsï»¿](https://dt-url.net/vj038vk).

To add exceptions for specific pods within the selected namespaces, you can [annotate the respective pods](#podexclusion).

## Exclude specific namespaces

To exclude certain namespaces from being monitored, modify the DynaKube custom resource as follows.

* `key` defines the key of the label. Starting with Kubernetes version 1.22, a default label `kubernetes.io/metadata.name` is added to namespaces.
* `values` define the value of the label.

```
...



namespaceSelector:



matchExpressions:



- key: LabelKey



operator: NotIn



values:



- LabelValue
```

Example with Kubernetes default label

If you run `kubectl describe namespace dynatrace`, you'll see:

```
metadata:



name: dynatrace



labels:



kubernetes.io/metadata.name=dynatrace
```

A valid selector example to exclude `dynatrace` would be:

```
...



namespaceSelector:



matchExpressions:



- key: kubernetes.io/metadata.name



operator: NotIn



values:



- dynatrace
```

The webhook will inject every namespace that matches all `namespaceselector`.

For more details, see [Resources that support set-based requirementsï»¿](https://dt-url.net/hi03yvm).

## Exclude specific pods in monitored namespaces

To exclude specific pods within monitored namespaces, annotate the pods accordingly.

```
...



metadata:



annotations:



...



oneagent.dynatrace.com/inject: "false"
```

Annotations available for fine-grained control include.

* `dynatrace.com/inject`: Disables all injection when set to `false`. However, setting it to `true` will have no effect; the annotation can only be used to exclude pods from injection.
* `metadata-enrichment.dynatrace.com/inject`: Prevents [metric enrichment file](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") addition when `false`.
* `oneagent.dynatrace.com/inject`: Disables OneAgent modifications when set to `false`.
* `otlp-exporter-configuration.dynatrace.com/inject`: Disables [OTLP exporter auto-configuration](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.") when set to `false`.

## Exclude specific containers in monitored pods

Dynatrace Operator version 1.0.0+

To exclude specific container images within monitored namespaces, annotate the pods or DynaKube accordingly (this can be useful to, for example, exclude sidecar containers).

```
...



metadata:



annotations:



...



container.inject.dynatrace.com/<container-name>: "false"
```

This annotation can be applied at the **DynaKube level (affecting all pods)** or at the **individual pod level (affecting only the specified pod)**.

This excludes the container from all types of injection (OneAgent/metadata)

## Monitor only specific pods

Dynatrace Operator version 0.8.0+

Dynatrace Operator can be set to monitor namespaces without injecting into any pods, so you can choose which pods to monitor.

1. Disable the automatic injection feature for the DynaKube deployment to your cluster.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/automatic-injection: "false"



   spec:



   oneAgent:



   cloudNativeFullStack:



   namespaceSelector:



   matchLabels:



   dt-monitoring: "true"



   ...
   ```
2. Use label selectors or manual annotations on the namespaces you want to monitor selectively.

   ```
   kubectl label namespace <my_namespace> dt-monitoring=true
   ```
3. Annotate the pods you intend to monitor.

   * Works with `oneagent.dynatrace.com/inject`, `metadata-enrichment.dynatrace.com/inject`, and `otlp-exporter-configuration.dynatrace.com/inject` annotation.

   ```
   ...



   metadata:



   annotations:



   ...



   oneagent.dynatrace.com/inject: "true"
   ```

## Fine-tuning of injection for `applicationMonitoring` without CSI driver

This section has been deprecated with Dynatrace Operator version 1.5.0 and superseded by the new [node image pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") feature.

* `oneagent.dynatrace.com/flavor`: Set to `default` or `musl` to specify the binary compatibility. This indicates whether `glibc` or `musl` binaries should be downloaded, with `glibc` as the default setting. For containers based on `musl` (for example, Alpine), specify this annotation to ensure proper monitoring.

  + Ignored if the CSI volume is or the [node image pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") feature is used.
* `oneagent.dynatrace.com/technologies`: A comma-separated list of technologies. This filters the code modules to be downloaded, defaulting to `all`. Use this to tailor the OneAgent to monitor specific technologies within your application.

  + Ignored if the CSI volume is used.
* `oneagent.dynatrace.com/install-path`: Specifies the path where the OneAgent directory will be mounted. By default, it is set to `/opt/dynatrace/oneagent-paas`. Adjust this path based on your environment or requirements.

Below is an example showcasing how to apply these annotations within your deployment.

```
...



metadata:



annotations:



oneagent.dynatrace.com/technologies: "java,nginx"



oneagent.dynatrace.com/flavor: "musl"



oneagent.dynatrace.com/install-path: "/dynatrace"
```