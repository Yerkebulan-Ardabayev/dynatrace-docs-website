---
title: Filter classic metrics by management zone
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics-classic/metrics-mz
scraped: 2026-02-17T05:02:26.879277
---

# Filter classic metrics by management zone

# Filter classic metrics by management zone

* 4-min read
* Updated on Jul 12, 2023

You can filter metric data by [management zone](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") in two ways.

* First, you can set up [entity-based rules](#entity-based-rules) for a management zone to match metrics with an associated entity type.
* Second, you can set up [dimensional rules](#dimensional-rules) for a management zone to match metric series by metric or dimension keys.

The following sections discuss each method and any [security considerations](#security) of filtering metric data by management zone.

## Entity-based rules to filter metric data

You can define [UI-based](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules#ui "Define rules to limit the entities accessible within a management zone.") or [text-based rules](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules#text "Define rules to limit the entities accessible within a management zone.") to provide access to entities within a management zone. Management-zone users automatically get access to the metrics whose **entity type** matches the entities scoped within the management zone. Note that the entity type of a metric is the primary entity associated with that metric. While a metric can have several **entity-based dimensions**, these are not the same thing as the entity type.

### Metric entity type

You can check the entity type of a metric using:

* The metric information side panel in [Data Explorer](/docs/analyze-explore-automate/explorer#metric-name "Query for metrics and transform results to gain desired insights.").

  ![Metric entity type in Data Explorer](https://dt-cdn.net/images/data-explorer-entity-type-1122-6a93ade8f2.png)
* The [Metric browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").
* The [GET metric descriptor endpoint of the Metrics API](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API."); check the [`entityType` element](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor#response "View the descriptor of a metric via Metrics v2 API.").

Alternatively, you can explicitly configure the entity type for **ingested custom metrics** by setting the **Source entity type** on the [**Metric metadata** page](/docs/analyze-explore-automate/dashboards-classic/metrics-browser#configuration-ui "Browse metrics with the Dynatrace metrics browser.").

![Metric metadata modal with completed 'Source entity type' field.](https://dt-cdn.net/images/sourceentitytype-metricmetadata-1270-b154365f51.png)

### Limitations

There are two limitations of filtering metric data in management zones via entity-based rules.

1. Filtering metrics by entity-based rules only works for the **entity type** of a metric. A metric can have multiple **entity-based dimensions** like `dt.entity.host` and `dt.entity.disk`, but most metrics have only one entity type. Suppose an entity-based rule of a management zone refers to an entity that's not the entity type of a metric. In that case, the metric series won't be visible when the management zone is applied, even if an entity-based dimension of the metric does match the rule.

   For example, if your management-zone rule matches `QUEUE` entities starting with a given string, the metric `builtin:queue.incoming_requests` won't be visible in the management zone. This is because even though the metric has the `dt.entity.service` and `dt.entity.queue` entity-based dimensions, its entity type is `SERVICE`, which doesn't match the rule referring to `QUEUE` entities.
2. If a metric has **multiple entity types**, management-zone filtering isn't applied. This limitation impacts metrics with the dimensions `dt.entity.monitored_entity` or `dt.entity.device_application`.

## Dimensional rules for metric data

If a metric's entity type doesn't match the entity-based rule in a management zone, you can define a dimensional rule to match the metric's **entity-based dimension**. For example, for the `builtin:queue.incoming_requests` metric, you need to define a dimensional rule for the `dt.entity.queue` dimension. Note that the value of the dimension condition must be the entity ID (for example, `'dt.entity.queue' equals 'QUEUE-43717C10AF1BD1E0'`) and not the entity name (see the image below).

![Management-zone rule based on metric dimension name and value](https://dt-cdn.net/images/mz-metric-rule-dimension-key-condition-1823-6c1199e837.png)

## Security considerations

The following are the security considerations of metric data display and measures to mitigate the impact.

### Metric series visible in all management zones

Management-zone filtering doesn't work for metrics with multiple entity types. The following metrics are affected by this limitation.

* `builtin:billing.ddu.metrics.byEntity`
* `builtin:billing.ddu.metrics.byEntityRaw`
* `builtin:billing.ddu.log.byEntity`
* `builtin:billing.ddu.events.byEntity`
* `builtin:billing.ddu.serverless.byEntity`
* `builtin:billing.ddu.traces.byEntity`
* Multiple `builtin:apps.other.` metrics with the dimension `dt.entity.device_application`

Due to this limitation, users who shouldn't have access to these metric series can still access them regardless of management zone.

### Metric-selector transformations

The [metric-selector transformations](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") `parents` and `names` add information to metric data queries, which can expose the ID of the parent monitored entity (such as the ID of a host that is parent to a process) or the display name of the entity in the case of the `names` transformation.

### Impact

While these caveats are noteworthy, the practical security impact is limited. The data from the [metrics with multiple entity types](#multiple-entity-types) is typically not sensitive. For security-sensitive environments, we recommend taking the caveats regarding [metric-selector transformations](#metric-selector-transformations) (for example, entity IDs such as `HOST-27A71FA663E7F352` and the display of hostnames) into account when granting a user permission to read any metric data.

We recommend special care in deciding which dimensions are sent as part of the data for **security-sensitive custom metrics** to ensure that the desired read-access restrictions are effective.

## Related topics

* [Management zones](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")