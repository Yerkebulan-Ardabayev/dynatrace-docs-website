---
title: Analyze network for network zones deployment (migration)
source: https://docs.dynatrace.com/managed/manage/network-zones/migration/analyze
---

# Analyze network for network zones deployment (migration)

# Analyze network for network zones deployment (migration)

* 1-min read
* Published Jan 28, 2020

Follow the steps below to analyze your network in preparation for network zones deployment.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Take a look at your network**](/managed/manage/network-zones/migration/analyze#step-1 "Find out how to analyze your network in preparation for network zones deployment.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Structure the network into zones**](/managed/manage/network-zones/migration/analyze#step-2 "Find out how to analyze your network in preparation for network zones deployment.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Name the network zones**](/managed/manage/network-zones/migration/analyze#step-3 "Find out how to analyze your network in preparation for network zones deployment.")

## Step 1 Take a look at your network

Check the documentation of your network. Typically, networks are documented in:

* Configuration management database (CMDB )
* Network diagrams

## Step 2 Structure the network into zones

Just one rule here. Every zone there must have at least one ActiveGate accessible by any OneAgent or zRemote of this zone (with no firewall between that ActiveGate and the OneAgents and zRemotes).

## Step 3 Name the network zones

Give names to your network zones. For more information, see [Network zones naming](/managed/manage/network-zones/network-zones-basic-info#naming "Learn how to get started with network zones.").