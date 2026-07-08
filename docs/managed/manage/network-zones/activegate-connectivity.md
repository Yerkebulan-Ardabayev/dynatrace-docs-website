---
title: ActiveGate connectivity in network zones
source: https://docs.dynatrace.com/managed/manage/network-zones/activegate-connectivity
---

# ActiveGate connectivity in network zones

# ActiveGate connectivity in network zones

* Explanation
* 1-min read
* Published Mar 30, 2020

Network zones enforce the connectivity order for OneAgents and ActiveGates. This page describes connectivity priority for ActiveGates. For information about OneAgents, see [OneAgent connectivity in network zones](/managed/manage/network-zones/oneagent-connectivity "Find out how network zones prioritize ActiveGates for OneAgent connectivity.").

* Group 1—ActiveGates from the same network zone.
* Group 2—ActiveGates from the alternative network zone.
* Group 3—ActiveGates from the default network zone.
* Group 4—All other ActiveGates.

In every group, ActiveGates are further prioritized depending on the type:

* Index 1—Embedded ActiveGates
* Index 2—Cluster ActiveGates

![ActiveGate priority](https://dt-cdn.net/images/ag-routing-1532-4db537c11f.png)

ActiveGate priority

The preferable ActiveGate is the one with lowest possible index. For load balancing, an Environment ActiveGate rotates through all available endpoints of ActiveGates with the lowest possible index.

If the preferable ActiveGate is not available, Environment ActiveGate tries the next higher index, until a connection is established. In that case, Environment ActiveGate will regularly check in the background for availability of ActiveGates with a lower index.

For example, if three ActiveGates are available:

* Embedded ActiveGate from the same network zone (index 1.1)
* Embedded ActiveGate from an alternative network zone (index 2.1)
* Cluster ActiveGate from the same network zone (index 1.2)

the ActiveGate with index 1.1 is used. If it becomes unavailable, the next choice is the ActiveGate with index 1.2. If Environment ActiveGate fails to connect to this one, the ActiveGate with index 2.1 is used.

## Unconfigured ActiveGates

Environment ActiveGates with no network zone configured (that includes all ActiveGates from the **Default** network zone) work as if the network zone doesn't exist. Such ActiveGates try to connect to the first available ActiveGate based on the following priority:

* Index 1—Embedded ActiveGates
* Index 2—Cluster ActiveGates

For load balancing, after a few minutes they try to switch to the next responding ActiveGate of the lowest possible index.

## Related topics

* [Supported connectivity schemes for ActiveGates](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.")