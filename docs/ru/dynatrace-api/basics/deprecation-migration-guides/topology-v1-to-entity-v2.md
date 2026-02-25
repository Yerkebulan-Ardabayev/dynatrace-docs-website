---
title: Migrate from Topology and Smartscape API to Monitored entities API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2
scraped: 2026-02-25T21:22:12.249202
---

# Migrate from Topology and Smartscape API to Monitored entities API

# Migrate from Topology and Smartscape API to Monitored entities API

* Reference
* Published Mar 22, 2023

The [Topology and Smartscape API](/docs/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.") has been deprecated with [Dynatrace version 1.263](/docs/whats-new/dynatrace-api/sprint-242 "Changelog for Dynatrace API version 1.242"). Its replacement is the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API."). We recommend that you migrate to the new API at your earliest convenience.

This migration affects endpoint URLs, query parameters, and response/request body parameters, as well as the scope of the token for request authentication.

## New features

The Monitored entities API offers you the following new features:

* Entity type agnostic endpointâyou can query every type of entity via the same URL
* Powerful [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") that helps you to filter entities you want to read
* Unified timeframe selector
* Customizable return valueâyou can control which entity properties are included in the response
* Entity types endpoints
* Custom tags endpoints

## Base URL

| new Monitored entities | old Topology and Smartscape |
| --- | --- |
| `/api/v2/entities` | `/api/v1/entity/applications` `/api/v1/entity/infrastrucutre/hosts` `/api/v1/entity/infrastrucutre/processes` `/api/v1/entity/infrastrucutre/process-groups` `/api/v1/entity/services` |
| `/api/v2/entities/custom` | `/api/v1/entity/infrastructure/custom/{customDeviceId}` |
| `/api/v2/tags` | `/api/v1/entity/applications/{meIdentifier}` `/api/v1/entity/infrastrucutre/hosts/{meIdentifier}` `/api/v1/entity/infrastrucutre/process-groups/{meIdentifier}` `/api/v1/entity/services/{meIdentifier}` |

## Authentication token scope

| new Monitored entities | old Topology and Smartscape |
| --- | --- |
| **Read entities** (`entities.read`) **Write entities** (`entities.write`) | **Access problem and event feed, metrics, and topology** (`DataExport`) |

## Parameters

To learn about new query/body parameters, see the documentation of individual requests in [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.").

## Changes in workflow

With the upgrade to the Monitored entities API, some workflows require sending additional requests or calling additional endpoints. Be sure to adapt your automation accordingly.

### Pagination

When you query entities in a bulk, pagination is used to reduce the payload size.

1. Specify the number of entities per page in the **pageSize** query parameter.
2. Use the cursor from the **nextPageKey** field of the previous response in the **nextPageKey** query parameter to obtain subsequent pages.

### Create custom devices

In the Monitored entities API, you can't assign tags to the custom device upon creation. If you need to assign tags to your custom device, use a separate request to the [POST custom tags](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.") endpoint.

### Report data to custom devices

In the Monitored entities API, you can't report data to custom devices. Use the [POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") call instead.

## Examples

Here are some examples of differences in API usage.

### List entities

In this example, we're querying the list of hosts that were active within the last 2 hours. Also, we don't need the full information about the host: we only need monitoring mode and the list of tags, assigned to the host. The result is truncated to two entries.

Compare the following tabs to see how we do this using the new Monitored entities API and the deprecated Topology and Smartscape API:

Monitored entities API

Topology and Smartscape API

In the Monitored entities API:

* You can control which fields are returned (via the **fields** parameter). In this example, we use the **monitoringMode** and **tags** fields. Type, display name, and entity ID are always included in the response.
* The timeframe is defined via the **from** query parameter. It supports multiple formats; see the individual request documentation to learn more about them.
* The result of the query is split into pages. You can control the page size with the **pageSize** parameter. In this example, the parameter is not set; therefore, the default of 50 entries per page is used.

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities?fields=properties.monitoringMode,tags&entitySelector=type(%22HOST%22)&from=now-2h
```

#### Query parameters

```
fields=properties.monitoringMode,tags



entitySelector=type("HOST")



from=now-2h
```

#### Response body

```
{



"totalCount": 85,



"pageSize": 50,



"nextPageKey": "AQAMdHlwZSgiSE9TV==",



"entities": [



{



"entityId": "HOST-01A00204B50FF735",



"type": "HOST",



"displayName": "easytravel-backend.internal",



"properties": {



"monitoringMode": "FULL_STACK"



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "Stage",



"value": "PreProduction",



"stringRepresentation": "Stage:PreProduction"



},



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Linux",



"stringRepresentation": "OS:Linux"



},



{



"context": "CONTEXTLESS",



"key": "backend",



"stringRepresentation": "backend"



}



]



},



{



"entityId": "HOST-0AF138A0258C7DFF",



"type": "HOST",



"displayName": "easytravel-frontend.prod",



"properties": {



"monitoringMode": "FULL_STACK"



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "Stage",



"value": "Production",



"stringRepresentation": "Stage:Production"



},



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Windows",



"stringRepresentation": "OS:Windows"



},



{



"context": "CONTEXTLESS",



"key": "frontend",



"stringRepresentation": "frontend"



}



]



}



]



}
```

In the Topology and Smartscape API:

* You have limited control over returned fieldsâyou can use **includeDetails** to remove some properties, but you can't select particular fields to be included.
* The timeframe is defined via the **relativeTime** query parameter, which provides a limited amount of pre-defined values. Alternatively, you can use **startTimestamp** and **endTimestamp** fields. Additionally, the timeframe size is restricted to 3 days.
* All the entities are returned in a single payload; pagination is not available.

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts?relativeTime=2hours&includeDetails=false
```

