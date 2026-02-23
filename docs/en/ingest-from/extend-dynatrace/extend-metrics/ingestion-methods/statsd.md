---
title: Send StatsD metrics to Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd
scraped: 2026-02-23T21:22:40.516065
---

# Send StatsD metrics to Dynatrace

# Send StatsD metrics to Dynatrace

* Latest Dynatrace
* 5-min read
* Updated on Jun 18, 2025

StatsD is an industry standard for communicating arbitrary statistics and other metrics in a vendor-independent way via UDP. We recommend that you use Dynatrace OneAgent to ingest your metrics, as OneAgent comes with a StatsD daemon out of the box. This means that any application or library that supports StatsD can send metrics to Dynatrace. You only need to install OneAgent and make sure that your StatsD client uses the right port (`18125` by default).

Supported OneAgent

StatsD daemon is only available on OneAgent installed on the VM or host that you want to monitor. OneAgent deployed on Kubernetes, for example using Dynatrace Operator, isn't supported. For Kubernetes environments, we recommend [remote StatsD monitoring](#remote) using an environment ActiveGate.

If you can't install OneAgent on a host with your StatsD metrics, however, you can use an ActiveGate to act as a remote listener.

## Choose your StatsD ingestion method

OneAgent

ActiveGate

OpenTelemetry Collector

Use OneAgent for direct installation on the host with StatsD. For more details, go to [OneAgent listener](#oneagent-listener).

If OneAgent cannot be installed on the host, use ActiveGate as a remote listener to collect StatsD metrics. For more details, go to [Remote StatsD](#remote-statsd).

For distributed environments or when using Kubernetes, OpenTelemetry Collector provides a solution to ingest StatsD metrics into Dynatrace. For more details, see [Ingest data from StatsD](/docs/ingest-from/opentelemetry/collector/use-cases/statsd "Configure the OpenTelemetry Collector to ingest StatsD data.").

## Enable DynatraceStatsD

The DynatraceStatsD listener comes with OneAgent version 1.201+. You only need to enable DynatraceStatsD metric ingestion at the environment, host, or host group level. Note that the host-level and host group-level configurations override the environment configuration.

Enable at the environment level

To enable DynatraceStatsD metric ingestion at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable Dynatrace StatsD**.

Enable at the host group level

To enable DynatraceStatsD metric ingestion at the host group level

1. Go to **Settings** and select **Monitoring overview** > **Hosts**.
2. Select the host group name for a chosen host.
3. On the **Host group settings** page, select **Extension Execution Controller**.
4. Turn on **Enable Dynatrace StatsD**.

Enable for a single host

To enable DynatraceStatsD metric ingestion only for selected hosts

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.
6. Turn on **Enable Dynatrace StatsD**.

Enable remote StatsD

ActiveGate version 1.227+

If you can't use OneAgent to ingest StatsD metrics, you can use an Environment ActiveGate as your DynatraceStatsD ingestion point. Your ActiveGate needs to be able to connect to your StatsD client over UDP.

DynatraceStatsD metric ingestion is disabled by default on an ActiveGate.

To enable DynatraceStatsD metric ingestion

1. Edit the `extensionsuser.conf` file in the following directory

   * Linux
     `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
   * Windows
     `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`
2. Set the `statsdenabled` parameter to `true`:

   ```
   statsdenabled=true
   ```
3. Restart the Extension Execution Controller service.

   * Linux
     Run the following commands:

     + for systems with SystemV:

       ```
       service extensionsmodule stop



       service extensionsmodule start
       ```
     + for systems with systemd:

       ```
       systemctl stop extensionsmodule



       systemctl start extensionsmodule
       ```
   * Windows
     Use **Task Manager** and restart the `Dynatrace Extensions Controller` service or run the following commands:

     ```
     net stop "Dynatrace Extensions Controller"



     net start "Dynatrace Extensions Controller"
     ```

Note that the default port for remote StatsD is different than for the OneAgent DynatraceStatsD listener (`18126`). See [Remote StatsD](#remote-statsd).

This file is not modified during ActiveGate updates.

Make sure that your ActiveGate can connect to your StatsD client. For example, you should configure the DNS name for your ActiveGate and make sure that it works after a new IP address is assigned from DHCP.

## Communication port

### OneAgent listener

The default DynatraceStatsD UDP listening port for the OneAgent listener is `18125`. If necessary, you can use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command to check or change the metric ingestion port. Changing the port requires restart of OneAgent. Add [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to the command to restart OneAgent automatically.

#### Check the ingestion port

Use the `--get-extensions-statsd-port` parameter to show the current DynatraceStatsd UDP listening port (default = `18125`).

* **Linux**:
  `./oneagentctl --get-extensions-statsd-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-statsd-port`

#### Set a custom ingestion port

Use the `--set-extensions-statsd-port=<arg>` parameter to set a custom DynatraceStatsd UDP listening port.

* **Linux**:
  `./oneagentctl --set-extensions-statsd-port=18125 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-statsd-port=18125 --restart-service`

### Remote StatsD

The default DynatraceStatsD UDP listening port for a remote listener is `18126`.

To change the default `18126` listening port, modify the `StatsdPort` parameter in the ActiveGate `extensionsuser.conf` file:

* Linux
  `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* Windows
  `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`:

```
StatsdPort=18126
```

## Topology awareness

Using DynatraceStatsD with OneAgent, the host ID and host name context are added as dimensions to each metric automatically. For more information, see [Metric ingestion](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."). Note that we're already working on more automatic metric enrichments. For remote ingestion, no extra enrichment is added. If you want to add context to your metrics, you'll need to add dimensions of your choice to your StatsD metrics.

## Security

The DynatraceStatsD OneAgent listener only accepts input from localhost addresses. This means that only processes that are running on the same host as OneAgent can leverage the interface. This ensures that no unauthorized programs are sending data to your Dynatrace environment.

## StatsD metric format

DynatraceStatsD accepts the following metrics in the [native StatsD formatï»¿](https://github.com/statsd/statsd/blob/master/docs/metric_types.md):

* `count`

  ```
  <metric name>:<value>|c
  ```
* `gauge`

  ```
  <metric name>:<value>|g
  ```
* `time`

  ```
  <metric name>:<value>|ms
  ```
* `histogram`

  ```
  <metric name>:<value>|h
  ```
* `set` OneAgent version 1.303+

  ```
  <metric name>:<value>|s
  ```
* `distribution`

  ```
  <metric name>:<value>|d
  ```

DynatraceStatsD extends the original protocol to enable you to also send dimensions. Use the following format:

```
<metric name>:<value>|g|#<Dimension1>:<value>,<Dimension2>:<value>
```

## Datasource limits and performance

The limits are based on the test that deploys a Linux machine in the AWS cloud. The purpose of this test is to determine how much StatsD load the infrastructure framework can handle.

### Hardware specification

OneAgent and ActiveGate are installed in a Linux-based VM in Amazon EC2 [c5.largeï»¿](https://dt-url.net/rv031ec) instance type.

* CPU: x2
* RAM: 4 GiB
* Storage: EBS
* Network bandwidth: up to 10 GBPS

|  | Total records | Packets | Lines per packet | Connections | Metrics |
| --- | --- | --- | --- | --- | --- |
| StatsD on OneAgent | 290,000 | 11,600 | 25 | 1 | 1 |
| StatsD on ActiveGate | 345,000 | 13,800 | 25 | 1 | 1 |