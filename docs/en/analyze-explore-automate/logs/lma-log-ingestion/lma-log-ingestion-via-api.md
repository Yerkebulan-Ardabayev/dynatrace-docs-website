---
title: Log ingestion API
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api
scraped: 2026-02-17T21:31:22.294255
---

# Log ingestion API

# Log ingestion API

* Latest Dynatrace
* Overview
* 3-min read
* Updated on Oct 08, 2025

## Ingest via Log ingestion API

When unable to install OneAgent, use the Log ingestion API. For example, in serverless environments like AWS Fargate, where logging relies on a built-in log router such as Fluent Bit, which can be easily integrated with the Dynatrace Log ingestion API. The Log ingest API allows you to stream log records to the Grail data lakehouse, and have Dynatrace transform the stream into meaningful log messages. You can configure Log ingest API integration for the vast variety of use cases, and you can include custom integrations. You can use our supported integrations for clouds or log shippers and for your custom use cases.

![log-api](https://dt-cdn.net/images/log-api-1980-03664b6a2d.png)

You can configure Log ingestion API integration for any log shippers that integrate with Dynatrace REST API, e.g. [OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector."), [Fluentbit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace."), [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace."), [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace.").

Dynatrace automatically collects log and event data from a vast array of technologies. With the Log ingestion API, you can stream log records to a system and have Dynatrace transform the stream into meaningful log messages.

![LMA - Generic log ingestion API](https://dt-cdn.net/images/lma-generic-log-ingestion-api-2500-090a5b5c43.png)

The Log ingestion API allows you to stream log records to the system. It is available via [Ingest JSON and TXT logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs "Understand how JSON and TXT logs are processed, whether in flattened or raw mode.") or via [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

* For Dynatrace SaaS, the logs ingestion endpoint is available in your environment.
* If the Environment ActiveGate is your choice for an endpoint in your local environment, install an ActiveGate instance: In Dynatrace Hub, select **ActiveGate** > **Set up**. The Log ingestion API v2 is automatically enabled on ActiveGate.
* The endpoint is enabled by default on all of your ActiveGates.
* ActiveGate is responsible for serving the endpoint, collecting the data, and forwarding it to Dynatrace in batches.
* SaaS endpoints:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`
* Environment ActiveGate endpoints:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`
* For Kubernetes environments, you can use [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.") or [Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.") to forward logs to Dynatrace.

ActiveGate will collect and attempt to automatically transform any log data containing the following elements:

* Log content
* Timestamp
* Key-Values attributes

When using log processing with the custom processing pipeline (OpenPipeline), ingest supports all JSON data types for attribute values. This requires SaaS version 1.295+ when using the SaaS API endpoint or ActiveGate version 1.295+ when using the ActiveGate API endpoint. In all other cases, all ingested values are converted to the string type.

### Retry failed requests

API clients have to retry executing log ingestion requests that failed on retryable errors.

Each API endpoint documentation specifies which response codes are retryable. When retrying, the client implements an exponential backoff strategy.

## Log data queue

You can customize the log data queue properties by editing the `custom.properties` file (see [Configuration properties and parameters of ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#generic-ingest "Learn which ActiveGate properties you can configure based on your needs and requirements.")) on your ActiveGate to set the following values:

```
[generic_ingest]



#disk_queue_path=<custom_path> # defaults to temp folder



#disk_queue_max_size_mb=<limit> # defaults to 300 MB
```

503 Usable space limit reached

The log data ingestion API returns a `503 Usable space limit reached` error when the ingested log data exceeds the configured queue size. Typically, this is a temporary situation that occurs only during spikes. If this error persists, increase the value of `disk_queue_max_size_mb` in `custom.properties` to allow log ingestion spikes to be queued.

## Example

In this example, the API request ingests JSON log data that will create a log event with defined log attributes `content`, `status`, `service.name`, and `service.namespace`.

The API token is passed in the Authorization header.

The response contains response code `204`.

#### Curl

```
curl -X POST \



https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest \



-H 'Content-Type: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-d '[



{



"content": "Exception: Custom error log sent via Log ingestion API",



"status": "error",



"service.name": "log-monitoring-tenant",



"service.namespace": "dev-stage-cluster"



}



]'
```

#### Request URL

```
https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest
```

#### Response content

```
Success
```

#### Response code

`204`

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

* [Troubleshooting log Ingestion via API - POST ingest logsï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Related topics

* [Ingest JSON and TXT logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs "Understand how JSON and TXT logs are processed, whether in flattened or raw mode.")
* [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")
* [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")
* [OpenTelemetry logs ingest API](/docs/dynatrace-api/environment-api/opentelemetry/post-logs "Send OpenTelemetry logs to Dynatrace via API.")
* [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation "Log ingestion API automatically transforms log data into output values for the loglevel attribute.")