---
title: Adaptive Data Retention
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/adaptive-data-retention
scraped: 2026-03-01T21:28:21.461370
---

# Adaptive Data Retention

# Adaptive Data Retention

* Latest Dynatrace
* 6-min read
* Updated on Jan 18, 2023

Adaptive Data Retention doesn't apply to Grail-enabled deployments.

Dynatrace periodically deletes transaction storage, Session Replay storage, and Log monitoring storage data that is older than the configured retention time. Adaptive Data Retention is a functionality according to which Dynatrace periodically increases or decreases the retention time of this data if the tenant environment storage quota is exceeded.

Each data type stored on a disk has a default retention time, which specifies how long that data type can be stored on disk. See [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.") for more details.

The maximum amount of a given data type that can be stored on disk is determined as follows:

* The configured retention time defines how long data of a certain type should be stored on the disk. Older data is periodically deleted.
* The adapted retention time is the configured retention time reduced by a factor calculated when the tenant data exceeds its quota. If this condition doesn't apply, the adapted retention time is equal to the configured retention time.

For example, suppose all of the following statements are true:

* The configured retention time of Session Replay storage data is 10 days
* The environment has exceeded its session storage data quota
* The factor for calculating adapted retention time is 10%

In this case, the adapted retention time would be 9 days for session storage data:  
Real retention time = 10 days Ã ((100 â 10) 100) = 10 Ã 0.9 = 9 days

This would result in all Session Replay storage data older than 9 days being deleted immediately, even though the configured retention time is 10 days.

### How retention time is adapted

Retention time is decreased if the environment uses more disk space than its quota allows. This condition is continuously evaluated. If it's violated, retention time is decreased and deletion of data older than the adapted retention time begins.

After data is deleted according to the adapted retention time:

* If enough data was deleted and neither of the conditions is currently violated, then the retention time is increased again.
* If at least one of the conditions is still violated, the retention time is further decreased, and more data is deleted.

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