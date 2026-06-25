---
title: Problems API v2 - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/models
scraped: 2026-05-12T12:09:51.787604
---

# Problems API v2 - JSON models

# Problems API v2 - JSON models

* Reference
* Published Oct 12, 2020

Some JSON models of the **Problems v2** API vary depending on the **type** of the model. The JSON models for each variation are listed below.

## Variations of the `Evidence` object

The `Evidence` object is the base for evidence of a problem. The actual set of fields depends on the **type** of the evidence.

### AVAILABILITY\_EVIDENCE

AvailabilityEvidenceMetadata

Parameters

JSON model

#### The `AvailabilityEvidence` object

The availability evidence of the problem.

Indicates an entity that has been unavailable during the problem lifespan and that might be related to the root cause.

| Element | Type | Description |
| --- | --- | --- |
| endTime | integer | The end time of the evidence, in UTC milliseconds. |

```
{



"evidenceType": "AVAILABILITY_EVIDENCE",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602500000000,



"endTime": 1602600000000



}
```

### EVENT

EventEvidenceMetadata

Parameters

JSON model

#### The `EventEvidence` object

The event evidence of the problem.

An event that occurred during the problem lifespan that might be related to the root cause.

| Element | Type | Description |
| --- | --- | --- |
| data | [Event](#openapi-definition-Event) | Configuration of an event. |
| endTime | integer | The end timestamp of the event, in UTC milliseconds.  Has `-1` value, if the event is still active. |
| eventId | string | The ID of the event. |
| eventType | string | The type of the event. |

#### The `Event` object

Configuration of an event.

| Element | Type | Description |
| --- | --- | --- |
| correlationId | string | The correlation ID of the event. |
| endTime | integer | The timestamp when the event was closed, in UTC milliseconds.  Has the value of `null` if the event is still active. |
| entityId | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |
| entityTags | [METag[]](#openapi-definition-METag) | A list of tags of the related entity. |
| eventId | string | The ID of the event. |
| eventType | string | The type of the event. |
| frequentEvent | boolean | If `true`, the event happens [frequentlyï»¿](https://dt-url.net/4da3kdg).  A frequent event doesn't raise a problem. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | A list of all management zones that the event belongs to. |
| properties | [EventProperty[]](#openapi-definition-EventProperty) | A list of event properties. |
| startTime | integer | The timestamp when the event was raised, in UTC milliseconds. |
| status | string | The status of the event. The element can hold these values * `CLOSED` * `OPEN` |
| suppressAlert | boolean | The alerting status during a [maintenanceï»¿](https://dt-url.net/b2123rg0):  * `false`: Alerting works as usual. * `true`: Alerting is disabled. |
| suppressProblem | boolean | The problem detection status during a [maintenanceï»¿](https://dt-url.net/b2123rg0):  * `false`: Problem detection works as usual. * `true`: Problem detection is disabled. |
| title | string | The title of the event. |
| underMaintenance | boolean | If `true`, the event happened while the monitored system was under maintenance. |

#### The `EntityStub` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | A short representation of a monitored entity. |
| name | string | The name of the entity.  Not included in the response in case no entity with the relevant ID was found. |

#### The `EntityId` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the entity. |
| type | string | The type of the entity. |

#### The `METag` object

The tag of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. |
| key | string | The key of the tag. |
| stringRepresentation | string | The string representation of the tag. |
| value | string | The value of the tag. |

#### The `ManagementZone` object

A short representation of a management zone.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the management zone. |
| name | string | The name of the management zone. |

#### The `EventProperty` object

A property of an event.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The key of the event property. |
| value | string | The value of the event property. |

```
{



"evidenceType": "EVENT",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602511312869,



"eventId": "string",



"eventType": "string"



}
```

### MAINTENANCE\_WINDOW

MaintenanceWindowEvidenceMetadata

Parameters

JSON model

#### The `MaintenanceWindowEvidence` object

The maintenance window evidence of the problem.

The maintenance window during which the problem occurred.

| Element | Type | Description |
| --- | --- | --- |
| endTime | integer | The end time of the evidence, in UTC milliseconds. |
| maintenanceWindowConfigId | string | The ID of the related maintenance window. |

```
{



"evidenceType": "MAINTENANCE_WINDOW",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602500000000,



"maintenanceWindowConfigId": "string",



"endTime": 1602600000000



}
```

### METRIC

MetricEvidenceMetadata

Parameters

JSON model

#### The `MetricEvidence` object

The metric evidence of the problem.

A change of metric behavior that indicates the problem and/or is its root cause.

| Element | Type | Description |
| --- | --- | --- |
| endTime | integer | The end time of the evidence, in UTC milliseconds.  The value `null` indicates that the evidence is still open. |
| metricId | string | The ID of the metric. |
| unit | string | The unit of the metric. The element can hold these values * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| valueAfterChangePoint | number | The metric's value after the problem start. |
| valueBeforeChangePoint | number | The metric's value before the problem start. |

```
{



"evidenceType": "METRIC",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602500000000,



"metricId": "string",



"valueBeforeChangePoint": 2,



"valueAfterChangePoint": 3,



"unit": "Count",



"endTime": 1602600000000



}
```

### TRANSACTIONAL

TransactionalEvidenceMetadata

Parameters

JSON model

#### The `TransactionalEvidence` object

The transactional evidence of the problem.

A behavior of a metric in an transaction that indicates the problem and/or is its root cause.

| Element | Type | Description |
| --- | --- | --- |
| endTime | integer | The end time of the evidence, in UTC milliseconds |
| unit | string | The unit of the metric. |
| valueAfterChangePoint | number | The metric's value after the problem start. |
| valueBeforeChangePoint | number | The metric's value before the problem start. |

```
{



"evidenceType": "TRANSACTIONAL",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602500000000,



"valueBeforeChangePoint": 2,



"valueAfterChangePoint": 3,



"unit": "Count",



"endTime": 1602600000000



}
```

## Variations of the `Impact` object

The `Impact` object is the base for impacts of a problem. The actual set of fields depends on the **type** of the impact.

### APPLICATION

ApplicationImpactDto

Parameters

JSON model

#### The `ApplicationImpact` object

Analysis of problem impact to an application.

| Element | Type | Description |
| --- | --- | --- |
| estimatedAffectedUsers | integer | The estimated number of affected users. |
| impactType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `SERVICE` -> ServiceImpact * `APPLICATION` -> ApplicationImpact * `MOBILE` -> MobileImpact * `CUSTOM_APPLICATION` -> CustomApplicationImpact The element can hold these values * `APPLICATION` * `CUSTOM_APPLICATION` * `MOBILE` * `SERVICE` |
| impactedEntity | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |

#### The `EntityStub` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | A short representation of a monitored entity. |
| name | string | The name of the entity.  Not included in the response in case no entity with the relevant ID was found. |

#### The `EntityId` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the entity. |
| type | string | The type of the entity. |

```
{



"impactType": "APPLICATION",



"impactedEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"estimatedAffectedUsers": 5



}
```

### CUSTOM\_APPLICATION

CustomApplicationImpactDto

Parameters

JSON model

#### The `CustomApplicationImpact` object

Analysis of problem impact to a custom application.

| Element | Type | Description |
| --- | --- | --- |
| estimatedAffectedUsers | integer | The estimated number of affected users. |
| impactType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `SERVICE` -> ServiceImpact * `APPLICATION` -> ApplicationImpact * `MOBILE` -> MobileImpact * `CUSTOM_APPLICATION` -> CustomApplicationImpact The element can hold these values * `APPLICATION` * `CUSTOM_APPLICATION` * `MOBILE` * `SERVICE` |
| impactedEntity | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |

#### The `EntityStub` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | A short representation of a monitored entity. |
| name | string | The name of the entity.  Not included in the response in case no entity with the relevant ID was found. |

#### The `EntityId` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the entity. |
| type | string | The type of the entity. |

```
{



"impactType": "CUSTOM_APPLICATION",



"impactedEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"estimatedAffectedUsers": 5



}
```

### MOBILE

MobileImpactDto

Parameters

JSON model

#### The `MobileImpact` object

Analysis of problem impact to a mobile application.

| Element | Type | Description |
| --- | --- | --- |
| estimatedAffectedUsers | integer | The estimated number of affected users. |
| impactType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `SERVICE` -> ServiceImpact * `APPLICATION` -> ApplicationImpact * `MOBILE` -> MobileImpact * `CUSTOM_APPLICATION` -> CustomApplicationImpact The element can hold these values * `APPLICATION` * `CUSTOM_APPLICATION` * `MOBILE` * `SERVICE` |
| impactedEntity | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |

#### The `EntityStub` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | A short representation of a monitored entity. |
| name | string | The name of the entity.  Not included in the response in case no entity with the relevant ID was found. |

#### The `EntityId` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the entity. |
| type | string | The type of the entity. |

```
{



"impactType": "MOBILE",



"impactedEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"estimatedAffectedUsers": 5



}
```

### SERVICE

ServiceImpactDto

Parameters

JSON model

#### The `ServiceImpact` object

Analysis of problem impact to a service.

| Element | Type | Description |
| --- | --- | --- |
| numberOfPotentiallyAffectedServiceCalls | integer | The number of potentially impacted services. |

```
{



"impactType": "SERVICE",



"impactedEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"estimatedAffectedUsers": 5,



"numberOfPotentiallyAffectedServiceCalls": 50



}
```