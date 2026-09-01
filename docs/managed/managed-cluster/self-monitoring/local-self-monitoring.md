---
title: Local self-monitoring
source: https://docs.dynatrace.com/managed/managed-cluster/self-monitoring/local-self-monitoring
---

# Local self-monitoring

# Local self-monitoring

* Explanation
* 2-min read
* Updated on Aug 28, 2026

A Dynatrace Managed Cluster includes a dedicated local self-monitoring environment that collects internal deployment self-monitoring metrics. The local self-monitoring environment is a fully working Dynatrace environment. The self-monitoring environment includes all the self-monitoring metrics collected and aggregated from the other environments on your Dynatrace Managed Cluster. Dynatrace Managed stores all data exclusively on-premises.

No contribution to license consumption

* The self-monitoring environment doesn't count toward license consumption. Certain functionality is unavailable in this environment. For example, you can't connect OneAgents to the self-monitoring environment.
* The self-monitoring environment is available only for Dynatrace Managed customers using DDU licensing.

## Self-monitoring environment

You can navigate to the self-monitoring environment from the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user "Explore Dynatrace Managed, including navigation, browser requirements, timeframe selection, metric notation, and accessibility.") as you would to any other environment. The local self-monitoring environment has the name **Local-Self-Monitoring**. The self-monitoring environment also appears in the Cluster Management Console so you can assign user permissions to it.

## Explore self-monitoring metrics

For an overview of the currently implemented self-monitoring metrics, filter for metrics prefixed with `dsfm:` in the [metric browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."). The metric description provides details. You can use the self-monitoring environment to set up alerting or further dashboarding. Dynatrace protects this environment from deletion.

## Cluster deployment health and utilization dashboard

The dashboard Cluster health self-monitoring shows aggregated data for all environments in your Managed Cluster, including current utilization and an indicator of whether your Managed Cluster has sufficient capacity for the current load.

The Cluster deployment health and utilization dashboard provides:

* Insights into the current utilization of your Managed Cluster.
* An overview of the different data ingest channels and the current capture rate.
* An overview of the connected Dynatrace OneAgents.

The self-monitoring dashboard targets the self-monitoring environment of Dynatrace Managed Clusters.