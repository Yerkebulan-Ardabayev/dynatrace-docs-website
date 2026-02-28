---
title: Supported connectivity schemes for ActiveGates
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates
scraped: 2026-02-28T21:18:44.704416
---

# Supported connectivity schemes for ActiveGates

# Supported connectivity schemes for ActiveGates

* Latest Dynatrace
* 4-min read
* Published Jul 17, 2018

Dynatrace requires certain ports and paths to be opened and accessible through the monitored infrastructure, firewalls and other components. The ports are [configurable](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#com-compuware-apm-webserver "Learn which ActiveGate properties you can configure based on your needs and requirements.") and the default values are shown here.

## Dynatrace SaaS connectivity scheme

All possible connections for the SaaS connectivity scheme, with preferred and alternative paths are shown below.

The **solid arrows** indicate the preferred paths. For example, OneAgent will connect to an Environment ActiveGate, if one is present. It will, however, connect to a the Dynatrace Saas Cluster directly, if no connection to an Environment ActiveGate is possible.
The **direction of arrows** in the diagrams indicates which component initiates the connection.

![Dynatrace SaaS connectivity scheme](https://dt-cdn.net/images/connectivity-saas-003-1200-822497778d.png)

## Port usage

* Environment ActiveGate receives connections on port 9999.

* Dynatrace SaaS Cluster receives connections on port 443.

If you run [Browser monitors](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") or [HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.") from private Synthetic locations, you need to make sure the Synthetic-enabled ActiveGate has access to the tested resource. If you use ActiveGate extensions, you need to make sure the ActiveGate executing the extensions has access to the monitored technology.

Connection

**[Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.")** configuration means that OneAgents will prefer to communicate with ActiveGates from the same zone, before connecting to ActiveGates outside of the active zone.

## Proxy and load balancer configuration

All Dynatrace components (OneAgents, ActiveGates, Dynatrace Cluster) detect their hostnames and distribute them as communication endpoints among each other to achieve the highest possible connection robustness.  
This works automatically, unless there are networking devices (proxies, load balancers) in your environment, which should be taken into account, and of which Dynatrace is not aware.

The diagram below shows all possible proxy and load balancer (reverse proxy) placements for an ActiveGate deployment. For simplicity, direct connectionsâthose that are not through proxies or load balancersâare not shown in this diagram. Alternative connections (those that connect through one or more proxies or load balancers), are shown as dashed lines.

* If there is a load balancer between OneAgents and an ActiveGate, you should specify the load balancer's address as the [`dnsEntryPoint`](/docs/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Configure ActiveGate properties to set up a reverse proxy or a load balancer for OneAgent.") property in the ActiveGate configuration.
* If there is a load balancer between ActiveGate and the next communication endpoint that traffic should be routed through, configure [`seedServerUrl` and `ignoreClusterRuntimeInfo`](/docs/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Learn how to configure ActiveGate properties to set up a reverse proxy or a load balancer.")
* If a proxy is used to reach the Dynatrace Cluster or any of the monitored clouds, [configure a proxy](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy.").

![Proxy and load balancer placements for ActiveGate deployments](https://dt-cdn.net/images/proxy-rev-proxy-005-1018-c916f384ca.png)

## ActiveGate headers

You can configure the ActiveGate headers in your firewall.

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

* [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.")