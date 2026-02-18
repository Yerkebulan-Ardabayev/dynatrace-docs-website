---
title: NetApp on Google Cloud monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-netapp-monitoring
scraped: 2026-02-18T05:47:30.764792
---

# NetApp on Google Cloud monitoring

# NetApp on Google Cloud monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
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

The following feature sets are available for NetApp on Google Cloud.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| netapp\_cloud\_volume/default\_metrics | Volume inode allocation | Unspecified | netapp.com/cloudvolume/inode\_allocation |
| netapp\_cloud\_volume/default\_metrics | Volume inode usage | Unspecified | netapp.com/cloudvolume/inode\_usage |
| netapp\_cloud\_volume/default\_metrics | Operations count | Count | netapp.com/cloudvolume/operation\_count |
| netapp\_cloud\_volume/default\_metrics | Bytes read | Byte | netapp.com/cloudvolume/read\_bytes\_count |
| netapp\_cloud\_volume/default\_metrics | Volume IO operation latency | MilliSecond | netapp.com/cloudvolume/request\_latencies |
| netapp\_cloud\_volume/default\_metrics | Volume space allocation | Byte | netapp.com/cloudvolume/volume\_size |
| netapp\_cloud\_volume/default\_metrics | Volume space usage | Byte | netapp.com/cloudvolume/volume\_usage |
| netapp\_cloud\_volume/default\_metrics | Bytes written | Byte | netapp.com/cloudvolume/write\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Logical Bytes Backed Up | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/logical\_bytes\_backed\_up |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Operation Count | Count | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/operation\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Read Bytes Count | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/read\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Request Latencies | MilliSecond | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/request\_latencies |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Volume Size | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_size |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Volume Usage | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_usage |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Write Bytes Count | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/write\_bytes\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")