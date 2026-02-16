---
title: Sensitive data masking (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/sensitive-data-masking
scraped: 2026-02-16T21:26:39.267404
---

# Sensitive data masking (Logs Classic)

# Sensitive data masking (Logs Classic)

* 11-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace version 1.253+ OneAgent version 1.243+

Your log data contains information that may be considered sensitive. Specific log messages may include user names, email addresses, URL parameters, and other information that you may not want to disclose. Log Monitoring features the ability to mask any information by modifying the configuration file on each OneAgent that handles information you consider to be sensitive.

For the newest Dynatrace version, see [Sensitive data masking in OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.").

You can select the data that needs to be protected by applying a set of masking rules. Within each rule, you can decide what you need to hide and what to replace your hidden content with. If you need to address only specific attributes, such as predefined containers, log sources or process groups, you can achieve it by adding matchers to your rules.

## Rule hierarchy

Masking rule execution occurs in a predefined hierarchy, from top to bottom. Each consecutive rule is applied to the result of a preceding rule.
The hierarchy is as follows:

1. Host configuration rules
2. Host group configuration rules
3. Environment configuration rules

### Host configuration rules

The host configuration rules can be accessed through the **Host settings** for a specific host.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. From the host settings, go to **Log Monitoring** > **Sensitive data masking**.
5. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

### Host group configuration rules

The host group configuration rules can be accessed via the **Host** page.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Sensitive data masking**.
7. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

### Environment configuration rules

The tenant scope is available in the settings menu.

1. Go to **Settings** > **Log Monitoring** > **Sensitive data masking**.
2. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

## Create rule

You can configure sensitive data masking on the host, host group or environment level.

1. Select **Create new rule** to start configuring your rule.
2. **Name:** The name to display for your configuration.
3. **Search expression:** A regular expression to match the string that you want to mask. Use the regular expression format.
4. **Masking type:** You can replace your data with a string or Secure Hash Algorithm 1 (SHA-1).

   * If you select **replace with string**, set **Replacement** to the string that is meant to replace your sensitive data.
   * If you select **SHA-1**, your data will be replaced by the 40-character hash string.
5. Select **Add matcher** to create a specific match for this rule and narrow down the scope for that rule. You can include multiple matchers in one rule. For example, the masking rule can be applied to logs from a specific container, namespace, or log source.
6. Select the matching attribute.

   Attribute

   Description

   **Container name**

   Matching is based on the name of the container.

   **DT entity container group ID**

   Matching is based on the DT entity container group ID.

   **K8s container name**

   Matching is based on the name of the Kubernetes container.

   **K8s deployment name**

   Matching is based on the name of the Kubernetes deployment.

   **K8s namespace name**

   Matching is based on the name of the Kubernetes namespace.

   **Log source**

   Matching is based on a log path; wildcards are supported in form of an asterisk.

   **Process group**

   Matching is based on the process group ID.

   **Process technology**

   Matching is based on the technology name.
7. Select **Add value** and, from the **Values** list, select the detected log data items (log files or process groups that contain log data). Multiple values can be added to the selected operator. You can have one matcher that indicates log source and matches values **/var/log/syslog** and **Windows Application Log**.
8. Select **Save changes**.

Defined rules can be reordered, and they are executed in the order in which they appear on the **Sensitive data masking** page.

The **Active** toggle

Starting with OneAgent version 1.249, you can activate/inactivate your rules by turning on/off the **Active** toggle. To manage your rules effectively, we recommend that you upgrade your OneAgent to version 1.249. If you have any rules set on the host with OneAgent version earlier than 249, you will not be able to inactivate them, in which case you need to remove such rules by selecting **Delete** on the rule level or via the REST API.

## REST API

You can use the Settings API to manage your sensitive data masking configuration:

* View schema
* List stored configuration objects
* View single configuration object
* Create, edit, or remove configuration object

To check the current schema version for sensitive data masking configuration, list all available schemas and look for the `builtin:logmonitoring.sensitive-data-masking-settings` schema identifier. Sensitive data masking configuration objects are available for configuration on the following scopes:

* `tenant`âconfiguration object affects all hosts in a given environment.
* `host_group`âconfiguration object affects all hosts assigned to a given host group.
* `host`âconfiguration object affects only the given host.

To create a sensitive data masking configuration using the API

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) permissions.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The sensitive data masking configuration schema identifier (`schemaId`) is `builtin:sensitive-data-masking-settings`. Here is an example JSON payload with the sensitive data masking configuration:

```
[



{



"schemaId":"builtin:logmonitoring.sensitive-data-masking-settings",



"scope":"tenant",



"value":{



"config-item-title":"Added from REST API",



"masking":{



"expression":"run (\\d+?)",



"type":"STRING",



"replacement":"testing"



},



"matchers":[



{



"attribute":"log.source",



"operator":"MATCHES",



"values":[



"/var/log/syslog"



]



}



]



}



}



]
```

## SHA-1 examples

You can mask such data as your credit card or phone number, with or without specifying the capturing group.

### Mask credit card number

In this example, you will configure a sensitive data masking rule that targets a credit card number in the following log record:

```
Username: John Doe, CreditCardNumber: 1234-1234-1234-1234
```

The rule is further narrowed to the `c:\inetpub\logs\LogFiles\ex_*.log` files in two process groups: `IIS (PROCESS_GROUP-3D9D854163F8F07A)` and `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`.

Go to **Settings** > **Log Monitoring** > **Sensitive data masking**

1. Select **Create new rule** and provide the name for your configuration.
2. Provide a regular expression for the credit card number, such as `CreditCardNumber: (\d{4}-\d{4}-\d{4}-\d{4})`.
3. Select `SHA-1` for Masking type.
4. Select **Add matcher**.
5. From the **Attribute** list select **Process group**.
6. In the **Value** field, type `IIS`, and select `IIS (PROCESS_GROUP-3D9D854163F8F07A)` from the suggestions list.
7. In the **Value** field, again type `IIS`, and select the second process group from the suggestions list: `PROCESS_GROUP-4A7B47FDB53137AE`.
8. Select **Add matcher** again.
9. Select the matching attribute **Log Source**.
10. Select **Add value** and type `c:\inetpub\logs\LogFiles\ex_*.log`.
11. **Save changes**.

Only content found within a capturing group is masked, and it is transformed to the following:

```
Username: John Doe, CreditCardNumber: 7e938e089861f3975b38cff3a93cc3aa659f7779
```

### Mask phone number

In this example, you will configure a sensitive data masking rule that targets all phone numbers in the following log record for all log files.

```
Username: John Doe, PhoneNumber: +48123010100
```

Go to **Settings** > **Log Monitoring** > **Sensitive data masking**.

1. Select **Create new rule** and provide the name for your configuration.
2. Provide a regular expression for the phone number. For example, `PhoneNumber: [0-9\-\+]{9,15}`.
3. Select `SHA-1` for Masking type.
4. Select **Add matcher**.
5. **Save changes**.

The capturing group is not specified, so the full expression is treated as one capturing group and is masked so that it is transformed into the following in all log files:

```
Username: John Doe, 011897d555c81e88f286cbb74c59f4ad99ec2f8d
```

## Advanced SHA-1 examples

In the examples below, you can see how various combinations of sensitive data can be masked. You can use the listed payload JSON files in the REST API, or enter the listed masking rules, matchers, Regex expressions, and attributes directly when creating your rules via Dynatrace web UI.

### Mask credit card numbers and emails

To mask all credit card numbers and emails in your content, you need to create two separate rules, each with a different matcher:

```
{



"masking": {



"expression": "(\\d{4}-\\d{4}-\\d{4}-\\d{4})",



"type": "STRING",



"replacement": "MaskedCreditCardNumber"



},



"matchers": [



],



"enabled": true



},



{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



],



"enabled": true



}
```

### Mask Apache logs

To mask logs that are written by Apache AND whose log filename is `error.log`, you can create one rule with two matchers:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error.log"



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

To mask logs that are written by Apache OR whose log filename is `error.log`, you need to create two rules with one matcher each:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error.log"



]



}



],



