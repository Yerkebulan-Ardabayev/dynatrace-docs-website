---
title: Stream logs to Dynatrace with Fluent Bit
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit
scraped: 2026-02-20T21:28:20.274976
---

# Stream logs to Dynatrace with Fluent Bit

# Stream logs to Dynatrace with Fluent Bit

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Jan 22, 2026

You can send logs to Dynatrace using Fluent Bit. Configure Fluent Bit to send logs to the Dynatrace generic ingest API.

## Capabilities

* Fluent Bit is a multiplatform log processor and forwarder that allows you to collect data/logs from different sources, unify and send them to multiple destinations. It is compatible with the Docker and Kubernetes environments.
* Dynatrace can be configured as the target log management and analytics environment for your data thanks to Fluent Bit's configurable `http output`.
* You can use any of Fluent Bit input plugins to get logs and events from your application to Dynatrace.

## Configuration

The Fluent Bit `http output` plugin allows you to stream your logs to the Dynatrace generic logs ingest endpoint.

1. Get a [Dynatrace API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the `logs.ingest` (Ingest Logs) scope.
2. [Deploy Fluent Bitï»¿](https://dt-url.net/zd034je).
3. To send logs into the Dynatrace [generic logs ingest](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") endpoint, configure the [http output pluginï»¿](https://dt-url.net/0z034x4) through the configuration file.
4. In your main Fluent Bit configuration file, append the Output section with the following parameters:

```
[OUTPUT]



name  http



match *



header Content-Type application/json; charset=utf-8



header Authorization Api-Token {your-API-token-here}



allow_duplicated_headers false



host  {your-environment-id}.live.dynatrace.com



Port  443



URI   /api/v2/logs/ingest



Format json



json_date_format iso8601



json_date_key timestamp



tls On



tls.verify On
```

You can place your API token in the header or as `GET` variable in URI (see example below).

* For Dynatrace SaaS, the [generic logs ingest](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") endpoint is available in your environment.
* If [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate#agtypes "Understand the basic concepts related to ActiveGate.") is your choice for an endpoint in local environment, install ActiveGate instance.

  In Dynatrace Hub, select **ActiveGate** > **Set up**.
* Generic log ingest API v2 is automatically enabled on ActiveGate.

## Example: Ingest ECS Fargate logs with Fluent Bit

Fluent Bit is the recommended solution whenever reducing resource consumption is critical.
The example below describes how you can configure the ingestion of AWS Fargate logs with Fluent Bit.

When creating a new task definition using the AWS Management Console, the FireLens integration section makes it easy to add a log router container. Follow the steps below to configure log ingest:

1. In the AWS Management Console, go to the Firelens integration section.

![Final log integration page in AWS Management Console](https://dt-cdn.net/images/final-log-route-integration-870-b11a329df9.png)

2. Pick the built-in Fluent Bit image.

3. Edit the container in which your log-generating apps are running.

4. In the **Storage and Logging** section, select **awsfirelens** as the log driver.

![Set AWS Firelens as a log driver](https://dt-cdn.net/images/log-driver-950-0bbba4a0fb.png)

The settings for the log driver should point to the log ingest API of your SaaS tenant. You need to provide two headers for Fluent Bit: content type and authorization token. As FireLens supports only one header, you can pass the content type as part of the URL. Your configuration for AWS FireLens should contain certain key-value pairs, as shown in the code block below.

```
Name: http



TLS: on



Format: json



Header: Authorization Api-Token {your-API-token-here}



Host: {your-environment-id}.live.dynatrace.com



Port: 443



URI: /api/v2/logs/ingest?Content-Type=application/json



Allow_Duplicated_Headers": "false"



Json_Date_Format": "iso8601"



Json_Date_Key": "timestamp"
```

To avoid publishing the token in plaintext, follow the steps in [AWS Secrets Managerï»¿](https://dt-url.net/r5234z4).
Once your application starts publishing logs, you can view them in the Dynatrace UI.

Refer to [AWS sample repositoryï»¿](https://dt-url.net/3j0348v) for the task definition JSON with Dynatrace configuration.

For more configuration details, see [Amazon ECS Developer Guideï»¿](https://dt-url.net/cf4349a).

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

* [Troubleshooting logs ingested via Fluent Bitï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)