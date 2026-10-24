---
title: Process grouping rules
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/process-grouping-rules
---

# Process grouping rules

# Process grouping rules

* Explanation
* 3-min read
* Updated on Oct 20, 2026

OneAgent version 1.329+

In large, dynamic environments, the number of processes running on your hosts can become overwhelming. Dynatrace automatically organizes these processes into process groups so you can monitor them together. When the default grouping doesn't match how you want to view your processes, process grouping rules let you split, merge, or exclude process groups using rules based on process properties detected by OneAgent.

## What are process grouping rules?

Process grouping rules define how OneAgent groups monitored processes into process groups (PGs) and process group instances (PGIs). You can apply rules at the environment, host group, Kubernetes cluster, and host levels.

Simple detection rules, advanced detection rules, and declarative process grouping are now deprecated. Process grouping rules replace all three. You can migrate all valid detection rules to the new format. For details, see [Migrate to process grouping rules](/managed/observe/infrastructure-observability/process-groups/configuration/process-grouping-rules/process-grouping-rules-migration "Learn how to migrate your process groups and process group instances to process grouping rules.").

## Capabilities

* Split one process group into more granular groups.
* Merge multiple process groups into one.
* Exclude specific processes from monitoring using reporting modes: Always, Automatic, or Never.

Rules configured on scopes lower than environment and Kubernetes cluster, that is, on host group or host level, might currently not work reliably in cloud-native full-stack monitoring.

## Compatibility considerations

Be cautious when using process grouping rules, as changes may cause compatibility issues with extensions or plugins that depend on process group instance (PGI) names or technologies. Such modifications can lead to malfunctions and loss of data or metrics in monitored processes.

To minimize the risk of compatibility issues when setting up process grouping rules, you can:

* Verify that your extensions or plugins will not be affected by the new process grouping rules.
* Test the process grouping rules in a controlled environment before applying them in a production environment to ensure they do not cause any unintended side effects.
* Review and update your process grouping rules regularly to ensure they align with any changes in your environment or application setup.

## Use cases

For configuration steps, see [Configure process grouping rules](/managed/observe/infrastructure-observability/process-groups/configuration/process-grouping-rules/process-grouping-rules-configure "Learn how to split and merge process groups and process group instances through process grouping rules.").

### Split processes by part of their command line

Consider the following scenario:

* Processes that belong together share part of their command line, such as a specific argument.
* You want to group them based on that part.

**Solution:** Match a substring of the command line.

### Split processes by an environment variable

Consider the following scenario:

* Processes that belong together share an environment variable value.
* You want to group them based on that variable.

**Solution:** Group processes by the environment variable property.

### Group Node.js processes by script

Consider the following scenario:

* You run Node.js processes that are grouped together.
* You want them separated by the script they run.

**Solution:** Group processes by the Node.js script name property.

## Configuration and reference

[#### Migrate to process grouping rules

Learn how to migrate your process groups and process group instances to process grouping rules.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/process-groups/configuration/process-grouping-rules/process-grouping-rules-migration)[#### Configure process grouping rules

Learn how to split and merge process groups and process group instances through process grouping rules.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/process-groups/configuration/process-grouping-rules/process-grouping-rules-configure)