---
title: Monitor Kubernetes clusters with the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring
---

# Monitor Kubernetes clusters with the OTel Collector

# Monitor Kubernetes clusters with the OTel Collector

* How-to guide
* 5-min read
* Updated on Nov 20, 2025

The OTel Collector provides extensive support for Kubernetes cluster and workload monitoring. It supports various receivers to collect critical metrics about the Kubernetes cluster, nodes, and objects.

This use case explains how to set up your Collector to get full visibility into your Kubernetes clusters through [**Data Explorer**](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") or custom dashboards in Dashboards Classic.

Dynatrace Operator

Dynatrace recommends using the [Dynatrace Operator for Kubernetes monitoring](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes").
However, this use case is designed specifically for OpenTelemetry users who choose not to deploy the Dynatrace Operator.
Setting up the Collector as described below will make Kubernetes monitoring data available to be used in [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") and [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").

## Prerequisites

* One of the following Collector distributions with the [Kubernetes Cluster﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/k8sclusterreceiver), [Kubernetes Events﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/k8seventsreceiver), and [Kubelet Stats﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kubeletstatsreceiver) receivers:

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom-built OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* Collector deployment in [agent mode](/managed/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "How to deploy the Dynatrace OpenTelemetry Collector.") for node and cluster level telemetry
* The [API URL](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") of your Dynatrace environment
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope
* [Kubernetes configured](#kubernetes-configuration) for the required role-based access control

See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set these up with the configurations provided below.

## Demo configurations

### RBAC configuration

Configure the following `rbac.yaml` file with your Kubernetes instance, to allow the Collector to use the Kubernetes API with the service-account authentication type.

```
apiVersion: v1



kind: ServiceAccount



metadata:



labels:



app: otelcol-dt



name: otelcol-dt



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: otelcol-dt



labels:



app: otelcol-dt



rules:



- apiGroups:



- ""



resources:



- events



- namespaces



- namespaces/status



- nodes



- nodes/spec



- nodes/stats



- nodes/proxy



- persistentvolumes



- persistentvolumeclaims



- pods



- pods/status



- replicationcontrollers



- replicationcontrollers/status



- resourcequotas



- services



verbs:



- get



- list



- watch



- apiGroups:



- apps



resources:



- daemonsets



- deployments



- replicasets



- statefulsets



verbs:



- get



- list



- watch



- apiGroups:



- batch



resources:



- jobs



- cronjobs



verbs:



- get



- list



- watch



- apiGroups:



- autoscaling



resources:



- horizontalpodautoscalers



verbs:



- get



- list



- watch



- apiGroups:



- coordination.k8s.io



resources:



- leases



verbs:



- get



- list



- watch



- create



- update



- patch



- delete



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRoleBinding



metadata:



name: otelcol-dt



labels:



app: otelcol-dt



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: ClusterRole



name: otelcol-dt



subjects:



- kind: ServiceAccount



name: otelcol-dt



namespace: default
```

### Collector configuration

Service account

In addition to the Collector configuration, be sure to also update your Kubernetes configuration to match the service account name used in the [RBAC file](#kubernetes-configuration)
(see entries for [Helm﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.127.2/charts/opentelemetry-collector/values.yaml#L245-L252) and [Operator﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.154.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec)).

```
extensions:



health_check:



endpoint: 0.0.0.0:13133



k8s_leader_elector:



auth_type: "serviceAccount"



lease_name: k8smonitoring



lease_namespace: ${env:POD_NAMESPACE}



receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



k8s_events:



auth_type: "serviceAccount"



k8s_leader_elector: k8s_leader_elector



kubelet_stats:



auth_type: "serviceAccount"



collection_interval: 10s



node: '${env:K8S_NODE_NAME}'



extra_metadata_labels:



- k8s.volume.type



k8s_api_config:



auth_type: "serviceAccount"



endpoint: "https://${env:K8S_NODE_NAME}:10250"



insecure_skip_verify: true



metric_groups:



- node



- pod



- container



- volume



k8s_cluster:



auth_type: "serviceAccount"



collection_interval: 10s



k8s_leader_elector: k8s_leader_elector



allocatable_types_to_report:



- cpu



- memory



- pods



node_conditions_to_report:



- Ready



- MemoryPressure



- PIDPressure



- DiskPressure



- NetworkUnavailable



metrics:



k8s.node.condition:



enabled: true



k8s.pod.status_reason:



enabled: true



processors:



cumulativetodelta:



max_staleness: 25h



filter:



error_mode: ignore



metrics:



metric:



- 'IsMatch(name, "k8s.volume.*") and resource.attributes["k8s.volume.type"] == nil'



- 'resource.attributes["k8s.volume.type"] == "configMap"'



- 'resource.attributes["k8s.volume.type"] == "emptyDir"'



- 'resource.attributes["k8s.volume.type"] == "secret"'



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



- k8s_leader_elector



pipelines:



metrics/node:



receivers:



- kubelet_stats



processors:



- filter



- k8sattributes



- transform



- cumulativetodelta



exporters:



- otlp_http



metrics:



receivers:



- k8s_cluster



processors:



- k8sattributes



- transform



- cumulativetodelta



exporters:



- otlp_http



logs:



receivers:



- k8s_events



processors:



- transform



exporters:



- otlp_http



traces:



receivers:



- otlp



processors:



- k8sattributes



- transform



exporters:



- otlp_http
```

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

Cumulativetodelta processor recommendation

It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor) to a value higher than how often the Collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.

## Components

For our configuration, we configured the following components:

#### Receivers

Under `receivers`, we specify the following receivers as active receiver components for our deployment:

* [`otlp`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/receiver/otlpreceiver): To accept OTLP traces.
* [`k8sevents`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/k8seventsreceiver): To receive Kubernetes events from the Kubernetes API server. [1](#fn-1-1-def)
* [`k8s_cluster`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/k8sclusterreceiver): To receive cluster-level metrics and entity events from the Kubernetes API server.
* [`kubelet_stats`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kubeletstatsreceiver): To receive node-level metrics. This receiver requires the environment variable `K8S_NODE_NAME` to be set to `spec.nodeName` using the [Kubernetes Downward API﻿](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/) (see [example﻿](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)).

1

The `k8sevents` receiver is currently in alpha stage and may undergo significant changes. Despite its early stage of maturity, it has been included in the Dynatrace distribution of the Collector to support early adoption and experimentation. Be aware that stability, performance, and feature completeness are not guaranteed at this stage.

#### Processors

Under `processors`, we specify the following processors:

* [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor): To filter Kubernetes attributes.
* [`k8sattributes`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/k8sattributesprocessor): To extract and provide pod data.
* [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor): To transform Kubernetes metrics. This requires the environment variable `CLUSTER_NAME` to be set with the name of the cluster. Set the variable value to an arbitrary name that you want your cluster to show up with inside Dynatrace.
* [`cumulativetodelta`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor): To enable conversion of cumulative metrics.

#### Exporters

Under `exporters`, we specify the [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

#### Extensions

Under `extensions`, we specify the [`k8sleaderelector` extension﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/extension/k8sleaderelector) to choose the leader of the agent replicas, which is going to scrape and export cluster-level telemetry.
This ensures that only one collector instance scrapes the data at a time to avoid telemetry duplication.

#### Service pipelines

Under `service`, we assemble our receiver, processor, and exporter objects into pipelines for traces, metrics, and logs. These pipelines allow us to send OpenTelemetry signals via the Collector instance and have them automatically enriched with additional Kubernetes-specific details.

## Use Data Explorer

Data Explorer greatly enhances your abilities to query and visualize metrics.
For more information, see [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

## Use custom dashboards

To set up custom dashboards, see [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")