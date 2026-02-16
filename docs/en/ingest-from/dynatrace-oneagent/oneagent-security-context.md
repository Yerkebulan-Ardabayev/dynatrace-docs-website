---
title: Set up Grail permissions for OneAgent
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-security-context
scraped: 2026-02-16T09:22:53.604227
---

# Set up Grail permissions for OneAgent

# Set up Grail permissions for OneAgent

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Aug 19, 2025

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

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your data. This security context can represent your security architecture and could even be hierarchical by encoding this into a string: `department-A/department-AB/team-C`.

You need to ensure the attribute exists as part of the telemetry data and that OneAgent provides the value directly at the VM level.

To set a security context for your host, use the following command:

* Linux and AIX

  ```
  ./oneagentctl --set-host-property=dt.security_context=easytrade_sec
  ```
* Windows

  ```
  `.\oneagentctl.exe --set-host-property=dt.security_context=easytrade_sec`
  ```

This adds the security context to all metrics, spans, events, and logs collected by OneAgent on this host.

The `dt.security_context` is utilized by many features in Dynatrace and available for all telemetry data. You can use it for [record-level security](/docs/platform/grail/organize-data/assign-permissions-in-grail#field-permissions "Find out how to assign permissions to buckets and tables in Grail.").