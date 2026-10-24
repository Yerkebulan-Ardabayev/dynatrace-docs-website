---
title: Management zones (Dynatrace Classic)
source: https://docs.dynatrace.com/managed/manage/identity-access-management-classic/permission-management/management-zones
---

# Management zones (Dynatrace Classic)

# Management zones (Dynatrace Classic)

* Reference
* 2-min read
* Published Sep 25, 2018

Management zones are a powerful information-partitioning mechanism that promotes focus on specific parts of your observed topology and the sharing of relevant team-specific data while simultaneously ensuring access control.

Each customizable management zone comprises a set of monitored entities or dimensional data (such as logs and metrics) in your environment, be it hosts that share a common purpose, [log data pertaining to specific hosts](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones."), a specific application, [SLOs for an application](/managed/analyze-explore-automate/service-level-objectives-classic/configure-and-monitor-slo#mz "Create, configure, and monitor service-level objectives with Dynatrace."), a staging environment, or the services of a certain technology. Entities are readied and grouped for inclusion in management zones or for [automatic tagging](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.") by Dynatrace conditional processing.

Management zones may overlap, just as team responsibilities might overlap. Users may be granted access to entire environments, a specific management zone, or a subset of related management zones. Dynatrace users see auto-filtered views of their environment based on the management zones that they can access. Users who have access to multiple management zones can focus on any particular management zone and filter all Dynatrace views so that they only see the metrics that are related to the entities of that particular management zone.

The [Problems page](/managed/dynatrace-intelligence/root-cause-analysis/concepts "Learn the core Davis AI root cause analysis concepts, including incidents, problems, fault tree analysis, impact analysis, and the problem lifecycle.") is also filtered based on the selected management zone—only those problems that affect entities in the currently selected management zone are included. However, when a problem spans multiple management zones, users see a full end-to-end view of the problem, but can only analyze the details of the hosts, processes, services, and applications that they have permission to view within their assigned management zones. This ensures productive and effective collaboration while still enforcing rigid access restrictions where it matters.

### Basics

* [Set up management zones (Dynatrace Classic)](/managed/manage/identity-access-management-classic/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.")
* [Management-zone rules (Dynatrace Classic)](/managed/manage/identity-access-management-classic/permission-management/management-zones/management-zone-rules "Define management-zone rules to control access to monitored entities, logs, and metrics using entity conditions, dimensional data, and entity selectors.")
* [Apply and use management zones (Dynatrace Classic)](/managed/manage/identity-access-management-classic/permission-management/management-zones/apply-and-use-management-zones "Apply management zones to organize your Dynatrace environment and control user access to specific data.")

### Additional

* [Management zones and ingested log data](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.")
* [SLOs and management zones](/managed/analyze-explore-automate/service-level-objectives-classic/configure-and-monitor-slo#mz "Create, configure, and monitor service-level objectives with Dynatrace.")
* [Best practices for scaling management-zone rules](/managed/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.")
* [Management-zone security and metrics](/managed/analyze-explore-automate/metrics-classic/metrics-mz "How to filter metrics by management zone and related security considerations")
* [Queue tags and management zones](/managed/observe/infrastructure-observability/queues/configuration/tags-and-management-zones "Automatically apply tags to queues and organize them into management zones.")
* [Define maintenance windows filtered by management zones](/managed/analyze-explore-automate/alerting-and-notifications-classic/maintenance-windows/define-maintenance-window#scope "Create maintenance windows and define their scope.")

## Related topics

* [Management zones﻿](https://www.dynatrace.com/platform/management-zones/)