#### Query parameters

```
relativeTime=2hours



includeDetails=false
```

#### Response body

```
[



{



"entityId": "HOST-01A00204B50FF735",



"displayName": "easytravel-backend.internal",



"discoveredName": "APM-ET-MF2",



"firstSeenTimestamp": 1627476376157,



"lastSeenTimestamp": 1679410093531,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Stage",



"value": "PreProduction"



},



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Linux"



},



{



"context": "CONTEXTLESS",



"key": "backend"



}



],



"fromRelationships": {},



"toRelationships": {},



"osType": "LINUX",



"osArchitecture": "X86",



"osVersion": "Ubuntu 20.04.1 LTS (Focal Fossa) (kernel 5.4.0-135-generic)",



"hypervisorType": "VMWARE",



"ipAddresses": [



"192.168.0.1"



],



"bitness": "64bit",



"cpuCores": 4,



"logicalCpuCores": 4,



"monitoringMode": "FULL_STACK",



"networkZoneId": "default",



"agentVersion": {



"major": 1,



"minor": 259,



"revision": 339,



"timestamp": "20230228-182655",



"sourceRevision": ""



},



"consumedHostUnits": 2.0,



"userLevel": "SUPERUSER",



"autoInjection": "ENABLED",



"oneAgentCustomHostName": "easytravel-backend.internal",



"managementZones": [



{



"id": "460039148655162069",



"name": "backend"



}



]



},



{



"entityId": "HOST-0AF138A0258C7DFF",



"displayName": "easytravel-frontend.prod",



"firstSeenTimestamp": 1619706183299,



"lastSeenTimestamp": 1679409948352,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Stage",



"value": "Production",



"stringRepresentation": "Stage:Production"



},



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Windows",



"stringRepresentation": "OS:Windows"



},



{



"context": "CONTEXTLESS",



"key": "frontend",



"stringRepresentation": "frontend"



}



],



"fromRelationships": {},



"toRelationships": {},



"osType": "WINDOWS",



"osArchitecture": "X86",



"osVersion": "Windows Server 2008 R2 Datacenter Service Pack 1, ver. 6.1.7601",



"hypervisorType": "XEN",



"ipAddresses": [



"192.168.0.2",



"192.168.0.3"



],



"bitness": "64bit",



"cpuCores": 1,



"logicalCpuCores": 2,



"cloudType": "EC2",



"monitoringMode": "FULL_STACK",



"networkZoneId": "default",



"agentVersion": {



"major": 1,



"minor": 247,



"revision": 277,



"timestamp": "20221006-094946",



"sourceRevision": ""



},



"consumedHostUnits": 0.5,



"userLevel": "SUPERUSER",



"autoInjection": "ENABLED",



"softwareTechnologies": [



{



"type": "CITRIX",



"edition": null,



"version": null



}



],



"managementZones": [



{



"id": "-4279023605659327282",



"name": "frontend"



}



]



}



]
```

