---
title: Management zones
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/management-zones
---

# Management zones

# Management zones

* Reference
* 2-min read
* Published Sep 25, 2018

Management zones are a powerful information-partitioning mechanism that promotes focus on specific parts of your observed topology and the sharing of relevant team-specific data while simultaneously ensuring access control.

Each customizable management zone comprises a set of monitored entities or dimensional data (such as logs and metrics) in your environment, be it hosts that share a common purpose, [log data pertaining to specific hosts](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones."), a specific application, [SLOs for an application](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#mz "Create, configure, and monitor service-level objectives with Dynatrace."), a staging environment, or the services of a certain technology. Entities are readied and grouped for inclusion in management zones or for [automatic tagging](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") by Dynatrace conditional processing.

Management zones may overlap, just as team responsibilities might overlap. Users may be granted access to entire environments, a specific management zone, or a subset of related management zones. Dynatrace users see auto-filtered views of their environment based on the management zones that they can access. Users who have access to multiple management zones can focus on any particular management zone and filter all Dynatrace views so that they only see the metrics that are related to the entities of that particular management zone.

The [Problems page](/managed/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") is also filtered based on the selected management zone—only those problems that affect entities in the currently selected management zone are included. However, when a problem spans multiple management zones, users see a full end-to-end view of the problem, but can only analyze the details of the hosts, processes, services, and applications that they have permission to view within their assigned management zones. This ensures productive and effective collaboration while still enforcing rigid access restrictions where it matters.

### Basics

* [Set up management zones](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.")
* [Management-zone rules](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Define rules to limit the entities accessible within a management zone.")
* [Apply and use management zones](/managed/manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones "Apply management zones to organize your Dynatrace environment and control user access to specific data.")

### Additional

* [Management zones and ingested log data](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.")
* [SLOs and management zones](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#mz "Create, configure, and monitor service-level objectives with Dynatrace.")
* [Best practices for scaling management-zone rules](/managed/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.")
* [Management-zone security and metrics](/managed/analyze-explore-automate/metrics-classic/metrics-mz "How to filter metrics by management zone and related security considerations")
* [Queue tags and management zones](/managed/observe/infrastructure-observability/queues/configuration/tags-and-management-zones "Automatically apply tags to queues and organize them into management zones.")
* [Define maintenance windows filtered by management zones](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window#scope "Create maintenance windows and define their scope.")

## Related topics

* [Management zones﻿](https://www.dynatrace.com/platform/management-zones/)