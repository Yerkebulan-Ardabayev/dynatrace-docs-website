---
title: Installation
source: https://docs.dynatrace.com/managed/managed-cluster/installation
scraped: 2026-05-12T11:11:15.011604
---

# Installation

# Installation

* 1-min read
* Updated on May 09, 2026

Install and configure a Dynatrace Managed Cluster. Start by reviewing the hardware, operating system, and network requirements, then run the cluster installer. After installation, you can add nodes, install a Cluster ActiveGate, and configure SSL certificates. For environments without internet access, the offline mode section covers all relevant steps.

## Prerequisites

[### Hardware requirements

Review CPU, RAM, storage, and multi-node sizing requirements.](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.")[### Operating system requirements

Review supported Linux distributions and host requirements.](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.")[### Configure SELinux

Enable or disable SELinux on the cluster host before installation.](/managed/managed-cluster/installation/selinux "Configure Dynatrace Managed to run on a system with SELinux enabled in enforcing mode, or disable SELinux on your host.")[### Cluster node ports

Configure firewall rules for required inbound and outbound ports.](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.")[### Hardware requirements for cloud deployments

Find recommended VM sizes for AWS, Azure, and Google Cloud.](/managed/managed-cluster/installation/managed-cloud-requirements "Find the required virtual machine sizes for deploying Dynatrace Managed on Amazon Web Services, Microsoft Azure, and Google Cloud.")

## Installation

[### Install a Managed Cluster

Download, verify, and run the Managed Cluster installer.](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[### Customize installation

Configure installation parameters such as paths, ports, and SSL settings.](/managed/managed-cluster/installation/customize-managed-cluster-install "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.")[### Add a Cluster node

Expand an existing cluster by adding a new node.](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.")[### Managed Cluster certificate

Configure a custom SSL certificate on a Managed Cluster node.](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")[### Install a Cluster ActiveGate

Install and configure a Cluster ActiveGate for external communication.](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")[### Cluster ActiveGate certificate

Configure a custom SSL certificate on a Cluster ActiveGate.](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate "Configure a custom SSL certificate on a Cluster ActiveGate instead of relying on Dynatrace-managed certificate automation.")

## Offline mode

[### Dynatrace Managed in offline mode

Install and update Dynatrace Managed without an internet connection.](/managed/managed-cluster/installation/dynatrace-managed-offline "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[### Convert Managed Cluster from offline to online

Switch a Managed Cluster from offline to online mode.](/managed/managed-cluster/installation/cluster-offline-to-online "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")