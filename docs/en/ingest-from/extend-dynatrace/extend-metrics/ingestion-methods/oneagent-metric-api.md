---
title: OneAgent metric API
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api
scraped: 2026-02-17T21:20:29.002060
---

# OneAgent metric API

# OneAgent metric API

* Latest Dynatrace
* 2-min read
* Updated on Jan 28, 2026

You can use the local `http://localhost:<port>/metrics/ingest` API endpoint to push locally retrieved metrics to Dynatrace over a secure and authenticated channel. This endpoint is available only to local clients and cannot be reached from remote hosts.

If you can't push metrics using a local API endpoint, you can also use the public [Metric API v2](#api) endpoint.

## Enable the OneAgent metric API

ActiveGate version 1.243+

OneAgent version 1.243+

The OneAgent metric API comes with OneAgent version 1.201 by default. You only need to enable the OneAgent metric API at the environment or host level. Note that the host-level configuration overrides the environment configuration.

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

If you want to change your limits for EEC resource consumption, see [Performance profile](/docs/ingest-from/extensions/concepts#performance-profile "Learn more about the concept of Dynatrace Extensions.").

## Topology awareness

Using the local API endpoint, the host ID and host name context are automatically added to each metric as dimensions. Learn how to [enrich your metrics with other Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") and apply Dynatrace-AI causation details to your ingested data.

## Metric format

Provided data points must follow the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

The request consumes a `text/plain` payload with the `charset=utf-8` character set. The payload is limited to `1,000` lines.

## Example

With this `curl` command, you'll ingest the `cpu.temperature` metric assigned to the `cpu=1` dimension. The metric will be automatically assigned to a respective host ID and host name.

```
curl --data "cpu.temperature,cpu=1 55" http://localhost:14499/metrics/ingest \



-H "Content-Type: text/plain; charset=utf-8"
```

Successful response:

```
{



"error": null,



"linesValid": 1,



"linesInvalid": 0



}
```

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

Note that changing the port for the OneAgent metric API also affects scripting integration and Telegraf.

## Metrics API v2

Unlike the local ingestion interface, which adds the topology context automatically (each metric is assigned to a respective host), metrics pushed through the public [Metrics API](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") v2 are flat by default. This is especially beneficial for business-related metrics that don't have any relation to the topology entities in your environment.

However, to have events raised for a selected host and have Dynatrace Intelligence perform causation analysis based on your metrics, you can configure your app to add the `dt.entity.host` dimension. To automatically enrich process group identifier with the metric, provide `dt.process.pid` dimension. For more information, see [Metrics API - POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.").

## Related topics

* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")