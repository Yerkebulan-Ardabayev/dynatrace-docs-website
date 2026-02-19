---
title: Manage Prometheus extensions
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions
scraped: 2026-02-19T21:28:59.900905
---

# Manage Prometheus extensions

# Manage Prometheus extensions

* Latest Dynatrace
* 4-min read
* Published Feb 01, 2022

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from a Prometheus endpoint. With it, you can bring the Prometheus data into Dynatrace at scale and in context with all other data.

* To take full advantage of the Dynatrace Prometheus extension, you need a OneAgent on the monitored box, but it can also work in an agentless manner.
* Check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=prometheus) to see if your technology is already covered by an existing extension. If this is not the case, you can easily build your own [Dynatrace Prometheus extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.").

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Before you begin**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#before-you-begin "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add extension to environment**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#add-extension "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Define monitoring source**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#define-monitoring-source "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Advanced properties**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#advanced-properties "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Autodiscovery**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#autodiscovery "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Activate extension**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#activate-extension "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")

## Step 1 Before you begin

Decide which of your hosts will provide the Prometheus data for the extension.

Prometheus extensions can run locally on a OneAgent (recommended) or remotely on an ActiveGate.

* When run locally, the extension connects to the Prometheus interface automatically. Make sure the Extension Execution Controller (EEC) is enabled at the environment or selected host level. For more information, see [Extension Execution Controller](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").
* When monitored remotely, the ActiveGates belonging to an ActiveGate group that you'll designate for remote monitoring need to be able to connect to the host where Prometheus metrics originate.

Required permission: **Change monitoring settings**

## Step 2 Add extension to environment

Dynatrace Hub provides a unified workflow to enable and manage extensions that ingest Prometheus data into your Dynatrace environment.

1. In Dynatrace Hub, search for a Prometheus extension. You can use the "Prometheus" keyword to filter results.
2. Select and install the extension you're interested in. This enables the extension in your monitoring environment.
3. Add a monitoring configuration so that the extension can begin collecting data.

## Step 3 Define monitoring source

Decide how you want to monitor your host: local or remote.

### Local monitoring

1. Select the host, host group or management zone for which you will run the extension, or choose to monitor the whole environment. The host needs to be running a OneAgent that is [enabled to run extensions](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").
2. Select **Next step**.
3. Select **Add endpoint**.
4. Define the Prometheus endpoint providing metrics and authentication details. For more information on supported authentication schemes, see [Authentication](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#authentication "Learn about Prometheus extensions in the Extensions framework."). Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

### Remote monitoring

1. Select **Monitor remotely**.
2. Define the Prometheus endpoint providing metrics and authentication details. For more information on supported authentication schemes, see [Authentication](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#authentication "Learn about Prometheus extensions in the Extensions framework.")
3. Select **Next step**.
4. Select the ActiveGate group to determine which ActiveGates will run the extension. When done, select **Next step**.

## Step 4 Advanced properties

Select **Define** to configure optional advanced properties:

* **Timeout in seconds**: The maximum time (in seconds) to wait to return data. Default = 10 seconds.
* **Retries**: The maximum number of retries for a query if it fails (total time for a query is `timeoutSecs` x `retries`). Default = 0 retries.

## Step 5 Autodiscovery

Autodiscovery is a feature that automatically resolves the DNS endpoints. If autodiscovery is defined, the URL becomes the DNS name.

Select **Define** to configure DNS endpoints:

* **Auto discovery type**: Only the `DNS` type available.
* **DNS type**: The type of DNS query to perform. Only the `A` type is available, which corresponds to IPv4 addresses.
* **DNS port**: Specifies the port assigned to all IPs resolved by the DNS.
* **DNS refresh interval (s)**: Sets interval time in seconds to the frequently changing IP addresses.

## Step 6 Activate extension

Provide final configuration details.

* Description
  Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, this can give your teams details of this particular monitoring configuration.
* Feature sets
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension. For more information, see [Prometheus data source reference](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#featureset "Learn about Prometheus extensions in the Extensions framework.").

When done, select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")