### Assign entity tags



In this example, we assign additional tags (**Datacenter:Linz** and **Rack:014**) to hosts from the list entities example.

Compare the following tabs to see how we do this using the new Monitored entities API and the deprecated Topology and Smartscape API:

Monitored entities API

Topology and Smartscape API

In the new Monitored entities API, you can assign tags to multiple entities at the same time by selecting them via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints."). In this example, we select hosts by their entity IDs.

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=entityId(%22HOST-01A00204B50FF735%22,%22HOST-0AF138A0258C7DFF%22)
```

#### Query parameters

```
entitySelector=entityId("HOST-01A00204B50FF735","HOST-0AF138A0258C7DFF")
```

#### Request body

```
{



"tags": [



{



"key": "Datacenter",



"value": "Linz"



},



{



"key": "Rack",



"value": "014"



}



]



}
```

#### Response body

```
{



"matchedEntitiesCount": 2,



"appliedTags": [



{



"context": "CONTEXTLESS",



"key": "Datacenter",



"value": "Linz",



"stringRepresentation": "Datacenter:Linz"



},



{



"context": "CONTEXTLESS",



"key": "Rack",



"value": "014",



"stringRepresentation": "Rack:014"



}



]



}
```

In the deprecated Topology and Smartscape API, you can assign tags to one entity at a time. The example shows the tag assignment for only one of two hosts. A second request with the same payload is needed to assign tags to another host.

Moreover, the tags are not stored in the `key:value` format. You can only set the `key` part of the tag via this API.

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-01A00204B50FF735
```

#### Request body

```
{



"tags": [



"Datacenter:Linz",



"Rack:014"



]



}
```

### Create custom devices

In this example, we create a custom device with the ID of `restExample` and the following parameters:

* type: `F5-Firewall`
* IP address `172.16.115.211`
* listen port `9999`

Compare the following tabs to see how we do this using the new Monitored entities API and the deprecated Topology and Smartscape API:

Monitored entities API

Topology and Smartscape API

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities/custom
```

#### Request body

```
{



"customDeviceId": "restExample",



"displayName": "F5 Firewall 24",



"ipAddresses": ["172.16.115.211"],



"listenPorts": ["9999"],



"type": "F5-Firewall",



"favicon": "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl": "http://192.128.0.1:8080",



"properties": {



"Sample Property 1": "Sample value 1"



}



}
```

#### Response body

```
{



"entityId": "CUSTOM_DEVICE-1525F193C0578E2C",



"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"



}
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/restExample
```

#### Request body

```
{



"displayName": "F5 Firewall 24",



"ipAddresses": ["172.16.115.211"],



"listenPorts": ["9999"],



"type": "F5-Firewall",



"favicon": "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl": "http://192.128.0.1:8080",



"tags": ["REST example"],



"properties": {



"Sample Property 1": "Sample value 1"



}



}
```

#### Response body

```
{



"entityId": "CUSTOM_DEVICE-6A567B33AADC306E",



"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"



}
```

## Related topics

* [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.")
* [Tokens API v1](/docs/dynatrace-api/environment-api/tokens-v1 "Learn how to manage Dynatrace API authentication tokens in your environment.")