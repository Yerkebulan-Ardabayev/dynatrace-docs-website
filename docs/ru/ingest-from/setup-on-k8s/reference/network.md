---
title: Network traffic
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/network
scraped: 2026-02-24T21:20:21.600034
---

# Network traffic

# Network traffic

* Latest Dynatrace
* 3-min read
* Updated on Jan 02, 2026

To ensure Dynatrace Operator components work correctly in a Kubernetes cluster, they need to be able to communicate with both the Dynatrace Cluster and the Kubernetes cluster.

Dynatrace Operator components are accessible through specific ports and access various resources inside and outside the Kubernetes cluster. For more details on which resources are accessed within the Kubernetes cluster, see the [Operator RBAC permissions](/docs/ingest-from/setup-on-k8s/reference/security "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") reference page.

## Ingress traffic

1

[Liveness probesï»¿](https://dt-url.net/dh03q2c) are used by Kubernetes to verify the container is running properly. If the request fails, the container will be restarted. [Readiness probesï»¿](https://dt-url.net/ml23qbl) are used by Kubernetes to verify the Pod is ready to accept traffic.

2

[Metrics endpointsï»¿](https://dt-url.net/t543q6q) emit additional metrics in Prometheus format.

No ingress traffic is accepted for EdgeConnect and OneAgent.

## Egress traffic

Dynatrace Operator components have to access both the Kubernetes cluster and resources outside the Cluster to function properly. All resources in the namespace of Dynatrace Operator, with the default namespace being `dynatrace`, need to be able to resolve DNS requests.

Depending on your setup, the default port may be different from `TCP 443`.

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