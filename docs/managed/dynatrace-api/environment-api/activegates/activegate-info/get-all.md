---
title: ActiveGate API - GET all ActiveGates
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/activegate-info/get-all
---

# ActiveGate API - GET all ActiveGates

# ActiveGate API - GET all ActiveGates

* Reference
* Published Jul 02, 2020

Lists all ActiveGates that are currently connected to the environment or have been connected during the last 2 hours.

You can narrow down the output by specifying filtering parameters in your request.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates` |

## Authentication

To execute this request, you need an access token with `activeGates.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| hostname | string | Filters the resulting set of ActiveGates by the name of the host it's running on.  You can specify a partial name. In that case, the `CONTAINS` operator is used. | query | Optional |
| osType | string | Filters the resulting set of ActiveGates by the OS type of the host it's running on. The element can hold these values * `LINUX` * `WINDOWS` | query | Optional |
| osArchitecture | string | Filters the resulting set of ActiveGates by the OS architecture of the host it's running on. The element can hold these values * `X86` * `S390` * `ARM` * `PPCLE` | query | Optional |
| networkAddress | string | Filters the resulting set of ActiveGates by the network address.  You can specify a partial address. In that case, the `CONTAINS` operator is used. | query | Optional |
| loadBalancerAddress | string | Filters the resulting set of ActiveGates by the Load Balancer address.  You can specify a partial address. In that case, the `CONTAINS` operator is used. | query | Optional |
| type | string | Filters the resulting set of ActiveGates by the ActiveGate type. The element can hold these values * `ENVIRONMENT` * `ENVIRONMENT_MULTI` | query | Optional |
| networkZone | string | Filters the resulting set of ActiveGates by the network zone.  You can specify a partial name. In that case, the `CONTAINS` operator is used. | query | Optional |
| updateStatus | string | Filters the resulting set of ActiveGates by the auto-update status. The element can hold these values * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` | query | Optional |
| versionCompareType | string | Filters the resulting set of ActiveGates by the specified version.  Specify the comparison operator here. The element can hold these values * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Optional |
| version | string | Filters the resulting set of ActiveGates by the specified version.  Specify the version in `<major>.<minor>.<revision>` format (for example, `1.195.0`) here. | query | Optional |
| autoUpdate | string | Filters the resulting set of ActiveGates by the actual state of auto-update. The element can hold these values * `DISABLED` * `ENABLED` | query | Optional |
| group | string | Filters the resulting set of ActiveGates by the group.  You can specify a partial name. In that case, the `CONTAINS` operator is used. | query | Optional |
| online | boolean | Filters the resulting set of ActiveGates by the communication status. | query | Optional |
| enabledModule | string[] | Filters the resulting set of ActiveGates by the enabled modules. The element can hold these values * `AWS` * `AZURE` * `BEACON_FORWARDER` * `CLOUD_FOUNDRY` * `DB_INSIGHT` * `DEBUGGING` * `EXTENSIONS_V1` * `EXTENSIONS_V2` * `KUBERNETES` * `LOGS` * `MEMORY_DUMPS` * `METRIC_API` * `ONE_AGENT_ROUTING` * `OTLP_INGEST` * `REST_API` * `SYNTHETIC` * `VMWARE` * `Z_OS` | query | Optional |
| disabledModule | string[] | Filters the resulting set of ActiveGates by the disabled modules. The element can hold these values * `AWS` * `AZURE` * `BEACON_FORWARDER` * `CLOUD_FOUNDRY` * `DB_INSIGHT` * `DEBUGGING` * `EXTENSIONS_V1` * `EXTENSIONS_V2` * `KUBERNETES` * `LOGS` * `MEMORY_DUMPS` * `METRIC_API` * `ONE_AGENT_ROUTING` * `OTLP_INGEST` * `REST_API` * `SYNTHETIC` * `VMWARE` * `Z_OS` | query | Optional |
| containerized | boolean | Filters the resulting set of ActiveGates to those which are running in container (`true`) or not (`false`). | query | Optional |
| tokenState | string | Filters the resulting set of ActiveGates to those with authorization token in specified state. The element can hold these values * `ABSENT` * `EXPIRING` * `INVALID` * `UNKNOWN` * `UNSUPPORTED` * `VALID` | query | Optional |
| tokenExpirationSet | boolean | Filters the resulting set of ActiveGates to those with set expiration date for authorization token. | query | Optional |
| fipsMode | boolean | Filters the resulting set of ActiveGates to those which are running in FIPS mode (`true`) or not (`false`). | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ActiveGateList](#openapi-definition-ActiveGateList) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ActiveGateList` object

