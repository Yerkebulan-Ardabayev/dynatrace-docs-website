---
title: Configure advanced permissions with security context
source: https://www.dynatrace.com/docs/platform/grail/organize-data/advanced-permission-setup
scraped: 2026-03-06T21:27:14.199849
---

# Configure advanced permissions with security context


* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 20, 2025

This guide outlines Dynatrace permission set up for your data-from basic access controls to advanced configurations such as enriching data with `dt.security_context`, applying OpenPipeline processors for conditional access, and managing IAM policies with boundaries and templates for scalable control.

Dynatrace has a permission model for Grail. This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](assign-permissions-in-grail.md#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has metadata enrichment enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](assign-permissions-in-grail.md#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## General permission setup

You can set up access controls for your data and entities using the guides below.

* OneAgent permission setup
* [Kubernetes permission setup](../../../ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment.md#security-context-and-cost-allocation "Guides for telemetry enrichment on Kubernetes")

* Logs permission setup
* Traces permission setup
* Entities permission setup
* [OpenPipeline permission setup](advanced-permission-setup.md#set-up-the-security-context-in-openpipeline "Configure advanced permissions with security context.")

## Set up the security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your specific data.

### Set up the security context in OpenPipeline

You can define a security context based on existing resource attributes to your [data within OpenPipeline](../../openpipeline/getting-started/tutorial-configure-processing.md#process "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
After configuring your pipeline, add `Set Security Context` processors on the `Permission` tab.

To define the `dt.security_context` attribute

1. Define a matching condition to filter records to assign the security context.

   For example: `matchesValue(http.route, â/basketâ)`
2. Add the `dt.security_context` for those records. The value of this attribute can be a literal value, for example `TeamA`, or a value copied from another field present on the record.
3. Verify your security context is set correctly.

   When new data arrives, the security context processors of OpenPipeline assign a `dt.security_context` attribute with the value `TeamA`. Open a Notebook to confirm that your security context processors handled the records. To verify, use a DQL query such as:

   `fetch logs | filter matchesValue(dt.security_context, "TeamA")`
4. Repeat this configuration for all the applicable data types (logs, metrics, spans).

Based on the created attribute, you can enforce security-related user and group policies, as described in the next section.

## Enforce access controls

You can enforce access controls to ensure that teams only access data that is relevant to them by using policy statements such as:

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH (â*-database-*â);


ALLOW storage:logs:read WHERE storage:dt.security_context = "TeamA" AND storage:dt.host_group.id MATCH ("shared_host_*");
```

You can also use policy boundaries or policy templating for easier management of your access controls.

## Related topics

* Set up Grail permissions for OneAgent
* Metadata enrichment of all telemetry originating from Kubernetes
* Set up Grail permissions for logs
* Set up Grail permissions for Distributed Tracing
* Grant access to entities with security context
* OpenPipeline processing examples