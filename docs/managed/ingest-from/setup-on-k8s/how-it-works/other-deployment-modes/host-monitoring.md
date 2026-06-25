---
title: Host monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/host-monitoring
scraped: 2026-05-12T11:54:00.387980
---

# Host monitoring

# Host monitoring

* 1-min read
* Published Oct 31, 2024

Host monitoring collects host metrics and process data from Kubernetes nodes. It deploys OneAgent to capture metrics such as CPU, memory, disk, and network usage. This mode does not include application-level monitoring.

See the [`.spec.oneAgent.hostMonitoring`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") section of DynaKube for additional information.

## Capabilities

Collects host metrics and process data.

## Limitations

Diagnostic files (support archives) for application Pods aren't yet supported for read-only file systems.

## Deployed resources

### Dynatrace Operator components

The following components are deployed via Helm/Manifests as part of the core installation. For more information, go to their respective sections:

* [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Components of Dynatrace Operator") manages the automated rollout, configuration, and lifecycle of Dynatrace components in your Kubernetes environment.
* [Dynatrace Operator webhook](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Components of Dynatrace Operator") validates DynaKube definitions, converts definitions with older API versions, and injects configurations into Pods.
* [Dynatrace Operator CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Components of Dynatrace Operator") deployed as a DaemonSet, provides writable volume storage for OneAgent binaries to minimize network and storage usage.

### Operator-managed components

The following components are deployed by applying a DynaKube with full-stack observability:

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") collects host metrics from Kubernetes nodes.
* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") routes observability data to the Dynatrace cluster.

![host-monitoring](https://dt-cdn.net/images/image-20240612-113305-1637-c57403b85c.png)

host-monitoring