A list of ActiveGates.

| Element | Type | Description |
| --- | --- | --- |
| activeGates | [ActiveGate](#openapi-definition-ActiveGate)[] | A list of ActiveGates. |

#### The `ActiveGate` object

Parameters of the ActiveGate.

| Element | Type | Description |
| --- | --- | --- |
| activeGateTokens | [ActiveGateTokenInfoDto](#openapi-definition-ActiveGateTokenInfoDto)[] | A list of the ActiveGate tokens. |
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
| modules | [ActiveGateModule](#openapi-definition-ActiveGateModule)[] | A list of modules of the ActiveGate. |
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
| id | string | The ActiveGate token identifier, consisting of [prefix and public part﻿](https://dt-url.net/rn00tjg?dt=m) of the token. |
| state | string | State of the ActiveGate token. The element can hold these values * `ABSENT` * `EXPIRING` * `INVALID` * `UNKNOWN` * `UNSUPPORTED` * `VALID` |

#### The `ActiveGateAutoUpdateConfig` object

Configuration of the ActiveGate auto-updates.

| Element | Type | Description |
| --- | --- | --- |
| effectiveSetting | string | The actual state of the ActiveGate auto-update.  Applicable only if the **setting** parameter is set to `INHERITED`. In that case, the value is taken from the parent setting. Otherwise, it's just a duplicate of the **setting** value. The element can hold these values * `ENABLED` * `DISABLED` |
| setting | string | The state of the ActiveGate auto-update: enabled, disabled, or inherited.  If set to `INHERITED`, the setting is inherited from the global configuration set on the environment or Managed cluster level. The element can hold these values * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | The target version of the ActiveGate.  Specify the version in the `<major>.<minor>` format (for example `1.342`) or `latest`, `previous`, or `older`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Basic information about all configured update windows |

#### The `UpdateWindowsConfig` object

Basic information about all configured update windows

| Element | Type | Description |
| --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | List of update windows when the OneAgent update can start. If there is no value and update should be performed, the update will start at earliest convenience. |

#### The `UpdateWindow` object

Basic information about one maintenance window

| Element | Type | Description |
| --- | --- | --- |
| id | string | Identifier of maintenance window |
| name | string | The name of maintenance window |

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
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
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



"activeGates": [



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



"setting": "INHERITED",



"targetVersion": "latest",



"updateWindows": {



"windows": [



{



"id": "vu9U3hXa3q0AAAABADdkeW5hdHJhY2Uuc2V0dGluZ3MuZGVwbG95bWVudC5tYW5h",



"name": "Daily maintenance window"



}



]



}



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



]



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

In this example, the request lists all ActiveGates available for the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/activeGates' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/activeGates
```

#### Response body

```
{



"activeGates": [



{



"id": "1541791174",



"networkAddresses": [



"orange-15.easytravel.com",



"150.134.11.6"



],



"osType": "LINUX",



"autoUpdateStatus": "UP2DATE",



"offlineSince": null,



"version": "1.193.0.20200416-144858",



"type": "ENVIRONMENT",



"hostname": "orange-15.easytravel.com",



"mainEnvironment": null,



"environments": [



"mySampleEnv"



],



"networkZone": "default"



},



{



"id": "974977376",



"networkAddresses": [



"win-18.easytravel.com",



"66.165.59.105"



],



"osType": "WINDOWS",



"autoUpdateStatus": "OUTDATED",



"offlineSince": null,



"version": "1.198.0.20200629-221007",



"type": "ENVIRONMENT",



"hostname": "win-18.easytravel.com",



"mainEnvironment": null,



"environments": [



"mySampleEnv"



],



"networkZone": "default"



}



]



}
```

#### Response code

200

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")