---
title: Adjust the sensitivity of anomaly detection for infrastructure
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure
scraped: 2026-02-26T21:19:58.136873
---

# Adjust the sensitivity of anomaly detection for infrastructure

# Adjust the sensitivity of anomaly detection for infrastructure

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jan 28, 2026

Dynatrace detects multiple infrastructure-related performance anomalies that might lead to problems with your infrastructure (the particular list depends on the type of your infrastructure). Each anomaly type is detected independently and triggers related problems and alerts.

To adjust the global configuration of anomaly detection for infrastructure

1. Go to **Settings** > **Anomaly detection**.
2. In the **Infrastructure** section, select the infrastructure type for which you want to configure anomaly detection.

Anomaly detection can be configured for all hosts monitored by Dynatrace regardless of their type (physical or virtual). Dynatrace also detects network and disk problems of your hosts.

For each anomaly type, you can either select automatic detection to rely on Dynatrace Intelligence to alert you about problems, or you can provide a fixed threshold. Just select the required option from the respective list.

By default, Dynatrace alerts only about unexpected outages.

* During a graceful shutdown, the host outage is expected and the operating system has sent a shutdown signal notifying OneAgent that an operator is intentionally shutting down the host.
* If OneAgent receives no shutdown signal, the shutdown is classified as unexpected.

You can opt-in to receive notifications about graceful shutdowns as well.

## Thresholds for specific disks

Server-side disk alerting for new tenants

Starting with SaaS version 1.308, server-side disk alerting is disabled for new tenants by default. We recommend using [Disk Edge alerting](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection#disk-edge-alerting "Configure host anomaly detection, including problem and event thresholds.") instead. Disk Edge alerting allows you to create more complex and specific rules using:

* Metrics to alert on (available disk space, is read-only file system, read time, write time, and available inodes)
* Operating system to which the policy should be applied
* Disk name filters
* Host custom metadata conditions
* Custom-defined properties attached to the triggered event

Keep in mind that Disk Edge alerting requires OneAgent version 1.293+.

Dynatrace Intelligence automatically detects disk anomalies such as low available disk space or slow disks. There are different kinds of disks on a host, such as a boot disk, a disk holding all the logs, or a disk for storing business data. While alerting on low disk space would not make any sense for a fixed-sized boot disk image, it makes perfect sense for a disk containing critical business data.

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

### Anomaly detection configuration hierarchy

You can configure anomaly detection on multiple levelsâenvironment, host group, host, and so on. When you have multiple rules affecting the same entity, the most specific rule prevails over more generic rules, as described on the diagram below.

![Disk alerting override scheme](https://dt-cdn.net/images/disk-alerting-override-scheme-1500-928615f8bc.png)

## Thresholds for a specific host group

To configure the disk rules for a specific host group

1. Go to **Deployment Status**.
2. Filter the table by **Host group** and select the name of the host group for which you want to configure custom disk-detection rules.
3. For one of the listed hosts, select the host group.
4. Expand **Anomaly detection** and select **Custom disk-detection rules**.
5. Select **Add item**.
6. Select the metric to be monitored and provide a meaningful name for the rule.
7. Specify the threshold for the metric and the number of samples that must violate the threshold to trigger an alert.
8. Optional Specify the name pattern of the disk.
9. Optional To further narrow down the disk usage, list the tags that the host must have.
10. Select **Save changes**.

## Thresholds for a specific host

As an alternative to defining thresholds globally across your entire environment, you can provide fine-tuned thresholds for individual hosts. Host-level thresholds override global thresholds for the host, while global settings still apply to other hosts. You can revert to globally defined thresholds at any time.

To change threshold settings for a specific host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Select the host you want to configure.
3. In the upper-right corner of the page, select **More** (**â¦**) > **Settings**.
4. Go to **Anomaly detection** > **Infrastructure** to customize the configuration.

## Related topics

* [Host anomaly detection](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.")
* [Anomaly detection API - Hosts](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts "Learn what the Dynatrace Anomaly detection API for hosts offers.")
* [Anomaly detection API - AWS](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws "Learn what the Dynatrace Anomaly detection API for AWS offers.")
* [Anomaly detection API - VMware](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware "Learn what the Dynatrace Anomaly detection API for VMware offers.")
* [Anomaly detection API - Disk events](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events "Learn what the Dynatrace Anomaly detection API for disk events offers.")