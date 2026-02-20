---
title: Extend built-in unified analysis pages
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages
scraped: 2026-02-20T21:18:10.731741
---

# Extend built-in unified analysis pages

# Extend built-in unified analysis pages

* Reference
* 2-min read
* Published May 19, 2022

If your extension supplies additional data for a default entity with its own unified analysis page, you can extend the page using card injections. Examples of built-in unified analysis pages are the [host overview page](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.") or any unified analysis Kubernetes page. Card injections are available since Dynatrace version 1.233.

## Define card injection

The configuration of a card injection is similar to the configuration of the page layout itself with one significant modification: injected cards are ordered alphabetically by their key, which should use a well-specified key prefix. This ensures that unrelated data supplied by different extensions won't be mixed on a unified analysis page. Injections can be added under the `detailsInjections` and `listInjections` sections of the screen configuration.

```
detailsInjections:



- type: CHART_GROUP



key: my-host-feature-windows-only-chart



conditions:



- entityAttribute|osType=WINDOWS



- type: CHART_GROUP



key: my-host-feature-chart1



- type: CHART_GROUP



key: my-host-feature-chart2



- type: CHART_GROUP



key: my-host-feature-process-chart



entitySelectorTemplate: type(PROCESS_GROUP_INSTANCE), fromRelationships.isProcessOf($(entityConditions))



width: HALF_SIZE
```

The following options are available for a card supplied by your extension:

* `type`: Card type available to be supplied to a unified analysis page. Supported types include `CHART_GROUP`, `ENTITIES_LIST`, `EVENTS`, `LOGS`, and `MESSAGE`.
* `key`: Unique card key used to reference the desired card configuration. Use a well-specified key prefix to ensure that related cards are placed properly on a page. Cards are sorted alphabetically based on key.
* `entitySelectorTemplate`: An entity selector that is used to reference cards from another monitored entity type. For more information, see [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

  Details

  It can serve multiple purposesâselecting the entity where the chart will be displayed and filtering them based on certain rules or relating entities. It is used in conjunction with `entityType` to further refine which entities are applicable for the card. For example, if `entityType` is `HOST`, you can use `entitySelectorTemplate` to show the card only for hosts using a certain operating system.

  `$entityConditions` acts as a dynamic placeholder, adapting to the context in which the card appears. For example, when the card is displayed on a page dedicated to a specific host, `$entityConditions` will automatically adjust to conditions applicable to that host.

  For example, when the card with the following configuration is displayed on the host page.

  ```
  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf($(entityConditions))"
  ```

  The `$(entityConditions)` placeholder will be automatically replaced to point to the specific host entity.

  ```
  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf(type(HOST) AND entityId(HOST-<id>))"
  ```
* `width`: Determines how wide that card is in relation to the page width. Supported values are `HALF_SIZE` and `FULL_SIZE`.
* `conditions`: A list of conditions that need to be fulfilled for the card to be visible.

## Reference card injection

As a final step, you need to reference the card to be injected on a built-in unified analysis page with an Extensions 2.0 package and place it in your `extension.yaml` file in the `screens` section. In this example, we extend the built-in host overview page (`entityType: HOST`).

```
name: custom:com.ua.example.extension



version: 1.0.0



minDynatraceVersion: 1.233.0



author:



name: StackEnterprise



# Here comes your usual extension YAML content: data source, declarative metrics, topology, etc.



screens:



- entityType: HOST



detailsInjections:



- type: CHART_GROUP



key: my-host-feature-windows-only-chart



conditions:



- entityAttribute|osType=WINDOWS



- type: CHART_GROUP



key: my-host-feature-chart1



- type: CHART_GROUP



key: my-host-feature-chart2



- type: CHART_GROUP



key: my-host-feature-process-chart



entitySelectorTemplate: type(PROCESS_GROUP_INSTANCE), fromRelationships.isProcessOf($(entityConditions))



width: HALF_SIZE



chartsCards:



- key: my-host-feature-windows-only-chart



...



- key: my-host-feature-chart1



...



- key: my-host-feature-chart2



...



- entityType: PROCESS_GROUP_INSTANCE



chartsCards:



- key: my-host-feature-process-chart



...
```