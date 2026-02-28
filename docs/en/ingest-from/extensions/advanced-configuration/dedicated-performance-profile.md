---
title: Dedicated performance profile configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/advanced-configuration/dedicated-performance-profile
scraped: 2026-02-28T21:25:01.208202
---

# Dedicated performance profile configuration

# Dedicated performance profile configuration

* Latest Dynatrace
* How-to guide
* 1-min read
* Published May 12, 2023

The dedicated performance profile offers powerful performance optimization for your Dynatrace environment. With the dedicated profile, you can enhance the computing capabilities of your ActiveGate host to improve monitoring and analysis capabilities.

## Limitations

* The dedicated performance profile should be used on powerful instances, such as `C6i.2xlarge`.
* When using the dedicated performance profile, no other ActiveGate functionality should be running simultaneously with extensions.
* If you use ActiveGate groups, ensure that all ActiveGates within the group have the same custom configuration applied for the chosen performance profile.

## Configuration

To configure the ActiveGate for the dedicated performance profile

1. Modify the `custom.properties` file to restrict ActiveGate functionality to Extensions 2.0 only.

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



   [beacon_forwarder]



   beacon_forwarder_enabled = false



   [metrics_ingest]



   metrics_ingest_enabled = false



   [collector]



   DumpSupported = false



   [collector]



   MSGrouter = false



   [otlp_ingest]



   otlp_ingest_enabled = false



   [collector]



   restInterface = false
   ```
2. Modify ActiveGate memory settings via the `launcheruserconfig.conf` file.

   ```
   -java.xmx.absolute_part=2000



   -java.xmx.relative_part=0
   ```
3. [Restart the ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") to apply the configuration changes.
4. [Set the performance profile of the ActiveGate](/docs/ingest-from/extensions/concepts#performance-profile "Learn more about the concept of Dynatrace Extensions.") to `Dedicated limits`.

## Related topics

* [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.")