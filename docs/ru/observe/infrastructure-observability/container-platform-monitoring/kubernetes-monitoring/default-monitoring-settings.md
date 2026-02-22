---
title: Global default monitoring settings for Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/default-monitoring-settings
scraped: 2026-02-22T21:15:05.854026
---

# Global default monitoring settings for Kubernetes/OpenShift

# Global default monitoring settings for Kubernetes/OpenShift

* 2-min read
* Updated on Jun 15, 2023

Dynatrace version 1.270+

You can configure default monitoring settings for Kubernetes/OpenShift clusters. These default values are used for all new clusters unless monitoring settings are specified during their creation.

## Configuration via web UI

The monitoring settings can be configured either per cluster or for the whole environment.

### Configure environment-level settings

To configure the default settings for the whole environment

1. Go to **Settings** and select **Cloud and virtualization** > **Kubernetes**.
2. On the **Monitoring settings** page, change settings as needed.
3. Select **Save changes**.

![Kubernetes monitoring settings on tenant](https://dt-cdn.net/images/tenant-monitoring-settings-1425-ab644e8cd0.png)

These environment-level settings will be used as default values for all clusters that do not explicitly override them.

### List overriding clusters

To see which clusters are currently overriding these settings

1. On the environment-level **Monitoring settings** page, select **More** (**â¦**) > **Hierarchy and overrides** in the upper-right corner.
2. Review the **Hierarchy and overrides** table.

For details on the settings hierarchy, see [Settings documentation](/docs/manage/settings/settings-20#scope-and-hierarchy-of-settings "Introduction to the Settings 2.0 framework").

![Kubernetes monitoring settings overrides](https://dt-cdn.net/images/tenant-monitoring-settings-overrides-2058-db713cf077.png)

### Remove cluster-level overrides

If you want to remove an override from a specific cluster

1. In the **Hierarchy and overrides** table, select the name of the cluster.

   This opens the **Monitoring settings** page for the selected cluster. The message "These settings are overriding Environment settings" is displayed.
2. In the message box, select **Remove override**. If no override is set, the values set on the environment will be used.

![Kubernetes monitoring settings on cluster](https://dt-cdn.net/images/cluster-monitoring-settings-override-929-a45970ae1e.png)

## Configuration via API

You can also configure monitoring settings via the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") using the [Monitoring settings schema](/docs/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "View builtin:cloud.kubernetes.monitoring settings schema table of your monitoring environment via the Dynatrace API.").

To change the default values for the environment, set the `scope` property in the request to `environment`.

To use the default settings when connecting a cluster, the [Connection settings schema](/docs/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "View builtin:cloud.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") should be version `3.0.0` or higher. Using older versions will automatically override the default monitoring settings for this cluster.

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")