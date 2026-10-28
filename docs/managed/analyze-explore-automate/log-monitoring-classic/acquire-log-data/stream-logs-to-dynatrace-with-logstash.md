---
title: Stream logs to Dynatrace with Logstash (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring-classic/acquire-log-data/stream-logs-to-dynatrace-with-logstash
---

# Stream logs to Dynatrace with Logstash (Logs Classic)

# Stream logs to Dynatrace with Logstash (Logs Classic)

* Explanation
* 1-min read
* Updated on Jun 09, 2026

Log Monitoring Classic

[Dynatrace Log Monitoring](/managed/analyze-explore-automate/log-monitoring-classic "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") uses OneAgent DaemonSet, which includes a log module. This is the recommended way of streaming logs from nodes and pods to Dynatrace.

Alternatively, you can use the [Dynatrace Logstash output plugin﻿](https://github.com/dynatrace-oss/logstash-output-dynatrace), which is an open-source module, to stream logs.

![Logstash pipeline to Dynatrace](https://cdn.bfldr.com/B686QPH3/as/hq9cw74gk5mzsw49bzsz4s/Stream_logs_to_Dynatrace_with_Logstash-Light_Mode?auto=webp&format=png&position=1)

Logstash pipeline to Dynatrace

## Capabilities

Supports sending logs to [Dynatrace log ingest API v2](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

The Dynatrace Logstash output plugin also provides the following capabilities:

* Dynatrace API authentication
* Retry failed requests due to temporary network conditions
* Split large payloads into smaller batches ensuring each batch respects Dynatrace API limits (plugin version `0.5.1+`)
* Optional gzip compression (plugin version `0.6.1+`)
* Optional HTTP proxy configuration (plugin version `0.5.0+`)
* Optionally disable SSL verification for use with self-signed certificates

## Deploy integration

For instructions on how to deploy Logstash integration, see the [documentation on GitHub﻿](https://github.com/dynatrace-oss/logstash-output-dynatrace/blob/main/README.md)

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