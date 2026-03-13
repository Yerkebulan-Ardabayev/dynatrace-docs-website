---
title: Set up Grail permissions for Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/permissions
scraped: 2026-03-06T21:12:31.901700
---

# Set up Grail permissions for Distributed Tracing

# Set up Grail permissions for Distributed Tracing

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 20, 2025

Dynatrace has a [permission model for Grail](../../../platform/grail/organize-data/assign-permissions-in-grail.md "Find out how to assign permissions to buckets and tables in Grail."). This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](../../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has [metadata enrichment](../../../ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment.md "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](../../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## Set up the security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your data. This context can represent your security architecture and could even be hierarchical by encoding this into a string such as: `department-A/department-AB/team-C`.

### Leverage existing tags at the source

You can define the security context at the source via [OneAgent](../../../ingest-from/dynatrace-oneagent/oneagent-security-context.md "Learn how to set up Grail permissions for OneAgent."), [OpenTelemetry](../../../ingest-from/opentelemetry/opentelemetry-security-context.md "Set up Grail permissions for OpenTelemetry."), or [Kubernetes labels or annotations](../../../ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment.md "Guides for telemetry enrichment on Kubernetes"). This allows you to use your existing labels and tags to facilitate permissions in Dynatrace.

## Set up the security context in OpenPipeline

Alternatively, you can define a security context based on existing resource attributes to your [span data within OpenPipeline](../../../platform/openpipeline/concepts/processing.md "Learn the core concepts of Dynatrace OpenPipeline processing."):

1. Filter the records that should get the `dt.security_context` attribute added to them. To do so, open a new [notebook](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and create a filtering DQL query, such as:

```
fetch spans



| filter matchesPhrase(deployment.release_stage, "prod-")
```

This query allows you to filter the span records to which you'll want to add the `dt.security_context` attribute. Once you're satisfied with the query result, copy the span processing function of the DQL query, in this case: `matchesPhrase(deployment.release_stage, "prod-")`.

2. Define the spans security context rule using the resulting function and specify the value of the `dt.security_context` attribute. The value of the `dt.security_context` attribute can be a literal value that you provide, or the name of another attribute; the value will be used as the value of `dt.security_context`.

## Recommendations for Distributed Tracing permissions

Permissions are typically configured for distributed tracing so users can see the complete end-to-end trace. Traces often span multiple services, hosts, or clusters, and cutting across traces with permission boundaries can result in incomplete or fragmented data. While service-level trace analytics will be less affected, and the distributed tracing app will work just fine, the potential lack of visibility impacts analytics and troubleshooting.

When setting up permissions for Distributed Tracing, consider these recommendations:

1. Avoid cutting through tracesâmake sure users can access all spans within a trace relevant to their role or deployment stage, while restricting access to sensitive services. Therefore, set graceful permissions and avoid boundaries restricting access to whole spans within a trace, as this can prevent a comprehensive analysis. For example, provide access to all spans in the relevant deployment stage (such as staging or production) or within organizational units (such as department or geographic region), and just restrict access to sensitive services (for example, the SSO).
2. Use field-level security for sensitive dataâinstead of restricting access to entire spans or traces, use field-level security to protect sensitive information.

   * Dynatrace automatically identifies selected span attributesâdefined in the [Global Field Reference](../../../semantic-dictionary/fields.md "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.")âand requests [attributes marked as confidential](../../../manage/data-privacy-and-security/configuration/configure-global-privacy-settings.md "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").
   * Only users with the `builtin-sensitive-spans` and `builtin-request-attributes-spans` [field permissions](../../../platform/grail/organize-data/assign-permissions-in-grail.md#field-permissions "Find out how to assign permissions to buckets and tables in Grail.") can see these sensitive fields.
   * Custom fieldsets can also be defined to specify sensitive attributes and the scope in which they apply. For example, see [Masking at display](../../../manage/data-privacy-and-security/configuration/configure-global-privacy-settings.md#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").
3. Leverage the security context to define permissions on individual span recordsâDynatrace allows you to tweak your ingested span data by adding a [`dt.security_context`](../../business-observability/bo-event-processing/bo-security-context.md "Use Dynatrace powered by Grail and DQL to reshape incoming business events data for better understanding, analysis, or further processing.") attribute to specific span records. This allows you to set additional options, such as permissions for individual records. To create a security context to your ingested span data, you need to create a pipeline rule.

## User permissions for Distributed Tracing

When working with the ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**, make sure that you've read and set all the necessary permissions:

1

Sensitive attributes for spans are tagged as `sensitive-spans` in [Global field reference](../../../semantic-dictionary/fields.md "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

2

To learn more about restricted view access to personal data and confidential request attributes, see [Masking at display](../../../manage/data-privacy-and-security/configuration/configure-global-privacy-settings.md#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").