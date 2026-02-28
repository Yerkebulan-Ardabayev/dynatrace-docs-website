---
title: OpenTelemetry to Dynatrace semantic mapping
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/otel-semantic-mapping
scraped: 2026-02-28T21:25:40.736971
---

# OpenTelemetry to Dynatrace semantic mapping

# OpenTelemetry to Dynatrace semantic mapping

* Latest Dynatrace
* Reference
* 2-min read
* Published Jan 08, 2026

Dynatrace automatically maps OpenTelemetry semantic conventions to the [Dynatrace Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.").

This mapping ensures consistent data interpretation across your observability stack and enables Dynatrace apps, analytics, and visualization features to work with OpenTelemetry instrumentation.

## Messaging operations

Dynatrace maps OpenTelemetry messaging attributes to the Dynatrace semantic model.

| OpenTelemetry attribute | Dynatrace attribute |
| --- | --- |
| `messaging.operation` | `messaging.operation.type` |

For [`messaging.operation.type`](/docs/semantic-dictionary/fields#messaging "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types."), the value `send` is normalized to `publish`.

## URL parsing

Dynatrace automatically parses [`url.full`](/docs/semantic-dictionary/fields#url "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") into its constituent components:

| Derived attribute | Description |
| --- | --- |
| `url.path` | The path component of the URL |
| `url.scheme` | The protocol scheme (for example, `https`) |
| `url.fragment` | The fragment identifier |
| `url.query` | The query string |
| `server.address` | The host address |
| `server.port` | The port number |

### Deprecated attributes

Dynatrace maps deprecated OpenTelemetry HTTP attributes to their current equivalents:

| Deprecated attribute | Current attribute |
| --- | --- |
| `http.url` | `url.full` |
| `http.method` | `http.request.method` |
| `http.status_code` | `http.response.status_code` |

## Cloud provider attributes

Dynatrace creates provider-specific attributes from standard OpenTelemetry cloud attributes.

### Account and project identifiers

Dynatrace creates provider-specific account attributes from the standard [`cloud.account.id`](/docs/semantic-dictionary/fields#cloud "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") attribute:

| Cloud provider | OpenTelemetry attribute | Created attribute |
| --- | --- | --- |
| AWS | `cloud.account.id` | `aws.account.id` |
| Azure | `cloud.account.id` | `azure.subscription` |
| Google Cloud | `cloud.account.id` | `gcp.project.id` |

### Regional attributes

Dynatrace creates provider-specific region attributes from standard [`cloud.region`](/docs/semantic-dictionary/fields#cloud "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") and related attributes:

| Cloud provider | OpenTelemetry attributes | Created attribute |
| --- | --- | --- |
| AWS | `cloud.region` | `aws.region` |
| Azure | `cloud.region` | `azure.location` |
| Google Cloud | `gcp.location` `gcp.zone` `cloud.region` `cloud.availability_zone` | `gcp.region` |

For Google Cloud, if multiple source attributes are present, they are evaluated in the order listed above.

## Use standard OpenTelemetry conventions

Standard [OpenTelemetry semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/) are supported in your instrumentation. Dynatrace handles the translation automatically. This allows standard OpenTelemetry semantic conventions to work with Dynatrace semantic analysis.