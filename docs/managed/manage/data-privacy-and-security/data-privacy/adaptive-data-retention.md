---
title: Adaptive Data Retention
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-privacy/adaptive-data-retention
scraped: 2026-05-12T11:08:27.044961
---

# Adaptive Data Retention

# Adaptive Data Retention

* 6-min read
* Updated on Jan 18, 2023

Dynatrace periodically deletes transaction storage, Session Replay storage, and Log monitoring storage data that is older than the configured retention time. Adaptive Data Retention is a functionality according to which Dynatrace periodically increases or decreases the retention time of this data if disk space is insufficient.

Each data type stored on a disk has a default retention time, which specifies how long that data type can be stored on disk.

You can view the current environment storage quotas and retention times specific for your environment at **Cluster Management Console** > **Environments**.

Example CMC 'Environments' page

![Storage settings](https://dt-cdn.net/images/max-user-actions-minute-1752-112909ea0c.png)

Storage settings

The maximum amount of a given data type that can be stored on disk is determined as follows:

* The configured retention time defines how long data of a certain type should be stored on the disk. Older data is periodically deleted.
* The adapted retention time is the configured retention time reduced by a factor calculated when the following conditions apply:

  + The tenant data exceeds its quota
  + Disk space is exceeded

  If neither of these conditions apply, the adapted retention time is equal to the configured retention time.

For example, suppose all of the following statements are true:

* The configured retention time of Session Replay storage data is 10 days
* The environment has exceeded its session storage data quota
* The factor for calculating adapted retention time is 10%

In this case, the adapted retention time would be 9 days for session storage data:  
Real retention time = 10 days Ã ((100 â 10) 100) = 10 Ã 0.9 = 9 days

This would result in all Session Replay storage data older than 9 days being deleted immediately, even though the configured retention time is 10 days.

### How retention time is adapted

Retention time is decreased if:

* The environment uses more disk space than its quota allows
* The disk is full

These conditions are continuously evaluated. If one of these conditions is violated, retention time is decreased and deletion of data older than the adapted retention time begins.

After data is deleted according to the adapted retention time:

* If enough data was deleted and neither of the conditions is currently violated, then the retention time is increased again.
* If at least one of the conditions is still violated, the retention time is further decreased, and more data is deleted.

### How to find out if the retention time is currently adapted

If retention times are currently adapted, you should see a note on the **Cluster Management Console** > **Environments** > **[environment]** page, section **Storage settings**, under the affected data type.

![Truncated transaction storage retention time](https://dt-cdn.net/images/storage-settings-quota-1428-b3d09e1a62.png)

Truncated transaction storage retention time

Additionally, you'll receive a cluster event. For example:

**The node with id 123 is not properly configured**  
The disk volume 'dynatrace-storage' attached to the cluster node 123 is too small to persist the expected amount of data in the cluster. This cluster node will be shut down. Make sure that all cluster nodes have the same partition size for the 'dynatrace-storage'. After the resize operation, restart the cluster node using the 'dynatrace.sh' command. To troubleshoot, visit: [Storage recommendationsï»¿](https://dt-url.net/wa035hb).

### What to do if the retention time is adapted

Adaptation of data retention time can be caused by an undersized disk or an inappropriate quota.

To prevent unwanted adaptation of retention time for data:

* Increase your quota
* Increase your disk size

## FAQ

Adaptive Data Retention is impacted by several factors. Under certain rare circumstances, the adaptation of retention time can lead to excessive data deletion for an environment. As a result, the amount of processed data that is retained and the amount of available storage, which is limited by disk space or quota, are not aligned.

To mitigate this issue:

* Increase the available disk space or quota.
* Decrease the retention time for that environment so that adaptation has less impact.

### How does a decrease in retention time affect retention time adaptation?

Because retention time adaptation is a percentage of your data retention time, a longer data retention time proportionally causes more dataâand therefore more hoursâto be deleted.

### How does adding a new environment affect the existing environments on a cluster running on full disks?

As the new environment takes up disk space, the existing environments' retention times are gradually decreased. After some time, all of the cluster's environments have the same percentage change of their configured data retention times.

### Why is the current retention time lower than the configured retention time even though there seems to be enough free disk space?

Some deviation is expected. When the deviation is too extreme, the required disk space for the configured retention time usually diverges heavily from the available disk space. Try setting the retention times to a more realistic value better suiting the currently available disk space.

### Why was the data retention time reduced more than what CMC shows as the value for the reduction?

The Adaptive Data Retention reduction displayed in Cluster Management Console is only a snapshot of the current situation. After the data is removed from the disk, the reduction is decreased continuously, resulting in this behavior.