---
title: Dedicated performance profile configuration
source: https://docs.dynatrace.com/managed/ingest-from/extensions/advanced-configuration/dedicated-performance-profile
---

# Dedicated performance profile configuration

# Dedicated performance profile configuration

* How-to guide
* 1-min read
* Updated on Apr 28, 2026

The dedicated performance profile offers powerful performance optimization for your Dynatrace environment. With the dedicated profile, you can enhance the computing capabilities of your ActiveGate host to improve monitoring and analysis capabilities.

## Limitations

* The dedicated performance profile should be used on powerful instances, such as `C6i.2xlarge` (AWS), `Standard_F8s_v2` (Azure), or `c2-standard-8` (GCP).
* When using the dedicated performance profile, no other ActiveGate functionality should be running simultaneously with extensions.
* If you use ActiveGate groups, ensure that all ActiveGates within the group have the same custom configuration applied for the chosen performance profile.

## Configuration

To configure the ActiveGate for the dedicated performance profile

1. Restrict ActiveGate functionality to Extensions only.

   agctl

   custom.properties

   ActiveGate version 1.333+

   Use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Learn how to use agctl to configure and manage ActiveGate from the command line") to disable modules:

   ```
   agctl modules disable aws_monitoring,azure_monitoring,cloudfoundry_monitoring,debugging,kubernetes_monitoring,log_analytics_collector,vmware_monitoring,dbAgent,zremote,synthetic,metrics_ingest,DumpSupported,MSGrouter,otlp_ingest
   ```

   Modify the `custom.properties` file:

   ```
   [aws_monitoring]



   aws_monitoring_enabled = false



   [azure_monitoring]



   azure_monitoring_enabled = false



   [cloudfoundry_monitoring]



   cloudfoundry_monitoring_enabled = false



   [debugging]



   debugging_enabled = false



   [kubernetes_monitoring]



   kubernetes_monitoring_enabled = false



   [log_analytics_collector]



   log_analytics_collector_enabled = false



   [vmware_monitoring]



   vmware_monitoring_enabled = false



   [dbAgent]



   dbAgent_enabled = false



   [zremote]



   zremote_enabled = false



   [synthetic]



   synthetic_enabled = false



   [metrics_ingest]



   metrics_ingest_enabled = false



   [collector]



   DumpSupported = false



   [collector]



   MSGrouter = false



   [otlp_ingest]



   otlp_ingest_enabled = false
   ```
2. Modify ActiveGate memory settings via the `launcheruserconfig.conf` file.

   ```
   -java.xmx.absolute_part=2000



   -java.xmx.relative_part=0
   ```
3. [Restart the ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") to apply the configuration changes.
4. [Set the performance profile of the ActiveGate](/managed/ingest-from/extensions/concepts#performance-profile "Learn more about the concept of Dynatrace Extensions.") to `Dedicated limits`.

## Related topics

* [About Extensions](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.")