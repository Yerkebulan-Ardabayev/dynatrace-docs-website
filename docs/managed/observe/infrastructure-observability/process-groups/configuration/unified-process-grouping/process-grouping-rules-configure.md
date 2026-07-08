---
title: Configure process grouping rules
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/unified-process-grouping/process-grouping-rules-configure
---

# Configure process grouping rules

# Configure process grouping rules

* How-to guide
* 5-min read
* Published Mar 24, 2026

With process grouping rules, you can merge multiple process groups into one or split a process group into separate, more granular groups.

## Before you begin

Prior knowledge

* [Process grouping rules FAQ](#faq)

Prerequisites

* Dynatrace environment with **process grouping rules** enabled.
* Permissions: **Environment admin** or **process group configuration** rights.

## Access process grouping rules settings

1. Go to **Settings** > **Processes and containers** > **Process group detection** > **Process grouping rules**.

## Initial setup

1. Select **Add rule**.
2. Optional Choose a **Custom technology name**. This name will appear on the process group instance screen.
3. Select **Extract process groups**.

## Define group properties

1. Optional Choose a **Process group display name**.

   If you leave this field empty, Dynatrace generates a name for the group automatically.
2. Choose the reporting mode by selecting an option in **Report process group**.

   Reporting options

   * **Always:** The process is always marked as important and its data is always sent to the server. Available for both deep-monitored and non-deep monitored processes.
   * **Automatic:** Only processes that OneAgent considers important are sent to the server. These processes satisfy at least one of two conditions:

     + Deep-monitored processes.
     + High-resource consuming processes.
   * **Never:** Process is never reported.
3. Optional Choose a **Type of captured processes**.

   Usage guidance

   * You can use this option to restrict the created rule to specific process types to avoid mixing deep-monitored properties, which can lead to confusing results.
   * If you intend to monitor more than one technology, leave this field empty.

## Define detection rules

1. Select **Add detection rule**.

   Multiple conditions

   * You can add multiple conditions. Added conditions appear in the **Summary** section below.
   * All conditions must be met for the rule to match.
2. Select a **Property** to detect.
3. Create a detection condition using one of the matching functions.

   Matching functions

   * `$contains(svc)` — Matches if `svc` appears anywhere in the process property value.
   * `$eq(svc.exe)` — Matches if `svc.exe` matches the process property value exactly.
   * `$prefix(svc)` — Matches if `svc` matches the prefix of the process property value.
   * `$suffix(svc.py)` — Matches if `svc.py` matches the suffix of the process property value.

   For example, `$suffix(svc.py)` would detect processes named `loyaltysvc.py` and `paymentssvc.py`.
4. Optional Select **Case sensitive**. When enabled, matching conditions are case sensitive. When disabled, matching conditions are case insensitive.

## Define grouping rules

The grouping rule determines how matched processes are split or merged.

1. Choose if the rule should be a [standalone rule](#standalone-rules).
2. Select an **ID type** to define which property identifies your process group.

   Custom ID calculation parameter

   Enter a **Process group identifier**. This identifier is used by Dynatrace to recognize this process group. All processes matched by the detection rule receive this same seed for ID calculation, which results in all matched processes being merged into a single process group.

   Existing process property

   1. Select a **Property**. Processes are dynamically split or merged based on the selected property value:

      * Processes that share the same property value are merged into one group.
      * Processes with different values are split into separate groups.
   2. Optional Expand **Advanced settings** to set delimiters:

      * **Delimit from** — Where the relevant portion of the property value starts.
      * **Delimit to** — Where the relevant portion of the property value ends.
3. Optional Define a **Process ID source** property to identify individual processes.
4. Optional Add **Advanced settings** to set delimiters.

   Advanced settings

   * **Delimit from** — Where the relevant portion of the property value starts.
   * **Delimit to** — Where the relevant portion of the property value ends.

## Examples

Split process groups

You have `server.js` processes that spawn `worker.js` workers, all managed by PM2 process manager:

```
NodeJS v18.20.6 PM2 Process Manager



\_ node /my/path/server.js



|   \_ /bin/node /my/path/worker.js



\_ node /my/path/server.js



|   \_ /bin/node /my/path/worker.js



\_ node /my/path/server.js



|   \_ /bin/node /my/path/worker.js



\_ node /my/path/server.js



\_ /bin/node /my/path/worker.js
```

All these processes are automatically grouped together. The PM2 process manager starts processes in a special type of container, which causes command line swapping. Because of this, you cannot use the command line for splitting. To split them into groups of server processes and worker processes, use the `Node.js script name` property.

1. In **Type of captured processes**, select `Node.js`.
2. Add a detection rule with **Property** set to `Node.js script name` and condition `$eq(worker.js)`.
3. Add a detection rule with **Property** set to `Node.js script name` and condition `$eq(server.js)`.
4. In **Define grouping rules**, enable **Standalone rule**.
5. Set **ID type** to **Existing process property** and select `Node.js script name`.

This splits the matched processes into separate groups based on the script name — one group for `server.js` and one for `worker.js`.

Merge process groups

You have two processes:

```
\_ node /my/path/server.js



|



\_ python /my/path/server.py
```

Dynatrace automatically groups these separately because the server processes use different technologies. To merge them into a single group, find a common property shared only by the desired processes. For example:

* Environment variable
* Executable path
* Any common property that is characteristic of the desired processes only. If the property is not unique to those processes, other processes may be grouped together unintentionally.

## FAQ

What are standalone rules?

Process grouping rules provide the option to define process groups and process group instances through standalone rules. To define standalone rules, enable the feature while creating a new rule. This results in the following:

* Default Dynatrace separation rules are disabled for the detected process.
* The standalone rule is the only rule used to create the process group.

Standalone rules are valid only for deep monitored processes.

What is the difference between Command line and Command line - single argument?

Two common properties used for defining detection rules are `Command line` and `Command line - single argument`. Despite the similar names, they are distinct properties with different matching behavior:

* The **Command line** property represents the whole command line, including the executable.
* The **Command line — single argument** property treats each argument separately.

For a process such as:

```
myProgram.exe --instance=10 --port=9090 --arg=32
```

**Command line** matches the full string, so the following conditions apply:

* `$contains(--port=9090)`
* `$suffix(=32)`
* `$prefix(my)`
* `$eq(myProgramm.exe --instance=10 --port=9090 --arg=32)`

**Command line — single argument** matches each argument individually, so the following conditions apply:

* `$contains(--port=9090)`
* `$suffix(exe)`, `$suffix(=10)`, `$suffix(9090)`, `$suffix(arg=32)`
* `$prefix(my)`, `$prefix(--instance)`, `$prefix(--p)`, `$prefix(--arg=)`
* `$eq(myProgramm.exe)`, `$eq(--instance=10)`, `$eq(--port=9090)`, `$eq(--arg=32)`

What are legacy grouping variables?

The following environment variables are legacy variables which should only be used as a last resort, as they can lead to errors. These variables are accessible as environment variables, as well as Dynatrace custom cluster ID variables and Dynatrace custom node ID variables.

Dynatrace custom cluster ID variables:

* `DT_CLUSTER_ID`
* `RUXIT_CLUSTER_ID`

Dynatrace custom node ID variables:

* `DT_NODE_ID`
* `RUXIT_NODE_ID`

When is a deep-monitored process restart required?

Restart deep-monitored processes after each configuration change.

To help you with this, Dynatrace displays a **Restart required** warning on each process group instance when it detects that the loaded configuration is outdated.

Note that changes to technology or group name in a rule don't trigger the warning, so the old technology or group name may still appear in the UI.

Which processes cannot be monitored with process grouping rules?

The following processes cannot be monitored with process grouping rules:

* `conhost.exe`
* `cmd.exe`

This is because an ID can't be calculated for them. Other processes can spawn thousands of these processes, so the OS Agent skips certain data for them — such as working directory, command line, and container properties — which are crucial for the ID calculation.