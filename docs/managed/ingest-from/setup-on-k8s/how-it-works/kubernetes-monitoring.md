---
title: Kubernetes platform monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/how-it-works/kubernetes-monitoring
scraped: 2026-05-12T11:54:01.558186
---

# Kubernetes platform monitoring

# Kubernetes platform monitoring

* 1-min read
* Published Oct 31, 2024

Kubernetes platform monitoring sets the foundation for understanding and troubleshooting your Kubernetes clusters. This setup does not include OneAgent or application-level monitoring by default, but it can be combined with other monitoring and injection approaches.

See the [`.spec.activeGate`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-ag "List the available parameters for setting up Dynatrace Operator on Kubernetes.") section of DynaKube for additional information.

## Capabilities

* Provides insights into the health and utilization of your Kubernetes clusters, including object relationships (topology)
* Uses the Kubernetes API and cAdvisor to get node- and container-level metrics and Kubernetes events
* Enables out-of-the-box alerting and anomaly detection for workloads, Pods, nodes, and clusters

## Deployed resources

### Dynatrace Operator components

The following components are deployed via Helm/Manifests as part of the core installation. For more information, go to their respective sections:

* [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Components of Dynatrace Operator") manages the automated rollout, configuration, and lifecycle of Dynatrace components in your Kubernetes environment.
* [Dynatrace Operator webhook](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Components of Dynatrace Operator") validates DynaKube definitions, converts definitions with older API versions, and injects configurations into Pods.

### Operator-managed components

The following component is deployed by applying a DynaKube with Kubernetes platform monitoring:

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") routes observability data to the Dynatrace cluster and monitors the Kubernetes API.

![k8s-monitoring](https://dt-cdn.net/images/screenshot-2024-01-31-at-3-22-25-pm-2348-59be4489a6.png)

k8s-monitoring