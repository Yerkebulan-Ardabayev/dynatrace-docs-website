---
title: Get started with network zones
source: https://docs.dynatrace.com/managed/manage/network-zones/network-zones-basic-info
scraped: 2026-05-12T11:10:43.920108
---

# Get started with network zones

# Get started with network zones

* Tutorial
* 3-min read
* Updated on Dec 10, 2025

Network zones are Dynatrace entities that represent your network structure. They help you to route the traffic efficiently, avoiding unnecessary traffic across data centers and network regions.

### Without network zones

![Routing - without network zones](https://dt-cdn.net/images/routing-1-1-800-a92215b7e5.png)

Routing - without network zones

All of your OneAgents are able to reach all of your ActiveGates that are routing traffic to Dynatrace. If you decide to introduce a firewall that prevents some OneAgents to reach ActiveGates they've been using, it may produce unnecessary traffic.

Also, since every OneAgent can connect to any ActiveGate, it is possible that OneAgent is able to connect to an ActiveGate that is hosted in another region, so your traffic has to go around the world.

### With network zones

![Routing - with network zones](https://dt-cdn.net/images/routing-2-1-800-dcdfba1450.png)

Routing - with network zones

Network zones prevent inefficient connections by defining the ActiveGate that each OneAgent should use. You can still use ActiveGates in other zones as a [backup option](/managed/manage/network-zones/network-zones-basic-info#alternative "Learn how to get started with network zones.") in case primary ActiveGates becomes unavailable for some reason.

### Deploy network zones

Deployment of network zones depends on whether you're starting a new Dynatrace deployment (new installation scenario) or adding network zones to an existing deployment (migration scenario).

In either case, however, the overall steps are the same. Follow the steps from your scenario to start using network zones.

[#### Migration

Start using network zones in an existing Dynatrace environment.

* How-to guide

Read this guide](/managed/manage/network-zones/migration)[#### New installation

Start using network zones with a fresh Dynatrace installation.

* How-to guide

Read this guide](/managed/manage/network-zones/new-installation)

## Activate network zones

To activate network zones

1. Go to **Settings** and select **Preferences** > **Network zones**.
2. Turn on **Enable network zones in this environment**.

Alternatively you can use the [PUT global configuration](/managed/dynatrace-api/environment-api/network-zones/put-global-config "Edit the global network zones configuration via the Dynatrace API.") API call.

## Network zone organization

Network zones are organized per Managed cluster.

You can get an overview of network zones in [Cluster Management Console](/managed/managed-cluster/basics/managed-components#cluster-management-console "Understand the Dynatrace Managed architecture, including the Managed Cluster, the Cluster Management Console, and Mission Control.") or via [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.").

## Network zone naming

The name of a network zone is a string of alphanumeric characters. Additionally, you can use hyphens (`-`), and underscores (`_`). The length of the string is limited to 256 characters.

A dot (`.`) serves as a separator in the name of the network zone (see the **Naming pattern** section below). You can't use it for other purposes and the network zone must not start with a dot.

Network zone names are not case-sensitive. Dynatrace stores these names in lowercase.

There is a pre-created **default** network zone. OneAgents use it when no network zone is specified or the setting is reset. The name **default** is equal to an empty name.

### Naming pattern

To make it easier for you to use network zones, we recommend the following naming pattern:

```
provider.region.availability-zone.datacenter.tier
```

Use your company name as the `provider` part if you're using your own infrastructure.

You can add additional fields to this pattern.

## Alternative network zone

For each network zone, you can configure one or more alternative zonesânetwork zones that OneAgents should use when no ActiveGate from the primary zone is available. Make sure that ActiveGates from an alternative network zone are reachable by OneAgents of the primary network zone.

To configure alternative network zones

1. Go to **Deployment Status** and select **Network zones**.
2. Select the network zone you want to configure and the select **Edit** in the upper-right corner of the page.
3. Select the required network zones.

Alternatively, you can use the [PUT a network zone](/managed/dynatrace-api/environment-api/network-zones/put-network-zone "Update a network zone via the Dynatrace API.") call of the Environment API to configure the list of alternative zones.

## Fallback mode

Fallback mode determines how the network handles traffic if no ActiveGates are available in this network zone and there are no alternative network zones.

Available fallback modes:

* **Any ActiveGate (default)**: Traffic is routed to any available ActiveGate if the primary network zone is not accessible.
* **Only DefaultZone**: Traffic is directed only to the default network zone.
* **None (drop traffic)**: Traffic is discarded if the primary network zone is unavailable.

### Configure fallback mode

1. Go to **Deployment Status** and select **Network zones**.
2. Choose the network zone for which you want to set the fallback mode.

   Note that the default network zone is not configurable.
3. Select **Edit**.
4. In the **Fallback mode** section, select a fallback mode from the list.
5. Select **Save changes**.

## Limitations

The maximum number of network zones per environment is 10,000 by default. If you need more, contact a Dynatrace product expert via live chat within your Dynatrace environment.

## Related topics

* [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.")