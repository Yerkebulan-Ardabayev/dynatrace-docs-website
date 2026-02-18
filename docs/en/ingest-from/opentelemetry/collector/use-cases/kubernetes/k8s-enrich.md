---
title: Enrich OTLP requests with Kubernetes data
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich
scraped: 2026-02-18T05:54:25.230299
---

# Enrich OTLP requests with Kubernetes data

# Enrich OTLP requests with Kubernetes data

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Sep 24, 2025

The following configuration example shows how to configure a Collector instance to enrich OTLP telemetry data with additional Kubernetes metadata. This includes, for example, pod, deployment, and cluster details and allows Dynatrace to correctly map the provided telemetry data to the appropriate entities within Dynatrace.

Dynatrace recommends using ActiveGate to enhance status and performance monitoring of your Kubernetes cluster.
Deploying ActiveGate enables the Dynatrace Kubernetes application to visualize Kubernetes and OpenTelemetry data and map it to the corresponding Kubernetes entities.

## Prerequisites

* A deployed ActiveGate for Kubernetes API monitoring Optional
* One of the following Collector distributions with the [Kubernetes Attributesï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/k8sattributesprocessor) and [Transformï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) processors:

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The Collector deployed in [agent mode](/docs/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "How to deploy Dynatrace OTel Collector.")
* The [API URL](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") of your Dynatrace environment
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope
* [Kubernetes configured](#kubernetes-configuration) for the required role-based access control

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

Service account

In addition to the Collector configuration, be sure to also update your Kubernetes configuration to match the service account name used in the [RBAC file](#kubernetes-configuration) (see entries for [Helmï»¿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operatorï»¿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.144.0/docs/api.md#opentelemetrycollectorspec)).

```
extensions:



health_check:



endpoint: ${env:MY_POD_IP}:13133



receivers:



otlp:



protocols:



grpc:



endpoint: ${env:MY_POD_IP}:4317



http:



endpoint: ${env:MY_POD_IP}:4318



processors:



transform:



error_mode: ignore



trace_statements: &dynatrace_transformations



# Set attributes taken from k8s metadata.



- context: resource



statements:



- set(attributes["k8s.cluster.name"], "${env:CLUSTER_NAME}")



- set(attributes["k8s.workload.kind"], "job") where IsString(attributes["k8s.job.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.job.name"]) where IsString(attributes["k8s.job.name"])



- set(attributes["k8s.workload.kind"], "cronjob") where IsString(attributes["k8s.cronjob.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.cronjob.name"]) where IsString(attributes["k8s.cronjob.name"])



- set(attributes["k8s.workload.kind"], "daemonset") where IsString(attributes["k8s.daemonset.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.daemonset.name"]) where IsString(attributes["k8s.daemonset.name"])



- set(attributes["k8s.workload.kind"], "statefulset") where IsString(attributes["k8s.statefulset.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.statefulset.name"]) where IsString(attributes["k8s.statefulset.name"])



- set(attributes["k8s.workload.kind"], "replicaset") where IsString(attributes["k8s.replicaset.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.replicaset.name"]) where IsString(attributes["k8s.replicaset.name"])



- set(attributes["k8s.workload.kind"], "deployment") where IsString(attributes["k8s.deployment.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.deployment.name"]) where IsString(attributes["k8s.deployment.name"])



# remove the delete statements if you want to preserve these attributes



- delete_key(attributes, "k8s.deployment.name")



- delete_key(attributes, "k8s.replicaset.name")



- delete_key(attributes, "k8s.statefulset.name")



- delete_key(attributes, "k8s.daemonset.name")



- delete_key(attributes, "k8s.cronjob.name")



- delete_key(attributes, "k8s.job.name")



# Set attributes from metadata specified in Dynatrace and set through the Dynatrace Operator.



# For more info: https://docs.dynatrace.com/docs/shortlink/k8s-metadata-telemetry-enrichment



- context: resource



statements:



- merge_maps(attributes, ParseJSON(attributes["metadata.dynatrace.com"]), "upsert") where IsMatch(attributes["metadata.dynatrace.com"], "^\\{")



- delete_key(attributes, "metadata.dynatrace.com")



metric_statements: *dynatrace_transformations



log_statements: *dynatrace_transformations



k8sattributes:



extract:



metadata:



- k8s.pod.name



- k8s.pod.uid



- k8s.pod.ip



- k8s.deployment.name



- k8s.replicaset.name



- k8s.statefulset.name



- k8s.daemonset.name



- k8s.job.name



- k8s.cronjob.name



- k8s.namespace.name



- k8s.node.name



- k8s.cluster.uid



- k8s.container.name



annotations:



- from: pod



key_regex: metadata.dynatrace.com/(.*)



tag_name: $$1



- from: pod



key: metadata.dynatrace.com



tag_name: metadata.dynatrace.com



pod_association:



- sources:



- from: resource_attribute



name: k8s.pod.name



- from: resource_attribute



name: k8s.namespace.name



- sources:



- from: resource_attribute



name: k8s.pod.ip



- sources:



- from: resource_attribute



name: k8s.pod.uid



- sources:



- from: connection



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



extensions:



- health_check



pipelines:



traces:



receivers: [otlp]



processors: [k8sattributes, transform]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [k8sattributes, transform]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [k8sattributes, transform]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Kubernetes configuration

Configure the following `rbac.yaml` file with your Kubernetes instance, to allow the Collector to use the Kubernetes API with the service-account authentication type.

```
apiVersion: v1



kind: ServiceAccount



metadata:



labels:



app: collector



name: collector



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: collector



labels:



app: collector



rules:



- apiGroups:



- ''



resources:



- 'pods'



- 'namespaces'



verbs:



- 'get'



- 'watch'



- 'list'



- apiGroups:



- 'apps'



resources:



- 'replicasets'



verbs:



- 'get'



- 'list'



- 'watch'



- apiGroups:



- 'extensions'



resources:



- 'replicasets'



verbs:



- 'get'



- 'list'



- 'watch'



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRoleBinding



metadata:



name: collector



labels:



app: collector



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: ClusterRole



name: collector



subjects:



- kind: ServiceAccount



name: collector



namespace: default
```

## Components

For our configuration, we configured the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as an active receiver component for our Collector instance.

This is mainly for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Processors

Under `processors`, we specify the [`k8sattributes` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/k8sattributesprocessor) with the following parameters:

* `extract`âSpecifies which information should be extracted.
* `pod_association`âSpecifies how the pod information is linked to attributes.

Note that the `k8s.container.name` attribute will only be extracted if the pod from which the incoming
signal has been received contains only one container, or if the ingested signal contains the `k8s.container.id` resource attribute.
Otherwise, the k8sattributes processor will not be able to correctly associate the correct container.

Dynatrace Operator enriches OpenTelemetry data from Kubernetes pods with `metadata.dynatrace.com` annotations. When these annotations are present, the `k8sattributes` processor extracts them.

We also configure the [`transform` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) to have Kubernetes cluster information automatically added as resource attributes for all telemetry signals.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver, processor, and exporter objects into pipelines for traces, metrics, and logs. These pipelines allow us to send OpenTelemetry signals via the Collector instance and have them automatically enriched with additional Kubernetes-specific details.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")