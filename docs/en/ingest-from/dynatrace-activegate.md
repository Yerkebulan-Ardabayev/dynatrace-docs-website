---
title: Dynatrace ActiveGate
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate
scraped: 2026-03-06T21:12:45.606066
---

# Dynatrace ActiveGate


* Latest Dynatrace
* 3-min read
* Published Jul 23, 2018

### ActiveGate acts as a secure proxy

A Dynatrace ActiveGate acts as a secure proxy between Dynatrace OneAgents and Dynatrace Clusters or between Dynatrace OneAgents and other ActiveGatesâthose closer to the Dynatrace Cluster.  
It establishes Dynatrace presenceâin your local network. In this way it allows you to reduce your interaction with Dynatrace to one single pointâavailable locally. Besides convenience, this solution optimizes traffic volume, reduces the complexity of the network and cost. It also ensures the security of sealed networks.

### ActiveGate performs monitoring

In addition to routing monitoring data captured by OneAgents, Dynatrace ActiveGate is also capable of performing monitoring tasksâusing API to query and monitor a wide range of technologies. The list of monitored technologies is not limited, but can be extended dynamically. It includes cloud and data center technologies, for example, AWS, VMware, Azure, Kubernetes, OpenShift, Cloud Foundry, Google Cloud, Oracle, SNMP, WMI, Prometheus, and many others.

### 

Diagram of ActiveGate Functions

![Functions of an ActiveGate](https://dt-cdn.net/images/ag-general-005-1-1048-b2d55cede0.png)

### ActiveGate types, purposes and functional modules

You will need different types of ActiveGatesâ**Environment ActiveGates** or **Cluster ActiveGates**âbased on the Dynatrace deployment solution you are using and also based on the purpose for which you are using Dynatrace.

If you are using the Dynatrace [SaaS solution](dynatrace-activegate/supported-connectivity-schemes-for-activegates.md#saas-scheme "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents."), you only need to install an Environment ActiveGate.

To use specific ActiveGate functional featuresâreferred to as modulesâyou need an ActiveGate with those modules installed or activated: When you install an ActiveGate, you select the main purpose of the installation and thenâdepending on the purposeâyou can install or activate a different set of functional modules.

An ActiveGate can be deployed in the conventional mannerâon a physical or virtual hostâthis is **host-based ActiveGate deployment**.
An ActiveGate packaged in a container is referred to as **containerized ActiveGate deployment**.

### ActiveGate purposes and functionality

Route OneAgent traffic

Monitor cloud environments and remote technologies

Run synthetic monitors

Route z/OS traffic

Dynatrace API

Functionality per ActiveGate type

### System and hardware requirements

Routing/monitoring ActiveGate, on Linux

Routing/monitoring ActiveGate, on Windows

Synthetic-enabled ActiveGate

ActiveGate for routing z/OS traffic to Dynatrace

### See also

ActiveGate connectivity schemes

## Installation

Operating systems

Container platforms

[Linux](dynatrace-activegate/installation/linux.md) [Windows](dynatrace-activegate/installation/windows.md)

[Kubernetes](dynatrace-activegate/activegate-in-container.md) [OpenShift](dynatrace-activegate/activegate-in-container.md)