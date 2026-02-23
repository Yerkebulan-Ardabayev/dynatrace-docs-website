---
title: Set up Grail permissions for Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/permissions
scraped: 2026-02-23T21:20:35.070737
---

# Set up Grail permissions for Distributed Tracing

# Set up Grail permissions for Distributed Tracing

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

## Set up the security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your data. This context can represent your security architecture and could even be hierarchical by encoding this into a string such as: `department-A/department-AB/team-C`.

### Leverage existing tags at the source

You can define the security context at the source via [OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent."), [OpenTelemetry](/docs/ingest-from/opentelemetry/opentelemetry-security-context "Set up Grail permissions for OpenTelemetry."), or [Kubernetes labels or annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes"). This allows you to use your existing labels and tags to facilitate permissions in Dynatrace.

## Set up the security context in OpenPipeline

Alternatively, you can define a security context based on existing resource attributes to your [span data within OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing."):

1. Filter the records that should get the `dt.security_context` attribute added to them. To do so, open a new [notebook](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and create a filtering DQL query, such as:

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

   * Dynatrace automatically identifies selected span attributesâdefined in the [Global Field Reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.")âand requests [attributes marked as confidential](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").
   * Only users with the `builtin-sensitive-spans` and `builtin-request-attributes-spans` [field permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#field-permissions "Find out how to assign permissions to buckets and tables in Grail.") can see these sensitive fields.
   * Custom fieldsets can also be defined to specify sensitive attributes and the scope in which they apply. For example, see [Masking at display](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").
3. Leverage the security context to define permissions on individual span recordsâDynatrace allows you to tweak your ingested span data by adding a [`dt.security_context`](/docs/observe/business-observability/bo-event-processing/bo-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming business events data for better understanding, analysis, or further processing.") attribute to specific span records. This allows you to set additional options, such as permissions for individual records. To create a security context to your ingested span data, you need to create a pipeline rule.

## User permissions for Distributed Tracing

When working with the ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**, make sure that you've read and set all the necessary permissions:

Policy scope

Table permission

Read buckets data

`storage:buckets:read`

Read span data

`storage:spans:read`

Read entities data

`storage:entities:read`

Read log data

`storage:logs:read`

Read filter-segments data

`storage:filter-segments:read`

View sensitive fields trace data [1](#fn-1-1-def) [2](#fn-1-2-def)

`storage:fieldsets:read WHERE storage:fieldset-name="builtin-sensitive-spans`

`storage:fieldsets:read WHERE storage:fieldset-name="builtin-request-attributes-spans`

Read user app states

`state:user-app-states:read`

Write user app states

`state:user-app-states:write`

Delete user app states

`state:user-app-states:delete`

1

Sensitive attributes for spans are tagged as `sensitive-spans` in [Global field reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

2

To learn more about restricted view access to personal data and confidential request attributes, see [Masking at display](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").