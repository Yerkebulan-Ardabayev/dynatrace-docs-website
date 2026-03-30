---
title: Log ingestion API (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api
scraped: 2026-03-06T21:16:13.984280
---

# Log ingestion API (Logs Classic)


* Classic
* Overview
* 3-min read
* Updated on Jan 30, 2026

Log Monitoring Classic

For the newest Dynatrace version, see Log ingestion API.

Dynatrace automatically collects log and event data from a vast array of technologies. With the Log ingestion API, you can stream log records to a system, and have Dynatrace transform the stream into meaningful log messages.

The Log ingestion API allows you to stream log records to the system. It is available via Ingest JSON and TXT logs (Logs Classic) or via Ingest OTLP logs.

* For Dynatrace SaaS, the Log ingestion endpoint is available in your environment.

* If the Environment ActiveGate is your choice for an endpoint in your local environment, install an ActiveGate instance:

In Dynatrace Hub, select **ActiveGate** > **Set up**.

The Log ingestion API v2 is automatically enabled on ActiveGate. ActiveGate is responsible for serving the endpoint, collecting the data, and forwarding it to Dynatrace in batches.

* Saas endpoints:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`

* Environment ActiveGate endpoints:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`

## Log data queue on Environment ActiveGate

You can customize the log data queue properties by editing the `custom.properties` file (see Configuration properties and parameters of ActiveGate) on your ActiveGate to set the following values:

```
[generic_ingest]


#disk_queue_path=<custom_path> # defaults to temp folder


#disk_queue_max_size_mb=<limit> # defaults to 300 MB
```

503 Usable space limit reached

The log data ingestion API returns a `503 Usable space limit reached` error when the ingested log data exceeds the configured queue size. Typically, this is a temporary situation that occurs only during spikes. If this error persists, increase the value of `disk_queue_max_size_mb` in `custom.properties` to allow log ingestion spikes to be queued.

## Example

In this example, the API request ingests log data that will create a log event with defined log attributes `content`, `status`, `service.name`, and `service.namespace`.

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

Visit Dynatrace Community for troubleshooting guides, as well as see Troubleshooting Log Monitoring (Logs Classic).

* [Troubleshooting log Ingestion via API - POST ingest logsï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Related topics

* Log Monitoring API v2 - POST ingest logs
* Ingest OTLP logs