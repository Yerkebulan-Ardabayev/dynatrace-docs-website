---
title: Configure advanced permissions with security context
source: https://www.dynatrace.com/docs/platform/grail/organize-data/advanced-permission-setup
scraped: 2026-02-23T21:39:53.559359
---

# Configure advanced permissions with security context

# Configure advanced permissions with security context

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 20, 2025

This guide outlines Dynatrace permission set up for your data-from basic access controls to advanced configurations such as enriching data with `dt.security_context`, applying OpenPipeline processors for conditional access, and managing IAM policies with boundaries and templates for scalable control.

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

## General permission setup

You can set up access controls for your data and entities using the guides below.

* [OneAgent permission setup](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent.")
* [Kubernetes permission setup](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#security-context-and-cost-allocation "Guides for telemetry enrichment on Kubernetes")

* [Logs permission setup](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")
* [Traces permission setup](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.")
* [Entities permission setup](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context")
* [OpenPipeline permission setup](/docs/platform/grail/organize-data/advanced-permission-setup#set-up-the-security-context-in-openpipeline "Configure advanced permissions with security context.")

## Set up the security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your specific data.

### Set up the security context in OpenPipeline

You can define a security context based on existing resource attributes to your [data within OpenPipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#process "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
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

You can [enforce access controls](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.") to ensure that teams only access data that is relevant to them by using policy statements such as:

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH (â*-database-*â);



ALLOW storage:logs:read WHERE storage:dt.security_context = "TeamA" AND storage:dt.host_group.id MATCH ("shared_host_*");
```

You can also use [policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") or [policy templating](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policy-templating "Policy templating") for easier management of your access controls.

## Related topics

* [Set up Grail permissions for OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent.")
* [Metadata enrichment of all telemetry originating from Kubernetes](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes")
* [Set up Grail permissions for logs](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")
* [Set up Grail permissions for Distributed Tracing](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.")
* [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context")
* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")