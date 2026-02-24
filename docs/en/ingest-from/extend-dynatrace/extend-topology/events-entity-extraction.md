---
title: Event topology extraction and mapping
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-topology/events-entity-extraction
scraped: 2026-02-24T21:33:41.176253
---

# Event topology extraction and mapping

# Event topology extraction and mapping

* Latest Dynatrace
* 4-min read
* Updated on Jan 28, 2026

Every event stored in Dynatrace is mapped to a monitored entity that it impacts. Dynatrace Intelligence uses this topological knowledge in its automated root cause analysis. An example of a topological context is a CPU usage spike that is mapped to the host where it was observed. However, once you start ingestion of your own data sources into Dynatrace, out-of-the-box topological mapping might not be sufficient anymore: you might need to map events to your custom entities.

The [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") enables you to include metadata in events you're ingesting into Dynatrace. With such enrichment, you can include topological context in the event itself. Dynatrace can extract this information and map an incoming event to the entity it belongs to.

## Map to predefined entity types

To map an event to an entity of a predefined type, specify it in the **entitySelector** field. Note that you can map an event only to entities that have been active within the last 24 hours. If no entity matches your selector or the selector is omitted altogether, the event is mapped to the environment level. No additional configuration is needed. To learn the entity selector syntax, see [Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

## Map to generic entity types

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Define custom entity type**](#define-type)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Provide event metadata**](#configure-event-metadata)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Define extraction rules**](#extract-map)

### Step 1 Define custom entity type

You can map events only to entities of an existing custom-defined generic type. If you don't have the required type defined yet, create it. To learn how, see [**Define new entity type**](/docs/ingest-from/extend-dynatrace/extend-topology/custom-topology#define-new-entity-type "Learn how to create a custom topology model that's suited to your telemetry data.").

You can't extract entities of predefined types and re-map events to them.

### Step 2 Provide event metadata

To be able to extract generic entities from events, you need to provide the relevant information in the event configuration. The following elements of event properties control the feature. You can find descriptions on all event configuration fields in [**POST an event**](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.").

Show an example JSON

```
{



"eventType": "CUSTOM_ALERT",



"title": "Truck fuel low",



"timeout": 5,



"properties": {



"trucknr": "13",



"dt.event.allow_entity_remapping": "true",



"dt.event.preferred_entity_type": "logistics:truck"



}



}
```

### Step 3 Define extraction rules

To assign an extraction rule to a generic entity type

1. Go to **Settings** > **Topology model** > **Generic types**.
2. Expand the generic type to which you want to map your events.
3. Select **Add extraction rule**.
4. In the **Extracted ID pattern** field, specify the placeholder of the event property that holds the entity ID. For our Easy Shipping example, that would be `{trucknr}`.
5. Optional In the **Instance name pattern**, provide the human-friendly pattern for names of extracted entities. Use placeholders to automatically create unique names. For our Easy Shipping example, that could be `Truck {trucknr}`.
6. Select **Add source**.
7. Select **Events** as the data source type.
8. In the condition field, use the `$eq()` condition with the event type value. For our Easy Shipping example, that would be `$eq(CUSTOM_ALERT)`.
9. Save your changes.

## Troubleshooting

If the remapping fails, you can retrieve the diagnostic information on an event overview page or via the [**GET an event**](/docs/dynatrace-api/environment-api/events-v2/get-event "View parameters of an event via the Events API v2.") request. Look for the **Entity remapping failure information** (`dt.event.entity_remapping_failure_info`) field.

## Related topics

* [Root cause analysis concepts](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.")
* [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.")