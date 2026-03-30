---
title: "Service-Level Objectives"
source: https://docs.dynatrace.com/managed/deliver/service-level-objectives-classic
updated: 2026-02-09
---

* 1-min read

Dynatrace comes with native support for service-level objective (SLO) monitoring according to [Site Reliability Engineering (SRE) fundamentals published by Google](https://dt-url.net/cv030av).

## SLO overview

You can review the current health status, error budgets, target and warning, along with the timeframe of all your SLOs on the **SLOs** overview page.

## Define and configure

* You can define SLOs based on preconfigured templates provided by Dynatrace or create and configure your own SLO definitions. For a better understanding of how to configure out-of-the-box SLOs, see Example configuration of service-level objective definitions.
* You can control access to the SLOs in your environment based on management-zone permissions.

## Visualize

You can

* Pin SLO tiles to your dashboard to visualize their current state along with the remaining error budgets.
* Query and chart metrics in Data Explorer.
* Review a list of current SLOs on the **Hosts**, **Services**, and **Kubernetes workload** details pages.

## Alerting

You get Davis support to determine SLO violations before software is in production and to provide root-cause analysis.
