---
title: Processes API - GET all processes
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all
scraped: 2026-02-22T21:15:38.897038
---

# Processes API - GET all processes

# Processes API - GET all processes

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Fetches the list of all [processes](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") in your Dynatrace environment, along with their parameters and relationships.

The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.

You can additionally limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **Next-Page-Key** response header in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/processes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/processes` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The timeframe is restricted to a **maximum period of 3 days**.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |
| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |
| tag | string[] | Filters the resulting set of processes by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The process has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| entity | string[] | Filters result to the specified processes only.  To specify several processes use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| hostTag | string[] | Filters processes by the host they're running at.  Specify tags of the host you're interested in. | query | Optional |
| host | string[] | Filters processes by the host they're running at.  Specify Dynatrace IDs of the host you're interested in.  To specify several hosts use the following format: `host=hostID1&host=hostID2`.  The **OR** logic applies. | query | Optional |
| actualMonitoringState | string | Filters processes by the actual monitoring state of the process. The element can hold these values * `OFF` * `ON` | query | Optional |
| expectedMonitoringState | string | Filters processes by the expected monitoring state of the process. The element can hold these values * `OFF` * `ON` | query | Optional |
| managementZone | integer | Only return processes that are part of the specified management zone. | query | Optional |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| pageSize | integer | The number of processes per result page.  If not set, pagination is not used and the result contains all processes fitting the specified filtering criteria. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProcessGroupInstance[]](#openapi-definition-ProcessGroupInstance) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `ProcessGroupInstance` object

Parameters of a process.

| Element | Type | Description |
| --- | --- | --- |
| agentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Versions of OneAgents currently running on the entity. |
| azureHostName | string | - |
| azureSiteName | string | - |
| bitness | string | -The element can hold these values * `32bit` * `64bit` |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | - |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| listenPorts | integer[] | - |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| metadata | object | - |
| modules | string[] | - |
| monitoringState | [MonitoringState](#openapi-definition-MonitoringState) | Defines the current monitoring state of an entity. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |
| versionedModules | [ProcessGroupInstanceModule[]](#openapi-definition-ProcessGroupInstanceModule) | - |

#### The `AgentVersion` object

Defines the version of the agent currently running on the entity.

| Element | Type | Description |
| --- | --- | --- |
| major | integer | The major version number. |
| minor | integer | The minor version number. |
| revision | integer | The revision number. |
| sourceRevision | string | A string representation of the SVN revision number. |
| timestamp | string | A timestamp string: format "yyyymmdd-hhmmss |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `MonitoringState` object

Defines the current monitoring state of an entity.

| Element | Type | Description |
| --- | --- | --- |
| actualMonitoringState | string | The current actual monitoring state on the entity. The element can hold these values * `OFF` * `ON` |
| expectedMonitoringState | string | The monitoring state that is expected from the configuration The element can hold these values * `OFF` * `ON` |
| restartRequired | boolean | Defines whether or not the process has to restarted to enable monitoring |

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

#### The `ProcessGroupInstanceModule` object

| Element | Type | Description |
| --- | --- | --- |
| name | string | - |
| version | string | - |

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
[



{



"agentVersions": [



{



"major": 1,



"minor": 1,



"revision": 1,



"sourceRevision": "string",



"timestamp": "string"



}



],



"azureHostName": "string",



"azureSiteName": "string",



"bitness": "32bit",



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isInstanceOf": [



"string"



],



"isNetworkClientOf": [



"string"



],



"isProcessOf": [



"string"



]



},



"lastSeenTimestamp": 1,



"listenPorts": [



1



],



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"metadata": {



"adobe.em.env_type": [



"string"



],



"adobe.em.program": [



"string"



],



"adobe.em.service": [



"string"



],



"adobe.em.tier": [



"string"



],



"agentValueMetadata": {},



"apacheConfigPaths": [



"string"



],



"apacheSparkMasterIpAddresses": [



"string"



],



"aspDotNetCoreApplicationPaths": [



"string"



],



"awsEcrImageAccountIds": [



"string"



],



"awsEcrImageRegions": [



"string"



],



"awsEcsCluster": [



"string"



],



"awsEcsContainerARN": [



"string"



],



"awsEcsContainerName": [



"string"



],



"awsEcsDockerID": [



"string"



],



"awsEcsDockerName": [



"string"



],



"awsEcsFamily": [



"string"



],



"awsEcsRevision": [



"string"



],



"awsEcsTaskARN": [



"string"



],



"awsLambdaFunctionNames": [



"string"



],



"awsRegions": [



"string"



],



"azure.containerapp.dnssuffix": [



"string"



],



"azure.containerapp.hostname": [



"string"



],



"azure.containerapp.name": [



"string"



],



"azure.containerapp.replica.name": [



"string"



],



"azure.servicefabric.application.id": [



"string"



],



"azure.servicefabric.application.name": [



"string"



],



"azure.servicefabric.codepackage.name": [



"string"



],



"azure.servicefabric.hostedservice.name": [



"string"



],



"azure.servicefabric.instance.id": [



"string"



],



"azure.servicefabric.replica.id": [



"string"



],



"azure.servicefabric.servicepackage.name": [



"string"



],



"azure.spring.application.name": [



"string"



],



"azure.spring.cloudconfiguri": [



"string"



],



"azure.website.instance.id": [



"string"



],



"azure.website.owner.name": [



"string"



],



"azure.website.site.name": [



"string"



],



"cassandraClusterNames": [



"string"



],



"catalinaBaseValues": [



"string"



],



"catalinaHomeValues": [



"string"



],



"cloudFoundryAppIds": [



"string"



],



"cloudFoundryAppNames": [



"string"



],



"cloudFoundryInstanceIndexes": [



"string"



],



"cloudFoundrySpaceIds": [



"string"



],



"cloudFoundrySpaceNames": [



"string"



],



"cloudfoundryMetadata": {},



"coldfusionJvmConfigFiles": [



"string"



],



"commandLineArgs": [



"string"



],



"datasourceMonitoringConfigId": [



"string"



],



"declarativeConfigRuleId": [



"string"



],



"declarativeId": [



"string"



],



"dockerContainerIds": [



"string"



],



"dockerContainerImageNames": [



"string"



],



"dockerContainerImageVersions": [



"string"



],



"dockerContainerNames": [



"string"



],



"dotNetCommands": [



"string"



],



"dotnetCommandPath": [



"string"



],



"dynatraceClusterIds": [



"string"



],



"dynatraceNodeIds": [



"string"



],



"elasticSearchClusterNames": [



"string"



],



"elasticSearchNodeNames": [



"string"



],



"envVariables": {},



"equinoxConfigPath": [



"string"



],



"executablePaths": [



"string"



],



"executables": [



"string"



],



"glassfishDomainNames": [



"string"



],



"glassfishInstanceNames": [



"string"



],



"google.appengine.version": [



"string"



],



"google.cloudrun.execution": [



"string"



],



"google.cloudrun.job": [



"string"



],



"google.cloudrun.revision": [



"string"



],



"googleAppEngineInstances": [



"string"



],



"googleAppEngineServices": [



"string"



],



"googleCloudInstanceId": [



"string"



],



"googleCloudInstanceRegion": [



"string"



],



"googleCloudProjects": [



"string"



],



"googleCloudRunService": [



"string"



],



"googleComputeEngineMetadata": {},



"heroku.appdefaultdomainname": [



"string"



],



"heroku.dyno": [



"string"



],



"heroku.releaseversion": [



"string"



],



"hostGroups": [



"string"



],



"hybrisBinDirectories": [



"string"



],



"hybrisConfigDirectories": [



"string"



],



"hybrisDataDirectories": [



"string"



],



"ibmApplid": [



"string"



],



"ibmCicsImsApplid": [



"string"



],



"ibmCicsImsJobName": [



"string"



],



"ibmCicsRegion": [



"string"



],



"ibmCtgName": [



"string"



],



"ibmImsConnectRegions": [



"string"



],



"ibmImsControlRegions": [



"string"



],



"ibmImsMessageProcessingRegions": [



"string"



],



"ibmImsSoapGwName": [



"string"



],



"ibmIntegrationNodeName": [



"string"



],



"ibmIntegrationServerName": [



"string"



],



"ibmJobName": [



"string"



],



"iisAppPools": [



"string"



],



"iisRoleNames": [



"string"



],



"javaJarFiles": [



"string"



],



"javaJarPaths": [



"string"



],



"javaMainClasses": [



"string"



],



"javaMainModules": [



"string"



],



"jbossHomes": [



"string"



],



"jbossModes": [



"string"



],



"jbossServerNames": [



"string"



],



"kubernetesAnnotations": {},



"kubernetesBasePodNames": [



"string"



],



"kubernetesClusterId": [



"string"



],



"kubernetesContainerNames": [



"string"



],



"kubernetesFullPodNames": [



"string"



],



"kubernetesNamespaces": [



"string"



],



"kubernetesPodUids": [



"string"



],



"kubernetesRuleResult": [



"string"



],



"linkage": [



"string"



],



"mssqlInstanceName": [



"string"



],



"nodejsAppBaseDirectories": [



"string"



],



"nodejsAppNames": [



"string"



],



"nodejsScriptNames": [



"string"



],



"oracleSid": [



"string"



],



"osagent.groupIdName": [



"string"



],



"osagent.instanceIdName": [



"string"



],



"phpScripts": [



"string"



],



"phpWorkingDirectories": [



"string"



],



"pluginMetadata": {},



"pythonModule": [



"string"



],



"pythonScript": [



"string"



],



"pythonScriptPath": [



"string"



],



"rke2Type": [



"string"



],



"rubyAppRootPaths": [



"string"



],



"rubyScriptPaths": [



"string"



],



"ruleResult": [



"string"



],



"serviceNames": [



"string"



],



"softwareAgInstallRoot": [



"string"



],



"softwareAgProductPropertyName": [



"string"



],



"springBootAppName": [



"string"



],



"springBootProfileName": [



"string"



],



"springBootStartupClass": [



"string"



],



"tibcoBWEnginePropertyFilePaths": [



"string"



],



"tibcoBusinessWorksAppNodeName": [



"string"



],



"tibcoBusinessWorksAppSpaceName": [



"string"



],



"tibcoBusinessWorksCeAppName": [



"string"



],



"tibcoBusinessWorksCeVersion": [



"string"



],



"tibcoBusinessWorksDomainName": [



"string"



],



"tibcoBusinessWorksEnginePropertyFiles": [



"string"



],



"tibcoBusinessWorksHome": [



"string"



],



"varnishInstanceNames": [



"string"



],



"weblogicClusterNames": [



"string"



],



"weblogicDomainNames": [



"string"



],



"weblogicHomeValues": [



"string"



],



"weblogicNames": [



"string"



],



"websphereCellNames": [



"string"



],



"websphereClusterNames": [



"string"



],



"websphereLibertyServerName": [



"string"



],



"websphereNodeNames": [



"string"



],



"websphereServerNames": [



"string"



],



"zCodeModuleVersion": [



"string"



]



},



"modules": [



"string"



],



"monitoringState": {



"actualMonitoringState": "OFF",



"expectedMonitoringState": "OFF",



"restartRequired": true



},



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



"isNetworkClientOf": [



"string"



],



"runsOnProcessGroupInstance": [



"string"



]



},



"versionedModules": [



{



"name": "string",



"version": "string"



}



]



}



]
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

## Response headers

| Header | Type | Description |
| --- | --- | --- |
| Total-Count | integer | The estimated number of results. |
| Next-Page-Key | string | The cursor for the next page of results. Without it you'll get the first page again. |
| Page-Size | string | The maximum number of results per page. |

## Example

In this example, the request lists all processes in your Dynatrace environment detected **within the last 5 minutes**.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes?relativeTime=5mins' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes?relativeTime=5mins
```

#### Response body

```
[



{



"entityId": "PROCESS_GROUP_INSTANCE-EC9688429EB24B6B",



"displayName": "Apache Web Server apache2",



"discoveredName": "Apache Web Server apache2",



"firstSeenTimestamp": 1464951001104,



"lastSeenTimestamp": 1544024894801,



"tags": [],



"fromRelationships": {



"isProcessOf": [



"HOST-5FD609AD6757BE7D"



],



"isInstanceOf": [



"PROCESS_GROUP-B34081EFF9E5F516"



]



},



"toRelationships": {



"runsOnProcessGroupInstance": [



"SERVICE-C3173FEB08025322",



"SERVICE-B8C88BAA442098CF"



]



},



"metadata": {



"commandLineArgs": [



"/usr/sbin/apache2 -k start"



],



"executables": [



"apache2"



],



"executablePaths": [



"/usr/sbin/apache2"



],



"apacheConfigPaths": [



"/etc/apache2/apache2.conf"



]



},



"softwareTechnologies": [



{



"type": "PHP",



"edition": "Apache",



"version": "5.5.9"



},



{



"type": "APACHE_HTTPD",



"edition": null,



"version": "2.4.7"



},



{



"type": "SQLITE",



"edition": null,



"version": null



}



],



"listenPorts": [



443,



80



],



"bitness": "64bit",



"monitoringState": {



"actualMonitoringState": "ON",



"expectedMonitoringState": "ON",



"restartRequired": false



},



"agentVersions": [



{



"major": 1,



"minor": 157,



"revision": 167,



"timestamp": "20181127-152923",



"sourceRevision": ""



}



]



},



{



"entityId": "PROCESS_GROUP_INSTANCE-C43E52A77ED8F809",



"displayName": "OneAgent network monitoring",



"discoveredName": "OneAgent network monitoring",



"firstSeenTimestamp": 1543571247077,



"lastSeenTimestamp": 1544024847791,



"tags": [



{



"context": "CONTEXTLESS",



"key": "sample tag"



}



],



"fromRelationships": {



"isProcessOf": [



"HOST-CCEA78FDE257A4B9"



],



"isInstanceOf": [



"PROCESS_GROUP-E2B399E9E7FF43C0"



],



"isNetworkClientOf": [



"PROCESS_GROUP_INSTANCE-9E7865921C2C984E"



]



},



"toRelationships": {},



"metadata": {



"hostGroups": [



"wazuh"



]



},



"softwareTechnologies": [



{



"type": "APMNG",



"edition": null,



"version": null



}



],



"bitness": "64bit",



"monitoringState": {



"actualMonitoringState": "ON",



"expectedMonitoringState": "ON",



"restartRequired": false



}



}



]
```

#### Response code

200

## Related topics

* [Process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")