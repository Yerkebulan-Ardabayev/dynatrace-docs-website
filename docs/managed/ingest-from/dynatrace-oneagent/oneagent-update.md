---
title: OneAgent update
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/oneagent-update
---

# OneAgent update

# OneAgent update

* 3-min read
* Updated on Jun 23, 2026

OneAgent has a built-in, configurable auto-update mechanism.

OneAgent automatic updates are easy

With auto-update turned on, you don't have to worry about manually updating the OneAgents running in your environment. Each time a new version is released, OneAgent automatically downloads all necessary binaries and libraries and installs them for you. No manual configuration is required.

Following OneAgent automatic updates, you do need to restart all server processes. This is because some components of OneAgent keep running in processes that are monitored by Dynatrace (for example, Java, .NET, Apache, and IIS).

* Before restart, these processes will continue to be monitored with the previous version of OneAgent.
* After restart, these processes will be monitored with the latest version of OneAgent.

OneAgent automatic updates are flexible

By default, global automatic OneAgent updates are turned on, but this is configurable at the global, host group, and host level. At each level, you can choose one of the following OneAgent update strategies:

* **Automatic updates at earliest convenience**: OneAgent updates as soon as a new version is available, regardless of update windows.
* **Automatic updates during update windows**: OneAgent updates only during a configured [update window](#maintenance-windows). The same windows govern Environment ActiveGate updates, see [Configure update windows](#maintenance-windows) below.
* **No automatic updates**: OneAgent doesn't update on its own. You aren't notified when instances are outdated.

Additionally:

* At the host group level, you can choose to inherit the global OneAgent update settings.
* At the host level, you can choose to inherit the host group OneAgent update settings.

Host settings override host group settings, and host group settings override global settings.

OneAgent automatic updates are secure

* OneAgent communication is encrypted.
* OneAgent installers are signed and the signature is verified for each downloaded installer package. If the verification fails, the auto-update attempt is aborted.

OneAgent updates are also manageable through the Dynatrace API

In addition to the Dynatrace web UI procedures described here, you can use the [OneAgent configuration API](/managed/dynatrace-api/configuration-api/oneagent-configuration "Manage OneAgent configuration via the Dynatrace API.") to manage OneAgent updates.

* [Host level](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Manage the configuration of OneAgent instances on your hosts via the Dynatrace API.")
* [Host group level](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group "Manage the configuration of OneAgent instances in your host groups via the Dynatrace API.")
* [Environment level](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide "Manage environment-wide configuration of OneAgent via the Dynatrace API.")

OneAgent won't automatically be updated when first installed. By default, Dynatrace waits 45 minutes before updating hosts (both EC2 and non-EC2).

This delay is not enforced for manual updates via **Update now**, which means that updates initiated in this way are applied immediately.

## Monitor OneAgent updates

To monitor OneAgent updates, go to **Settings** > **Deployment** > **OneAgent updates**.

* Check or change the auto-update settings on the environment level
* Monitor the update status per operating system (Linux, AIX, and Windows)
* Check or change the auto-update status of the real user monitoring JavaScript library

Monitor global OneAgent update

For environment-wide monitoring of OneAgent updates, go to **Settings** > **Deployment** > **OneAgent updates**.

#### OneAgent updates

Use this section to check or change the environment-level setting:

* **Automatic updates at earliest convenience**  
  Update all OneAgents automatically, regardless of update windows.
* **Automatic updates during update windows**  
  Update all OneAgents automatically during the selected update window.

  + When you choose this setting, a list of available update windows is displayed. Select one.
  + To configure a new update window for OneAgent updates, go to **Settings** > **Deployment** > **Update windows**.
* **No automatic updates**  
  Do not automatically update OneAgents.

#### Automatic updates status

Use this section to check the status of automatic updates per operating system. For each operating system, this page displays a count of OneAgent instances with a breakdown by OneAgent update status.

#### Real user monitoring JavaScript library

Turn on **Automatically update real user monitoring JavaScript library** to keep the real user monitoring JavaScript library up to date automatically. The current version of the library is listed under the switch.

OneAgent update statuses

* Incompatible—No auto-update possible. Manual update may be needed for this host/version.
* Update available—There is an update available for this OneAgent version.
* Suppressed—No download because auto-update is not supported for this deployment.
* Unknown—This may mean, for example, that the host was not found, or that no auto-update is available for it.
* Up to date—The installer version is up to date.
* Update in progress—This host has requested and downloaded an installer, but has not reconnected with the expected new version yet.
* Update pending—An update is configured for this host. It takes priority over any other activities or updates for newly seen hosts, but the update may not start immediately for reasons such as internal cluster upgrades, throttling, and stability checks.
* Update problem—There was a problem while performing the update. Please review the details.
* Scheduled—An update is scheduled to occur during a configured update window.

## Configure OneAgent updates

You can configure OneAgent update globally, per host group, and per host.

Configure global OneAgent update

When automatic updates are turned on globally, whenever a new version of OneAgent becomes available, all of your installed OneAgent instances—except where you have turned off auto-updates at the host group or host level—will automatically download the update and upgrade their binaries and configuration files.

Automatic update settings at the host group and individual host level override global settings.

1. Go to **Settings** > **Deployment** > **OneAgent updates**.
2. Select one of the update options:

   * **Automatic updates at earliest convenience**  
     Update all OneAgents automatically, regardless of update windows.
   * **Automatic updates during update windows**  
     Update all OneAgents automatically during the selected update window.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Deployment** > **Update windows**.
   * **No automatic updates**  
     Do not automatically update OneAgents.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host group OneAgent update

OneAgent update settings at the host group level override global settings and are overridden by settings at the host level.

1. Open the **Host group settings** page.  
   Access alternatives:

   * Go to **Settings** > **Monitoring** > **Monitoring overview**, find any host that is in the host group you want to configure, and select the host group name (not the host name).
   * Go to **Hosts**, open a host page, and expand the **Properties and tags** section. If the host belongs to a group, there is a link to it under **Host group**.
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
     + To configure a new update window for OneAgent updates, go to **Settings** > **Deployment** > **Update windows**.
   * **No automatic updates**  
     Do not automatically update OneAgents in this host group. Ignore the global update settings.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host-level OneAgent update

OneAgent update settings at the host level override OneAgent update settings at the global and host group levels.

1. Open the **Host** page for the host you want to configure.  
   Access options:

   * Go to **Hosts** and then select the host.
   * Go to **Settings** > **Monitoring** > **Monitoring overview**, select the **Hosts** tab, and then select the host.
2. On the **Host** page, open the browse menu (**…**) and select **Settings**.
3. Select **OneAgent updates** on the left side of the page.
4. Select one of the update options:

   * **Inherit…**  
     Follow the host group or global update settings for updating this OneAgent.

     + If the selected host belongs to a host group, the current host group setting is displayed in parentheses on this line, and the group name is a link to the host group configuration page.
     + If the selected host does not belong to a host group, the global setting is displayed in parentheses on this line, and "global" is a link to the global configuration page (**Settings** > **Deployment** > **OneAgent updates**).
   * **Automatic updates at earliest convenience**  
     Update this OneAgent automatically, regardless of update windows. Ignore the host group update settings.
   * **Automatic updates during update windows**  
     Update this OneAgent automatically during the selected update window. Ignore the global update settings.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Deployment** > **Update windows**.
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

1. Go to **Settings** > **Deployment** > **OneAgent updates**.
2. In **Update mode**, select **No automatic updates** to disable automatic OneAgent updates.

   For details on how to disable OneAgent automatic updates on Paas/Kubernetes, see [DynaKube parameters for Dynatrace Operator on Kubernetes/OpenShift](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").
3. In **Target version**, select the version of OneAgent to install on all new hosts.

The selected OneAgent version is also used for PaaS integrations.

Select OneAgent version to update to

To select which version of OneAgent to update to

1. Go to **Settings** > **Deployment** > **OneAgent updates**.
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

## Configure update windows

Use update windows to schedule automatic OneAgent and Environment ActiveGate updates. They apply when you select **Automatic updates during update windows** for OneAgent (at the global, host group, or host level) or **Automatic (during update window)** for ActiveGate (at the environment or per-ActiveGate level). The same windows govern both products, so configuring a window once applies it to every host and Environment ActiveGate that opts in.

* For procedures to list, create, edit, turn on, turn off, delete, and apply windows, see below.
* For ActiveGate-specific update mode, target version, and concurrency rules, see [Update ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/update-activegate "Configure Environment ActiveGate automatic updates---update mode, target version, and update windows---and download or install manually.").

Update windows are shared with Environment ActiveGate. Creating, editing, turning off, or deleting a window also affects the ActiveGate updates that use it.

Update windows currently do not apply in Kubernetes environments.

List all update windows

1. Go to **Settings** > **Deployment** > **Update windows**.
2. Review the list of all existing update windows.

Turn an update window on or off

1. Go to **Settings** > **Deployment** > **Update windows**.
2. Find the update window you want to turn on or off.
3. Turn the switch on or off.

Delete an update window

1. Go to **Settings** > **Deployment** > **Update windows**.
2. Find the update window you want to delete.
3. Select **X** in the **Delete** column.

Create or edit an update window

1. Go to **Settings** > **Deployment** > **Update windows**.
2. Open an update window for editing:

   * To create a new update window, select **Create update window**.
   * To edit an existing update window, expand **Details** for the update window you want to edit.
3. Set **Name** to the name under which you want to list this update window in the Dynatrace web UI and API.
4. Describe the update window:

   * To specify a single, nonrecurring update window:

     + Set **Recurrence** to `Once`
     + Set **Update time** to the single date and time to update OneAgent
   * To schedule an update window every x days:

     + Set **Recurrence** to `Daily intervals`
     + Set **Every x days** to the number of days between updates (`1` = every day, `2` = every two days, `3` = every three days, etc.)
     + Set **Update time** to the time during the specified days when you want to update OneAgent
   * To schedule an update window every x weeks on certain days of the week:

     + Set **Recurrence** to `Weekly intervals`
     + Turn on each day of the week you want to add to the update window
     + Set **Every x weeks** to the number of weeks between updates (`1` = every week, `2` = every two weeks, `3` = every three weeks, etc.)
     + Set **Update time** to the time during the specified days when you want to update OneAgent
   * To schedule an update window every x months on a certain day of the month:

     + Set **Recurrence** to `Monthly intervals`
     + Set **Day of the month** to the day of the month on which to update OneAgent
     + Set **Every x months** to the number of months between updates (`1` = every month, `2` = every two months, `3` = every three months, etc.)
5. Select **Save changes**.

After you configure an update window, you can use it to configure automatic OneAgent updates at the global, host group, or host level.

Apply an update window to OneAgent updates

You can apply an update window to OneAgent automatic updates at the environment, host group, or host level.

**Environment**

1. Go to **Settings** > **Deployment** > **OneAgent updates**.
2. Select **Automatic updates during update windows**.
3. When the list is displayed, select the update window you want to apply at this level.

**Host group**

1. Go to **Settings** > **Monitoring** > **Monitoring overview**.
2. Find any host that is in the host group you want to configure.
3. Select the host group name (not the host name).
4. On the **Host group settings** page, select **OneAgent updates** on the left side of the page.
5. Select **Automatic updates during update windows**.
6. When the list is displayed, select the update window you want to apply at this level.

**Host**

1. Open the **Host** page for the host you want to configure.  
   Access options:

   * Go to **Hosts** and then select the host.
   * Go to **Settings** > **Monitoring** > **Monitoring overview**, select the **Hosts** tab, and then select the host.
2. On the **Host** page, open the browse menu (**…**) and select **Settings**.
3. Select **OneAgent updates** on the left side of the page.
4. Select **Automatic updates during update windows**.
5. When the list is displayed, select the update window you want to apply at this level.

API

For API equivalents, see [OneAgent configuration API](/managed/dynatrace-api/configuration-api/oneagent-configuration "Manage OneAgent configuration via the Dynatrace API.").

## Turn off automatic updates

We don't recommend that you turn off OneAgent automatic updates. For troubleshooting, you can temporarily turn off automatic updates in Dynatrace at **Settings** > **Deployment** > **OneAgent updates**. If you have very strict software rollout rules, however, you can turn off auto-updates permanently with the [OneAgent command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#automatic-updates "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").