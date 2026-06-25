---
title: Deployment
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment
scraped: 2026-05-12T11:11:02.252135
---

# Deployment

# Deployment

* 6-min read
* Updated on Jan 28, 2026

Dynatrace provides a flexible approach to Kubernetes observability where you can pick and choose the level of observability you need for your Kubernetes clusters. This page gives an overview and guided path on the recommended options to cover your Kubernetes observability needs.
All deployment options on this page leverage [Dynatrace Operatorï»¿](https://github.com/Dynatrace/dynatrace-operator). For dedicated documentation and options for the major Kubernetes distributions, see [Distributions](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

## Observability options

### Full Kubernetes observability

Get immediate insights into your Kubernetes health and out-of-the-box distributed tracing and analytics for your workloads

#### Deployment options

* Recommended [Deploy Dynatrace Operator in cloud-native full-stack mode](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes")
* [Deploy Dynatrace Operator in classic full-stack mode](/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes")  
  Limitations: Thereâs a startup dependency between the container in which OneAgent is deployed and application containers to be instrumented (for example, containers that have deep process monitoring enabled). The OneAgent container must be started and the oneagenthelper process must be running before the application container is launched so that the application can be properly instrumented.

Other option

* Deprecated [Manual OneAgent rollout via Daemonset](/managed/ingest-from/setup-on-k8s/deployment/other/oneagent-daemonset "Deploy, update, and uninstall OneAgent DaemonSet on Kubernetes.") (not based on Dynatrace Operator)

### Kubernetes observability

Understand and troubleshoot the health of your Kubernetes clusters

#### Deployment

[Deploy Dynatrace Operator for Kubernetes observability](/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed "Deploy Dynatrace Operator for Kubernetes observability.")

### Application observability

Enhance workload health and performance with automated distributed tracing and code-level visibility.

#### Deployment

[Deploy Dynatrace Operator in application monitoring mode](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")

Other options

The following options for application monitoring are not based on Dynatrace Operator:

* [Pod-runtime injection](/managed/ingest-from/setup-on-k8s/deployment/other/pod-runtime "Inject Dynatrace code modules into a container during its deployment.")
* [Build-time injection](/managed/ingest-from/setup-on-k8s/deployment/other/container-buildtime "Inject Dynatrace code modules into a container during the build process for every new Pod deployment.")

For the S390x architecture, [pod runtime](/managed/ingest-from/setup-on-k8s/deployment/other/pod-runtime "Inject Dynatrace code modules into a container during its deployment.") and [container build-time](/managed/ingest-from/setup-on-k8s/deployment/other/container-buildtime "Inject Dynatrace code modules into a container during the build process for every new Pod deployment.") injections are supported.

## Deployment from Marketplaces

Dynatrace supports deploying Dynatrace Operator from within the following Marketplaces:

* [OpenShift OperatorHub](/managed/ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub "Deploy Dynatrace Operator on OpenShift via OperatorHub.")
* [AWS Marketplaceï»¿](https://aws.amazon.com/marketplace/pp/prodview-brb73nceicv7u)
* [GKE Marketplaceï»¿](https://console.cloud.google.com/marketplace/product/dynatrace-marketplace-prod/dynatrace-operator)
* [Azure Marketplaceï»¿](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/dynatrace.azure-dynatrace-operator?tab=Overview)

## Learn more

[### How it works

Familiarize yourself with Dynatrace components that are deployed in your Kubernetes cluster.](/managed/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.")[### Guides

Learn how you can configure Dynatrace Operator to support specific use cases.](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases")[### Reference

API reference and configuration options for all Dynatrace components within your Kubernetes cluster.](/managed/ingest-from/setup-on-k8s/reference "Contains a reference page with configuration options for each Dynatrace component")[### Dynatrace Operator release notes

See release notes for Dynatrace Operator.](/managed/whats-new/dynatrace-operator "Release notes for Dynatrace Operator")