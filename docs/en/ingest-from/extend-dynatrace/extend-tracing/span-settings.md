---
title: Span settings
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings
scraped: 2026-02-18T05:32:01.534768
---

# Span settings

# Span settings

* Latest Dynatrace
* 4-min read
* Updated on Dec 20, 2023

OneAgent version 1.215+ Dynatrace version 1.216+

Dynatrace automatically captures all OpenTracing and OpenTelemetry spans, but you can control and adapt how OpenTelemetry and OpenTracing spans are combined with OneAgent data into PurePathÂ® distributed traces.

The span settings are available at **Settings** > **Server-side service monitoring**. You can define rules to:

* Store and mask only specific attributesâ**Attribute capturing**
* Exclude specific spansâ**Span capturing**
* Define spans that should be considered as entry pointsâ**Span entry points**
* Enable context propagation for certain spansâ**Span context propagation**

For details, see the sections that follow.

## Attributes

The OneAgent code module's OpenTelemetry Span Sensor automatically captures all OpenTelemetry attributes.
If you want to prevent the accidental storage of personal data, you can exclude specific attribute keys for which the values must not be persisted.
By omitting attributes containing personal data, you can meet your organization's privacy requirements and control the scope of stored monitoring data.

To configure attribute storage and masking settings for your environment

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Select **Server-side service monitoring** > **Attribute capturing**.
3. optional To change the default OpenTelemetry attribute persistence, go to **Preferences**.

   * To store all attributes except the ones in the **Blocked attributes** list, select **Allow all attributes**
   * To block all attributes except the ones in the **Allowed attributes** list, select **Block all attributes**

   Only one setting preference is possible.
4. Add an attribute name to the attribute list.

   1. On the **Attribute capturing** page, select **Blocked attributes** or **Allowed attributes**.

      Allowed attributes list Dynatrace recommends a few basic attributes to generally be included, such as `service.name` or `service.version`. For ease of use, Dynatrace comes with a default configuration that can be adjusted.
   2. Select **Add item** to add a new key to the attribute list and enter the key.
   3. Select **Save changes**.
5. Perform the following actions to mask a stored attribute value.

   1. On the **Attribute capturing** page, select **Attribute data masking**.
   2. Select **Add item** to add a new key to the masked attributed list.
   3. Enter a stored value key and select an option from the **Masking** dropdown list. To learn more about masking options, see [OpenTelemetry traces](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#otel-traces "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.").
   4. Select **Save changes**.

You can then find the attribute key on the **Distributed traces** page on the [**Summary** tab](/docs/observe/application-observability/distributed-traces/use-cases/segment-request#summary-tab "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").

## Span capture

All detected OpenTelemetry and OpenTracing spans are captured by default. This means that every detected span is added to distributed traces. This gives code-level visibility along with span attributes, even for technologies not supported by OneAgent out of the box.

You can create [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") based on spans to segment the distributed traces.

We recommend that you exclude spans for technologies supported out of the box by OneAgent for [Java](/docs/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") and [Go](/docs/ingest-from/technology-support#go "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

To control your span capturing

1. Go to **Settings** > **Server-side service monitoring** > **Span capturing**.
2. Select **Add item**.
3. Enter a **Rule name**.
4. In the **Rule action** list, decide whether you want to **Ignore** or **Capture** spans matching the criteria you're about to define.
5. Select **Add item**.
6. You can control span capturing based on the value of the following sources:

   * **Attribute**
   * **Instrumentation scope name**, `OpenTelemetry`
   * **Instrumentation scope version**
   * **Span kind**âfor example, `server`
   * **Span name**
7. Select the **Comparison type**âfor example, **Contains** or **Equals**.
8. Enter the value for the source you specified earlier.
9. By default, the search for key and value is not case sensitive. Turn on **Case sensitive** if you want your rule to consider key and value case.
10. Select **Save changes**.

## Span entry points

By default:

* OpenTelemetry/OpenTracing span kinds `server` and `consumer` start new distributed traces automatically. This means that all OneAgent sensors contribute to that distributed trace and a default service is created for the distributed trace.
* OpenTelemetry/OpenTracing span kinds `client`, `internal`, and `producer` don't start new distributed trace automatically.

You can choose to start distributed traces based on `client`, `internal`, and `producer` span kinds, and to opt out for `server` and `consumer` span kinds, based on various span details.

To control your span entry points

1. Go **Settings** > **Server-side service monitoring** > **Span entry points**
2. Select **Add item**.
3. Enter a **Rule name**.
4. In the **Rule action** list, specify **Create entry point** or **Do not create entry point** for spans matching the criteria you're about to define.
5. Select **Add item**.
6. You can control span entry points based on the value of the following sources:

   * **Attribute**
   * **Instrumentation scope name**, `OpenTelemetry`
   * **Instrumentation scope version**
   * **Span kind**âfor example, `server`
   * **Span name**
7. Select the **Comparison type**âfor example, **Contains** or **Equals**.
8. Enter the value for the source you specified earlier.
9. By default, the search for key and value is not case sensitive. Turn on **Case sensitive** if you want your rule to consider key and value case.
10. Select **Save changes**.

## Span context propagation

Context propagation enables you to connect distributed traces through OpenTelemetry/OpenTracing. You can connect distributed traces through any protocol and propagate the inject and extract usage to the Dynatrace PurePathÂ® distributed traces context.

To reduce the risk of context propagation conflicts with built-in sensors, context propagation is disabled by default and is limited to spans matching the criteria of your choice.

To define rules to enable context propagation for specific spans

1. Go **Settings** > **Server-side service monitoring** > **Span context propagation**
2. Select **Add item**.
3. Enter a **Rule name**.
4. In the **Rule action** list, specify **Propagate** or **Do not propagate** span context for spans matching the criteria you're about to define.
5. Select **Add item**.
6. You can control span context propagation based on the value of the following sources

   * **Attribute**
   * **Instrumentation scope name**, `OpenTelemetry`
   * **Instrumentation scope version**
   * **Span kind**âfor example, `server`
   * **Span name**
7. Select the **Comparison type**âfor example, **Contains** or **Equals**.
8. Add the value for the source you specified earlier.
9. By default, the search for key and value is not case sensitive. Turn on **Case sensitive** if you want your rule to consider key and value case.
10. Select **Save changes**.