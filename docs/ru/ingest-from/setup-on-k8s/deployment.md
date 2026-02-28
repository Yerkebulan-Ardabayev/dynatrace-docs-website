---
title: Deployment
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment
scraped: 2026-02-28T21:22:09.026841
---

# Deployment

# Deployment

* Latest Dynatrace
* 6-min read
* Updated on Jan 28, 2026

Dynatrace provides a flexible approach to Kubernetes observability where you can pick and choose the level of observability you need for your Kubernetes clusters. This page gives an overview and guided path on the recommended options to cover your Kubernetes observability needs.
All deployment options on this page leverage [Dynatrace Operatorï»¿](https://github.com/Dynatrace/dynatrace-operator). For dedicated documentation and options for the major Kubernetes distributions, see [Distributions](/docs/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

## Observability options

1

For new users, the Dynatrace environment is preconfigured to ingest logs, and opting out is managed through [log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

Rollout and permissions overview

This table gives an overview of all the used components and required permissions for your Kubernetes observability needs. Dynatrace Operator manages the lifecycle of all observability components needed for your Kubernetes observability needs.

1

Please see [Dynatrace Operator security](/docs/ingest-from/setup-on-k8s/reference/security "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") for more detailed documentation.

[### Kubernetes platform monitoring

Understand and troubleshoot the health of your Kubernetes clusters.](/docs/ingest-from/setup-on-k8s/deployment/platform-observability "Deploy Dynatrace Operator for Kubernetes platform monitoring.")[### Kubernetes platform monitoring + Application observability

Ensure workload and microservice health and performance with automatic instrumentation.](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")[### Kubernetes platform monitoring + Full-Stack observability

Ensure workload, microservice and infrastructure health and performance throughout your cluster.](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes")

## Leverage the Dynatrace platform value

The Dynatrace platform offers a variety of apps, analytics and automation functionality to cover your use cases for unified observability and security. You can leverage these capabilities for all the Kubernetes observability data you collect with any of the above modes, such as the ability to:

* Explore Kubernetes health and signals in the [Kubernetes app](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")
* Visualize data with [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")
* Collaborate and conduct custom analysis with [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* Automate with [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* Boost productivity with [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") and [enerative AI](/docs/dynatrace-intelligence/copilot "Learn about Dynatrace Intelligence generative AI.")
* Forecast trends and prevent issues with [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.")
* And much moreâ¦

## Deployment from Marketplaces

Dynatrace supports deploying Dynatrace Operator from within the following Marketplaces:

* [OpenShift OperatorHub](/docs/ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub "Deploy Dynatrace Operator on OpenShift via OperatorHub.")
* [AWS Marketplaceï»¿](https://aws.amazon.com/marketplace/pp/prodview-brb73nceicv7u)
* [GKE Marketplaceï»¿](https://console.cloud.google.com/marketplace/product/dynatrace-marketplace-prod/dynatrace-operator)
* [Azure Marketplaceï»¿](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/dynatrace.azure-dynatrace-operator?tab=Overview)

## Learn more

[### How it works

Familiarize yourself with Dynatrace components that are deployed in your Kubernetes cluster.](/docs/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.")[### Guides

Learn how you can configure Dynatrace Operator to support specific use cases.](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases")[### Reference

API reference and configuration options for all Dynatrace components within your Kubernetes cluster.](/docs/ingest-from/setup-on-k8s/reference "Contains a reference page with configuration options for each Dynatrace component")[### Dynatrace Operator release notes

See release notes for Dynatrace Operator.](/docs/whats-new/dynatrace-operator "Release notes for Dynatrace Operator")