---
title: OneAgent health overview
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-health
scraped: 2026-02-21T21:11:12.740868
---

# OneAgent health overview

# OneAgent health overview

* Latest Dynatrace
* 4-min read
* Updated on Jan 15, 2026

The OneAgent health overview empowers you to discover all your deployed [OneAgent modules](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") at scale and detect anomalies before they become problems. With the OneAgent health overview, for example, you can discover:

* Outdated OneAgent modules that require an update to continue full Dynatrace support.
* Connectivity issues between OneAgent modules and your Dynatrace Cluster.
* Incompatible OneAgent modules that require corrective actions.
* Processes that require a restart to continue monitoring.
* OneAgent modules where auto-update is disabled.

## Get started

To get started with the OneAgent health overview, go to **OneAgent Health**.

![OneAgent Health](https://dt-cdn.net/images/oneagent-health-1744-afe02d9e3b.png)

The **OneAgent health overview** comprises

* An area chart focusing on the [Health state metric](#health-state-metric).

  The area chart includes data on OneAgent modules during the selected timeframe. You can split the area chart by health state, monitoring state, module type, module version, process type, and operating system type.
* A data table presenting a variety of attributes of the contributing OneAgent modules.

  The data table contains real-time data of the OneAgent modules seen in your environment in the last 5 minutes. You can filter it by specific attributes. To display additional attributes, select **Configure columns**.

  Above the data table, the lowest and highest compatible OneAgent versions for this Dynatrace cluster are displayed.

  The environment permission [Install OneAgent](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") is required to visualize data in this table.

Select a specific data point in the area chart to see the contributing OneAgent modules in the data table.

## Health state metric

The **Health state** metric (`dsfm:cluster.oneagent.agent_modules`) indicates the health state of your deployed OneAgent modules. It is divided into four classesâCritical, Warning, Info, and Healthy. Each class has different implications.

Health state

Implications

Critical

* A OneAgent module struggles with problems that might result in monitoring outage.
* Corrective action is required.

Warning

* A OneAgent module struggles with anomalies that might impact monitoring availability.
* Corrective action is recommended.

Info

* The health of a OneAgent module could be improved to ensure monitoring availability.
* Corrective action is not necessary.

Healthy

* A OneAgent module is healthy without monitoring disturbances.
* No action is required.

### Health state examples

The following conditions are applied to your OneAgent modules and result in specific recommendations.

Health state

Condition

Recommendation

Critical

Installer version date older than 11 months

Update OneAgent to a newer version to maintain full Dynatrace support.

Critical

Module heartbeat is 180 seconds overdue

Dynatrace hasnât received data from this module for 180 seconds. There might be communication problems, or your process might have exited unexpectedly.

Critical

Host ID conflict

Multiple monitored hosts report that theyâre using the same host identifier. This unexpected situation might be the result of machine cloning. Please contact a Dynatrace product expert via live chat within your environment.

Critical

Host quota exceeded

Monitoring is currently disabled. Please contact a Dynatrace product expert via live chat within your environment.

Critical

Installer version marked as faulty by Dynatrace

Update OneAgent to a newer version. Processes might also need to be restarted.

Critical

Module version marked as faulty by Dynatrace

Update OneAgent to a newer version. A process restart might also be required.

Warning

Installer version is between 9 and 11 months old

Update to a newer OneAgent version to stay current.

Warning

Minimum OneAgent version incompatible

Update OneAgent to a newer version. A process restart might also be required, even if youâve already updated your module.

Warning

Maximum OneAgent version incompatible

Only OneAgent versions that are equal to or lower than the Dynatrace cluster version can be connected. Download a compatible OneAgent version from this cluster.

Info

Process restart needed

Your module version is outdated. Restart your process to update the module to a newer OneAgent version.

Info

Auto-update suppressed

Enable auto-update to stay current.

### Limitations

* Only the **Health state** metric includes the z/OS Java module and AWS Lambda, Azure, and Google Cloud integrations.
* Only OneAgent modules seen in the last 5 minutes are shown in the data table.
* Only the data table can be filtered by management zone.