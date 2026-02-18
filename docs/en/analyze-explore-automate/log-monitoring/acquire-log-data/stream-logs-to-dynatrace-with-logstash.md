---
title: Stream logs to Dynatrace with Logstash (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-to-dynatrace-with-logstash
scraped: 2026-02-18T05:50:45.725546
---

# Stream logs to Dynatrace with Logstash (Logs Classic)

# Stream logs to Dynatrace with Logstash (Logs Classic)

* Explanation
* 1-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

For the newest Dynatrace version, see [Stream logs to Dynatrace with Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace.").

[Dynatrace Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") uses OneAgent DaemonSet, which includes a log module. This is the recommended way of streaming logs from nodes and pods to Dynatrace.

Alternatively, you can use the [Dynatrace Logstash output pluginï»¿](https://github.com/dynatrace-oss/logstash-output-dynatrace), which is an open-source module, to stream logs.

![Logstash pipeline to Dynatrace](https://dt-cdn.net/images/logstash-anna-new-eb3c5ac7a3.svg)

## Capabilities

Supports sending logs to [Dynatrace log ingest API v2](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

The Dynatrace Logstash output plugin also provides the following capabilities:

* Dynatrace API authentication
* Retry failed requests due to temporary network conditions
* Split large payloads into smaller batches ensuring each batch respects Dynatrace API limits (plugin version `0.5.1+`)
* Optional gzip compression (plugin version `0.6.1+`)
* Optional HTTP proxy configuration (plugin version `0.5.0+`)
* Optionally disable SSL verification for use with self-signed certificates

## Deploy integration

For instructions on how to deploy Logstash integration, see the [documentation on GitHubï»¿](https://github.com/dynatrace-oss/logstash-output-dynatrace/blob/main/README.md)

**Example configuration:**

```
output {



dynatrace {



id => "dynatrace_output"



ingest_endpoint_url => "${ACTIVE_GATE_URL}/api/v2/logs/ingest"



api_key => "${API_KEY}"



}



}
```