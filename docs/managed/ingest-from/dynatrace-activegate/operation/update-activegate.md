---
title: Update ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/operation/update-activegate
scraped: 2026-05-12T11:36:40.866676
---

# Update ActiveGate

# Update ActiveGate

* 1-min read
* Published Jul 17, 2018

Limitations

**Auto-update** and **One-click update** functionalities are limited to host-basedâusing installerâdeployment only.

* [Containerized ActiveGate update behavior](/managed/ingest-from/dynatrace-activegate/activegate-in-container/differences#auto-update "Learn how containerized ActiveGate differs from host-based ActiveGate")

To see a list of installed ActiveGates, go to **Deployment Status** > **ActiveGates**. For each ActiveGate, the list gives the current **Version** of the ActiveGate and the **Update status** (up to date, pending, or in progress).

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") The yellow warning icon indicates that your ActiveGate is behind by more than five versions. You should update these ActiveGates as soon as possible.

ActiveGates in containers are deployed and uploaded using cloud-specific tooling. For example, Kubernetes uses [custom resource definitions](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "Monitor the Kubernetes API using Dynatrace").

### Automatic update

To manage the update functionality of a particular ActiveGate in the list, select the ActiveGate to expand the details.

Go to **Settings** to open the **ActiveGate updates** settings for the particular ActiveGate.

* **Auto-update**  
  To use the auto-update feature, make sure that the **Automatic updates at earliest convenience** toggle for the ActiveGate is turned on. This means that when a new version of ActiveGate becomes available, a new installation package will be downloaded to the particular host, and the new version of ActiveGate will be installed. This is the default setting for new environments. For existing environments, the setting remains unchanged.  
  The availability check is performed at 30-minute intervals.
* **One-click update**  
  To perform the update immediately, select **Update**. This functionality is available only if the **Automatic updates at earliest convenience** toggle is turned off for the particular ActiveGate.

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
* Update is on hold becauseâon another Environmentâthere were update problems with the offered version of ActiveGate.

**Unknown**  
The connection to this ActiveGate has been lost and no status can be determined.  
This status can also be displayed if an ActiveGate was successfully removed: In this case, **Deployment Status** will continue to display the uninstalled ActiveGate with update status `Unknown` for seven days.