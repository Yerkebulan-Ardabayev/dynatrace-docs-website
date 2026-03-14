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

You will need different types of ActiveGatesâ**Environment ActiveGates** or **Cluster ActiveGates**âbased on the Dynatrace [deployment solution](dynatrace-activegate/supported-connectivity-schemes-for-activegates.md "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.") you are using and also based on the [purpose](dynatrace-activegate/capabilities.md "Learn the capabilities and uses of ActiveGate.") for which you are using Dynatrace.

If you are using the Dynatrace [SaaS solution](dynatrace-activegate/supported-connectivity-schemes-for-activegates.md#saas-scheme "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents."), you only need to install an Environment ActiveGate.

To use specific ActiveGate functional featuresâreferred to as [modules](dynatrace-activegate/configuration/configure-activegate.md#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.")âyou need an ActiveGate with those modules installed or activated: When you install an ActiveGate, you select the main [purpose](dynatrace-activegate/capabilities.md "Learn the capabilities and uses of ActiveGate.") of the installation and thenâdepending on the purposeâyou can install or activate a different set of functional [modules](dynatrace-activegate/configuration/configure-activegate.md#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.").

An ActiveGate can be deployed in the conventional mannerâon a physical or virtual hostâthis is **host-based ActiveGate deployment**.
An ActiveGate packaged in a container is referred to as **containerized ActiveGate deployment**.

### ActiveGate purposes and functionality

[Route OneAgent traffic](dynatrace-activegate/capabilities/routing-monitoring-purpose.md#route "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

[Monitor cloud environments and remote technologies](dynatrace-activegate/capabilities/routing-monitoring-purpose.md#monitor "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

[Run synthetic monitors](dynatrace-activegate/capabilities/synthetic-purpose.md "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")

[Route z/OS traffic](dynatrace-activegate/capabilities/zremote-purpose.md "Learn about installing the zRemote module for z/OS monitoring.")

[Dynatrace API](dynatrace-activegate/capabilities/routing-monitoring-purpose.md#api "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

[Functionality per ActiveGate type](dynatrace-activegate/capabilities.md "Learn the capabilities and uses of ActiveGate.")

### System and hardware requirements

[Routing/monitoring ActiveGate, on Linux](dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements.md "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

[Routing/monitoring ActiveGate, on Windows](dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements.md "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

[Synthetic-enabled ActiveGate](../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic.md "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations")

[ActiveGate for routing z/OS traffic to Dynatrace](dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote.md "Prepare and install the zRemote for z/OS monitoring.")

### See also

[ActiveGate connectivity schemes](dynatrace-activegate/supported-connectivity-schemes-for-activegates.md "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.")

## Installation

Operating systems

Container platforms

[Linux](dynatrace-activegate/installation/linux.md) [Windows](dynatrace-activegate/installation/windows.md)

[Kubernetes](dynatrace-activegate/activegate-in-container.md) [OpenShift](dynatrace-activegate/activegate-in-container.md)