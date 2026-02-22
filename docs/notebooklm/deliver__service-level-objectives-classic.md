# Документация Dynatrace: deliver/service-level-objectives-classic
Язык: Русский (RU)
Сгенерировано: 2026-02-22
Файлов в разделе: 2
---

## deliver/service-level-objectives-classic/slo-mz-permissions.md

---
title: SLO management with management-zone permissions
source: https://www.dynatrace.com/docs/deliver/service-level-objectives-classic/slo-mz-permissions
scraped: 2026-02-22T21:29:38.365019
---

# SLO management with management-zone permissions

# SLO management with management-zone permissions

* Reference
* 3-min read
* Published Feb 16, 2022

You can control access to the SLOs in your environment by setting write and/or read permissions to users or user groups at the environment or management-zone level.
For details on how to set permissions, see [Role-based permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Permission checks are based only on the global entity selector.

## Read access based on permission levels

* At the environment level, a user with **View environment** permission can view any SLO. To manage group permissions, you can [create policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

  **Example policy:** `ALLOW settings:objects:read, settings:schemas:read WHERE settings:schemaId = "builtin:monitoring.slo";`
* On a management-zone level, a user with **View environment** permission can read all global SLOs and all SLOs belonging to the respective management zone.

  Currently, a policy can't be assigned on the management-zone level.

## Write access based on permission levels

* At the environment level, a user with **Change monitoring settings** permissions can create and update any SLO, including global SLOs without management zones specified. To manage group permissions, you can [create policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

  **Example policy:** `ALLOW settings:objects:read, settings:schemas:read, settings:objects:write WHERE settings:schemaId = "builtin:monitoring.slo";`.
* On a management-zone level, a user with **Change monitoring settings** permissions can create and update any SLO for the respective management zone, but can't create or update global SLOs.

## View and edit SLOs based on permission levels

The SLO evaluation takes into account both your selected management zone and the management zone from the entity selector.

* At the environment level

  + You can view, create, update, and delete SLOs. Specifying an entity selector in the SLO is optional.
* On a management-zone level

  + You can view all SLOs without entity selectors, or with entity selectors where a management zone isn't specified, but they will be evaluated against your selected management zone only.
  + You can view SLOs that have one of your management zones specified in the entity selector.
  + You can edit SLOs that have one of your management zones specified in the entity selector if you have write permissions on that specific management zone.
  + You can create new SLOs that state at least one management zone to which you have access in the entity selector.

## View and add SLO dashboard tiles based on permission levels

* You can add SLOs that are visible on the **Service-level objectives** page to your own classic dashboards by selecting **Pin to dashboard** in **Actions**.
* You can add newly created SLOs directly on the dashboard. The selection is filtered based on the SLOs visible in the selected management zone.
* Global SLOs (without entity selectors, or with entity selectors where management zone isn't specified) can be added when you filter for **All** in the management zone filter.
* You can't filter for SLO tiles. Depending on your access to the management zones of the SLO in a tile, for a selected management zone you can either access the tile or get an **N/A** result.
* If there's an SLO with a management zone for which you don't have access on a dashboard, the tile reads **Access denied**.

Starting with Dynatrace version 1.233+, you can also set a custom management zone for a specific tile, similar to the timeframe. In this case, the global management zone filter isn't relevant for the respective tile.

---

## deliver/service-level-objectives-classic.md

---
title: Service-Level Objectives Classic
source: https://www.dynatrace.com/docs/deliver/service-level-objectives-classic
scraped: 2026-02-20T21:16:46.439804
---

# Service-Level Objectives Classic

# Service-Level Objectives Classic

* Overview
* 1-min read
* Published Sep 14, 2020

Dynatrace comes with native support for [service-level objective (SLO)](/docs/deliver/service-level-objectives-classic/slo-basics "Basic terminology related to service-level objectives") monitoring according to [Site Reliability Engineering (SRE) fundamentals published by Googleï»¿](https://dt-url.net/cv030av).

## SLO overview

You can review the current health status, error budgets, target and warning, along with the timeframe of all your SLOs on the **SLOs** overview page.

## Define and configure

* You can [define SLOs based on preconfigured templates provided by Dynatrace or create and configure your own SLO definitions](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#config "Create, configure, and monitor service-level objectives with Dynatrace."). For a better understanding of how to configure out-of-the-box SLOs, see [Example configuration of service-level objective definitions](/docs/deliver/service-level-objectives-classic/slo-definition-configuration-examples "Explore the out-of-the-box service-level objective definitions by way of examples.").
* You can [control access to the SLOs in your environment based on management-zone permissions](/docs/deliver/service-level-objectives-classic/slo-mz-permissions "Permissions required at the environment and management-zone level to manage service-level objectives.").

## Visualize

You can

* [Pin SLO tiles to your dashboard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace.") to visualize their current state along with the remaining error budgets.
* [Query and chart metrics in Data Explorer](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
* Review a list of current SLOs on the [**Hosts**](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring#slo "Monitor hosts with Dynatrace."), **Services**, and [**Kubernetes workload**](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes "Keep track of SLOs for Kubernetes/OpenShift.") details pages.

## Alerting

You get [Davis support](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#davis-support "Create, configure, and monitor service-level objectives with Dynatrace.") to determine SLO violations before software is in production and to provide root-cause analysis.

---
