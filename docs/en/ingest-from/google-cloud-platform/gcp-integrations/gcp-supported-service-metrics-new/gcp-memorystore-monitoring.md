---
title: Google Cloud Memorystore monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-memorystore-monitoring
scraped: 2026-02-21T21:21:50.420019
---

# Google Cloud Memorystore monitoring

# Google Cloud Memorystore monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
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

The following feature sets are available for Google Cloud Memorystore.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| redis\_instance/default\_metrics | Blocked Clients | Count | redis.googleapis.com/clients/blocked |
| redis\_instance/default\_metrics | Connected Clients | Count | redis.googleapis.com/clients/connected |
| redis\_instance/default\_metrics | Calls | Count | redis.googleapis.com/commands/calls |
| redis\_instance/default\_metrics | Total Time of Calls | MicroSecond | redis.googleapis.com/commands/total\_time |
| redis\_instance/default\_metrics | Time per Call | Count | redis.googleapis.com/commands/usec\_per\_call |
| redis\_instance/default\_metrics | Average TTL | MilliSecond | redis.googleapis.com/keyspace/avg\_ttl |
| redis\_instance/default\_metrics | Keys | Count | redis.googleapis.com/keyspace/keys |
| redis\_instance/default\_metrics | Expirable Keys | Count | redis.googleapis.com/keyspace/keys\_with\_expiration |
| redis\_instance/default\_metrics | Persisting RDB | Count | redis.googleapis.com/persistence/rdb/bgsave\_in\_progress |
| redis\_instance/default\_metrics | Bytes lagging | Byte | redis.googleapis.com/replication/master/slaves/lag |
| redis\_instance/default\_metrics | Replication byte offset (Replica) | Byte | redis.googleapis.com/replication/master/slaves/offset |
| redis\_instance/default\_metrics | Replication byte offset (Master) | Byte | redis.googleapis.com/replication/master\_repl\_offset |
| redis\_instance/default\_metrics | Bytes pending replication | Byte | redis.googleapis.com/replication/offset\_diff |
| redis\_instance/default\_metrics | Node Role | Count | redis.googleapis.com/replication/role |
| redis\_instance/default\_metrics | Uptime | Second | redis.googleapis.com/server/uptime |
| redis\_instance/default\_metrics | Cache Hit ratio | Count | redis.googleapis.com/stats/cache\_hit\_ratio |
| redis\_instance/default\_metrics | Total Connections Received | Count | redis.googleapis.com/stats/connections/total |
| redis\_instance/default\_metrics | CPU seconds | Second | redis.googleapis.com/stats/cpu\_utilization |
| redis\_instance/default\_metrics | Evicted Keys | Count | redis.googleapis.com/stats/evicted\_keys |
| redis\_instance/default\_metrics | Expired Keys | Count | redis.googleapis.com/stats/expired\_keys |
| redis\_instance/default\_metrics | Hits | Count | redis.googleapis.com/stats/keyspace\_hits |
| redis\_instance/default\_metrics | Misses | Count | redis.googleapis.com/stats/keyspace\_misses |
| redis\_instance/default\_metrics | Maximum Memory | Byte | redis.googleapis.com/stats/memory/maxmemory |
| redis\_instance/default\_metrics | Time in system memory overload | MicroSecond | redis.googleapis.com/stats/memory/system\_memory\_overload\_duration |
| redis\_instance/default\_metrics | System Memory Usage Ratio | Count | redis.googleapis.com/stats/memory/system\_memory\_usage\_ratio |
| redis\_instance/default\_metrics | Used Memory | Byte | redis.googleapis.com/stats/memory/usage |
| redis\_instance/default\_metrics | Memory Usage Ratio | Count | redis.googleapis.com/stats/memory/usage\_ratio |
| redis\_instance/default\_metrics | Total traffic to Redis | Byte | redis.googleapis.com/stats/network\_traffic |
| redis\_instance/default\_metrics | Pubsub Channels | Count | redis.googleapis.com/stats/pubsub/channels |
| redis\_instance/default\_metrics | Pubsub Patterns | Count | redis.googleapis.com/stats/pubsub/patterns |
| redis\_instance/default\_metrics | Rejected Connections | Count | redis.googleapis.com/stats/reject\_connections\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")