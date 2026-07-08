---
title: Adaptive data retention
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-privacy/adaptive-data-retention
---

# Adaptive data retention

# Adaptive data retention

* Explanation
* 4-min read
* Updated on Jun 16, 2026

Dynatrace Managed periodically deletes transaction storage, Session Replay storage, and Log Monitoring data older than the configured retention time. Adaptive data retention periodically increases or decreases the retention time of this data when disk space is insufficient.

## Overview

Each data category on a disk has a default retention time, which specifies the maximum duration for which Dynatrace Managed retains that category.

To check the current environment storage quotas and retention times specific to your environment, go to **Cluster Management Console (CMC)** > **Environments**.

![Storage settings on the Cluster Management Console Environments page](https://dt-cdn.net/images/max-user-actions-minute-1752-112909ea0c.png)

Storage settings on the Cluster Management Console Environments page

### Retention time calculation

Dynatrace determines the maximum amount of a given data category to retain on disk, as follows:

* The configured retention time defines how long data of a certain category remains on the disk. Older data is periodically deleted.
* The adapted retention time is the configured retention time reduced by a factor calculated when the following conditions apply:

  + The environment data exceeds its quota.
  + Disk space is exceeded.

  If neither of these conditions applies, the adapted retention time is equal to the configured retention time.

For example, suppose all the following statements are true:

* The configured retention time of Session Replay storage data is 10 days.
* The environment has exceeded its session storage data quota.
* The factor for calculating adapted retention time is 10 percent.

In this case, the adapted retention time would be 9 days for session storage data:

```
Real retention time = 10 days x ((100 - 10) / 100) = 10 x 0.9 = 9 days
```

The adapted retention time would result in all Session Replay storage data older than 9 days being deleted immediately, even though the configured retention time is 10 days.

### Retention time adaptation

Dynatrace decreases retention time if:

* The environment uses more disk space than its quota allows.
* The disk is full.

These conditions are continuously evaluated. If one of these conditions is violated, Dynatrace decreases retention time and begins deleting data older than the adapted retention time.

After data is deleted according to the adapted retention time:

* If enough data was deleted and neither condition is currently violated, Dynatrace increases retention time again.
* If at least one condition is still violated, the retention time is further decreased, and more data is deleted.

### Adaptation status

If retention times are currently adapted, a note appears on the **CMC** > **Environments** > **[environment]** page, in the **Storage settings** section, under the affected data category.

![Truncated transaction storage retention time](https://dt-cdn.net/images/storage-settings-quota-1428-b3d09e1a62.png)

Truncated transaction storage retention time

Additionally, Dynatrace generates a Managed Cluster event. For example:

**The node with id 123 isn't configured correctly**
The disk volume `dynatrace-storage` attached to the Managed Cluster node 123 is too small to persist the expected amount of data in the Managed Cluster. Dynatrace shuts down this Managed Cluster node. All Managed Cluster nodes must have the same partition size for `dynatrace-storage`. After the resize operation, restart the node using the `dynatrace.sh` command. To troubleshoot, visit [Storage recommendations﻿](https://dt-url.net/wa035hb).

### Response to adaptation

An undersized disk or an inappropriate quota can cause retention time adaptation.

To prevent unwanted adaptation of retention time for data, increase the quota for the affected environment or increase the disk size.

## Frequently asked questions

What factors impact adaptive data retention?

Several factors impact adaptive data retention. Under certain rare circumstances, the adaptation of retention time can lead to excessive data deletion for an environment. As a result, the amount of processed data retained and the amount of available storage, which is limited by disk space or quota, aren't aligned.

To mitigate this issue:

* Increase the available disk space or quota.
* Decrease the retention time for that environment so that adaptation has less impact.

How does decreased retention time affect retention time adaptation?

Because retention time adaptation is a percentage of your data retention time, a longer data retention time proportionally causes more data, and therefore more hours, to be deleted.

How does adding a new environment affect a Managed Cluster running on full disks?

As the new environment takes up disk space, the existing environments' retention times are gradually decreased. After some time, all the Managed Cluster's environments have the same percentage change of their configured data retention times.

Why is current retention time lower than configured despite available disk space?

Some deviation is expected. When the deviation is too extreme, the required disk space for the configured retention time usually diverges from the available disk space. Try setting the retention times to a more realistic value that better suits the currently available disk space.

Why was data retention time reduced more than what Cluster Management Console shows?

The adaptive data retention reduction displayed in CMC is only a snapshot of the current situation. After the data is removed from the disk, the reduction is decreased continuously, resulting in this behavior.

## Related topics

* [Data retention periods](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.")
* [Hardware requirements](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.")