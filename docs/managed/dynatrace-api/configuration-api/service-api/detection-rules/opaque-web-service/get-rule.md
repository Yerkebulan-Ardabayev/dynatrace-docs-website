---
title: Service detection API - GET an opaque web service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/get-rule
scraped: 2026-05-12T11:18:52.430715
---

# Service detection API - GET an opaque web service rule

# Service detection API - GET an opaque web service rule

* Reference
* Published Sep 06, 2019

Shows the properties of the specified service detection rule for opaque and external web services.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required service detection rule. | path | Required |

## Response

Refer to [JSON models](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Learn the variations of JSON models in the Dynatrace service detection rules API.") to find all JSON models that depend on the type of the model.

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [OpaqueAndExternalWebServiceRule](#openapi-definition-OpaqueAndExternalWebServiceRule) | Success. The response contains properties of the specified rule. |
| **404** | - | Failed. The rule with the specified ID doesn't exist. |

### Response body objects

#### The `OpaqueAndExternalWebServiceRule` object

The service detection rule of the `OPAQUE_AND_EXTERNAL_WEB_SERVICE` type

| Element | Type | Description |
| --- | --- | --- |
| conditions | [ConditionsOpaqueAndExternalWebServiceAttributeTypeDto[]](#openapi-definition-ConditionsOpaqueAndExternalWebServiceAttributeTypeDto) | A list of conditions of the rule.  If several conditions are specified, the AND logic applies. |
| description | string | A short description of the rule. |
| detectAsWebRequestService | boolean | Detect the matching requests as web services (`false`) or web request services (`true`).  Setting this field to `true` prevents detecting of matching requests as opaque web services. An opaque web request service is created instead. If you need to further modify the resulting web request service, you need to create a separate rule of the `OPAQUE_AND_EXTERNAL_WEB_REQUEST` type.  Default is `false`, detecting matching requests as opaque web services. |
| enabled | boolean | The rule is enabled(`true`) or disabled (`false`). |
| id | string | The ID of the service detection rule. |
| managementZones | string[] | The management zone (specified by the ID) of the process group for which this service detection rule should be created.  You can specify only 1 management zone here. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| name | string | The name of the rule. |
| order | string | The order of the rule in the rules list.  The rules are evaluated from top to bottom. The first matching rule applies. |
| port | [Port](#openapi-definition-Port) | The contribution to the service ID calculation from the port, where the web request has been detected. |
| type | string | The type of the service detection rule. |
| urlPath | [UrlPath](#openapi-definition-UrlPath) | The contribution from the URL, where the web request has been detected, into service ID calculation.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. |

#### The `ConditionsOpaqueAndExternalWebServiceAttributeTypeDto` object

A condition of the service detection rule.

| Element | Type | Description |
| --- | --- | --- |
| attributeType | string | The type of the attribute to be checked. The element can hold these values * `ENDPOINT` * `IP` * `OPERATION_NAME` * `PG_TAG` * `URL_PATH` * `URL_PORT` |
| compareOperations | [CompareOperation[]](#openapi-definition-CompareOperation) | A list of conditions for the rule.  If several conditions are specified, the AND logic applies. |

#### The `CompareOperation` object

The condition of the rule.

The actual set of fields depends on the type of the condition. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON modelsï»¿](https://dt-url.net/2ie3slq).

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation The element can hold these values * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `Port` object

The contribution to the service ID calculation from the port, where the web request has been detected.

| Element | Type | Description |
| --- | --- | --- |
| doNotUseForServiceId | boolean | The port is used (`false`) or isn't used (`true`) in the service ID calculation. |

#### The `UrlPath` object

The contribution from the URL, where the web request has been detected, into service ID calculation.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

#### The `TransformationBase` object

Configuration of transformation of the detected value.

If several transformations are specified, they are handled sequentially from top to bottom. Each transformation is applied to the result of the preceding transformation. For example, the second transformation is applied to the result of the first transformation.

The actual set of fields depends on the type of the transformation. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON modelsï»¿](https://dt-url.net/2ie3slq).

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation The element can hold these values * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

### Response body JSON models

```
{



"conditions": [



{



"attributeType": "URL_PATH",



"compareOperations": [



{



"ignoreCase": "false",



"invert": "false",



"type": "STRING_CONTAINS",



"values": [



"value1",



"value2"



]



}



]



}



],



"description": "REST API example",



"detectAsWebRequestService": false,



"enabled": true,



"managementZones": [



"zone 1"



],



"name": "My sample rule",



"port": {



"doNotUseForServiceId": "true"



},



"type": "OPAQUE_AND_EXTERNAL_WEB_SERVICE",



"urlPath": {



"valueOverride": "abc"



}



}
```

## Related topics

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")
* [Opaque services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services "Understand what opaque services are.")