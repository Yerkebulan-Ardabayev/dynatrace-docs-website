---
title: Send Telegraf metrics to Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf
scraped: 2026-02-18T21:23:40.675243
---

# Send Telegraf metrics to Dynatrace

# Send Telegraf metrics to Dynatrace

* Latest Dynatrace
* 2-min read
* Published Oct 15, 2020

[Telegrafï»¿](https://github.com/influxdata/telegraf) is a plugin-driven server agent for collecting, processing, aggregating, and writing metrics. Telegraf comes with the Dynatrace Output Plugin that enables you to easily send Telegraf metrics to Dynatrace.

## Enable Telegraf ingestion

Telegraf metric ingestion comes with OneAgent version 1.201+. The easiest configuration scenario is to install Telegraf and OneAgent on the same host. Then you only need to enable the Dynatrace Output Plugin in your Telegraf configuration (Telegraf version 1.16+) and enable Telegraf metric ingestion at the environment or host level in your Dynatrace configuration. Note that the host-level configuration overrides the environment-level configuration.

Enable the Dynatrace Output Plugin in Telegraf configuration

### Telegraf and OneAgent on the same host

1. Edit `telegraf.conf`, the [Telegraf configuration fileï»¿](https://docs.influxdata.com/telegraf/v1.16/administration/configuration/).
2. Uncomment the `[[outputs.dynatrace]]` line.
3. Optional Uncomment the `prefix = "telegraf."` line and set the prefix to easily find the Telegraf ingested metrics. The prefix will also be visible in the Dynatrace metric key.
4. Save the file.

```
# # Send telegraf metrics to a Dynatrace environment



[[outputs.dynatrace]]



#   ## For usage with the Dynatrace OneAgent you can omit any configuration,



#   ## the only requirement is that the OneAgent is running on the same host.



#   ## Only setup environment url and token if you want to monitor a Host without the OneAgent present.



#   ##



#   ## Your Dynatrace environment URL.



#   ## For Dynatrace OneAgent you can leave this empty or set it to "http://127.0.0.1:14499/metrics/ingest" (default)



#   ## For Dynatrace SaaS environments the URL scheme is "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"



#   ## For Dynatrace Managed environments the URL scheme is "https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest"



#   url = ""



#



#   ## Your Dynatrace API token.



#   ## Create an API token within your Dynatrace environment, by navigating to Settings > Integration > Dynatrace API



#   ## The API token needs data ingest scope permission. When using OneAgent, no API token is required.



#   api_token = ""



#



#   ## Optional prefix for metric names (e.g.: "telegraf.")



prefix = "telegraf."



#



#   ## Optional TLS Config



#   # tls_ca = "/etc/telegraf/ca.pem"



#   # tls_cert = "/etc/telegraf/cert.pem"



#   # tls_key = "/etc/telegraf/key.pem"



#



#   ## Optional flag for ignoring tls certificate check



#   # insecure_skip_verify = false



#



#



#   ## Connection timeout, defaults to "5s" if not set.



#   timeout = "5s"
```

### No OneAgent on the host

If you can't install OneAgent on the Telegraf-monitored host, you can configure the Dynatrace Output Plugin to push metrics directly to your Dynatrace environment through [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

#### Prerequisites

* [API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the **Ingest metrics data points** scope.
* Your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

1. Edit `telegraf.conf`, the [Telegraf configuration fileï»¿](https://docs.influxdata.com/telegraf/v1.15/administration/configuration/).
2. Uncomment the `# [[outputs.dynatrace]]` line.
3. Optional Uncomment the `# prefix = "telegraf."` line and set the prefix to easily find the Telegraf ingested metrics. The prefix will also be visible in the Dynatrace metric key.
4. Uncomment the `# api_token = ""` line and add your API token, for example `api_token = "abcdefjhij1234567890"`
5. Uncomment the `# url = ""` line and add your Dynatrace metric API endpoint. For example,

   * Dynatrace SaaS `url = "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"`
   * Dynatrace Managed `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest`
6. Save the file.

```
# # Send telegraf metrics to a Dynatrace environment



[[outputs.dynatrace]]



#   ## For usage with the Dynatrace OneAgent you can omit any configuration,



#   ## the only requirement is that the OneAgent is running on the same host.



#   ## Only setup environment url and token if you want to monitor a Host without the OneAgent present.



#   ##



#   ## Your Dynatrace environment URL.



#   ## For Dynatrace OneAgent you can leave this empty or set it to "http://127.0.0.1:14499/metrics/ingest" (default)



#   ## For Dynatrace SaaS environments the URL scheme is "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"



#   ## For Dynatrace Managed environments the URL scheme is "https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest"



#   url = "https://abd12345.live.dynatrace.com/api/v2/metrics/ingest"



#



#   ## Your Dynatrace API token.



#   ## Create an API token within your Dynatrace environment, by navigating to Settings > Integration > Dynatrace API



#   ## The API token needs data ingest scope permission. When using OneAgent, no API token is required.



api_token = "abcdefjhij1234567890"



#



#   ## Optional prefix for metric names (e.g.: "telegraf.")



prefix = "telegraf."



#



#   ## Optional TLS Config



#   # tls_ca = "/etc/telegraf/ca.pem"



#   # tls_cert = "/etc/telegraf/cert.pem"



#   # tls_key = "/etc/telegraf/key.pem"



#



#   ## Optional flag for ignoring tls certificate check



#   # insecure_skip_verify = false



#



#



#   ## Connection timeout, defaults to "5s" if not set.



#   timeout = "5s"
```

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

## Topology awareness

When OneAgent and Telegraf are installed on the same host, the host ID and host name context are automatically added to each metric as dimensions. Learn how to [enrich your metrics with other Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") and apply Dynatrace-AI causation details to your ingested data.

## Metric format

Provided data points must follow the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

## Communication port

The Telegraf Dynatrace Output Plugin sends metrics to the [OneAgent metric API](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") endpoint.

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

If you change the default OneAgent communication port, make sure you also update the Telegraf configuration.

1. Edit `telegraf.conf`, the [Telegraf configuration fileï»¿](https://docs.influxdata.com/telegraf/v1.15/administration/configuration/).
2. Set the `url` property to `url = "http://127.0.0.1:<your-custom-port>/metrics/ingest"`.
3. Save the file.

Note that changing the port for Telegraf ingested metrics also affects OneAgent REST API and Scripting integration.