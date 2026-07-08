---
title: Metric events anomaly detection API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/json-models
---

# Metric events anomaly detection API - JSON models

# Metric events anomaly detection API - JSON models

* Reference
* Updated on Apr 26, 2023
* Deprecated

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Metric events** (`builtin:anomaly-detection.metric-events`) schema.

Some JSON models of the **Metric events anomaly detection** API vary, depending on the **filterType** of some objects. Here you can find JSON models for each variation.

## Variations of the `MetricEventAlertingScope` object

The `MetricEventAlertingScope` object is the base for alerting scopes of metric events. The actual set of fields depends on the **filterType** of the scope.

### CUSTOM\_DEVICE\_GROUP\_NAME

CustomDeviceGroupNameAlertingScope

Parameters

JSON model

#### The `CustomDeviceGroupNameAlertingScope` object

A scope filter for the related custom device group name.

| Element | Type | Description |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | A filter for a string value based on the given operator. |

#### The `MetricEventTextFilterMetricEventTextFilterOperatorDto` object

A filter for a string value based on the given operator.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | The operator to match on. The element can hold these values * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | The value to match on. |

```
{



"filterType": "CUSTOM_DEVICE_GROUP_NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### ENTITY\_ID

EntityIdAlertingScope

Parameters

JSON model

#### The `EntityIdAlertingScope` object

A scope filter for a monitored entity identifier.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | The monitored entities id to match on. |

```
{



"filterType": "ENTITY_ID",



"entityId": "HOST-B7A6F9EE9F366CB5"



}
```

### HOST\_NAME

HostNameAlertingScope

Parameters

JSON model

#### The `HostNameAlertingScope` object

A scope filter for the related host name.

| Element | Type | Description |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | A filter for a string value based on the given operator. |

#### The `MetricEventTextFilterMetricEventTextFilterOperatorDto` object

A filter for a string value based on the given operator.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | The operator to match on. The element can hold these values * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | The value to match on. |

```
{



"filterType": "HOST_NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### HOST\_GROUP\_NAME

HostGroupNameAlertingScope

Parameters

JSON model

#### The `HostGroupNameAlertingScope` object

A scope filter for the related host group name.

| Element | Type | Description |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | A filter for a string value based on the given operator. |

#### The `MetricEventTextFilterMetricEventTextFilterOperatorDto` object

A filter for a string value based on the given operator.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | The operator to match on. The element can hold these values * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | The value to match on. |

```
{



"filterType": "HOST_GROUP_NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### MANAGEMENT\_ZONE

ManagementZoneAlertingScope

Parameters

JSON model

#### The `ManagementZoneAlertingScope` object

A scope filter for a management zone identifier.

| Element | Type | Description |
| --- | --- | --- |
| mzId | string | The management zone id to match on. |

```
{



"filterType": "MANAGEMENT_ZONE",



"mzId": "6958644387494623526"



}
```

### NAME

NameAlertingScope

Parameters

JSON model

#### The `NameAlertingScope` object

A scope filter for a monitored entity name.

| Element | Type | Description |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | A filter for a string value based on the given operator. |

#### The `MetricEventTextFilterMetricEventTextFilterOperatorDto` object

A filter for a string value based on the given operator.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | The operator to match on. The element can hold these values * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | The value to match on. |

```
{



"filterType": "NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### PROCESS\_GROUP\_ID

ProcessGroupIdAlertingScope

Parameters

JSON model

#### The `ProcessGroupIdAlertingScope` object

A scope filter for a process group identifier.

| Element | Type | Description |
| --- | --- | --- |
| processGroupId | string | The process groups id to match on. |

```
{



"filterType": "PROCESS_GROUP_ID",



"processGroupId": "PROCESS_GROUP-B34081EFF9E5F516"



}
```

### PROCESS\_GROUP\_NAME

ProcessGroupNameAlertingScope

Parameters

JSON model

#### The `ProcessGroupNameAlertingScope` object

A scope filter for the related process group name.

| Element | Type | Description |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | A filter for a string value based on the given operator. |

#### The `MetricEventTextFilterMetricEventTextFilterOperatorDto` object

A filter for a string value based on the given operator.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | The operator to match on. The element can hold these values * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | The value to match on. |

```
{



"filterType": "PROCESS_GROUP_NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### TAG

TagFilterAlertingScope

Parameters

JSON model

#### The `TagFilterAlertingScope` object

A scope filter for tags on entities.

| Element | Type | Description |
| --- | --- | --- |
| tagFilter | [TagFilter](#openapi-definition-TagFilter) | A tag-based filter of monitored entities. |

#### The `TagFilter` object

A tag-based filter of monitored entities.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

```
{



"filterType": "TAG",



"tagFilter": {



"context": "CONTEXTLESS",



"key": "Infrastructure",



"value": "Linux"



}



}
```

## Variations of the `MetricEventDimensions` object

The `MetricEventDimensions` object is the base for metric dimensions. The actual set of fields depends on the **filterType** of the dimension.

### ENTITY

MetricEventEntityDimensions

Parameters

JSON model

#### The `MetricEventEntityDimensions` object

A filter for the metrics entity dimensions.

| Element | Type | Description |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventDimensionsFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventDimensionsFilterOperatorDto) | A filter for a string value based on the given operator. |

#### The `MetricEventTextFilterMetricEventDimensionsFilterOperatorDto` object

A filter for a string value based on the given operator.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | The operator to match on. The element can hold these values * `EQUALS` |
| value | string | The value to match on. |

```
{



"filterType": "ENTITY",



"name": "dimension",



"index": 1,



"nameFilter": {



"value": "entity name",



"operator": "EQUALS"



}



}
```

### STRING

MetricEventStringDimensions

Parameters

JSON model

#### The `MetricEventStringDimensions` object

A filter for the metrics string dimensions.

| Element | Type | Description |
| --- | --- | --- |
| textFilter | [MetricEventTextFilterMetricEventDimensionsFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventDimensionsFilterOperatorDto) | A filter for a string value based on the given operator. |

#### The `MetricEventTextFilterMetricEventDimensionsFilterOperatorDto` object

A filter for a string value based on the given operator.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | The operator to match on. The element can hold these values * `EQUALS` |
| value | string | The value to match on. |

```
{



"filterType": "STRING",



"name": "dimension",



"index": 1,



"textFilter": {



"value": "entity name",



"operator": "EQUALS"



}



}
```

## Variations of the `MetricEventMonitoringStrategy` object

The `MetricEventMonitoringStrategy` object is the base for monitoring strategy of a metric event. The actual set of fields depends on the **type** of the strategy.

### AUTO\_ADAPTIVE\_BASELINE

MetricEventAutoAdaptiveBaselineMonitoringStrategy

Parameters

JSON model

#### The `MetricEventAutoAdaptiveBaselineMonitoringStrategy` object

An auto-adaptive baseline strategy to detect anomalies within metrics that show a regular change over time, as the baseline is also updated automatically. An example is to detect an anomaly in the number of received network packets or within the number of user actions over time.

| Element | Type | Description |
| --- | --- | --- |
| alertCondition | string | The condition for the **threshold** value check: above or below. The element can hold these values * `ABOVE` * `BELOW` |
| alertingOnMissingData | boolean | If true, also one-minute samples without data are counted as violating samples. |
| dealertingSamples | integer | The number of one-minute samples within the evaluation window that must go back to normal to close the event. |
| numberOfSignalFluctuations | number | Defines the factor of how many signal fluctuations are valid. Values above the baseline plus the signal fluctuation times the number of tolerated signal fluctuations are alerted. |
| samples | integer | The number of one-minute samples that form the sliding evaluation window. |
| violatingSamples | integer | The number of one-minute samples within the evaluation window that must violate the threshold to trigger an event. |

```
{



"type": "AUTO_ADAPTIVE_BASELINE",



"samples": 5,



"violatingSamples": 3,



"dealertingSamples": 5,



"alertCondition": "ABOVE",



"alertingOnMissingData": false,



"numberOfSignalFluctuations": 1.0



}
```

### STATIC\_THRESHOLD

MetricEventStaticThresholdMonitoringStrategy

Parameters

JSON model

#### The `MetricEventStaticThresholdMonitoringStrategy` object

A static threshold monitoring strategy to alert on hard limits within a given metric. An example is the violation of a critical memory limit.

| Element | Type | Description |
| --- | --- | --- |
| alertCondition | string | The condition for the **threshold** value check: above or below. The element can hold these values * `ABOVE` * `BELOW` |
| alertingOnMissingData | boolean | If true, also one-minute samples without data are counted as violating samples. |
| dealertingSamples | integer | The number of one-minute samples within the evaluation window that must go back to normal to close the event. |
| samples | integer | The number of one-minute samples that form the sliding evaluation window. |
| threshold | number | The value of the static threshold based on the specified unit. |
| unit | string | The unit of the threshold, matching the metric definition. The element can hold these values * `AMPERE` * `BILLION` * `BIT` * `BIT_PER_HOUR` * `BIT_PER_MINUTE` * `BIT_PER_SECOND` * `BYTE` * `BYTE_PER_HOUR` * `BYTE_PER_MINUTE` * `BYTE_PER_SECOND` * `CORES` * `COUNT` * `DAY` * `DECIBEL_MILLI_WATT` * `GIBI_BYTE` * `GIBI_BYTE_PER_HOUR` * `GIBI_BYTE_PER_MINUTE` * `GIBI_BYTE_PER_SECOND` * `GIGA` * `GIGA_BYTE` * `GIGA_BYTE_PER_HOUR` * `GIGA_BYTE_PER_MINUTE` * `GIGA_BYTE_PER_SECOND` * `HERTZ` * `HOUR` * `KIBI_BYTE` * `KIBI_BYTE_PER_HOUR` * `KIBI_BYTE_PER_MINUTE` * `KIBI_BYTE_PER_SECOND` * `KILO` * `KILO_BYTE` * `KILO_BYTE_PER_HOUR` * `KILO_BYTE_PER_MINUTE` * `KILO_BYTE_PER_SECOND` * `KILO_METRE_PER_HOUR` * `MEBI_BYTE` * `MEBI_BYTE_PER_HOUR` * `MEBI_BYTE_PER_MINUTE` * `MEBI_BYTE_PER_SECOND` * `MEGA` * `MEGA_BYTE` * `MEGA_BYTE_PER_HOUR` * `MEGA_BYTE_PER_MINUTE` * `MEGA_BYTE_PER_SECOND` * `METRE_PER_HOUR` * `METRE_PER_SECOND` * `MICRO_SECOND` * `MILLION` * `MILLI_CORES` * `MILLI_SECOND` * `MILLI_SECOND_PER_MINUTE` * `MINUTE` * `MONTH` * `MSU` * `NANO_SECOND` * `NANO_SECOND_PER_MINUTE` * `NOT_APPLICABLE` * `PERCENT` * `PER_HOUR` * `PER_MINUTE` * `PER_SECOND` * `PIXEL` * `PROMILLE` * `RATIO` * `SECOND` * `STATE` * `TRILLION` * `UNSPECIFIED` * `VOLT` * `WATT` * `WEEK` * `YEAR` |
| violatingSamples | integer | The number of one-minute samples within the evaluation window that must violate the threshold to trigger an event. |

```
{



"type": "STATIC_THRESHOLD",



"samples": 3,



"violatingSamples": 1,



"dealertingSamples": 3,



"alertCondition": "BELOW",



"alertingOnMissingData": false,



"threshold": 99,



"unit": "COUNT"



}
```