---
title: Service-Level Objectives Classic
source: https://www.dynatrace.com/docs/deliver/service-level-objectives-classic
scraped: 2026-03-04T21:33:40.088795
---

# Service-Level Objectives Classic

# Service-Level Objectives Classic

* Classic
* Overview
* 1-min read
* Published Sep 14, 2020

Dynatrace comes with native support for [service-level objective (SLO)](service-level-objectives-classic/slo-basics.md "Basic terminology related to service-level objectives") monitoring according to [Site Reliability Engineering (SRE) fundamentals published by Googleï»¿](https://dt-url.net/cv030av).

## SLO overview

You can review the current health status, error budgets, target and warning, along with the timeframe of all your SLOs on the **SLOs** overview page.

## Define and configure

* You can [define SLOs based on preconfigured templates provided by Dynatrace or create and configure your own SLO definitions](service-level-objectives-classic/configure-and-monitor-slo.md#config "Create, configure, and monitor service-level objectives with Dynatrace."). For a better understanding of how to configure out-of-the-box SLOs, see [Example configuration of service-level objective definitions](service-level-objectives-classic/slo-definition-configuration-examples.md "Explore the out-of-the-box service-level objective definitions by way of examples.").
* You can [control access to the SLOs in your environment based on management-zone permissions](service-level-objectives-classic/slo-mz-permissions.md "Permissions required at the environment and management-zone level to manage service-level objectives.").

## Visualize

You can

* [Pin SLO tiles to your dashboard](service-level-objectives-classic/configure-and-monitor-slo.md#dash "Create, configure, and monitor service-level objectives with Dynatrace.") to visualize their current state along with the remaining error budgets.
* [Query and chart metrics in Data Explorer](service-level-objectives-classic/configure-and-monitor-slo.md#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
* Review a list of current SLOs on the [**Hosts**](../observe/infrastructure-observability/hosts/monitoring/host-monitoring.md#slo "Monitor hosts with Dynatrace."), **Services**, and [**Kubernetes workload**](../observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes.md "Keep track of SLOs for Kubernetes/OpenShift.") details pages.

## Alerting

You get [Davis support](service-level-objectives-classic/configure-and-monitor-slo.md#davis-support "Create, configure, and monitor service-level objectives with Dynatrace.") to determine SLO violations before software is in production and to provide root-cause analysis.