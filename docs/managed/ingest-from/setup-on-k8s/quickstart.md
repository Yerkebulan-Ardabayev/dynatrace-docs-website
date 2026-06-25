---
title: Quickstart
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/quickstart
scraped: 2026-05-12T11:11:16.232515
---

# Quickstart

# Quickstart

* 2-min read
* Updated on Dec 18, 2024

This page guides you to install Dynatrace components within a minute on your Kubernetes cluster in order to quickly benefit from the Dynatrace observability & analytics platform.

Prerequisites

Before installing Dynatrace on your Kubernetes cluster, ensure that you meet the following requirements:

* Your `kubectl` CLI is connected to the Kubernetes cluster that you want to monitor.
* You have sufficient privileges on the monitored cluster to run `kubectl` or `oc` commands.

### Cluster setup and configuration

* You must allow egress for Dynatrace pods (default: Dynatrace namespace) to your Dynatrace environment URL.

  + For Dynatrace Managed, you can optionally use a Cluster ActiveGate URL.
* For OpenShift Dedicated, you need the [cluster-admin roleï»¿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Helm installation Use [Helm version 3ï»¿](https://dt-url.net/n5036j1).

### Supported versions

See supported Kubernetes/OpenShift [platform versions](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") and [distributions](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

## Deploy Dynatrace Operator

You will get insights and actionable answers into your Kubernetes platform as well as your containerized apps by [deploying Dynatrace for Full Kubernetes Observability](/managed/ingest-from/setup-on-k8s/deployment#fullObs "Deploy Dynatrace Operator on Kubernetes") in cloud-native full-stack mode.

1. Go to **Kubernetes**.
2. Select **Connect automatically via Dynatrace Operator**.
3. Follow the on-screen instructions.

![quickstart](https://dt-cdn.net/images/quickstart-2nd-gen-2976-cd3bfad512.png)

quickstart

## Learn more

[### Deployment mode

Determine the recommended deployment mode for your intended setup based on your requirements.](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes")[### Integrations

Leverage open source components to ingest additional observability signals into Dynatrace.](/managed/ingest-from/setup-on-k8s/extend-observability-k8s "How data ingest can be extended with open source components")[### How it works

Familiarize yourself with Dynatrace components that are deployed in your Kubernetes cluster.](/managed/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.")[### Guides

Learn how you can configure Dynatrace Operator to support specific use cases.](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases")[### Get actionable answers

Start to analyze your Kubernetes clusters and containerized Apps with Dynatrace and benefit from actionable answers.](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")

## Related topics

* [Kubernetes cluster and workload monitoringï»¿](https://www.dynatrace.com/technologies/kubernetes-monitoring/)