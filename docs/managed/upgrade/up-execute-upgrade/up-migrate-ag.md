---
title: Migrate ActiveGate
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-ag
---

# Migrate ActiveGate

# Migrate ActiveGate

* Published Dec 07, 2023

There are three main approaches in the migration of ActiveGate from Dynatrace Managed to SaaS:

1. Recommended Concurrent deployment of new ActiveGates on the new hardware
2. ActiveGate reconfiguration
3. ActiveGate reinstallation on the same hardware

### What are the pros and cons of concurrent deployment of new ActiveGates on the new hardware?

Recommended

| Pros | Cons |
| --- | --- |
| * Potentially the least possible downtime for monitoring (cut-over is performed agent-side) * Can test ActiveGate setup before decommissioning existing setup * Could be well suited for highly regulated environments | * Additional cost of deploying and managing more infrastructure * Requires more time * May need to re-apply any customizations made to `custom.properties` and `launcheruserconfig.conf` |

To install a new ActiveGate in parallel on new hardware

1. Provision new hardware for the ActiveGate from the new SaaS environment.
2. Backup custom configuration files: `custom.properties`, `launcheruserconfig.conf`, and keystore/truststore.

   To learn more about these files, see [Configuration properties and parameters of ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").
3. Follow the selected [ActiveGate installation](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") procedure. Customize the installation command to apply keystore and truststore files.
4. [Stop the ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
5. Add or replace original configuration files: `custom.properties`, `launcheruserconfig.conf` to the new ActiveGate installation path.
6. [Start the ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
7. You can uninstall the old ActiveGate after you migrate all OneAgents that reported to it. You can check which OneAgents report to the ActiveGate at [OneAgent health overview](/managed/ingest-from/dynatrace-oneagent/oneagent-health "Discover deployed OneAgent modules at scale and detect anomalies before they turn into problems.").

### What are the pros and cons of ActiveGate reconfiguration?

| Pros | Cons |
| --- | --- |
| * Less downtime and bandwidth (don't need to download and run any installers) * Re-use existing infrastructure * Avoid re-deploying extension packages | * Error-prone due to manual configuration modification * Possible monitoring gaps without failover for OneAgent * Requires environment token rotation |

To reconfigure an existing ActiveGate to point OneAgent traffic to the new SaaS environment

1. [Stop the ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
2. Backup configuration files: `connectivity.history`, `config.properties`, `cluster.properties`, `custom.properties`, `launcheruserconfig.conf`, and keystore/truststore.

   To learn more about these files, see [Configuration properties and parameters of ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").
3. Update `config.properties` with the **seedServerUrl** and **configured=false** to your SaaS environment URL.
4. If you use a load balancer between the ActiveGate and the Dynatrace Managed cluster, and if the `--ignore-cluster-runtime` parameter was used, remove it from the `custom.properties` file.

   To learn more, see [Reverse proxy or load balancer for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Learn how to configure ActiveGate properties to set up a reverse proxy or a load balancer.").
5. Modify the `authorization.properties` file. Replace the current `tenantToken` field with [tenant token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") collected from the environment you want the ActiveGate to connect to.
6. [Create a new ActiveGate token](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/post-activegate-token "Create a new ActiveGate token via Dynatrace API.") on the target tenant, and use it to replace the one set in the `authorization.properties` file (source tenant). Otherwise, the ActiveGate startup fails with the following errors:

   ```
   2024-04-12 13:58:46 UTC WARNING [<rtc43848>] [<collector.core>, InitialCollectorSetupPoller] Initial collector setup received with error:REQUEST_REJECTED, reason=Invalid ActiveGate Token source=ANY_SERVER 0x0000000000000000 [Suppressing further messages for 1 hour]



   2024-04-12 13:59:18 UTC INFO    [<rtc43848>] [<WatchDog>, WatchDogImpl] Connected successfully to native watchdog on 127.0.0.1:50000
   ```
7. [Start the ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

### What are the pros and cons of ActiveGate reinstallation on the same hardware?

| Pros | Cons |
| --- | --- |
| * Less error-prone, as you don't need to modify existing configuration files * Re-use existing infrastructure * You can re-use your existing automation tools | * Downtime when running an installer * May need to re-apply any customization made to `custom.properties` and `launcheruserconfig.conf` * Possible monitoring gaps without failover for OneAgent |

To reinstall an ActiveGate on the same hardware to point OneAgent traffic to the new SaaS environment

1. Make a backup of any custom configuration, including `custom.properties` and `launcheruserconfig.conf`.
   To learn more about these files, see [Configuration properties and parameters of ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").
2. [Uninstall ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/uninstall-activegate "Learn how to remove ActiveGate from Windows or Linux-based systems.").
3. Follow the selected [ActiveGate installation](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") procedure. Customize the installation command to apply keystore and truststore files.
4. [Stop the ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
5. Add or replace original configuration files: `custom.properties`, `launcheruserconfig.conf` to the new ActiveGate installation path.
6. [Start the ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").