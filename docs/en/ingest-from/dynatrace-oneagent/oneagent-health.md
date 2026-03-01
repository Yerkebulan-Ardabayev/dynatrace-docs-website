---
title: OneAgent health overview
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-health
scraped: 2026-03-01T21:18:45.003480
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

### Health state examples

The following conditions are applied to your OneAgent modules and result in specific recommendations.

### Limitations

* Only the **Health state** metric includes the z/OS Java module and AWS Lambda, Azure, and Google Cloud integrations.
* Only OneAgent modules seen in the last 5 minutes are shown in the data table.
* Only the data table can be filtered by management zone.