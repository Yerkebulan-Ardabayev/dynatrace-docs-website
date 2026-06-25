---
title: ActiveGate API - GET an ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/activegate-info/get-activegate
scraped: 2026-05-12T11:55:45.610208
---

# ActiveGate API - GET an ActiveGate

# ActiveGate API - GET an ActiveGate

* Reference
* Published Jul 02, 2020

Gets the information about the specified ActiveGate.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}` |

## Authentication

To execute this request, you need an access token with `activeGates.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| agId | string | The ID of the required ActiveGate. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ActiveGate](#openapi-definition-ActiveGate) | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Not found. See response body for details. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ActiveGate` object

Parameters of the ActiveGate.

| Element | Type | Description |
| --- | --- | --- |
| activeGateTokens | [ActiveGateTokenInfoDto[]](#openapi-definition-ActiveGateTokenInfoDto) | A list of the ActiveGate tokens. |
| autoUpdateSettings | [ActiveGateAutoUpdateConfig](#openapi-definition-ActiveGateAutoUpdateConfig) | Configuration of the ActiveGate auto-updates. |
| autoUpdateStatus | string | The current status of auto-updates of the ActiveGate. The element can hold these values * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` |
| connectedHosts | [ActiveGateConnectedHosts](#openapi-definition-ActiveGateConnectedHosts) | Information about hosts currently connected to the ActiveGate |
| containerized | boolean | ActiveGate is deployed in container (`true`) or not (`false`). |
| environments | string[] | A list of environments (specified by IDs) the ActiveGate can connect to. |
| fipsMode | boolean | ActiveGate is running in FIPS compliant mode (`true`) or not (`false`). |
| group | string | The group of the ActiveGate. |
| hostname | string | The name of the host the ActiveGate is running on. |
| id | string | The ID of the ActiveGate. |
| loadBalancerAddresses | string[] | A list of Load Balancer addresses of the ActiveGate. |
| mainEnvironment | string | The ID of the main environment for a multi-environment ActiveGate. |
| modules | [ActiveGateModule[]](#openapi-definition-ActiveGateModule) | A list of modules of the ActiveGate. |
| networkAddresses | string[] | A list of network addresses of the ActiveGate. |
| networkZone | string | The network zone of the ActiveGate. |
| offlineSince | integer | The timestamp since when the ActiveGate is offline.  The `null` value means the ActiveGate is online. |
| osArchitecture | string | The OS architecture that the ActiveGate is running on. The element can hold these values * `S390` * `X86` * `ARM` * `PPCLE` |
| osBitness | string | The OS bitness that the ActiveGate is running on. The element can hold these values * `64` |
| osType | string | The OS type that the ActiveGate is running on. The element can hold these values * `LINUX` * `WINDOWS` |
| type | string | The type of the ActiveGate. The element can hold these values * `CLUSTER` * `ENVIRONMENT` * `ENVIRONMENT_MULTI` |
| version | string | The current version of the ActiveGate in the `<major>.<minor>.<revision>.<timestamp>` format. |

#### The `ActiveGateTokenInfoDto` object

Information about ActiveGate token.

| Element | Type | Description |
| --- | --- | --- |
| environmentId | string | The environment ID to which the token belongs.  Only available if more than one environment is supported. |
| id | string | The ActiveGate token identifier, consisting of [prefix and public partï»¿](https://dt-url.net/rn00tjg) of the token. |
| state | string | State of the ActiveGate token. The element can hold these values * `ABSENT` * `EXPIRING` * `INVALID` * `UNKNOWN` * `UNSUPPORTED` * `VALID` |

#### The `ActiveGateAutoUpdateConfig` object

Configuration of the ActiveGate auto-updates.

| Element | Type | Description |
| --- | --- | --- |
| effectiveSetting | string | The actual state of the ActiveGate auto-update.  Applicable only if the **setting** parameter is set to `INHERITED`. In that case, the value is taken from the parent setting. Otherwise, it's just a duplicate of the **setting** value. The element can hold these values * `ENABLED` * `DISABLED` |
| setting | string | The state of the ActiveGate auto-update: enabled, disabled, or inherited.  If set to `INHERITED`, the setting is inherited from the global configuration set on the environment or Managed cluster level. The element can hold these values * `DISABLED` * `ENABLED` * `INHERITED` |

#### The `ActiveGateConnectedHosts` object

Information about hosts currently connected to the ActiveGate

| Element | Type | Description |
| --- | --- | --- |
| number | integer | The number of hosts currently connected to the ActiveGate |

#### The `ActiveGateModule` object

Information about ActiveGate module

| Element | Type | Description |
| --- | --- | --- |
| attributes | object | The attributes of the ActiveGate module. |
| enabled | boolean | The module is enabled (`true`) or disabled (`false`). |
| misconfigured | boolean | The module is misconfigured (`true`) or not (`false`). |
| type | string | The type of ActiveGate module. The element can hold these values * `AWS` * `AZURE` * `BEACON_FORWARDER` * `CLOUD_FOUNDRY` * `DB_INSIGHT` * `DEBUGGING` * `EXTENSIONS_V1` * `EXTENSIONS_V2` * `KUBERNETES` * `LOGS` * `MEMORY_DUMPS` * `METRIC_API` * `ONE_AGENT_ROUTING` * `OTLP_INGEST` * `REST_API` * `SYNTHETIC` * `VMWARE` * `Z_OS` |
| version | string | The version of the ActiveGate module. |

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



"activeGateTokens": [



{



"environmentId": "string",



"id": "dt0g02.4KWZO5EF",



"state": "ABSENT"



}



],



"autoUpdateSettings": {



"effectiveSetting": "ENABLED",



"setting": "INHERITED"



},



"autoUpdateStatus": "OUTDATED",



"connectedHosts": {



"number": 150



},



"containerized": true,



"environments": [



"string"



],



"fipsMode": true,



"group": "default",



"hostname": "exampleHostname",



"id": "0x3efdd091",



"loadBalancerAddresses": [



"string"



],



"mainEnvironment": "d1bf4a7e-666b-43af-9f45-718g98372e2f",



"modules": [



{



"attributes": {},



"enabled": true,



"misconfigured": true,



"type": "KUBERNETES",



"version": "string"



}



],



"networkAddresses": [



"string"



],



"networkZone": "exampleNetworkZone",



"offlineSince": 1582031917814,



"osArchitecture": "X86",



"osBitness": "64",



"osType": "WINDOWS",



"type": "ENVIRONMENT",



"version": "1.185.0.20200201-120000"



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

In this example, the request lists the parameters of the ActiveGate with the ID of **876651882**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -L -X GET 'https://mySampleEnv/api/v2/activeGates/876651882' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv/api/v2/activeGates/876651882
```

#### Response body

```
{



"id": "876651882",



"networkAddresses": [



"orange-13.easytravel.com",



"228.245.125.39"



],



"osType": "LINUX",



"autoUpdateStatus": "UPDATE_IN_PROGRESS",



"offlineSince": null,



"version": "1.198.0.20200630-163221",



"type": "ENVIRONMENT",



"hostname": "orange-13.easytravel.com",



"mainEnvironment": null,



"environments": [



"mySampleEnv"



],



"networkZone": "easytravel.europe.austria.05"



}
```

#### Response code

200

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")