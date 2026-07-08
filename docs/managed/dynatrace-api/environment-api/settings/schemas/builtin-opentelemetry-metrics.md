---
title: Settings API - OpenTelemetry metrics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-opentelemetry-metrics
---

# Settings API - OpenTelemetry metrics schema table

# Settings API - OpenTelemetry metrics schema table

* Published Dec 05, 2023

### OpenTelemetry metrics (`builtin:opentelemetry-metrics)`

Configure how OpenTelemetry metrics are ingested into Dynatrace via the OTLP endpoint.

**Notes:**

* Changes made to these settings only apply to newly ingested data points. Data points that are already stored in Dynatrace will not change.
* Changes made to these settings may have an impact on existing dashboards, events and alerts that use dimensions configured here. In this case, they will need to be updated manually.
* Settings marked with `(Metrics Classic)` have no effect in Metrics powered by Grail. For Metrics powered by Grail all attributes (resource, scope and metric) are accepted by default. Use the block-list if you want to avoid ingesting certain attributes.
* For OpenTelemetry trace/span settings, navigate to: **Settings** > **Server-side service monitoring**.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:opentelemetry-metrics` | * `group:metrics` | `environment`  `environment-default` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:opentelemetry-metrics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:opentelemetry-metrics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:opentelemetry-metrics` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Add Meter name and version as metric dimensions (Metrics Classic) `meterNameToDimensionEnabled` | boolean | When enabled, the Meter name (also referred to as InstrumentationScope or InstrumentationLibrary in OpenTelemetry SDKs) and version will be added as dimensions (`otel.scope.name` and `otel.scope.version`) to ingested OTLP metrics. | Required |
| Advanced OTLP metric dimensions `enableMintV2Ingest` | boolean | Enable advanced OpenTelemetry metric capabilities with Grail, including primary field enrichment, flexible dimensions, enhanced routing, cost allocation, and support for high-cardinality queries. For more details about this and its effect on enrichment with the `dt.entity.service` dimension, please see [this post﻿](https://dt-url.net/otlp-metrics-advanced). | Optional |
| Add the resource and scope attributes configured below as dimensions (Metrics Classic) `additionalAttributesToDimensionEnabled` | boolean | - | Required |
| `additionalAttributes` | Set<[AdditionalAttributeItem](#AdditionalAttributeItem)> | When enabled, the attributes defined in the list below will be added as dimensions to ingested OTLP metrics if they are present in the OpenTelemetry resource or in the instrumentation scope.  **Notes:**  * Attributes **must** be added in their **original format**, as exported to Dynatrace by the telemetry source. For example, if the attribute is in `PascalCase`, the same case must be used when adding the attribute to the list. * Dynatrace does not recommend changing/removing the attributes starting with "dt.". Dynatrace leverages these attributes to [Enrich metrics﻿](https://www.dynatrace.com/support/help/extend-dynatrace/extend-metrics/reference/enrich-metrics). | Required |
| `toDropAttributes` | Set<[DropAttributeItem](#DropAttributeItem)> | The attributes defined in the list below will be dropped from all ingested OTLP metrics.  **Notes:**  * Attributes **must** be added in their **original format**, as exported to Dynatrace by the telemetry source. For example, if the attribute is in `PascalCase`, the same case must be used when adding the attribute to the list. * Wildcards are only supported in Metrics powered by Grail. * Dynatrace does not recommend including attributes starting with "dt." to the deny list. Dynatrace leverages these attributes to [Enrich metrics﻿](https://www.dynatrace.com/support/help/extend-dynatrace/extend-metrics/reference/enrich-metrics). | Required |

##### The `AdditionalAttributeItem` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | When enabled, the attribute will be added as a dimension to ingested metrics if present in the OpenTelemetry resource or in the instrumentation scope. | Required |
| Attribute key `attributeKey` | text | - | Required |

##### The `DropAttributeItem` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | When enabled, the attribute will be dropped on all ingested metrics. | Required |
| Attribute key `attributeKey` | text | - | Required |