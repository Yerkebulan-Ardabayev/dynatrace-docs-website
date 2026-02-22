---
title: Update OneAgent on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux
scraped: 2026-02-22T21:12:24.292665
---

# Update OneAgent on Linux

# Update OneAgent on Linux

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

OneAgent installed in full-stack mode has a built-in, configurable auto-update mechanism.

See [OneAgent update](/docs/ingest-from/dynatrace-oneagent/oneagent-update "Learn how to update OneAgent.") for an overview of OneAgent update, including how to monitor updates and how to create update windows.

## Configure OneAgent updates

You can configure OneAgent update globally, per host group, and per host.

Configure global OneAgent update

When automatic updates are turned on globally, whenever a new version of OneAgent becomes available, all of your installed OneAgent instancesâexcept where you have turned off auto-updates at the host group or host levelâwill automatically download the update and upgrade their binaries and configuration files.

Automatic update settings at the host group and individual host level override global settings.

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. Select one of the update options:

   * **Automatic updates at earliest convenience**  
     Update all OneAgents automatically, regardless of update windows.
   * **Automatic updates during update windows**  
     Update all OneAgents automatically during the selected update window.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update OneAgents.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host group OneAgent update

OneAgent update settings at the host group level override global settings and are overridden by settings at the host level.

1. Open the **Host group settings** page.  
   Access alternatives:

   * Go to **Settings** > **Monitoring** > **Monitoring overview**, find any host that is in the host group you want to configure, and select the host group name (not the host name).
   * Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**, open a host page, and expand the **Properties and tags** section. If the host belongs to a group, there is a link to it under **Host group**.
   * Go to **Deployment Status** > **OneAgents**. If a host belongs to a host group, a link to the host group settings page is displayed under the host name.
2. On the **Host group settings** page, select **OneAgent updates** on the left side of the page.
3. Select one of the update options:

   * **Inherit global update settings**  
     Follow the global update settings for updating OneAgents in this host group.

     + The current global setting is displayed in parentheses on this line.
     + To go to the global configuration page, select the `global` link.
   * **Automatic updates at earliest convenience**  
     Update all OneAgents in this host group automatically, regardless of update windows. Ignore the global update settings.
   * **Automatic updates during update windows**  
     Update all OneAgents in this host group automatically during the selected update window. Ignore the global update settings.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update OneAgents in this host group. Ignore the global update settings.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host-level OneAgent update

OneAgent update settings at the host level override OneAgent update settings at the global and host group levels.

1. Open the **Host** page for the host you want to configure.  
   Access options:

   * Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and then select the host.
   * Go to **Settings** > **Monitoring** > **Monitoring overview**, select the **Hosts** tab, and then select the host.
2. On the **Host** page, open the browse menu (**â¦**) and select **Settings**.
3. Select **OneAgent updates** on the left side of the page.
4. Select one of the update options:

   * **Inheritâ¦**  
     Follow the host group or global update settings for updating this OneAgent.

     + If the selected host belongs to a host group, the current host group setting is displayed in parentheses on this line, and the group name is a link to the host group configuration page.
     + If the selected host does not belong to a host group, the global setting is displayed in parentheses on this line, and "global" is a link to the global configuration page (**Settings** > **Updates** > **OneAgent updates**).
   * **Automatic updates at earliest convenience**  
     Update this OneAgent automatically, regardless of update windows. Ignore the host group update settings.
   * **Automatic updates during update windows**  
     Update this OneAgent automatically during the selected update window. Ignore the global update settings.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update this OneAgent. Ignore the global update settings.

Manually update OneAgent on individual hosts

To manually update OneAgent running on an individual host:

1. Go to **Settings > Monitoring > Monitoring overview**.
2. Select the **Hosts** tab.
3. To update OneAgent or download the latest version, select **Update** next to the name of the host you're interested in.

   The **Update** button appears only if the installed version of OneAgent on a specific host is outdated and if it is a full-stack OneAgent. This button doesn't appear with PaaS and standalone OneAgents.
4. Select **Update now**.  
   If the **Update now** button is disabled, you don't have permissions to download the installer.

Alternatively, you can download the latest version of the OneAgent installer, copy it manually to the target host, and perform installation directly on the target host.

Select OneAgent version to install on new hosts

To control which version of OneAgent is automatically installed on all new hosts:

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. In **Update mode**, select **No automatic updates** to disable automatic OneAgent updates.

   For details on how to disable OneAgent automatic updates on Paas/Kubernetes, see [DynaKube parameters for Dynatrace Operator on Kubernetes/OpenShift](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").
3. In **Target version**, select the version of OneAgent to install on all new hosts.

The selected OneAgent version is also used for PaaS integrations.

Select OneAgent version to update to

To select which version of OneAgent to update to

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. In the **Target version** list, you can specify a particular version by OneAgent version number or select a relative target version:

   * **Latest stable version**  
     The most recent stable OneAgent version that is available in your environment. The actual version number is displayed in parentheses.
   * **Previous stable version**  
     The stable version before **Latest stable version**. The currently corresponding version number is displayed in parentheses. The OneAgent version number increases by *two* for each release, so this number will be *two* less than the latest version number.
   * **Older stable version**  
     The stable version before **Previous stable version**. The currently corresponding version number is displayed in parentheses. The OneAgent version number increases by *two* for each release, so this number will be *four* less than the latest version number.

* **Specific OneAgent version**

The target version is used for:

* Automatic updates
* Automatic updates during maintenance windows
* Manual updates when you select the version you want to update to

You can set the target version and update mode at:

* **Environment level**
  Affects all OneAgents of an environment. Is also used for Deployment API.
* **Host group**
  Affects all OneAgents of a host-group. Overrides the environment level. Does not affect Deployment API.
* **Host**
  Affects OneAgent on this host. Overrides host group and environment-level configuration. Does not affect Deployment API.

If you select an older version than a currently deployed version, you won't be able to downgrade OneAgent. You will need to install a newer version over an existing OneAgent version.

## System requirements

### Disk space

For details, see [OneAgent files and disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.")

### Free memory

Your host requires 200 MB free memory to run OneAgent update.

## Check installed version of OneAgent

Use one of these methods to check which version of OneAgent you currently have installed.



### OneAgent command-line interface

Run `oneagentctl` with the `--version` parameter. For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#display-oneagent-version "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Host Overview

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Click the host you are interested in.
3. Expand **Properties** under the host's name. The installed version of OneAgent is included in the listed properties.

### Deployment status

1. Go to **Deployment Status**.
2. Click the **All hosts** or **Recently connected hosts** tab.
3. Expand the host entry you are interested in. The installed version of OneAgent is included in the information that shows up.