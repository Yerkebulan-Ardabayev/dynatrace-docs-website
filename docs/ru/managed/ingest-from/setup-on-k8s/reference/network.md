---
title: Network traffic
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/network
scraped: 2026-02-18T21:32:09.644994
---

# Network traffic

# Network traffic

* Latest Dynatrace
* 3-min read
* Updated on Jan 02, 2026

To ensure Dynatrace Operator components work correctly in a Kubernetes cluster, they need to be able to communicate with both the Dynatrace Cluster and the Kubernetes cluster.

Dynatrace Operator components are accessible through specific ports and access various resources inside and outside the Kubernetes cluster. For more details on which resources are accessed within the Kubernetes cluster, see the [Operator RBAC permissions](/docs/ingest-from/setup-on-k8s/reference/security "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") reference page.

## Ingress traffic

Source

Destination

Port

Note

kubelet

Dynatrace Operator `/healthz`

`TCP 10080`

Liveness probe [1](#fn-1-1-def)

Prometheus metrics scraper Optional

Dynatrace Operator `/metrics`

`TCP 8080`

Metrics address [2](#fn-1-2-def)

kubelet

Dynatrace Webhook `/healthz`

`TCP 10080`

Liveness/Readiness probe [1](#fn-1-1-def)

kube-apiserver

Dynatrace Webhook `/inject`, `/label-ns`, `/validate*`

`TCP 8443`

Dynamic Admission Controller

Prometheus metrics scraperOptional

Dynatrace Webhook `/metrics`

`TCP 8080`

Metrics address [2](#fn-1-2-def)

kubelet

Dynatrace Operator CSI driver `server` container `/healthz`

`TCP 9808`

Liveness probe [1](#fn-1-1-def)

kubelet

Dynatrace Operator CSI driver `provisioner` container `/healthz`

`TCP 10090`

Liveness probe [1](#fn-1-1-def)

Prometheus metrics scraper Optional

Dynatrace Operator CSI driver `server` container `/metrics`

`TCP 8080`

Metrics address [2](#fn-1-2-def)

Prometheus metrics scraper Optional

Dynatrace Operator CSI driver `provisioner` container `/metrics`

`TCP 8090`

Metrics address [2](#fn-1-2-def)

kubelet

ActiveGate `/rest/health`

`TCP 9999`

Readiness probe [1](#fn-1-1-def)

kubelet

Extension Execution Controller `/readyz`

`TCP 14599`

Readiness probe [1](#fn-1-1-def)

Application pods

ActiveGate `/*`

`TCP 9999`

Default `HTTPS` port

Application pods

ActiveGate `/*`

`TCP 9998`

Default `HTTP` port, Data ingest, API access

Application pods

Dynatrace Collector

[Telemetry ingest ports](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest#port-list "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.")

[Ingest telemetry data](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.")

kubelet

SQL Extension Executor container `/health/live`

`TCP 8080`

Liveness probe [1](#fn-1-1-def)

kubelet

SQL Extension Executor container `/health/ready`

`TCP 8080`

Readiness probe [1](#fn-1-1-def)

1

[Liveness probesï»¿](https://dt-url.net/dh03q2c) are used by Kubernetes to verify the container is running properly. If the request fails, the container will be restarted. [Readiness probesï»¿](https://dt-url.net/ml23qbl) are used by Kubernetes to verify the Pod is ready to accept traffic.

2

[Metrics endpointsï»¿](https://dt-url.net/t543q6q) emit additional metrics in Prometheus format.

No ingress traffic is accepted for EdgeConnect and OneAgent.

## Egress traffic

Dynatrace Operator components have to access both the Kubernetes cluster and resources outside the Cluster to function properly. All resources in the namespace of Dynatrace Operator, with the default namespace being `dynatrace`, need to be able to resolve DNS requests.

Depending on your setup, the default port may be different from `TCP 443`.

Source

Destination

Port

Note

* Dynatrace Operator
* Dynatrace Webhook
* Dynatrace Operator CSI driver
* ActiveGate
* Extension Execution Controller

kube-dns

`TCP 53`, `UDP 53` [1](#fn-2-1-def)

Host name resolution for service discovery

Dynatrace Operator

Dynatrace server

`TCP 443` [1](#fn-2-1-def)

Server-side configuration [2](#fn-2-2-def)

Dynatrace Operator

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

Lifecycle management of components

Dynatrace Webhook

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

Mutating/Validating/Conversion requests

Dynatrace Operator CSI driver

Dynatrace server

`TCP 443` [1](#fn-2-1-def)

Default location for code module binaries [2](#fn-2-2-def)

Dynatrace Operator CSI driver

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

CSI volume handling

Dynatrace Operator CSI driver

private registry

`TCP 443` [1](#fn-2-1-def)

Optional Communication with private registry to access code modules [3](#fn-2-3-def)

ActiveGate

Communication endpoints [4](#fn-2-4-def)

`TCP 443`, `TCP 9999` [1](#fn-2-1-def)

Observability information [2](#fn-2-2-def)

ActiveGate

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

Collect resources

ActiveGate

Application Pods

Prometheus Exporter port [1](#fn-2-1-def)

Collect metrics

OneAgent

Communication endpoints [4](#fn-2-4-def)

`TCP 443`, `TCP 9999` [1](#fn-2-1-def)

Observability information [2](#fn-2-2-def)

EdgeConnect

Dynatrace server

`TCP 443` [1](#fn-2-1-def)

Server-side configuration [2](#fn-2-2-def)

EdgeConnect

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

Optional Workflow interactions [5](#fn-2-5-def)

Extension Execution Controller

ActiveGate

`TCP 443` [1](#fn-2-1-def)

Extension configuration and telemetry data [2](#fn-2-2-def)

1

Depending on your setup, the port may differ from the default.

2

Communication with hosts must be allowed as configured in [DynaKube](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") (`apiUrl`) or [EdgeConnect](/docs/ingest-from/setup-on-k8s/reference/edgeconnect-parameters "List of configuration parameters for EdgeConnect.") (`apiServer`) custom resources. Different communication endpoints may be used as fallback to ensure proper connection.

3

Only required when `codeModulesImage` field is used.

4

[Supported connectivity schemes for ActiveGates](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.")

5

Only required when Kubernetes Automation is enabled.