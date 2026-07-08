---
title: OneAgent connectivity in network zones
source: https://docs.dynatrace.com/managed/manage/network-zones/oneagent-connectivity
---

# OneAgent connectivity in network zones

# OneAgent connectivity in network zones

* Explanation
* 1-min read
* Updated on Sep 26, 2023

Network zones enforce the connectivity order for OneAgents and ActiveGates. This page describes connectivity priority for OneAgents. For information about ActiveGates, see [ActiveGate connectivity in network zones](/managed/manage/network-zones/activegate-connectivity "Find out how network zones prioritize ActiveGates for Environment ActiveGate connectivity.").

## Priority groups

A network zone instructs OneAgent to communicate with ActiveGates from the same network zone. If that isn't possible, OneAgent tries to connect to another ActiveGate. To organize these fallback connections, all ActiveGates are sorted into priority groups:

* Group 1—ActiveGates from the same network zone.
* Group 2—ActiveGates from the alternative network zone.
* Group 3—ActiveGates from the default network zone.
* Group 4—All other ActiveGates.

In every group, ActiveGates are further prioritized depending on the type:

* Index 1—Environment ActiveGates
* Index 2—Cluster ActiveGates
* Index 3—Embedded ActiveGates

![ActiveGate priority](https://dt-cdn.net/images/ag-priority-1532-2ffac1c718.png)

ActiveGate priority

OneAgents are load-balanced to use an ActiveGate with the lowest possible index. That is, if several ActiveGates with the low index are available, OneAgents will try to switch between the available ActiveGates on a regular basis.

If the preferable ActiveGate is not available, OneAgent tries the next higher index, until a connection is established. In that case, OneAgent will regularly check in the background for availability of ActiveGates with a lower index.

[Multi-environment ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Read the step-by-step procedure for configuring a single Environment ActiveGate for multi-environment support.") can have only one zone that is valid across all connected environments.

For example, suppose the following three ActiveGates are available:

* Environment ActiveGate from the same network zone (index 1.1)
* Environment ActiveGate from an alternative network zone (index 2.1)
* Cluster ActiveGate from the same network zone (index 1.2)

The ActiveGate with index 1.1 is used. If it becomes unavailable, the next choice is the ActiveGate with index 1.2. If OneAgent fails to connect to this one, the ActiveGate with index 2.1 is used.

## Fallback modes for network zones

When determining fallback connections for OneAgents, the following modes are considered (with reference to the [priority groups](#priority-groups) described earlier):

* **Any ActiveGate (default)** corresponds to priority groups 1, 2, 3, and 4.
* **Only DefaultZone** corresponds to priority groups 1, 2, and 3.
* **None (drop traffic)** corresponds to priority groups 1 and 2.

## Unconfigured OneAgents

OneAgents with no network zone configured (that includes all OneAgents from the **Default** network zone) work as if the network zone doesn't exist.

Such OneAgents try to connect to any ActiveGate in a random order and choose the first responding Environment ActiveGate. For load balancing, after a few minutes they try to switch to the next responding Environment ActiveGate.

Dynatrace Managed If no Environment ActiveGate can be reached, OneAgents connect to the first responding Cluster ActiveGate. For load balancing, after a few minutes they try to switch to the next responding Cluster ActiveGate. In that case, OneAgent traffic goes to the Dynatrace Managed cluster uncompressed.

## Related topics

* [Supported connectivity schemes for ActiveGates](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.")