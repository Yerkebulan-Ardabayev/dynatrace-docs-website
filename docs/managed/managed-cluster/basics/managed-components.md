---
title: Managed components
source: https://docs.dynatrace.com/managed/managed-cluster/basics/managed-components
scraped: 2026-05-12T11:08:47.577972
---

# Managed components

# Managed components

* Explanation
* 3-min read
* Updated on May 08, 2026

The following image shows the Dynatrace Managed components.

![Managed architecture](https://dt-cdn.net/images/managed-general-architecture-1892-448d089eed.png)

Managed architecture

## Managed Cluster

The Managed Cluster is responsible for managing various [monitoring environments](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments."). A Managed Cluster typically comprises multiple nodes. Each Managed Cluster has a dedicated Cluster Management Console.

The Managed Cluster provides Mission Control with self-monitoring and licensing data to enable proactive support.

You need to [obtain a license](/managed/discover-dynatrace/get-started "Learn how to get started with Dynatrace Managed.") every time you want to set up a new Managed Cluster.

## Managed Installer

The Managed Installer handles the installation of Dynatrace Managed and all the necessary components:

* Dynatrace Server
* Apache Cassandra
* Elasticsearch
* NGINX
* An embedded ActiveGate

All listed components are deployed on the first node you create when [setting up a Managed Cluster](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration."), as well as on every [subsequent node](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.").

## Cluster Management Console

For each Managed Cluster you set up, there is a dedicated Cluster Management Console. The Cluster Management Console is a web-based UI for managing your Managed Cluster. From here you can view the deployment status of your Managed Cluster at any time.

With the Cluster Management Console, you can, for example:

* [Create user accounts and groups](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Learn about the supported permissions and policies, how you can assign them to groups, and how you can manage your users and groups.").
* [Add Cluster nodes](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.").
* [Add monitoring environments](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.").

## Mission Control

[Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") receives self-monitoring and license data from the Managed Cluster. Based on this data, the Dynatrace Mission Control team can proactively analyze and detect misconfigurations or potential incompatibilities with your installation. Mission Control also provides software updates for the Managed Cluster.