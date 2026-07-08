---
title: Track license usage
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/track-license-usage
---

# Track license usage

# Track license usage

* Explanation
* 3-min read
* Updated on May 15, 2026

You can track the license usage of your host units, Davis data units, and Digital Experience Monitoring units under classic licensing in two ways:

* Via the **Cluster Management Console**
* In the **Local-Self-Monitoring** environment

## Cluster Management Console

To track license usage of a Managed Cluster, log in to the **Cluster Management Console** and select **Licensing** in the menu.

The **Licensing** page displays license metadata, the quota per license unit, and current consumption. You can also see whether the overage quota applies and how much of it your Managed Cluster has consumed.

All data displayed here is also available via the [Cluster API v2 - Cluster License](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-license/get-cluster-license-usage "Use the API to get cluster license details and billed usage.").

![Cluster Management Console licensing page](https://dt-cdn.net/images/cmc-licensing-1990-836a6a9a72.png)

Cluster Management Console licensing page

## Local-Self-Monitoring environment

Dynatrace Managed version 1.330+

To track license usage of a Managed Cluster, go to the [**Local-Self-Monitoring**](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn about the local self-monitoring environment that collects internal Dynatrace Managed Cluster health metrics and stores all data exclusively on-premises.") environment and select **Dashboards** > **Cluster license usage**.

The **Cluster license usage** dashboard displays several charts for each license unit, illustrating its quota and the percentage consumed. You can also see whether the overage quota applies and how much of it your Managed Cluster has consumed.

![Cluster license usage dashboard](https://dt-cdn.net/images/managed330-cluster-license-usage-2335-1d3ae4be6a.png)

Cluster license usage dashboard

### Billing metrics

Each chart uses self-monitoring billing metrics. Six billing metrics are available per license unit. Use metric events to generate alerts for license events—for example, when units are about to run out.

#### Host units

The following self-monitoring billing metrics are available.

| Metric name | Metric key |
| --- | --- |
| Cluster - Billing - Hostunit - Quota | `isfm:cluster.billing.hostunit.quota` |
| Cluster - Billing - Hostunit - Quota - Used | `isfm:cluster.billing.hostunit.quota.used` |
| Cluster - Billing - Hostunit - Quota - Used Percent | `isfm:cluster.billing.hostunit.quota.used_percent` |
| Cluster - Billing - Hostunit - Overage - Hours - Quota | `isfm:cluster.billing.hostunit.overage.hours.quota` |
| Cluster - Billing - Hostunit - Overage - Hours - Quota - Used | `isfm:cluster.billing.hostunit.overage.hours.quota.used` |
| Cluster - Billing - Hostunit - Overage - Hours - Quota - Used Percent | `isfm:cluster.billing.hostunit.overage.hours.quota.used_percent` |

#### Davis data units

The following self-monitoring billing metrics are available.

| Metric name | Metric key |
| --- | --- |
| Cluster - Billing - Ddu - Quota | `isfm:cluster.billing.ddu.quota` |
| Cluster - Billing - Ddu - Quota - Used | `isfm:cluster.billing.ddu.quota.used` |
| Cluster - Billing - Ddu - Quota - Used Percent | `isfm:cluster.billing.ddu.quota.used_percent` |
| Cluster - Billing - Ddu - Overage - Quota | `isfm:cluster.billing.ddu.overage.quota` |
| Cluster - Billing - Ddu - Overage - Quota - Used | `isfm:cluster.billing.ddu.overage.quota.used` |
| Cluster - Billing - Ddu - Overage - Quota - Used Percent | `isfm:cluster.billing.ddu.overage.quota.used_percent` |

#### Digital Experience Monitoring units

The following self-monitoring billing metrics are available.

| Metric name | Metric key |
| --- | --- |
| Cluster - Billing - Dem - Quota | `isfm:cluster.billing.dem.quota` |
| Cluster - Billing - Dem - Quota - Used | `isfm:cluster.billing.dem.quota.used` |
| Cluster - Billing - Dem - Quota - Used Percent | `isfm:cluster.billing.dem.quota.used_percent` |
| Cluster - Billing - Dem - Overage - Quota | `isfm:cluster.billing.dem.overage.quota` |
| Cluster - Billing - Dem - Overage - Quota - Used | `isfm:cluster.billing.dem.overage.quota.used` |
| Cluster - Billing - Dem - Overage - Quota - Used Percent | `isfm:cluster.billing.dem.overage.quota.used_percent` |

### License events

To set up a license event (for example, when your Managed Cluster consumes 80% of the Davis data units):

1. Go to the **Local-Self-Monitoring** environment and select **Settings** > **Anomaly detection** > **Metric events**.
2. Select **Add metric event**.
3. Define the **Query definition** properties:

   * Query type: **Metric selector**
   * Metric selector: Metric key with `max` and `rollup` transformations. For example:

     `isfm:cluster.billing.ddu.quota.used_percent:max:rollup(max,10m)`
4. Define the **Monitoring strategy** properties:

   * Model type: **Static threshold**
   * Threshold: `80`
   * Threshold input unit: **percent**
   * Alert condition: **Alert if metric is above**
5. Define the **Advanced model** properties:

   * Violating samples: `3`
   * Sliding window: `5`
   * Dealerting samples: `5`
6. Test the configuration using **Alert preview**.
7. Define the **Event template** and set event type to **Error**.
8. Select **Save changes**.

When your Managed Cluster exceeds 80% of the Davis data units, Dynatrace opens a problem. Under **Problems** you'll find, for example, an alert like this:

![80% of Davis data units used](https://dt-cdn.net/images/license-problem-80percent-1398-0b3f1b9fe2.png)

80% of Davis data units used