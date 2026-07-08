---
title: How to define a maintenance window
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window
---

# How to define a maintenance window

# How to define a maintenance window

* 7-min read
* Updated on Jan 12, 2026

Dynatrace provides two methods for defining maintenance windows

* Configuration API
* Dynatrace web UI

You can have up to 2000 maintenance windows per monitoring environment. This limit applies to all maintenance windows regardless of state.

This page describes the UI-based approach. For the API reference, see [Maintenance windows API](/managed/dynatrace-api/configuration-api/maintenance-windows-api/post-mw "Create a maintenance window via the Dynatrace API.").

Each maintenance window you configure has a name and description that you can use to provide contextual information about the purpose of the maintenance window.

To define a maintenance window

1. Go to **Settings** > **Maintenance windows** > **Monitoring, alerting, and availability**.
2. Select **Create maintenance window**.
3. Define a **Name** for the maintenance window.
4. Optional Provide a **Description** of the purpose of the maintenance window.
5. From the **Maintenance type** list, select [**Planned** or **Unplanned**](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows#mw-types "Understand when to use a maintenance window. Read about the supported maintenance window types.").
6. Use the fields provided to define a recurrence schedule (one-time, daily, weekly, or monthly), the recurrence timeframe, and the time zone.
7. From the **Problem detection and alerting** list, specify what Dynatrace should do if a monitored component experiences a problem during the maintenance window:

   * **Detect problems and alert**: Dynatrace automatically detects and reports all problems as usual and displays a maintenance window icon on each problem that is detected during the maintenance window.
   * **Detect problems but don't alert**: Dynatrace detects problems but does not send out alerts for them. Each problem is listed on the **Problems** page with a maintenance window icon.
   * **Disable problem detection**: Dynatrace does not detect problems or send out alerts for them. Problems that occur during scheduled maintenance windows are not included on the **Problems** page and no alerts are sent out.
8. Optional **[Disable synthetic monitor execution](#disable-synthetic)** during the maintenance window.
9. If necessary, [define the scope of the new maintenance window](#scope). Otherwise, it applies to the entire environment.

When a maintenance window is created, it is enabled by default. You can disable or delete it from the **Maintenance windows** settings page.

![Maintenance windows page](https://dt-cdn.net/images/mw-disabled-1296-31c1f5c264.png)

Maintenance windows page

[Maintenance windows may be excluded from Synthetic Monitoring availability calculations](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Understand Synthetic Monitoring Classic metric calculations.") by applying a global setting.

## Disable synthetic monitor execution

You can opt to **Disable synthetic monitor execution** during a maintenance window. During the maintenance window, HTTP and browser monitors within the [scope of the maintenance window](#scope) are not executed.

To disable synthetic monitor execution during a maintenance window, the synthetic monitors must be within the [scope of the maintenance window](#scope). Execution will only be disabled for the subset of synthetic monitors included within the maintenance window.

Note that any browser and HTTP monitors associated with services and web, mobile, and custom applications included within the scope of the maintenance window are also not executed.

In the example below, the following synthetic monitoring entities explicitly added to the maintenance window are disabled:

1. A specific HTTP monitor, `VSP - Test`
2. All browser monitors (**Synthetic monitor** entity type)

![Synthetic monitors explicitly scoped within a maintenance window](https://dt-cdn.net/images/mw-synthetic-scope-1295-bd6a846c8e.png)

Synthetic monitors explicitly scoped within a maintenance window

However, if you define a maintenance window with a single filter for the `easyTravel` application (shown in the image below), any browser and HTTP monitors associated with that application are disabled, even though they are not explicitly scoped within the maintenance window.

![Single application scoped within a maintenance window](https://dt-cdn.net/images/mw-scope-single-app-916-5e34f43682.png)

Single application scoped within a maintenance window

## Define the scope of a maintenance window

By default, a maintenance window applies to your entire environment. You can narrow down the scope of a maintenance window to specific monitored entities while leaving everything else unaffected.

You define maintenance-window scope by specifying one or more **Filters** (**Add filter**).

**Each filter is applied separately**, that is, an entity matching any filter is added to the maintenance window. If you add a filter for browser monitors tagged `easytravel` and `frontend` and another for HTTP monitors tagged `easytravel-api`, your maintenance window will include browser monitors with both the tags `easytravel` and `frontend` as well as HTTP monitors with the tag `easytravel-api`.

You can define a filter by providing a value for one or more conditions. An entity must **match all conditions defined within a filter** to be scoped within the maintenance window.

* You can specify an **Entity type**—select the entity type from the autocomplete suggestions that appear as you type. You can add only one **Entity type** per filter.

  ![Entity type](https://dt-cdn.net/images/mwentitytype-543-a791cec214.png)

  Entity type

  If you don't add any other conditions, all entities of the specified type are matched to the maintenance window. You can narrow this scope by adding conditions via **Entity tags** or **Management zones**.
* You can limit the filter to a specific **Entity**—select the entity type and then select the entity from the provided list of entity names and IDs. You can add only one **Entity** by entity ID per filter.

  ![Entity ID and name](https://dt-cdn.net/images/mwentityid-632-84f181ea10.png)

  Entity ID and name
* Specify one or more **Entity tags** as key-value pairs (**Add tag**). You can also specify an optional entity type. You can specify more than one tag—entities need to match **all** tags in order to be included within the maintenance window.

  **Note**: Entity tags are case-sensitive.

  ![Tag condition for maintenance windows](https://dt-cdn.net/images/mw-tags-398-ed1877ed40.png)

  Tag condition for maintenance windows
* Specify one or more **Management zones** (**Add item** > select a [management zone](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") from the list provided). You can specify more than one management zone—entities need to match **all** management zones in order to be included within the maintenance window.

  There are monitored entities in Dynatrace (such as the **Disk** entity type) that don't support management zones. When you add such an entity to a maintenance window and specify a management-zone condition, the management zone of the parent entity is used instead. So if you add the **Disk** entity type to a maintenance window and specify a management zone, all disks from hosts belonging to that management zone are matched to the maintenance window. If there's no parent management zone, the monitored entity is matched to the maintenance window only if no management zone is specified.

### Parent and group relationships

In determining the scope of a maintenance window, Dynatrace considers entity parent and group relationships.

If a **parent** entity is scoped within a maintenance window, its **immediate** children are considered to be under maintenance as well. For example, if a maintenance window is configured for a host, all its disks are considered to be under maintenance as well. If a problem is raised on a disk, and the parent host is under maintenance, the affected child disk is considered to be under maintenance as well.

If an entity **group** is scoped within a maintenance window, its **immediate** members are considered to be under maintenance as well. For example, if a host group falls within a maintenance window, its member hosts are considered to be under maintenance as well. However, the child disks of the parent hosts are not considered to be under maintenance, unless, of course, the hosts are explicitly scoped within the maintenance window.

### Best practices and guidelines

Filters are applied separately, and within each filter, an entity needs to meet **all** conditions to be scoped within a maintenance window.

* If you specify an **Entity type** and no other conditions, all entities of that type are added to the maintenance window.
* Create a separate filter for each entity type you wish to add to the maintenance window. (If you create a filter where you add one **Entity type** and one tag that's always applied to another entity type, no entities will match the maintenance window.)
* If you wish to add an entity by ID to a filter, do not specify any other conditions as this might result in no entity being matched to the maintenance window.
* To add all entities with a given tag to the maintenance window, set up the filter with a single tag condition; do not specify any other conditions. Set up a separate filter for each such tag you wish to add to the maintenance window.
* To add all entities within a given management zone to a maintenance window, set up the filter with a single management-zone condition; do not specify any other conditions. Set up a separate filter for each such management zone you wish to add to the maintenance window.