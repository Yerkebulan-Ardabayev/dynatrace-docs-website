---
title: Management-zone rules
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules
scraped: 2026-02-28T21:23:32.658070
---

# Management-zone rules

# Management-zone rules

* How-to guide
* 16-min read
* Updated on Oct 03, 2025

Management zones comprise one or more rules that define and limit the entities or dimensional data (such as logs and metrics) that can be accessed within the management zone.

When you select a management zone in **Settings** > **Preferences** > **Management zones**, all configured rules are displayed. You can **Disable/Enable** individual rules.

![Management zone rules](https://dt-cdn.net/images/mz-rules-1a-1227-bcb209a202.png)

Read more about:

* How log data can be ingested and automatically assigned to management zones in [Management zones and ingested log data (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.").
* How to [add a service-level objective to a management zone](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#mz "Create, configure, and monitor service-level objectives with Dynatrace.") so users with access to the management zone can view SLO status and error budget in the **Service-level objectives** page.

## Rule types

Management zones offer **UI-based rule definition** for:

* [Monitored entities](#ui)
* [Dimensional data (logs and metrics)](#logs-metrics)

You can select the type of rule, and then create rule conditions based on entity/data properties, operators, and values where relevant.

When creating rules for some entities, you can propagate access to related topological entities without creating an extra rule. See [How management-zone rules are applied](#rules-apply) below.

For UI-based rules for dimensional log and metric data, you can define conditions based on the log file name, metric keys and dimension keys and values. Built-in, calculated, and ingested metrics are supported.

More information on the Metrics API v2

Use the powerful [metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") of the [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") for metric and dimension keys and values:

* [GET a list of all available metrics](/docs/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.") in your environment.
* [GET the details of a specified metric](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") to check dimension keys.
* [GET a list of data points](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.") to check dimension values.

Note that users automatically get access to logs and metrics associated with entities that are included within their assigned management zones.

**[Text-based rules](#text)** leverage the powerful [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") for v2 Environment APIs to define entities. Text-based rules enable you to define entity access based on all the entity types, properties, values, and relationships exposed by the [Monitored entities API v2](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.").

There are several advantages of text-based rules.

* You can provide granular and focused entity definitions without having to review the subset of choices available in the UI.
* While UI-based rules allow for some relationship-based [propagation of entity access](#rules-apply), with text-based rules, you can explicitly use relationships to filter your entity selection. You have the flexibility to decide exactly which relationships you want to use to filter entities.
* You can define text-based rules for including your own custom entity types, attributes, and relationships in management zones.

Per monitoring environment, you can add:

* 5,000 management zones by default. For any questions, contact a Dynatrace product expert via live chat.
* 300 UI-based management-zone rules for entities (150 for Dynatrace versions 1.323 and earlier).
* 300 UI-based management-zone rules for dimensional data (150 for Dynatrace versions 1.323 and earlier).
* 300 text-based entity selector rules for management zones (150 for Dynatrace versions 1.323 and earlier).
* 100,000 conditions for all management-zone rules taken together (does not apply to [entity selector rules](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules#text "Define rules to limit the entities accessible within a management zone.")).
* Any individual entity to a maximum of 200 management zones (run the [GET an entity](/docs/dynatrace-api/environment-api/entity-v2/get-entity "View parameters of a monitored entity via Dynatrace API.") API call to see an entity's management zones).

Check our documentation on [how to optimize management-zone rule performance at scale](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.").

### Add a UI-based rule for entities

See [Examples](#examples) for different rule types and implementations.

1. [Select/create a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") and then select **Add a new rule**.
2. Select **Monitored entity** as the **Rule type**. (See also information on [rules for dimensional data](#logs-metrics) and [text-based rule definition](#text) via the **Entity selector**.)
3. Select the entity type to which the rule should apply (**Rule applies to**), for example, **Web applications**.

   ![Select an entity type](https://dt-cdn.net/images/mz-rules-entity-type-571-8a758524db.png)
4. Each entity can be defined and limited by several different conditions. Select **Add condition**.
5. Choose the condition **Property**, **Operator**, and **Value** (where relevant). For example, you can specify that the **Web application name begins with** a specified string. You can enter up to 80 characters; wildcard characters are not allowed; regular expressions are allowed in the **contains regex** and **does not contain regex** condition operators.
6. If you enter a text string, specify whether it is **Case sensitive**.

   ![Rule conditions](https://dt-cdn.net/images/mz-rules-3a-958-3a6e99d6a0.png)
7. For some entities, you can propagate access to related topological entities without creating an extra rule. For example, turn on the appropriate toggles to include underlying hosts and process groups when defining a management-zone rule for **Services**.

   ![Include related entities](https://dt-cdn.net/images/mz-rules-4a-879-f4b10ae36b.png)
8. Select **Add condition** to add another condition (or **Remove condition** to remove a condition) as required.

   * You need to define at least one condition per rule.
   * Conditions are applied using the `AND` logicâall conditions need to be met for the rule to apply to an entity.
   * There's no limit on the number of conditions per rule. However, there's a limit of 100,000 conditions for all rules taken together per environment.
9. Select **Preview** to see entities matching the rule that were active and online in the last 72 hours. Of course, when you actually apply the management zone, all entities matching the rules for the given timeframe will be displayed. Note that **Preview** is only available for entity-based rules.

   ![Rule preview](https://dt-cdn.net/images/mz-rules-5a-957-2b8d1b7d14.png)
10. **Save changes**.

### Add a UI-based rule for dimensional data

See [Examples](#examples) for different rule types and implementations.

1. [Select/create a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") and then select **Add a new rule**.
2. Select **Dimensional data** for **Rule type**. (See also information on [rules for entities](#ui) and [text-based rule definition](#text) via the **Entity selector**.)
3. Select the data **Type** to which the rule should apply.

   * For a UI-based rule for a built-in, calculated, or ingested metric, select **METRIC**.
   * For a UI-based rule for logs, select **LOG**.
4. Each rule can be defined and limited by several different conditions. Select **Add condition**.
5. Choose the condition **Type**, **Key** (where appropriate), **Operator**, and **Value**. You can enter up to 80 characters in any text field; wildcard characters are not allowed.

   Condition types are:

   * For a log attribute or metric dimension, **DIMENSION**.

     ![Log attribute or metric dimension condition](https://dt-cdn.net/images/mz-rules-data-dimension-580-3843630e79.png)
   * For a log filename, **LOG\_FILE\_NAME**. The log filename should match the attribute `log.source`.

     ![Log filename condition](https://dt-cdn.net/images/mz-rules-log-filename-580-7f89e2cbd4.png)
   * For a metric key, **METRIC\_KEY**.

     ![Metric key condition](https://dt-cdn.net/images/mz-rules-metric-key-580-fac4735560.png)
   * For a combined log or metric condition, **ANY**.

   Allowed operators are **begins with** and **equals**.
6. Select **Add condition** to add another condition (or **Remove condition** to remove a condition) as required.

   * You need to define at least one condition per rule.
   * Conditions are applied using the `AND` logicâall conditions need to be met for the rule to apply to an entity.
   * There's no limit on the number of conditions per rule. However, there's a limit of 100,000 conditions for all rules taken together per environment.
   * **Preview** is not available for dimensional-data rules.
7. **Save changes**.

### Add a text-based entity selector rule

1. [Select/create a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") and then select **Add a new rule**.
2. In **Rule type**, select **Entity selector**.
3. To fill out the **Entity Selector** text string, you might need to run [Monitored entities API v2 calls](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") to fetch entity types, properties, values, and relationships. Consult [entity selector documentation](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") for details on how to construct an entity definition. See [Examples](#examples) for different rule types and implementations.

   **Important parts of the entity selector string**

   * `type(<entityType>)` defines the type of entity that is subject to the rule. For example, the entity type for hosts is `host` and for process groups is `process_group`. The entity type is not case sensitive. You can only provide a single entry in `<entityType>`.

     Run the [GET all entity types](/docs/dynatrace-api/environment-api/entity-v2/get-all-entity-types "View all types of monitored entities in your environment via Dynatrace API.") API call for a list of all entity types in your environment (including custom entities) and their properties.

     Alternatively, you can specify multiple individual entity IDs with the `entityId` criterion. You can run the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") API call for a list of actual entities in your environment and their properties.
   * Entity properties and values filter the entity list that your rule applies to. For example:

     + `entityName.startsWith("Book")` filters for entities whose name starts with `Book`.
     + `serviceType(WEB_REQUEST_SERVICE)` filters for web request services.

     You can run the [GET entity type API call](/docs/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") for any entity type (for example, `service`) to get a list of all its properties (for example, `serviceType`). You can also run the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") API call for a list of actual entities in your environment with their property values (for example, `WEB_REQUEST_SERVICE`).
   * Relationships further refine entity selection by defining an entity in terms of its relationship to another. Relationships are of two kinds.

     + A `fromRelationship` implies that the direction of the relationship is **from the given entity** (that is, the entity being queried) to a related entity. When you query all the services that service A calls, this is a relationship âfrom (service A)â to other services.
     + A `toRelationship` implies that the direction of the relationship is from a related entity **to the given entity** (that is, the entity being queried). When you query all the services that call service A, this relationship is âto (service A).â

     You can run the [GET entity type API call](/docs/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") on any entity type to get a list of the entity's from/to relationships and the related entity types. You can also run the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") API call to get a list of the actual entities in your environment along with their relationship values (for example, a `service` entity type can have a `calls` "from relationship" to another `service`).
4. Select **Preview** to see entities matching the rule that were active and online in the last 72 hours. (Of course, when you actually apply the management zone, all entities matching the rules for the given timeframe will be displayed.)

   ![Entity-selector rule preview](https://dt-cdn.net/images/mz-rules-6a-998-ebeb2f11bd.png)
5. **Save changes**.

## How management-zone rules are applied

* Conditions are applied using the `AND` logicâall conditions within a rule need to be met for the rule to apply to an entity.
* Rules are applied using the `OR` logicâany rule must apply for an entity to be included in a management zone.
* When creating rules for some entities, you can propagate access to related topological entities without creating an extra rule. For example, when creating a rule for services, you can opt to add underlying hosts and process groups. See [Add a UI-based rule](#ui) above.

  In other cases, the propagation of access to related topological entities is implicit. For example, when you grant access to a host in a management zone, any custom metrics ingested via that host are also accessible within the management zone. Note that this does not automatically include all measurements of those custom metrics but only those measurements that were sent in for your host.

  In cases where such propagation isn't available, you need to explicitly create rules for the entities you wish to add to a management zone. For example, a management-zone rule that applies to **Host groups** does not automatically grant access to the hosts within those groups; you need to explicitly add rules for the **Hosts** you wish to include in the management zone, as shown in [Examples](#examples) below.

  Management zones are always implicitly propagated to the following related entities. However, this does not apply to entity selector based rules.
* When you add an entity using tags to a management zone as part of entity creation via API, there might be a delay in management-zone assignment depending on the number and complexity of your tagging rules. See [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.") for best practices to speed up the time taken to assign tags and management zones within your monitoring environments.
* You cannot define management-zone rules where the entity selector for one management zone filters by another management zone. Management zone predicates such as `mzID` or `mzName` are not allowed in entity selector strings. This means, for example, that you cannot define management zone A as containing hosts belonging to management zone B. Management-zone rules based on other management zones increase the number of runs made by the conditional decision engine and can greatly delay management-zone assignment. See also [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.") for related information.

  As a workaround, use the same entity selector string in both management zones. For example, consider that:

  + Management zone A has the rule `type(SERVICE),entityName.startsWith("myService"),tag("my:tag")`.
  + Management zone B is required to include services that call services in Management zone A. To do so, define the rule `type(SERVICE),fromRelationships.calls(type(SERVICE),entityName.startsWith("myService"),tag("my:tag"))`.

## Examples

Example 1: Management-zone rules providing access to hosts of specific host groups; users assigned to the zone can filter by accessible host groups.

1. Set up a rule for hosts.

   1. Select **Monitored entity** as the **Rule type**.
   2. Select **Hosts** as the entity that the **Rule applies to**.
   3. Add a condition.
   4. Select **Host group** as the **Property**.
   5. Select or search for a host group in the **Value** field.
   6. **Preview** the list of matching entities.

      ![Preview the rule for hosts](https://dt-cdn.net/images/mz-sample-1-1a-1026-c1e2a8cd09.png)
   7. **Save changes**.

   Add a rule in this way for each set of hosts per host group.
2. Set up a rule for host groups.

   In order for users to have visibility into host groups containing the hosts in the management zone, you need to set up host group rulesâone per host group you wish to include. This ensures that users can filter by the host groups on the **Hosts** page.

   1. Select **Monitored entity** as the **Rule type**.
   2. Choose **Host groups** as the entity that the **Rule applies to**.
   3. Add a condition.
   4. Select **Host group name** as the **Property**.
   5. Define the condition for the host group name, for example, a text string contained in the host group's name.
   6. **Preview** the list of matching host groups.

      ![Rule for a host group](https://dt-cdn.net/images/mz-sample-1-2a-1025-fd96aea449.png)
   7. **Save changes**.

   Add a rule in this way for each host group you wish to include in the management zone. Host group names are shown in the filter on the **Hosts** page only if a corresponding management-zone rule is defined for them. Generally, you would grant access to the same host groups that the hosts in your management zone belong to.

When the management zone is applied, the user can see only the assigned hosts and can filter the **Hosts** page by **Host group**. The host groups are those defined in your management-zone rules.

![Host groups filter](https://dt-cdn.net/images/mz-sample-1-3-1612-2b773ed1d7.png)

Example 2: Management-zone rules providing access to all synthetic monitors

Management-zone rules can be defined for three types of synthetic entities:

* Browser monitors
* HTTP monitors
* Third-party monitors

To provide access to all synthetic monitors, you need to define rules to cover all monitors per monitor type.

![Management zones: synthetic entities](https://dt-cdn.net/images/mz-sample-2-1a-823-7985b67d21.png)

To set up a rule to cover all **Browser monitors**, for example:

Specify that the **Browser monitor name exists**. **Preview** the rule to see the matching entities.

![Browser-monitor rule](https://dt-cdn.net/images/mz-sample-2-2a-1119-c1287aafd6.png)

Additionally, set up similar rules for HTTP and third-party monitors to cover all synthetic monitors in your environment.

If you'd like your user to be able to create or edit synthetic monitors in a management zone, you need to provide the **Manage monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the management-zone or environment level.

Example 3: Management-zone rules providing access to specific measurements of specific ingested metrics

You can provide access to an ingested metric, filtered by a dimension value so that only specific measurements of the given metric are accessible within the management zone (for charting and analysis, for example).

1. Select the **Dimensional data** entity of type **METRIC**.
2. Fill out the condition for the metric name (**METRIC\_KEY**). You can provide access to a specific metric by providing the entire name or a set of metrics by specifying the opening string (for example, `business.revenue`).

   ![Management-zone rule for custom metric name](https://dt-cdn.net/images/mz-sample-3-1-955-64a30c6239.png)
3. To filter for specific measurements of the metrics, you need to add a condition for the metric dimension. Select **DIMENSION** and provide the dimension name (**Key**) and (**Value**). For example, to filter your business metrics for the US eastern region, you would specify the dimension name `region` and value `useast`.

   ![Dimensional metric data in a management zone](https://dt-cdn.net/images/mz-sample-3-2-937-3087a6c4e0.png)
4. **Save changes**.

If your management zone already provides access to the host through which a custom metric and its measurements are ingested, you automatically provide access to that custom metric; you don't need to set up an explicit rule for the custom metric. Note that this doesnât include all measurements of that custom metric but only those measurements that were sent in for your host.

Example 4: Management-zone rules providing access to specific measurements of specific ingested logs

You can provide access to logs filtered by a log attribute value (as an alternative to filtering logs by entities).

1. Select **Dimensional data** in the **Rule type** field.
2. Select **LOG** in the **Type** field.
3. Add a condition for logs.

   1. Select **DIMENSION** for condition type.
   2. Provide the log attribute name in the **Key** field. You can list only one attribute value.
   3. Add the phrase to search for in the **Value** field.
   4. You can also set the **Operator** as `begins with` or `equals` for the **Value** entered. For example, to filter your logs for a specific Kubernetes deployment name, specify the `k8s.deployment.name` key and `begins with` `automation-server` as the value.
4. **Save changes**.

![Example management-zone rule for logs](https://dt-cdn.net/images/mz-log-example-726-67634de796.png)

If your management zone already provides access to the host through which logs are ingested, you automatically provide access to those logs. This means that you don't need to set up an explicit dimensional rule for such logs.

Example 5: Entity selector rule based on entity relationships

In order to filter for services that directly call a service with the name `JourneyService`, you can run the [GET all entity types](/docs/dynatrace-api/environment-api/entity-v2/get-all-entity-types "View all types of monitored entities in your environment via Dynatrace API.") API call to check the entity type and relationships for services.

From the information gathered, you can now construct an entity-selector rule for the entity type `service` that has a `calls` "from relationship" to the entity type `service` with the name `JourneyService`:

`type(SERVICE),fromRelationship.calls(type(SERVICE),entityName(JourneyService))`

This can also be written as `type(SERVICE),fromRelationship.calls(type(SERVICE) AND entityName.equals(JourneyService))`.

![Entity-selector rule based on relationships](https://dt-cdn.net/images/mz-sample-4-1-954-606bb32f43.png)

## Related topics

* [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")
* [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.")
* [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")
* [Metrics API - Metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.")
* [Management zones and ingested log data (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.")
* [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.")