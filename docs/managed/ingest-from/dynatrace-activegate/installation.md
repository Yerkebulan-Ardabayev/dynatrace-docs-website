---
title: Installation
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation
---

# Installation

# Installation

* 1-min read
* Published Apr 09, 2021

Dynatrace offers two types of ActiveGate: Environment ActiveGate and Cluster ActiveGate. Dynatrace Managed deployments typically require both ActiveGate types, though the most important type is the [Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster."). For Dynatrace Managed deployments, see [additional ActiveGate use cases for Dynatrace Managed](/managed/managed-cluster/basics/managed-deployments#scenario-2-pure-dynatrace-managed-setup "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.").

An Environment ActiveGate can be installed:

* using an installer, on a virtual or physical host—this is called **host-based deployment**
* in a container—this is called **containerized deployment**

## Host-based ActiveGate deployment

### Linux

[Install an Environment ActiveGate on Linux](/managed/ingest-from/dynatrace-activegate/installation/linux "Learn how to install ActiveGate on Windows, customize installation, and more.")

### Windows

[Install an Environment ActiveGate on Windows](/managed/ingest-from/dynatrace-activegate/installation/windows "Learn how to install ActiveGate on Windows, customize installation, and more.")

## Containerized ActiveGate deployment

### Kubernetes

[Install an Environment ActiveGate on Kubernetes](/managed/ingest-from/dynatrace-activegate/activegate-in-container "Deploy a containerized ActiveGate.")

### OpenShift

[Install an Environment ActiveGate on OpenShift](/managed/ingest-from/dynatrace-activegate/activegate-in-container "Deploy a containerized ActiveGate.")