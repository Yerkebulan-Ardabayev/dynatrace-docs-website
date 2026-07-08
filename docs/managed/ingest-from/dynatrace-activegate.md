---
title: Dynatrace ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate
---

# Dynatrace ActiveGate

# Dynatrace ActiveGate

* 3-min read
* Updated on Jun 09, 2026

### ActiveGate acts as a secure proxy

A Dynatrace ActiveGate acts as a secure proxy between Dynatrace OneAgents and Dynatrace Clusters or between Dynatrace OneAgents and other ActiveGates—those closer to the Dynatrace Cluster.  
It establishes Dynatrace presence—in your local network. In this way it allows you to reduce your interaction with Dynatrace to one single point—available locally. Besides convenience, this solution optimizes traffic volume, reduces the complexity of the network and cost. It also ensures the security of sealed networks.

### ActiveGate performs monitoring

In addition to routing monitoring data captured by OneAgents, Dynatrace ActiveGate is also capable of performing monitoring tasks—using API to query and monitor a wide range of technologies. The list of monitored technologies is not limited, but can be extended dynamically. It includes cloud and data center technologies, for example, AWS, VMware, Azure, Kubernetes, OpenShift, Cloud Foundry, Google Cloud, Oracle, SNMP, WMI, Prometheus, and many others.

### 

Diagram of ActiveGate Functions

![Functions of an ActiveGate](https://cdn.bfldr.com/B686QPH3/as/t4j8ggtv98xv8v8pccpvwf27/ActiveGate-ActiveGate_performance_monitoring-Light_Mode?auto=webp&format=png&position=1)

Functions of an ActiveGate

### ActiveGate types, purposes and functional modules

You will need different types of ActiveGates—**Environment ActiveGates** or **Cluster ActiveGates**—based on the Dynatrace [deployment solution](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.") you are using and also based on the [purpose](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") for which you are using Dynatrace.

Dynatrace [Managed deployments](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#managed-scheme "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.") typically require both ActiveGate types, though the most important type for Dynatrace Managed deployments is the [Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.").

To use specific ActiveGate functional features—referred to as [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.")—you need an ActiveGate with those modules installed or activated: When you install an ActiveGate, you select the main [purpose](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") of the installation and then—depending on the purpose—you can install or activate a different set of functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.").

An ActiveGate can be deployed in the conventional manner—on a physical or virtual host—this is **host-based ActiveGate deployment**.
An ActiveGate packaged in a container is referred to as **containerized ActiveGate deployment**.

### ActiveGate purposes and functionality

[Route OneAgent traffic](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#route "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

[Monitor cloud environments and remote technologies](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#monitor "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

[Run synthetic monitors](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")

[Route z/OS traffic](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring.")

[Dynatrace API](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#api "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

[Functionality per ActiveGate type](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.")

### System and hardware requirements

[Routing/monitoring ActiveGate, on Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

[Routing/monitoring ActiveGate, on Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

[Synthetic-enabled ActiveGate](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations")

[ActiveGate for routing z/OS traffic to Dynatrace](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.")

### See also

[ActiveGate connectivity schemes](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.")

## Installation

Operating systems

Container platforms

[Linux](/managed/ingest-from/dynatrace-activegate/installation/linux) [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows)

[Kubernetes](/managed/ingest-from/dynatrace-activegate/activegate-in-container) [OpenShift](/managed/ingest-from/dynatrace-activegate/activegate-in-container)