---
title: Extract metrics from spans and distributed traces
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-extract-metrics-from-spans
scraped: 2026-02-17T21:18:13.610298
---

# Extract metrics from spans and distributed traces

# Extract metrics from spans and distributed traces

* Latest Dynatrace
* Tutorial
* 5-min read
* Published Dec 23, 2025

This tutorial shows you how to extract metrics directly from your spans and distributed traces, via OpenPipeline, which provides flexible processing, enrichment, and routing at scale. New metrics can be calculated and derived based on any data available within the captured distributed trace, and the metrics can also be split by multiple dimensions, for example, a Kubernetes workload or a request attribute.

## Who this is for

This article is intended for app users building long-term dashboard-ready metrics from traces.

## What you will learn

How to set up OpenPipeline to extract a metric from a captured span via five examples you can adapt to your own services.

## Before you begin

Prior knowledge

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* Dynatrace Platform Subscription (DPS) with [Traces powered by Grail (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.") capabilities.
* OpenPipeline permissions: `settings:objects:read` and `settings:objects:write`. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
* [Distributed Tracing permissions](/docs/observe/application-observability/distributed-tracing/permissions#user-permissions-for-distributed-tracing "Manage permissions for Distributed Tracing powered by Grail.")

## Examples

### Requests to a workload split by Kubernetes pod

This example shows the new, recommended way to get [service instance-level insights](/docs/observe/application-observability/services-classic/analyze-individual-service-instances "Find out how you can perform a service-instance analysis."), a concept that is going away. Extract metrics from spans and split by real deployment dimensions like Kubernetes workload, pod, host, and more.

For common splits such as namespace, cluster or cloud region, use the out-of-the-box [primary Grail fields](/docs/semantic-dictionary/tags/primary-fields) already available in service metrics; you don't need a new metric.

1. Find the condition for the relevant spans in Notebooks

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open an existing or new notebook.
2. Select  > **DQL**.
3. Use a DQL query to prototype your filters, fields, and groupings before you configure OpenPipeline. For example, to explore the spans that represent requests to the workload, you can use the following query:

   ```
   fetch spans



   | filter k8s.workload.name == "my-otel-demo-frontend" and span.kind == "server" and isNotNull(endpoint.name)



   | fields k8s.pod.name, dt.entity.service, endpoint.name, duration



   | limit 200
   ```

   Run in Playground

Understanding the filter conditions

* `span.kind == "server"` only keeps inbound service-handled requests and excludes client or internal spans.
* `isNotNull(endpoint.name)` ensures the span represents a request to an endpoint that Dynatrace considers in its endpoint detection rules, and that it isn't a muted request, for example.

2. Create a pipeline for metric extraction

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **System events** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To configure metric extraction, go to **Metric extraction** >  **Processor** > **Sampling aware counter metric** and define the processor by entering:

   * A descriptive nameâfor example, `Requests to my-otel-demo-frontend split by Kubernetes pod`
   * The matching condition:

     ```
     k8s.workload.name == "my-otel-demo-frontend"
     ```
   * The new metric keyâfor example, `span.my-otel-demo-frontend.requests_by_pod.count`
   * The metric dimensions:

     1. Select **Pre-defined** and choose `k8s.pod.name` and `k8s.pod.uid` from the [pre-defined dimensions](/docs/semantic-dictionary/model/dt-system-events#audit-event "Get to know the Semantic Dictionary models related to system events."). These dimensions identify the pods where the workload is running. Other dimensions have also been pre-selected, such as `dt.entity.service`.
     2. Select **Save**.

You successfully created a new pipeline to extract a metric containing information about how many requests there were for the `my-otel-demo-frontend` workload and, because the metric has the pod as a dimension, you'll be able to split the requests by pod. The new pipeline is visible in the pipelines list.

3. Route spans to the pipeline

Create a dynamic route that funnels the spans you're interested in into the team's pipeline.

* One span will be routed to exactly one dynamic route. Spans can't be routed to multiple dynamic routes, so keep matching conditions precise and mutually exclusive.
* Dynamic routes are evaluated from top to bottom; as soon as a matching condition evaluates to "true", the span is routed through that dynamic route.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **System events** > **Dynamic routing**.
2. To create a new route, select  **Dynamic route** and specify:

   * A descriptive nameâfor example, `Spans for TeamA Cluster1 Namespace2`
   * The matching condition:

     ```
     k8s.cluster.name == "Cluster1" and k8s.namespace.name == "Namespace2"
     ```
3. Select **Add**.

You successfully created a new route. All spans of Kubernetes "Cluster1" and "Namespace2" are routed to the pipeline where a metric is extracted. The new route is visible in the routes list.

4. Query the metric

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open an existing or new notebook.
2. Select  > **Metrics** > **Select a metric**.
3. Enter and select the new metric key (`span.my-otel-demo-frontend.requests_by_pod.count`).
4. Select  **Run**.

You've successfully extracted a metric to track requests to the `my-otel-demo-frontend` workload.

* You can use a Kubernetes pod dimension to split this metric.
* Spans are routed to the new pipeline; when the span belongs to the `my-otel-demo-frontend` workload (matching condition of the processor), the new pipeline extracts a metric containing the pod where the workload is running, in addition to other details.
* You can query the metric in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, or see it in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** or ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

### Number of books successfully sold per service

In this example, we describe the creation of the pipeline and the metric-extraction processor. For detailed steps, follow the approach of the [workload split by Kubernetes pod example](#workload-requests-pod), but adapt the filter queries and routing.

Assumptions for the example

The number of books sold is captured as a [request attribute](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views."), for example, `request_attribute.book_orders_count`. Request attributes are exposed under [`request_attribute.__attribute_name__`](/docs/semantic-dictionary/fields#request-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **System events** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To configure metric extraction, go to **Metric extraction** >  **Processor** > **Sampling aware counter metric** and define the processor by entering:

   * A descriptive nameâfor example, `Number of books successfully sold per service`
   * The matching condition:

     ```
     endpoint.name == "POST /book/{id}/checkout" and isNotNull(request_attribute.book_orders_count) and request.is_failed != true
     ```
   * For the measurement type, select **Custom**, as we're not measuring durations.
   * The field name from which to extract the value (`request_attribute.book_orders_count`).
   * The sampling options enabled (leave as is), so that the metric extraction is sampling aware.
   * The new metric keyâfor example, `span.books.sold.count`.
   * The metric dimensions. You can use the pre-selected dimensions, as `dt.entity.service` is selected by default.
4. Select **Save**.

You successfully created a new processor to extract a metric containing information about the number of books successfully sold, and, because the metric has the `dt.entity.service` service as a dimension, you'll be able to split the metric per service.

### Top database calls per service and query group

In this example, we describe the creation of the pipeline and the metric-extraction processor. For detailed steps, follow the approach of the [workload split by Kubernetes pod example](#workload-requests-pod), but adapt the filter queries and routing.

For this example metric, we want to know the top database operations or commands executed across our services. For example, the MongoDB command name, SQL keyword, Redis command name, together with the name of the target database (`db.namespace`).

We're not creating a metric for the actual `db.query.text` being executed (for example, `SELECT * FROM user_table`), as that would result in a metric with a very high cardinality.

To see a list of the actual queries being executed by your services, use the [database query performance analysis in the Services app](/docs/observe/application-observability/services/services-app#database-query-performance-analysis "Maintain centralized control over service health, performance, and resources with the Services app.").

1. Add a new query group attribute to database spans

We'll add a new attribute to our database spans that contains the query group we're interested in having in our metric: `db.operation.name +Â db.namespace`. We can then use the newly created attribute in our metric extraction step.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To add the new attribute to incoming database spans, go to **Processing** > **+ Processor** > **DQL** and define the processor by entering:

   * A descriptive nameâfor example, `Construct low cardinality db.query.group`
   * The matching condition:

     ```
     isNotNull(db.operation.name) and isNotNull(db.namespace)
     ```
   * The DQL processor definition:

     ```
     fieldsAdd db.query.group = concat(db.operation.name, " ", db.namespace)
     ```

Conclusion

You added a new `db.query.group` attribute to the database spans that you can now use to create your metric.

**Before**

```
{



"db.namespace": "books",



"db.operation.name": "SELECT",



"db.query.text": "select b1_0.id,b1_0.author,b1_0.title from books b1_0 where b1_0.title=?"



}
```

**After**

```
{



"db.query.group": "SELECT books",



"db.namespace": "books",



"db.operation.name": "SELECT",



"db.query.text": "select b1_0.id,b1_0.author,b1_0.title from books b1_0 where b1_0.title=?"



}
```

2. Use the new attribute in the metric extraction

1. Go to **Metric extraction** >  **Processor** > **Sampling aware counter metric** and define the processor by entering:

   * A descriptive nameâfor example, `Database calls per service and query group`
   * The matching condition:

     ```
     isNotNull(db.query.group)
     ```
   * The field name from which to extract the value (`request_attribute.book_orders_count`).
   * The sampling options enabled (leave as is), so that the metric extraction is sampling aware.
   * The new metric keyâfor example, `span.service.db_calls_by_group.count`.
   * The metric dimensions. Select **Custom** and choose `db.query.group` as the **Field name on record**. For the service dimension, `dt.entity.service` is selected by default.
2. Select **Save**.

You successfully created a new processor to extract a metric containing information about the database calls per service and query group.

3. Query the top 10 values

In ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** or ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, use [Explore interface for Metrics](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-metrics "Explore your data with our point-and-click interface.") to plot the `span.service.db_calls_by_group.count`:

* Split by `db.query.group` and `dt.entity.service`
* Sort by the `value.A` metric in a `DESC` order
* Use [**Limit**](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#metric-limit "Explore your data with our point-and-click interface.") `10` to display the top 10 results

![Explore metrics - Top 10 queries](https://dt-cdn.net/images/screenshot-2025-12-23-at-18-23-49-2414-9876a1a980.png)

### CPU time per service endpoint

In this example, we describe the creation of the pipeline and the metric-extraction processor. For detailed steps, follow the approach of the [workload split by Kubernetes pod example](#workload-requests-pod), but adapt the filter queries and routing.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To configure a value metric extraction, **Metric extraction** >  **Processor** > **Sampling aware value metric** and define the processor by entering:

   * A descriptive nameâfor example, `CPU time per service endpoint`
   * The matching condition:

     ```
     request.is_root_span == true
     ```

     This condition ensures that weâll be capturing the first span of a request within a service. That is, the span where endpoint detection rules are evaluated.
   * For the measurement type, select **Custom**, as we're not measuring durations.
   * The field name from which to extract the value (`span.timing.cpu`). This attribute tracks the overall CPU time spent executing the span, including the CPU times of child spans that are running on the same thread on the same call stack.
   * The sampling options enabled (leave as is), so that the metric extraction is sampling aware.
   * The new metric keyâfor example, `span.request.cpu_time`.
   * The metric dimensions:

     1. Select **Pre-defined** and choose `endpoint.name` from the [pre-defined dimensions](/docs/semantic-dictionary/model/dt-system-events#audit-event "Get to know the Semantic Dictionary models related to system events."). Other dimensions also get pre-selected, such as `dt.entity.service`.
     2. Select **Save**.

You successfully created a new processor to extract a metric containing information about the CPU time consumed per endpoint. The CPU-time field is measured in nanoseconds.

### Response time for outbound calls to paypal.com per service, as measured by the caller

Upcoming features

Histogram metric extraction support is coming soon.

Later in 2026, Dynatrace will provide out-of-the-box metrics for third-party calls, as part of the modernization of [Monitor third-party services](/docs/observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services "Configure how Dynatrace should monitor third-party services.").

In this example, we describe the creation of the pipeline and the metric-extraction processor. For detailed steps, follow the approach of the [workload split by Kubernetes pod example](#workload-requests-pod), but adapt the filter queries and routing.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To configure a histogram metric extraction, go to **Metric extraction** >  **Processor** > **Sampling aware histogram metric** and define the processor by entering:

   * A descriptive nameâfor example, `Response time for outbound calls to paypal.com per service, as measured by the caller`.
   * The matching condition:

     ```
     span.kind == "client" and matchesValue(server.address, "*.paypal.com")
     ```
   * **Measurement** set to **Duration**.
   * The new metric keyâfor example, `span.outbound_paypal_requests.response_time`.
   * The metric dimensionsâyou can use the pre-selected dimensions, as `dt.entity.service` is selected by default.
4. Select **Save**.

You successfully created a new processor to extract a metric containing the response time for outbound calls to paypal.com, as measured by the caller. Also, because the metric has the calling service (`dt.entity.service`) as a dimension, you'll be able to split the metric per service.