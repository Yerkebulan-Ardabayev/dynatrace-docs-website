---
title: Ingest sources in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/api-ingestion-reference
scraped: 2026-03-06T21:16:01.329825
---

# Ingest sources in OpenPipeline

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

* [How to capture business events](../../../observe/business-observability/bo-events-capturing.md "Capture business events for Dynatrace Business Observability.")
* [OpenPipeline Data extraction stage](../concepts/processing.md#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* [DDUs for business events](../../../license/monitoring-consumption-classic/davis-data-units/ddus-for-business-events.md "Understand how the volume of DDU consumption is calculated for business events.")

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

To learn more, see [Ingest business events via API](../../../observe/business-observability/bo-api-ingest.md "Set up authentication for and ingest business events via API.").

Logs

### Prior knowledge

* [How to ingest logs](../../../analyze-explore-automate/logs/lma-log-ingestion.md "Stream log data to Dynatrace.")
* [Stream logs via Amazon Data Firehose](../../../ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose.md "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* [DDUs for Log Management and Analytics](../../../license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics.md "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.") or [Log Analytics (DPS)](../../../license/capabilities/log-analytics.md "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")

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

To learn more, see [Log Monitoring API v2 - POST ingest logs](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Push custom logs to Dynatrace via the Log Monitoring API v2.").

#### OpenTelemetry

Pushes custom logs to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest logs** (`logs.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see [Ingest OTLP logs](../../../ingest-from/opentelemetry/otlp-api/ingest-logs.md "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

Events (generic events)

### Prior knowledge

* [Events powered by Grail overview (DPS)](../../../license/capabilities/events.md "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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

To learn more, see [OpenPipeline Ingest API - POST Built-in generic events](openpipeline-ingest-api/generic-events/events-generic-builtin.md "Ingest generic events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom API

Configures custom endpoints to ingest generic events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events (Custom)** (`openpipeline.events.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom generic event endpoint](openpipeline-ingest-api/generic-events/events-generic-custom-endpoint.md "Configure a custom generic event endpoint via OpenPipeline Ingest API.").

Events-Davis events

### Prior knowledge

* [Davis events](../../../../common/semantic-dictionary/model/davis.md "Get to know the Semantic Dictionary models related to Davis AI.")
* [OpenPipeline Data extraction stage](../concepts/processing.md#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* [Events powered by Grail overview (DPS)](../../../license/capabilities/events.md "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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

To learn more, see [Events API v2 - POST an event](../../../dynatrace-api/environment-api/events-v2/post-event.md "Ingests an event via the Dynatrace API.").

Events-Davis problems

### Prior knowledge

* [Davis problems](../../../../common/semantic-dictionary/model/davis.md "Get to know the Semantic Dictionary models related to Davis AI.")
* [Classic root cause analysis](../../../dynatrace-intelligence/root-cause-analysis/concepts.md#root-cause-analysis "Get acquainted with root cause analysis concepts.")
* [Events powered by Grail overview (DPS)](../../../license/capabilities/events.md "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Classic Root Cause Analysis | *(none)* | Built-in |

Events-SDLC events

### Prior knowledge

* [How to ingest SDLC events](../../../deliver/pipeline-observability-sdlc-events/sdlc-events.md "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.")
* [Events powered by Grail overview (DPS)](../../../license/capabilities/events.md "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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

To learn more, see [OpenPipeline Ingest API - POST Built-in SDLC events](openpipeline-ingest-api/sdlc-events/events-sdlc-builtin.md "Ingest SDLC events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom endpoint for Software Development Lifecycle events

Configures custom endpoints to ingest SDLC events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.sdlc` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events, Security Development Lifecycle (Custom)** (`openpipeline.sdlc.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom SDLC event endpoint](openpipeline-ingest-api/sdlc-events/events-sdlc-custom-endpoint.md "Configure a custom SDLC event endpoint via OpenPipeline Ingest API.").

Events-Security events

Migrate by December 2025

The endpoints `events.security` are planned to be deprecated. Migrate your configurations to `security.events` endpoints by **end of December 2025**. The previous endpoints will remain available **until the migration is complete**.

For a full overview of what's changing and step-by-step guidance on how to migrate, follow the instructions in the [Grail security table migration guide](../../../secure/threat-observability/migration.md "Understand the changes in the new Grail security table and learn how to migrate to it.").

### Prior knowledge

* [How to ingest security events](../../../secure/threat-observability/security-events-ingest.md#ingest "Ingest external security data into Grail.")
* [Events powered by Grail overview (DPS)](../../../license/capabilities/events.md "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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

To learn more, see [OpenPipeline Ingest API - POST Built-in security events (legacy)](openpipeline-ingest-api/security-events/events-security-builtin.md "Ingest security events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom security events API (legacy)

Configures custom endpoints to ingest security events. For details, see [Ingest custom security events via API](../../../secure/threat-observability/security-events-ingest/ingest-custom-data.md "Ingest security events from custom third-party products via API.").

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.security` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom security event endpoint (legacy)](openpipeline-ingest-api/security-events/events-security-custom-endpoint.md "Configure a custom security event endpoint via OpenPipeline Ingest API.").

Metrics

### Prior knowledge

* [How to ingest metrics](../../../analyze-explore-automate/metrics.md "Metrics powered by Grail offer a comprehensive solution to manage your metrics data, in integration with logs, spans, and events, providing a unified approach to data analysis.")
* [Metrics powered by Grail overview (DPS)](../../../license/capabilities/metrics.md "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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

To learn more, see [Metrics API - POST ingest data points](../../../dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md "Ingest custom metrics to Dynatrace via Metrics v2 API.").

#### OpenTelemetry

Ingests OpenTelemetry metrics into Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest metrics** (`metrics.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see [OpenTelemetry metrics ingest API](../../../dynatrace-api/environment-api/opentelemetry/post-metrics.md "Send OpenTelemetry metrics to Dynatrace via API.").

Security events (new)

### Prior knowledge

* [How to ingest security events](../../../secure/threat-observability/security-events-ingest.md#ingest "Ingest external security data into Grail.")
* [Events powered by Grail overview (DPS)](../../../license/capabilities/events.md "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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

To learn more, see [OpenPipeline Ingest API - POST Built-in security events (new)](openpipeline-ingest-api/security-events/security-events-builtin.md "Ingest security events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom security events API (new)

Configures custom endpoints to ingest security events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/security.events` |
| Method | POST |
| Authentication | [Access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom security event endpoint (new)](openpipeline-ingest-api/security-events/security-events-custom-endpoint.md "Configure a custom security event endpoint via OpenPipeline Ingest API.").

Spans

### Prior knowledge

* [How to ingest traces](../../../observe/application-observability/distributed-tracing/ingest-traces.md "Instrument your applications with OneAgent or OpenTelemetry to start ingesting trace data into Dynatrace.")
* [Traces powered by Grail overview (DPS)](../../../license/capabilities/traces.md "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.")

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

To learn more, see [OpenTelemetry trace ingest API](../../../dynatrace-api/environment-api/opentelemetry/post-traces.md "Send OpenTelemetry traces to Dynatrace via API..").

System events

### Prior knowledge

* [System event models](../../../semantic-dictionary/model/dt-system-events.md "Get to know the Semantic Dictionary models related to system events.")
* [Extensions](../../../ingest-from/extensions.md "Learn how to create and manage Dynatrace Extensions.")
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

* [User events](../../../observe/digital-experience/rum-concepts/user-and-error-events.md "Learn about user and error events and the types of user and error events captured by Dynatrace.")
* [User sessions](../../../observe/digital-experience/rum-concepts/user-session.md "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.")
* How to capture user events and sessions on [Android](../../../observe/digital-experience/new-rum-experience/mobile-frontends/android/id-09-user-and-session.md "Identify users across sessions and devices, manage session lifecycle, and attach properties that apply to all events in a session."), [iOS](../../../observe/digital-experience/new-rum-experience/mobile-frontends/ios/id-09-user-and-session.md "Identify users, manage sessions, and report session properties in your iOS application."), [Flutter](../../../observe/digital-experience/new-rum-experience/mobile-frontends/flutter/id-09-user-and-session.md "Learn how to identify users, manage sessions, and report session properties in your Flutter application.") or [React Native](../../../observe/digital-experience/new-rum-experience/mobile-frontends/react-native/id-09-user-and-session.md "Learn how to identify users, manage sessions, and report session properties in your React Native application.")
* [Digital Experience Monitoring (DEM) overview (DPS)](../../../license/capabilities/digital-experience-monitoring.md "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| RUM Agent | `rumagent` | Built-in |

## Related topics

* [Data flow in OpenPipeline](../concepts/data-flow.md "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [How to ingest data (events)](../getting-started/how-to-ingestion.md "How to ingest data for a configuration scope in OpenPipeline.")