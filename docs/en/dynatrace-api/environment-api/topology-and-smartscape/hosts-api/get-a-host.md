---
title: Hosts API - GET a host
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host
scraped: 2026-02-25T21:22:09.599718
---

# Hosts API - GET a host

# Hosts API - GET a host

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the parameters of the specified host.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/hosts/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/hosts/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the required host. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Host](#openapi-definition-Host) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Host` object

Information about the host.

| Element | Type | Description |
| --- | --- | --- |
| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Defines the version of the agent currently running on the entity. |
| amiId | string | - |
| autoInjection | string | Status of auto-injection The element can hold these values * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |
| autoScalingGroup | string | - |
| awsInstanceId | string | - |
| awsInstanceType | string | - |
| awsNameTag | string | The name inherited from AWS. |
| awsSecurityGroup | string[] | - |
| azureComputeModeName | string | -The element can hold these values * `DEDICATED` * `SHARED` |
| azureEnvironment | string | - |
| azureHostNames | string[] | - |
| azureResourceGroupName | string | - |
| azureResourceId | string | - |
| azureSiteNames | string[] | - |
| azureSku | string | -The element can hold these values * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |
| azureVmName | string | - |
| azureVmScaleSetName | string | - |
| azureVmSizeLabel | string | - |
| azureZone | string | - |
| beanstalkEnvironmentName | string | - |
| bitness | string | -The element can hold these values * `32bit` * `64bit` |
| boshAvailabilityZone | string | The Cloud Foundry BOSH availability zone. |
| boshDeploymentId | string | The Cloud Foundry BOSH deployment ID. |
| boshInstanceId | string | The Cloud Foundry BOSH instance ID. |
| boshInstanceName | string | The Cloud Foundry BOSH instance name. |
| boshName | string | The Cloud Foundry BOSH name. |
| boshStemcellVersion | string | The Cloud Foundry BOSH stemcell version. |
| cloudPlatformVendorVersion | string | Defines the cloud platform vendor version. |
| cloudType | string | -The element can hold these values * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |
| consumedHostUnits | string | Consumed Host Units. Applicable only for [Dynatrace classic licensingï»¿](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |
| cpuCores | integer | - |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| esxiHostName | string | - |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| gceInstanceId | string | The Google Compute Engine instance ID. |
| gceInstanceName | string | The Google Compute Engine instance name. |
| gceMachineType | string | The Google Compute Engine machine type. |
| gceProject | string | The Google Compute Engine project. |
| gceProjectId | string | The Google Compute Engine numeric project ID. |
| gcePublicIpAddresses | string[] | The public IP addresses of the Google Compute Engine. |
| gcpZone | string | The Google Cloud Platform Zone. |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | - |
| hypervisorType | string | -The element can hold these values * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPERV` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUALBOX` * `VMWARE` * `WPAR` * `XEN` |
| ipAddresses | string[] | - |
| isMonitoringCandidate | boolean | - |
| kubernetesCluster | string | The kubernetes cluster the entity is in. |
| kubernetesLabels | object | The kubernetes labels defined on the entity. |
| kubernetesNode | string | The kubernetes node the entity is in. |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| localHostName | string | - |
| localIp | string | - |
| logicalCpuCores | integer | - |
| logicalCpus | integer | The AIX instance logical CPU count. |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| monitoringMode | string | -The element can hold these values * `FULL_STACK` * `INFRASTRUCTURE` * `OFF` |
| networkZoneId | string | The ID of network zone the entity is in. |
| oneAgentCustomHostName | string | The custom name defined in OneAgent config. |
| openStackInstaceType | string | - |
| openstackAvZone | string | - |
| openstackComputeNodeName | string | - |
| openstackProjectName | string | - |
| openstackSecurityGroups | string[] | - |
| openstackVmName | string | - |
| osArchitecture | string | -The element can hold these values * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |
| osType | string | -The element can hold these values * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |
| osVersion | string | - |
| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | The versions of the PaaS agents currently running on the entity. |
| paasMemoryLimit | integer | - |
| paasType | string | -The element can hold these values * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |
| publicHostName | string | - |
| publicIp | string | - |
| scaleSetName | string | - |
| simultaneousMultithreading | integer | The AIX instance simultaneous threads count. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| userLevel | string | -The element can hold these values * `NON_SUPERUSER` * `NON_SUPERUSER_STRICT` * `SUPERUSER` |
| virtualCpus | integer | The AIX instance virtual CPU count. |
| vmwareName | string | - |
| zosCPUModelNumber | string | The CPU model number. |
| zosCPUSerialNumber | string | The CPU serial number. |
| zosLpaName | string | Name of the LPAR. |
| zosSystemName | string | Name of the system. |
| zosTotalGeneralPurposeProcessors | integer | Number of assigned processors for this LPAR. |
| zosTotalPhysicalMemory | integer | Memory assigned to the host (Terabyte). |
| zosTotalZiipProcessors | integer | Number of assigned support processors for this LPAR. |
| zosVirtualization | string | Type of virtualization on the mainframe. |

#### The `AgentVersion` object

Defines the version of the agent currently running on the entity.

| Element | Type | Description |
| --- | --- | --- |
| major | integer | The major version number. |
| minor | integer | The minor version number. |
| revision | integer | The revision number. |
| sourceRevision | string | A string representation of the SVN revision number. |
| timestamp | string | A timestamp string: format "yyyymmdd-hhmmss |

#### The `HostGroup` object

| Element | Type | Description |
| --- | --- | --- |
| meId | string | The Dynatrace entity ID of the host group. |
| name | string | The name of the Dynatrace entity, displayed in the UI. |

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



"agentVersion": {



"major": 1,



"minor": 1,



"revision": 1,



"sourceRevision": "string",



"timestamp": "string"



},



"amiId": "string",



"autoInjection": "DISABLED_MANUALLY",



"autoScalingGroup": "string",



"awsInstanceId": "string",



"awsInstanceType": "string",



"awsNameTag": "string",



"awsSecurityGroup": [



"string"



],



"azureComputeModeName": "DEDICATED",



"azureEnvironment": "string",



"azureHostNames": [



"string"



],



"azureResourceGroupName": "string",



"azureResourceId": "string",



"azureSiteNames": [



"string"



],



"azureSku": "BASIC",



"azureVmName": "string",



"azureVmScaleSetName": "string",



"azureVmSizeLabel": "string",



"azureZone": "string",



"beanstalkEnvironmentName": "string",



"bitness": "32bit",



"boshAvailabilityZone": "string",



"boshDeploymentId": "string",



"boshInstanceId": "string",



"boshInstanceName": "string",



"boshName": "string",



"boshStemcellVersion": "string",



"cloudPlatformVendorVersion": "string",



"cloudType": "AZURE",



"consumedHostUnits": "string",



"cpuCores": 1,



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esxiHostName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isNetworkClientOfHost": [



"string"



]



},



