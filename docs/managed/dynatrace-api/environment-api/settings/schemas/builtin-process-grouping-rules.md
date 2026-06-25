---
title: Settings API - Process grouping rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-grouping-rules
scraped: 2026-05-12T11:45:40.909516
---

# Settings API - Process grouping rules schema table

# Settings API - Process grouping rules schema table

* Published May 05, 2025

### Process grouping rules (`builtin:process-grouping-rules)`

Dynatrace automatically monitors process groups that are of known technology types or that consume significant resources. With process grouping rules, you can automatically monitor additional technologies.

For more information read the [community postï»¿](https://dt-url.net/ea2319k).

Process grouping rules also work for processes that have [deep monitoring enabledï»¿](https://dt-url.net/3203vvp).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-grouping-rules` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-grouping-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-grouping-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-grouping-rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Custom technology name `customTechnologyName` | text | Note: Reported only in full-stack, infrastructure and discovery modes. | Optional |
| Define the process groups `pgExtraction` | [ProcessGroupExtraction](#ProcessGroupExtraction)[] | Define process groups and processes. | Required |

##### The `ProcessGroupExtraction` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| 1.1. Process group display name (optional) `name` | text | When this field is empty, OneAgent will automatically assign the process group name based on process type and properties like executable name. If you expect that multiple processes will be matched by the rule, it is highly recommended that you fill this field because it is unspecified which process will be used as the group name source. | Optional |
| 1.2. Report process group `report` | enum | Auto reports only processes which are important - meaning deep monitored or with high resource usage The element has these enums * `always` * `auto` * `never` | Required |
| 1.3. Type of captured processes (optional) `processType` | enum | Note: Not all types can be detected at startup.  Restrict this rule to specific process types to avoid mixing deep monitored properties leading to confusing results. The element has these enums * `PROCESS_TYPE_APACHE_HTTPD` * `PROCESS_TYPE_GLASSFISH` * `PROCESS_TYPE_GO` * `PROCESS_TYPE_IBM_CICS_REGION` * `PROCESS_TYPE_IBM_IMS_CONTROL` * `PROCESS_TYPE_IBM_IMS_MPR` * `PROCESS_TYPE_IIS_APP_POOL` * `PROCESS_TYPE_JBOSS` * `PROCESS_TYPE_JAVA` * `PROCESS_TYPE_NGINX` * `PROCESS_TYPE_NODE_JS` * `PROCESS_TYPE_PHP` * `PROCESS_TYPE_RUBY` * `PROCESS_TYPE_TOMCAT` * `PROCESS_TYPE_WEBLOGIC` * `PROCESS_TYPE_WEBSPHERE` | Optional |
| `detection` | [DetectionCondition](#DetectionCondition)[] | Define process detection rules to select processes on which this rule will apply to. **At least one rule must be defined.** | Required |
| `pgIdSource` | [GroupIdSource](#GroupIdSource) | **3.1. Process group id source** | Required |
| `pgiIdSource` | [InstanceIdSource](#InstanceIdSource) | **3.2. Process id source (optional)**  Define a property that should be used to identify your process. | Optional |

##### The `DetectionCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| 2.1. Property `property` | text | - | Required |
| 2.2. Variable name `name` | text | If Dynatrace detects this property at startup of a process, it will be matched to this grouping rule. | Required |
| 2.2. Condition `condition` | text | * $contains(svc) â Matches if svc appears anywhere in the process property value. * $eq(svc.exe) â Matches if svc.exe matches the process property value exactly. * $prefix(svc) â Matches if app matches the prefix of the process property value. * $suffix(svc.py) â Matches if svc.py matches the suffix of the process property value.  For example, $suffix(svc.py) would detect processes named loyaltysvc.py and paymentssvc.py.  For more details, see [documentationï»¿](https://dt-url.net/j142w57). | Required |
| Case sensitive `caseSensitive` | boolean | When enabled, matching conditions are case sensitive. When disabled, matching conditions are case insensitive | Required |

##### The `GroupIdSource` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Standalone rule `standaloneRule` | boolean | Valid only for **deep monitored** processes.  If this option is selected, the default Dynatrace behavior is disabled for the detected processes. Only this rule is used to separate the process group.  If this option is not selected, this rule contributes to the default Dynatrace process group detection.  [See our help page for examples.ï»¿](https://dt-url.net/1722wrz) | Required |
| 3.1.1. Id type `type` | enum | Pick which property should be used to identify your process group. You can pick a custom variable or pick an existing process property. The element has these enums * `CUSTOM` * `EXISTING` | Required |
| 3.1.2. Process group identifier `id` | text | This identifier is used by Dynatrace to recognize this process group. | Required |
| 3.1.2. Property `property` | text | - | Required |
| Variable name `name` | text | If Dynatrace detects this property at startup of a process, it will use its value to identify process groups. | Required |
| 3.1.3. Advanced settings (optional) `advancedSettings` | [AdvancedSettings](#AdvancedSettings) | Set advanced options to customize delimiters and control how property values are processed.  Consider an environment with processes such as:  * `python myScript.py --env=prod12 --id=12` * `python myScript.py --env=dev2 --id=2` * etc.  To group production *(prod)* and development *(dev)* processes together you could use Command line property with:  * **Delimiter** from `--env=` to `--id` to extract `prod12`  and `dev2` * Enable **Ignore numbers** to transform `prod12` to `prod*` and `dev2` to `dev*`. | Optional |

##### The `InstanceIdSource` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| 3.2.1. Property `property` | text | - | Optional |
| Variable name `name` | text | If Dynatrace detects this property at startup of a process, it will use its value to identify process groups more granular. | Required |
| 3.2.2. Advanced settings (optional) `advancedSettings` | [AdvancedSettings](#AdvancedSettings) | Set advanced options to customize delimiters and control how property values are processed.  Consider an environment with processes such as:  * `python myScript.py --env=prod12 --id=12` * `python myScript.py --env=dev2 --id=2` * etc.  To group production *(prod)* and development *(dev)* processes together you could use Command line property with:  * **Delimiter** from `--env=` to `--id` to extract `prod12`  and `dev2` * Enable **Ignore numbers** to transform `prod12` to `prod*` and `dev2` to `dev*`. | Optional |

##### The `AdvancedSettings` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Delimit from (optional) `from` | text | - | Optional |
| Delimit to (optional) `to` | text | - | Optional |
| Ignore numbers `ignoreNumbers` | boolean | (e.g. versions, hex, dates, and build numbers) | Required |