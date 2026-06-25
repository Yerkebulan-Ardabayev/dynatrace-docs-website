---
title: Declarative process grouping
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/declarative-process-grouping
scraped: 2026-05-12T12:07:25.643277
---

# Declarative process grouping

# Declarative process grouping

* How-to guide
* 5-min read
* Updated on Jan 07, 2026

OneAgent version 1.217+

Within large, dynamic environments, the number of processes running on your hosts can become overwhelming. For this reason, Dynatrace automatically monitors [important process group types](/managed/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.")âprocess groups that are either of a known technology or that consume significant resources.

However, Dynatrace also provides the option of monitoring specific processes that fall into neither of these two categories. This means you can monitor processes of a technology type unknown to Dynatrace that don't consume significant resources.

Starting with OneAgent version 1.307, deep-monitored processes are supported by declarative process grouping in Full-Stack Monitoring, Infrastructure Monitoring, and Discovery modes on OneAgent installer-based deployments and in Kubernetes classic full-stack deployment. For other deployments, declarative grouping is supported for processes that aren't deep-monitored.

After you make any configuration changes, restart deep-monitored processes to ensure the updates are applied.

Be cautious when using declarative process grouping, as it may cause compatibility issues with extensions or plugins that depend on Process Group Instance (PGI) names or technologies. Such modifications can lead to malfunctions and loss of data or metrics in monitored processes.

To minimize the risk of compatibility issues when setting up declarative process grouping, you can

* Verify that your extensions or plugins won't be affected by the new process grouping rules.
* Test the declarative process grouping rules in a controlled environment before applying them in a production environment to ensure they don't cause any unintended side effects.
* Regularly review and update your declarative process grouping rules to ensure they align with any changes in your environment or application setup.

Using the declarative process grouping feature, you can add fine-grained rules to match any specific process group. Declarative process grouping is based on the Settings 2.0 framework, so you can create the rules using the Dynatrace web UI or the [Settings API](#api) - see [Example JSON payload for a declarative process group configuration](#eg3).

## Create a declarative process group

To create a process group using the Dynatrace web UI

1. Go to **Settings**.
2. Select **Processes and containers** > **Declarative process grouping**.
3. Select **Add monitored technology**. The technology is a logical container to group detection rules. It will be visible as the main technology of the process group.
4. Select **Add process group**. A process group can comprise a number of individual detection rules. A process group is identified if all of the individual detection rules match.
5. Go to **Process group display name** and select a process group name.
6. Enter the **Process group identifier**. It's a unique string to let Dynatrace identify the process group.
7. OneAgent version 1.259+ Select a **Report process group** option:

   * **Always**âthe created process group is always reported to Dynatrace.
   * **Never**âthe created process group is never reported to Dynatrace.
   * **Only when resource usage is high**âthe created process group is reported if CPU, memory, or network traffic usage is over 5%. For details, refer to [Most important processes](/managed/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.").
8. Select **Add detection rule**.

   1. Select the object (process property) against which your detection rule will be tested:

      * **Command line arguments**
      * **Executable**
      * **Executable path**

      When you add the executable path, it is important to account for the differences between Windows and Linux operating systems. Windows uses backslashes as path separators, while Linux uses forward slashes. There is no automatic normalization of file paths on the OneAgent side. Therefore, it is essential to specify the correct path format for the operating system in use.
   2. Enter a **Condition**.

      In the previous step, you selected the process property that you want to examine (for example, the executable path). In this step, you specify a condition (an operator and a string) that is compared to the selected process property. You can use one of the following operators:

      * `$prefix` = starts with

        For example, `$prefix(/usr/sbin/keepalived)` is true if the selected process property starts with `/usr/sbin/keepalived`.
      * `$suffix` = ends with

        For example, `$suffix(keepalived)` is true if the selected process property ends with `keepalived`.
      * `$eq` = equals; exactly matches

        For example, `$eq(-d)` is true if the selected process property is `-d`.
      * `$contains` = contains; has this substring

        For example, `$contains(keepalived)` is true if `keepalived` occurs anywhere in the selected process property.

      The comparators work for each command line parameter separately. For example, a process `python my.py -ab -cd -ef` will be matched with a condition `$contains(cd)`, `$eq(-ab)`, but won't be matched with `$suffix(-cd -ef)` because `-cd` and `-ef` are separate arguments, which are processed separately.

      Note that the executable is also part of the command line as its first argument.

      All conditions are case insensitive.
   3. Optional Add another detection rule.

      * If you add more than one detection rule, a process is identified only when all detection rules match (AND relation).
      * If there are several rules that match the same process, only the first rule will be applied. This depends on the order of the rules.
9. When you finish defining all the rules, select **Save changes**.

After saving your changes, Dynatrace will automatically detect and monitor the newly defined custom process group across all hostsâeven on hosts that are launched following the definition of the custom process group.

## Manage declarative process grouping

To manage declarative process groups

1. Go to **Declarative process grouping** for the level you are configuring.

   Host level

   1. Go to **Hosts**.
   2. Find and select your host to display the host overview page.
   3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

   4. In the host settings, select **Declarative process grouping**.

   Host-group level

   1. Go to **Deployment Status** > **OneAgents**.
   2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
   3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

      The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

      The **Host group** property is not displayed when the selected host doesn't belong to any host group.
   4. Select the host group name in any row.

      As you have filtered by host group, all displayed hosts go to the same host group.

   5. In the host group settings, select **Declarative process grouping**.

   Environment level

   Go to **Settings** and select **Processes and containers** > **Declarative process grouping**.
2. The declarative process groups you have defined are displayed in a table under the **Add monitored technology** button.

   * To stop monitoring a listed process group, turn off **Enabled**.
   * To delete a process group from the table, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the **Delete** column.
   * To view and edit process group details, select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column.