---
title: Log ingest rules (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage
scraped: 2026-02-21T21:25:02.569220
---

# Log ingest rules (Logs Classic)

# Log ingest rules (Logs Classic)

* Tutorial
* 16-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace version 1.252+ OneAgent version 1.243+

For the newest Dynatrace version, see [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

If you use a OneAgent version earlier than 1.243 and Dynatrace Cluster version earlier than 1.252, go to [Log Sources and Storage](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-add-log-file-sources "Learn how to include and exclude log sources for analysis.").

Dynatrace allows you to include and exclude specific log sources for your analysis. Using [Dynatrace identity and access management (IAM) framework](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies"), you can control which user can change configurations on which scope.

The configuration is based on rules that use matchers for hierarchy, log path, and process groups. These rules determine which log files among those detected by OneAgent, either automatically or defined as custom log sources, are ingested.

## Log ingest rule



1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration.  
   By default, the **Include in storage** button is turned on, indicating that items configured by this rule will be stored in Dynatrace. Alternatively, you can select the **Exclude from storage** rule type.
3. Expand **Details** of your new rule and select **Add matcher** to create a specific match for this rule.  
   Multiple matchers can be included in one rule.

   Other than the **Log source** attribute in Windows (due to file paths being case insensitive), matchers are case-sensitive.
4. Select the matching attribute:

Attribute

Description

Search dropdown logic

**Process group**

Matching is based on the process group ID. The process group is determined by the detection rules described in [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection"). If a process changes its process group, log ingestion for that process may start or stop based on the changes made.

Attributes visible in the last 3 days are listed.

**Log source**

Matching is based on a log path or a Windows event log full name; wildcards are supported in form of an asterisk. Autocompletion for **Log source** is only partial. You can either choose one of the predefined values or enter your log source.

Can be entered manually. No time limit.

**Log source origin**[1](#fn-1-1-def)

Matching is based on the detector used by the log agent to discover the log file. Available options include:

* **Custom log source configuration**: Log source provided by the user through custom configuration.
* **Open log file detector**: Logs discovered automatically by the log module's autodetection mechanism.
* **System log detector**: Includes Windows application log or `/var/log/syslog` for Linux.
* **Container output**: Autodetected Kubernetes or Docker logs.
* **IIS log detector**: Logs detected by the IIS detector.

Can be entered manually. No time limit.

**Log content**

Matching is based on the content of the log; wildcards are supported in form of an asterisk.

Can be entered manually. No time limit.

**Log record level**[2](#fn-1-2-def)[3](#fn-1-3-def)

Matching is based on the level of the log record. It supports the following values: `alert`, `critical`, `debug`, `emergency`, `error`, `info`, `none`, `notice`, `severe`, `warn`.

Can be entered manually. No time limit.

**journald unit**[4](#fn-1-4-def)

Matching is based on any of the selected journald units. Unless you enrich other log sources with a `journald.unit` attribute, you should also add a `log.source` or `log.source.origin` matcher to the ingest rule to boost the Log Module performance.

Can be entered manually. No time limit.

**Host tag**[5](#fn-1-5-def)[6](#fn-1-6-def)

Matching is based on the host tag. The attribute only supports the tags set with the [OneAgent command line tool](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") or with the [Remote configuration](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") in a `key=value` pair format. They can be distinguished by the `[Environment]` prefix on the UI, but you should use the value without the prefix.
Multiple tags can be specified in a single matcher, but each tag needs to have the same key, such as `logscope=frontend`, `logscope=backend`.

Can be entered manually. No time limit.

**Kubernetes container name**

Matching is based on the name of the Kubernetes container.

Attributes visible in the last 90 days are listed.

**Kubernetes namespace name**

Matching is based on the name of the Kubernetes namespace.

Attributes visible in the last 90 days are listed.

**Kubernetes deployment name**

Matching is based on any of the selected deployments. It is deprecated for the OneAgent Log Module managed by Dynatrace Operator or when the **Collect all container logs** feature flag is enabled.

Can be entered manually.

**Kubernetes pod annotation**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected pod annotations. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container** logs feature flag to be enabled.

Can be entered manually.

**Kubernetes pod label**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected pod labels. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

Can be entered manually.

**Kubernetes workload name**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected workload names. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

Attributes visible in the last 90 days are listed.

**Kubernetes workload kind**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected workload kinds. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

Can be entered manually.

**Docker container name**

Matching is based on the name of the container.

Attributes visible in the last 90 days are listed.

**DT entity container group ID**

Matching is based on any of the selected container groups.

Can be entered manually. No time limit.

**Process technology**

Matching is based on the technology name.

Can be entered manually. No time limit.

**Windows log record event ID**[3](#fn-1-3-def)

Matching is based on any of the selected event ID attribute.

Can be entered manually. No time limit.

**Windows log record source**[3](#fn-1-3-def)

Matching is based on any of the selected source attributes.

Can be entered manually. No time limit.

**Windows log record task category**[3](#fn-1-3-def)

Matching is based on any of the selected task category attributes.

Can be entered manually. No time limit.

**Windows log record operational code**[3](#fn-1-3-def)

Matching is based on any of the selected operational code attribute.

Can be entered manually. No time limit.

**Windows log record user name**[8](#fn-1-8-def)

Matching is based on any of the selected user name attributes.

Can be entered manually. No time limit.

**Windows log record keywords**[8](#fn-1-8-def)

Matching is based on any of the selected keywords attributes.

Can be entered manually. No time limit.

1

OneAgent version 1.295+

2

Log record level attribute, transformed by OneAgent, is different than log `status` attribute transformed by Dynatrace server.

3

OneAgent version 1.273+

4

OneAgent version 1.309+

5

[Manually or automatically applied tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") are not visible to OneAgent.

6

OneAgent version 1.289+

7

Dynatrace Operator version 1.4.2+

8

OneAgent version 1.305+

The wildcard is supported for any attribute value, and might be used multiple times in a single value. However, some attributes, for example Process Group, have a limited, predefined list of possible values that are selected from an auto-complete list.

If no wildcard is used in the value, then the matcher looks for an exact fit to the value. If a wildcard is used, the matcher looks for the exact match. For example, the value `INFO` results in sending only the log data having the exact `INFO` string, but the value `*INFO*` (using the wildcards) matches log data that contain the `INFO` string in its content.

1. Select **Add value** and, from the **Values**, select the detected log data items (log files or process groups that contain log data). Multiple values can be added to the selected attribute. You can have one matcher that indicates log source and matches values **/var/log/syslog** and **Windows Application Log**.
2. **Save changes**.

Defined rules can be reordered and are executed in the order in which they appear on the **Log storage** page.

7. To activate your rule, turn on the **Active** toggle.

The **Active** toggle

Starting with OneAgent version 1.249, you can activate/inactivate your rules by turning on/off the **Active** toggle. To manage your rules effectively, we recommend that you upgrade your OneAgent to version 1.249. If you have any rules set on the host with OneAgent version earlier than 249, you will not be able to inactivate them, in which case you need to remove such rules by selecting **Delete** on the rule level or via the REST API.

## Matching a list of rules to log data

Matching occurs in a predefined hierarchy and rules are executed from top to bottom. This means that if a rule above on the list matches certain log data, then the lower ones will be omitted. Items matched in the higher-level configurations are overwritten in the lower-level configurations if they match the same log data. If no rule is matched, the file is not sent. The matching hierarchy is as follows:

1. Host configuration rules
2. Host group configuration rules
3. Tenant configuration rules

## Configuration scopes

Three hierarchy scopes are supported: host, host group, and tenant. The scope with the least possible set of rules has priority over larger sets.

![Log ingest rules priority](https://dt-cdn.net/images/log-storage-rule-priority-white-1491-d1d8126129.png)

1. Log storage rules configured for a host take precedence over log storage rules configured for a host group.
2. Log storage rules configured for a host group take precedence over log storage rules configured for a tenant.

### Host scope



The host scope can be accessed through the **Host settings** for a specific host.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. From the host settings, go to **Log Monitoring** > **Log ingest rules**.
5. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### Host group scope

The host group scope can be accessed via the **Host** page.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Log ingest rules**.
7. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### Tenant scope

The tenant scope is available in the settings menu.

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### List hosts and host groups with overriding rules

The table on **Settings** > **Log Monitoring** > **Log ingest rules** lists all log storage rules that you have set at the tenant level. However, you may want to see where you have set log storage rules for hosts and host groups that override the tenant-level rules.

To list all entities (hosts and host groups) to which more specific log storage rules are applied

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. In the upper-right corner of the **Log ingest rules** page, select **More** (**â¦**) > **Hierarchy and overrides**. A searchable **Hierarchy and overrides** panel lists all entities (hosts and host groups) on which you have set log storage rules that override the tenant-level rules listed on **Settings** > **Log Monitoring** > **Log ingest rules**.
3. Select an entity name to go to that entity's **Log ingest rules** page.

## Example upload

In this example, we configure the tenant storage upload for `c:\inetpub\logs\LogFiles\ex_*.log` files in two process groups: `IIS (PROCESS_GROUP-3D9D854163F8F07A)` and `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`. The log storage rule consists of two matchers: the first matcher finds the process groups and the second matcher matches only for the defined log source.

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the title for your configuration.
3. Select **Add matcher**. This is the first matcher to match two specified process groups.
4. From the **Attribute** list, select **Process group**.
5. Select **Add value** and type IIS, and then, from the suggestion list, select `IIS (PROCESS_GROUP-3D9D854163F8F07A)`.
6. Select **Add value** again, type `IIS` and select the second process group from the suggestion list: `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`.
7. Select **Add matcher** again. This is the second matcher to match the specified log data source.
8. From the **Attribute** list, select **Log source**.
9. Select **Add value** and enter `c:\inetpub\logs\LogFiles\ex_*.log` as the value.
10. Save changes.

## Example exclude

In this example, we configure the tenant storage upload for all log sources except `c:\inetpub\logs\LogFiles\ex_*.log` files in a process group `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`.

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the title for your configuration.
3. Turn off **Send to storage**.
4. Select **Add matcher**. This is the first matcher to match the specified process group.
5. From the **Attribute** list, select `Process group`.
6. Select **Add value** and type IIS, and then, from the suggestion list, select `IIS (PROCESS_GROUP-3D9D854163F8F07A)`.
7. Select **Add matcher** again. This is the second matcher to exclude the specified log data source.
8. From the **Attribute** list select **Log source**.
9. Select **Add value** and enter `c:\inetpub\logs\LogFiles\ex_*.log` as a value.
10. Save changes.

## REST API

You can use the Settings API to manage your log ingest rules:

* View schema
* List stored configuration objects
* View single configuration object
* Create new, edit, or remove existing configuration object

To check the current schema version for log ingest rules, list all available schemas and look for the `builtin:logmonitoring.log-storage-settings` schema identifier.

Log ingest rules can be configured for the following scopes:

* `tenant` â configuration object affects all hosts on a given tenant.
* `host_group` â configuration object affects all hosts assigned to a given host group.
* `host` â configuration object affects only the given host.

To create a log ingest rule using the API:

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) permissions.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The log storage configuration schema identifier (`schemaId`) is `builtin:logmonitoring.log-storage-settings`. Here is an example JSON payload with the log storage configuration:

   ```
   [



   {



   "insertAfter":"uAAZ0ZW5hbnQABnRlbmFudAAkMGUzYmY2ZmYtMDc2ZC0zNzFmLhXaq0",



   "schemaId": "builtin:logmonitoring.log-storage-settings",



   "schemaVersion": "0.1.0",



   "scope": "tenant",



   "value": {



   "config-item-title": "Added from REST API",



   "send-to-storage": true,



   "matchers": [



   {



   "attribute": "dt.entity.process_group",



   "operator": "MATCHES",



   "values": [



   "PROCESS_GROUP-05F00CBACF39EBD1"



   ]



   },



   {



   "attribute": "log.source",



   "operator": "MATCHES",



   "values": [



   "Windows System Log",



   "Windows Security Log"



   ]



   }



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

## Examples

The examples that follow show the results of various combinations of rules and matchers.

### Example 1: Multiple rules

In this example, there are two rules:

* Rule 1 is an Exclude rule and has two matchers: the process group attribute is Apache, and the Log source attribute is `access.log`).
* Rule 2 is an Include rule and has one matcher: the process group attribute is Apache.

Results: `access.log` is not sent, `error.log` (of Apache) is sent, and `error.log` (of other PG) is not sent.

* `access.log` written by Apache matches the first rule, which has `send-to-storage: false`, so it is not sent.
* `access.log` not written by Apache doesn't match the first rule (due to incorrect process group), and doesn't match the second rule, so it is not sent.
* `error.log` written by Apache does not match the first rule (due to incorrect source), but it matches the second rule, which has `send-to-storage: true`, so it is sent.
* `error.log` not written by Apache doesn't match the first rule (due to both incorrect process group and log source), and doesn't match the second rule, so it is not sent.

```
{



"send-to-storage": false,



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/access.log"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 2: Send logs written by Apache and containing 'ERROR'

This task requires setting one rule with two matchers.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 3: Send logs written by Apache or containing 'ERROR'

This task requires setting two rules with one matcher each.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 4: Send logs written by Apache, and containing 'ERROR' and 'Customer'



This task requires setting one rule with three matchers, with one value each.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*"



]



},



{



"attribute": "log.content",



"values": [



"*Customer*"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 5: Send logs written by Apache, and containing 'ERROR' or 'Customer'

This task requires setting one rule with two matchers: a matcher with the process group value, and a matcher with two content values.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*", "*Customer*"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 6: Send logs written by Apache or MySQL

This task requires setting two rules, or one rule with one matcher having two values.  
Rules with two matchers will not work here.

Setting two rules:

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

Setting one rule with one matcher having two values:

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID", "PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



}
```

### Example 7: Send all logs

This task requires setting a rule without any matchers.

```
{



"send-to-storage": true,



"matchers": [



],



"enabled": true



}
```

### Example 8: Send all logs except Apache and MySQL logs

This task requires setting two rules.

* The first rule is an Exclude rule with one matcher having two values.
* The second rule does not contain any matchers.

The rules have to be executed in the order indicated below.

```
{



"send-to-storage": false,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID", "PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



],



"enabled": true



}
```

## FAQ

Will older OneAgents work with this solution?

OneAgent versions earlier than `1.243` won't send any data; they will get an empty whitelist in response.

Why don't I see any configuration on the global page after migration from the hosts' perspective?

All host perspective configs are migrated to the corresponding host scope.

Are log ingest rules the same as/part of the autodiscovery process?

No. Autodiscovery is a mechanism of OneAgent that detects logs, but it doesn't mean that log files are sent to storage automatically. A configuration page for autodiscovery is planned for a future release. To learn more about autodiscovery, see [Log content autodiscovery (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2 "Learn about autodiscovery of log content and requirements for autodiscovery to occur.")

Is the order of configuration items important?

Yes, configuration items are matched from top to bottom, meaning that the top value is the most important.

How long do I need to wait for the configuration to be applied to the host?

It is applied within 90 seconds.

Does adding a content matcher reduce the number of log events sent to Dynatrace?

Yes. A content matcher narrows down the scope of log events (log entries) according to the criteria set (for example, searching only for error logs).

Where is filtering carried out, in Dynatrace and or in OneAgent?

* Filtering (narrowing down the scope according to the criteria set) is carried out in OneAgent.
* Setting limits (for example, the log events per minute limit or the attribute values limit) is conducted in Dynatrace.

Does filtering the content reduce DDU cost and/or network usage?

Yes. Content filtering conducted on OneAgent reduces both DDU costs and network usage. You can calculate the cost and network use reduction by determining your total data consumption and deducting the GB size of data that was filtered out. For details on how DDUs costs are calculated, see:

* [Log Monitoring DDU calculation](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.")

* [Log Management and analytics powered by Grail DDU calculation](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.")