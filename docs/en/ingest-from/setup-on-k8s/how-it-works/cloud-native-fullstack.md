---
title: Full-stack observability
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack
scraped: 2026-02-25T21:20:28.194738
---

# Full-stack observability

# Full-stack observability

* Latest Dynatrace
* 3-min read
* Published Oct 31, 2024

Full-stack observability combines infrastructure and application monitoring in Kubernetes environments. This setup includes the injection of Dynatrace OneAgent and provides insights into both cluster performance and application behavior.

See the [`.spec.oneAgent.cloudNativeFullStack`](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") section of DynaKube for additional information.

## Capabilities

* Offers similar functionality to the classic full-stack injection.
* Uses mutating webhooks to inject code modules into application Pods.
* Enables data enrichment for Kubernetes environments via [enrichment files](/docs/ingest-from/extend-dynatrace/extend-data#dynatrace-kubernetes-operator "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").

### Current limitations

* Diagnostic files (support archives) for application Pods aren't yet supported.
* Container monitoring rules aren't supported (the DynaKube label selector parameter provides similar functionality).
* [Go static monitoring](/docs/ingest-from/technology-support/application-software/go/support/go-known-limitations#static-monitoring "Learn the limitations for Go support and their workarounds.") is partially supported.
* OneAgent support archives, such as code module logs, can be gathered from the monitored process/Pod using the **Run OneAgent Diagnostics** menu option on the process-specific page. If no OneAgent support archive is available, it means one of the following:

  + No code module has been injected into the application Pod.
  + There is an issue with OneAgent creating the support archive.

## Deployed resources

### Dynatrace Operator components

The following components are deployed via Helm/Manifests as part of the core installation. For more information, go to their respective sections:

* [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Components of Dynatrace Operator") manages the automated rollout, configuration, and lifecycle of Dynatrace components in your Kubernetes environment.
* [Dynatrace Operator webhook](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Components of Dynatrace Operator") validates DynaKube definitions, converts definitions with older API versions, and injects configurations into Pods.
* [Dynatrace Operator CSI Driver](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Components of Dynatrace Operator") deployed as a DaemonSet, provides writable volume storage for OneAgent binaries to minimize network and storage usage.

### Operator-managed components

The following components are deployed by applying a DynaKube with full-stack observability:

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") collects host metrics from Kubernetes nodes.
* [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") routes observability data to the Dynatrace cluster and monitors the Kubernetes API.
* Dynatrace code modules are injected into your application to enable deep monitoring and observability.

![cloud-native](https://dt-cdn.net/images/screenshot-2024-01-31-at-2-40-02-pm-2352-4cba84df51.png)