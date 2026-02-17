---
title: Set up Grail permissions for telemetry from Kubernetes and Kubernetes workloads
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/k8-security-context
scraped: 2026-02-17T05:06:35.411327
---

# Set up Grail permissions for telemetry from Kubernetes and Kubernetes workloads

# Set up Grail permissions for telemetry from Kubernetes and Kubernetes workloads

* Latest Dynatrace
* How-to guide
* 1-min read
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

## Set up security context in Kubernetes

You may already have defined your own security boundaries outside of Dynatrace and defined them as Kubernetes labels or annotations. Suppose the permissions for the Kubernetes cluster or namespace are not sufficient. In that case, Dynatrace allows you to set up more fine-grained permissions by leveraging your own Kubernetes labels or annotations as the source for your [security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context") in Dynatrace.

This security context can represent your own security architecture and could even be hierarchical by encoding this into a string such as `department-A/department-AB/team-C`.

### Security context based on existing namespace labels or annotations (recommended)

Via the Kubernetes metadata enrichment feature, you can use already existing namespace labels and annotations as source for your security context. Just choose an existing label, and it will be added as `dt.security_context` on your telemetry.

To enable this functionality, make sure Dynatrace Operator has [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

For details, see [Use settings to use existing labels and annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#enrichment-options "Guides for telemetry enrichment on Kubernetes").

### Security context based on dedicated pod annotations

[Dedicated pod annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#dedicated-annotations "Guides for telemetry enrichment on Kubernetes") are only intended for scenarios where namespace labels or annotations cannot be used as a source.

Unlike the settings-based approach, manually added pod annotations do not provide full enrichment. They do not enrich Kubernetes metrics, Kubernetes events, Kubernetes Smartscape entities, or Prometheus metrics.

You can provide `dt.security_context` as a pod annotatation:

```
metadata:



annotations:



metadata.dynatrace.com/dt.security_context: foo
```

This works automatically for OneAgent and OpenTelemetry scenarios where you are enriching [attributes directly in your application code](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

For details, see [security context and cost allocation](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#security-context-and-cost-allocation "Guides for telemetry enrichment on Kubernetes").

## Related topics

* [Kubernetes cluster and workload monitoringï»¿](https://www.dynatrace.com/technologies/kubernetes-monitoring/)