"gceInstanceId": "string",



"gceInstanceName": "string",



"gceMachineType": "string",



"gceProject": "string",



"gceProjectId": "string",



"gcePublicIpAddresses": [



"string"



],



"gcpZone": "string",



"hostGroup": {



"meId": "string",



"name": "string"



},



"hypervisorType": "AHV",



"ipAddresses": [



"string"



],



"isMonitoringCandidate": true,



"kubernetesCluster": "string",



"kubernetesLabels": {},



"kubernetesNode": "string",



"lastSeenTimestamp": 1,



"localHostName": "string",



"localIp": "string",



"logicalCpuCores": 1,



"logicalCpus": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"monitoringMode": "FULL_STACK",



"networkZoneId": "string",



"oneAgentCustomHostName": "string",



"openStackInstaceType": "string",



"openstackAvZone": "string",



"openstackComputeNodeName": "string",



"openstackProjectName": "string",



"openstackSecurityGroups": [



"string"



],



"openstackVmName": "string",



"osArchitecture": "ARM",



"osType": "AIX",



"osVersion": "string",



"paasAgentVersions": [



{}



],



"paasMemoryLimit": 1,



"paasType": "AWS_ECS_EC2",



"publicHostName": "string",



"publicIp": "string",



"scaleSetName": "string",



"simultaneousMultithreading": 1,



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



"isNetworkClientOfHost": [



"string"



],



"isProcessOf": [



"string"



],



"isSiteOf": [



"string"



],



"runsOn": [



"string"



]



},



"userLevel": "NON_SUPERUSER",



"virtualCpus": 1,



"vmwareName": "string",



"zosCPUModelNumber": "string",



"zosCPUSerialNumber": "string",



"zosLpaName": "string",



"zosSystemName": "string",



"zosTotalGeneralPurposeProcessors": 1,



"zosTotalPhysicalMemory": 1,



"zosTotalZiipProcessors": 1,



"zosVirtualization": "string"



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

In this example, the request queries the parameters of the **tag009** host, which has the ID of **HOST-B7A6F9EE9F366CB5**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5
```

#### Response body

```
{



"entityId": "HOST-B7A6F9EE9F366CB5",



"displayName": "tag009",



"discoveredName": "tag009",



"firstSeenTimestamp": 1538473087608,



"lastSeenTimestamp": 1538641647769,



"tags": [



{



"context": "CONTEXTLESS",



"key": "loadtest"



},



{



"context": "CONTEXTLESS",



"key": "host tag"



}



],



"fromRelationships": {



"isNetworkClientOfHost": [



"HOST-80FF8584D8954C1D",



"HOST-A281F848361E79A1"



]



},



"toRelationships": {



"isProcessOf": [



"PROCESS_GROUP_INSTANCE-9146FB8A6A155F93"



],



"isSiteOf": [



"GEOLOC_SITE-F72DF471AE5F56F6"



],



"isNetworkClientOfHost": [



"HOST-80FF8584D8954C1D"



],



"runsOn": [



"PROCESS_GROUP-83D74C22E79B074F"



]



},



"osType": "LINUX",



"osArchitecture": "X86",



"osVersion": "Ubuntu 18.04.1",



"ipAddresses": [



"127.0.0.1",



"192.168.1.1"



],



"bitness": "64bit",



"cpuCores": 4,



"logicalCpuCores": 8,



"consumedHostUnits": 2,



"managementZones": [



{



"id": "6164525246045854296",



"name": "Zone Service E"



},



{



"id": "5678",



"name": "Infrastructure Linux"



}



]



}
```

#### Response code

200

## Related topics

* [Hosts Classic](/docs/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")