---
title: Google Vertex AI monitoring
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-vertex-ai
scraped: 2026-05-12T11:51:15.199172
---

# Google Vertex AI monitoring

# Google Vertex AI monitoring

* How-to guide
* 6-min read
* Published Sep 30, 2024

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Vertex AI.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| vertexai\_deployment\_resource\_pool/default\_metrics | Accelerator duty cycle | Percent | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/accelerator/duty\_cycle |
| vertexai\_deployment\_resource\_pool/default\_metrics | Accelerator memory usage | Byte | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/accelerator/memory/bytes\_used |
| vertexai\_deployment\_resource\_pool/default\_metrics | CPU utilization | Percent | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/cpu/utilization |
| vertexai\_deployment\_resource\_pool/default\_metrics | Memory usage | Byte | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/memory/bytes\_used |
| vertexai\_deployment\_resource\_pool/default\_metrics | Network bytes received | Byte | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/network/received\_bytes\_count |
| vertexai\_deployment\_resource\_pool/default\_metrics | Network bytes sent | Byte | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/network/sent\_bytes\_count |
| vertexai\_deployment\_resource\_pool/default\_metrics | Replica count | Count | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/replicas |
| vertexai\_deployment\_resource\_pool/default\_metrics | Replica target | Count | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/target\_replicas |
| vertexai\_endpoint/default\_metrics | Accelerator duty cycle | Percent | aiplatform\_googleapis\_com/prediction/online/accelerator/duty\_cycle |
| vertexai\_endpoint/default\_metrics | Accelerator memory usage | Byte | aiplatform\_googleapis\_com/prediction/online/accelerator/memory/bytes\_used |
| vertexai\_endpoint/default\_metrics | CPU utilization | Percent | aiplatform\_googleapis\_com/prediction/online/cpu/utilization |
| vertexai\_endpoint/default\_metrics | Number of online prediction errors | Count | aiplatform\_googleapis\_com/prediction/online/error\_count |
| vertexai\_endpoint/default\_metrics | Memory usage | Byte | aiplatform\_googleapis\_com/prediction/online/memory/bytes\_used |
| vertexai\_endpoint/default\_metrics | Network bytes received | Byte | aiplatform\_googleapis\_com/prediction/online/network/received\_bytes\_count |
| vertexai\_endpoint/default\_metrics | Network bytes sent | Byte | aiplatform\_googleapis\_com/prediction/online/network/sent\_bytes\_count |
| vertexai\_endpoint/default\_metrics | Number of online predictions | Count | aiplatform\_googleapis\_com/prediction/online/prediction\_count |
| vertexai\_endpoint/default\_metrics | Prediction latencies | MilliSecond | aiplatform\_googleapis\_com/prediction/online/prediction\_latencies |
| vertexai\_endpoint/default\_metrics | Private endpoint prediction latencies | MilliSecond | aiplatform\_googleapis\_com/prediction/online/private/prediction\_latencies |
| vertexai\_endpoint/default\_metrics | Private endpoint response count | Count | aiplatform\_googleapis\_com/prediction/online/private/response\_count |
| vertexai\_endpoint/default\_metrics | Replica count | Count | aiplatform\_googleapis\_com/prediction/online/replicas |
| vertexai\_endpoint/default\_metrics | Response count | Count | aiplatform\_googleapis\_com/prediction/online/response\_count |
| vertexai\_endpoint/default\_metrics | Replica target | Count | aiplatform\_googleapis\_com/prediction/online/target\_replicas |
| vertexai\_feature\_online\_store/feature\_store | Request count | Count | aiplatform\_googleapis\_com/featureonlinestore/online\_serving/request\_count |
| vertexai\_feature\_online\_store/feature\_store | Response bytes count | Count | aiplatform\_googleapis\_com/featureonlinestore/online\_serving/serving\_bytes\_count |
| vertexai\_feature\_online\_store/feature\_store | Request latency | MilliSecond | aiplatform\_googleapis\_com/featureonlinestore/online\_serving/serving\_latencies |
| vertexai\_feature\_online\_store/feature\_store | Running sycs | Count | aiplatform\_googleapis\_com/featureonlinestore/running\_sync |
| vertexai\_feature\_online\_store/feature\_store | Serving data ages | Second | aiplatform\_googleapis\_com/featureonlinestore/serving\_data\_ages |
| vertexai\_feature\_online\_store/feature\_store | Serving data by synced time | Count | aiplatform\_googleapis\_com/featureonlinestore/serving\_data\_by\_sync\_time |
| vertexai\_feature\_online\_store/feature\_store | CPU load | Percent | aiplatform\_googleapis\_com/featureonlinestore/storage/bigtable\_cpu\_load |
| vertexai\_feature\_online\_store/feature\_store | CPU load (hottest node) | Percent | aiplatform\_googleapis\_com/featureonlinestore/storage/bigtable\_cpu\_load\_hottest\_node |
| vertexai\_feature\_online\_store/feature\_store | Node count | Count | aiplatform\_googleapis\_com/featureonlinestore/storage/bigtable\_nodes |
| vertexai\_feature\_online\_store/feature\_store | Optimized node count | Count | aiplatform\_googleapis\_com/featureonlinestore/storage/optimized\_nodes |
| vertexai\_feature\_online\_store/feature\_store | Bytes stored | Byte | aiplatform\_googleapis\_com/featureonlinestore/storage/stored\_bytes |
| vertexai\_feature\_store/feature\_store | CPU load | Percent | aiplatform\_googleapis\_com/featurestore/cpu\_load |
| vertexai\_feature\_store/feature\_store | CPU load (hottest node) | Percent | aiplatform\_googleapis\_com/featurestore/cpu\_load\_hottest\_node |
| vertexai\_feature\_store/feature\_store | Node count | Count | aiplatform\_googleapis\_com/featurestore/node\_count |
| vertexai\_feature\_store/feature\_store | Entities updated on the Featurestore online storage | Byte | aiplatform\_googleapis\_com/featurestore/online\_entities\_updated |
| vertexai\_feature\_store/feature\_store | Latencies | MilliSecond | aiplatform\_googleapis\_com/featurestore/online\_serving/latencies |
| vertexai\_feature\_store/feature\_store | Request size | Byte | aiplatform\_googleapis\_com/featurestore/online\_serving/request\_bytes\_count |
| vertexai\_feature\_store/feature\_store | Serving count | Count | aiplatform\_googleapis\_com/featurestore/online\_serving/request\_count |
| vertexai\_feature\_store/feature\_store | Response size | Byte | aiplatform\_googleapis\_com/featurestore/online\_serving/response\_size |
| vertexai\_feature\_store/feature\_store | Billable bytes | Byte | aiplatform\_googleapis\_com/featurestore/storage/billable\_processed\_bytes |
| vertexai\_feature\_store/feature\_store | Bytes stored | Byte | aiplatform\_googleapis\_com/featurestore/storage/stored\_bytes |
| vertexai\_feature\_store/feature\_store | Offline storage write for streaming write | Count | aiplatform\_googleapis\_com/featurestore/streaming\_write/offline\_processed\_count |
| vertexai\_feature\_store/feature\_store | Streaming write to offline storage delay time | Second | aiplatform\_googleapis\_com/featurestore/streaming\_write/offline\_write\_delays |
| vertexai\_location/default\_metrics | Executing PipelineJobs | Count | aiplatform\_googleapis\_com/executing\_vertexai\_pipeline\_jobs |
| vertexai\_location/default\_metrics | Executing PipelineTasks | Count | aiplatform\_googleapis\_com/executing\_vertexai\_pipeline\_tasks |
| vertexai\_location/default\_metrics | Generate content requests per minute per project per base model | Count | aiplatform\_googleapis\_com/generate\_content\_requests\_per\_minute\_per\_project\_per\_base\_model |
| vertexai\_location/default\_metrics | Online prediction dedicated requests per base model version | Count | aiplatform\_googleapis\_com/online\_prediction\_dedicated\_requests\_per\_base\_model\_version |
| vertexai\_location/default\_metrics | Online prediction dedicated tokens per minute per base model version | Count | aiplatform\_googleapis\_com/online\_prediction\_dedicated\_tokens\_per\_base\_model\_version |
| vertexai\_location/default\_metrics | Online prediction requests per base model | Count | aiplatform\_googleapis\_com/online\_prediction\_requests\_per\_base\_model |
| vertexai\_location/default\_metrics | Online prediction tokens per minute per base model | Count | aiplatform\_googleapis\_com/online\_prediction\_tokens\_per\_minute\_per\_base\_model |
| vertexai\_location/default\_metrics | Generate content requests per minute per project per base model quota exceeded error | Count | aiplatform\_googleapis\_com/quota/generate\_content\_requests\_per\_minute\_per\_project\_per\_base\_model/exceeded |
| vertexai\_location/default\_metrics | Generate content requests per minute per project per base model quota limit | Count | aiplatform\_googleapis\_com/quota/generate\_content\_requests\_per\_minute\_per\_project\_per\_base\_model/limit |
| vertexai\_location/default\_metrics | Generate content requests per minute per project per base model quota usage | Count | aiplatform\_googleapis\_com/quota/generate\_content\_requests\_per\_minute\_per\_project\_per\_base\_model/usage |
| vertexai\_location/default\_metrics | Online prediction dedicated requests per base model version quota exceeded error | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_requests\_per\_base\_model\_version/exceeded |
| vertexai\_location/default\_metrics | Online prediction dedicated requests per base model version quota limit | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_requests\_per\_base\_model\_version/limit |
| vertexai\_location/default\_metrics | Online prediction dedicated requests per base model version quota usage | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_requests\_per\_base\_model\_version/usage |
| vertexai\_location/default\_metrics | Online prediction dedicated tokens per minute per base model version quota exceeded error | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_tokens\_per\_base\_model\_version/exceeded |
| vertexai\_location/default\_metrics | Online prediction dedicated tokens per minute per base model version quota limit | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_tokens\_per\_base\_model\_version/limit |
| vertexai\_location/default\_metrics | Online prediction dedicated tokens per minute per base model version quota usage | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_tokens\_per\_base\_model\_version/usage |
| vertexai\_location/default\_metrics | Online prediction requests per base model quota exceeded | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_requests\_per\_base\_model/exceeded |
| vertexai\_location/default\_metrics | Online prediction requests per base model quota limit | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_requests\_per\_base\_model/limit |
| vertexai\_location/default\_metrics | Online prediction requests per base model quota usage | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_requests\_per\_base\_model/usage |
| vertexai\_location/default\_metrics | Online prediction tokens per minute per base model quota exceeded | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_tokens\_per\_minute\_per\_base\_model/exceeded |
| vertexai\_location/default\_metrics | Online prediction tokens per minute per base model quota limit | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_tokens\_per\_minute\_per\_base\_model/limit |
| vertexai\_location/default\_metrics | Online prediction tokens per minute per base model quota usage | Count | aiplatform\_googleapis\_com/quota/online\_prediction\_tokens\_per\_minute\_per\_base\_model/usage |
| vertexai\_pipeline\_job/pipelines | PipelineJob duration | Second | aiplatform\_googleapis\_com/pipelinejob/duration |
| vertexai\_pipeline\_job/pipelines | Completed PipelineTasks | Count | aiplatform\_googleapis\_com/pipelinejob/task\_completed\_count |
| vertexai\_index/vector\_search | Datapoint count | Count | aiplatform\_googleapis\_com/matching\_engine/stream\_update/datapoint\_count |
| vertexai\_index/vector\_search | Stream update latencies | MilliSecond | aiplatform\_googleapis\_com/matching\_engine/stream\_update/latencies |
| vertexai\_index/vector\_search | Request count | Count | aiplatform\_googleapis\_com/matching\_engine/stream\_update/request\_count |
| vertexai\_index\_endpoint/vector\_search | CPU request utilization | Percent | aiplatform\_googleapis\_com/matching\_engine/cpu/request\_utilization |
| vertexai\_index\_endpoint/vector\_search | Current replicas | Count | aiplatform\_googleapis\_com/matching\_engine/current\_replicas |
| vertexai\_index\_endpoint/vector\_search | Current shards | Count | aiplatform\_googleapis\_com/matching\_engine/current\_shards |
| vertexai\_index\_endpoint/vector\_search | Memory usage | Byte | aiplatform\_googleapis\_com/matching\_engine/memory/used\_bytes |
| vertexai\_index\_endpoint/vector\_search | Request latency | MilliSecond | aiplatform\_googleapis\_com/matching\_engine/query/latencies |
| vertexai\_index\_endpoint/vector\_search | Request count | Count | aiplatform\_googleapis\_com/matching\_engine/query/request\_count |
| vertexai\_publisher\_model/default\_metrics | Character count | Count | aiplatform\_googleapis\_com/publisher/online\_serving/character\_count |
| vertexai\_publisher\_model/default\_metrics | Characters | Count | aiplatform\_googleapis\_com/publisher/online\_serving/characters |
| vertexai\_publisher\_model/default\_metrics | Character Throughput | Count | aiplatform\_googleapis\_com/publisher/online\_serving/consumed\_throughput/count |
| vertexai\_publisher\_model/default\_metrics | First token latencies | MilliSecond | aiplatform\_googleapis\_com/publisher/online\_serving/first\_token\_latencies |
| vertexai\_publisher\_model/default\_metrics | Model invocation count | Count | aiplatform\_googleapis\_com/publisher/online\_serving/model\_invocation\_count |
| vertexai\_publisher\_model/default\_metrics | Model invocation latencies | MilliSecond | aiplatform\_googleapis\_com/publisher/online\_serving/model\_invocation\_latencies |
| vertexai\_publisher\_model/default\_metrics | Token count | Count | aiplatform\_googleapis\_com/publisher/online\_serving/token\_count |
| vertexai\_publisher\_model/default\_metrics | Tokens | Count | aiplatform\_googleapis\_com/publisher/online\_serving/tokens |
| visionai\_instance/vision\_ai | Request count | Count | visionai\_googleapis\_com/platform/connected\_service/request\_count |
| visionai\_instance/vision\_ai | Request latencies | MilliSecond | visionai\_googleapis\_com/platform/connected\_service/request\_latencies |
| visionai\_instance/vision\_ai | Prediction count | Count | visionai\_googleapis\_com/platform/custom\_model/predict\_count |
| visionai\_instance/vision\_ai | Prediction latencies | MilliSecond | visionai\_googleapis\_com/platform/custom\_model/predict\_latencies |
| visionai\_instance/vision\_ai | Uptime | MilliSecond | visionai\_googleapis\_com/platform/instance/uptime |
| visionai\_stream/vision\_ai | Received bytes | Byte | visionai\_googleapis\_com/stream/network/received\_bytes\_count |
| visionai\_stream/vision\_ai | Received packets | Count | visionai\_googleapis\_com/stream/network/received\_packets\_count |
| visionai\_stream/vision\_ai | Sent bytes | Byte | visionai\_googleapis\_com/stream/network/sent\_bytes\_count |
| visionai\_stream/vision\_ai | Sent packets | Count | visionai\_googleapis\_com/stream/network/sent\_packets\_count |

## Related topics

* [Google Cloud integrations](/managed/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")