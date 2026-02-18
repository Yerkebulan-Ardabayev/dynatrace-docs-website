---
title: Migrate to Google Cloud integration version 1.0
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function
scraped: 2026-02-18T05:48:13.646174
---

# Migrate to Google Cloud integration version 1.0

# Migrate to Google Cloud integration version 1.0

* Latest Dynatrace
* How-to guide
* 5-min read
* Published Jan 17, 2022

Dynatrace version 1.230+

The new version of the Google Cloud integration (v.1.0) uses [Extensions 2.0](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") and introduces [custom topology](/docs/ingest-from/extend-dynatrace/extend-topology/custom-topology "Learn how to create a custom topology model that's suited to your telemetry data.") for a number of Google Cloud services.

List of services with custom topology

* Google Compute Engine
* Google Cloud Storage
* Google Cloud Functions
* Google Cloud Run
* Google App Engine
* Google Cloud Tasks
* Google Cloud SQL
* Google Cloud Datastore
* Google Load Balancing
* Google Cloud NAT Gateway
* Google Filestore
* Google Kubernetes Engine
* Google Pub/Sub
* Google Pub/Sub Lite
* Google Memorystore
* Google Spanner

Note that your existing metric dimension names will change when you switch to Google Cloud integration using Dynatrace Extensions 2.0. Dimension name changes affect all configured managements zones, custom alerts, and custom dashboards in your environment. To restore proper functionality for these entities, please follow the instructions below.

Upgrading existing `dynatrace-gcp-monitor` installations from earlier versions is not supported. You need to first delete your existing deployment and then install the Google Cloud integration v.1.0. For instructions, see below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Delete existing deployment**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#delete-deployment "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Remove dashboards and/or alerts**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#remove-dashboards "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Install new Google Cloud deployment**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#install-deployment "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Update dimensions**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#update-dimensions "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.")

## Step 1 Delete existing deployment

For Kubernetes container deployment

For GC Function deployment

1. Find out what release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Uninstall the release.

   Be sure to replace `<release-name>` with the release name from the previous output.

   ```
   helm uninstall <release-name> -n dynatrace
   ```

1. Uninstall the release.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/uninstall.sh -O uninstall.sh ; chmod a+x uninstall.sh ; ./uninstall.sh
```

2. Remove the `activation-config.yaml` service configuration file.

## Step 2 Remove dashboards and/or alerts

You need to manually remove any dashboards or alerts created manually during the previous installation.

## Step 3 Install new Google Cloud deployment

To install the new Google Cloud deployment, see [Set up the Dynatrace Google Cloud metric and log integration (v.1.0) on a new GKE Autopilot cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

## Step 4 Update dimensions

If you created your own dashboards, alerts, or management zones based on Google Cloud metrics, you need to manually update the dimensions according to the list below in order to get links for entities.

### List of dimension changes

| Old dimension name | New dimension name |
| --- | --- |
| `project_id` | `gcp.project.id` |
| `region` | `gcp.region` |
| `zone` | `gcp.region` |
| `instance_id` | `gcp.instance.id` |
| `autoscaler_id` | `gcp.instance.id` |
| `model_id` | `gcp.instance.id` |
| `queue_id` | `gcp.instance.id` |
| `device_registry_id` | `gcp.instance.id` |
| `job_id` | `gcp.instance.id` |
| `version_id` | `gcp.instance.id` |
| `database_id` | `gcp.instance.id` |
| `volume_id` | `gcp.instance.id` |
| `router_id` | `gcp.instance.id` |
| `instance_group_id` | `gcp.instance.id` |
| `interconnect` | `gcp.instance.id` |
| `attachment` | `gcp.instance.id` |
| `volume_id` | `gcp.instance.id` |
| `snapshot_id` | `gcp.instance.id` |
| `subscription_id` | `gcp.instance.id` |
| `topic_id` | `gcp.instance.id` |
| `key_id` | `gcp.instance.id` |
| `worker_id` | `gcp.instance.id` |
| `agent_id` | `gcp.instance.id` |
| `gateway_id` | `gcp.instance.id` |
| `name` | `gcp.instance.name` |
| `autoscaler_name` | `gcp.instance.name` |
| `environment_name` | `gcp.instance.name` |
| `cluster_name gcp.instance.name` | `gcp.instance.name` |
| `function_name gcp.instance.name` | `gcp.instance.name` |
| `revision_name` | `gcp.instance.name` |
| `job_name` | `gcp.instance.name` |
| `instance_name` | `gcp.instance.name` |
| `domain_name` | `gcp.instance.name` |
| `table_name` | `gcp.instance.name` |
| `firewall_name` | `gcp.instance.name` |
| `bucket_name` | `gcp.instance.name` |
| `container_name` | `gcp.instance.name` |
| `url_map_name` | `gcp.instance.name` |
| `instance_group_name` | `gcp.instance.name` |
| `load_balancer_name` | `gcp.instance.name` |
| `canonical_service_name` | `gcp.instance.name` |
| `node_name` | `gcp.instance.name` |
| `pod_name` | `gcp.instance.name` |
| `broker_name` | `gcp.instance.name` |
| `revision_name` | `gcp.instance.name` |
| `trigger_name` | `gcp.instance.name` |
| `fqdn` | `gcp.instance.name` |
| `target_domain_name` | `gcp.instance.name` |
| `gateway_name` | `gcp.instance.name` |
| `policy_name` | `gcp.instance.name` |
| `proxy_name` | `gcp.instance.name` |
| `load_balancer_name` | `gcp.instance.name` |
| `backend_target_name` | `gcp.instance.name` |
| `connector_name` | `gcp.instance.name` |
| `gateway_name` | `gcp.instance.name` |

* To update dimensions for dashboards

  1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
  2. Select the dashboard for which you want to update dimensions, and then select **More** (**â¦**) > **Configure**.
  3. Select **Dashboard JSON**.
  4. In the `"splitBy"` section, replace the old dimensions with the new values as determined from the [list of dimension changes](#dimension).
  5. Select **Save changes**.

Alternatively, you can replace the dimensions by configuring each dashboard tile of a selected dashboard in Data Explorer.

* To update dimensions for alerts

  1. Go to **Settings**.
  2. Select **Anomaly detection** > **Metric events**.
  3. Select the event for which you want to update dimensions.
  4. In the **Add dimension filter** field, select the new dimension keys and enter the corresponding dimension values as determined from the [list of dimension changes](#dimension).
  5. Select **Save changes**.
* To update dimensions for management zones

  1. Go to **Settings**.
  2. Select **Preferences** > **Management zones**.
  3. Select **Edit** for the management zone for which you want to update dimensions.
  4. Select **Edit** to edit an existing rule.
  5. In **Conditions**, edit the `DIMENSION` value according to the [List of dimension changes](#dimension).
  6. Select **Save changes**.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")