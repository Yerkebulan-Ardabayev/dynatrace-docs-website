---
title: Monitor service-level objectives in Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes
scraped: 2026-02-16T09:29:39.866551
---

# Monitor service-level objectives in Kubernetes/OpenShift

# Monitor service-level objectives in Kubernetes/OpenShift

* 2-min read
* Published Jan 19, 2023

You can keep track of current [service-level objectives](/docs/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.") related to a Kubernetes/OpenShift workload on the **Kubernetes workload** details pages.

* Select **SLOs** on the notifications bar to display the **Service-level objectives** panel, which lists SLOs that are directly or indirectly connected to the workload.

## Directly connected SLOs

* An SLO is directly connected to a workload when the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO meets the following criteria:

  + The entity type is set to `"CLOUD_APPLICATION"`.
  + The entity ID is set to the workload ID.
* To see only SLOs that are directly connected to the workload, make sure that **Show only directly connected SLOs** is turned on.

## Indirectly connected SLOs

* An SLO isn't directly connected to a workload when, in the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO, no entity ID is provided.

  Example: When generic values such as `type("CLOUD_APPLICATION"),tag("slo")` are provided, the query results in all SLOs for all workloads, including the current workload.
* To see SLOs that are not directly connected to the workload, turn off **Show only directly connected SLOs**.

## Options

* Select **Details** to view a chart of the respective SLO metrics.
* In **Actions**, select

  + **View in Data Explorer** to [see SLO metrics in Data Explorer](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard** to [pin the SLO to your dashboard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace."). For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").
  + **SLO definition** to edit the SLO in **Service-level objective definitions**.
  + **Clone** to [clone the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert** to [create an alert for the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

## No SLOs

If no SLOs are found, you can

* Select a different timeframe in the upper-right corner.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)
* Select **Add SLO** to create an SLO in the [SLO wizard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

## Example SLO panel

![slo-card-workloads](https://dt-cdn.net/images/slo-card-754-ec31947bef.png)

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")