---
title: Ingest sources in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/api-ingestion-reference
scraped: 2026-03-06T21:16:01.329825
---

# Ingest sources in OpenPipeline


* Latest Dynatrace
* Reference
* 5-min read
* Updated on Dec 04, 2025

In this article, you can find reference material on OpenPipeline ingest sources, split by each configuration scope. It includes

* Availabile ingest sources and the associated `dt.openpipeline.source`
* Ingest API specification, such as the endpoint URL and the authentication method
* Prior knowledge, such as concepts, licesing compatibility, and setup

Request query parameters

Each request query parameter becomes a top-level record attribute. If there is a pre-existing attribute in the payload with the same name, the attribute from the query parameter overrides the pre-existing attribute value. An overridden original value is preserved in a new field with name syntax `overwritten<index>.<original field name>`, for example, `overwritten1.myField`.

Business events

### Prior knowledge

* How to capture business events
* [OpenPipeline Data extraction stage](../concepts/processing.md#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* DDUs for business events

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| OneAgent | `oneagent` | Built-in |
| RUM Agent | `rumagent` | Built-in |
| Business Events API | `/api/v2/bizevents/ingest` | Built-in |
| Data Extraction | `data_extraction` | Built-in |

#### Business Events API

Captures business events in Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/bizevents/ingest` |
| Method | POST |
| Authentication | [OAuth](../../../observe/business-observability/bo-api-ingest.md#oauth "Set up authentication for and ingest business events via API.") [Access token](../../../observe/business-observability/bo-api-ingest.md#access-token "Set up authentication for and ingest business events via API.") with **Ingest bizevents** (`bizevents.ingest`) token scope |
| Payload | `application/json` `application/cloudevent+json` `application/cloudevent-batch+json` |

To learn more, see Ingest business events via API.

Logs

### Prior knowledge

* How to ingest logs
* Stream logs via Amazon Data Firehose
* DDUs for Log Management and Analytics or Log Analytics (DPS)

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Amazon Data Firehose | `/api/v2/logs/ingest/aws_firehose` | Built-in |
| Extensions | `<extension>` | Ready-made |
| Log ingest API | `/api/v2/logs/ingest` | Built-in |
| OneAgent | `oneagent` | Built-in |
| OpenTelemetry | `/api/v2/otlp/v1/logs` | Built-in |

#### Log ingest API

Pushes custom logs to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest` `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Ingest logs** (`logs.ingest`) scope |
| Payload | `text/plain` `application/json` |

To learn more, see Log Monitoring API v2 - POST ingest logs.

#### OpenTelemetry

Pushes custom logs to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest logs** (`logs.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see Ingest OTLP logs.

Events (generic events)

### Prior knowledge

* Events powered by Grail overview (DPS)

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Default API | `/platform/ingest/v1/events` | Built-in |
| Custom API | `/platform/ingest/custom/events/<custom-endpoint-name>` | Custom |

#### Default API

Ingests generic events from built-in endpoints.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events** (`openpipeline.events`) token scope |
| Payload | `application/json` |

To learn more, see OpenPipeline Ingest API - POST Built-in generic events.

#### Custom API

Configures custom endpoints to ingest generic events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events (Custom)** (`openpipeline.events.custom`) token scope |
| Payload | `application/json` |

To learn more, see OpenPipeline Ingest API - POST Custom generic event endpoint.

Events-Davis events

### Prior knowledge

* Davis events
* [OpenPipeline Data extraction stage](../concepts/processing.md#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* Events powered by Grail overview (DPS)

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| OneAgent | `oneagent` | Built-in |
| Classic environment API | `events/ingest` | Built-in |
| Data Extraction | `data_extraction` | Built-in |

#### Classic environment API

Ingests a custom event to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/events/ingest` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest Events** (`events.ingest`) token scope |
| Payload | `application/json` |

To learn more, see Events API v2 - POST an event.

Events-Davis problems

### Prior knowledge

* Davis problems
* [Classic root cause analysis](../../../dynatrace-intelligence/root-cause-analysis/concepts.md#root-cause-analysis "Get acquainted with root cause analysis concepts.")
* Events powered by Grail overview (DPS)

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Classic Root Cause Analysis | *(none)* | Built-in |

Events-SDLC events

### Prior knowledge

* How to ingest SDLC events events which you can then ingest to use to generate analytics.")
* Events powered by Grail overview (DPS)

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Endpoint for Software Development Lifecycle events | `/platform/ingest/v1/events.SDLC` | Built-in |
| Custom endpoint for Software Development Lifecycle events | `/platform/ingest/custom/events.SDLC/<custom-endpoint-name>` | Custom |

#### Endpoint for Software Development Lifecycle events

Ingests SDLC events from built-in endpoints.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events.sdlc` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events, Security Development Lifecycle** (`openpipeline.sdlc`) token scope |
| Payload | `application/json` |

To learn more, see OpenPipeline Ingest API - POST Built-in SDLC events.

#### Custom endpoint for Software Development Lifecycle events

Configures custom endpoints to ingest SDLC events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.sdlc` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events, Security Development Lifecycle (Custom)** (`openpipeline.sdlc.custom`) token scope |
| Payload | `application/json` |

To learn more, see OpenPipeline Ingest API - POST Custom SDLC event endpoint.

Events-Security events

Migrate by December 2025

The endpoints `events.security` are planned to be deprecated. Migrate your configurations to `security.events` endpoints by **end of December 2025**. The previous endpoints will remain available **until the migration is complete**.

For a full overview of what's changing and step-by-step guidance on how to migrate, follow the instructions in the Grail security table migration guide.

### Prior knowledge

* [How to ingest security events](../../../secure/threat-observability/security-events-ingest.md#ingest "Ingest external security data into Grail.")
* Events powered by Grail overview (DPS)

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Security events endpoint | `/platform/ingest/v1/events.security` | Built-in |
| Custom security events API | `/platform/ingest/custom/events.security/<custom-endpoint-name>` | Custom |

#### Security events endpoint (legacy)

Ingests security events from built-in endpoints.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events.security` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) token scope |
| Payload | `application/json` |

To learn more, see OpenPipeline Ingest API - POST Built-in security events (legacy).

#### Custom security events API (legacy)

Configures custom endpoints to ingest security events. For details, see Ingest custom security events via API.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.security` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) token scope |
| Payload | `application/json` |

To learn more, see OpenPipeline Ingest API - POST Custom security event endpoint (legacy).

Metrics

### Prior knowledge

* How to ingest metrics
* Metrics powered by Grail overview (DPS)

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| OneAgent | `oneagent` | Built-in |
| Classic environment API | `/api/v2/metrics/ingest` | Built-in |
| OpenTelemetry | `/api/v2/otlp/v1/metrics` | Built-in |

#### Classic environment API

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest metrics** (`metrics.ingest`) token scope |
| Payload | `text/plain` |

To learn more, see Metrics API - POST ingest data points.

#### OpenTelemetry

Ingests OpenTelemetry metrics into Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest metrics** (`metrics.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see OpenTelemetry metrics ingest API.

Security events (new)

### Prior knowledge

* [How to ingest security events](../../../secure/threat-observability/security-events-ingest.md#ingest "Ingest external security data into Grail.")
* Events powered by Grail overview (DPS)

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Security events endpoint | `/platform/ingest/v1/security.events` | Built-in |
| Custom security events API | `/platform/ingest/custom/security.events/<custom-endpoint-name>` | Custom |

#### Security events endpoint (new)

Ingests security events from built-in endpoints.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/security.events` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) token scope |
| Payload | `application/json` |

To learn more, see OpenPipeline Ingest API - POST Built-in security events (new).

#### Custom security events API (new)

Configures custom endpoints to ingest security events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/security.events` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) token scope |
| Payload | `application/json` |

To learn more, see OpenPipeline Ingest API - POST Custom security event endpoint (new).

Spans

### Prior knowledge

* How to ingest traces
* Traces powered by Grail overview (DPS) model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| OneAgent | `oneagent` | Built-in |
| OpenTelemetry | `/api/v2/otlp/v1/traces` | Built-in |

#### OpenTelemetry

Ingests OpenTelemetry traces to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/traces` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see OpenTelemetry trace ingest API.

System events

### Prior knowledge

* System event models
* Extensions
* Supported system events in OpenPipeline are limited to

  + App Lifecycle Notifications

    `event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY"`
  + Workflow Execution events

    `event.kind == "WORKFLOW_EVENT" AND event.provider == "AUTOMATION_ENGINE"`
  + ECC self-monitoring events

    `event.kind == "EXTENSIONS_EVENT"`

  To learn the path and type of the system events processed in your environment

  1. Go to **Notebooks**.
  2. Create a new notebook containing the following query

     ```
     fetch dt.system.events


     | filter isNotNull(dt.openpipeline.pipelines)
     ```
  3. Select **Run**.

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| System Events API[1](#fn-1-1-def) | `system_events` | Built-in |
| Extensions | `<extension>` | Ready-made |

1

Internally generated

User events & sessions

### Prior knowledge

* User events
* User sessions
* How to capture user events and sessions on Android, iOS, Flutter or React Native
* Digital Experience Monitoring (DEM) overview (DPS) consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| RUM Agent | `rumagent` | Built-in |

## Related topics

* Data flow in OpenPipeline
* How to ingest data (events)