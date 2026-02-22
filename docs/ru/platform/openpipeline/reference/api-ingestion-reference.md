---
title: Ingest sources in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/api-ingestion-reference
scraped: 2026-02-22T21:19:35.967158
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

* [How to capture business events](/docs/observe/business-observability/bo-events-capturing "Capture business events for Dynatrace Business Observability.")
* [OpenPipeline Data extraction stage](/docs/platform/openpipeline/concepts/processing#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* [DDUs for business events](/docs/license/monitoring-consumption-classic/davis-data-units/ddus-for-business-events "Understand how the volume of DDU consumption is calculated for business events.")

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
| Authentication | [OAuth](/docs/observe/business-observability/bo-api-ingest#oauth "Set up authentication for and ingest business events via API.") [Access token](/docs/observe/business-observability/bo-api-ingest#access-token "Set up authentication for and ingest business events via API.") with **Ingest bizevents** (`bizevents.ingest`) token scope |
| Payload | `application/json` `application/cloudevent+json` `application/cloudevent-batch+json` |

To learn more, see [Ingest business events via API](/docs/observe/business-observability/bo-api-ingest "Set up authentication for and ingest business events via API.").

Logs

### Prior knowledge

* [How to ingest logs](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.")
* [Stream logs via Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* [DDUs for Log Management and Analytics](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.") or [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")

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
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Ingest logs** (`logs.ingest`) scope |
| Payload | `text/plain` `application/json` |

To learn more, see [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

#### OpenTelemetry

Pushes custom logs to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest logs** (`logs.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

Events (generic events)

### Prior knowledge

* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events** (`openpipeline.events`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Built-in generic events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-builtin "Ingest generic events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom API

Configures custom endpoints to ingest generic events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events (Custom)** (`openpipeline.events.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom generic event endpoint](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-custom-endpoint "Configure a custom generic event endpoint via OpenPipeline Ingest API.").

Events-Davis events

### Prior knowledge

* [Davis events](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI.")
* [OpenPipeline Data extraction stage](/docs/platform/openpipeline/concepts/processing#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest Events** (`events.ingest`) token scope |
| Payload | `application/json` |

To learn more, see [Events API v2 - POST an event](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.").

Events-Davis problems

### Prior knowledge

* [Davis problems](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI.")
* [Classic root cause analysis](/docs/dynatrace-intelligence/root-cause-analysis/concepts#root-cause-analysis "Get acquainted with root cause analysis concepts.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Classic Root Cause Analysis | *(none)* | Built-in |

Events-SDLC events

### Prior knowledge

* [How to ingest SDLC events](/docs/deliver/pipeline-observability-sdlc-events/sdlc-events "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events, Security Development Lifecycle** (`openpipeline.sdlc`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Built-in SDLC events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-builtin "Ingest SDLC events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom endpoint for Software Development Lifecycle events

Configures custom endpoints to ingest SDLC events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.sdlc` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events, Security Development Lifecycle (Custom)** (`openpipeline.sdlc.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom SDLC event endpoint](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-custom-endpoint "Configure a custom SDLC event endpoint via OpenPipeline Ingest API.").

Events-Security events

Migrate by December 2025

The endpoints `events.security` are planned to be deprecated. Migrate your configurations to `security.events` endpoints by **end of December 2025**. The previous endpoints will remain available **until the migration is complete**.

For a full overview of what's changing and step-by-step guidance on how to migrate, follow the instructions in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

### Prior knowledge

* [How to ingest security events](/docs/secure/threat-observability/security-events-ingest#ingest "Ingest external security data into Grail.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Built-in security events (legacy)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom security events API (legacy)

Configures custom endpoints to ingest security events. For details, see [Ingest custom security events via API](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data "Ingest security events from custom third-party products via API.").

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.security` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom security event endpoint (legacy)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API.").

Metrics

### Prior knowledge

* [How to ingest metrics](/docs/analyze-explore-automate/metrics "Metrics powered by Grail offer a comprehensive solution to manage your metrics data, in integration with logs, spans, and events, providing a unified approach to data analysis.")
* [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest metrics** (`metrics.ingest`) token scope |
| Payload | `text/plain` |

To learn more, see [Metrics API - POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.").

#### OpenTelemetry

Ingests OpenTelemetry metrics into Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest metrics** (`metrics.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see [OpenTelemetry metrics ingest API](/docs/dynatrace-api/environment-api/opentelemetry/post-metrics "Send OpenTelemetry metrics to Dynatrace via API.").

Security events (new)

### Prior knowledge

* [How to ingest security events](/docs/secure/threat-observability/security-events-ingest#ingest "Ingest external security data into Grail.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

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
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Built-in security events (new)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom security events API (new)

Configures custom endpoints to ingest security events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/security.events` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom security event endpoint (new)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API.").

Spans

### Prior knowledge

* [How to ingest traces](/docs/observe/application-observability/distributed-tracing/ingest-traces "Instrument your applications with OneAgent or OpenTelemetry to start ingesting trace data into Dynatrace.")
* [Traces powered by Grail overview (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.")

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
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see [OpenTelemetry trace ingest API](/docs/dynatrace-api/environment-api/opentelemetry/post-traces "Send OpenTelemetry traces to Dynatrace via API..").

System events

### Prior knowledge

* [System event models](/docs/semantic-dictionary/model/dt-system-events "Get to know the Semantic Dictionary models related to system events.")
* [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
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

* [User events](/docs/observe/digital-experience/rum-concepts/user-and-error-events "Learn about user and error events and the types of user and error events captured by Dynatrace.")
* [User sessions](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.")
* How to capture user events and sessions on [Android](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/android/id-09-user-and-session "Identify users across sessions and devices, manage session lifecycle, and attach properties that apply to all events in a session."), [iOS](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/ios/id-09-user-and-session "Identify users, manage sessions, and report session properties in your iOS application."), [Flutter](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/flutter/id-09-user-and-session "Learn how to identify users, manage sessions, and report session properties in your Flutter application.") or [React Native](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/react-native/id-09-user-and-session "Learn how to identify users, manage sessions, and report session properties in your React Native application.")
* [Digital Experience Monitoring (DEM) overview (DPS)](/docs/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| RUM Agent | `rumagent` | Built-in |

## Related topics

* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [How to ingest data (events)](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline.")