---
title: Google Cloud supported service metrics (legacy)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy
scraped: 2026-02-23T21:34:33.027394
---

# Google Cloud supported service metrics (legacy)

# Google Cloud supported service metrics (legacy)

* Latest Dynatrace
* How-to guide
* 7-min read
* Published Apr 12, 2021
* Deprecated

This page refers to the GCP supported service metrics for version 0.1 of the GCP integration, which is scheduled for deprecation.
For a list of supported services and their metrics for version 1.0 of the GCP integration, see [Google Cloud service metrics (new)](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.").

Dynatrace supports all metrics available in the Google Operations API.

## Prerequisites

Deploy Dynatrace integration [as a GCP function](/docs/ingest-from/google-cloud-platform/legacy/deploy-with-google-cloud-function-legacy "Set up monitoring for Google Cloud services using a Google Cloud Function.") or [in a Kubernetes container](/docs/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Set up log and metric monitoring for GCP services in a Kubernetes container.").

## Supported services

After deploying the Dynatrace integration, you can start monitoring the GCP supported services. The table below shows available metrics configurations[1](#fn-1-1-def) per service, including [Davis data units (DDUs)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") consumption[2](#fn-1-2-def) per instance per minute.

1

**Metrics configuration** refers to groups of metrics that can be ingested. Use the **Configuration ID** when adjusting the monitoring scope of your setup.

2

**DDU consumption** is an estimation that may vary depending on characteristics of your environment. We recommend that you check your weekly DDU consumptions for more accurate budgeting.

| Service name | Preset dashboard | Configuration name | Configuration ID | DDUs per minute per instance |
| --- | --- | --- | --- | --- |
| Google Cloud Function | Applicable |  | cloud\_function/default | 0.073 DDU |
| Cloud SQL | Applicable | Database | cloudsql\_database/default | 0.066 DDU |
| Google Cloud APIs | Applicable |  | api/default | 0.086 DDU |
| Google Cloud Pub/Sub | Applicable | Snapshot | pubsub\_snapshot/default | 0.021 DDU |
|  |  | Subscription | pubsub\_subscription/default | 0.166 DDU |
|  |  | Topic | pubsub\_topic/default | 0.049 DDU |
| Google Pub/Sub Lite |  | Subscription Partition | pubsublite\_subscription\_partition/default | 0.006 DDU |
|  |  | Topic Partition | pubsublite\_topic\_partition/default | 0.013 DDU |
| Cloud Load Balancing | Applicable | Google Internal HTTP/S Load Balancing Rule | internal\_http\_lb\_rule/default | 0.405 DDU |
|  |  | Google Internal TCP Load Balancer Rule | internal\_tcp\_lb\_rule/default | 0.135 DDU |
|  |  | Google Internal UDP Load Balancer Rule | internal\_udp\_lb\_rule/default | 0.108 DDU |
|  |  | Google Cloud Network UDP Load Balancer Rule | udp\_lb\_rule/default | 0.036 DDU |
|  |  | Google Cloud HTTP/S Load Balancing Rule | https\_lb\_rule/default | 3.897 DDU |
|  |  | Google Cloud Network TCP Load Balancer Rule | tcp\_lb\_rule/default | 0.045 DDU |
|  |  | Google Cloud TCP/SSL Proxy Rule | tcp\_ssl\_proxy\_rule/default | 0.054 DDU |
| Google Kubernetes Engine | Applicable | Container Agent | k8s\_container/agent | 0.021 DDU |
|  |  | Container Apigee | k8s\_container/apigee | 0.268 DDU |
|  |  | Container NGINX | k8s\_container/nginx | 0.017 DDU |
|  |  | Container | k8s\_container/default | 0.024 DDU |
|  |  | Container | gke\_container/default | 0.109 DDU |
|  |  | Cluster | k8s\_cluster/default | 0.009 DDU |
|  |  | Node | k8s\_node/default | 0.039 DDU |
| Google Cloud Datastore | Applicable |  | datastore\_request/default | 0.025 DDU |
| Google Filestore | Applicable | Instance | filestore\_instance/default | 0.048 DDU |
| Google Cloud Storage | Applicable | bucket | gcs\_bucket/default | 0.185 DDU |
| Google VM Instance |  |  | gce\_instance/appenginee | 0.108 DDU |
|  |  | Instance | gce\_instance/default | 2.828 DDU |
|  |  | Agent | gce\_instance/agent | 2.794 DDU |
|  |  | Firewall Insights | gce\_instance/firewallinsights | 0.18 DDU |
|  |  | Google Cloud Router | gce\_router/default | 0.032 DDU |
|  |  | Google Zone Network Health | gce\_zone\_network\_health/default | 0.243 DDU |
|  |  | Uptime Checks | gce\_instance/uptime\_check | 2.187 DDU |
| Google Cloud Spanner |  | Instance | spanner\_instance/default | 0.223 DDU |
| Google Cloud BigQuery |  | BI Engine Model | bigquery\_biengine\_model/default | 0.055 DDU |
|  |  | Dataset | bigquery\_dataset/default | 0.147 DDU |
|  |  | Project | bigquery\_project/default | 0.085 DDU |
| Google Interconnect |  | Default | interconnect/default | 0.03 DDU |
|  |  | Attachment | interconnect\_attachment/default | 0.005 DDU |
| Google Cloud Memorystore |  | Instance | redis\_instance/default | 0.169 DDU |
| Google Apigee |  | Proxy (v2) | apigee.googleapis.com/ProxyV2/default | 0.246 DDU |
|  |  | Environment | apigee.googleapis.com/Environment/default | 0.027 DDU |
|  |  | Proxy | apigee.googleapis.com/Proxy/default | 0.207 DDU |
| Google Consumer Quota |  |  | consumer\_quota/default | 0.021 DDU |
| Google Cloud NAT Gateway |  |  | nat\_gateway/default | 0.04 DDU |
| Google Transfer Service Agent |  |  | transfer\_service\_agent/default | 0.002 DDU |
| Google Cloud DNS Query |  |  | dns\_query/default | 0.003 DDU |
| Google Cloud Run for Anthos Trigger |  |  | knative\_trigger/default | 0.57 DDU |
|  |  | Google Cloud Run for Anthos Broker | knative\_broker/default | 0.27 DDU |
|  |  | Google Cloud Run for Anthos Revision | knative\_revision/default | 0.547 DDU |
| Google Instance Group |  |  | instance\_group/default | 0.001 DDU |
| Google App Engine |  | Application - Uptime Checks | gae\_app\_uptime\_check/default | 2.916 DDU |
|  |  | Application | gae\_app/default | 0.101 DDU |
|  |  | Instance | gae\_instance/default | 0.005 DDU |
| Google Compute Engine Autoscaler |  | Google Autoscaler | autoscaler/default | 0.006 DDU |
| Google Dataflow |  | Job | dataflow\_job/default | 3.397 DDU |
| Google Network Security Policy |  |  | network\_security\_policy/default | 0.018 DDU |
| Google Cloud Logging |  | export sink | logging\_sink/default | 0.003 DDU |
| Google VPC Access Connector |  |  | vpc\_access\_connector/default | 0.004 DDU |
| Google Cloud ML |  | Job | cloudml\_job/default | 0.162 DDU |
|  |  | Model Version | cloudml\_model\_version/default | 0.038 DDU |
| Google Cloud Bigtable |  | Cluster | bigtable\_cluster/default | 0.018 DDU |
|  |  | Table | bigtable\_table/default | 0.111 DDU |
| Google Cloud Amazon EC2 Instance (via GCP) |  |  | cloud\_tasks\_queue/default | 0.014 DDU |
| Google Cloud Composer |  | Environment | cloud\_composer\_environment/default | 0.129 DDU |
| Google Cloud Data Loss Prevention |  | Project | cloud\_dlp\_project/default | 0.019 DDU |
| Google Cloud Dataproc |  | Cluster | cloud\_dataproc\_cluster/default | 0.081 DDU |
| Google Cloud Run Revision |  |  | cloud\_run\_revision/default | 0.059 DDU |
| Google Cloud Trace |  |  | cloudtrace.googleapis.com/CloudtraceProject/default | 0.003 DDU |
| Google Cloud TPU |  | Worker | tpu\_worker/default | 0.013 DDU |
| Google reCAPTCHA |  | Key | recaptchaenterprise.googleapis.com/Key/default | 0.003 DDU |
| Google Firestore |  | Instance | firestore\_instance/default | 0.324 DDU |
| Google NetApp CVS-SO |  |  | cloudvolumesgcp-api.netapp.com/NetAppCloudVolumeSO/default | 0.013 DDU |
| Google NetApp Cloud Volume |  |  | netapp\_cloud\_volume/default | 0.032 DDU |
| Google Assistant Smart Home |  | Google Assistant Action Project | assistant\_action\_project/default | 0.567 DDU |
| Google Firebase Hosting |  | Google Firebase Realtime Database | firebase\_namespace/default | 0.104 DDU |
|  |  | Site Domain | firebase\_domain/default | 1.921 DDU |
| Google Cloud IoT Registry |  |  | cloudiot\_device\_registry/default | 0.026 DDU |
| Google Consumed API |  |  | consumed\_api/default | 0.084 DDU |
| Google Cloud Microsoft Active Directory Domain |  |  | microsoft\_ad\_domain/default | 0.028 DDU |
| Google IAM Service Account |  |  | iam\_service\_account/default | 0.04 DDU |
| Google Producer Quota |  |  | producer\_quota/default | 0.012 DDU |
| Google Uptime Check URL |  |  | uptime\_url/default | 2.916 DDU |
| Google Cloud VPN Tunnel |  |  | vpn\_gatewayv/ | 0.09 DDU |

## View GCP service metrics

Dynatrace provides preset dashboards for a number of GCP services. You can see which GCP services have preset dashboards in the list of GCP supported services above.  
After deploying the Dynatrace integration, you can view these preset dashboards in ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.

**Example preset dashboard:**

![GCP dash](https://dt-cdn.net/images/gcp-api-dashboard-2744-cef7a39830.png)

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")