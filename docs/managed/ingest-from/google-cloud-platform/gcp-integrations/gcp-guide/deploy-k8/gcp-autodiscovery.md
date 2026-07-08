---
title: Monitor Google Cloud projects using auto-discovery
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery
---

# Monitor Google Cloud projects using auto-discovery

# Monitor Google Cloud projects using auto-discovery

* How-to guide
* 6-min read
* Published Sep 25, 2023
* Early Access

Starting from the Google Cloud Monitor integration version 1.3.0+, you can extend your metric coverage beyond the predefined set of services supported by extensions.

* For a complete list of supported services, see [Google Cloud supported service metrics](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.").
* To monitor any metric from any Google resource not covered by those services, follow the instructions on this page to activate auto-discovery.

Possible auto-discovery scenarios depend on the services from which you want to monitor metrics:

* Expand metrics for already supported services
* Integrate any service based on the resource name

## Before you begin

This guide is a component of the main [Dynatrace Google Cloud Metric and Log Integration setup](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."), and focuses solely on auto-discovery configuration.

### Minimum version

If Google Cloud integration has been previously set up using a version earlier than 1.3.0, you need to run a fresh deployment of the complete solution using version 1.3.0+.

### Set up auto-discovery monitoring

#### Ensure permissions

If you are managing permissions manually, ensure the following permissions are added to the Dynatrace Google Cloud Metrics Monitor role.

* `monitoring.metricDescriptors.list`
* `monitoring.monitoredResourceDescriptors.get`
* `monitoring.monitoredResourceDescriptors.list`

#### Enable auto-discovery metric enrichment

To enable the auto-discovery metric enrichment, edit the following parameter in `values.yaml`:

```
metricAutodiscovery: "true"
```

## Expand metrics for already supported services

Within the scope of standard supported services, a predetermined set of metrics is routinely sent to Dynatrace. For details on how to enable those services, see [Choose services for metrics monitoring](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#services-metrics "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Auto-discovery mode, however, brings more flexibility by allowing the collection of all available metrics for a particular service.

### Enable auto-discovery

To enable it, you need to modify the `values.yaml` file by searching for the specific service as follows:

```
- service: cloud_service_name



allowAutodiscovery: True
```

### Supported services

Expand the following table for a list of resources currently monitored by supported services that can be extended with auto-discovery.

### Dynatrace Google Cloud supported services

| Monitored resource | Service name |
| --- | --- |
| alloydb.googleapis.com/Database | Google AlloyDB |
| alloydb.googleapis.com/Instance | Google AlloyDB |
| api | Google Cloud APIs |
| apigee.googleapis.com/Environment | Google Apigee |
| apigee.googleapis.com/Proxy | Google Apigee |
| apigee.googleapis.com/ProxyV2 | Google Apigee |
| apigee.googleapis.com/TargetV2 | Google Apigee |
| assistant\_action\_project | Google Assistant Smart Home |
| autoscaler | Google Compute Engine |
| aws\_ec2\_instance | Google Compute Engine |
| baremetalsolution.googleapis.com/Instance | Google Compute Engine |
| bigquery\_biengine\_model | Google BigQuery |
| bigquery\_project | Google BigQuery |
| bigtable\_cluster | Google Cloud Bigtable |
| bigtable\_table | Google Cloud Bigtable |
| cloud\_composer\_environment | Google Cloud Composer |
| cloud\_dataproc\_cluster | Google Dataproc |
| cloud\_dlp\_project | Google Cloud Data Loss Prevention |
| cloud\_function | Google Cloud Functions |
| cloud\_run\_job | Google Cloud Run |
| cloud\_run\_revision | Google Cloud Run |
| cloud\_tasks\_queue | Google Cloud Tasks |
| cloudiot\_device\_registry | Google Cloud IoT Core |
| cloudml\_job | Google AI Platform |
| cloudml\_model\_version | Google AI Platform |
| cloudsql\_database | Google Cloud SQL |
| cloudsql\_instance\_database | Google Cloud SQL |
| cloudvolumesgcp-api.netapp.com/CloudVolume | NetApp on Google Cloud |
| consumed\_api | Google Cloud APIs |
| consumer\_quota | Google Cloud APIs |
| dataflow\_job | Google Dataflow |
| datastore\_request | Google Firestore in Datastore mode |
| dns\_query | Google Cloud DNS |
| filestore\_instance | Google Cloud Filestore |
| firebase\_domain | Google Firebase |
| firebase\_namespace | Google Firebase |
| firestore.googleapis.com/Database | Google Cloud Filestore |
| firestore\_instance | Google Cloud Filestore |
| gae\_app | Google App Engine |
| gae\_instance | Google App Engine |
| gce\_router | Google Hybrid Connectivity |
| gce\_zone\_network\_health | Google Network Topology |
| gcs\_bucket | Google Cloud Storage |
| https\_lb\_rule | Google Cloud Load Balancing |
| instance\_group | Google Compute Engine |
| interconnect | Google Hybrid Connectivity |
| interconnect\_attachment | Google Hybrid Connectivity |
| internal\_http\_lb\_rule | Google Cloud Load Balancing |
| internal\_tcp\_lb\_rule | Google Cloud Load Balancing |
| internal\_udp\_lb\_rule | Google Cloud Load Balancing |
| istio\_control\_plane | Google Kubernetes Engine |
| k8s\_container | Google Kubernetes Engine |
| k8s\_node | Google Kubernetes Engine |
| k8s\_pod | Google Kubernetes Engine |
| loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule | Google Cloud Load Balancing |
| microsoft\_ad\_domain | Google Managed Microsoft AD |
| nat\_gateway | Google Cloud Router |
| netapp\_cloud\_volume | NetApp on Google Cloud |
| network\_security\_policy | Google Network Security |
| produced\_api | Google Cloud APIs |
| producer\_quota | Google Cloud APIs |
| pubsub\_snapshot | Google Pub/Sub |
| pubsub\_subscription | Google Pub/Sub |
| pubsub\_topic | Google Pub/Sub |
| pubsublite\_subscription\_partition | Google Pub/Sub Lite |
| pubsublite\_topic\_partition | Google Pub/Sub Lite |
| recaptchaenterprise.googleapis.com/Key | Google reCAPTCHA Enterprise |
| redis\_instance | Google Memorystore |
| spanner\_instance | Google Cloud Spanner |
| tcp\_lb\_rule | Google Cloud Load Balancing |
| tcp\_ssl\_proxy\_rule | Google Cloud Load Balancing |
| tpu\_worker | Google Compute Engine |
| transfer\_service\_agent | Google Cloud Storage Transfer Service |
| udp\_lb\_rule | Google Cloud Load Balancing |
| vpc\_access\_connector | Google Virtual Private Cloud |
| vpn\_gateway | Google Hybrid Connectivity |

## Integrate any service based on resource name

For situations where the extended monitoring capabilities of supported services are insufficient, Google Cloud auto-discovery provides a solution to monitor any service offered by Google.

### Limitations

* Auto-discovery mode is designed to detect only metrics linked to a single resource.
* These metrics are not attached to any supported service, so there will be no entity or any enrichment extracted from them.

### Configure parameter values

The helm deployment package contains the `autodiscovery-values.yaml` file with the necessary configuration for this scenario. Edit this file to set the required and optional parameter values as follows.

| **Parameter name** | **Description** | **Default value** |
| --- | --- | --- |
| `autodiscoveryQueryInterval` | Required Auto-discovery polling interval in minutes. Minimum value: `60`. | `60` |
| `autodiscoveryIncludeAlphaMetrics` | Optional When set to `true`, it enables the automatic discovery of experimental Google Cloud metrics withthe 'Alpha' label. | `true` |
| `autodiscoveryAddLabels` | Optional When set to `true`, it appends the label `[Autodiscovered]` to metric names during automatic discovery. | `true` |
| `autodiscoveryResourcesYaml` | Optional Configuration file for auto-discovery resources. |  |
| `autodiscoveryBlockListYaml` | Optional Configuration file for auto-discovery metrics name prefixes that shoud not be included. |  |

### Select resources

Specify the metrics to be sent to Dynatrace by listing the resource types of the monitored resources in the `autodiscoveryResourcesYaml` section. To identify the resources for monitoring within your project, see [Google Cloud metrics﻿](https://dt-url.net/th03qct).

Example:

```
autodiscoveryResourcesYaml: |



autodicovery_config:



searched_resources:



- memcache_node
```

### Disable selected metrics

To exclude specific metrics, list their prefixes in the `autodiscoveryBlockListYaml` section. Any matching metric will be excluded.

Example:

```
autodiscoveryBlockListYaml: |



block_list:



- memcache.googleapis.com/node/
```

## Related topics

* [Google Cloud integrations](/managed/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")
* [Monitor multiple Google Cloud projects](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.")