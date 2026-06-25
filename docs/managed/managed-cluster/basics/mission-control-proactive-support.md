---
title: Mission Control proactive support
source: https://docs.dynatrace.com/managed/managed-cluster/basics/mission-control-proactive-support
scraped: 2026-05-12T11:08:25.759496
---

# Mission Control proactive support

# Mission Control proactive support

* Explanation
* 3-min read
* Updated on May 08, 2026

Dynatrace Managed is proactively monitored and managed remotely by the Dynatrace Mission Control team to ensure your Managed Cluster remains secure, reliable, and up-to-date. Once you've granted the required permissions, the Mission Control team can remotely access your Managed Cluster to assist with updates and troubleshooting. You have full control over the data privacy settings.

For details, see [Dynatrace Managed Mission Control and Service Level Agreementï»¿](https://www.dynatrace.com/company/trust-center/sla/managed/?_ga=2.93129118.22206741.1563254436-509254238.1563254436).

## How Mission Control works

The Managed Cluster automatically sends [self-monitoring and license data](/managed/managed-cluster/basics/mission-control-data-exchange "Review the data your Managed Cluster exchanges with Mission Control and the available opt-out options for each data category.") to Mission Control. Based on this data, the Mission Control team can proactively analyze and detect misconfigurations or potential incompatibilities with your Managed installation. The Mission Control team never has access to your operating system or file system that's not related to the Managed installation.

Given appropriate permissions, the Mission Control team can monitor the service quality and hardware utilization of your Managed installation and notify you if additional resources are needed. The Mission Control team can also tune the configuration of your Managed installation to ensure highest service quality and best utilization of the provisioned hardware. All configuration changes are fully audit-logged, and you have full control over the [data privacy settings](/managed/managed-cluster/configuration/configure-cluster-preferences "Configure cluster preferences and privacy settings").

Mission Control provides software updates for the Managed Cluster. These software updates are mandatory and are typically released every four weeks. You can adjust the [timing of updates](/managed/managed-cluster/operation/update-cluster "Learn how to update a Managed cluster and how to schedule an automatic update.") to suit your needs.

## What happens if the connection to Mission Control is lost

To keep your Managed installation proactively supported, you need a constant connection to Mission Control. If the connection is interrupted, critical communication requests (such as billing requests or license checks) will be automatically resent once the connection is restored.

The behavior of the Managed Cluster during a connection outage depends on the license model.

| License model | Cluster behavior in case of a connection outage |
| --- | --- |
| [Classic licensing](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.") | If a connection outage to Mission Control lasts longer than 14 days (7 days for free trial accounts), the Managed Cluster disallows the ability to exceed the license limit (overages). However, monitoring of your applications within the licensed quotas isn't affected by a connection outage.  For example: If you have purchased a license for 10 hosts and overages for 2 more hosts, you can monitor 10 hosts for as long as the license is valid. Only the overages are no longer permitted. |
| [Dynatrace Platform Subscription](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") | If the connection to Mission Control is lost, the Managed Cluster collects usage data and sends it to Mission Control as soon as the connection is restored. Monitoring of your applications isn't affected by a connection outage. |

## Related topics

* [Mission Control data exchange](/managed/managed-cluster/basics/mission-control-data-exchange "Review the data your Managed Cluster exchanges with Mission Control and the available opt-out options for each data category.")