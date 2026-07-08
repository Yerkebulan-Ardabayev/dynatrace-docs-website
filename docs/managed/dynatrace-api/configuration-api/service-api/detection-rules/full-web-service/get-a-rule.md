---
title: Service detection API - GET a full web service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/get-a-rule
---

# Service detection API - GET a full web service rule

# Service detection API - GET a full web service rule

* Reference
* Published Sep 06, 2019

Shows the properties of the specified service detection rule for full web services.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/{id}` |

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
| **200** | [FullWebServiceRule](#openapi-definition-FullWebServiceRule) | Success. The response contains properties of the specified rule. |
| **404** | - | Failed. The rule with the specified ID doesn't exist. |

### Response body objects

#### The `FullWebServiceRule` object

The service detection rule of the `FULL_WEB_SERVICE` type.

If you have a condition with the **attributeType** set to `FRAMEWORK`, the **values** field from **compareOperations** is limited to the following possible values:

* `AXIS`
* `CXF`
* `HESSIAN`
* `JAX_WS_RI`
* `JBOSS`
* `JERSEY`
* `PROGRESS`
* `RESTEASY`
* `RESTLET`
* `SPRING`
* `TIBCO`
* `WEBLOGIC`
* `WEBMETHODS`
* `WEBSPHERE`
* `WINK`

| Element | Type | Description |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | The contribution to the service ID calculation from the detected application ID.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. |
| conditions | [ConditionsFullWebServiceAttributeTypeDto](#openapi-definition-ConditionsFullWebServiceAttributeTypeDto)[] | A list of conditions of the rule.  If several conditions are specified, the AND logic applies. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | The contribution to the service ID calculation from the detected context root.  The context root is the first segment of the request URL after server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `support`.  You have two options:  * Keep a part of the detected URL. Specify the number of segments to be kept in the **segmentsToCopyFromUrlPath** field. * Dynamically transform the detected URL. Specify the transformation parameters in the **transformations** field.  You can use one or both options. If you use both, the transformation applies to the modified URL. |
| description | string | A short description of the rule. |
| detectAsWebRequestService | boolean | Detect the matching requests as full web services (`false`) or web request services (`true`).  Setting this field to `true` prevents detecting of matching requests as full web services. A web request service is created instead. If you need to further modify the resulting web request service, you need to create a separate rule of the `FULL_WEB_REQUEST` type.  Default is `false`, detecting matching requests as full web services. |
| enabled | boolean | The rule is enabled(`true`) or disabled (`false`). |
| id | string | The ID of the service detection rule. |
| managementZones | string[] | The management zone (specified by the ID) of the process group for which this service detection rule should be created.  You can specify only 1 management zone here. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| name | string | The name of the rule. |
| order | string | The order of the rule in the rules list.  The rules are evaluated from top to bottom. The first matching rule applies. |
| serverName | [ServerName](#openapi-definition-ServerName) | The contribution to the service ID calculation from the detected server name.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. |
| type | string | The type of the service detection rule. |
| webServiceName | [WebServiceName](#openapi-definition-WebServiceName) | The contribution to the service ID calculation from the detected web service name.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. |
| webServiceNameSpace | [WebServiceNameSpace](#openapi-definition-WebServiceNameSpace) | The contribution to the service ID calculation from the detected web service name space.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. |

#### The `ApplicationId` object

The contribution to the service ID calculation from the detected application ID.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

#### The `TransformationBase` object

Configuration of transformation of the detected value.

If several transformations are specified, they are handled sequentially from top to bottom. Each transformation is applied to the result of the preceding transformation. For example, the second transformation is applied to the result of the first transformation.

The actual set of fields depends on the type of the transformation. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq).

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation The element can hold these values * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

#### The `ConditionsFullWebServiceAttributeTypeDto` object

A condition of the service detection rule.

| Element | Type | Description |
| --- | --- | --- |
| attributeType | string | The type of the attribute to be checked. The element can hold these values * `APPLICATION_ID` * `CONTEXT_ROOT` * `FRAMEWORK` * `IS_SOAP_SERVICE` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` * `WEBSERVICE_NAMESPACE` |
| compareOperations | [CompareOperation](#openapi-definition-CompareOperation)[] | A list of conditions for the rule.  If several conditions are specified, the AND logic applies. |

#### The `CompareOperation` object

The condition of the rule.

The actual set of fields depends on the type of the condition. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq).

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation The element can hold these values * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |

#### The `ContextRoot` object

The contribution to the service ID calculation from the detected context root.

The context root is the first segment of the request URL after server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `support`.

You have two options:

* Keep a part of the detected URL. Specify the number of segments to be kept in the **segmentsToCopyFromUrlPath** field.
* Dynamically transform the detected URL. Specify the transformation parameters in the **transformations** field.

You can use one or both options. If you use both, the transformation applies to the modified URL.

| Element | Type | Description |
| --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | The number of segments of the URL to be kept.  The URL is divided by slashes (`/`), the indexing starts with 1 at context root.  For example, if you specify `2` for the `www.dynatrace.com/support/help/dynatrace-api/` URL, the value of `support/help` is used. |
| transformations | [ContextRootTransformation](#openapi-definition-ContextRootTransformation)[] | Transformations to be applied to the detected value. |

#### The `ContextRootTransformation` object

Configuration of transformation of the detected value.

If several transformations are specified, they are handled sequentially from top to bottom. Each transformation is applied to the result of the preceding transformation. For example, the second transformation is applied to the result of the first transformation.

The actual set of fields depends on the `type` of the transformation.

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation The element can hold these values * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `ServerName` object

The contribution to the service ID calculation from the detected server name.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

#### The `WebServiceName` object

The contribution to the service ID calculation from the detected web service name.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

#### The `WebServiceNameSpace` object

The contribution to the service ID calculation from the detected web service name space.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

### Response body JSON models

```
{



"applicationId": {



"valueOverride": "abc"



},



"conditions": [



{



"attributeType": "APPLICATION_ID",



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



"contextRoot": {



"segmentsToCopyFromUrlPath": 2,



"transformations": [



{



"delimiter": "/",



"type": "BEFORE"



}



]



},



"description": "REST API example",



"detectAsWebRequestService": false,



"enabled": true,



"managementZones": [



"zone 1"



],



"name": "My sample rule",



"serverName": {



"transformations": [



{



"delimiter": "-",



"type": "BEFORE"



}



]



},



"type": "FULL_WEB_SERVICE",



"webServiceName": {



"valueOverride": "abc"



},



"webServiceNameSpace": {



"valueOverride": "abc"



}



}
```

## Related topics

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")