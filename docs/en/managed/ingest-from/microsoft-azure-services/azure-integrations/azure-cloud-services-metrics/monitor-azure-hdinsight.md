---
title: Azure HDInsight monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight
scraped: 2026-02-26T21:22:16.715519
---

# Azure HDInsight monitoring

# Azure HDInsight monitoring

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Jan 22, 2026

Dynatrace ingests metrics from Azure Metrics API for Azure HDInsight. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.  
On the Azure HDInsights dashboard, you get holistic insights into your Hadoop, Spark, and Kafka resources and can cover all angles of your big data monitoring in one place.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## Install OneAgent Optional

For additional Hadoop, Spark, and Kafka insights, you can install OneAgent on Azure HDInsight cluster nodes.

How to install OneAgent on Azure HDInsight cluster (Linux)

Follow the steps below to install OneAgent on Azure HDInsight cluster (Linux).

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an install script**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-1 "Monitor Azure HDInsight and view available metrics.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create an HDInsight cluster**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-2 "Monitor Azure HDInsight and view available metrics.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Restart the processes**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-3 "Monitor Azure HDInsight and view available metrics.")

### Step 1 Create an install script

1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Linux**.

3. On the **Install Dynatrace OneAgent on your Linux hosts** page, copy the command below **Use this command on the target host** and the command below **And run the installer with root rights** into a plain text document called `installdynatrace.sh`, and save it to your local machine.

**Example of install script**

```
wget  -O Dynatrace-OneAgent-Linux-1.137.163.sh "https://YOURTENANT.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=YOURAPITOKEN&arch=x86&flavor=default"



/bin/sh Dynatrace-OneAgent-Linux-1.137.163.sh  --set-app-log-content-access=1
```

3. Go to Microsoft Azure Storage Explorer and upload the Dynatrace installation file `installdynatrace.sh` to an accessible Blob Storage Container.
4. Click right on `installdynatrace.sh` and select **Set public access level**. In the pop-up window, set the access level to **Public read access for container and blobs**, and click **Apply**.
5. On the top menu of the Microsoft Azure Storage Explorer window, click on "Copy URL" and save it locally for later access.

### Step 2 Create an HDInsight cluster

1. Login to Microsoft Azure portal and select **HDInsight clusters** on the left-side menu.
2. Select **Create hdinsight cluster**.
3. Select **Custom** installation.
4. Follow the creating wizard to configure basic settings, set storage settings, applications and cluster size.
5. In the **Advanced settings** menu, select **Script Actions**.
6. Select **Submit new**.
7. In the **Submit script action** menu, enter **Custom** for the script type, choose a name, for instance **Install Dynatrace**, and paste the URL of the script you copied previously in the **Bash script URI** field. If you want to install Dynatrace OneAgent on all the nodes, select all node types (**Head**, **Worker**, **Zookeeper**).
8. Select **Create** to save the changes and create the HDInsight cluster.

### Step 3 Restart the processes

Once the installation is completed, make sure to restart the processes.

1. Select your newly created cluster on the MicrosoftAzure portal. On the **Overview** menu, click on your cluster URL.
2. For each node where you chose to install Dynatrace, go to **Service Actions** and select **Restart All**.

As soon as processes are restarted, Dynatrace will start collecting metrics.

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Hdinsights azure](https://dt-cdn.net/images/hdinsights-custom-dashboard-1898-9e1893ad04.png)

### Set up a management zone

To import a dashboard for Azure HDInsight, you need to [set up a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") to limit the entities displayed on the dashboard to cluster nodes only and exclude other hosts not relevant to the service.

When you create a management zone for this dashboard:

1. Create a rule that identifies hosts based on a common property:

   * Host name contains the `hdi` string
2. Create a rule that identifies custom devices based on a common property:

   * Custom device group contains the `HDInsight` string.
3. Create a rule that identifies services based on a common property:

   * Service technology: `Apache Hadoop`
   * Service technology: `Apache Hadoop Distributed File System`
   * Service technology: `Spark`

Example

![Azure management zone](https://dt-cdn.net/images/hdinsightmanagementzone-2629-26e6039169.webp)

After you create the management zone, assign it to your dashboard (from the dashboard, select **Edit** > **Settings** > **Default management zone**). For more information, see [Dashboard timeframe and management zone](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| CategorizedGatewayRequests | Number of gateway requests by categories (1xx/2xx/3xx/4xx/5xx) | HttpStatus | Count |  |
| GatewayRequests | Number of gateway requests | HttpStatus | Count | Applicable |
| NumActiveWorkers | Number of active workers | MetricName | Count | Applicable |