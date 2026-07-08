---
title: Private self-monitoring
source: https://docs.dynatrace.com/managed/managed-cluster/self-monitoring/private-self-monitoring
---

# Private self-monitoring

# Private self-monitoring

* How-to guide
* 1-min read
* Updated on Jun 11, 2026

To keep full control over data residency and access, opt out of reporting self-monitoring data to Dynatrace and set up your own private self-monitoring environment.

If your data privacy requirements are strict, you can opt out at any time. Opting out stops sending self-monitoring data to Dynatrace.

Setting up your own self-monitoring environment requires installing OneAgent on your Managed Cluster nodes, which consumes Dynatrace licenses.

## Opt out of reporting self-monitoring data

To opt out of reporting Dynatrace Managed self-monitoring data, you need Managed Cluster administrator permissions.

1. Sign in to your Dynatrace Managed Cluster Management Console.
2. Go to **Settings** to display the Dynatrace Managed settings page.
3. Select **Preferences**.
4. Turn off **Dynatrace deployment health monitoring**.

Please contact a Dynatrace product expert via live chat within your environment. if this setting is turned off.

## Set up your own self-monitoring

Setting up your own self-monitoring gives you additional visibility into your Managed Cluster and makes it easier for Dynatrace product experts to troubleshoot issues. You can install OneAgents on your Managed Cluster nodes and Environment ActiveGates.

To retain high availability of your self-monitoring data, set up cross-cluster monitoring. For example, have a pre-production Managed Cluster monitor a production Managed Cluster, and vice versa. If one Managed Cluster goes down, you still have access to self-monitoring data to troubleshoot on your own or with Dynatrace support and services teams.

For advanced configuration of a self-monitoring environment, dashboards, alerting, and naming rules, contact the [Dynatrace ACE Services﻿](https://www.dynatrace.com/services-support/expert-services/) team.