---
title: Route data
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/how-to-routing
scraped: 2026-02-22T21:15:20.598001
---

# Route data

# Route data

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jun 23, 2025

There are several use cases to split incoming records into different streams, for example, separating non-production-relevant data or enabling teams to safely format only records of the applications and services they own.

This guide shows you how to route logs of multiple production-relevant services to dedicated pipelines.

## Who this is for

This article is intended for administrators managing data streams.

## Steps

1. Determine the condition

You can use Notebooks ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") to determine how many routes are needed and their matching conditions. To determine the conditions of significant production-relevant services

1. Fetch logs of all production-relevant services and summarize the records by an attribute.

   When you fetch logs via DQL in Notebooks you get an overview of the detected attributes that you can use to narrow down your results, for example, `k8s.deployment.name`.

   The following DQL query fetches logs with the Kubernetes namespace `prod` and summarizes the results by deployment name.

   ```
   fetch logs



   | filter k8s.namespace.name == "prod"



   | summarize by:{k8s.deployment.name}, count()
   ```

   Run in Playground
2. Determine the key-value pairs that identify significant services.

   The key-value pairs will be used as matching conditions. This guide focuses on four services that are identified by the following key-value pairs:

   * `k8s.deployment.name == "checkoutservice-*"`
   * `k8s.deployment.name == "currencyservice-*"`
   * `k8s.deployment.name == "emailservice-*"`
   * `k8s.deployment.name == "paymentservice-*"`

You determined how many routes you need (4) and their matching conditions (for example, `k8s.deployment.name == "checkoutservice-*`).

2. Create pipelines

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines**.
2. Create a pipeline for each service.

   1. Select  **Pipeline** and enter a pipeline titleâfor example, `Checkout service pipeline` for the **checkoutservice** service.
   2. Select **Save**.

You created an empty pipeline for each service.

3. Route records to the dedicated pipeline

Create a route for each pipeline.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines** >  **Dynamic route**.
2. Define the routing condition with

   * A name
   * A matching condition
   * The target pipeline

   The following table contains example conditions based on the Kubernetes namespace and deployment to route each service's logs to the corresponding pipeline.

   Name

   Matching condition

   Target pipeline

   Checkout service

   `k8s.deployment.name == "checkoutservice-*"`

   Checkout service pipeline

   Currency service

   `k8s.deployment.name == "currencyservice-*"`

   Currency service pipeline

   Email service

   `k8s.deployment.name == "emailservice-*"`

   Email service pipeline

   Payment service

   `k8s.deployment.name == "paymentservice-*"`

   Payment service pipeline

Logs that match the routing condition are routed to the target pipeline. The routing table now includes the new routes.

## Conclusion

You routed log lines for each significant production-relevant service to a dedicated empty pipeline.

Inform teams that they can modify the pipeline content and create processing rules for their services. Once logs are ingested and routed to one of the newly created pipelines, they will be processed according to the defined rules.

Production-relevant log lines that don't match any of the newly defined conditions continue to be routed according to the Default route to the Classic pipeline. Define new conditions to route them to a different pipeline.

To change how logs are processed, you can modify the matching condition to exclude or include other log lines, or route log lines to a different processing pipeline, or change the target storage. For example, you can create a new pipeline to skip storage using the **No storage assignment** processor and route all non-production-relevant logs that match the `isNotNull(k8s.namespace.name) and k8s.namespace.name != "prod"` condition.

## Related topics

* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")