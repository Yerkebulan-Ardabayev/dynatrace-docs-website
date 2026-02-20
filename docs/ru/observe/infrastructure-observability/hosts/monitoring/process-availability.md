---
title: Process availability
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/monitoring/process-availability
scraped: 2026-02-20T21:23:28.611904
---

# Process availability

# Process availability

* How-to guide
* 5-min read
* Updated on Jan 21, 2026

OneAgent version 1.237+

To monitor the availability of key processes on your hosts, you need to define monitoring rules. After you create a rule, when a matching process is missing on a host, Dynatrace issues an alerting event.

You can analyze the latest activity of the processes defined for process availability in the [Process instance snapshots](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring#snapshots "Monitor hosts with Dynatrace.") section on the host overview page.

## Determine scope

You can create rules to apply at the environment, host group, and host levels. Lower-level rules override higher-level rules. For example, a rule created on the host level overrides a rule with the same name created on the environment level.

## Define monitoring rule

1. Go to the **Process availability** page for the level on which you want the rule to apply:

   * **Environment**: go to **Settings** and select **Processes and containers** > **Process availability**.
   * **Host group**: go to the host group page at `https://your-environment/ui/settings/HOST_GROUP-NAME` and select **Process availability**.
   * **Host**: go to the host overview page, select **More** (**â¦**), go to **Settings**, and select **Process availability**.
2. On the **Process availability** page, select **Add monitoring rule**. Process availability can comprise multiple individual detection rules. A process is identified if all of the individual detection rules match.
3. In **Monitoring rule name**, enter the name under which the rule will be listed.
4. Under **Operating system** (OneAgent version 1.287+), select the operating systems on which the monitoring rule should be applied. You can select more than one.

   * Windows
   * Linux
   * AIX
5. Set **Minimum number of matching processes** (OneAgent version 1.287+) to the minimum number of processes that should match this rule. If fewer processes match this rule on any individual host, an alert is triggered.
6. Select **Add detection rule** to define a detection rule.

   A single monitoring rule can have multiple detection rules. If you add more than one detection rule, a process is identified if all the detection rules match (AND relation).

   * **Rule scope**âYour selection of **Process** or **Host** determines the subsequent configuration details. Expand below for more.

     Process

     + **Select process property**âThe object against which your detection rule will be tested:

       - **Command line - single argument**âEach command line parameter is evaluated individually. Evaluation is case-sensitive.
       - **Command line**âOneAgent version 1.333+ The entire command line is evaluated. Evaluation is case-sensitive.
       - **Executable path**âRules are not case-sensitive
       - **User**âOneAgent version 1.287+ User is case-sensitive for Linux and AIX, not case-sensitive for Windows.

     The comparators evaluate each command line parameter individually for the **Command line - single argument** property (referred to as **Command line** in versions prior to 1.333). For example, a process `python my.py -ab -cd -ef` will be matched with a condition `$contains(cd)`, `$eq(-ab)`, but won't be matched with `$suffix(-cd -ef)` because `-cd` and `-ef` are distinct arguments, which are processed separately.

     OneAgent version 1.307+ The executable is also treated as a part of the command line as its the first argument.

     + **Condition**âDepending on what you want your rule to match, you can define a string that uses:

       - `$contains` matches if the property contains the specified value. For example, `$contains(keepalived)` matches if `keepalived` occurs anywhere in the property.
       - `$eq` matches if the property exactly matches the specified value. For example, `$eq(-d)` matches if `-d` exactly matches the property.
       - `$prefix` matches if the property starts with the specified value. For example, `$prefix(/usr/sbin/keepalived)` matches a property that starts with `/usr/sbin/keepalived`.
       - `$suffix` matches if the property ends with the specified value. For example,`$suffix(keepalived)` matches a property that ends with `keepalived`.

     Host

     OneAgent version 1.287+

     **Custom metadata** is user-defined key-value pairs that you can assign to hosts monitored by Dynatrace.

     By defining custom metadata, you can enrich the monitoring data with context specific to your organization's needs, such as environment names, team ownership, application versions, or any other relevant details.

     + **Key** specifies the metadata key you want to match
     + **Condition** in which you can define a string that:

       - `$contains(production)` â Matches if `production` appears anywhere in the host metadata value.
       - `$eq(production)` â Matches if `production` matches the host metadata value exactly.
       - `$prefix(production)` â Matches if `production` matches the prefix of the host metadata value.
       - `$suffix(production)` â Matches if `production` matches the suffix of the host metadata value.

       Available logic operations:

       - `$not($eq(production))` â Matches if the host metadata value is different from production.
       - `$and($prefix(production),$suffix(main))` â Matches if host metadata value starts with production and ends with main.
       - `$or($prefix(production),$suffix(main))` â Matches if host metadata value starts with production or ends with main.

       **Escape special characters**: When including special characters such as `(` and `)` within your matching expressions, escape these characters with a tilde `~`. For example, to match the metadata value `my(amazing)property`, enter `$eq(my~(amazing~)property)`.
7. If you need to add another detection rule to this monitoring rule, repeat the previous step.
8. Select **Add property** (OneAgent version 1.249+ Dynatrace version 1.249+) to specify a custom key-value property for the event.

   * **Key**: Type `dt.` in the **Key** field for hints.
   * **Value**: Type `{` in the **Value** field for hints.

   You can use only the values that are suggested as hints.

   Example custom message in the event details:

   * **Key** = `custom.message`
   * **Value** = `The {dt.entity.host} is deployed on: {dt.os.type}`

   In this example, note that **Value** includes two keys:

   * `{dt.entity.host}`
   * `{dt.os.type}`

   The entity host and OS type values will be extracted when the rule is triggered. If the key substitution fails, both the key and the value will be unavailable.
9. When you finish defining the monitoring rule, including all detection rules that are a part of the monitoring rule, select **Save changes**.

After you save your changes:

* Your monitoring rule is added to the list of monitoring rules on the **Process availability** page. The displayed name is what you entered in **Monitoring rule name**.
* Your monitoring rule is applied at the level you selected in the first step: environment, host group, or host.

## Manage rules

Monitoring rules are listed on the **Process availability** page. Each monitoring rule in turn contains a list of one or more detection rules.

* To view or edit the details of any listed monitoring or detection rule, select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column for that rule.
* To change rule order, drag ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") any rule to a different place in the list.
* To delete a rule, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the **Delete** column and then confirm your action.
* To enable or disable a rule (monitoring rules only), use the toggle in the **Enabled** column.