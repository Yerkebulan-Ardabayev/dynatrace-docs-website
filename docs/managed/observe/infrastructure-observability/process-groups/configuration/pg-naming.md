---
title: Process group naming
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming
---

# Process group naming

# Process group naming

* How-to guide
* 6-min read
* Published Mar 21, 2018

Not only does Dynatrace automatically detect [process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring."), it also attempts to name them with intuitive names that make sense to the DevOps staff who are tasked with deploying and monitoring them. In many cases, however, the auto-generated names created by Dynatrace may either be too generic or not reflect your naming standards. To change the naming schemes of detected process groups, you need process group naming rules.

## Define a new process group naming rule

To add a new process group naming rule:

1. Go to **Settings**.
2. Select **Processes and containers** > **Process group naming**.
3. Select **Add a new rule**.
4. Enter a rule name.
5. Define the **Process group name format** including any static text string that describes the named process group. Optional placeholders are available to make it easy to dynamically include specific process-group properties in your automated process-group naming scheme. When you use one of the defined placeholders you can add a [regex](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.") to extract a portion of the detected value. To extract, for example, something from `{ProcessGroup:DetectedName}` you could use `{ProcessGroup:DetectedName/REGEX}`. The regex simply extracts the complete match. It doesn’t allow to capture groups, only atomic and lookaround groups.
6. Add one or more Conditions to the rule to match the process groups that you want to apply the naming scheme to. Conditions check for the existence of many different types of specific attribute and state values, from the check of a Docker image to a check of the CloudFoundry space that a process group runs in.

   The example condition below applies only to Java processes that are started via a JAR file that begins with `com.dynatrace.easytravel`. Looking at the **Process group name format** below, you can see that it actually takes the JAR file and applies a regular expression to it.

   ![Process group naming rule example](https://dt-cdn.net/images/pg-naming-rules1-1531-db88a8a9d8.png)

   Process group naming rule example
7. Use the **Preview** button to verify that the list of returned entities matching your new rule includes only the entities you want.

   ![Process group naming rule](https://dt-cdn.net/images/pg-naming-rules2-1133-0080ee5066.png)

   Process group naming rule

In contrast to process group detection, process group naming rules don’t require a restart of your processes and of course they don’t affect how processes are identified and grouped. These rules simply provide a fast and easy means of applying intuitive naming conventions to your processes.

## Use custom metadata to enrich naming rules

You can further enrich Dynatrace process monitoring by [incorporating your own metadata into rule conditions](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment."). You can then use your custom metadata to better refine your process group naming rules. See highlighted example below.

![Examplepg](https://dt-cdn.net/images/2021-02-17-08-28-51-1724-16065e2f77.png)

Examplepg

![Custom metadata to enrich naming rules](https://dt-cdn.net/images/pg-naming-rules4-1527-667ccd721b.png)

Custom metadata to enrich naming rules

![Custom metadata to enrich naming rules](https://dt-cdn.net/images/pg-naming-rules5-1405-111b77a025.png)

Custom metadata to enrich naming rules

With custom metadata incorporated into your process-group naming rules, you can enforce your own granular naming standards system-wide.