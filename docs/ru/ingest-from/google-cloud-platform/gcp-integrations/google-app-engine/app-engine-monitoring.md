---
title: Google App Engine with Operations suite metrics monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring
scraped: 2026-02-19T21:33:44.799010
---

# Google App Engine with Operations suite metrics monitoring

# Google App Engine with Operations suite metrics monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google App Engine.

| Feature Set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| gae\_app/default\_metrics | Monitoring Agent API Request Count | Count | agent.googleapis.com/agent/api\_request\_count |
| gae\_app/default\_metrics | Logging Agent Log Entry Count | Count | agent.googleapis.com/agent/log\_entry\_count |
| gae\_app/default\_metrics | Logging Agent Retried Log Entry Writes Count | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gae\_app/default\_metrics | Monitoring Agent Memory Usage | Byte | agent.googleapis.com/agent/memory\_usage |
| gae\_app/default\_metrics | Monitoring Agent Metric Point Count | Count | agent.googleapis.com/agent/monitoring/point\_count |
| gae\_app/default\_metrics | Logging Agent API Request Count | Count | agent.googleapis.com/agent/request\_count |
| gae\_app/default\_metrics | Monitoring Agent Process Labels Size | Byte | agent.googleapis.com/agent/streamspace\_size |
| gae\_app/default\_metrics | Monitoring Agent is Throttling Processes | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gae\_app/default\_metrics | Monitoring/Logging Agent Uptime | Second | agent.googleapis.com/agent/uptime |
| gae\_app/default\_metrics | Autoscaling Metrics Utilization Capacity | Count | appengine.googleapis.com/flex/autoscaler/capacity |
| gae\_app/default\_metrics | Autoscaling Metrics Current Utilization | Count | appengine.googleapis.com/flex/autoscaler/current\_utilization |
| gae\_app/default\_metrics | Connections | Count | appengine.googleapis.com/flex/connections/current |
| gae\_app/default\_metrics | Reserved cores | Count | appengine.googleapis.com/flex/cpu/reserved\_cores |
| gae\_app/default\_metrics | CPU utilization | Percent | appengine.googleapis.com/flex/cpu/utilization |
| gae\_app/default\_metrics | Disk bytes read | Byte | appengine.googleapis.com/flex/disk/read\_bytes\_count |
| gae\_app/default\_metrics | Disk bytes written | Byte | appengine.googleapis.com/flex/disk/write\_bytes\_count |
| gae\_app/default\_metrics | Network bytes received. | Byte | appengine.googleapis.com/flex/network/received\_bytes\_count |
| gae\_app/default\_metrics | Network bytes sent. | Byte | appengine.googleapis.com/flex/network/sent\_bytes\_count |
| gae\_app/default\_metrics | Interception count | Count | appengine.googleapis.com/http/server/dos\_intercept\_count |
| gae\_app/default\_metrics | Quota denial count | Count | appengine.googleapis.com/http/server/quota\_denial\_count |
| gae\_app/default\_metrics | Response count | Count | appengine.googleapis.com/http/server/response\_count |
| gae\_app/default\_metrics | Response latency | MilliSecond | appengine.googleapis.com/http/server/response\_latencies |
| gae\_app/default\_metrics | Response count by style | Count | appengine.googleapis.com/http/server/response\_style\_count |
| gae\_app/default\_metrics | Memcache utilization | Count | appengine.googleapis.com/memcache/centi\_mcu\_count |
| gae\_app/default\_metrics | Hit ratio | Count | appengine.googleapis.com/memcache/hit\_ratio |
| gae\_app/default\_metrics | Memcache operations | Count | appengine.googleapis.com/memcache/operation\_count |
| gae\_app/default\_metrics | Memcache received bytes | Byte | appengine.googleapis.com/memcache/received\_bytes\_count |
| gae\_app/default\_metrics | Memcache sent bytes | Byte | appengine.googleapis.com/memcache/sent\_bytes\_count |
| gae\_app/default\_metrics | Used Cache Size | Byte | appengine.googleapis.com/memcache/used\_cache\_size |
| gae\_app/default\_metrics | Estimated instance count | Count | appengine.googleapis.com/system/billed\_instance\_estimate\_count |
| gae\_app/default\_metrics | CPU megacycles | Count | appengine.googleapis.com/system/cpu/usage |
| gae\_app/default\_metrics | Instance count | Count | appengine.googleapis.com/system/instance\_count |
| gae\_app/default\_metrics | Memory usage | Byte | appengine.googleapis.com/system/memory/usage |
| gae\_app/default\_metrics | Received bytes | Byte | appengine.googleapis.com/system/network/received\_bytes\_count |
| gae\_app/default\_metrics | Sent bytes | Byte | appengine.googleapis.com/system/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Connections | Count | appengine.googleapis.com/flex/instance/connections/current |
| gae\_instance/default\_metrics | CPU Utilization | Percent | appengine.googleapis.com/flex/instance/cpu/utilization |
| gae\_instance/default\_metrics | Network bytes received | Byte | appengine.googleapis.com/flex/instance/network/received\_bytes\_count |
| gae\_instance/default\_metrics | Network bytes sent | Byte | appengine.googleapis.com/flex/instance/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Websocket average duration | Second | appengine.googleapis.com/flex/instance/ws/avg\_duration |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")