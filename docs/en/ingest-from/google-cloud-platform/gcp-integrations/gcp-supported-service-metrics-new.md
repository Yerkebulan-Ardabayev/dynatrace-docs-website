---
title: Google Cloud supported services
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new
scraped: 2026-02-15T21:14:17.362056
---

# Google Cloud supported services

# Google Cloud supported services

* Latest Dynatrace
* Overview
* 3-min read
* Updated on Sep 23, 2024

Dynatrace version 1.230+

This section refers to Google Cloud service metrics that are available with Google Cloud version 1.0 integration.

* For Google Cloud service metrics that are available with earlier versions of the Google Cloud integration, see [Google Cloud supported service metrics (legacy)](/docs/ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy "Supported GCP service metrics, metrics configuration, DDU consumption, and preset dashboard availability").

## Prerequisites

[Deploy Dynatrace integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Supported services for metrics

After deploying the Dynatrace integration, you can get insights into Google Cloud services metrics collected from the Google Operations API to ensure health of your cloud infrastructure.

Below, see the list of Google Cloud supported services.

Services

Supported entities[1](#fn-1-1-def)

Supported logs

Logs entities

[Google Cloud AI Platform monitoring (deprecated)](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-ai-platform-monitoring "Monitor Google Cloud AI Platform and view available metrics.")

cloudml\_job, cloudml\_model\_version

yes

cloudml\_job, cloudml\_model\_version

[Google Cloud AlloyDB monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-alloydb-monitoring "Monitor Google Cloud AlloyDB and view available metrics.")

alloydb\_database, alloydb\_instance

yes

alloydb\_database, alloydb\_instance

[Google Cloud APIs monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring "Monitor Google Cloud APIs and view available metrics.")

no

[Google Cloud Apigee monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apigee-monitoring "Monitor Google Cloud Apigee and view available metrics.")

apigee\_environment, apigee\_proxy, apigee\_target

no

[Google App Engine with Operations suite metrics monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring "Monitor Google App Engine and view available metrics.")

gae\_app

yes

gae\_app

[Google Cloud Assistant Smart Home monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-assistant-smart-home-monitoring "Monitor Google Cloud Assistant Smart Home and view available metrics.")

no

[Google BigQuery monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring "Monitor Google BigQuery and view available metrics.")

bigquery\_bigengine\_model

no

[Google Cloud Bigtable monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigtable-monitoring "Monitor Google Cloud Bigtable and view available metrics.")

bigtable\_cluster, bigtable\_table

no

[Google Cloud DNS monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-dns-monitoring "Monitor Google Cloud DNS and view available metrics.")

no

[Google Cloud Functions monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Monitor Google Cloud Functions and view available metrics.")

cloud\_function

yes

cloud\_function

[Google Cloud IoT Core monitoring (deprecated)](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-iot-core-monitoring "Monitor Google Cloud IoT Core and view available metrics.")

no

[Google Cloud Router monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-router-monitoring "Monitor Google Cloud Router and view available metrics.")

nat\_gateway

yes

nat\_gateway

[Google Cloud Run monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring "Monitor Google Cloud Run and view available metrics.")

cloud\_function, cloud\_run\_revision

yes

cloud\_run\_revision

[Google Cloud Storage monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring "Monitor Google Cloud Storage and view available metrics.")

gcs\_bucket

yes

gcs\_bucket

[Google Cloud Tasks monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-tasks-monitoring "Monitor Google Cloud Tasks and view available metrics.")

cloud\_tasks\_queue

yes

cloud\_tasks\_queue

[Google Cloud Composer monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-composer-monitoring "Monitor Google Cloud Composer and view available metrics.")

cloud\_composer\_environment

yes

cloud\_composer\_environment

[Google Compute Engine with Operations suite metrics monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring "Monitor Google Compute Engine and view available metrics.")

autoscaler, gce\_instance, instance\_group, tpu\_worker

yes

autoscaler, gce\_autoscaler, gce\_instance\_group, gce\_instance, tpu\_worker

[Google Cloud Data Loss Prevention monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-data-loss-prevention-monitoring "Monitor Google Cloud Data Loss Prevention (now part of Sensitive Data Protection) and view available metrics.")

no

[Google Cloud Storage Transfer Service monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-storage-transfer-service-monitoring "Monitor Google Cloud Storage Transfer Service and view available metrics.")

storage\_transfer\_job, transfer\_service\_agent

yes

storage\_transfer\_job

[Google Cloud Dataflow monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataflow-monitoring "Monitor Google Cloud Dataflow and view available metrics.")

no

[Google Cloud Dataproc monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataproc-monitoring "Monitor Google Cloud Dataproc and view available metrics.")

cloud\_dataproc\_cluster

yes

cloud\_dataproc\_cluster

[Google Cloud Firestore in Datastore mode monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring "Monitor Google Cloud Firestore in Datastore mode and view available metrics.")

no

[Google Cloud Filestore monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring "Monitor Google Filestore and view available metrics.")

filestore\_instance

no

[Google Cloud Firebase monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-firebase-monitoring "Monitor Google Cloud Firebase and view available metrics.")

no

[Google Cloud Firestore monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-firestore-monitoring "Monitor Google Cloud Firestore and view available metrics.")

firestore\_database

no

[Google Cloud Hybrid Connectivity monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-hybrid-connectivity-monitoring "Monitor Google Cloud Hybrid Connectivity and view available metrics.")

interconnect, interconnect\_attachment, gce\_router, vpn\_gateway

yes

gce\_router, vpn\_gateway

[Google Kubernetes Engine monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring "Monitor Google Kubernetes Engine and view available metrics.")

k8s\_cluster, k8s\_container, k8s\_node, k8s\_pod

yes

k8s\_cluster, k8s\_container, k8s\_node, k8s\_pod

[Google Cloud Load Balancing monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring "Monitor Google Cloud Load Balancing and view available metrics.")

https\_lb, internal\_http\_lb\_rule, internal\_network\_lb\_rule, network\_lb\_rule, tcp\_ssl\_proxy\_rule

yes

http\_load\_balancer, internal\_http\_lb\_rule, internal\_network\_lb\_rule, network\_lb\_rule, tcp\_ssl\_proxy\_rule

[Google Managed Microsoft AD monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-managed-microsoft-ad-monitoring "Monitor Google Managed Microsoft AD and view available metrics.")

microsoft\_ad\_domain

no

[Google Cloud Memorystore monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-memorystore-monitoring "Monitor Google Cloud Memorystore and view available metrics.")

redis\_instance

yes

redis\_instance

[NetApp on Google Cloud monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-netapp-monitoring "Monitor NetApp on Google Cloud and view available metrics.")

netapp\_volumes\_replication, netapp\_volumes\_storage\_pool, netapp\_volumes\_volume

no

[Google Cloud Network Security monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-security-monitoring "Monitor Google Cloud Network Security and view available metrics.")

network\_security\_policy

yes

network\_security\_policy

[Operations: Cloud Monitoring & Logging](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-operations-cloud-monitoring-and-logging "Monitor Google Cloud's operations suite and view available metrics.")

uptime\_url

yes

uptime\_url

[Google Cloud Pub/Sub monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring "Monitor Google Cloud Pub/Sub and view available metrics.")

pubsub\_snapshot, pubsub\_subscription, pubsub\_topic

yes

pubsub\_snapshot, pubsub\_subscription, pubsub\_topic

[Google Cloud Pub/Sub Lite monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring "Monitor Google Cloud Pub/Sub Lite and view available metrics.")

subscription\_partition, topic\_partition

no

[Google Cloud Spanner monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-spanner-monitoring "Monitor Google Cloud Spanner and view available metrics.")

spanner\_instance

yes

spanner\_instance

[Google Cloud SQL monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql "Monitor Google Cloud SQL and view available metrics.")

cloudsql\_database

yes

cloudsql\_database

[Google Cloud Virtual Private Cloud (VPC) monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-virtual-private-cloud-monitoring "Monitor Google Cloud Virtual Private Cloud (VPC) and view available metrics.")

vpc\_access\_connector

yes

vpc\_access\_connector

[Google Cloud Network Topology monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-topology-monitoring "Monitor Google Cloud Network Topology and view available metrics.")

no

[Google Vertex AI monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-vertex-ai "Monitor Google Cloud Vertex AI and view available metrics.")

vertex\_ai\_deployment\_resource\_pool,  
vertex\_ai\_endpoint,  
vertex\_ai\_feature\_online\_store,  
vertex\_ai\_feature\_store,  
vertex\_ai\_pipeline\_job,  
vertex\_ai\_index, vertex\_ai\_index\_endpoint,  
vertex\_ai\_publisher\_model,  
vision\_ai\_instance,  
vision\_ai\_stream

yes

vertex\_ai\_deployment\_resource\_pool,  
vertex\_ai\_endpoint,  
vertex\_ai\_feature\_store,  
vertex\_ai\_pipeline\_job,  
vertex\_ai\_index\_endpoint

1

Services might have one entity, several entities, or none. For each entity, you can see metrics, properties, logs, errors, and many more in Dynatrace [![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app "Monitor all cloud platforms at once.").

## Check available metrics

To check available metrics for a service, you need to

1. Find the extension in the [Hubï»¿](https://www.dynatrace.com/hub/?query=google&filter=all) and select it to open the overview page. See example: [Google Cloud Functionsï»¿](https://www.dynatrace.com/hub/detail/google-functions/?query=cloud+function&filter=all).
2. Scroll down to the bottom of the overview page of the extension to find the **Feature sets** section.
3. In the table, select the **default\_metrics** dropdown.
4. Now, you can check all available metrics for the chosen service.

## Monitoring consumption

### Metric ingestion

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

### Log ingestion

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")