---
title: Set up Grail permissions for OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/opentelemetry-security-context
scraped: 2026-02-17T05:12:17.892609
---

# Set up Grail permissions for OpenTelemetry

# Set up Grail permissions for OpenTelemetry

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

To add the security context to your OpenTelemetry data, enrich your signals with the `dt.security_context` attribute. Dynatrace automatically propagates the `dt.security_context` value from spans to the service entity for span data.

You can use your existing labels and tags to facilitate permissions in Dynatrace.

### Security context via Kubernetes labels or annotations

You can use [Kubernetes labels or annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes") as a source for your `dt.security_context`. This is one of the most convenient ways of doing this.

Alternatively, you can [configure the OpenTelemetry Collector to enrich data in transit](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data."). If you do this, you might have to map your Kubernetes metadata to `dt.security_context` in OpenPipeline.

### Security context via OpenTelemetry resource attributes

To use the [`OTEL_RESOURCE_ATTRIBUTES`](/docs/deliver/release-monitoring/version-detection-strategies#otel_resource_attributes "Metadata for version detection in different technologies") environment variable, just directly set the `dt.security_context` as a resource attribute. You can also use any resource attribute in OpenPipeline as a source for your `dt.security_context`.

### Security context via OneAgent metadata file

Dynatrace OneAgent provides enrichment files or environment variables to [add attributes directly in your application code](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

To read more about enrichment options and setup, see how to [enrich via environment variable](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#expand--enrich-via-environment-variable--4 "Guides for telemetry enrichment on Kubernetes").