"enabled": true



},



{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



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

To mask logs that are written by Apache and whose log filename starts with `error` AND ends with `log`, you need to have one rule with three matchers, each matcher having one value.

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error*"



]



},



{



"attribute": "log.source",



"values": [



"*log"



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

To mask logs that are written by Apache and whose log filename starts with `error` OR ends with `log`, you need to have one rule with two matchers, one with the process group value, and the second one with two content values, `/path/to/error*` and `*log`:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error*", "*log"



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

### Mask Apache or MySQL logs

To mask logs that are written by Apache or MySQL, you need to have either two rules or one rule with one matcher that has two values.

The scenario with two rules:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



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



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



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

The scenario with one rule with a matcher that has two values:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



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

## Regex examples

The common regex formats for sensitive data include:

Sensitive data type

ReGEx

IPv4

`\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b`

Email address

`\b[\w\-\._]+?@[\w\-\._]+?\.\w{2,10}?\b`

Credit card number

`\b[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}\b`

Phone number

`\+?[0-9]{3}-?[0-9]{6,12}\b`

### Unsupported regular expressions

Data masking occurs within the entire expression or a capturing group. An expression has to match the regular expression engine syntax, and it cannot:

* Be part of more than one capturing group
* Contain the `lookbehind` zero-length assertion in a capturing group
* Contain the `backreference` zero-length assertion in a capturing group
* Contain greedy quantifiers (such as `x?`, `x*`, or `x+`) or possessive quantifiers (such as `x?+`, `x*+`, or `xx++`). Use lazy/reluctant qualifiers (such as `x??` and `x+?`) instead.

## FAQ

Where does sensitive data masking happen?

You can execute sensitive data masking in your environment so that the confidential data does not leave your infrastructure unprotected. If you import your data to Dynatrace via generic ingest, you need to mask the sensitive data on the source level, before ingestion. Alternatively, you can mask sensitive data during [Log Processing](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample13 "Example log processing scenarios."). However, if you choose to mask your data during Log processing, your data will leave your environment as log processing occurs on the Dynatrace side. Therefore, it is safer to mask it within your environment.

How many capturing groups are supported?

One. If none is provided, then the entire scope of the regular expression you provide is treated as one capturing group.

## Sensitive data masking limits

Be aware of the following limitations to sensitive data masking:

* If the masking process takes too much time, the log file affected is blocked until the restart of OneAgent or any configuration change, and then you get the `File not monitored - incorrect sensitive data masking rule` message.

## Related topics

* [Data privacy and security](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.")
* [Log Monitoring default limits (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.")