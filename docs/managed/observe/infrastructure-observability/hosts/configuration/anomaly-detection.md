---
title: Host anomaly detection
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/configuration/anomaly-detection
scraped: 2026-05-12T11:38:34.936539
---

# Host anomaly detection

# Host anomaly detection

* How-to guide
* 4-min read
* Updated on Mar 11, 2024

Dynatrace automatically detects infrastructure-related performance anomalies such as high CPU saturation and memory outages.

You can configure host anomaly detection, including problem and event thresholds, to meet your specific needs. For example, if you have a system with:

* Low resource consumption and you want to be alerted immediately in case your system exceeds the thresholds.
* High resource consumption and you don't want to be constantly alerted.

## Access anomaly detection

In Dynatrace, you can configure anomaly detection at multiple levelsâenvironment, host, host group, or for specific disks.

Host level

Host-group level

Environment level

1. Go to **Hosts**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Anomaly detection** > **Infrastructure**.

1. Go to **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Anomaly detection** > **Infrastructure**.

Go to **Settings** > **Anomaly detection** > **Infrastructure** > **Hosts**.

## Set problem-creation thresholds

You can configure the detection sensitivity and enable alerting for your hosts and networks.

### Hosts

1. Go to **Settings** > **Anomaly detection** > **Infrastructure** > **Hosts**.
2. Turn on or off the available options for each setting on the page or select **Use defaults** in the upper-right corner of the page.

   * If you choose **Automatic** from the drop-down menu, the built-in settings will be used.
   * If you choose **Based on custom settings**, configure **Alerting event thresholds** and **Dealerting event thresholds**. For details, refer to [Set event thresholds](#event-thresholds).
3. Select **Save changes**.

### Networks

1. Go to **Settings** > **Anomaly detection** > **Infrastructure** > **Networks**.
2. Turn on or off the available options for each setting on the page or select **Use defaults** in the upper-right corner of the page.

   * If you choose **Automatic** from the drop-down menu, the built-in settings will be used.
   * If you choose **Based on custom settings**, configure **Alerting event thresholds** and **Dealerting event thresholds**. For details, refer to [Set event thresholds](#event-thresholds).
3. Select **Save changes**.

## Set event thresholds

You can set the alerting/dealerting event thresholds for the anomaly detection settings.

### Alerting event thresholds

* **Violating samples**âThe number of violating 10-second samples that raise an alert. The value must be higher than the number of samples.
* **Evaluation window size for violating samples**âThe number of 10-second samples that form the sliding evaluation window to detect violating samples.

Examples

* 1-minute window

  + **Violating samples**: 3
  + **Evaluation window size for violating samples**: 6
* 5-minute window

  + **Violating samples**: 15
  + **Evaluation window size for violating samples**: 30
* 10-minute window

  + **Violating samples**: 30
  + **Evaluation window size for violating samples**: 60

### Dealerting event thresholds

* **Dealerting samples**âThe number of non-violating 10-second samples that deactivate the alert. The value must be lower than the number of samples.
* **Evaluation window size for dealerting samples**âThe number of 10-second samples that form the sliding evaluation window to detect deactivated samples.

The event thresholds are not available for the **Detect host or monitoring connection lost problems** and **Detect high retransmission rate** settings.

Examples

* 1-minute window

  + **Dealerting samples**: 3
  + **Evaluation window size for dealerting samples**: 6
* 5-minute window

  + **Dealerting samples**: 15
  + **Evaluation window size for dealerting samples**: 30
* 10-minute window

  + **Dealerting samples**: 30
  + **Evaluation window size for dealerting samples**: 60

## Set thresholds for specific disks

Server-side disk alerting for new tenants

Starting with SaaS version 1.308, server-side disk alerting is disabled for new tenants by default. We recommend using [Disk Edge alerting](/managed/observe/infrastructure-observability/hosts/configuration/anomaly-detection#disk-edge-alerting "Configure host anomaly detection, including problem and event thresholds.") instead. Disk Edge alerting allows you to create more complex and specific rules using:

* Metrics to alert on (available disk space, is read-only file system, read time, write time, and available inodes)
* Operating system to which the policy should be applied
* Disk name filters
* Host custom metadata conditions
* Custom-defined properties attached to the triggered event

Keep in mind that Disk Edge alerting requires OneAgent version 1.293+.

Davis automatically detects disk anomalies such as low available disk space or slow disks. There are different kinds of disks on a host, such as a boot disk, a disk holding all the logs, or a disk for storing business data. While alerting on low disk space would not make any sense for a fixed-sized boot disk image, it makes perfect sense for a disk containing critical business data.

With custom disk detection rules, you can provide fine-tuned rules for individual groups (groups are based on disk name patterns and/or host tags) of disks. Disk-level thresholds override global thresholds for matching disks, while global settings still apply to other disks.

To change threshold settings for a group of disks

1. Go to **Settings** > **Anomaly detection**.
2. In the **Infrastructure** section, select **Custom disk-detection rules**.
3. Select **Add item**.
4. Select the metric to be monitored and provide a meaningful name for the rule.
5. Specify the threshold for the metric and the number of samples that must violate the threshold to trigger an alert.
6. Optional Specify the name pattern of the disk.

   The individual rules aren't logically bound and are applied separately. For example, if one rule matches all disks not containing `A` and another matches all disks not containing `B`, then every disk will be matched by either the first, the second, or both rules simultaneously. Note that it is also not possible to add multiple values, wildcards, or regular expressions within a single rule filter.
7. Optional To further narrow down the disk usage, list the tags that the host must have.
8. Select **Save changes**.

## Disk Edge alerting

OneAgent version 1.293+

Use **Disk Edge** to set up alerts for automatic detection of performance anomalies related to disk infrastructure.

Disk Edge provides automatic detection of performance anomalies related to disk infrastructure. Use these settings to tailor detection sensitivity to a specific disk's name and/or custom metadata. Defining custom properties can help with the post-processing of the event.

You can define policies on the host, host group, and environment levels.

1. Go to **Settings** > **Anomaly detection** > **Infrastructure** > **Disk Edge**.
2. Select **Add policy**.
3. Define the policy.

   * **Policy name**: The name under which your policy will be listed.
   * **Operating system**: Detection rules can be specified for selected OS systems (if none are selected, settings will not be matched).
   * **Alerts**: One rule can have up to seven alerts, one for each of the event types. See the table below.
   * **Disk name filters**: Rules can be filtered by disk name.
   * **Host custom metadata conditions**: Rules can be filtered by [host custom metadata](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Learn how to tag and set additional properties for a monitored host.").
   * **Properties**: Properties can be added to the sent event using the supported placeholders:

     + `disk.all_mountpoints`
     + `disk.device_name`
     + `disk.mountpoint`
     + `dt.entity_host`
     + `dt.host_group.id`
     + `host.name`

| Event | Severity | Related OneAgent metric |
| --- | --- | --- |
| Available disk space (%) below | Smaller value is more severe | DiskStats object field: `availPercentage`   Mintv2 metric: `dt.host.disk.free`   Timeseries: `builtin:host.disk.free` |
| Available disk space (MiB) below | Smaller value is more severe | DiskStats object field: `avail`   Mintv2 metric: `dt.host.disk.avail`   Timeseries: `builtin:host.disk.avail` |
| Available inodes (%) below | Smaller value is more severe | DiskStats object field: `availINodesPercentag`   Mintv2 metric: `dt.host.disk.inodes_avail`   Timeseries: `builtin:host.disk.inodesAvail` |
| Available inodes (number) below | Smaller value is more severe | Calculated from Diskstats: `totalINodes` \* `availINodesPercentage`   Mintv2 metric: `dt.host.disk.inodes_avail` \* `dt.host.disk.inodes_total`   Timeseries: `builtin:host.disk.inodesTotal` \* `builtin:host.disk.inodesAvail` |
| Is read only file system | N/A | Disk object field: `readOnly`   Mintv2 metric: N/A   Timeseries: N/A |
| Read time (ms) exceeding | Larger value is more severe | Disk object field: `readTime`   Mintv2 metric: `dt.host.disk.read_time`   Timeseries: `builtin:host.disk.readTime` |
| Write time (ms) exceeding | Larger value is more severe | Disk object field: `writeTime`   Mintv2 metric: `dt.host.disk.write_time`   Timeseries: `builtin:host.disk.writeTime` |

## Anomaly detection configuration hierarchy

You can configure anomaly detection rules and policies on multiple levelsâhost, host group, environment.

When you have multiple rules affecting the same entity, the most specific rule prevails over more generic rules.

### Disk rules

Custom rules are evaluated from top to bottom, and the first matching rule applies, so be sure to place your rule in the correct position on the list.

Disk is assigned to the first policy it matches to (based on disk name and/or metadata) according to the policies hierarchy.

### Disk Edge policies

For Disk Edge, the order of policies is also evaluated from the more specific scope (more priority) to a more generic one (less priority).

## Related topics

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.")