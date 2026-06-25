---
title: Service detection API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/models
scraped: 2026-05-12T12:02:42.818699
---

# Service detection API - JSON models

# Service detection API - JSON models

* Reference
* Published Aug 06, 2019

JSON models of the **Service detection rules** API vary greatly, depending on the **type** of some objects. Here you can find JSON models for each variation.

## Variations of the `ServiceDetectionRule` object

The `ServiceDetectionRule` object is the base for all service detection rules. The actual set of fields depends on the **type** of the rule.

#### FULL\_WEB\_REQUEST

FullWebRequestRule

Parameters

JSON model

#### The `FullWebRequestRule` object

The service detection rule of the `FULL_WEB_REQUEST` type.

| Element | Type | Description |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | The contribution to the service ID calculation from the detected application ID.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. |
| conditions | [ConditionsFullWebRequestAttributeTypeDto[]](#openapi-definition-ConditionsFullWebRequestAttributeTypeDto) | A list of conditions of the rule.  If several conditions are specified, the AND logic applies. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | The contribution to the service ID calculation from the detected context root.  The context root is the first segment of the request URL after server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `support`.  You have two options:  * Keep a part of the detected URL. Specify the number of segments to be kept in the **segmentsToCopyFromUrlPath** field. * Dynamically transform the detected URL. Specify the transformation parameters in the **transformations** field.  You can use one or both options. If you use both, the transformation applies to the modified URL. |
| description | string | A short description of the rule. |
| enabled | boolean | The rule is enabled(`true`) or disabled (`false`). |
| id | string | The ID of the service detection rule. |
| managementZones | string[] | The management zone (specified by the ID) of the process group for which this service detection rule should be created.  You can specify only 1 management zone here. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| name | string | The name of the rule. |
| order | string | The order of the rule in the rules list.  The rules are evaluated from top to bottom. The first matching rule applies. |
| serverName | [ServerName](#openapi-definition-ServerName) | The contribution to the service ID calculation from the detected server name.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. |
| type | string | The type of the service detection rule. |

#### The `ApplicationId` object

The contribution to the service ID calculation from the detected application ID.

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

#### The `ConditionsFullWebRequestAttributeTypeDto` object

A condition of the service detection rule.

| Element | Type | Description |
| --- | --- | --- |
| attributeType | string | The type of the attribute to be checked. The element can hold these values * `APPLICATION_ID` * `CONTEXT_ROOT` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` |
| compareOperations | [CompareOperation[]](#openapi-definition-CompareOperation) | A list of conditions for the rule.  If several conditions are specified, the AND logic applies. |

#### The `CompareOperation` object

The condition of the rule.

The actual set of fields depends on the type of the condition. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON modelsï»¿](https://dt-url.net/2ie3slq).

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
| transformations | [ContextRootTransformation[]](#openapi-definition-ContextRootTransformation) | Transformations to be applied to the detected value. |

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
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"type": "FULL_WEB_REQUEST",



"id": "f69d6702-9b6e-4c47-b94c-628acc391995",



"order": "1",



"name": "string",



"description": "string",



"enabled": true,



"conditions": [



{



"attributeType": "URL_PATH",



"compareOperations": [



{



"type": "STRING_CONTAINS",



"negate": false,



"ignoreCase": true,



"values": [



"string"



]



}



]



}



],



"applicationId": {



"transformations": [],



"valueOverride": "string"



},



"contextRoot": {



"transformations": [



{



"type": "AFTER",



"delimiter": "string"



}



],



"segmentsToCopyFromUrlPath": 2



},



"serverName": {



"transformations": [



{



"type": "BEFORE",



"delimiter": "string"



}



]



}



}
```

#### OPAQUE\_AND\_EXTERNAL\_WEB\_REQUEST

OpaqueAndExternalWebRequestRule

Parameters

JSON model

#### The `OpaqueAndExternalWebRequestRule` object

The service detection rule of the `OPAQUE_AND_EXTERNAL_WEB_REQUEST` type.

| Element | Type | Description |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | The contribution to the service ID calculation from the detected application ID.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. |
| conditions | [ConditionsOpaqueAndExternalWebRequestAttributeTypeDto[]](#openapi-definition-ConditionsOpaqueAndExternalWebRequestAttributeTypeDto) | A list of conditions of the rule.  If several conditions are specified, the AND logic applies. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | The contribution to the service ID calculation from the detected context root.  The context root is the first segment of the request URL after server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `support`.  You have two options:  * Keep a part of the detected URL. Specify the number of segments to be kept in the **segmentsToCopyFromUrlPath** field. * Dynamically transform the detected URL. Specify the transformation parameters in the **transformations** field.  You can use one or both options. If you use both, the transformation applies to the modified URL. |
| description | string | A short description of the rule. |
| enabled | boolean | The rule is enabled(`true`) or disabled (`false`). |
| id | string | The ID of the service detection rule. |
| managementZones | string[] | The management zone (specified by the ID) of the process group for which this service detection rule should be created.  You can specify only 1 management zone here. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| name | string | The name of the rule. |
| order | string | The order of the rule in the rules list.  The rules are evaluated from top to bottom. The first matching rule applies. |
| port | [Port](#openapi-definition-Port) | The contribution to the service ID calculation from the port, where the web request has been detected. |
| publicDomainName | [PublicDomainName](#openapi-definition-PublicDomainName) | The contribution to the service ID calculation from the domain name where the web request has been detected.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. |
| type | string | The type of the service detection rule. |

#### The `ApplicationId` object

The contribution to the service ID calculation from the detected application ID.

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

#### The `ConditionsOpaqueAndExternalWebRequestAttributeTypeDto` object

A condition of the service detection rule.

| Element | Type | Description |
| --- | --- | --- |
| attributeType | string | The type of the attribute to be checked. The element can hold these values * `IP` * `PG_TAG` * `TOP_LEVEL_DOMAIN` * `URL` * `URL_HOST_NAME` * `URL_PATH` * `URL_PORT` |
| compareOperations | [CompareOperation[]](#openapi-definition-CompareOperation) | A list of conditions for the rule.  If several conditions are specified, the AND logic applies. |

#### The `CompareOperation` object

The condition of the rule.

The actual set of fields depends on the type of the condition. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON modelsï»¿](https://dt-url.net/2ie3slq).

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
| transformations | [ContextRootTransformation[]](#openapi-definition-ContextRootTransformation) | Transformations to be applied to the detected value. |

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

#### The `Port` object

The contribution to the service ID calculation from the port, where the web request has been detected.

| Element | Type | Description |
| --- | --- | --- |
| doNotUseForServiceId | boolean | The port is used (`false`) or isn't used (`true`) in the service ID calculation. |

#### The `PublicDomainName` object

The contribution to the service ID calculation from the domain name where the web request has been detected.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description |
| --- | --- | --- |
| copyFromHostName | boolean | Use (`true`) or don't use (`false`) the detected host name as base for transformation.  Not applicable if the override is specified. |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"type": "OPAQUE_AND_EXTERNAL_WEB_REQUEST",



"id": "9c22d0b1-e731-4baf-b3d0-140d14ead3c5",



"order": "2",



"name": "string",



"description": "string",



"enabled": true,



"conditions": [



{



"attributeType": "TOP_LEVEL_DOMAIN",



"compareOperations": [



{



"type": "ENDS_WITH",



"negate": false,



"ignoreCase": true,



"values": [



"string"



]



}



]



}



],



"applicationId": null,



"contextRoot": {



"transformations": [],



"segmentsToCopyFromUrlPath": 1



},



"port": null,



"publicDomainName": null



}
```

#### FULL\_WEB\_SERVICE

FullWebServiceRule

Parameters

JSON model

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
| conditions | [ConditionsFullWebServiceAttributeTypeDto[]](#openapi-definition-ConditionsFullWebServiceAttributeTypeDto) | A list of conditions of the rule.  If several conditions are specified, the AND logic applies. |
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
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

#### The `TransformationBase` object

Configuration of transformation of the detected value.

If several transformations are specified, they are handled sequentially from top to bottom. Each transformation is applied to the result of the preceding transformation. For example, the second transformation is applied to the result of the first transformation.

The actual set of fields depends on the type of the transformation. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON modelsï»¿](https://dt-url.net/2ie3slq).

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation The element can hold these values * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

#### The `ConditionsFullWebServiceAttributeTypeDto` object

A condition of the service detection rule.

| Element | Type | Description |
| --- | --- | --- |
| attributeType | string | The type of the attribute to be checked. The element can hold these values * `APPLICATION_ID` * `CONTEXT_ROOT` * `FRAMEWORK` * `IS_SOAP_SERVICE` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` * `WEBSERVICE_NAMESPACE` |
| compareOperations | [CompareOperation[]](#openapi-definition-CompareOperation) | A list of conditions for the rule.  If several conditions are specified, the AND logic applies. |

#### The `CompareOperation` object

The condition of the rule.

The actual set of fields depends on the type of the condition. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON modelsï»¿](https://dt-url.net/2ie3slq).

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
| transformations | [ContextRootTransformation[]](#openapi-definition-ContextRootTransformation) | Transformations to be applied to the detected value. |

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
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

#### The `WebServiceName` object

The contribution to the service ID calculation from the detected web service name.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

#### The `WebServiceNameSpace` object

The contribution to the service ID calculation from the detected web service name space.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. |
| valueOverride | string | The value to be used instead of the detected value. |

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"type": "FULL_WEB_SERVICE",



"id": "string",



"order": "1",



"name": "string",



"description": "string",



"enabled": true,



"conditions": [



{



"attributeType": "URL_PATH",



"compareOperations": [



{



"type": "STRING_CONTAINS",



"negate": false,



"ignoreCase": true,



"values": [



"string"



]



}



]



}



],



"detectWebRequestOnly": false,



"webServiceName" : {



"valueOverride": "string",



"transformations": []



},



"webServiceNameSpace": {



"valueOverride": "string",



"transformations": []



},



"applicationId": {



"transformations": [],



"valueOverride": "string"



},



"contextRoot": {



"transformations": [



{



"type": "AFTER",



"delimiter": "string"



}



],



"segmentsToCopyFromUrlPath": 2



},



"serverName": {



"transformations": [



{



"type": "BEFORE",



"delimiter": "string"



}



]



}



}
```

## Variations of the `CompareOperation` object

The `CompareOperation` object is the base for all comparison operations. The actual set of fields depends on the **type** of the comparison.

### STRING\_CONTAINS

StringContainsCompareOperation

Parameters

JSON model

#### The `StringContainsCompareOperation` object

The condition of the `STRING_CONTAINS` type.

The condition checks whether the string value contains the specified text.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. |
| negate | boolean | Inverts the operation of the condition. Set to `true` to turn **contains** into **does not contain**.  If not set, then `false` is used. |
| values | string[] | The value to compare to.  If several values are specified, the OR logic applies. |

```
{



"type": "STRING_CONTAINS",



"negate": false,



"ignoreCase": true,



"values": [



"compareValue1",



"compareValue2"



]



}
```

### STRING\_EQUALS

StringEqualsCompareOperation

Parameters

JSON model

#### The `StringEqualsCompareOperation` object

The condition of the `STRING_EQUALS` type.

The condition checks whether the string value equals the specified text.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. |
| negate | boolean | Inverts the operation of the condition. Set to `true` to turn **equals** into **does not equal**.  If not set, then `false` is used. |
| values | string[] | The value to compare to.  If several values are specified, the OR logic applies. |

```
{



"type": "STRING_EQUALS",



"negate": false,



"ignoreCase": true,



"values": [



"compareValue1",



"compareValue2"



]



}
```

### STARTS\_WITH

StartsWithCompareOperation

Parameters

JSON model

#### The `StartsWithCompareOperation` object

The condition of the `STARTS_WITH` type.

The condition checks whether the string value starts with the specified text.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. |
| negate | boolean | Inverts the operation of the condition. Set to `true` to turn **starts with** into **does not start with**.  If not set, then `false` is used. |
| values | string[] | The value to compare to.  If several values are specified, the OR logic applies. |

```
{



"type": "STARTS_WITH",



"negate": false,



"ignoreCase": true,



"values": [



"compareValue1",



"compareValue2"



]



}
```

### ENDS\_WITH

EndsWithCompareOperation

Parameters

JSON model

#### The `EndsWithCompareOperation` object

The condition of the `ENDS_WITH` type.

The condition checks whether the string value ends with the specified text.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. |
| negate | boolean | Inverts the operation of the condition. Set to `true` to turn **ends with** into **does not end with**.  If not set, then `false` is used. |
| values | string[] | The value to compare to.  If several values are specified, the OR logic applies. |

```
{



"type": "ENDS_WITH",



"negate": false,



"ignoreCase": true,



"values": [



"compareValue1",



"compareValue2"



]



}
```

### EXISTS

ExistsCompareOperation

Parameters

JSON model

#### The `ExistsCompareOperation` object

The condition of the `EXISTS` type.

The condition checks whether the specified attribute exists.

| Element | Type | Description |
| --- | --- | --- |
| negate | boolean | Inverts the operation of the condition. Set to `true` to turn **exists** into **does not exist**.  If not set, then `false` is used. |

```
{



"type": "EXISTS",



"negate": false



}
```

### IP\_IN\_RANGE

IpInRangeCompareOperation

Parameters

JSON model

#### The `IpInRangeCompareOperation` object

The condition of the `IP_IN_RANGE` type.

The condition checks whether the IP address belongs to a specified range.

| Element | Type | Description |
| --- | --- | --- |
| lower | string | The lower boundary of the IP range. |
| negate | boolean | Inverts the operation of the condition. Set to `true` to turn **IP is in range** into **IP is not in range**.  If not set, then `false` is used. |
| upper | string | The upper boundary of the IP range. |

```
{



"type": "IP_IN_RANGE",



"negate": false,



"lower": "192.168.0.1",



"upper": "192.168.0.10"



}
```

### INT\_EQUALS

IntEqualsCompareOperation

Parameters

JSON model

#### The `IntEqualsCompareOperation` object

The condition of the `INT_EQUALS` type.

The condition checks whether the integer value equals the specified value.

| Element | Type | Description |
| --- | --- | --- |
| negate | boolean | Inverts the operation of the condition. Set to `true` to turn **equals** into **does not equal**.  If not set, then `false` is used. |
| values | integer[] | The value to compare to.  If several values are specified, the OR logic applies. |

```
{



"type": "INT_EQUALS",



"negate": false,



"values": [



128,



258,



512



]



}
```

### LESS\_THAN

LessThanCompareOperation

Parameters

JSON model

#### The `LessThanCompareOperation` object

The condition of the `LESS_THAN` type.

The condition checks whether the integer value is less than the specified value.

| Element | Type | Description |
| --- | --- | --- |
| value | integer | The value to compare to. |

```
{



"type": "LESS_THAN",



"value": 512



}
```

### GREATER\_THAN

GreaterThanCompareOperation

Parameters

JSON model

#### The `GreaterThanCompareOperation` object

The condition of the `GREATER_THAN` type.

The condition checks whether the integer value is greater than the specified value.

| Element | Type | Description |
| --- | --- | --- |
| value | integer | The value to compare to. |

```
{



"type": "GREATER_THAN",



"value": 256



}
```

## Variations of the `TransformationBase` object

The `TransformationBase` object is the base for all transformation operations. The actual set of fields depends on the **type** of the transformation.

### BEFORE

BeforeTransformation

Parameters

JSON model

#### The `BeforeTransformation` object

The transformation of the `BEFORE` type.

The transformation keeps the value before the specified delimiter and removes everything after it.

| Element | Type | Description |
| --- | --- | --- |
| delimiter | string | The delimiter of the transformation. The transformation keeps everything before this delimiter and removes everything after it.  The delimiter itself is not kept.  If several delimiters appear in the initial value, only the first one is used. |

```
{



"type": "BEFORE",



"delimiter": "/"



}
```

### AFTER

AfterTransformation

Parameters

JSON model

#### The `AfterTransformation` object

The transformation of the `AFTER` type.The transformation removes everything before the specified delimiter and keeps the value after it.

| Element | Type | Description |
| --- | --- | --- |
| delimiter | string | The delimiter of the transformation. The transformation removes everything before this delimiter and keeps everything after it.  The delimiter itself is not kept.  If several delimiters appear in the initial value, only the first one is used. |

```
{



"type": "AFTER",



"delimiter": "/"



}
```

### BETWEEN

BetweenTransformation

Parameters

JSON model

#### The `BetweenTransformation` object

The transformation of the `BETWEEN` type.The transformation keeps value between the specified delimiters and removes everything outside them.

| Element | Type | Description |
| --- | --- | --- |
| after | string | The starting delimiter. The transformation removes everything before it. The delimiter itself is not kept. |
| before | string | The ending delimiter. The transformation removes everything after it. The delimiter itself is not kept. |

```
{



"type": "BETWEEN",



"after": "support",



"before": "/"



}
```

### REPLACE\_BETWEEN

ReplaceBetweenTransformation

Parameters

JSON model

#### The `ReplaceBetweenTransformation` object

The transformation of the `REPLACE_BETWEEN` type.

The transformation replaces the content in between specified delimiters with the specified value. The rest of the string remains intact.

| Element | Type | Description |
| --- | --- | --- |
| after | string | The starting delimiter. The transformation replaces everything from here until ending delimiter. The delimiter itself remain intact. |
| before | string | The ending delimiter. The transformation replaces everything from starting delimiter until here. The delimiter itself remain intact. |
| replacement | string | The value to be used instead of the content between delimiters. |

```
{



"type": "REPLACE_BETWEEN",



"after": "support",



"before": "/",



"replacement": "newValue"



}
```

### REMOVE\_NUMBERS

RemoveNumbersTransformation

Parameters

JSON model

#### The `RemoveNumbersTransformation` object

The transformation of the `REMOVE_NUMBERS` type.

The transformation removes any numbers from the detected value.

| Element | Type | Description |
| --- | --- | --- |
| includeHexNumbers | boolean | Remove (`true`) or keep (`false`) hexadecimal numbers.  If not set, then `false` is used, keeping hexadecimal numbers. |
| minDigitCount | integer | Remove numbers that contain at least *X* digits. |

```
{



"type": "REMOVE_NUMBERS",



"minDigitCount": 2,



"includeHexNumbers": true



}
```

### REMOVE\_CREDIT\_CARDS

RemoveCreditCardNumbersTransformation

Parameters

JSON model

#### The `RemoveCreditCardNumbersTransformation` object

The transformation of the `REMOVE_CREDIT_CARDS` type.

The transformation automatically detects and removes credit card numbers. No additional parameters needed.

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation The element can hold these values * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

```
{



"type": "REMOVE_CREDIT_CARDS"



}
```

### REMOVE\_IBANS

RemoveIBANsTransformation

Parameters

JSON model

#### The `RemoveIBANsTransformation` object

The transformation of the `REMOVE_IBANS` type.

The transformation automatically detects and removes International Bank Account Numbers (IBAN). No additional parameters needed.

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation The element can hold these values * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

```
{



"type": "REMOVE_IBANS"



}
```

### REMOVE\_IPS

RemoveIPsTransformation

Parameters

JSON model

#### The `RemoveIPsTransformation` object

The transformation of the `REMOVE_IPS` type.

The transformation automatically detects and removes IP addresses. No additional parameters needed.

| Element | Type | Description |
| --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation The element can hold these values * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

```
{



"type": "REMOVE_IPS"



}
```

### SPLIT\_SELECT

SplitSelectTransformation

Parameters

JSON model

#### The `SplitSelectTransformation` object

The transformation of the `SPLIT_SELECT` type.

The transformation splits the detected value into an array and keeps the specified element of the array.

| Element | Type | Description |
| --- | --- | --- |
| delimiter | string | The delimiter for splitting the detected value. The delimiter itself is not kept. |
| itemIndex | integer | The index of the element in the split array to be used. Indexing starts with `1`. |

```
{



"type": "SPLIT_SELECT",



"delimiter": "/",



"itemIndex": 2



}
```

### TAKE\_SEGMENTS

TakeSegmentsTransformation

Parameters

JSON model

#### The `TakeSegmentsTransformation` object

The transformation of the `TAKE_SEGMENTS` type.

The transformation splits the detected value into an array and keeps the specified number of first or last elements.

| Element | Type | Description |
| --- | --- | --- |
| delimiter | string | The delimiter for splitting the detected value. The delimiter itself is not kept. |
| segmentCount | integer | The number of elements to be kept. |
| takeFromEnd | boolean | Keeps the first (`false`) or last (`true`) elements.  If not set, then `false` is used, keeping the first elements. |

```
{



"type": "TAKE_SEGMENTS",



"delimiter": "/",



"takeFromEnd": false



}
```