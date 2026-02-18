---
title: OneAgent on a host - GET a list of hosts with OneAgent details
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents
scraped: 2026-02-06T16:31:11.346773
---

# OneAgent on a host - GET a list of hosts with OneAgent details

# OneAgent on a host - GET a list of hosts with OneAgent details

* Reference
* Published Feb 03, 2020

The **OneAgent on a host** API enables you to check the configuration of OneAgent instances on your hosts.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/oneagents` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/oneagents` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `oneAgents.read`
* `DataExport`

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 7 months (214 days). | query | Optional |
| relativeTime | string | The relative timeframe, back from now.  If you need to specify relative timeframe that is not presented in the list of possible values, specify the **startTimestamp** (up to 214 days back from now) and leave **endTimestamp** and **relativeTime** empty. The element can hold these values * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | query | Optional |
| tag | string[] | Filters the resulting set of hosts by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The host has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| entity | string[] | Filters result to the specified hosts only.  To specify several hosts use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| managementZoneId | integer | Only return hosts that are part of the specified management zone.  Specify the management zone ID here. | query | Optional |
| managementZone | string | Only return hosts that are part of the specified management zone.  Specify the management zone name here.  If the **managementZoneId** parameter is set, this parameter is ignored. | query | Optional |
| networkZoneId | string | Filters the resulting set of hosts by the specified network zone.  Specify the Dynatrace entity ID of the required network zone. You can fetch the list of available network zones with the [GET all network zonesï»¿](https://dt-url.net/u4o3r7z) call. | query | Optional |
| hostGroupId | string | Filters the resulting set of hosts by the specified host group.  Specify the Dynatrace entity ID of the required host group. | query | Optional |
| hostGroupName | string | Filters the resulting set of hosts by the specified host group.  Specify the name of the required host group. | query | Optional |
| osType | string | Filters the resulting set of hosts by the OS type. The element can hold these values * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` | query | Optional |
| cloudType | string | Filters the resulting set of hosts by the cloud type. The element can hold these values * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` | query | Optional |
| autoInjection | string | Filters the resulting set of hosts by the auto-injection status. The element can hold these values * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` | query | Optional |
| availabilityState | string | Filters the resulting set of hosts by the availability state of OneAgent.  * `MONITORED`: Hosts where OneAgent is enabled and active. * `UNMONITORED`: Hosts where OneAgent is disabled and inactive. * `CRASHED`: Hosts where OneAgent has returned a crash status code. * `LOST`: Hosts where it is impossible to establish connection with OneAgent. * `PRE_MONITORED`: Hosts where OneAgent is being initialized for monitoring. * `SHUTDOWN`: Hosts where OneAgent is shutting down in a controlled process. * `UNEXPECTED_SHUTDOWN`: Hosts where OneAgent is shutting down in an uncontrolled process. * `UNKNOWN`: Hosts where the state of OneAgent is unknown. The element can hold these values * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` | query | Optional |
| detailedAvailabilityState | string | Filters the resulting set of hosts by the detailed availability state of OneAgent.  * `UNKNOWN`: Hosts where the state of OneAgent is unknown. * `PRE_MONITORED`: Hosts where OneAgent is being initialized for monitoring. * `CRASHED_UNKNOWN`: Hosts where OneAgent has crashed for unknown reason. * `CRASHED_FAILURE`: Hosts where OneAgent has returned a crash status code. * `LOST_UNKNOWN`: Hosts where it is impossible to establish connection with OneAgent for unknown reason. * `LOST_CONNECTION`: Hosts where OneAgent has been recognized to be inactive. * `LOST_AGENT_UPGRADE_FAILED`: Hosts where OneAgent has a potential update problem due to inactivity after update. * `SHUTDOWN_UNKNOWN_UNEXPECTED`: Hosts where OneAgent is shutting down in an uncontrolled process. * `SHUTDOWN_UNKNOWN`: Hosts where OneAgent has shutdown for unknown reason. * `SHUTDOWN_GRACEFUL`: Hosts where OneAgent has shutdown because of host shutdown. * `SHUTDOWN_STOPPED`: Hosts where OneAgent has shutdown because the host has stopped. * `SHUTDOWN_AGENT_LOST`: Hosts where PaaS module has been recognized to be inactive. * `SHUTDOWN_SPOT_INSTANCE`: Hosts where OneAgent shutdown was triggered by the AWS Spot Instance interruption. * `SHUTDOWN_K8S_NODE_SHUTDOWN`: Hosts where OneAgent shutdown was triggered by a k8s node graceful shutdown. * `UNMONITORED_UNKNOWN`: Hosts where OneAgent is disabled and inactive for unknown reason. * `UNMONITORED_TERMINATED`: Hosts where OneAgent has terminated. * `UNMONITORED_DISABLED`: Hosts where OneAgent has been disabled in configuration. * `UNMONITORED_AGENT_STOPPED`: Hosts where OneAgent is stopped. * `UNMONITORED_AGENT_RESTART_TRIGGERED`: Hosts where OneAgent is being restarted. * `UNMONITORED_AGENT_UNINSTALLED`: Hosts where OneAgent is uninstalled. * `UNMONITORED_AGENT_DISABLED`: Hosts where OneAgent reported that it was disabled. * `UNMONITORED_AGENT_UPGRADE_FAILED`: Hosts where OneAgent has a potential update problem. * `UNMONITORED_ID_CHANGED`: Hosts where OneAgent has potentially changed ID during update. * `UNMONITORED_AGENT_LOST`: Hosts where OneAgent has been recognized to be unavailable due to server communication issues. * `UNMONITORED_AGENT_UNREGISTERED`: Hosts where a code module has been recognized to be unavailable because of shutdown. * `UNMONITORED_AGENT_VERSION_REJECTED`: Hosts where OneAgent was rejected because the version does not meet the minimum agent version requirement. * `UNMONITORED_AGENT_MIGRATED`: Hosts where OneAgent was migrated to another environment. * `MONITORED`: Hosts where OneAgent is enabled and active. * `MONITORED_ENABLED`: Hosts where OneAgent has been enabled in configuration. * `MONITORED_AGENT_REGISTERED`: Hosts where the new OneAgent has been recognized. * `MONITORED_AGENT_UPGRADE_STARTED`: Hosts where OneAgent has shutdown due to an update. * `MONITORED_AGENT_ENABLED`: Hosts where OneAgent reported that it was enabled. * `MONITORED_AGENT_VERSION_ACCEPTED`: Hosts where OneAgent was accepted because the version meets the minimum agent version requirement. The element can hold these values * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` | query | Optional |
| monitoringType | string | Filters the resulting set of hosts by monitoring mode of OneAgent deployed on the host. The element can hold these values * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` | query | Optional |
| agentVersionIs | string | Filters the resulting set of hosts to those that have a certain OneAgent version deployed on the host.  Specify the comparison operator here. The element can hold these values * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Optional |
| agentVersionNumber | string | Filters the resulting set of hosts to those that have a certain OneAgent version deployed on the host.  Specify the version in the `<major>.<minor>.<revision>` format, for example `1.182.0`. You can fetch the list of available versions with the [GET available versionsï»¿](https://dt-url.net/fo23rb5) call. | query | Optional |
| autoUpdateSetting | string | Filters the resulting set of hosts by the actual state of the auto-update setting of deployed OneAgents. The element can hold these values * `ENABLED` * `DISABLED` | query | Optional |
| updateStatus | string | Filters the resulting set of hosts by the update status of OneAgent deployed on the host. The element can hold these values * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` | query | Optional |
| faultyVersion | boolean | Filters the resulting set of hosts to those that run OneAgent version that is marked as faulty. | query | Optional |
| unlicensed | boolean | Filters the resulting set of hosts to those that run OneAgent that are unlicensed.  Example: Your Dynatrace license is missing the required "Foundation & Discovery" DPS capability for Discovery mode. | query | Optional |
| activeGateId | string | Filters the resulting set of hosts to those that are currently connected to the ActiveGate with the specified ID.  Use **DIRECT\_COMMUNICATION** keyword to find the hosts not connected to any ActiveGate. | query | Optional |
| technologyModuleType | string | Filters the resulting set of hosts to those that run the specified OneAgent code module.  If several code module filters are specified, the code module has to match **all** the filters. The element can hold these values * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` | query | Optional |
| technologyModuleVersionIs | string | Filters the resulting set of hosts to those that have a certain code module version deployed on the host.  Specify the comparison operator here.  If several code module filters are specified, the code module has to match **all** the filters. The element can hold these values * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Optional |
| technologyModuleVersionNumber | string | Filters the resulting set of hosts to those that have a certain code module version deployed on the host.  Specify the version in the `<major>.<minor>.<revision>` format, for example `1.182.0`. You can fetch the list of available versions with the [GET available versionsï»¿](https://dt-url.net/fo23rb5) call.  If several code module filters are specified, the code module has to match **all** the filters. | query | Optional |
| technologyModuleFaultyVersion | boolean | Filters the resulting set of hosts to those that run the code module version that is marked as faulty.  If several code module filters are specified, the code module has to match **all** the filters. | query | Optional |
| pluginName | string | Filters the resulting set of hosts to those that run the plugin with the specified name.  The **CONTAINS** operator is applied to the specified value.  If several plugin filters are specified, the plugin has to match **all** the filters. | query | Optional |
| pluginVersionIs | string | Filters the resulting set of hosts to those that have a certain plugin version deployed on the host.  Specify the comparison operator here.  If several plugin filters are specified, the plugin has to match **all** the filters. The element can hold these values * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Optional |
| pluginVersionNumber | string | Filters the resulting set of hosts to those that have a certain plugin version deployed on the host.  Specify the version in the `<major>.<minor>.<revision>` format, for example `1.182.0`. You can fetch the list of available versions with the [GET available versionsï»¿](https://dt-url.net/fo23rb5) call.  `<minor>` and `<revision>` parts of the version number are optional.  If several plugin filters are specified, the plugin has to match **all** the filters. | query | Optional |
| pluginState | string | Filters the resulting set of hosts to those that run the plugin with the specified state. The element can hold these values * `DISABLED` * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` | query | Optional |
| nextPageKey | string | The cursor for the next page of results, if results do not fit on one page. You can find the cursor value on the current page of the response, in the **nextPageKey** field.  To obtain subsequent pages, you must specify this cursor value in your query, and keep all other query parameters as they were in the original request.  If you don't specify the cursor, the first page will always be returned. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [HostsListPage](#openapi-definition-HostsListPage) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `HostsListPage` object

A list of hosts with OneAgent deployment information for each host.

| Element | Type | Description |
| --- | --- | --- |
| hosts | [HostAgentInfo[]](#openapi-definition-HostAgentInfo) | A list of hosts with OneAgent deployment information for each host. |
| nextPageKey | string | The cursor for the next page of results.  Has the value of `null` on the last page.  There might be another page of results even if the current page is empty. |
| percentageOfEnvironmentSearched | number | The progress of the environment search, in percent. |

#### The `HostAgentInfo` object

OneAgent deployment on a host.

| Element | Type | Description |
| --- | --- | --- |
| active | boolean | OneAgent is active (`true`) or inactive (`false`). |
| autoUpdateSetting | string | The effective auto-update setting of OneAgent. For host with inherited configuration it is calculated from its parent's configuration The element can hold these values * `ENABLED` * `DISABLED` |
| availabilityState | string | The availability state of OneAgent. The element can hold these values * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` |
| availableVersions | string[] | A list of versions OneAgent can be updated to. |
| configuredMonitoringEnabled | boolean | Monitoring is enabled (`true`) or disabled (`false`) in the OneAgent configuration. |
| configuredMonitoringMode | string | Configured monitoring mode of OneAgent. The element can hold these values * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` |
| ~~currentActiveGateId~~ | integer | DEPRECATED  This field is deprecated and provided for backward compatibility.  Use the **currentActiveGateIds** field instead. |
| currentActiveGateIds | string[] | The list of ActiveGate IDs of ActiveGates to which OneAgent is currently connected. |
| currentNetworkZoneId | string | The ID of the network zone that OneAgent is using. |
| detailedAvailabilityState | string | The detailed availability state of OneAgent. The element can hold these values * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` |
| faultyVersion | boolean | OneAgent version is faulty (`true`) or not (`false`). |
| hostInfo | [Host](#openapi-definition-Host) | Information about the host. |
| modules | [ModuleInfo[]](#openapi-definition-ModuleInfo) | A list of code modules deployed on the host. |
| monitoringType | string | The monitoring mode of OneAgent. The element can hold these values * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` |
| plugins | [PluginInfo[]](#openapi-definition-PluginInfo) | A list of plugins deployed on the host. |
| unlicensed | boolean | OneAgent is unlicensed. |
| updateStatus | string | The current update status of OneAgent. The element can hold these values * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` |

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

#### The `ModuleInfo` object

OneAgent code module.

| Element | Type | Description |
| --- | --- | --- |
| instances | [ModuleInstance[]](#openapi-definition-ModuleInstance) | A list of instances of the code module. |
| moduleType | string | The type of the code module. The element can hold these values * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` |

#### The `ModuleInstance` object

An instance of the OneAgent code module.

| Element | Type | Description |
| --- | --- | --- |
| active | boolean | The code module instance is active (`true`) or inactive (`false`). |
| faultyVersion | boolean | The code module version is faulty (`true`) or not (`false`). |
| instanceName | string | The name of the instance. |
| moduleVersion | string | The version of the code module. |

#### The `PluginInfo` object

OneAgent plugin.

| Element | Type | Description |
| --- | --- | --- |
| instances | [PluginInstance[]](#openapi-definition-PluginInstance) | A list of instances of the plugin. |
| pluginName | string | The name of the plugin. |

#### The `PluginInstance` object

An instance of the OneAgent plugin.

| Element | Type | Description |
| --- | --- | --- |
| pluginVersion | string | The version of the plugin. |
| state | string | The state of the plugin instance. |

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



"hosts": [



{



"active": true,



"autoUpdateSetting": "ENABLED",



"availabilityState": "CRASHED",



"availableVersions": [



"string"



],



"configuredMonitoringEnabled": true,



"configuredMonitoringMode": "CLOUD_INFRASTRUCTURE",



"currentActiveGateId": 1,



"currentActiveGateIds": [



"string"



],



"currentNetworkZoneId": "string",



"detailedAvailabilityState": "CRASHED_FAILURE",



"faultyVersion": true,



"hostInfo": {



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



},



"modules": [



{



"instances": [



{



"active": true,



"faultyVersion": true,



"instanceName": "string",



"moduleVersion": "string"



}



],



"moduleType": "APACHE"



}



],



"monitoringType": "CLOUD_INFRASTRUCTURE",



"plugins": [



{



"instances": [



{



"pluginVersion": "string",



"state": "string"



}



],



"pluginName": "string"



}



],



"unlicensed": true,



"updateStatus": "INCOMPATIBLE"



}



],



"nextPageKey": "string",



"percentageOfEnvironmentSearched": 1



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

## Related topics

* [OneAgent configuration on a host API](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Manage the configuration of OneAgent instances on your hosts via the Dynatrace API.")