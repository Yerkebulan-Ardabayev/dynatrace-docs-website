---
title: Services API - GET a service
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service
scraped: 2026-02-18T21:24:51.720068
---

# Services API - GET a service

# Services API - GET a service

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the parameters of a specified service.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required service. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Service](#openapi-definition-Service) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Service` object

| Element | Type | Description |
| --- | --- | --- |
| agentTechnologyType | string | -The element can hold these values * `APACHE` * `DOTNET` * `DUMPPROC` * `GO` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `N/A` * `NET` * `NETTRACER` * `NGINX` * `NODEJS` * `OPENTRACINGNATIVE` * `OS` * `PHP` * `PLUGIN` * `PROCESS` * `PYTHON` * `REMOTE_PLUGIN` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `WSMB` * `Z` |
| akkaActorSystem | string | The services of the akka actor system. |
| className | string | - |
| contextRoot | string | - |
| customizedName | string | The customized name of the entity |
| databaseHostNames | string[] | - |
| databaseName | string | - |
| databaseVendor | string | - |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| esbApplicationName | string | The ESB application name. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| ibmCtgGatewayUrl | string | The IBM CTG gateway URL. |
| ibmCtgServerName | string | The IBM CICS Transaction Gateway name. |
| iibApplicationName | string | The IIB application name. |
| ipAddresses | string[] | - |
| isExternalService | boolean | - |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| path | string | - |
| port | integer | - |
| publicDomainName | object | Public domain name. |
| remoteEndpoint | string | The endpoint of the remote service. |
| remoteServiceName | string | The name of the remote service. |
| serviceDetectionAttributes | object | Attributes that contributed to the service id. |
| serviceTechnologyTypes | string[] | - |
| serviceType | string | -The element can hold these values * `Cics` * `CicsInteraction` * `CustomApplication` * `Database` * `EnterpriseServiceBus` * `External` * `Ims` * `ImsInteraction` * `Messaging` * `Method` * `Mobile` * `Process` * `QueueInteraction` * `QueueListener` * `RemoteCall` * `Rmi` * `SaasVendor` * `Span` * `Unified` * `Unknown` * `WebRequest` * `WebService` * `WebSite` * `ZosConnect` |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| webApplicationId | string | - |
| webServerName | string | - |
| webServiceName | string | - |
| webServiceNamespace | string | - |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TechnologyInfo` object

| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"agentTechnologyType": "APACHE",



"akkaActorSystem": "string",



"className": "string",



"contextRoot": "string",



"customizedName": "string",



"databaseHostNames": [



"string"



],



"databaseName": "string",



"databaseVendor": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esbApplicationName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



],



"runsOn": [



"string"



],



"runsOnProcessGroupInstance": [



"string"



]



},



"ibmCtgGatewayUrl": "string",



"ibmCtgServerName": "string",



"iibApplicationName": "string",



"ipAddresses": [



"string"



],



"isExternalService": true,



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"path": "string",



"port": 1,



"publicDomainName": {},



"remoteEndpoint": "string",



"remoteServiceName": "string",



"serviceDetectionAttributes": {},



"serviceTechnologyTypes": [



"string"



],



"serviceType": "Cics",



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"calls": [



"string"



]



},



"webApplicationId": "string",



"webServerName": "string",



"webServiceName": "string",



"webServiceNamespace": "string"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Example

In this example, the request gets the details of the **PHP-FPM via domain socket /run/php7-fpm.sock** service, which has the ID of **SERVICE-72503CBDD2AEF066**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066
```

#### Response body

```
{



"entityId": "SERVICE-72503CBDD2AEF066",



"displayName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"discoveredName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"firstSeenTimestamp": 1505902015554,



"lastSeenTimestamp": 1546010106998,



"tags": [],



"fromRelationships": {



"runsOnProcessGroupInstance": [



"PROCESS_GROUP_INSTANCE-9BA70456D770536E",



"PROCESS_GROUP_INSTANCE-7E988C3503AE8803"



],



"runsOn": [



"PROCESS_GROUP-E5C3CC7EC1F80B5B"



]



},



"toRelationships": {



"calls": [



"SERVICE-5304CCF4AFBFF35E"



]



},



"agentTechnologyType": "N/A",



"serviceType": "WebRequest",



"softwareTechnologies": [



{



"type": "SQLITE",



"edition": null,



"version": null



},



{



"type": "PHP",



"edition": "FPM",



"version": "7.0.32"



},



{



"type": "PHP_FPM",



"edition": null,



"version": null



}



]



}
```

#### Response code

200

## Related topics

* [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")