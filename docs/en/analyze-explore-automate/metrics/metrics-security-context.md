---
title: Set up Grail permissions for Metrics
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/metrics-security-context
scraped: 2026-02-19T21:27:07.993712
---

# Set up Grail permissions for Metrics

# Set up Grail permissions for Metrics

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Nov 20, 2025

Dynatrace has a [permission model for Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail."). This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## Set up security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your data. This context can represent your security architecture and could even be hierarchical by encoding this into a string such as `department-A/department-AB/team-C`.

To use `dt.security_context` and other attributes for permissions, make sure these attributes are present in your telemetry data.

### Leverage existing tags at the source

You can define the security context at the source via [OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent."), [OpenTelemetry](/docs/ingest-from/opentelemetry/opentelemetry-security-context "Set up Grail permissions for OpenTelemetry."), or [Kubernetes labels or annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes"). This allows you to use your existing labels and tags to facilitate permissions in Dynatrace.

## Set up the security context in OpenPipeline

You can define a security context based on existing resource attributes for your data within OpenPipeline. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Metrics** > **Pipelines** and after configuring your pipeline, on the **Permission** tab, use the **Set Security Context processors** option.

To define the `dt.security_context` attribute

1. Define a matching condition to filter metric records to assign the security context, such as:

   ```
   matchesValue(metric.key, "http.server.request.duration_bucket") and matchesValue(http.route, "/basket")
   ```
2. Add the `dt.security_context` for those metric records. The value of this attribute can be a literal value such as `TeamA`, or a value copied from another field present on the metric record.
3. Verify your security context is set correctly.

When new metric data arrives, the OpenPipeline security context processors add a `dt.security_context` attribute with the value `TeamA` to the matching metric records. To confirm that your security context processors handled the metric records, open ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and run a DQL query such as:

```
timeseries median(http.server.request.duration_bucket), by:{http.route, dt.security_context} | filter matchesValue(dt.security_context, "TeamA")
```

Based on the created attribute, you can enforce security-related user and group policies.

## Related topics

* [Set up Grail permissions for OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent.")
* [Metadata enrichment of all telemetry originating from Kubernetes](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes")
* [Set up Grail permissions for logs](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")
* [Set up Grail permissions for Distributed Tracing](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.")
* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")