---
title: Metric scripting integration
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe
scraped: 2026-02-28T21:14:25.556127
---

# Metric scripting integration

# Metric scripting integration

* Latest Dynatrace
* 2-min read
* Published Oct 15, 2020

You can use the `dynatrace_ingest` tool to push locally retrieved metrics to Dynatrace over a secure and authenticated channel. The tool is available to local clients only and cannot be reached from remote hosts.

## Enable scripting integration

Scripting integration comes with OneAgent version 1.201+ by default. You only need to enable scripting integration at the environment or local host level. Note that the host-level configuration overrides the environment configuration.

Enable at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable local HTTP Metric, Log and Event Ingest API**.

Enable for a single host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.

Enable for a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Extension Execution Controller**.
6. Turn on **Enable Extension Execution Controller**.

## Binary location

The tool location depends on whether or not you've customized the OneAgent installation using the `<INSTALL_PATH>` parameter:

* **Linux**:  
  `<INSTALL_PATH>/agent/tools`, by default `/opt/dynatrace/oneagent/agent/tools`
* **Docker-based deployment**  
  `<INSTALL_PATH>/agent/tools`, by default `/opt/dynatrace/oneagent/agent/tools`  
  Note that this path will differ for a volume-based deployment.
* **Windows**:  
  `<INSTALL_PATH>\agent\tools`, by default `%PROGRAMFILES%\dynatrace\oneagent\agent\tools`

## Topology awareness

Using the `dynatrace_ingest` based scripting integration, the host ID and host name context are added to each metric as dimensions automatically. Learn how to [enrich your metrics with other Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") and apply Dynatrace-AI causation details to your ingested data.

## Metric format

Provided data points must follow the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

## Usage

The basic usage is:

```
dynatrace_ingest [Options] [Metrics]
```

Both `[Options]` and `[Metrics]` are optional. The syntax of metrics passed to the `[Metrics]` arguments must comply with the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

There two basic ways to pass metrics with `dynatrace_ingest`: (1) by piping another process output to `dynatrace_ingest`, or (2) using the call arguments.

### Piping process output

When metrics are omitted, `dynatrace_ingest` expects them to be passed via standard input. Each line is treated as one metric. This enables you to pipe metrics to `dynatrace_ingest` from the output of other processes. For example:

```
echo host.process_count `ps aux | wc -l` | dynatrace_ingest
```

### Call arguments

When using call arguments instead of standard input to pass metrics, pass each metric as a separate argument. For example, to pass two metrics using a single command:

```
dynatrace_ingest 'cpu.temperature,cpu=1 55'  'cpu.temperature,cpu=2 45'
```

### Command line options

`-v [ --verbose ]`  
Prints logs to standard output

`-p [ --port ] arg (=14499)`  
Sets custom port for communication with the OneAgent Extensions Execution Controller (EEC) module. If you change the default EEC port (`14499`), you must instruct `dynatrace_ingest` to use the new port. For more information on setting a custom EEC port, see [Communication port](#communication-port)

`-h [ --help ]`  
Prints help message and quit

## Communication port

Starting with OneAgent version 1.267+, AIX systems also support metric ingestion.

The default metric ingestion port is `14499`. If necessary, you can use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command to check or change the port. Changing the metric ingestion port requires restart of OneAgent. Add [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to the command to restart OneAgent automatically.

### Check the ingestion port

Use the `--get-extensions-ingest-port` parameter to show the current local ingestion port, `14499` by default.

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Set a custom ingestion port

Use the `--set-extensions-ingest-port=<arg>` parameter to set a custom local ingestion port.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Configure proxy

Configure your host proxy to allow localhost traffic going to the metric ingestion port, `14499` by default.

Note that changing the port for scripting integration also affects OneAgent REST API and Telegraf.