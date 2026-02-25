---
title: Host-level settings
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/configuration
scraped: 2026-02-25T21:15:58.339608
---

# Host-level settings

# Host-level settings

* How-to guide
* 2-min read
* Updated on Mar 28, 2024

In many cases, you can configure monitoring settings at the environment, host group, or host level.

* Settings at the host level override settings at the host group and environment levels.
* Settings at the host group level override settings at the environment level.

To configure settings at the host level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

From here, select items in the left panel to navigate through the host-level settings pages. In this example, you would display the **General** settings page for HOST-001.

![General section in the host settings](https://dt-cdn.net/images/select-host-settings-286-abb08ad1d1.png)

Hierarchy navigation

Changes to settings at the host level override settings at the host group and environment levels.

* If no settings have been changed at the host level, a message box offers a link up from the host-level settings to the equivalent settings on the host group level. If no settings are configured for the host group either, a similar message box offers a link up from the host group settings to the environment settings.
* If host-level settings have been changed, a message box states that "These settings are overriding [host group name] (Host group) settings." You can select the host group name to go to those settings or select **Remove override** if you want to remove the host-level settings and use the host group settings.

## General

The **General** page of **Host settings** displays a table of monitored technologies.

1. On the host-level **Host settings** page, select **General**.

   The **Monitored technologies** table lists monitoring technologies on the selected host:

   * **Technology**âthe name of the technology
   * **Type**âthe type of monitoring, such as `JMX monitoring`, `OneAgent extension`, `Custom extension`, and `Service insights`
   * **Configuration**âthe current configuration level for the selected host.
   * **Monitoring**âthe monitoring state of this technology on the selected host.
2. Select in the **Edit** column to see configuration options:

   * **Use host configuration** determines whether to use host-level monitoring settings, overriding the equivalent environment and host group settings.
   * When you turn on **Use host configuration**, technology-specific settings become available.

To manage host monitoring settings, go to [Host monitoring](#host-monitoring).

## Host monitoring

OneAgent automatically monitors a host and its processes, services, and applications, but you can turn off monitoring, full-stack monitoring, or auto-injection at the host level.

1. On the **Host settings** page, select **Host monitoring**.
   There are three tabs on this page:

   * **Monitoring**
   * **Monitoring Mode**
   * **Advanced Settings**
2. Go to **Monitoring** and set **Monitor this host** to turn monitoring on or off for the selected host.
3. Go to **Monitoring Mode** and set **Full-Stack**, **Infrastructure**, or **Discovery** to turn the selected monitoring mode on or off for the selected host.

   * For details, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").
   * The OneAgent's monitoring mode will automatically overwrite this setting whenever it is changed with oneagentctl or the OneAgent comes online.
4. Go to **Advanced settings** and set **ProcessAgent injection** or **CodeModule injection** to turn the automatic injection on or off for the selected host.
5. Select **Save changes**.

## Container technologies

Dynatrace OneAgent automatically monitors all processes that are running on your monitored hosts. Within container environments (for example, Kubernetes, OpenShift, Cloud Foundry, or Docker), OneAgent automatically injects code modules into containerized processes to provide out-of-the-box full-stack visibility into applications running within containers.

1. On the **Host settings** page, select **Container technologies**.
2. For each container type, turn **Enabled** on or off to determine whether code modules are automatically injected.

   * If turned on, auto-injection provides deep monitoring for all processes within containers, at both the request- and distributed trace levels, for the selected host.
   * If turned off, OneAgent will not inject into a container of the selected type on the selected host.

## Disk options

OneAgent automatically detects and monitors all your mount points, but you can create exception rules to remove certain disks from the monitoring list.

1. On the **Host settings** page, select **Disk options**.
2. Set host-specific disk options as needed.

   * **Show all NFS disks** Linux

     When disabled, OneAgent attempts to deduplicate NFS disks. Disabled by default.
   * **Exclude disks**

     You can create exception rules to remove disks from monitoring.

     For details, see [Exclude disks and network traffic from host monitoring](/docs/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic#disk-options "Learn how to exclude selected disks and network traffic from host monitoring.").

## Disk Analytics Extension

Linux

Install the Disk Analytics extension to gain more detailed visibility into local data stores and their volumes, partitions, and raid instances on Linux hosts.

1. On the **Host settings** page, select **Disk Analytics Extension**.
2. Turn **Enable Disk Analytics data collection** on or off to determine whether Disk Analytics data is collected on the selected host.

   If you enable data collection without adding the extension, the data is visible only in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

For details on installing and using the Disk Analytics extension, see [Disk Analytics extension](/docs/observe/infrastructure-observability/extensions/disk-analytics "Gain detailed visibility into Linux host local datastores where OneAgent is installed.").

## NetTracer traffic

Linux

NetTracer is an open-source tool for tracing TCP events and collecting network connection metrics on Linux.

1. On the **Host settings** page, select **NetTracer traffic**.
2. Turn **Enable NetTracer traffic network monitoring** on or off to determine whether NetTracer monitors network traffic on the selected host.
3. Select **Save changes**.

For details, see [Extended network monitoring](/docs/observe/infrastructure-observability/networks/network-monitoring-with-nettracer "Extend network monitoring with network traffic metrics in containerized Linux hosts using NetTracer.").

## Exclude network traffic

OneAgent automatically detects and monitors all of your network traffic, but you can exclude traffic on specific network interfaces or hosts from monitoring.

1. On the **Host settings** page, select **Exclude network traffic**.

   There are two sections on this page:

   * **Exclude NIC**âThis section lists all network interfaces excluded from network traffic monitoring on a particular interface.

     + To add an entry, select **Add item**
     + To delete an entry, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") **Delete row**
     + To edit an entry, expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") **Details**
   * **Exclude IP**âThis section lists all host IP addresses to exclude when calculating connectivity (other metrics will still be calculated).

     + To add an entry, select **Add item**
     + To delete an entry, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") **Delete row**
     + To edit an entry, expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") **Details**
2. Select **Save changes**.

For details, see [Exclude disks and network traffic from host monitoring](/docs/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic#exclude-network-traffic "Learn how to exclude selected disks and network traffic from host monitoring.").

## Detected processes

The **Detected processes** page is a read-only table of processes detected on the selected host.

* To manage your process monitoring settings, select the **Process group monitoring** link.
* To enable or disable deep monitoring for certain process groups on the host, select the **Process group deep monitoring** link.

For details, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Process group monitoring



To enable or disable deep monitoring for a certain process group on a host

1. On the **Host settings** page, select **Process group monitoring**.

   The table lists process groups that have host-specific monitoring settings.

   * To add an entry, select **Add process group**, select a **Process group**, and set **Monitoring state** for the selected processing group.
   * To delete an entry, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") **Delete row**
   * To edit an entry, expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") **Details** and change the settings.
2. Select **Save changes**.

For details, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Process group detection flags

The **Built-in detection rules** page lists process group detection flag settings for the selected host.

To enable or disable process group detection flags

1. On the **Host settings** page, select **Process group detection flags**.

   If no host-level settings are configured, a message box offers a link to the equivalent settings on the host group level and, from there, up to the environment level.
2. Turn detection rules on or off as needed to set host-specific process group detection flags.

   Hover over the information icon for a rule to view rule details.
3. Select **Save changes**.

For details, see [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").

## Declarative process grouping

Dynatrace automatically monitors process groups that are of known technology types or that consume significant resources. With declarative process grouping, you can automatically monitor additional technologies.

The **Declarative process grouping** page lists all process groups defined through declarative process grouping.

To add a declarative process group to the table

1. On the **Host settings** page, select **Declarative process grouping**.
2. Select **Add process group**.
3. Enter a name, identifier, and reporting setting.
4. Select **Add detection rule** to describe how to detect the process group: property and condition. See the on-screen instructions for help with conditions.
5. Select **Save changes**.

For details, see [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection#declare "Ways to customize process-group detection").

## Process availability

Use **Process availability** to monitor if at least one process matching the specified monitoring rule exists on your host. If no process running on your host matches the rule, you receive an alert. If you also enable [process instance snapshots](#process-instance-snapshots), you receive a detailed report on the activity of the most resource-consuming processes, as well as on the latest activity of the processes matching the rule.

To add a process monitoring rule

1. On the **Host settings** page, select **Process availability**.
2. Select **Add monitoring rule**.
3. Enter a rule name.
4. Select **Add detection rule** to describe how to detect the process: property and condition. See the on-screen instructions for help with conditions.
5. Select **Add property** to define additional key-value properties to be attached to the triggered event.
6. Select **Save changes**.

For details, see [Process availability](/docs/observe/infrastructure-observability/hosts/monitoring/process-availability "Monitor availability and performance of the key processes on your hosts.").

## Process instance snapshots

If you enable process instance snapshots, Dynatrace examines the most resource-consuming processes running on your host and the processes monitored by [Process availability](#process-availability). When a triggering event occurs, metrics reported 10 minutes before and 10 minutes after the event for those processes are sent to the cluster.

To turn on process instance snapshots

1. On the **Host settings** page, select **Process instance snapshots**.
2. Turn on **Enable Process instance snapshots**.
3. Set **Reported processes limit** to the maximum number of processes that the host will report.
4. Select **Save changes**.

## Business Observability

OneAgent can capture business events from incoming HTTP requests based on capture rules that tell OneAgent to capture business events when specific web services or endpoints are called.

* A capture rule consists of trigger rules, mandatory business event information (for example, type and provider), and optional event data fields.
* A trigger defines the criteria that, when met, cause a business event to be captured (for example, endpoint â/api/buyâ is called).

To configure a capture rule on the host level

1. On the **Host settings** page, select **Business Observability** > **OneAgent**.
2. Select **Add new capture rule**.
3. Define a rule. For details, see [Business event capture](/docs/observe/business-observability/bo-events-capturing "Capture business events for Dynatrace Business Observability.").
4. Select **Save changes**.

For details, see [Business event capture](/docs/observe/business-observability/bo-events-capturing#report-business-event-oneagent "Capture business events for Dynatrace Business Observability.").

## Anomaly detection

Use the host-level anomaly detection pages to configure detection sensitivity, set alert thresholds, or disable alerting for the selected host.

To configure anomaly detection for the host

1. On the **Host settings** page, select **Anomaly detection** > **Infrastructure**.
2. Adjust the host-specific thresholds as needed.
3. Select **Save changes**.

To configure anomaly detection for host disks

1. On the **Host settings** page, select **Anomaly detection** > **Disks**.
2. Adjust the host-specific thresholds as needed.
3. Select **Save changes**.

For details, see [Adjust the sensitivity of anomaly detection for infrastructure](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.").

## OneAgent updates

Use **OneAgent updates** to configure the selected host's OneAgent update behavior.

* Automatic updates at earliest convenience
* Automatic updates during update windows
* No automatic updates

Manually triggered environment updates override individual host update settings. To learn more about environment updates, see [One Agent Updates](/docs/ingest-from/dynatrace-oneagent/oneagent-update#oneagent-environment-settings "Learn how to update OneAgent.").

To set automatic OneAgent update behavior on the selected host

1. On the **Host settings** page, select **OneAgent updates**.
2. Set **Update mode**.
3. Select **Save changes**.

To manually update OneAgent on the selected host

1. Set **Update OneAgent to a specific version** to the OneAgent version you want to put on the selected host.
2. Select **Update now**.

## OS services monitoring

Use **OS services monitoring** to set up alerts for OS services in undesirable states.

1. On the **Host settings** page, select **OS services monitoring**.
2. Select **Add policy**.
3. Set **System** (Linux or Windows).
4. Set **Rule name**.
5. Define the alerting conditions.
6. Select **Save changes**.

For details, see [OS services monitoring](/docs/observe/infrastructure-observability/hosts/monitoring/os-services "Improve the visibility of your infrastructure by monitoring the availability of operating system services.").

## Extension Execution Controller

Use **Extension Execution Controller** to configure the Extension Execution Controller (EEC) for OneAgent deployment.

1. On the **Host settings** page, select **Extension Execution Controller**.
2. Configure EEC settings:

   * Set **Enable Extension Execution Controller**.
   * Set **Enable local HTTP Metric, Log and Event Ingest API**.
   * Set **Enable Dynatrace StatsD**.
   * Set **Performance profile**. For details, see [Performance profile - resource consumption](#resource-consumption).
3. Select **Save changes**.

For EEC details, see [About Extensions](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").

## Log Monitoring

Use the **Log Monitoring** page to configure host-specific settings for log monitoring.

1. On the **Host settings** page, select **Log Monitoring**.
2. Open the configuration page for the settings you want to configure on this host.

   * OneAgent configuration

* Custom log source configurationâfor details, see [Custom log source](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source "Configure custom log sources to manually add log data sources that have not been autodetected.")
* Log storage configurationâfor details, see [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.")
* Sensitive data maskingâfor details, see [Sensitive data masking in OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.")
* Timestamp configurationâfor details, see [Timestamp/splitting configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.")
* Select **Save changes**.

## Crash dump analytics



Use **Crash dump analytics** to manage the automatic detection of application crashes.

1. On the **Host settings** page, select **Crash dump analytics**.
2. Turn on/off **Crash dump analytics** to determine whether Dynatrace automatically detects application crashes on the selected host.
3. Select **Save changes**.

For details on Linux and Windows core crash dumps, see [Crash analysis](/docs/observe/application-observability/profiling-and-optimization/crash-analysis "Learn how Dynatrace can help you gain insight into process crashes.").