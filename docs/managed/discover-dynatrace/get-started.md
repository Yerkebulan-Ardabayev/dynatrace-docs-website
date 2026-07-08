---
title: Get started
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started
---

# Get started

# Get started

* How-to guide
* 3-min read
* Updated on May 15, 2026

Dynatrace Managed is an on-premises observability platform that enables you to analyze, automate, and innovate with the power of AI. Get started with Dynatrace Managed in just a few steps.

## Get started

### Step 1 Obtain a Dynatrace Managed license

* To obtain a license for Dynatrace Managed, contact [Dynatrace Sales﻿](https://dt-url.net/c901yj9). Your sales representative will provide you with further details. Dynatrace monitoring uses a consumption-based licensing model where you purchase and consume monitoring units based on your needs. For details, see [License Dynatrace](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.").
* Once you reach an agreement, you'll receive an email with your license details and instructions on how to get started.

### Step 2 Set up a Managed Cluster

* Select a [deployment model](/managed/managed-cluster/basics/managed-deployments "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.") that best suits your needs. Based on your selected deployment model, [set up a Managed Cluster](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") and create your first Managed Cluster node.
* You can [add more nodes](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.") at any time. A Managed Cluster in production requires a minimum of 3 nodes.

### Step 3 Install ActiveGate

* Install [Cluster ActiveGates](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.") and [Environment ActiveGates](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") as your selected deployment model requires.

### Step 4 Ingest telemetry data

* [Install OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation "Install OneAgent on a server for the very first time.") on a host to automatically monitor and analyze the performance and health of your entire IT infrastructure.
* [Ingest data from OpenTelemetry﻿](https://www.dynatrace.com/news/blog/send-opentelemetry-data-to-dynatrace/#configure-the-otel-collector-for-dynatrace) for a more hybrid infrastructure.

### Step 5 Verify you receive data

* View your identified topology with [Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.") in your [monitoring environment](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").

### Step 6 Visualize data

* Start building your own [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").

### Step 7 Set up notifications

* Set up your first [notifications](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications "Learn how to integrate third-party problem notification systems with Dynatrace.").

## Additional resources

* If you work in a government context, see [Dynatrace for Government](/managed/discover-dynatrace/get-started/dynatrace-for-government "Learn about Dynatrace for Government, how to get started, how to deploy Dynatrace, how to monitor with Dynatrace, and much more.") for deployment and compliance considerations specific to government environments.