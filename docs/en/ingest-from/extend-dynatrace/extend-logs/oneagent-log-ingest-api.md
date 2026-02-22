---
title: OneAgent log ingest API
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api
scraped: 2026-02-22T21:28:59.169221
---

# OneAgent log ingest API

# OneAgent log ingest API

* Latest Dynatrace
* 2-min read
* Updated on Jul 01, 2025

You can use the local `http://localhost:<port>/v2/logs/ingest` API endpoint to push locally retrieved logs to Dynatrace over a secure and authenticated channel. This endpoint is available only to local clients and cannot be reached from remote hosts.

The OneAgent log ingest endpoint mimics the behavior of the public [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.") endpoint.

## Enable the log ingest API

You need to enable the OneAgent log ingest API at the environment or host level. Note that the host-level configuration overrides the environment configuration.

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

## Log event format

The request consumes an `application/json` payload with the `charset=utf-8` character set. For more information on the format, see [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

## Limits

The log events pushed to Dynatrace using the OneAgent log ingest API are subject to the same limits as those for the public [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs#request-body-objects "Push custom logs to Dynatrace via the Log Monitoring API v2.").

## Example

With this `curl` command, you'll ingest the `Exception: Custom error log sent via OneAgent log ingest` event, with the severity set to `error` and a custom attribute set to `attribute value`. As the timestamp isn't provided, the event is automatically timestamped with the event reading time. You'll be able to access the event in [Log viewer (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.").

```
curl -i -X POST "http://127.0.0.1:14499/v2/logs/ingest" -H "Content-Type: application/json; charset=utf-8" -d "{\"content\":\"Exception: Custom error log sent via Generic Log Ingest\",\"custom.attribute\":\"attribute value\",\"severity\": \"error\"}"
```

Successful response returns the `204` code.

```
HTTP/1.1 204 No Content



Content-Type: application/json



Server: EEC



Content-Length: 116
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

Note that changing the port for the OneAgent log ingest API also affects [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities."), [Metric scripting integration](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration."), and [Telegraf metrics integration](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Ingest Telegraf metrics into Dynatrace.").