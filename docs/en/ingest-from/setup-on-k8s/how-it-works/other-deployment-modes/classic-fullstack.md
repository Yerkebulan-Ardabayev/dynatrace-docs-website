---
title: Classic Full-Stack monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack
scraped: 2026-02-28T21:16:10.078915
---

# Classic Full-Stack monitoring

# Classic Full-Stack monitoring

* Latest Dynatrace
* 2-min read
* Published Oct 31, 2024

Classic Full-Stack monitoring integrates host and application monitoring for Kubernetes environments. Instrumented Pods maintain their relationship with hosts, enabling the collection of host metrics.

See [`.spec.oneAgent.classicFullStack`](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") section of DynaKube for additional information.

## Capabilities

* Instrumented Pods maintain their taxonomic relationship with hosts and host metrics. OneAgent complements code modules with OOM detection, disk and storage monitoring, network monitoring, and more.
* This all-in-one approach includes Kubernetes cluster monitoring, distributed tracing, fault domain isolation, and deep code-level insights using a single deployment configuration across your clusters.

## Limitations

Thereâs a startup dependency between the container where OneAgent is deployed and the application container to be instrumented (for example, containers with deep process monitoring enabled). The OneAgent container must be started, and the `oneagenthelper` process must be running before the application container is launched to ensure proper instrumentation.

## Deployed resources

### Dynatrace Operator components

The following components are deployed via Helm/Manifests as part of the core installation. For more information, go to their respective sections:

* [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Components of Dynatrace Operator") manages the automated rollout, configuration, and lifecycle of Dynatrace components in your Kubernetes environment.
* [Dynatrace Operator webhook](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Components of Dynatrace Operator") validates DynaKube definitions, converts definitions with older API versions, and injects configurations into Pods.

### Operator-managed components

The following components are deployed by applying a DynaKube with full-stack observability:

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") collects host metrics from Kubernetes nodes.
* [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") routes observability data to the Dynatrace cluster and monitors the Kubernetes API.

![classic-full-stack](https://dt-cdn.net/images/screenshot-2024-01-31-at-2-37-54-pm-2354-6d55b949e0.png)

Classic full-stack injection requires *write access* from the OneAgent Pod to the Kubernetes node file system to detect and inject into newly deployed containers.