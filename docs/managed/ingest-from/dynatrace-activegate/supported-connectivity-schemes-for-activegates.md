---
title: Supported connectivity schemes for ActiveGates
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates
scraped: 2026-05-12T11:08:07.634086
---

# Supported connectivity schemes for ActiveGates

# Supported connectivity schemes for ActiveGates

* 4-min read
* Published Jul 17, 2018

ActiveGate can be used in a **[Dynatrace Managed connectivity scheme](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#managed-scheme "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.")**. The Dynatrace Managed connectivity scheme can be deployed in several different **[deployment scenarios](/managed/managed-cluster/basics/managed-deployments "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.")**.

Dynatrace requires certain ports and paths to be opened and accessible through the monitored infrastructure, firewalls and other components. The ports are [configurable](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#com-compuware-apm-webserver "Learn which ActiveGate properties you can configure based on your needs and requirements.") and the default values are shown here.

## Dynatrace Managed connectivity scheme

All possible connections for the Dynatrace Managed connectivity schemeâin all possible deployment scenariosâare shown below in one diagram.

The **solid arrows** indicate the preferred paths. For example, OneAgent will connect to an Environment ActiveGate, if one is present. It will, however, connect to a Cluster ActiveGate, if no connection to an Environment ActiveGate is possible, and it can even connect directly to a Dynatrace Managed Cluster.
The **direction of arrows** in the diagrams indicates which component initiates the connection.

![Dynatrace Managed connectivity scheme](https://dt-cdn.net/images/connectivity-managed-005-1200-04934824a0.png)

Dynatrace Managed connectivity scheme

## Port usage

* Environment ActiveGate receives connections on port 9999.

* Cluster ActiveGate receives connections on port 9999.
* Dynatrace Managed Cluster (embedded ActiveGate) receives connections on port 443.
  For more information see diagrams above.

If you run [Browser monitors](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") or [HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.") from private Synthetic locations, you need to make sure the Synthetic-enabled ActiveGate has access to the tested resource. If you use ActiveGate extensions, you need to make sure the ActiveGate executing the extensions has access to the monitored technology.

For Dynatrace Managed, ActiveGate must have network access to other services as well on specific ports, based on your [deployment scenario](/managed/managed-cluster/basics/managed-deployments "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.").

## Connection hierarchy

ActiveGates exist in the following hierarchy:

* Level 1âEnvironment ActiveGates
* Level 2âCluster ActiveGates
* Level 3âEmbedded ActiveGatesâActiveGates embedded within cluster nodes (not shown on graphs above).

ActiveGates can only send data to higher hierarchy levels. It is impossible to send data to the same or lower level of the hierarchy.

Environment ActiveGates, by default, connect directly to the Dynatrace Cluster (unless custom network zones are usedâsee below). This eliminates an intermediate step of connecting to a Cluster ActiveGate. Connecting through the Cluster ActiveGate needs to be arranged, if the Dynatrace Cluster is not directly reachable. For example, if the Environment ActiveGate is in a different network or different data center.

Connectivity can also depend on **[network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.")** if such are configured. Network zone configuration means that ActiveGates and OneAgents will prefer to communicate with ActiveGates from the same zone, before connecting to ActiveGates outside of the active zone.

## Proxy and load balancer configuration

All Dynatrace components (OneAgents, ActiveGates, Dynatrace Cluster) detect their hostnames and distribute them as communication endpoints among each other to achieve the highest possible connection robustness.  
This works automatically, unless there are networking devices (proxies, load balancers) in your environment, which should be taken into account, and of which Dynatrace is not aware.

The diagram below shows all possible proxy and load balancer (reverse proxy) placements for an ActiveGate deployment. For simplicity, direct connectionsâthose that are not through proxies or load balancersâare not shown in this diagram. Alternative connections (those that connect through one or more proxies or load balancers), are shown as dashed lines.

* If there is a load balancer between OneAgents and an ActiveGate, you should specify the load balancer's address as the [`dnsEntryPoint`](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Configure ActiveGate properties to set up a reverse proxy or a load balancer for OneAgent.") property in the ActiveGate configuration.
* If there is a load balancer between ActiveGate and the next communication endpoint that traffic should be routed through, configure [`seedServerUrl` and `ignoreClusterRuntimeInfo`](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Learn how to configure ActiveGate properties to set up a reverse proxy or a load balancer.")
* If a proxy is used to reach the Dynatrace Cluster or any of the monitored clouds, [configure a proxy](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy.").

![Proxy and load balancer placements for ActiveGate deployments](https://dt-cdn.net/images/proxy-rev-proxy-005-1018-c916f384ca.png)

Proxy and load balancer placements for ActiveGate deployments

## ActiveGate headers

You can configure the ActiveGate headers in your firewall.

| Header | Value |
| --- | --- |
| `User-Agent` | * Environment ActiveGate:  `ruxit/<dynatrace-version> <activegate-instance-id> <environment-id>`[1](#fn-1-1-def) * HTTP monitors:  `DynatraceSynthetic/<dynatrace-version>`[2](#fn-1-2-def) * Browser monitors:  `RuxitSynthetic/<dynatrace-version>`[3](#fn-1-3-def) |
| `dynatrace-gateway-type` | * Environment ActiveGate: `PRIVATE` * Managed or SaaS ActiveGate: `PUBLIC`  * Cluster ActiveGate: `PUBLIC_MANAGED`  * Multi-environment ActiveGate: `MULTI_TENANT` |
| `Authorization` | `Basic <TOKEN>` |

1

Example values:   
 **Environment and Multi-environment ActiveGate**: `ruxit/1.229.163.20211109-103203 0x37badd8e c04442b4-7ea6-4ec4-a5c4-7f94c7cf25fa`.   
 **Cluster ActiveGate**: `ruxit/1.229.163.20211109-103203 0x37badd8e`.

2

Example value:   
 `DynatraceSynthetic/1.258.0.20221207-142354`.

3

Example value:   
 `Mozilla/5.0 (Windows NT 6.3;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36 RuxitSynthetic/1.258.0.20221207-142354`.

## Related topics

* [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.")