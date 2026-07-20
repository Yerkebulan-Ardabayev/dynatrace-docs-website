---
title: Ingest Kubernetes pod logs with the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-podlogs
---

# Ingest Kubernetes pod logs with the OTel Collector

# Ingest Kubernetes pod logs with the OTel Collector

* How-to guide
* 4-min read
* Updated on Apr 09, 2026

The following configuration example shows how you configure a Collector instance to fetch logs from all Kubernetes pods. It also shows how to enrich the logs with Kubernetes metadata in order to automatically link OpenTelemetry services to pods and attach the logs to the Kubernetes services and pods.

## Prerequisites

* A deployed ActiveGate for Kubernetes API monitoring
* One of the following Collector distributions with the [Filelog﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/receiver/filelogreceiver) receiver and the [Kubernetes Attributes﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/k8sattributesprocessor) processor:

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* the OTel Collector deployed on each node
* The [API URL](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") of your Dynatrace environment
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope
* [Kubernetes configured](#kubernetes-configuration) for the required role-based access control
* Kubernetes Secrets set up as shown in [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.")

See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

Kubernetes configuration

This sample configuration uses the same Kubernetes enrichment approach as the use case at [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.").

In addition to the Collector configuration, be sure to also update your Kubernetes configuration for the following components:

* **Service account**: Specify the same service account name used in the [RBAC file](#kubernetes-configuration) (see entries for [Helm﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operator﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.156.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))
* **Mounted volumes**: Specify the file system volumes where your Kubernetes host keeps the relevant log files (see entries for [Helm﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L241), [Operator﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.156.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))
* **Mount paths**: Specify the file system paths, to which the previously configured volumes should be mounted within the container (see entries for [Helm﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L244), [Operator﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.156.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))

```
receivers:



# configure the filelog receiver to access the pod logs



# from the mounted volumes



file_log:



include:



- /var/log/pods/*/*/*.log



include_file_name: false



include_file_path: true



start_at: end



operators:



- id: container-parser



type: container



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



pipelines:



logs:



receivers: [file_log]



processors: [k8sattributes,transform]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Kubernetes configuration

Configure the following `rbac.yaml` file with your Kubernetes instance, to allow the OTel Collector to use the Kubernetes API with the service-account authentication type.

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

Configuration for GKE Autopilot or AWS EKS

If you are running the Collector on GKE Autopilot or AWS EKS, you need the following adjustments in the configuration:

* **Deployment mode**: The Collector needs to be deployed as a DaemonSet to be able to access the pod log files on the host. For details on deploying the Collector as a DaemonSet, see [Deployment instructions](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.").
* **Volume mount**: Volume mounts to `/var/log/pods` are required to be read-only, otherwise the Collector will not be able to access the log files
  within that directory.

Below is an example configuration for a Collector DaemonSet with the required volume mounts for gathering the pod logs:

```
apiVersion: apps/v1



kind: DaemonSet



metadata:



name: dynatrace-otel-collector



spec:



selector:



matchLabels:



app.kubernetes.io/name: dynatrace-otel-collector



template:



metadata:



labels:



app.kubernetes.io/instance: dynatrace-otel-collector



app.kubernetes.io/name: dynatrace-otel-collector



spec:



serviceAccountName: collector



tolerations:



# these tolerations are to have the daemonset runnable on control plane nodes



# remove them if your control plane nodes should not run pods



- key: node-role.kubernetes.io/control-plane



operator: Exists



effect: NoSchedule



- key: node-role.kubernetes.io/master



operator: Exists



effect: NoSchedule



containers:



- args: ["--config", "/conf/otel-collector-config.yaml"]



env:



- name: MY_POD_IP



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: status.podIP



image: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0



name: otel-collector



resources:



limits:



memory: 512Mi



volumeMounts:



- name: dynatrace-otel-collector-config



mountPath: /conf



# read-only volumeMount for the directory containing the pod logs



- name: logs



mountPath: /var/log



readOnly: true



volumes:



- configMap:



name: dynatrace-otel-collector-config



items:



- key: otel-collector-config



path: otel-collector-config.yaml



name: dynatrace-otel-collector-config



# hostPath volume containing the pod logs of the respective node the Collector instance is running on



- hostPath:



path: /var/log



name: logs
```

## Components

For our configuration, we configured the following components.

### Receivers

Under `receivers`, we specify the `filelog` receiver as active receiver component for our Collector instance.

The Filelog receiver supports a number of [configuration parameters﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/receiver/filelogreceiver/README.md), which enable you to customize its behavior. For the example, we use the following:

* `include`—Specifies the path pattern of the files we want to ingest.
* `start_at`—Specifies if the receiver should read from the beginning of the file or, for the most recent entries only, the end.
* `operators`—Configures the [`container`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/stanza/docs/operators/container.md) operator, which automatically parses each log entry.

### Processors

Under `processors`, we specify the [`k8sattributes` processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/k8sattributesprocessor) with the following parameters:

* `extract`—Specifies which information should be extracted.
* `pod_association`—Specifies how the pod information is linked to attributes.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token, as set up and configured under [Kubernetes Secrets](#kubernetes-secrets).

### Service pipelines

Under `service`, we assemble our receiver, processor, and exporter objects into pipelines for traces, metrics, and logs. These pipelines allow us to send OpenTelemetry signals via the Collector instance and have them automatically enriched with additional Kubernetes-specific details.

## Related topics

* [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Ingest logs from files with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")