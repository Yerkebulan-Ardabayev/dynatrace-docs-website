---
title: Event topology extraction and mapping
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-topology/events-entity-extraction
scraped: 2026-02-16T21:27:52.251752
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

Name

ID

Description

Allow entity remapping

`dt.event.allow_entity_remapping`

Defines whether the remapping is allowed. Set to `"true"` to allow remapping to extracted entities.

If set to `"false"`, no remapping will happen, even if there's a matching extraction rule. However, if there **is** a matching rule, the extracted entity will still be created/updated. You can use such incoming events to keep your custom entities up-to-date.

Note that the values of the property must be of the `String` type.

Preferred entity type for remapping

`dt.event.preferred_entity_type`

Defines the generic entity type to which the event should be mapped. Use this property if your event metadata contains multiple entities of different types. If no entity of the specified type is extracted, no remapping is applied. If not set, Dynatrace Intelligence automatically decides on the appropriate entity type.

Entity identification

User-defined

Defines the ID of your entity. Since generic entities are user-defined, so is the ID of this property. As an illustration, for our [Easy Shipping LTD logistics example](/docs/ingest-from/extend-dynatrace/extend-topology#custom-topology-model-in-action "Ensure that all incoming observations are context-rich and analyzed in the context of the monitored entities they relate to."), this property could use the key **trucknr**.

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