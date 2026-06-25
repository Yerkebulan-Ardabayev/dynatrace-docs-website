---
title: Set up management zones
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones
scraped: 2026-05-12T11:54:10.993865
---

# Set up management zones

# Set up management zones

* How-to guide
* 2-min read
* Updated on Jan 29, 2023

Management zones are comprised of rules that define which entities and dimensional data (such as logs and metrics) can be accessed within each management zone. Management-zone rules (as well as [automatic tagging rules](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")) are based on the same powerful Dynatrace conditional decision engine. In combination with [user and group permissions](/managed/manage/identity-access-management/user-and-group-management "User and group management"), you can set up management zones to create multiple overlapping partitions in your environment to promote observability, collaboration, and security.

## Create a management zone

You can create up to 5,000 management zones by default in your Dynatrace monitoring environment. (For any questions, contact a Dynatrace product expert via live chat within your Dynatrace environment.)

1. Go to **Settings** > **Preferences** > **Management zones** (or select the **Management zones** settings page from search results).

   ![Management zones](https://dt-cdn.net/images/mz-settings-page-1609-53fa2b9df7.png)

   Management zones
2. Select **Add new management zone**.
3. Provide a **Management zone name** and **Description**.
4. Create [management-zone rules](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Define rules to limit the entities accessible within a management zone.") governing which entities and data are part of and accessible within the management zone. These rules for entities and dimensional data are based on two approaches: a UI-based approach and a text-based approach leveraging the powerful [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of the Environment API v2.

   ![Management zone rules](https://dt-cdn.net/images/mz-rules-1a-1227-bcb209a202.png)

   Management zone rules

   Select a rule (for example, **Web applications** in the image above) > **Preview entities** to see the **Matching entities**.

   Read more about:

   * How log data can be ingested and automatically assigned to management zones in [Management zones and ingested log data (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.").
   * How to [add a service-level objective to a management zone](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#mz "Create, configure, and monitor service-level objectives with Dynatrace.") so users with access to the management zone can view SLO status and error budget in the **Service-level objectives** page.

## Assign access rights to management zones

After you set up a management zone, define which user groups should have access to the management zone and at what level.

From the main menu of the Cluster Management Console, select **User authentication** > **User groups** > your user group to [assign permissions](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Learn about the supported permissions and policies, how you can assign them to groups, and how you can manage your users and groups.").

![Dynatrace Managed user groups](https://dt-cdn.net/images/dynatracemanagedusergroups-1903-5e1be74e08.png)

Dynatrace Managed user groups

See [Apply and use management zones](/managed/manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones "Apply management zones to organize your Dynatrace environment and control user access to specific data.") for details.

## Related topics

* [Management zones and ingested log data (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.")
* [Configure and monitor service-level objectives with Dynatrace](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo "Create, configure, and monitor service-level objectives with Dynatrace.")