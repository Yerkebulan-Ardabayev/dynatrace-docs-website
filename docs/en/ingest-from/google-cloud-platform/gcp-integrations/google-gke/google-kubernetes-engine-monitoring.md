---
title: Google Kubernetes Engine monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring
scraped: 2026-02-15T21:27:12.866062
---

# Google Kubernetes Engine monitoring

# Google Kubernetes Engine monitoring

* Latest Dynatrace
* How-to guide
* 7-min read
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

The following feature sets are available for Google Kubernetes Engine.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| k8s\_cluster/default\_metrics | Log entries | Count | logging.googleapis.com/log\_entry\_count |
| k8s\_node/default\_metrics | Allocatable cores | Unspecified | kubernetes.io/node/cpu/allocatable\_cores |
| k8s\_node/default\_metrics | CPU allocatable utilization | Count | kubernetes.io/node/cpu/allocatable\_utilization |
| k8s\_node/default\_metrics | CPU usage time | Second | kubernetes.io/node/cpu/core\_usage\_time |
| k8s\_node/default\_metrics | Total cores | Unspecified | kubernetes.io/node/cpu/total\_cores |
| k8s\_node/default\_metrics | Allocatable ephemeral storage | Byte | kubernetes.io/node/ephemeral\_storage/allocatable\_bytes |
| k8s\_node/default\_metrics | Free inodes | Count | kubernetes.io/node/ephemeral\_storage/inodes\_free |
| k8s\_node/default\_metrics | Total inodes | Count | kubernetes.io/node/ephemeral\_storage/inodes\_total |
| k8s\_node/default\_metrics | Total ephemeral storage | Byte | kubernetes.io/node/ephemeral\_storage/total\_bytes |
| k8s\_node/default\_metrics | Ephemeral storage usage | Byte | kubernetes.io/node/ephemeral\_storage/used\_bytes |
| k8s\_node/default\_metrics | Allocatable memory | Byte | kubernetes.io/node/memory/allocatable\_bytes |
| k8s\_node/default\_metrics | Memory allocatable utilization | Count | kubernetes.io/node/memory/allocatable\_utilization |
| k8s\_node/default\_metrics | Total memory | Byte | kubernetes.io/node/memory/total\_bytes |
| k8s\_node/default\_metrics | Memory usage | Byte | kubernetes.io/node/memory/used\_bytes |
| k8s\_node/default\_metrics | Bytes received | Byte | kubernetes.io/node/network/received\_bytes\_count |
| k8s\_node/default\_metrics | Bytes transmitted | Byte | kubernetes.io/node/network/sent\_bytes\_count |
| k8s\_node/default\_metrics | PID capacity | Count | kubernetes.io/node/pid\_limit |
| k8s\_node/default\_metrics | PID usage | Count | kubernetes.io/node/pid\_used |
| k8s\_node/default\_metrics | CPU usage time | Second | kubernetes.io/node\_daemon/cpu/core\_usage\_time |
| k8s\_node/default\_metrics | Memory usage | Byte | kubernetes.io/node\_daemon/memory/used\_bytes |
| k8s\_pod/default\_metrics | Bytes received | Byte | kubernetes.io/pod/network/received\_bytes\_count |
| k8s\_pod/default\_metrics | Bytes transmitted | Byte | kubernetes.io/pod/network/sent\_bytes\_count |
| k8s\_pod/default\_metrics | Volume capacity | Byte | kubernetes.io/pod/volume/total\_bytes |
| k8s\_pod/default\_metrics | Volume usage | Byte | kubernetes.io/pod/volume/used\_bytes |
| k8s\_pod/default\_metrics | Volume utilization | Count | kubernetes.io/pod/volume/utilization |
| k8s\_pod/istio | Client Connection Close Count | Byte | istio.io/service/client/connection\_close\_count |
| k8s\_pod/istio | Client Connection Open Count | Byte | istio.io/service/client/connection\_open\_count |
| k8s\_pod/istio | Client Received Bytes Count | Byte | istio.io/service/client/received\_bytes\_count |
| k8s\_pod/istio | Client Request Bytes | Byte | istio.io/service/client/request\_bytes |
| k8s\_pod/istio | Client Request Count | Count | istio.io/service/client/request\_count |
| k8s\_pod/istio | Client Response Bytes | Byte | istio.io/service/client/response\_bytes |
| k8s\_pod/istio | Client Roundtrip Latencies | MilliSecond | istio.io/service/client/roundtrip\_latencies |
| k8s\_pod/istio | Client Sent Bytes Count | Byte | istio.io/service/client/sent\_bytes\_count |
| k8s\_container/default\_metrics | CPU usage time | Second | kubernetes.io/container/cpu/core\_usage\_time |
| k8s\_container/default\_metrics | Limit cores | Unspecified | kubernetes.io/container/cpu/limit\_cores |
| k8s\_container/default\_metrics | CPU limit utilization | Count | kubernetes.io/container/cpu/limit\_utilization |
| k8s\_container/default\_metrics | Request cores | Unspecified | kubernetes.io/container/cpu/request\_cores |
| k8s\_container/default\_metrics | CPU request utilization | Count | kubernetes.io/container/cpu/request\_utilization |
| k8s\_container/default\_metrics | Ephemeral storage limit | Byte | kubernetes.io/container/ephemeral\_storage/limit\_bytes |
| k8s\_container/default\_metrics | Ephemeral storage request | Byte | kubernetes.io/container/ephemeral\_storage/request\_bytes |
| k8s\_container/default\_metrics | Ephemeral storage usage | Byte | kubernetes.io/container/ephemeral\_storage/used\_bytes |
| k8s\_container/default\_metrics | Memory limit | Byte | kubernetes.io/container/memory/limit\_bytes |
| k8s\_container/default\_metrics | Memory limit utilization | Count | kubernetes.io/container/memory/limit\_utilization |
| k8s\_container/default\_metrics | Page faults | Count | kubernetes.io/container/memory/page\_fault\_count |
| k8s\_container/default\_metrics | Memory request | Byte | kubernetes.io/container/memory/request\_bytes |
| k8s\_container/default\_metrics | Memory request utilization | Count | kubernetes.io/container/memory/request\_utilization |
| k8s\_container/default\_metrics | Memory usage | Byte | kubernetes.io/container/memory/used\_bytes |
| k8s\_container/default\_metrics | Restart count | Count | kubernetes.io/container/restart\_count |
| k8s\_container/default\_metrics | Uptime | Second | kubernetes.io/container/uptime |
| k8s\_container/agent | Monitoring Agent API Request Count | Count | agent.googleapis.com/agent/api\_request\_count |
| k8s\_container/agent | Logging Agent Log Entry Count | Count | agent.googleapis.com/agent/log\_entry\_count |
| k8s\_container/agent | Logging Agent Retried Log Entry Writes Count | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| k8s\_container/agent | Monitoring Agent Memory Usage | Byte | agent.googleapis.com/agent/memory\_usage |
| k8s\_container/agent | Monitoring Agent Metric Point Count | Count | agent.googleapis.com/agent/monitoring/point\_count |
| k8s\_container/agent | Logging Agent API Request Count | Count | agent.googleapis.com/agent/request\_count |
| k8s\_container/agent | Monitoring Agent Process Labels Size | Byte | agent.googleapis.com/agent/streamspace\_size |
| k8s\_container/agent | Monitoring Agent is Throttling Processes | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| k8s\_container/agent | Monitoring/Logging Agent Uptime | Second | agent.googleapis.com/agent/uptime |
| k8s\_container/apigee | Apigee Cassandra client request latency | Count | apigee.googleapis.com/cassandra/clientrequest\_latency |
| k8s\_container/apigee | Apigee Cassandra pending compaction tasks | Count | apigee.googleapis.com/cassandra/compaction\_pendingtasks |
| k8s\_container/apigee | Apigee Cassandra bytes committed per area | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_committed |
| k8s\_container/apigee | Apigee Cassandra initial memory bytes | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_init |
| k8s\_container/apigee | Apigee Cassandra max bytes of memory | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_max |
| k8s\_container/apigee | Apigee Cassandra used JVM memory bytes | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_used |
| k8s\_container/apigee | Apigee Cassandra bytes committed per memory pool | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_committed |
| k8s\_container/apigee | Apigee Cassandra initial bytes of JVM memory pool | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_init |
| k8s\_container/apigee | Apigee Cassandra JVM memory pool bytes max | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_max |
| k8s\_container/apigee | Apigee Cassandra bytes per memory pool | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_used |
| k8s\_container/apigee | Apigee Cassandra user and system CPU in seconds | Second | apigee.googleapis.com/cassandra/process\_cpu\_seconds\_total |
| k8s\_container/apigee | Apigee Cassandra process max file descriptors | Count | apigee.googleapis.com/cassandra/process\_max\_fds |
| k8s\_container/apigee | Apigee Cassandra process open file descriptors | Count | apigee.googleapis.com/cassandra/process\_open\_fds |
| k8s\_container/apigee | Apigee server fault count | Count | apigee.googleapis.com/server/fault\_count |
| k8s\_container/apigee | Apigee server latencies | MilliSecond | apigee.googleapis.com/server/latencies |
| k8s\_container/apigee | Apigee server nio | Count | apigee.googleapis.com/server/nio |
| k8s\_container/apigee | Apigee server thread count | Count | apigee.googleapis.com/server/num\_threads |
| k8s\_container/apigee | Apigee server request count | Count | apigee.googleapis.com/server/request\_count |
| k8s\_container/apigee | Apigee server response count | Count | apigee.googleapis.com/server/response\_count |
| k8s\_container/apigee | Apigee UDCA disk used bytes | Byte | apigee.googleapis.com/udca/disk/used\_bytes |
| k8s\_container/apigee | Apigee UDCA server local file count | Count | apigee.googleapis.com/udca/server/local\_file\_count |
| k8s\_container/apigee | Apigee UDCA server timestamp difference between current time and latest file | Second | apigee.googleapis.com/udca/server/local\_file\_latest\_ts |
| k8s\_container/apigee | Apigee UDCA server timestamp difference between current time and oldest file | Second | apigee.googleapis.com/udca/server/local\_file\_oldest\_ts |
| k8s\_container/apigee | Apigee UDCA pruned file count | Count | apigee.googleapis.com/udca/server/pruned\_file\_count |
| k8s\_container/apigee | Apigee UDCA outstanding number of entries in retry cache | Count | apigee.googleapis.com/udca/server/retry\_cache\_size |
| k8s\_container/apigee | Apigee UDCA server total latencies | Second | apigee.googleapis.com/udca/server/total\_latencies |
| k8s\_container/apigee | Apigee UDCA server upload latencies | Second | apigee.googleapis.com/udca/server/upload\_latencies |
| k8s\_container/apigee | Apigee UDCA server HTTP error count | Count | apigee.googleapis.com/udca/upstream/http\_error\_count |
| k8s\_container/apigee | Apigee UDCA server HTTP latencies | Second | apigee.googleapis.com/udca/upstream/http\_latencies |
| k8s\_container/apigee | Apigee UDCA uploaded file count | Count | apigee.googleapis.com/udca/upstream/uploaded\_file\_count |
| k8s\_container/apigee | Apigee UDCA uploaded file size distribution | Byte | apigee.googleapis.com/udca/upstream/uploaded\_file\_sizes |
| k8s\_container/apigee | Apigee upstream latencies | MilliSecond | apigee.googleapis.com/upstream/latencies |
| k8s\_container/apigee | Apigee upstream request count | Count | apigee.googleapis.com/upstream/request\_count |
| k8s\_container/apigee | Apigee upstream response count | Count | apigee.googleapis.com/upstream/response\_count |
| k8s\_container/istio | Config Convergence Latencies | MilliSecond | istio.io/control/config\_convergence\_latencies |
| k8s\_container/istio | Config Event Count | Count | istio.io/control/config\_event\_count |
| k8s\_container/istio | Config Push Count | Count | istio.io/control/config\_push\_count |
| k8s\_container/istio | Config Validation Count | Count | istio.io/control/config\_validation\_count |
| k8s\_container/istio | Proxy Clients | Count | istio.io/control/proxy\_clients |
| k8s\_container/istio | Rejected Config Count | Count | istio.io/control/rejected\_config\_count |
| k8s\_container/istio | Sidecar Injection Count | Count | istio.io/control/sidecar\_injection\_count |
| k8s\_container/istio | Server Connection Close Count | Byte | istio.io/service/server/connection\_close\_count |
| k8s\_container/istio | Server Connection Open Count | Byte | istio.io/service/server/connection\_open\_count |
| k8s\_container/istio | Server Received Bytes Count | Byte | istio.io/service/server/received\_bytes\_count |
| k8s\_container/istio | Server Request Bytes | Byte | istio.io/service/server/request\_bytes |
| k8s\_container/istio | Server Request Count | Count | istio.io/service/server/request\_count |
| k8s\_container/istio | Server Response Bytes | Byte | istio.io/service/server/response\_bytes |
| k8s\_container/istio | Server Response Latencies | MilliSecond | istio.io/service/server/response\_latencies |
| k8s\_container/istio | Server Sent Bytes Count | Byte | istio.io/service/server/sent\_bytes\_count |
| k8s\_container/nginx | Nginx connections\_accepted | Unspecified | kubernetes.io/nginx/connections\_accepted |
| k8s\_container/nginx | Nginx connections\_active | Unspecified | kubernetes.io/nginx/connections\_active |
| k8s\_container/nginx | Nginx connections\_handled | Unspecified | kubernetes.io/nginx/connections\_handled |
| k8s\_container/nginx | Nginx connections\_reading | Unspecified | kubernetes.io/nginx/connections\_reading |
| k8s\_container/nginx | Nginx connections\_waiting | Unspecified | kubernetes.io/nginx/connections\_waiting |
| k8s\_container/nginx | Nginx connections\_writing | Unspecified | kubernetes.io/nginx/connections\_writing |
| k8s\_container/nginx | Nginx http\_requests\_total | Unspecified | kubernetes.io/nginx/http\_requests\_total |
| k8s\_container/nginx | Nginx nginxexporter\_build\_info | Count | kubernetes.io/nginx/nginxexporter\_build\_info |
| k8s\_container/nginx | Nginx up | Count | kubernetes.io/nginx/up |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")