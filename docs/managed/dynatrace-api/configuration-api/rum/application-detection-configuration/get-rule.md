---
title: Applications detection rules API - GET a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-rule
scraped: 2026-05-12T11:16:04.817144
---

# Applications detection rules API - GET a rule

# Applications detection rules API - GET a rule

* Reference
* Published Aug 30, 2019

Gets parameters of the specified application detection rule.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required application detection rule. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ApplicationDetectionRuleConfig](#openapi-definition-ApplicationDetectionRuleConfig) | Success |

### Response body objects

#### The `ApplicationDetectionRuleConfig` object

Application detection rule.

| Element | Type | Description |
| --- | --- | --- |
| applicationIdentifier | string | The Dynatrace entity ID of the application, for example `APPLICATION-4A3B43`.  You must use an existing ID. If you need to create a rule for an application that doesn't exist yet, [create an application firstï»¿](https://dt-url.net/vt03khh) and then configure detection rules for it. |
| filterConfig | [ApplicationFilter](#openapi-definition-ApplicationFilter) | The condition of an application detection rule. |
| id | string | The ID of the rule. |
| metadata | [ConfigurationMetadataDtoImpl](#openapi-definition-ConfigurationMetadataDtoImpl) | Metadata useful for debugging. |
| name | string | The unique name of the Application detection rule. |
| order | string | The order of the rule in the rules list.  The rules are evaluated from top to bottom. The first matching rule applies. |

#### The `ApplicationFilter` object

The condition of an application detection rule.

| Element | Type | Description |
| --- | --- | --- |
| applicationMatchTarget | string | Where to look for the the **pattern** value. The element can hold these values * `DOMAIN` * `URL` |
| applicationMatchType | string | The operator of the matching. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `MATCHES` |
| pattern | string | The value to look for. |

#### The `ConfigurationMetadataDtoImpl` object

Metadata useful for debugging.

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

### Response body JSON models

```
{



"applicationIdentifier": "APPLICATION-123456",



"filterConfig": {



"applicationMatchTarget": "DOMAIN",



"applicationMatchType": "EQUALS",



"pattern": "myapp.example.com"



},



"id": "12345678-abcd-1234-abcd-1234567890ab",



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"name": "uniqueName"



}
```

## Example

In this example, the request gets the properties of the **easyTravel** rule, which has the ID **95b22afb-4e3d-4f9f-a37d-81bc3d388a33**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/95b22afb-4e3d-4f9f-a37d-81bc3d388a33 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/95b22afb-4e3d-4f9f-a37d-81bc3d388a33
```

#### Response body

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.188.0.20200203-155649"



},



"id": "95b22afb-4e3d-4f9f-a37d-81bc3d388a33",



"applicationIdentifier": "APPLICATION-900C1E36674F607D",



"filterConfig": {



"pattern": "easyTravel",



"applicationMatchType": "EQUALS",



"applicationMatchTarget": "DOMAIN"



}



}
```

#### Response code

200

## Related topics

* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [Check application detection rules](/managed/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Easily understand the detection rules of your RUM application.")
* [Define applications for Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")