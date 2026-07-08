---
title: Azure Kubernetes Service (AKS) monitoring
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-aks/monitor-azure-kubernetes-service
---

# Azure Kubernetes Service (AKS) monitoring

# Azure Kubernetes Service (AKS) monitoring

* How-to guide
* 1-min read
* Published Aug 19, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Azure Kubernetes Service. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.200+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to **Technologies & Processes**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**…**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**…**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![AKS dash](https://dt-cdn.net/images/dashboard-35-2560-d7064f1619.png)

AKS dash

The **STANDARD** namespace has only four metrics. All `Nodes` metrics are inside the **CUSTOM** namespace, while the `Node disk capacity` and `IO` metrics are in the **CUSTOM (LOG-BASED)** namespace.

## Available metrics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| node\_cpu\_usage\_percentage |  | Percent | Name of the node, Name of the nodepool | Applicable |
| node\_memory\_working\_set\_bytes |  | Byte | Name of the node, Name of the nodepool | Applicable |
| node\_memory\_working\_set\_percentage |  | Percent | Name of the node, Name of the nodepool | Applicable |
| kube\_node\_status\_allocatable\_cpu\_cores | Total number of available CPU cores in a managed cluster | Count |  | Applicable |
| kube\_node\_status\_allocatable\_memory\_bytes | Total amount of available memory in a managed cluster | Byte |  | Applicable |
| kube\_node\_status\_condition | Statuses for various node conditions | Count | condition, status, node | Applicable |
| kube\_pod\_status\_phase | Number of pods by phase | Count | phase, namespace, pod | Applicable |
| kube\_pod\_status\_ready | Number of pods in Ready state | Count | namespace, pod | Applicable |