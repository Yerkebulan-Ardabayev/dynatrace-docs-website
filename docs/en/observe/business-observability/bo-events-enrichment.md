---
title: Business event enrichment
source: https://www.dynatrace.com/docs/observe/business-observability/bo-events-enrichment
scraped: 2026-02-26T21:21:40.004611
---

# Business event enrichment

# Business event enrichment

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Mar 19, 2024

Dynatrace SaaS version 1.253+

Dynatrace automatically enriches business events with additional context to enhance analysis and facilitate drill-down navigation. Specifically, Dynatrace adds certain properties to your business events, for example, information on geolocation, operating system, application, and more. You can then use [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") to analyze your business events.

## OneAgent and external business event enrichment

Fields defined in the table below can be used to enrich business events. Some fields are automatically added depending on their source (OneAgent or API).

1

Not an enriched field per se, but required by the Dynatrace internal schema

2

If no original timestamp is available, it's populated at ingest time.

3

Set by OneAgent and required by CloudEvents specification, but not enforced by the Dynatrace internal schema

## RUM business event enrichment

Business events [reported via RUM](/docs/observe/business-observability/bo-events-capturing#report-business-event-rum "Capture business events for Dynatrace Business Observability.") are enriched with fields relevant to the device and user, such as geolocation, device, browser, and application. The following fields are added automatically, depending on the application typeâweb or mobile.

### Top-level fields

The top-level fields contain generally relevant information for all events and data points.

1

If no original timestamp is available, it's populated at ingest time.

2

Unix timestamp in nanoseconds

### Event fields

The `event` namespace contains common identification, categorization, and context on events in Dynatrace.

1

Not enriched automatically; you set it via API when you report a business event.

2

Full domain name for web, app bundle for mobile, and application ID for OpenKit

### Dynatrace RUM fields

The `dt.rum` namespace contains Dynatrace RUM-specific fields.

1

Also known as the internal user ID or visitor ID

2

If available

### Device fields

The `device` namespace contains information on the device running an application.

### OS fields

The `os` namespace contains information on the operating system running an application.

### Browser fields

The `browser` namespace contains information on the browser running an application.

1

Possible values: `desktop`, `mobile`, `tablet`, `robot`, `other`

### Client fields

The `client` namespace contains information on the initiator of a network connection.

### Application fields

The `app` namespace contains information on the application sending the business event.

### Geolocation fields

The `geo` namespace contains geolocation information.