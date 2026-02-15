---
title: Organize your environment using host groups
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups
scraped: 2026-02-15T09:00:16.923603
---

# Organize your environment using host groups

# Organize your environment using host groups

* How-to guide
* 3-min read
* Updated on Aug 21, 2023

Host groups enable you to categorize and manage multiple hosts that share similar characteristics or purposes within your environment.

## Check host group assignment

To determine the host group to which a host belongs

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

## List all hosts in a host group

To list all hosts in a host group

1. Go to **Deployment Status** and select **OneAgents**.  
   This lists all hosts in your deployment.
2. In the filter bar, select **Host group** and the name of the host group.  
   This lists all hosts in the selected host group.

## Assign a host to a host group

You can assign a host to a host group during or after [OneAgent installation](/docs/ingest-from "Learn how to install and configure ActiveGate and OneAgent on various platforms.").

* **During** OneAgent installation

  To assign a host to a host group when you install OneAgent, use the `--set-host-group` parameter, shown in the example below.

  `/bin/sh Dynatrace-OneAgent-Linux-1.177.65.sh --set-host-group=MyHostGroup`

  On Windows, you can also type the group name in the installer UI.
* **After** OneAgent installation

  To assign a host to a host group after you install OneAgent

  CLI

  Dynatrace UI

  Use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-groups "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command-line tool.

  1. Go to **Deployment Status** and check the box next to the desired host.
  2. Select **modify host group** at the bottom of the page.
  3. Select **Run action**.
  4. Now you can either choose **Specify host group to be assigned** or **Remove current host group assignment**.
  5. Select **Next**.
  6. Review your changes and select **Apply changes**.

  Note that OneAgent will automatically restart after the changes are applied.

Host group string requirements

* Can contain only alphanumeric characters, hyphens, underscores, and periods.
* Must not start with `dt.`.
* Maximum length is 100 characters.

The host group is statically assigned to the host. Each host belongs to at most one host group and the host group can be changed by using the 'oneagentctl' command, [remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API."), or by re-installing OneAgent. Host groups are displayed, for example, on the **Hosts** page from the [**Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations#hosts "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.") app, and on the **Monitoring overview** page, where you can select the **Host group** link to edit the settings for all hosts in a host group.

![Host groups](https://dt-cdn.net/images/host-groups-1200-d314d1729f.png)

## How host groups affect your monitoring environment

Host groups are sets of hosts. Each group can be configured on the host-group level. This makes it easy to change the settings for a large number of hosts. You can define alerting thresholds and OneAgent update settings on a per-host-group basis. In the example below, the host group accepts the globally-configured anomaly thresholds without overriding them.

![Host groups](https://dt-cdn.net/images/host-groups2-1422-845f78e968.png)

You can also define the OneAgent update settings and trigger the update for all the OneAgent installations of a single host group, as shown in the example below. Here the global settings are overridden and all OneAgent installations are automatically updated whenever a new version is released.

![Host groups](https://dt-cdn.net/images/host-groups3-1426-aa75a3847f.png)

Additionally, host groups affect how process groups are detected. When the same process is running in two different host groups, Dynatrace will create one process group for each host group. This means you can also configure process groups differently depending on which host group they run in. Consequently, services are also grouped per host group. So you can configure services differently per host group.

Host groups can also be used in [tagging rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") and for defining [management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") so you can apply additional context information to the different entities in Dynatrace, based on host groups. As shown in the example below, you can tag entities based on the host group they belong to.

![Host groups](https://dt-cdn.net/images/host-groups4-1414-8039d74ee9.png)