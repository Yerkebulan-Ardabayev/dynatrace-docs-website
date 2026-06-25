---
title: Apply and use management zones
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones
scraped: 2026-05-12T12:05:02.759422
---

# Apply and use management zones

# Apply and use management zones

* How-to guide
* 4-min read
* Updated on Aug 20, 2025

After [setting up management zones](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones."), you can [assign them to user groups](#apply) and provide the required management zoneâlevel permissions. Members of those groups can then [filter their environments based on their assigned management zones](#filter) assigned to them. You can also [use management zones to set up maintenance windows](#mw).

## Apply a management zone

These high-level steps take you through the process of assigning a management zone to a user via group settings.

1. [Set up a management zone](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") (**Settings** > **Preferences** > **Management zones**) or check the management zone name and [rules](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Define rules to limit the entities accessible within a management zone.") defining which entities and data is accessible within the zone.
2. In the Cluster Management Console, go to **User authentication** > **User groups**.
3. Create or select a group to which you want to add the user.

   Assign the group the required environment-level and management zoneâlevel [permissions](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Learn about the supported permissions and policies, how you can assign them to groups, and how you can manage your users and groups.") that you'd like the user to have over the entities accessible within the management zone. For example, if you want your user to create or edit synthetic monitors in a management zone, you need to provide the **Manage monitoring settings** permission at the management zone or environment level.
4. Check that your user has **ACTIVE** status.
5. Assign the group (with access to the management zone) from the step above to the user.

When the user logs in to the environment, they can use the **Filter** button  in the menu bar to access the management zones they are assigned to.

## Filter by a management zone

Management zones are accessible as filters (via the **Filter** button  in the menu bar) to all users who are assigned to those management zonesâselect the appropriate management zone from the list.

![Filter by management zones](https://dt-cdn.net/images/mz-filter-2560-89a3233cbf.png)

Filter by management zones

Management zone filters apply to all views that display multiple entities, including individual [dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic."), list pages (for example, for hosts, process groups, services, synthetic monitors, applications, and [SLOs](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#mz "Create, configure, and monitor service-level objectives with Dynatrace."), [Logs](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones."), [Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment."), and the Technologies page. This enables each user to view only those entities that are relevant to them.

Note that there might be a delay in assigned entities appearing within management zones when such entities are created and assigned using tags via API. See [Best practices for scaling tagging and management-zone rules](/managed/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.") for tips on optimizing tagging and speeding up the management-zone assignment process.

From within a management zone, you can only see the entities you have access to in Dynatrace. No data is displayed on pages where you don't have access to entities.

You can see [**Dashboards**](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.") created by others and create your own for the entities you have access to.

Note that viewing [Real User Monitoring (RUM)](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") data requires the **View environment** [environment-level permission](/managed/manage/identity-access-management/permission-management/role-based-permissions#permissions "Role-based permissions").

## Management zones and maintenance windows

You can [define maintenance windows that are filtered by management zones](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window#scope "Create maintenance windows and define their scope.")âentities matching the management zones are considered to be under maintenance.