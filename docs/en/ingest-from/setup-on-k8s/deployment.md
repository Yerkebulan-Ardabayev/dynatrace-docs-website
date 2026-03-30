---
title: Deployment
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment
scraped: 2026-03-06T21:18:13.543710
---

# Deployment


* Latest Dynatrace
* 6-min read
* Updated on Jan 28, 2026

Dynatrace provides a flexible approach to Kubernetes observability where you can pick and choose the level of observability you need for your Kubernetes clusters. This page gives an overview and guided path on the recommended options to cover your Kubernetes observability needs.
All deployment options on this page leverage [Dynatrace Operatorï»¿](https://github.com/Dynatrace/dynatrace-operator). For dedicated documentation and options for the major Kubernetes distributions, see Distributions.

## Observability options

1

For new users, the Dynatrace environment is preconfigured to ingest logs, and opting out is managed through log ingest rules.

Rollout and permissions overview

This table gives an overview of all the used components and required permissions for your Kubernetes observability needs. Dynatrace Operator manages the lifecycle of all observability components needed for your Kubernetes observability needs.

1

Please see Dynatrace Operator security for more detailed documentation.

### Kubernetes platform monitoring

Understand and troubleshoot the health of your Kubernetes clusters.### Kubernetes platform monitoring + Application observability

Ensure workload and microservice health and performance with automatic instrumentation.### Kubernetes platform monitoring + Full-Stack observability

Ensure workload, microservice and infrastructure health and performance throughout your cluster.

## Leverage the Dynatrace platform value

The Dynatrace platform offers a variety of apps, analytics and automation functionality to cover your use cases for unified observability and security. You can leverage these capabilities for all the Kubernetes observability data you collect with any of the above modes, such as the ability to:

* Explore Kubernetes health and signals in the Kubernetes app
* Visualize data with Dashboards
* Collaborate and conduct custom analysis with Notebooks
* Automate with Workflows
* Boost productivity with Dynatrace Intelligence and enerative AI
* Forecast trends and prevent issues with Dynatrace Intelligence predictive AI analysis
* And much moreâ¦

## Deployment from Marketplaces

Dynatrace supports deploying Dynatrace Operator from within the following Marketplaces:

* OpenShift OperatorHub
* [AWS Marketplaceï»¿](https://aws.amazon.com/marketplace/pp/prodview-brb73nceicv7u)
* [GKE Marketplaceï»¿](https://console.cloud.google.com/marketplace/product/dynatrace-marketplace-prod/dynatrace-operator)
* [Azure Marketplaceï»¿](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/dynatrace.azure-dynatrace-operator?tab=Overview)

## Learn more

### How it works

Familiarize yourself with Dynatrace components that are deployed in your Kubernetes cluster.### Guides

Learn how you can configure Dynatrace Operator to support specific use cases.### Reference

API reference and configuration options for all Dynatrace components within your Kubernetes cluster.### Dynatrace Operator release notes

See release notes for Dynatrace Operator.