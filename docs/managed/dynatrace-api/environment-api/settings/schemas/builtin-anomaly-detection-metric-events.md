---
title: Settings API - Metric events schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-metric-events
scraped: 2026-05-12T11:49:26.446943
---

# Settings API - Metric events schema table

# Settings API - Metric events schema table

* Published Dec 05, 2023

### Metric events (`builtin:anomaly-detection.metric-events)`

Metric event configurations are used to automatically detect anomalies in metric timeseries by using thresholds or baselines.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.metric-events` | * `group:anomaly-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.metric-events` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.metric-events` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.metric-events` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Summary `summary` | text | The textual summary of the metric event entry | Required |
| Query definition `queryDefinition` | [QueryDefinition](#QueryDefinition) | - | Required |
| Monitoring strategy `modelProperties` | [ModelProperties](#ModelProperties) | - | Required |
| Event template `eventTemplate` | [EventTemplate](#EventTemplate) | - | Required |
| Dimension key of entity for events `eventEntityDimensionKey` | text | Controls the preferred entity type used for triggered events. | Optional |
| Config id `legacyId` | text | - | Optional |

##### The `QueryDefinition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Type `type` | enum | The element has these enums * `METRIC_KEY` * `METRIC_SELECTOR` | Required |
| Metric selector `metricSelector` | text | To learn more, visit [Metric Selectorï»¿](https://dt-url.net/metselad) | Required |
| Metric key `metricKey` | text | - | Required |
| Aggregation `aggregation` | enum | The element has these enums * `MIN` * `MAX` * `SUM` * `COUNT` * `AVG` * `VALUE` * `MEDIAN` * `PERCENTILE90` | Required |
| Management zone `managementZone` | text | - | Optional |
| Query offset `queryOffset` | integer | Minute offset of sliding evaluation window for metrics with latency | Optional |
| Entities `entityFilter` | [EntityFilter](#EntityFilter) | Use rule-based filters to define the scope this event monitors. | Required |
| Dimension filter `dimensionFilter` | [DimensionFilter](#DimensionFilter)[] | - | Required |

##### The `ModelProperties` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Model type `type` | enum | Metric-key-based query definitions only support static thresholds. The element has these enums * `STATIC_THRESHOLD` * `AUTO_ADAPTIVE_THRESHOLD` * `SEASONAL_BASELINE` | Required |
| Threshold `threshold` | float | Raise an event if this value is violated | Required |
| Alert on missing data `alertOnNoData` | boolean | The ability to set an alert on missing data in a metric. When enabled, missing data samples will be treated as violating samples defined in the advanced model properties. When disabled, missing data is not treated as a violation but will still contribute to dealerting. We recommend disabling alerting on missing data for sparse timeseries to avoid false alerts. To learn more, visit [anomaly detection configurationï»¿](https://dt-url.net/lz02mwi). | Required |
| Number of signal fluctuations `signalFluctuation` | float | Controls how many times the signal fluctuation is added to the baseline to produce the actual threshold for alerting | Required |
| Tolerance `tolerance` | float | Controls the width of the confidence band and larger values lead to a less sensitive model | Required |
| Alert condition `alertCondition` | enum | The element has these enums * `ABOVE` * `BELOW` * `OUTSIDE` | Required |
| Violating samples `violatingSamples` | integer | The number of one-minute samples within the evaluation window that must violate to trigger an event. | Required |
| Sliding window `samples` | integer | The number of one-minute samples that form the sliding evaluation window. | Required |
| Dealerting samples `dealertingSamples` | integer | The number of one-minute samples within the evaluation window that must go back to normal to close the event. | Required |

##### The `EventTemplate` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Title `title` | text | The title of the event to trigger. Type '{' for placeholder hints. | Required |
| Description `description` | text | The description of the event to trigger. Type '{' for placeholder hints. | Required |
| Event type `eventType` | enum | The event type to trigger. The element has these enums * `INFO` * `ERROR` * `AVAILABILITY` * `SLOWDOWN` * `RESOURCE` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `MARKED_FOR_TERMINATION` * `WARNING` | Required |
| Allow merge `davisMerge` | boolean | DavisÂ® AI will try to merge this event into existing problems, otherwise a new problem will always be created. | Required |
| Properties `metadata` | Set<[MetadataItem](#MetadataItem)> | Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2ï»¿](https://dt-url.net/9622g1w). | Required |

##### The `EntityFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Dimension key of entity type `dimensionKey` | text | Dimension key of entity type to filter | Optional |
| `conditions` | [EntityFilterCondition](#EntityFilterCondition)[] | - | Required |

##### The `DimensionFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Dimension key `dimensionKey` | text | - | Required |
| Operator `operator` | enum | The element has these enums * `EQUALS` * `DOES_NOT_EQUAL` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `CONTAINS_CASE_SENSITIVE` * `DOES_NOT_CONTAIN_CASE_SENSITIVE` | Optional |
| Dimension value `dimensionValue` | text | - | Required |

##### The `MetadataItem` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key `metadataKey` | text | Type 'dt.' for key hints. | Required |
| Value `metadataValue` | text | Type '{' for placeholder hints. | Required |

##### The `EntityFilterCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Filter type `type` | enum | The element has these enums * `NAME` * `ENTITY_ID` * `MANAGEMENT_ZONE` * `TAG` * `HOST_NAME` * `HOST_GROUP_NAME` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_ID` * `CUSTOM_DEVICE_GROUP_NAME` | Required |
| Operator `operator` | enum | The element has these enums * `EQUALS` * `DOES_NOT_EQUAL` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `CONTAINS_CASE_SENSITIVE` * `DOES_NOT_CONTAIN_CASE_SENSITIVE` * `CONTAINS_CASE_INSENSITIVE` * `DOES_NOT_CONTAIN_CASE_INSENSITIVE` | Required |
| Value `value` | text | - | Required |