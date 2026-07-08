---
title: Update ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/operation/update-activegate
---

# Update ActiveGate

# Update ActiveGate

* How-to guide
* 5-min read
* Updated on Jun 23, 2026

Limitations

**Auto-update** and the manual **Update now** action only support host-based deployments installed via the installer.

* [Containerized ActiveGate update behavior](/managed/ingest-from/dynatrace-activegate/activegate-in-container/differences#auto-update "Learn how containerized ActiveGate differs from host-based ActiveGate")

## View installed ActiveGates and update status

To see a list of installed ActiveGates, go to **Deployment Status** > **ActiveGates**. For each ActiveGate, the list gives the current **Version** of the ActiveGate and the **Update status** (up to date, pending, or in progress).

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") The yellow warning icon indicates that your ActiveGate is behind by more than five versions. You should update these ActiveGates as soon as possible.

ActiveGates in containers are deployed and uploaded using cloud-specific tooling. For example, Kubernetes uses [custom resource definitions](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "Monitor the Kubernetes API using Dynatrace").

### Automatic update

To manage the update functionality of a particular ActiveGate in the list, select the ActiveGate to expand the details.

## Configure automatic updates

To configure how Environment ActiveGates update:

* Go to **Settings** > **Deployment** > **ActiveGate updates**.

### Update mode

The update mode controls when an Environment ActiveGate applies a pending update.

* **Automatic (earliest convenience)** (default for new environments):
  ActiveGate downloads and installs new versions as soon as they become available. The availability check runs every 30 minutes.
* **Automatic (during update window)**:
  ActiveGate updates only during a configured [update window](/managed/ingest-from/dynatrace-oneagent/oneagent-update#maintenance-windows "Learn how to update OneAgent."). Updates that become available outside an active window are deferred until the window opens. The same update windows govern both OneAgent and ActiveGate, see [Update windows](#update-windows) below.
* **No automatic updates**:
  ActiveGate does not update on its own. When a [target version](#target-version) is configured and the ActiveGate is on an older version, you can trigger the update manually from that individual ActiveGate's update settings. See [Update now to target version](#update-now-to-target-version) below.

For existing environments, the update mode keeps your previous behavior: if auto-update was turned on, it becomes **Automatic (earliest convenience)**; if it was turned off, it becomes **No automatic updates**.

### Target version

Select which ActiveGate version Dynatrace should converge on.

* **Latest stable** (default):
  The newest stable ActiveGate version available on the cluster.
* **Previous stable**:
  One main version behind the latest stable.
* **Older stable**:
  Two main versions behind the latest stable.
* **Specific main version** (for example, `1.327`):
  Pins the ActiveGate to a chosen main version. Dynatrace automatically applies the latest sub-version of that main version. Unlike OneAgent, ActiveGate does not expose a sub-version selector; the latest sub-version of the chosen main version is always applied.

The selector displays the current main version next to each stable preset (for example, `Latest stable (currently 1.343)`) so you can see which build each preset resolves to.

The **Environment** [Deployment API](/managed/dynatrace-api/environment-api/deployment/activegate/download-activegate-latest "Download the latest ActiveGate installer via Dynatrace API.") treats the configured target version as the latest available for the environment. Build-unit protection prevents the cluster from pruning the installer for any version that's configured as a target.

Downgrade is prohibited: A configured target version is never used to roll an ActiveGate back to a lower version.

### Update windows

You configure update windows once and share them between OneAgent and Environment ActiveGate. See [Configure update windows](/managed/ingest-from/dynatrace-oneagent/oneagent-update#maintenance-windows "Learn how to update OneAgent.") on the OneAgent update page to list, create, edit, turn on, turn off, delete, and apply windows.

When the same window applies to ActiveGates, Dynatrace throttles concurrent updates per pool (see [Concurrency and safety](#concurrency-and-safety) below).

### Scope hierarchy

ActiveGate auto-update settings follow this override order:

1. Per-ActiveGate settings (configured for the individual ActiveGate at **Settings** > **Deployment** > **ActiveGate updates**)
2. Environment defaults

By default (new environment installation), ActiveGates update at the earliest convenience to the latest eligible version.

### Update now to target version

You update an individual ActiveGate manually from its own update settings, not from the environment-wide defaults: open the **ActiveGate updates** settings for that specific ActiveGate. For an ActiveGate set to **No automatic updates** that is on a version older than its configured **target version**, the settings show the version it will update to and provide an **Update now to target version** button. Select the button to trigger the update immediately.

**Update now to target version** is unavailable when the configured target version cannot be resolved (for example, the build is no longer present on the cluster).

### Concurrency and safety

To preserve routing capacity for monitored hosts, Dynatrace throttles concurrent ActiveGate updates within each **pool**. A pool is defined by the combination of network zone, ActiveGate group, and ActiveGate purpose (for example, default routing or synthetic). By default:

* When a pool contains **two or more** ActiveGates, **at most one of them** updates at a time. The remaining ActiveGates wait until the running update finishes (or its tracking window expires).
* When a pool contains **only one** ActiveGate, that ActiveGate updates without waiting—there is nothing to fall back to.
* ActiveGates in **different** pools (for example, different network zones or different groups) can update in parallel because each pool is throttled independently.

Additional safeguards:

* Dynatrace updates only ActiveGates that have auto-update turned on.
* Pre-update checks validate compatibility before Dynatrace applies an update.
* If an update fails, the ActiveGate automatically reverts to the previous working version.
* Success and failure of updates surface via existing Dynatrace alerting channels and the **Deployment Status** > **ActiveGates** [update status](#update-status) values.

### Limitations and scope

* [Containerized ActiveGates](/managed/ingest-from/dynatrace-activegate/activegate-in-container/differences#auto-update "Learn how containerized ActiveGate differs from host-based ActiveGate") don't support update mode, target version, or update windows—the container runtime manages their lifecycle.
* [Cluster ActiveGates](/managed/managed-cluster/operation/update-dynatrace-managed-activegate "Learn about manual and one-click cluster ActiveGate updates.") are updated alongside Dynatrace Managed and don't use these settings.
* Multi-environment ActiveGates follow the configuration of their **primary environment**.

### Programmatic access

* Configure auto-update programmatically via the [ActiveGate auto-update configuration API](/managed/dynatrace-api/environment-api/activegates/auto-update-config "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.").
* The update window schema is defined at [`builtin:deployment.management.update-windows`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-management-update-windows "View builtin:deployment.management.update-windows settings schema table of your monitoring environment via the Dynatrace API.").
* The Environment Deployment API endpoints [download-activegate-latest](/managed/dynatrace-api/environment-api/deployment/activegate/download-activegate-latest "Download the latest ActiveGate installer via Dynatrace API.") (which also covers `…/latest/metainfo`) and [download-activegate-version](/managed/dynatrace-api/environment-api/deployment/activegate/download-activegate-version "Download the ActiveGate installer of the specific version via Dynatrace API.") honor the configured target version.

## Manual download and update

### Manual download and update

You can also download and update your ActiveGate manually. You don't need to uninstall your current version of ActiveGate. Just install the new version over the old one, and the ActiveGate configuration will be migrated.

* [Install an Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate").

During an update, your ActiveGate configuration is preserved in the `custom.properties` and `launcheruserconfig.conf` files. These two files will not be overwritten during an update, but it's good practice to back them up before updating the ActiveGate.

* See [Configure ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") for `custom.properties` file properties.
* See [Configure ActiveGate launcher](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") for `launcheruserconfig.conf` properties.

## Update status

The update status for an ActiveGate, as listed on the **Deployment Status** page, can assume the following values:

**Up to date**  
The latest available ActiveGate version is installed on the respective host.

**Update available**  
There is an update available for this ActiveGate version.

**Update pending**  
Immediately after selecting **Update ActiveGate**, the status changes to **Update pending** and remains in this status until the update process begins.
The status may also be listed as `pending` if:

* The cluster is currently upgrading.
* The maximum number of concurrent update downloads has been reached and the ActiveGate is waiting to resume the download.

**Update in progress**  
The ActiveGate has requested and downloaded the new installation package from the server, and is currently in the process of installing it or re-connecting to the server.

**Update problem**  
In this case you will see the old version number displayed for the ActiveGate.  
Possible problems are:

* ActiveGate downloaded the new installer, but the installation was not attempted or was not performed successfully; consequently ActiveGate is still at the old version.
  Check the ActiveGate auto-updater logs and installer logs for the reason why the installation was not attempted or failed.
* ActiveGate downloaded the new installer but then failed to re-connect to the server (was lost).
  Check the ActiveGate installer logs for the reason why the installation failed.
* There are no installers available for ActiveGate.
* Update is on hold because—on another Environment—there were update problems with the offered version of ActiveGate.

**Unknown**  
The connection to this ActiveGate has been lost and no status can be determined.  
This status can also be displayed if an ActiveGate was successfully removed: In this case, **Deployment Status** will continue to display the uninstalled ActiveGate with update status `Unknown` for seven days.