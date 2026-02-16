# Dynatrace Documentation: managed/observe

Generated: 2026-02-16

Files combined: 4

---


## Source: merged-services.md


---
title: Merged services
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services
scraped: 2026-02-16T09:30:17.346463
---

# Merged services

# Merged services

* How-to guide
* 3-min read
* Updated on Oct 04, 2022

**Settings** > **Merged service monitoring** is deprecated.

* If merged services exist in your environment, you can still access the page to view and edit them.
* You can't create new merged services from this setting page. To create or edit the equivalent of a merged service via rule-based detection, see [Create a rule to aggregate services](#create-merged-service) below.

A merged service is a service that aggregates multiple [web-request services](/docs/observe/application-observability/services/service-detection/service-detection-v1#web-request-service "Find out how Dynatrace Service Detection v1 detects and names different types of services.") of the same process group that perform identical functions across separate cluster nodes. These web-request services are effectively identical from a performance-monitoring perspective. A merged service appears in Dynatrace as a single service that contains all the data of all aggregated services.

Say you have an Apache web server with several virtual host definitions (for example, `dynatrace.com`, `dynatrace.at`, and `dynatrace.pl`). From the Apache perspective, these are independent virtual hosts. Dynatrace therefore detects them as separate services. For your monitoring purposes however, you might want to view these services as a single merged service called `Dynatrace web page`.

Dynatrace automatically identifies mergeable services for you and displays them on the **Merged service monitoring** page (**Settings** > **Server-side service monitoring** > **Merged service monitoring**). Only services included in this list can be merged.

## Characteristics of existing merged services

* Once merged, the data of individual merged services can no longer be distinguishedâmonitoring data is available only in aggregate form for all the merged services.
* The original services of a merged service are no longer updated as data sources. While historical data remains available (for example, for charting), no new data is tracked for the original services. The aggregated data is assigned to and associated with the merged service.
* Merged services are of the same type. For example, they belong to the same process group, share the same underlying technology, or follow the same naming pattern. Multiple virtual hosts, context roots, or listen ports that represent the same logical entity can be part of a service merging.
* Only near-identical, standalone web-request services of the same process group are mergedâmerged services are not merged into other merged services.

## Split merged services

When you split a service from a merged service ("unmerge" the service), the historic data will be available only for the merged service. All newly captured data will be associated with the new standalone service.

To split a service from a merged service

1. Go to **Settings** > **Server-side service monitoring** > **Merged service monitoring**.
2. Select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in the row of the merged service you want to split.
3. Select **Remove** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the row of the service you want to remove.
4. Select **Update**.

## Delete merged service

If you delete a merged service, all individual merged services will be split and once again treated as standalone services.

To delete a merged service:

1. Go to **Settings** > **Server-side service monitoring** > **Merged service monitoring**.
2. Select **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the row of the merged service you want to delete.

## Create a rule to aggregate services

To carry out the equivalent task of creating a merged service, but via rule-based service detection

1. Go to **Settings** > **Service Detection**.

   * Select **Full web request rules** if the web requests are fully monitored by Dynatrace.
   * Select **External web request rules** for web requests going to external resources.
2. Select **Add item** and add a name for your new rule.
3. Turn on at least one service identifier contributor from the following: **Application identifier**, **URL context root**, and **Server name**.
4. Optional You can modify your rule by:

   * Setting a management zone
   * Adding specific conditions
   * Disabling the port
5. Select **Save changes**.

To learn more about how to create, edit, or delete service detection rules, see [Manage rule-based service detection](/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection#manage "Use detection rules to customize and enhance the automated detection of your services.").

## Related topics

* [Service detection rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services.")


---


## Source: monitor-cluster-utilization-kubernetes.md


---
title: Monitor Kubernetes/OpenShift cluster utilization
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes
scraped: 2026-02-15T21:20:04.913642
---

# Monitor Kubernetes/OpenShift cluster utilization

# Monitor Kubernetes/OpenShift cluster utilization

* 2-min read
* Updated on Apr 29, 2024

Dynatrace version 1.232+

## Prerequisites

* In Dynatrace, go to your Kubernetes cluster settings page and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.

## Kubernetes page

After enabling access to the Kubernetes overview page for a specific Kubernetes cluster, the specific cluster will appear on the **Kubernetes** page. The Kubernetes page provides an overview of all Kubernetes clusters showing monitoring data like the clustersâ sizing and utilization.  
To access this page, go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.

![Cluster utilization](https://dt-cdn.net/images/cluster-list-3710-4c21475cfb.png)

## Utilization of cluster resources over time

As Kubernetes can run any containerized workloads and allow for horizontal pod autoscaling, the actual utilization of cluster resources will likely be very volatile. That is why Dynatrace offers a single pane of glass for the most important utilization and performance metrics on a cluster level. These metrics are:

* Percentage of CPU resources used out of the total allocatable CPU resources.
* Percentage of CPU resources requested/limited out of the total allocatable CPU resources.
* Percentage of memory resources requested/used out of the total allocatable memory resources.
* Percentage of memory resources limited out of the total allocatable memory resources.
* Total CPU/Memory usage.
* CPU/Memory resources requested/limited.
* CPU/Memory resources allocatable to pods.
* Total number of pods running/allocatable on cluster nodes.
* Number of times containers have been restarted.

![Monitor k8](https://dt-cdn.net/images/cluster-1-3700-55f0edc5fe.png)

## View available resources on your Kubernetes nodes

You can get detailed insights of the Kubernetes node metrics on a per-node level to understand how individual nodes are utilized. The **Node analysis** page also provides information about how much workload can still be deployed on nodes.

![View resource k8](https://dt-cdn.net/images/cluster-2-3700-209833d1e0.png)

By selecting a specific node, you can access the host details at the top of the node overview page. From there, you can delve into code-level insights on currently deployed containers, along with relevant cloud-specific host properties and Kubernetes node labels.

![View host k8](https://dt-cdn.net/images/cluster-3-3700-0d7e54a3e8.png)

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: postgres.md


---
title: Monitor PostgreSQL database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/postgres
scraped: 2026-02-16T09:38:39.064440
---

# Monitor PostgreSQL database

# Monitor PostgreSQL database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

Monitor PostgreSQL databases with the Dynatrace Extension Framework to collect performance data and understand database impact on your applications.

## Prerequisites

* Designate an ActiveGate group or groups that will remotely connect to your PostgreSQL database server to pull data. All ActiveGates in each group must connect to your PostgreSQL database server.
* For self-hosted Postgres:

  + Postgres [additional supplied modules](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#monitor-self-hosted-postgres "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.") must be installed.
* For cloud-managed Postgres services:

  + Ensure that [specific extensions and settings are enabled](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#setup-cloud-monitoring-capabilities "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.").
* Create a dedicated database user in your database instance. Dynatrace uses this user to run monitoring queries against your PostgreSQL database.

  ```
  CREATE USER dynatrace WITH PASSWORD '<PASSWORD>' INHERIT;
  ```

### Compatibility information

* Supported from PostgreSQL version 11+.
* Postgres 14, 15, 16, and 17 are fully supported.

## Set up the PostgreSQL extension for monitoring

To set up and activate the extension, go to ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** and follow these steps for each instance.

### Add a database instance

1. Open the **Add DB instance** wizard from the top-right corner of ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases**.
2. Select **PostgreSQL** as the database vendor.
3. Select **Next**.

### Select hosting type

Select a hosting type from the options. This choice determines which script generates the necessary database objects later in the process.

1. Select the host type that matches your requirement.
2. Select **Next**.

### Select an ActiveGate group

1. Select the [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.") to determine which ActiveGates run the extension.
2. Select **Next**.

### Create a connection

Set up the connection to your database instance. Provide the required credentials directly in the wizard or use secure alternatives:

1. Add a name for the connection so you can identify it later.
2. Add the details in the **Configure connection** section.

   1. Choose **Select from existing hosts** or **Enter manually** to add connection details.
   2. Add the **Database name**.
3. Provide the **Authenticate** credentials for the `dynatrace` monitoring user you created directly or use secure alternatives.

   * Basic credentials: Authentication details passed to Dynatrace when activating monitoring configuration are masked to prevent them from being retrieved.
   * Credential vault: Use [vault credentials](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring#authentication "PostgreSQL extensions in the Extensions framework.") to securely store and retrieve database credentials.
4. Select **Next**.

### Install the instance

Run the provided script to create the necessary objects on the database instance. The agent requires these objects to collect monitoring data.

1. Complete the manual setup for the required instances.
2. Complete manual setup for required instances.
3. Select **Create DB instance monitoring**.

You must run this script to retrieve metrics from the database. To learn more, refer to the helper function details in the [install the instance](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#install-instance "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.") section.

Recommended

After running the creation script, run the validation script to confirm all required objects were created. This ensures the monitoring setup will work as expected.

### Open the Databases app in Explorer

1. Go to the ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** app and select the **Explorer** tab.
2. View the added database in the **Database instances** list. The Explorer view displays all monitored database instances.
3. Select any monitored database instance to view its details. Metrics and performance data appear in the app within 2 to 3 minutes after you complete the setup.

## Use cases

Learn more about PostgreSQL monitoring in these [use cases](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#use-cases "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.").

## Feature sets

[Feature sets](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#feature-sets "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.") restrict which metrics are collected when you activate the extension.

## FAQ and troubleshooting

For complete details, go to the [FAQ](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#faq "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.") section.

## Related topics

* [PostgreSQL extension](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.")


---


## Source: vmware-vsphere-monitoring.md


---
title: VMware vSphere monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/vmware-vsphere-monitoring
scraped: 2026-02-16T09:21:48.690898
---

# VMware vSphere monitoring

# VMware vSphere monitoring

* How-to guide
* Published Aug 12, 2021

Setting up Dynatrace monitoring of a VMware platform is easy using ActiveGate as a communication gateway.

* ActiveGate receives the data from VMware and sends it to the Dynatrace Cluster.
* OneAgent, which is installed on each virtual machine, provides complementary data about your infrastructure health.

**Flow of monitoring data from your VMware platform to Dynatrace:**

![Virtualization data flow](https://dt-cdn.net/images/virtualization-flow-1280-93a1053e89.png)

The following applies to VMware only. For other virtualization platforms, you only need to install OneAgent for virtualized host monitoring, as the monitoring of virtualization management layers is supported only for VMware.

Once Dynatrace OneAgent is installed and process monitoring is activated on a virtual machine, you can see what's happening in your operating systemâspecifically, how your host-based processes behave and communicate.

Dynatrace collects information related to virtualized CPU usage, memory consumption, and storage-related activities. Dynatrace also detects virtual machine migrations (vMotion) and the creation of new virtual machines.

Follow the steps below to set up monitoring on the virtualization management layer of your VMware vCenter or standalone ESXi hosts.

## Prerequisites

* Read-only access to vCenter server, or access to the standalone ESXi host.

## Install and configure ActiveGate

[Install an Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") in your data center before connecting Dynatrace to your VMware platform.  
For **Dynatrace Managed** you can use the embedded ActiveGate running on the cluster node. However, the Cluster ActiveGate is typically used to forward RUM and/or Synthetic monitoring data to the Dynatrace Cluster. We recommend that you don't overutilize this ActiveGate with another type of monitoring data. Depending on the VMware size, you might consider using a dedicated ActiveGate per environment.

For virtualization monitoring, the `vmware_monitoring_enabled` property in `custom.properties` must be set to `true` (default value).

See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#vmware "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details.

## Connect Dynatrace to your VMware platform

To connect Dynatrace to your VMware platform

1. Go to **Settings** > **Cloud and virtualization** > **VMware**, and select **Connect new instance**.
2. Select the IP address or name of the vCenter server or standalone ESXi host you want to monitor (skip the `http://` or `https://` protocol prefix).
3. Check the network/proxy settings.  
   If you get a communication error even though the data provided is correct, it might be because of your network/proxy settings. We recommend that you revise the network/proxy settings when adding a new VMware integration.

   Optional You can also bypass the proxy for connecting with vCenter or ESXi when configuring the VMware integration. Modify [ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#exclude-hosts "Learn how to configure ActiveGate properties to set up a proxy.") to exclude a specific host from the proxy.
4. Enter the associated user credentials so that ActiveGate can sign in and collect monitoring data. The required privileges for this user are **view and read-only access**. Administrator-level access isn't required to enable monitoring (no changes to your VMware settings are required).

   You donât need to add ESXi hosts individually if they're managed by a vCenter server.
5. ActiveGate version 1.268+ Specify a filter condition to limit the number of monitored clusters:

   * `$prefix(parameter)`âproperty value starts with `parameter`
   * `$eq(parameter)`âproperty value exactly matches `parameter`
   * `$suffix(parameter)`âproperty value ends with `parameter`
   * `$contains(parameter)`âproperty value contains `parameter`
6. Select **Test connection** to verify that the entered data has successfully connected to your vCenter.

   Credentials

   The credentials are no longer validated automatically, so it's important to provide valid credentials that connect to your vCenter. If you provide invalid credentials, Dynatrace will still attempt to connect to your vCenter, which can create unnecessary network traffic.

   If your credentials for a particular vCenter change over time and you forget to update them in the settings, Dynatrace will detect five failed attempts to connect to your vCenter. After this, this setting will be disabled to prevent your VMware account from being blocked.
7. Select **Save changes**.

   Time synchronization

   Differences in system time can lead to missing VMware metrics. For Dynatrace to properly display monitoring data, synchronize time settings on all monitored host environments and vCenters with an NTP server.

To cover your entire virtual infrastructure, repeat these steps for all other vCenter servers or standalone ESXi hosts in your environment.

## Limit VMware infrastructure monitoring

After you set up VMware monitoring, you might want to limit which infrastructural elements (such as hosts and VMs) should actually be monitored by Dynatrace. To do this, you can use the permissions mechanism available in VMware. For more information, see [Limit VMware infrastructure monitoring using permissions](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring/limit-infrastructure-monitoring-using-permissions "Limit the size of your monitored VMware infrastructure using the VMware permissions mechanism.").

## Troubleshoot VMware connection

* Option 1 - [vCentre Event Consoleï»¿](https://dt-url.net/mh238c4)
* Option 2 - [VMware PowerCLIï»¿](https://dt-url.net/ni038yh) Windows only
* [Monitoring invalid credentialsï»¿](https://dt-url.net/fi038fn)

## Configure vSphere monitoring using Settings API

You can use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to configure VMware vSphere monitoring.

1. To learn the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:virtualization.vmware` as the schemaId.
2. Based on the `builtin:virtualization.vmware` schema, create your configuration object.
3. To create your configuration, use [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").


---
