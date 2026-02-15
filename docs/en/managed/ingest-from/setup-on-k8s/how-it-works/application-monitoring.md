---
title: Application observability
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/how-it-works/application-monitoring
scraped: 2026-02-15T21:20:37.272243
---

# Application observability

# Application observability

* Latest Dynatrace
* 3-min read
* Published Oct 31, 2024

Application observability focuses on monitoring application-level metrics by injecting code modules into application Pods. This mode offers multiple injection strategies (automatic, runtime, and build-time) to collect application-specific metrics. For infrastructure-level insights, combine it with [Kubernetes platform monitoring](/docs/ingest-from/setup-on-k8s/how-it-works/kubernetes-monitoring "In-depth description of Kubernetes platform monitoring using Dynatrace Operator.").

See [`.spec.oneAgent.applicationMonitoring`](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") section of DynaKube for additional information.

## Automatic injection

You can use the automatic injection strategy for application Pods. Dynatrace injects code modules into Pods using the Kubernetes admission controller. This approach allows you to collect application-specific metrics and monitor container-level metrics.

### Capabilities

* Dynatrace injects code modules into Pods using the Kubernetes admission controller.
* Get granular control over the instrumented Pods using namespaces and annotations.
* Route Pod metrics to different Dynatrace environments within the same Kubernetes cluster.
* [Enable data enrichment for Kubernetes environments](/docs/ingest-from/extend-dynatrace/extend-data#dynatrace-kubernetes-operator "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

### Current limitations

* Diagnostic files (support archives) for application Pods aren't yet supported.
* [Go static monitoring](/docs/ingest-from/technology-support/application-software/go/support/go-known-limitations#static-monitoring "Learn the limitations for Go support and their workarounds.") is partially supported.

When deployed in application monitoring, Dynatrace code modules monitor processes within the container, including disk, CPU, and networking metrics. Host metrics are not monitored. Without [Kubernetes Platform Monitoring](#kubernetes-monitoring), topology is limited to Pods and containers.

### Deployed resources

The following components are deployed via Helm/Manifests as part of the core installation. For more information, go to their respective sections:

* [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Components of Dynatrace Operator") manages the automated rollout, configuration, and lifecycle of Dynatrace components in your Kubernetes environment.
* [Dynatrace Operator webhook](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Components of Dynatrace Operator") validates DynaKube definitions, converts definitions with older API versions, and injects configurations into Pods.
* [Dynatrace Operator CSI Driver](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Components of Dynatrace Operator") Optional, deployed as a DaemonSet, provides writable volume storage for OneAgent binaries to minimize network and storage usage.

The following component is deployed by applying a DynaKube with Application observability:

* [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") routes observability data to the Dynatrace cluster.
* Dynatrace code modules are injected into your application to enable deep monitoring and observability.

![auto-injection](https://dt-cdn.net/images/screenshot-2024-01-31-at-3-23-56-pm-2358-6db693bc75.png)

## Pod runtime injection

You can use the application monitoring for application Pods. You don't install OneAgent Pods and can't collect host metrics from Kubernetes nodes.

### Capabilities

* Dynatrace code modules are injected into Pods using Kubernetes init containers.
* Different container images can have separate configurations for different Dynatrace environments.

### Limitations

Because Dynatrace Operator is not involved, no automatic injection, configuration, or enrichment occurs. You need to manually adjust your Kubernetes workloads.

![PodRuntime Illustration](https://dt-cdn.net/images/podruntime-891-f7ca7624de.png)

## Container build-time injection

You can use the application monitoring for application Pods. You don't install OneAgent Pods and can't collect host metrics from Kubernetes nodes.

### Capabilities

* Dynatrace code modules are embedded into container images during the build process.
* Different container images can be configured for different Dynatrace environments and used across any container platform or PaaS in addition to Kubernetes.

### Limitations

Without Dynatrace Operator, there is no automatic injection, configuration, or enrichment. You need to manually adapt your build process.

![BuildTimeInjection illustration](https://dt-cdn.net/images/buildtimeinjection-891-1c5525cb55.png)