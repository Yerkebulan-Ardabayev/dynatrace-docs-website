---
title: Process groups API - GET all process groups
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all
scraped: 2026-02-15T09:00:23.802758
---

# Process groups API - GET all process groups

# Process groups API - GET all process groups

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Gets the list of all [process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") in your Dynatrace environment, along with their parameters and relationships.

The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.

You can additionally limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **Next-Page-Key** response header in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/process-groups` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups` |

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
| tag | string[] | Filters the resulting set of process groups by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The process group has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| entity | string[] | Filters result to the specified process groups only.  To specify several process groups use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| host | string[] | Filters process groups by the host they're running at.  Specify Dynatrace IDs of the host you're interested in.  To specify several hosts use the following format: `host=hostID1&host=hostID2`.  The **OR** logic applies. | query | Optional |
| managementZone | integer | Only return process groups that are part of the specified management zone. | query | Optional |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| pageSize | integer | The number of process groups per result page.  If not set, pagination is not used and the result contains all process groups fitting the specified filtering criteria. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |

## Response headers

| Header | Type | Description |
| --- | --- | --- |
| Total-Count | integer | The estimated number of results. |
| Next-Page-Key | string | The cursor for the next page of results. Without it you'll get the first page again. |
| Page-Size | string | The maximum number of results per page. |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProcessGroup[]](#openapi-definition-ProcessGroup) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `ProcessGroup` object

Parameters of a process group.

| Element | Type | Description |
| --- | --- | --- |
| azureHostName | string | - |
| azureSiteName | string | - |
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
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | - |

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
[



{



"azureHostName": "string",



"azureSiteName": "string",



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isNetworkClientOfProcessGroup": [



"string"



],



"runsOn": [



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



"isInstanceOf": [



"string"



],



"isNetworkClientOfProcessGroup": [



"string"



],



"runsOn": [



"string"



]



}



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

## Example

In this example, the request lists all the process groups of the environment detected **within the last 5 minutes**.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups?relativeTime=5mins' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups?relativeTime=5mins
```

#### Response body

```
[



{



"entityId": "PROCESS_GROUP-B34081EFF9E5F516",



"displayName": "Apache Web Server apache2",



"discoveredName": "Apache Web Server apache2",



"firstSeenTimestamp": 1405316247660,



"lastSeenTimestamp": 1545149212556,



"tags": [],



"fromRelationships": {},



"toRelationships": {



"runsOn": [



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



]



},



{



"entityId": "PROCESS_GROUP-E5C3CC7EC1F80B5B",



"displayName": "PHP-FPM",



"discoveredName": "PHP-FPM",



"firstSeenTimestamp": 1503909407206,



"lastSeenTimestamp": 1545149349700,



"tags": [],



"fromRelationships": {



"runsOn": [



"HOST-74CDC8809AD43931",



"HOST-9A81EACCA0270218"



]



},



"toRelationships": {



"isInstanceOf": [



"PROCESS_GROUP_INSTANCE-7E988C3503AE8803"



],



"isNetworkClientOfProcessGroup": [



"PROCESS_GROUP-49C926A7091830E3"



],



"runsOn": [



"SERVICE-72503CBDD2AEF066"



]



},



"metadata": {



"hostGroups": [



"authoring"



],



"commandLineArgs": [



"/usr/sbin/php-fpm7.0 --nodaemonize --fpm-config /etc/php/7.0/fpm/php-fpm.conf"



],



"executables": [



"php-fpm7.0"



],



"executablePaths": [



"/usr/sbin/php-fpm7.0"



]



},



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



]
```

#### Response code

200

## Related topics

* [Process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")